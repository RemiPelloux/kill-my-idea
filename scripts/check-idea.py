#!/usr/bin/env python3
"""Check one kill-my-idea folder (or every folder under ideas/) against the rules in SKILL.md.

    python3 scripts/check-idea.py ideas/2026-11-my-idea
    python3 scripts/check-idea.py --all [ideas]    # every ideas/*/ folder with a verdict.json
    python3 scripts/check-idea.py --board [ideas]  # ideas/board-data.js, written by build-brain.py
    python3 scripts/check-idea.py --legacy examples/x-report  # an old report: rule errors become warnings

No dependencies. Exit code 1 when any ERROR is found. It recomputes the score from the 21
sub-scores, applies the fixed rules R1-R5, and checks sources, counts, kill-shot coherence,
the premortem / why-now / ICP sections and the shape of report-data.js (one strict data
literal: no functions, comments or template literals). WARN lines are advice; ERROR lines
must be fixed.
"""
import datetime
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

WEIGHTS = {"profit": 25, "feasibility": 20, "time_to_first_revenue": 15, "demand": 15,
           "competition": 10, "risk": 10, "fit": 5}
SUBS = {"profit": ["gross_margin", "ltv_cac", "pricing_power"],
        "feasibility": ["build_effort", "skills_match", "capital_needed"],
        "time_to_first_revenue": ["time_to_mvp", "sales_cycle", "channel_readiness"],
        "demand": ["search_demand", "trend", "willingness_to_pay"],
        "competition": ["free_alternatives", "competitor_density", "differentiation"],
        "risk": ["legal_regulatory", "platform_dependency", "market_risk"],
        "fit": ["skills", "assets", "interest"]}
KILL_SHOTS = ["free_alternative", "strong_competitor", "graveyard", "no_distribution",
              "costs_eat_margin", "weak_demand", "legal_platform_risk", "saturated_wave"]
# R5: a kill shot hit must show in the sub-scores -> (criterion, sub, max score)
COHERENCE = {"free_alternative": [("competition", "free_alternatives", 2)],
             "no_distribution": [("time_to_first_revenue", "channel_readiness", 2)],
             "costs_eat_margin": [("profit", "gross_margin", 2)],
             "weak_demand": [("demand", "trend", 2.5)],
             "saturated_wave": [("competition", "competitor_density", 2)],
             "strong_competitor": [("competition", "competitor_density", 3)]}
MIN_SOURCES = {"kill": (20, 10), "deepdive": (40, 15), "roast": (10, 6), "check-tweet": (20, 10)}
TYPES = {"saas": ["churn_benchmark", "switching_cost"], "marketplace": ["liquidity", "disintermediation"],
         "mobile_app": ["store_search_demand", "platform_fees"], "ecommerce": ["contribution_margin", "returns_shipping"],
         "content": ["rpm", "platform_policy"], "service": ["founder_time_ceiling", "client_concentration"],
         "local": ["location_traffic", "permits_capex"]}
SCHEMA_VERSION = "1.0"  # the file format; 1.x readers accept every 1.x file
DIFF_ORDER = {"doable": 0, "hard": 1, "very-hard": 2}
URL_RX = re.compile(r"^https?://", re.I)
DATE_RX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TEMPLATE = pathlib.Path(__file__).resolve().parent.parent / "skills" / "kill" / "report.html"


def round_half_up(x):
    return int(x + 0.5) if x >= 0 else -int(-x + 0.5)


def band(score):
    return "GO" if score >= 70 else "PIVOT" if score >= 50 else "NO-GO"


def domain(url):
    try:
        host = urlsplit(url).hostname or ""
    except ValueError:
        return ""
    return host[4:] if host.startswith("www.") else host


class Report:
    def __init__(self, folder):
        self.folder = folder
        self.errors, self.warnings = [], []
        self.lenient = False  # --legacy: rules added after a report was written only warn

    def error(self, msg):
        if self.lenient:
            self.warnings.append(f"legacy: {msg}")
        else:
            self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def legacy(self, what, since="0.7"):
        self.warn(f"legacy (pre-{since}) verdict: missing {what}. Fine for an old report; a new run must write it.")


def load_json(rep, path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.error(f"{path.name}: invalid JSON ({e})")
        return None


def check_url(rep, where, url, required=False):
    if url is None or url == "":
        if required:
            rep.error(f"{where}: missing source URL")
        return
    if not isinstance(url, str) or not URL_RX.match(url):
        rep.error(f"{where}: not an http(s) URL: {str(url)[:80]!r}")


def check_type_and_answers(rep, idea, v):
    """1.0: idea.type picks 2 type checks; answers record the questions asked and what they fed."""
    if not isinstance(idea, dict):
        return
    t = idea.get("type")
    if t is None:
        rep.legacy("idea.type (and verdict.type_checks)", since="1.0")
    elif t not in TYPES:
        rep.error(f"idea.json: type {t!r} must be one of {', '.join(TYPES)}")
    else:
        tc = v.get("type_checks")
        if not isinstance(tc, list):
            rep.error(f"verdict.json: type_checks is required for a {t} idea: {', '.join(TYPES[t])}")
        else:
            got = [c.get("check") for c in tc if isinstance(c, dict)]
            if sorted(got) != sorted(TYPES[t]):
                rep.error(f"verdict.json: type_checks are {got}; a {t} idea needs exactly {TYPES[t]}")
            for c in tc:
                if not isinstance(c, dict):
                    continue
                if c.get("result") not in ("hit", "clear", "unknown"):
                    rep.error(f"verdict.json: type check {c.get('check')} result {c.get('result')!r} must be hit, clear or unknown")
                if not c.get("note"):
                    rep.error(f"verdict.json: type check {c.get('check')} needs a note")
                if c.get("result") == "hit":
                    check_url(rep, f"verdict.json type check {c.get('check')}.source", c.get("source"), required=True)
    ans = idea.get("answers")
    if ans is None:
        return
    if not isinstance(ans, list) or len(ans) > 10:
        rep.error("idea.json: answers must be a list of at most 10")
        return
    keys = {s for subs in SUBS.values() for s in subs} | set(KILL_SHOTS) | {c for cs in TYPES.values() for c in cs} | {"country", "confidence", "rescue"}
    stages = {"intake": 0, "follow_up": 0}
    for i, a in enumerate(ans):
        w = f"idea.json answers[{i}]"
        if not isinstance(a, dict) or not a.get("question"):
            rep.error(f"{w}: needs a question")
            continue
        st = a.get("stage")
        if st not in stages:
            rep.error(f"{w}: stage {st!r} must be intake or follow_up")
            continue
        stages[st] += 1
        feeds = a.get("feeds")
        if not isinstance(feeds, list) or not feeds:
            rep.error(f"{w}: feeds must list the sub-scores or kill shots the answer changes")
        else:
            bad = [f for f in feeds if f not in keys]
            if bad:
                rep.error(f"{w}: unknown feeds {bad}; use sub-score, kill-shot or type-check keys")
        if st == "follow_up" and not a.get("effect"):
            rep.error(f"{w}: a follow-up needs an effect (what the answer changed, or 'no change')")
    if stages["intake"] > 8:
        rep.error(f"idea.json: {stages['intake']} intake questions; ask at most 8")
    if stages["follow_up"] > 2:
        rep.error(f"idea.json: {stages['follow_up']} follow-up questions; ask at most 2")


def check_run(rep, v):
    """1.0: what the run cost, shown in the report footer."""
    r = v.get("run")
    if r is None:
        return
    if not isinstance(r, dict):
        rep.error("verdict.json: run must be an object")
        return
    for k in ("minutes", "searches", "fetches"):
        x = r.get(k)
        if x is not None and (not isinstance(x, (int, float)) or isinstance(x, bool) or x < 0 or x > 10000):
            rep.error(f"verdict.json: run.{k} {x!r} must be a non-negative number")


def check_version(rep, where, obj):
    """Every file written since 1.0 says which format wrote it."""
    if not isinstance(obj, dict):
        return
    ver = obj.get("schema_version")
    if ver is None:
        rep.legacy(f"{where} schema_version (run scripts/migrate.py)", since="1.0")
    elif not isinstance(ver, str) or not re.match(r"^1\.\d+$", ver):
        rep.error(f"{where}: schema_version {ver!r} is not a 1.x format; this checker reads 1.x files")


def check_idea(rep, idea):
    if idea is None:
        rep.error("idea.json: missing")
        return
    for k in ("slug", "title", "source", "countries", "unknowns"):
        if k not in idea:
            rep.error(f"idea.json: missing required field {k!r}")
    slug = idea.get("slug", "")
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(slug)):
        rep.error(f"idea.json: slug {slug!r} is not kebab-case ASCII")
    for c in idea.get("countries") or []:
        if not re.match(r"^[A-Z]{2}$", str(c)):
            rep.error(f"idea.json: country {c!r} is not an ISO 3166-1 alpha-2 code (e.g. FR)")
    if not idea.get("countries"):
        rep.warn("idea.json: no country. The verdict depends on it; ask or assume one and record the assumption.")
    lang = idea.get("language")
    if lang is None:
        rep.legacy("idea.language")
    elif not re.match(r"^[a-z]{2}$", str(lang)):
        rep.error(f"idea.json: language {lang!r} must be an ISO 639-1 code (en, fr)")
    src = idea.get("source") or {}
    if not isinstance(src, dict) or not src.get("text"):
        rep.error("idea.json: source.text (the verbatim input) is required")
    check_url(rep, "idea.json source.url", src.get("url") if isinstance(src, dict) else None)
    if "created" in idea and not DATE_RX.match(str(idea["created"])):
        rep.error(f"idea.json: created {idea['created']!r} is not YYYY-MM-DD")
    unknowns = set(idea.get("unknowns") or [])
    for f in ("problem", "customer", "solution", "revenue_model", "price", "channel"):
        if f in idea and idea[f] is None and f not in unknowns:
            rep.warn(f"idea.json: {f} is null but not listed in unknowns")
    price = idea.get("price")
    if isinstance(price, dict):
        if not isinstance(price.get("amount"), (int, float)):
            rep.error("idea.json: price.amount must be a number")
        if not re.match(r"^[A-Z]{3}$", str(price.get("currency", ""))):
            rep.error(f"idea.json: price.currency {price.get('currency')!r} must be ISO 4217 (EUR, USD)")


def check_scores(rep, v):
    """Recompute the score from the 21 sub-scores and apply the fixed rules."""
    cd = v.get("criteria_detail")
    crit = v.get("criteria") or {}
    if not isinstance(cd, dict):
        rep.error("verdict.json: criteria_detail (the 21 sub-scores) is required")
        return None
    means, sourced = {}, 0
    for c, subs in SUBS.items():
        block = cd.get(c)
        if not isinstance(block, dict):
            rep.error(f"verdict.json: criteria_detail.{c} is missing")
            continue
        extra = set(block) - set(subs)
        if extra:
            rep.error(f"verdict.json: criteria_detail.{c} has unknown sub-scores {sorted(extra)}; expected {subs}")
        vals = []
        for s in subs:
            sub = block.get(s)
            if not isinstance(sub, dict) or "score" not in sub:
                rep.error(f"verdict.json: criteria_detail.{c}.{s} is missing or has no score")
                continue
            sc = sub["score"]
            if not isinstance(sc, (int, float)) or not 1 <= sc <= 5 or (sc * 2) != int(sc * 2):
                rep.error(f"verdict.json: {c}.{s} score {sc!r} must be 1-5 in half points")
                continue
            vals.append(sc)
            note = sub.get("note")
            if not note or not isinstance(note, str):
                rep.error(f"verdict.json: {c}.{s} needs a one-line note")
            elif len(note) > 160:
                rep.error(f"verdict.json: {c}.{s} note is {len(note)} chars; max 160")
            elif len(note) < 10:
                rep.warn(f"verdict.json: {c}.{s} note is very short: {note!r}")
            if sub.get("source"):
                check_url(rep, f"verdict.json {c}.{s}.source", sub["source"])
                sourced += 1
        if len(vals) != 3:
            continue
        mean = sum(vals) / 3
        means[c] = mean
        disp = round(mean * 2) / 2
        if c not in crit:
            rep.error(f"verdict.json: criteria.{c} is missing")
        elif abs(float(crit[c]) - disp) > 1e-9:
            rep.error(f"verdict.json: criteria.{c} = {crit[c]} but the mean of its sub-scores is {mean:.2f}, which displays as {disp}")
    if len(means) != 7:
        return None
    raw = sum(WEIGHTS[c] * means[c] / 5 for c in WEIGHTS)
    raw1 = round(raw + 1e-9, 1)
    expected = round_half_up(raw)
    rules = v.get("rules_applied")
    if rules is None:
        rep.legacy("rules_applied")
        rules = []
    elif not isinstance(rules, list):
        rep.error("verdict.json: rules_applied must be a list")
        rules = []
    rule_ids = {r.get("rule") if isinstance(r, dict) else r for r in rules}
    ks = v.get("kill_shots") or {}
    capped = "R2_no_channel" in rule_ids or ks.get("no_distribution") is True
    if ks.get("no_distribution") is True and "R2_no_channel" not in rule_ids and expected > 69:
        if v.get("rules_applied") is not None:
            rep.error("verdict.json: kill_shots.no_distribution is true and the raw total is above 69, so rules_applied must contain R2_no_channel")
    r7 = means.get("profit", 5) <= 2 + 1e-9
    if r7:
        # R7: a model that doesn't make money loses 10 points and is never better than NO-GO
        if "R7_unprofitable_model" not in rule_ids and v.get("rules_applied") is not None:
            rep.error(f"verdict.json: Profit potential is {means['profit']:.2f} (2 or less): rules_applied must contain R7_unprofitable_model (-10 points, at most 49)")
        expected = min(expected - 10, 49)
    if capped:
        expected = min(expected, 69)
    if v.get("quick") is True:
        expected = min(expected, 69)  # a quick run is never a GO
    lc = ((v.get("metrics") or {}).get("ltv_cac") or {}).get("value")
    r6 = ks.get("no_distribution") is True and isinstance(lc, (int, float)) and not isinstance(lc, bool) and lc < 1
    if r6:
        if "R6_unprofitable_no_channel" not in rule_ids and expected > 49 and v.get("rules_applied") is not None:
            rep.error(f"verdict.json: no channel and LTV:CAC {lc} (below 1): rules_applied must contain R6_unprofitable_no_channel and the score is capped at 49")
        expected = min(expected, 49)
    if "score_raw" in v:
        if not isinstance(v["score_raw"], (int, float)) or abs(float(v["score_raw"]) - raw1) > 0.051:
            rep.error(f"verdict.json: score_raw = {v.get('score_raw')} but sum(weight x mean) / 5 = {raw1}")
    else:
        rep.legacy("score_raw")
    score = v.get("score")
    if not isinstance(score, int):
        rep.error(f"verdict.json: score {score!r} must be an integer")
    elif score != expected:
        how = f"raw {raw1} rounds half up to {round_half_up(raw)}" + (", minus 10 and at most 49 (R7: unprofitable model)" if r7 else "") + (", capped at 49 (R6: loses money, no channel)" if r6 else ", capped at 69 (R2: no channel)" if capped else "")
        rep.error(f"verdict.json: score is {score} but recomputes to {expected} ({how})")
    verdict = v.get("verdict")
    if isinstance(score, int) and verdict != band(score):
        rep.error(f"verdict.json: verdict {verdict!r} does not match score {score} (band: {band(score)})")
    # R1 / R3 / R4 effects
    if rule_ids & {"R1_free_equivalent", "R3_saturated_wave"} and means.get("competition", 0) > 1.5 + 1e-9:
        rep.error("verdict.json: R1/R3 applied but Competitive room mean is above 1.5; lower the sub-scores to match")
    if "R3_saturated_wave" in rule_ids and cd["competition"]["differentiation"]["score"] > 1.5:
        rep.error("verdict.json: R3 applied but differentiation is above 1.5")
    if "R1_free_equivalent" in rule_ids and cd["competition"]["free_alternatives"]["score"] > 1.5:
        rep.error("verdict.json: R1 applied but free_alternatives is above 1.5")
    if "R4_ltv_cac_below_1" in rule_ids and means.get("profit", 0) > 2 + 1e-9:
        rep.error("verdict.json: R4 applied but Profit potential mean is above 2")
    if isinstance(lc, (int, float)) and not isinstance(lc, bool) and lc < 0:
        rep.error(f"verdict.json: LTV:CAC is {lc}; a ratio of two costs can't be negative (a loss per customer means LTV is 0 or the margin is negative: write 0)")
    if isinstance(lc, (int, float)) and lc < 1 and "R4_ltv_cac_below_1" not in rule_ids and means.get("profit", 0) > 2:
        rep.warn(f"verdict.json: LTV:CAC is {lc} (below 1) and Profit potential is {means['profit']:.2f}: apply R4, or state the path that fixes it in the ltv_cac note")
    # R5 coherence
    for shot, reqs in COHERENCE.items():
        if ks.get(shot) is True:
            for c, s, mx in reqs:
                sc = cd[c][s]["score"]
                if sc > mx:
                    rep.error(f"verdict.json: kill shot {shot} hit but {c}.{s} = {sc} (R5: must be <= {mx})")
    if ks.get("legal_platform_risk") is True:
        lo = min(cd["risk"]["legal_regulatory"]["score"], cd["risk"]["platform_dependency"]["score"])
        if lo > 2.5:
            rep.error(f"verdict.json: kill shot legal_platform_risk hit but min(legal_regulatory, platform_dependency) = {lo} (R5: must be <= 2.5)")
    return {"raw": raw1, "sourced": sourced, "means": means}


def check_metrics(rep, v):
    m = v.get("metrics")
    if not isinstance(m, dict):
        rep.error("verdict.json: metrics object is required")
        return
    for k, met in m.items():
        if not isinstance(met, dict):
            rep.error(f"verdict.json: metrics.{k} must be an object with value and basis")
            continue
        basis = met.get("basis")
        if basis not in ("sourced", "estimate", "unknown"):
            rep.error(f"verdict.json: metrics.{k}.basis {basis!r} must be sourced, estimate or unknown")
        if basis == "sourced":
            check_url(rep, f"verdict.json metrics.{k}.source", met.get("source"), required=True)
        elif basis == "estimate":
            r = met.get("reasoning")
            if not r or not isinstance(r, str) or len(r) < 10:
                rep.error(f"verdict.json: metrics.{k} is an estimate without its formula (reasoning)")
        val = met.get("value")
        if basis == "unknown" and val not in (None, "unknown"):
            rep.warn(f"verdict.json: metrics.{k} has basis unknown but a value {val!r}")
        if basis != "unknown" and val in (None, "unknown"):
            rep.error(f"verdict.json: metrics.{k} has basis {basis} but no value")
    for k in ("ltv_cac", "break_even_customers_per_month", "time_to_first_revenue_weeks", "competitors_found", "cac", "ltv", "gross_margin_pct"):
        if k not in m:
            rep.warn(f"verdict.json: metrics.{k} is missing (write it as unknown if not found)")
    # derived values must follow from their inputs when all are numbers
    num = lambda k: m.get(k, {}).get("value") if isinstance(m.get(k, {}).get("value"), (int, float)) else None
    ltv, cac, lc = num("ltv"), num("cac"), num("ltv_cac")
    if ltv is not None and cac and lc is not None and abs(ltv / cac - lc) > max(0.15, 0.1 * abs(lc)):
        rep.error(f"verdict.json: ltv_cac = {lc} but ltv / cac = {ltv / cac:.2f}")
    price, vc, gm = num("price"), num("variable_cost_per_unit"), num("gross_margin_pct")
    if price and vc is not None and gm is not None and abs((price - vc) / price * 100 - gm) > 5:
        rep.error(f"verdict.json: gross_margin_pct = {gm} but (price - variable cost) / price = {(price - vc) / price * 100:.0f}%")


def check_kill_shots(rep, v):
    ks = v.get("kill_shots")
    if not isinstance(ks, dict):
        rep.error("verdict.json: kill_shots object is required")
        return
    for k in KILL_SHOTS:
        if k not in ks:
            (rep.legacy if k == "saturated_wave" else rep.error)(f"kill_shots.{k} (true = hit, false = clear, null = not checked)")
        elif ks[k] not in (True, False, None):
            rep.error(f"verdict.json: kill_shots.{k} must be true, false or null")
    extra = set(ks) - set(KILL_SHOTS)
    if extra:
        rep.error(f"verdict.json: unknown kill shots {sorted(extra)}")
    unchecked = [k for k in KILL_SHOTS if ks.get(k, False) is None]
    if unchecked:
        rep.warn(f"verdict.json: kill shots not checked: {', '.join(unchecked)}")
    pk = v.get("primary_kill_shot", "absent")
    if pk == "absent":
        rep.legacy("primary_kill_shot")
    elif pk is not None and pk not in KILL_SHOTS:
        rep.error(f"verdict.json: primary_kill_shot {pk!r} is not a kill shot key")
    elif pk is not None and ks.get(pk) is not True:
        rep.error(f"verdict.json: primary_kill_shot {pk} is not marked as a hit")
    elif pk is None and any(ks.get(k) is True for k in KILL_SHOTS) and v.get("verdict") != "GO":
        rep.error("verdict.json: kill shots hit but primary_kill_shot is null")


def _pub_key(p):
    """'2025', '2025-03' or '2025-03-14' -> the last day it can stand for, as YYYY-MM-DD, or None."""
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$", str(p or "").strip())
    if not m:
        return None
    y, mo, d = m.group(1), m.group(2), m.group(3)
    return f"{y}-{mo or '01'}-{d or '01'}"


def check_as_of(rep, v, narrative):
    """Hindsight guard: with as_of set, no source may be published after it."""
    as_of = v.get("as_of")
    if as_of is None:
        return
    if not DATE_RX.match(str(as_of)):
        rep.error(f"verdict.json: as_of {as_of!r} is not YYYY-MM-DD")
        return
    srcs = (narrative or {}).get("sources") or []
    later, undated = [], 0
    for s in srcs:
        if not isinstance(s, dict):
            continue
        k = _pub_key(s.get("published"))
        if k is None:
            undated += 1
        elif k > as_of:
            later.append(f"{s.get('published')} {str(s.get('url'))[:60]}")
    if later:
        rep.error(f"verdict.json: as_of {as_of} but {len(later)} source(s) were published after it (hindsight): {'; '.join(later[:3])}")
    if srcs and undated * 2 > len(srcs):
        rep.warn(f"verdict.json: as_of {as_of} but {undated} of {len(srcs)} sources have no published date, so hindsight can't be ruled out; add published dates")


def check_sources_and_confidence(rep, v, narrative, scores):
    mode = v.get("mode")
    if mode is None:
        rep.legacy("mode")
        mode = "kill"
    elif mode not in MIN_SOURCES:
        rep.error(f"verdict.json: mode {mode!r} must be one of {sorted(MIN_SOURCES)}")
        mode = "kill"
    srcs = v.get("sources")
    if not isinstance(srcs, list):
        rep.error("verdict.json: sources must be a list of URLs")
        srcs = []
    for s in srcs:
        check_url(rep, "verdict.json sources[]", s, required=True)
    urls = [s for s in srcs if isinstance(s, str) and URL_RX.match(s)]
    if len(set(urls)) != len(urls):
        rep.warn("verdict.json: sources contains duplicates")
    domains = {domain(u) for u in urls}
    min_n, min_d = MIN_SOURCES[mode]
    conf = v.get("confidence")
    level = conf.get("level") if isinstance(conf, dict) else None
    if v.get("quick") is True:
        # quick mode: 10 sources from 6 domains, always low confidence, never a GO
        min_n, min_d = 10, 6
        if level != "low":
            rep.error("verdict.json: a quick run's confidence must be low (quick mode, SKILL.md §3)")
    if len(set(urls)) < min_n or len(domains) < min_d:
        msg = f"{len(set(urls))} sources from {len(domains)} domains; a {mode} needs {min_n} from {min_d}"
        if level == "low":
            rep.warn(f"verdict.json: {msg} (confidence is low, as required)")
        else:
            rep.error(f"verdict.json: {msg}. Research more, or set confidence.level to low and say so in the report")
    primary = None
    if narrative and isinstance(narrative.get("sources"), list):
        tiers = [s.get("tier") for s in narrative["sources"] if isinstance(s, dict)]
        if any(t for t in tiers):
            primary = sum(1 for t in tiers if t == "primary")
    if conf is None:
        rep.legacy("confidence")
        return
    if not isinstance(conf, dict):
        rep.error("verdict.json: confidence must be an object")
        return
    for k in ("level", "sourced_subscores", "sources", "primary_sources"):
        if k not in conf:
            rep.error(f"verdict.json: confidence.{k} is required")
    if level not in ("high", "medium", "low"):
        rep.error(f"verdict.json: confidence.level {level!r} must be high, medium or low")
        return
    ss = conf.get("sourced_subscores")
    if scores and isinstance(ss, int) and ss != scores["sourced"]:
        rep.error(f"verdict.json: confidence.sourced_subscores = {ss} but {scores['sourced']} sub-scores carry a source")
    if isinstance(conf.get("sources"), int) and conf["sources"] != len(set(urls)):
        rep.error(f"verdict.json: confidence.sources = {conf['sources']} but sources lists {len(set(urls))} unique URLs")
    if primary is not None and isinstance(conf.get("primary_sources"), int) and conf["primary_sources"] != primary:
        rep.error(f"verdict.json: confidence.primary_sources = {conf['primary_sources']} but report-data.js has {primary} primary-tier sources")
    ss, ns, ps = (scores["sourced"] if scores else ss or 0), len(set(urls)), (primary if primary is not None else conf.get("primary_sources") or 0)
    want = "high" if (ss >= 14 and ns >= 25 and ps >= 5) else "medium" if (ss >= 8 and ns >= 15 and ps >= 2) else "low"
    if level != want:
        rep.error(f"verdict.json: confidence.level is {level} but {ss} sourced sub-scores, {ns} sources and {ps} primary sources give {want}")


def check_rescue_and_test(rep, v):
    rescue = v.get("rescue")
    if rescue is None:
        if v.get("verdict") != "GO":
            rep.warn("verdict.json: no rescue paths. Write 1-3, or state that none reaches 50.")
        rescue = []
    if not isinstance(rescue, list):
        rep.error("verdict.json: rescue must be a list")
        return
    if len(rescue) > 3:
        rep.error(f"verdict.json: {len(rescue)} rescue paths; at most 3")
    keys = []
    for i, r in enumerate(rescue):
        if not isinstance(r, dict):
            rep.error(f"verdict.json: rescue[{i}] must be an object")
            continue
        for k in ("change", "score_after", "difficulty"):
            if k not in r:
                rep.error(f"verdict.json: rescue[{i}].{k} is required")
        if "why" not in r:
            rep.warn(f"verdict.json: rescue[{i}].why (which kill shot it fixes) is missing")
        sa = r.get("score_after")
        if not isinstance(sa, int) or not 0 <= sa <= 100:
            rep.error(f"verdict.json: rescue[{i}].score_after {sa!r} must be an integer 0-100")
        if r.get("difficulty") not in DIFF_ORDER:
            rep.error(f"verdict.json: rescue[{i}].difficulty {r.get('difficulty')!r} must be doable, hard or very-hard")
        if isinstance(sa, int) and r.get("difficulty") in DIFF_ORDER:
            keys.append((-sa, DIFF_ORDER[r["difficulty"]]))
    if keys != sorted(keys):
        rep.error("verdict.json: rescue paths must be sorted by score_after descending, then doable before hard before very-hard")
    for i, k in enumerate(v.get("kill_criteria") or []):
        if not isinstance(k, str) or not re.search(r"\d", k):
            rep.error(f"verdict.json: kill_criteria[{i}] has no number: {str(k)[:80]!r}")
    if v.get("verdict") != "NO-GO" and not (v.get("kill_criteria") or []):
        rep.warn("verdict.json: a GO / PIVOT needs kill criteria with numbers (\"fewer than 10 sign-ups by day 7 -> stop\")")
    if v.get("verdict") != "NO-GO" and not v.get("cheapest_test"):
        rep.warn("verdict.json: a GO / PIVOT needs a cheapest_test")
    for h in v.get("history") or []:
        if not isinstance(h, dict) or not {"mode", "evaluated", "score", "verdict"} <= set(h):
            rep.error("verdict.json: each history entry needs mode, evaluated, score and verdict")


def code_outside_strings(text):
    """The text with every double-quoted JSON string replaced by "", so only code is left."""
    out, i, n = [], 0, len(text)
    while i < n:
        ch = text[i]
        if ch == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            out.append('""')
            i = j + 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


# Things a data file must never contain outside its strings: it is loaded with <script src>.
FORBIDDEN_CODE = [(re.compile(r"\bfunction\b"), "a function"),
                  (re.compile(r"=>"), "an arrow function"),
                  (re.compile(r"`"), "a template literal (backtick)"),
                  (re.compile(r"//|/\*"), "a comment"),
                  (re.compile(r"'"), "a single-quoted string"),
                  (re.compile(r"\b(?:new|import|require|eval|document|fetch)\b"), "code (new, import, require, eval, document, fetch)"),
                  (re.compile(r"[()]"), "a call or parenthesis")]


def load_js_literal(rep, path, var):
    """A data file must be exactly one statement, window.<var> = {...}; with a strict JSON literal."""
    if not path.exists():
        return None
    name = path.name
    text = path.read_text(encoding="utf-8")
    if text.startswith("﻿"):
        rep.error(f"{name}: starts with a byte-order mark; save it as UTF-8 without BOM")
        text = text[1:]
    if re.search(r"</?script", text, re.I):
        rep.error(f"{name}: contains a <script> or </script> tag; inside a string, escape it as <\\/script>")
    if "<!--" in text:
        rep.error(f"{name}: contains '<!--', which browsers treat as a comment inside a script")
    code = code_outside_strings(text)
    for rx, what in FORBIDDEN_CODE:
        if rx.search(code):
            rep.error(f"{name}: contains {what} outside a string. It must be a plain data literal")
    if code.rstrip().rstrip(";").count(";"):
        rep.error(f"{name}: contains more than one statement")
    m = re.match(r"^\s*window\." + re.escape(var) + r"\s*=\s*(\{.*\})\s*;?\s*$", text, re.S)
    if not m:
        rep.error(f"{name}: must be exactly one statement, window.{var} = {{...}};")
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        rep.error(f"{name}: the object is not strict JSON ({e}). Use double quotes, no trailing commas, no functions or comments")
        return None


def load_report_data(rep, path):
    """report-data.json (1.0+, strict JSON) or report-data.js (exactly one statement: window.KMI_DATA = {...};)."""
    jf = path.with_suffix(".json")
    if jf.exists():
        data = load_json(rep, jf)
        if data is not None and not isinstance(data, dict):
            rep.error("report-data.json: must be a JSON object")
            return None
        return data
    if path.exists():
        rep.warn("report-data.js is JavaScript the browser runs; since 1.0 write report-data.json and run scripts/build-report.py")
    return load_js_literal(rep, path, "KMI_DATA")


def check_text(rep, where, val, max_len, required=True):
    """A non-empty string of at most max_len characters. Returns True when it is one."""
    if val is None or val == "":
        if required:
            rep.error(f"report-data: {where} is required")
        return False
    if not isinstance(val, str):
        rep.error(f"report-data: {where} must be a string")
        return False
    if len(val) > max_len:
        rep.error(f"report-data: {where} is {len(val)} chars; max {max_len}")
    return True


def check_premortem(rep, n, v):
    """narrative.premortem: at most 3 failure causes, each linked to a kill shot or sub-score of this report."""
    pm = n.get("premortem")
    if pm is None:
        rep.legacy("narrative.premortem", "0.8")
        return
    if not isinstance(pm, list):
        rep.error("report-data: narrative.premortem must be a list")
        return
    if len(pm) > 3:
        rep.error(f"report-data: narrative.premortem has {len(pm)} causes; at most 3")
    if not pm:
        rep.warn("report-data: narrative.premortem is empty; write the 3 most likely causes of failure")
    ks = v.get("kill_shots") if isinstance(v.get("kill_shots"), dict) else {}
    cd = v.get("criteria_detail") if isinstance(v.get("criteria_detail"), dict) else {}
    subs = {s for block in cd.values() if isinstance(block, dict) for s in block}
    subs |= {f"{c}.{s}" for c, block in cd.items() if isinstance(block, dict) for s in block}
    for i, p in enumerate(pm):
        where = f"premortem[{i}]"
        if not isinstance(p, dict):
            rep.error(f"report-data: {where} must be an object")
            continue
        check_text(rep, f"{where}.cause", p.get("cause"), 160)
        check_text(rep, f"{where}.early_signal", p.get("early_signal"), 160)
        if p.get("likelihood") not in ("L", "M", "H"):
            rep.error(f"report-data: {where}.likelihood {p.get('likelihood')!r} must be L, M or H")
        link = p.get("linked_to")
        if not isinstance(link, str) or not link:
            rep.error(f"report-data: {where}.linked_to is required (a kill shot or sub-score key)")
        elif link not in ks and link not in subs:
            rep.error(f"report-data: {where}.linked_to {link!r} is not a kill shot in verdict.kill_shots or a sub-score in verdict.criteria_detail")
        elif link in ks and ks[link] is None:
            rep.warn(f"report-data: {where} links to kill shot {link}, which was not checked")
    order = {"H": 0, "M": 1, "L": 2}
    lk = [order[p["likelihood"]] for p in pm if isinstance(p, dict) and p.get("likelihood") in order]
    if lk != sorted(lk):
        rep.warn("report-data: premortem causes should be sorted most likely first")


def check_why_now(rep, n):
    wn = n.get("why_now")
    if wn is None:
        rep.legacy("narrative.why_now", "0.8")
        return
    if not isinstance(wn, dict):
        rep.error("report-data: narrative.why_now must be an object")
        return
    verdict = wn.get("verdict")
    if verdict not in ("now", "early", "late", "unclear"):
        rep.error(f"report-data: why_now.verdict {verdict!r} must be now, early, late or unclear")
    changes = wn.get("changes")
    if changes is None:
        changes = []
    if not isinstance(changes, list):
        rep.error("report-data: why_now.changes must be a list")
        changes = []
    if len(changes) > 5:
        rep.error(f"report-data: why_now.changes has {len(changes)} entries; at most 5")
    for i, c in enumerate(changes):
        where = f"why_now.changes[{i}]"
        if not isinstance(c, dict):
            rep.error(f"report-data: {where} must be an object")
            continue
        check_text(rep, f"{where}.what", c.get("what"), 200)
        check_text(rep, f"{where}.when", c.get("when"), 40)
        check_url(rep, f"report-data.js {where}.source", c.get("source"))
    sourced = sum(1 for c in changes if isinstance(c, dict) and c.get("source"))
    if verdict in ("now", "early", "late") and not sourced:
        rep.error(f"report-data: why_now.verdict is {verdict} but no change has a source; cite one or use unclear")
    check_text(rep, "why_now.note", wn.get("note"), 200, required=False)


def check_icp(rep, n):
    icp = n.get("icp")
    if icp is None:
        rep.legacy("narrative.icp", "0.8")
        return
    if not isinstance(icp, dict):
        rep.error("report-data: narrative.icp must be an object")
        return
    check_text(rep, "icp.who", icp.get("who"), 200)
    for k in ("pays_for_today", "budget", "trigger"):
        if icp.get(k) in (None, ""):
            rep.warn(f"report-data: icp.{k} is empty; write unknown if not found")
        else:
            check_text(rep, f"icp.{k}", icp.get(k), 200)
    where = icp.get("where")
    if where is None or where == []:
        rep.warn("report-data: icp.where is empty; name where this customer can be reached")
    elif not isinstance(where, list) or not all(isinstance(w, str) and w for w in where):
        rep.error("report-data: icp.where must be a list of strings")
    else:
        if len(where) > 5:
            rep.error(f"report-data: icp.where has {len(where)} entries; at most 5")
        for i, w in enumerate(where):
            if len(w) > 120:
                rep.error(f"report-data: icp.where[{i}] is {len(w)} chars; max 120")


def check_go_to_market(rep, n, v):
    """deepdive 1.0: personas, strategies, promotion angles, landing page and branding."""
    gtm = [k for k in ("personas", "strategies", "promotion", "branding") if n.get(k)]
    if not gtm:
        return
    if v.get("mode") != "deepdive":
        rep.warn(f"report-data: go-to-market sections ({', '.join(gtm)}) are written by deepdive; mode is {v.get('mode')!r}")
    best = max([v.get("score") or 0] + [r.get("score_after", 0) for r in v.get("rescue") or [] if isinstance(r, dict)])
    if best < 50:
        rep.error(f"report-data: go to market is only for an idea that survives (score or best rescue 50+); best is {best}")
    pers = n.get("personas") or []
    names = set()
    for i, p in enumerate(pers if isinstance(pers, list) else []):
        w = f"report-data: personas[{i}]"
        if not isinstance(p, dict) or not p.get("name"):
            rep.error(f"{w} needs a name")
            continue
        names.add(p["name"])
        q = p.get("pain_quotes") or []
        if not isinstance(q, list) or len(q) < 3:
            rep.error(f"{w} ({p['name']}) has {len(q) if isinstance(q, list) else 0} pain quotes; a persona needs at least 3 linked quotes")
        for j, x in enumerate(q if isinstance(q, list) else []):
            if not isinstance(x, dict) or not x.get("quote"):
                rep.error(f"{w}.pain_quotes[{j}] needs a quote")
            else:
                check_url(rep, f"{w}.pain_quotes[{j}].url", x.get("url"), required=True)
        for k in ("role", "trigger"):
            if not p.get(k):
                rep.error(f"{w} ({p['name']}) needs {k}")
    if isinstance(pers, list) and len(pers) > 3:
        rep.error("report-data: at most 3 personas")
    st = n.get("strategies") or []
    if st:
        rec = [s for s in st if isinstance(s, dict) and s.get("recommended") is True]
        if len(rec) != 1:
            rep.error(f"report-data: strategies need exactly one recommended (found {len(rec)})")
        for i, s in enumerate(st):
            sa = s.get("score_after") if isinstance(s, dict) else None
            if not isinstance(sa, int) or isinstance(sa, bool) or not 0 <= sa <= 100:
                rep.error(f"report-data: strategies[{i}].score_after must be an integer 0-100")
            if isinstance(s, dict) and s.get("recommended") and not s.get("why"):
                rep.error(f"report-data: the recommended strategy needs a why")
    for i, a in enumerate(n.get("promotion") or []):
        w = f"report-data: promotion[{i}]"
        if not isinstance(a, dict):
            rep.error(f"{w} must be an object")
            continue
        if names and a.get("persona") not in names:
            rep.error(f"{w}.persona {a.get('persona')!r} is not one of the personas {sorted(names)}")
        for k in ("pain", "headline", "proof"):
            if not a.get(k):
                rep.error(f"{w} needs {k}")
        if len(str(a.get("headline") or "")) > 70:
            rep.error(f"{w}.headline is over 70 characters")
        check_url(rep, f"{w}.proof_source", a.get("proof_source"), required=True)
        for j, b in enumerate(a.get("beat") or []):
            if isinstance(b, dict):
                check_url(rep, f"{w}.beat[{j}].url", b.get("url"), required=True)
    br = n.get("branding")
    if br:
        pos = br.get("positioning") if isinstance(br, dict) else None
        if not isinstance(pos, dict) or not all(pos.get(k) for k in ("for", "category", "difference")):
            rep.error("report-data: branding.positioning needs for, category and difference")
        nm = br.get("names") if isinstance(br, dict) else None
        if not isinstance(nm, list) or len(nm) != 5:
            rep.error(f"report-data: branding.names must have exactly 5 names (found {len(nm) if isinstance(nm, list) else 0})")
        for i, x in enumerate(nm if isinstance(nm, list) else []):
            w = f"report-data: branding.names[{i}]"
            if not isinstance(x, dict) or not x.get("name"):
                rep.error(f"{w} needs a name")
                continue
            for k, allowed in (("domain_com", ("available", "taken", "unknown")), ("trademark", ("clear", "conflict", "unknown"))):
                if x.get(k) not in allowed:
                    rep.error(f"{w}.{k} {x.get(k)!r} must be one of {', '.join(allowed)}")
            if x.get("domain_local") not in (None, "available", "taken", "unknown"):
                rep.error(f"{w}.domain_local must be available, taken or unknown")
            if x.get("trademark") in ("clear", "conflict"):
                check_url(rep, f"{w}.trademark_source", x.get("trademark_source"), required=True)
            if not DATE_RX.match(str(x.get("checked"))):
                rep.error(f"{w}.checked {x.get('checked')!r} is not YYYY-MM-DD (the day of the search)")


def check_report_data(rep, data, idea, v):
    if data is None:
        return None
    for k in ("idea", "verdict", "narrative"):
        if not isinstance(data.get(k), dict):
            rep.error(f"report-data: {k} object is required")
    if idea is not None and data.get("idea") != idea:
        rep.error("report-data: idea differs from idea.json; copy idea.json into it")
    if data.get("verdict") != v:
        rep.error("report-data: verdict differs from verdict.json; copy verdict.json into it")
    n = data.get("narrative") or {}
    check_go_to_market(rep, n, v)
    ans = n.get("answer")
    if not ans or not isinstance(ans, str):
        rep.error("report-data: narrative.answer is required")
    elif len(ans.split()) > 45:
        rep.warn(f"report-data: narrative.answer is {len(ans.split())} words; the standard is 45 at most")
    kf = n.get("key_findings")
    if not isinstance(kf, list) or len(kf) != 3:
        rep.error(f"report-data: narrative.key_findings must have exactly 3 entries (found {len(kf) if isinstance(kf, list) else 0})")
    else:
        for i, f in enumerate(kf):
            if not isinstance(f, dict) or not f.get("title") or not f.get("detail"):
                rep.error(f"report-data: key_findings[{i}] needs title and detail")
                continue
            if len(f["title"]) > 70:
                rep.error(f"report-data: key_findings[{i}].title is {len(f['title'])} chars; max 70")
            if len(f["detail"]) > 220:
                rep.error(f"report-data: key_findings[{i}].detail is {len(f['detail'])} chars; max 220")
            if f.get("source"):
                check_url(rep, f"report-data.js key_findings[{i}].source", f["source"])
            else:
                rep.warn(f"report-data: key_findings[{i}] has no source")
    if not n.get("recommendation"):
        rep.error("report-data: narrative.recommendation (one action, stated as a decision) is required")
    if "steelman" not in n:
        rep.legacy("narrative.steelman")
    check_premortem(rep, n, v)
    check_why_now(rep, n)
    check_icp(rep, n)
    ks = v.get("kill_shots") or {}
    nks = n.get("kill_shots") or {}
    for k in KILL_SHOTS:
        if ks.get(k) is True:
            ev = nks.get(k) if isinstance(nks, dict) else None
            if not isinstance(ev, dict) or not ev.get("evidence"):
                rep.error(f"report-data: kill shot {k} is a hit but narrative.kill_shots.{k}.evidence is missing")
            elif not ev.get("source"):
                rep.error(f"report-data: kill shot {k} is a hit without a source")
            else:
                check_url(rep, f"report-data.js kill_shots.{k}.source", ev["source"])
                if k == "strong_competitor" and not re.search(r"\d", str(ev.get("evidence"))):
                    # 1.0: a hit needs a traction number (revenue, reviews, funding, users or rank)
                    (rep.error if (idea or {}).get("type") else rep.warn)(
                        "report-data: strong_competitor is a hit but its evidence has no traction number "
                        "(revenue, reviews, funding, users or rank, SKILL.md §3)")
        elif ks.get(k) is False and isinstance(nks, dict) and not (nks.get(k) or {}).get("evidence"):
            rep.warn(f"report-data: kill shot {k} is clear; say what was searched in narrative.kill_shots.{k}.evidence")
    if ks.get("saturated_wave") is True and isinstance(nks, dict):
        ev = nks.get("saturated_wave") or {}
        if not isinstance(ev.get("count"), int) and not re.search(r"\d", str(ev.get("evidence", ""))):
            rep.error("report-data: saturated_wave is a hit but no launch count is given")
    comps = n.get("competitors") or []
    min_c = 10 if v.get("mode") == "deepdive" else 5
    if len(comps) < min_c:
        rep.warn(f"report-data: {len(comps)} competitors; a {v.get('mode') or 'kill'} should list at least {min_c}")
    for i, c in enumerate(comps):
        if not isinstance(c, dict) or not c.get("name"):
            rep.error(f"report-data: competitors[{i}] needs a name")
            continue
        for f in ("url", "price_source"):
            check_url(rep, f"report-data.js competitors[{i}].{f}", c.get(f))
        tr = c.get("traction")
        if tr is not None and (not isinstance(tr, int) or not 1 <= tr <= 5):
            rep.error(f"report-data: competitors[{i}].traction {tr!r} must be an integer 1-5 or null")
        if isinstance(c.get("price_low"), (int, float)) and c["price_low"] > 0 and not c.get("price_source") and not c.get("url"):
            rep.warn(f"report-data: competitors[{i}] ({c['name']}) has a price but no url or price_source")
    for i, q in enumerate(n.get("customer_voice") or []):
        if not isinstance(q, dict) or not q.get("quote") or not q.get("source"):
            rep.error(f"report-data: customer_voice[{i}] needs quote and source")
        else:
            check_url(rep, f"report-data.js customer_voice[{i}].source", q["source"], required=True)
    if v.get("mode") == "deepdive" and len(n.get("customer_voice") or []) < 15:
        rep.error(f"report-data: a deepdive needs 15 or more customer quotes (found {len(n.get('customer_voice') or [])})")
    sc = n.get("scenarios") or []
    if sc and len(sc) != 3:
        rep.warn(f"report-data: {len(sc)} scenarios; the standard is pessimistic, base and optimistic")
    for i, f in enumerate(n.get("fact_checks") or []):
        if not isinstance(f, dict) or f.get("status") not in ("true", "partly", "false", "unverified"):
            rep.error(f"report-data: fact_checks[{i}].status must be true, partly, false or unverified")
        elif f.get("source"):
            check_url(rep, f"report-data.js fact_checks[{i}].source", f["source"])
    for i, r in enumerate(n.get("risks") or []):
        if not isinstance(r, dict) or r.get("likelihood") not in ("L", "M", "H") or r.get("impact") not in ("L", "M", "H"):
            rep.error(f"report-data: risks[{i}] needs likelihood and impact in L / M / H")
    for i, t in enumerate(n.get("test_plan") or []):
        if not isinstance(t, dict) or not t.get("step") or not t.get("when"):
            rep.error(f"report-data: test_plan[{i}] needs when and step")
        elif not t.get("verify"):
            rep.warn(f"report-data: test_plan[{i}] has no verify signal")
    srcs = n.get("sources")
    if not isinstance(srcs, list) or not srcs:
        rep.error("report-data: narrative.sources is required (every URL cited, with title, tier and access date)")
        return n
    seen = set()
    missing_tier = 0
    for i, s in enumerate(srcs):
        if not isinstance(s, dict) or not s.get("url"):
            rep.error(f"report-data: sources[{i}] needs a url")
            continue
        check_url(rep, f"report-data.js sources[{i}].url", s["url"], required=True)
        if s["url"] in seen:
            rep.warn(f"report-data: duplicate source {s['url'][:80]}")
        seen.add(s["url"])
        if not s.get("title"):
            rep.warn(f"report-data: sources[{i}] has no title")
        if not s.get("accessed"):
            rep.warn(f"report-data: sources[{i}] has no accessed date")
        elif not DATE_RX.match(str(s["accessed"])):
            rep.error(f"report-data: sources[{i}].accessed {s['accessed']!r} is not YYYY-MM-DD")
        if s.get("tier") not in ("primary", "secondary", "tertiary"):
            missing_tier += 1
    if missing_tier == len(srcs):
        rep.legacy("source tiers (primary / secondary / tertiary)")
    elif missing_tier:
        rep.error(f"report-data: {missing_tier} sources have no tier (primary / secondary / tertiary)")
    vs = set(v.get("sources") or [])
    only_narrative = seen - vs
    if only_narrative and len(only_narrative) > len(seen) // 2:
        rep.warn(f"report-data: {len(only_narrative)} narrative sources are not in verdict.sources; verdict.sources should list every URL cited")
    # every URL used anywhere must be in the sources list
    cited = set()
    def walk(o):
        if isinstance(o, dict):
            for k, val in o.items():
                if k in ("source", "price_source", "url") and isinstance(val, str) and URL_RX.match(val):
                    cited.add(val)
                else:
                    walk(val)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk({k: val for k, val in n.items() if k != "sources"})
    walk(v.get("metrics"))
    walk(v.get("criteria_detail"))
    unlisted = cited - seen - vs
    if unlisted:
        rep.warn(f"{len(unlisted)} cited URLs are missing from the sources list, e.g. {sorted(unlisted)[0][:80]}")
    return n


def check_html(rep, folder, data):
    html = folder / "report.html"
    built = (folder / "report-data.json").exists()
    if not html.exists():
        if data is not None:
            rep.error("report.html is missing: run scripts/build-report.py" if built else "report.html is missing: copy it from skills/kill/report.html")
        return
    if built:
        br = _build_report()
        text = html.read_text(encoding="utf-8")
        if 'src="report-data.js"' in text:
            rep.error("report.html still loads report-data.js; rebuild it with scripts/build-report.py")
        try:
            emb = br.embedded(text)
        except json.JSONDecodeError:
            emb = None
            rep.error("report.html: the embedded #kmi-data block is not valid JSON; rebuild it with scripts/build-report.py")
        if emb is None:
            rep.error("report.html has no embedded data; rebuild it with scripts/build-report.py")
        elif data is not None and emb != data:
            rep.error("report.html embeds different data than report-data.json; rebuild it with scripts/build-report.py")
        elif data is not None and TEMPLATE.exists() and text != br.build(TEMPLATE.read_text(encoding="utf-8"), data):
            rep.error("report.html is not the plugin template plus its data (edited, or built from an older template); rebuild it with scripts/build-report.py")
        return
    if TEMPLATE.exists() and html.read_bytes() != TEMPLATE.read_bytes():
        rep.warn("report.html differs from the plugin template (older version or edited). Copy skills/kill/report.html again to update it.")


def _build_report():
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_report", pathlib.Path(__file__).resolve().parent / "build-report.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_folder(folder, legacy=False):
    rep = Report(folder)
    idea = load_json(rep, folder / "idea.json")
    v = load_json(rep, folder / "verdict.json")
    if v is None and not (folder / "verdict.json").exists() and ((folder / "report-data.js").exists() or (folder / "report-data.json").exists()):
        # a report folder shared without its JSON files: check the copies embedded in report-data.js
        embedded = load_report_data(rep, folder / "report-data.js")
        if isinstance(embedded, dict) and isinstance(embedded.get("verdict"), dict):
            rep.warn("verdict.json is missing; checking the copy embedded in report-data.js")
            v, idea = embedded["verdict"], idea or embedded.get("idea")
    if v is None:
        rep.error("verdict.json: missing or invalid")
        return rep
    rep.lenient = legacy
    for k in ("slug", "evaluated", "verdict", "score", "criteria", "metrics", "kill_shots"):
        if k not in v:
            rep.error(f"verdict.json: missing required field {k!r}")
    if idea and v.get("slug") != idea.get("slug"):
        rep.error(f"verdict.json slug {v.get('slug')!r} differs from idea.json slug {idea.get('slug')!r}")
    if not DATE_RX.match(str(v.get("evaluated", ""))):
        rep.error(f"verdict.json: evaluated {v.get('evaluated')!r} is not YYYY-MM-DD")
    check_idea(rep, idea)
    check_version(rep, "idea.json", idea)
    check_version(rep, "verdict.json", v)
    check_type_and_answers(rep, idea, v)
    check_run(rep, v)
    scores = check_scores(rep, v)
    check_metrics(rep, v)
    check_kill_shots(rep, v)
    rep.lenient = False  # the data file is code the browser loads: safety errors are never relaxed
    data = load_report_data(rep, folder / "report-data.js")
    rep.lenient = legacy
    narrative = check_report_data(rep, data, idea, v)
    check_sources_and_confidence(rep, v, narrative, scores)
    check_as_of(rep, v, narrative)
    check_rescue_and_test(rep, v)
    bc = v.get("by_country")
    if isinstance(bc, dict):
        for k in bc:
            if not re.match(r"^[A-Z]{2}$", k):
                rep.error(f"verdict.json: by_country key {k!r} must be an ISO country code (move 'recommended' to launch_reason)")
        if len(bc) > 1 and not v.get("launch_country"):
            rep.error("verdict.json: several countries but no launch_country")
    if idea and len(idea.get("countries") or []) > 1 and not isinstance(bc, dict):
        rep.warn("verdict.json: the idea targets several countries but by_country is missing")
    rep.lenient = False
    check_html(rep, folder, data)
    return rep


BOARD_OPTIONAL = {"history", "hits"}  # 0.9, written by build-brain.py
BOARD_KEYS = {"slug", "title", "verdict", "score", "confidence", "evaluated", "time_to_first_revenue_weeks",
              "ltv_cac", "primary_kill_shot", "best_rescue", "countries", "report", "stale"}


def check_board(ideas_dir):
    """ideas/board-data.js, written by compare: window.KMI_BOARD = {"generated": ..., "ideas": [...]};"""
    rep = Report(ideas_dir)
    path = ideas_dir / "board-data.js"
    if not path.exists():
        rep.error("board-data.js: missing (run /kill-my-idea:compare)")
        return rep
    board = load_js_literal(rep, path, "KMI_BOARD")
    if board is None:
        return rep
    top = {"schema_version", "generated", "ideas", "brain", "focus", "patterns"}
    if set(board) - top:
        rep.error(f"board-data.js: unknown top-level keys {sorted(set(board) - top)}")
    if "brain" in board and not isinstance(board["brain"], bool):
        rep.error("board-data.js: brain must be true or false")
    gen = board.get("generated")
    if not DATE_RX.match(str(gen)):
        rep.error(f"board-data.js: generated {gen!r} is not YYYY-MM-DD")
        gen = None
    ideas = board.get("ideas")
    if not isinstance(ideas, list):
        rep.error("board-data.js: ideas must be a list")
        return rep
    if not (ideas_dir / "board.html").exists():
        rep.warn("board.html is missing next to board-data.js: copy it from skills/compare/board.html")
    num = (int, float)
    slugs = set()
    for i, it in enumerate(ideas):
        w = f"board-data.js: ideas[{i}]"
        if not isinstance(it, dict):
            rep.error(f"{w} must be an object")
            continue
        missing, extra = BOARD_KEYS - set(it), set(it) - BOARD_KEYS - BOARD_OPTIONAL
        if missing:
            rep.error(f"{w} is missing {sorted(missing)}")
        if extra:
            rep.error(f"{w} has unknown keys {sorted(extra)}")
        slug = it.get("slug")
        if not isinstance(slug, str) or not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
            rep.error(f"{w}.slug {slug!r} is not kebab-case ASCII")
        elif slug in slugs:
            rep.error(f"{w}.slug {slug!r} appears twice")
        slugs.add(slug)
        if not isinstance(it.get("title"), str) or not it.get("title"):
            rep.error(f"{w}.title must be a non-empty string")
        if it.get("verdict") not in ("GO", "PIVOT", "NO-GO"):
            rep.error(f"{w}.verdict {it.get('verdict')!r} must be GO, PIVOT or NO-GO")
        sc = it.get("score")
        if not isinstance(sc, int) or isinstance(sc, bool) or not 0 <= sc <= 100:
            rep.error(f"{w}.score {sc!r} must be an integer 0-100")
        elif it.get("verdict") in ("GO", "PIVOT", "NO-GO") and band(sc) != it["verdict"]:
            rep.error(f"{w}.verdict {it['verdict']} does not match score {sc}")
        if it.get("confidence") not in ("high", "medium", "low", None):
            rep.error(f"{w}.confidence {it.get('confidence')!r} must be high, medium, low or null")
        ev = it.get("evaluated")
        if not DATE_RX.match(str(ev)):
            rep.error(f"{w}.evaluated {ev!r} is not YYYY-MM-DD")
        for k in ("time_to_first_revenue_weeks", "ltv_cac"):
            val = it.get(k)
            if val is not None and (not isinstance(val, num) or isinstance(val, bool)):
                rep.error(f"{w}.{k} {val!r} must be a number or null")
        pk = it.get("primary_kill_shot")
        if pk is not None and pk not in KILL_SHOTS:
            rep.error(f"{w}.primary_kill_shot {pk!r} is not a kill shot key")
        br = it.get("best_rescue")
        if br is not None:
            if not isinstance(br, dict) or set(br) != {"change", "score_after", "difficulty"}:
                rep.error(f"{w}.best_rescue must be null or {{change, score_after, difficulty}}")
            else:
                if not isinstance(br["change"], str) or not br["change"]:
                    rep.error(f"{w}.best_rescue.change must be a non-empty string")
                if not isinstance(br["score_after"], int) or not 0 <= br["score_after"] <= 100:
                    rep.error(f"{w}.best_rescue.score_after {br['score_after']!r} must be an integer 0-100")
                if br["difficulty"] not in DIFF_ORDER:
                    rep.error(f"{w}.best_rescue.difficulty {br['difficulty']!r} must be doable, hard or very-hard")
        cs = it.get("countries")
        if not isinstance(cs, list) or not all(isinstance(c, str) and re.match(r"^[A-Z]{2}$", c) for c in cs):
            rep.error(f"{w}.countries must be a list of ISO 3166-1 alpha-2 codes")
        rp = it.get("report")
        vj_ks = None
        if not isinstance(rp, str) or not re.match(r"^[A-Za-z0-9._-]+/report\.html$", rp) or rp.startswith("."):
            rep.error(f"{w}.report {rp!r} must be '<folder>/report.html', relative to ideas/")
        else:
            folder = ideas_dir / rp.split("/")[0]
            if not (folder / "report.html").exists():
                rep.warn(f"{w}.report {rp} does not exist")
            vj = load_json(rep, folder / "verdict.json")
            if vj is None and (folder / "report-data.js").exists():
                emb = load_js_literal(Report(folder), folder / "report-data.js", "KMI_DATA")
                vj = emb.get("verdict") if isinstance(emb, dict) else None
            vj_ks = vj.get("kill_shots") if isinstance(vj, dict) else None
            if isinstance(vj, dict):
                for k in ("slug", "verdict", "score", "evaluated", "primary_kill_shot"):
                    if k in vj and k in it and vj[k] != it[k]:
                        rep.error(f"{w}.{k} = {it[k]!r} but {folder.name}/verdict.json says {vj[k]!r}; rerun compare")
        hist = it.get("history", [])
        if not isinstance(hist, list) or len(hist) > 10 or not all(
                isinstance(h, dict) and set(h) == {"evaluated", "score"} and DATE_RX.match(str(h["evaluated"]))
                and isinstance(h["score"], int) and 0 <= h["score"] <= 100 for h in hist):
            rep.error(f"{w}.history must be at most 10 {{evaluated, score}} entries")
        elif hist and (hist[-1]["score"] != sc or hist[-1]["evaluated"] != ev):
            rep.error(f"{w}.history must end with the current evaluation ({ev}, {sc})")
        hits = it.get("hits", [])
        if not isinstance(hits, list) or not all(h in KILL_SHOTS for h in hits):
            rep.error(f"{w}.hits must be a list of kill shot keys")
        elif isinstance(vj_ks, dict) and "hits" in it and sorted(hits) != sorted(k for k in KILL_SHOTS if vj_ks.get(k) is True):
            rep.error(f"{w}.hits {hits} differ from the kill shots hit in verdict.json; rerun build-brain.py")
        st = it.get("stale")
        if not isinstance(st, bool):
            rep.error(f"{w}.stale must be true or false")
        elif gen and DATE_RX.match(str(ev)):
            age = (datetime.date.fromisoformat(gen) - datetime.date.fromisoformat(ev)).days
            if st != (age > 90):
                rep.error(f"{w}.stale is {st} but the verdict is {age} days old (stale = older than 90 days)")
    slugs_ok = {x.get("slug") for x in ideas if isinstance(x, dict)}
    fo = board.get("focus")
    if fo is not None:
        if not isinstance(fo, dict) or set(fo) - {"slug", "why", "first_action", "deadline", "decided"}:
            rep.error("board-data.js: focus must be null or {slug, why, first_action, deadline, decided}")
        elif fo.get("slug") not in slugs_ok:
            rep.error(f"board-data.js: focus.slug {fo.get('slug')!r} is not one of the ideas")
        elif not all(isinstance(v, str) and len(v) <= 300 for v in fo.values()):
            rep.error("board-data.js: focus values must be strings of at most 300 characters")
    pats = board.get("patterns")
    if pats is not None:
        if not isinstance(pats, list) or not all(isinstance(p, dict) and set(p) == {"kill_shot", "hits", "checked"}
                                                 and p["kill_shot"] in KILL_SHOTS for p in pats):
            rep.error("board-data.js: patterns must be a list of {kill_shot, hits, checked}")
        elif all(isinstance(x, dict) and isinstance(x.get("hits"), list) for x in ideas):
            want = {k: sum(k in x["hits"] for x in ideas) for k in KILL_SHOTS}
            for p in pats:
                if p["hits"] != want[p["kill_shot"]] or not isinstance(p["checked"], int) or p["checked"] < p["hits"]:
                    rep.error(f"board-data.js: patterns {p['kill_shot']} says {p['hits']} hits, the ideas say {want[p['kill_shot']]}; rerun build-brain.py")
    return rep


def print_report(name, rep):
    for e in rep.errors:
        print(f"ERROR  {name}: {e}")
    for w in rep.warnings:
        print(f"WARN   {name}: {w}")
    print(f"{'FAIL' if rep.errors else 'PASS'}   {name}: {len(rep.errors)} errors, {len(rep.warnings)} warnings")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--board":
        root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("ideas")
        if not root.is_dir():
            print(f"{root}: not a folder")
            return 1
        rep = check_board(root)
        print_report(root.name or str(root), rep)
        return 1 if rep.errors else 0
    legacy = argv[0] == "--legacy"
    if legacy:
        argv = argv[1:]
        if not argv:
            print("--legacy needs at least one folder")
            return 1
    if argv[0] == "--all":
        root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("ideas")
        folders = sorted(p.parent for p in root.glob("*/verdict.json"))
        if not folders:
            print(f"no verdict.json under {root}/")
            return 1
    else:
        folders = [pathlib.Path(a) for a in argv]
    failed = 0
    for f in folders:
        if not f.is_dir():
            print(f"{f}: not a folder")
            failed += 1
            continue
        rep = check_folder(f, legacy)
        print_report(f.name, rep)
        failed += bool(rep.errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
