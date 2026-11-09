#!/usr/bin/env python3
"""Check one kill-my-idea folder (or every folder under ideas/) against the rules in SKILL.md.

    python3 scripts/check-idea.py ideas/2026-11-my-idea
    python3 scripts/check-idea.py --all            # every ideas/*/ folder with a verdict.json

No dependencies. Exit code 1 when any ERROR is found. It recomputes the score from the 21
sub-scores, applies the fixed rules R1-R5, and checks sources, counts, kill-shot coherence
and the shape of report-data.js. WARN lines are advice; ERROR lines must be fixed.
"""
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

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def legacy(self, what):
        self.warn(f"legacy (pre-0.7) verdict: missing {what}. Fine for an old report; a new run must write it.")


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
    if capped:
        expected = min(expected, 69)
    if "score_raw" in v:
        if not isinstance(v["score_raw"], (int, float)) or abs(float(v["score_raw"]) - raw1) > 0.051:
            rep.error(f"verdict.json: score_raw = {v.get('score_raw')} but sum(weight x mean) / 5 = {raw1}")
    else:
        rep.legacy("score_raw")
    score = v.get("score")
    if not isinstance(score, int):
        rep.error(f"verdict.json: score {score!r} must be an integer")
    elif score != expected:
        how = f"raw {raw1} rounds half up to {round_half_up(raw)}" + (", capped at 69 (R2: no channel)" if capped else "")
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
    lc = ((v.get("metrics") or {}).get("ltv_cac") or {}).get("value")
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


def load_report_data(rep, path):
    """report-data.js must be exactly one statement: window.KMI_DATA = {...};"""
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if re.search(r"</?script", text, re.I):
        rep.error("report-data.js: contains a <script> tag")
    m = re.match(r"^\s*window\.KMI_DATA\s*=\s*(\{.*\})\s*;?\s*$", text, re.S)
    if not m:
        rep.error("report-data.js: must be exactly one statement, window.KMI_DATA = {...};")
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        rep.error(f"report-data.js: the object is not strict JSON ({e}). Use double quotes, no trailing commas, no functions or comments")
        return None


def check_report_data(rep, data, idea, v):
    if data is None:
        return None
    for k in ("idea", "verdict", "narrative"):
        if not isinstance(data.get(k), dict):
            rep.error(f"report-data.js: {k} object is required")
    if idea is not None and data.get("idea") != idea:
        rep.error("report-data.js: idea differs from idea.json; copy idea.json into it")
    if data.get("verdict") != v:
        rep.error("report-data.js: verdict differs from verdict.json; copy verdict.json into it")
    n = data.get("narrative") or {}
    ans = n.get("answer")
    if not ans or not isinstance(ans, str):
        rep.error("report-data.js: narrative.answer is required")
    elif len(ans.split()) > 45:
        rep.warn(f"report-data.js: narrative.answer is {len(ans.split())} words; the standard is 45 at most")
    kf = n.get("key_findings")
    if not isinstance(kf, list) or len(kf) != 3:
        rep.error(f"report-data.js: narrative.key_findings must have exactly 3 entries (found {len(kf) if isinstance(kf, list) else 0})")
    else:
        for i, f in enumerate(kf):
            if not isinstance(f, dict) or not f.get("title") or not f.get("detail"):
                rep.error(f"report-data.js: key_findings[{i}] needs title and detail")
                continue
            if len(f["title"]) > 70:
                rep.error(f"report-data.js: key_findings[{i}].title is {len(f['title'])} chars; max 70")
            if len(f["detail"]) > 220:
                rep.error(f"report-data.js: key_findings[{i}].detail is {len(f['detail'])} chars; max 220")
            if f.get("source"):
                check_url(rep, f"report-data.js key_findings[{i}].source", f["source"])
            else:
                rep.warn(f"report-data.js: key_findings[{i}] has no source")
    if not n.get("recommendation"):
        rep.error("report-data.js: narrative.recommendation (one action, stated as a decision) is required")
    if "steelman" not in n:
        rep.legacy("narrative.steelman")
    ks = v.get("kill_shots") or {}
    nks = n.get("kill_shots") or {}
    for k in KILL_SHOTS:
        if ks.get(k) is True:
            ev = nks.get(k) if isinstance(nks, dict) else None
            if not isinstance(ev, dict) or not ev.get("evidence"):
                rep.error(f"report-data.js: kill shot {k} is a hit but narrative.kill_shots.{k}.evidence is missing")
            elif not ev.get("source"):
                rep.error(f"report-data.js: kill shot {k} is a hit without a source")
            else:
                check_url(rep, f"report-data.js kill_shots.{k}.source", ev["source"])
        elif ks.get(k) is False and isinstance(nks, dict) and not (nks.get(k) or {}).get("evidence"):
            rep.warn(f"report-data.js: kill shot {k} is clear; say what was searched in narrative.kill_shots.{k}.evidence")
    if ks.get("saturated_wave") is True and isinstance(nks, dict):
        ev = nks.get("saturated_wave") or {}
        if not isinstance(ev.get("count"), int) and not re.search(r"\d", str(ev.get("evidence", ""))):
            rep.error("report-data.js: saturated_wave is a hit but no launch count is given")
    comps = n.get("competitors") or []
    min_c = 10 if v.get("mode") == "deepdive" else 5
    if len(comps) < min_c:
        rep.warn(f"report-data.js: {len(comps)} competitors; a {v.get('mode') or 'kill'} should list at least {min_c}")
    for i, c in enumerate(comps):
        if not isinstance(c, dict) or not c.get("name"):
            rep.error(f"report-data.js: competitors[{i}] needs a name")
            continue
        for f in ("url", "price_source"):
            check_url(rep, f"report-data.js competitors[{i}].{f}", c.get(f))
        tr = c.get("traction")
        if tr is not None and (not isinstance(tr, int) or not 1 <= tr <= 5):
            rep.error(f"report-data.js: competitors[{i}].traction {tr!r} must be an integer 1-5 or null")
        if isinstance(c.get("price_low"), (int, float)) and c["price_low"] > 0 and not c.get("price_source") and not c.get("url"):
            rep.warn(f"report-data.js: competitors[{i}] ({c['name']}) has a price but no url or price_source")
    for i, q in enumerate(n.get("customer_voice") or []):
        if not isinstance(q, dict) or not q.get("quote") or not q.get("source"):
            rep.error(f"report-data.js: customer_voice[{i}] needs quote and source")
        else:
            check_url(rep, f"report-data.js customer_voice[{i}].source", q["source"], required=True)
    if v.get("mode") == "deepdive" and len(n.get("customer_voice") or []) < 15:
        rep.error(f"report-data.js: a deepdive needs 15 or more customer quotes (found {len(n.get('customer_voice') or [])})")
    sc = n.get("scenarios") or []
    if sc and len(sc) != 3:
        rep.warn(f"report-data.js: {len(sc)} scenarios; the standard is pessimistic, base and optimistic")
    for i, f in enumerate(n.get("fact_checks") or []):
        if not isinstance(f, dict) or f.get("status") not in ("true", "partly", "false", "unverified"):
            rep.error(f"report-data.js: fact_checks[{i}].status must be true, partly, false or unverified")
        elif f.get("source"):
            check_url(rep, f"report-data.js fact_checks[{i}].source", f["source"])
    for i, r in enumerate(n.get("risks") or []):
        if not isinstance(r, dict) or r.get("likelihood") not in ("L", "M", "H") or r.get("impact") not in ("L", "M", "H"):
            rep.error(f"report-data.js: risks[{i}] needs likelihood and impact in L / M / H")
    for i, t in enumerate(n.get("test_plan") or []):
        if not isinstance(t, dict) or not t.get("step") or not t.get("when"):
            rep.error(f"report-data.js: test_plan[{i}] needs when and step")
        elif not t.get("verify"):
            rep.warn(f"report-data.js: test_plan[{i}] has no verify signal")
    srcs = n.get("sources")
    if not isinstance(srcs, list) or not srcs:
        rep.error("report-data.js: narrative.sources is required (every URL cited, with title, tier and access date)")
        return n
    seen = set()
    missing_tier = 0
    for i, s in enumerate(srcs):
        if not isinstance(s, dict) or not s.get("url"):
            rep.error(f"report-data.js: sources[{i}] needs a url")
            continue
        check_url(rep, f"report-data.js sources[{i}].url", s["url"], required=True)
        if s["url"] in seen:
            rep.warn(f"report-data.js: duplicate source {s['url'][:80]}")
        seen.add(s["url"])
        if not s.get("title"):
            rep.warn(f"report-data.js: sources[{i}] has no title")
        if not s.get("accessed"):
            rep.warn(f"report-data.js: sources[{i}] has no accessed date")
        elif not DATE_RX.match(str(s["accessed"])):
            rep.error(f"report-data.js: sources[{i}].accessed {s['accessed']!r} is not YYYY-MM-DD")
        if s.get("tier") not in ("primary", "secondary", "tertiary"):
            missing_tier += 1
    if missing_tier == len(srcs):
        rep.legacy("source tiers (primary / secondary / tertiary)")
    elif missing_tier:
        rep.error(f"report-data.js: {missing_tier} sources have no tier (primary / secondary / tertiary)")
    vs = set(v.get("sources") or [])
    only_narrative = seen - vs
    if only_narrative and len(only_narrative) > len(seen) // 2:
        rep.warn(f"report-data.js: {len(only_narrative)} narrative sources are not in verdict.sources; verdict.sources should list every URL cited")
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


def check_html(rep, folder, has_data):
    html = folder / "report.html"
    if not html.exists():
        if has_data:
            rep.error("report.html is missing: copy it from skills/kill/report.html")
        return
    if TEMPLATE.exists() and html.read_bytes() != TEMPLATE.read_bytes():
        rep.warn("report.html differs from the plugin template (older version or edited). Copy skills/kill/report.html again to update it.")


def check_folder(folder):
    rep = Report(folder)
    idea = load_json(rep, folder / "idea.json")
    v = load_json(rep, folder / "verdict.json")
    if v is None and not (folder / "verdict.json").exists() and (folder / "report-data.js").exists():
        # a report folder shared without its JSON files: check the copies embedded in report-data.js
        embedded = load_report_data(rep, folder / "report-data.js")
        if isinstance(embedded, dict) and isinstance(embedded.get("verdict"), dict):
            rep.warn("verdict.json is missing; checking the copy embedded in report-data.js")
            v, idea = embedded["verdict"], idea or embedded.get("idea")
    if v is None:
        rep.error("verdict.json: missing or invalid")
        return rep
    for k in ("slug", "evaluated", "verdict", "score", "criteria", "metrics", "kill_shots"):
        if k not in v:
            rep.error(f"verdict.json: missing required field {k!r}")
    if idea and v.get("slug") != idea.get("slug"):
        rep.error(f"verdict.json slug {v.get('slug')!r} differs from idea.json slug {idea.get('slug')!r}")
    if not DATE_RX.match(str(v.get("evaluated", ""))):
        rep.error(f"verdict.json: evaluated {v.get('evaluated')!r} is not YYYY-MM-DD")
    check_idea(rep, idea)
    scores = check_scores(rep, v)
    check_metrics(rep, v)
    check_kill_shots(rep, v)
    data = load_report_data(rep, folder / "report-data.js")
    narrative = check_report_data(rep, data, idea, v)
    check_sources_and_confidence(rep, v, narrative, scores)
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
    check_html(rep, folder, data is not None)
    return rep


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
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
        rep = check_folder(f)
        for e in rep.errors:
            print(f"ERROR  {f.name}: {e}")
        for w in rep.warnings:
            print(f"WARN   {f.name}: {w}")
        status = "FAIL" if rep.errors else "PASS"
        print(f"{status}   {f.name}: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
        failed += bool(rep.errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
