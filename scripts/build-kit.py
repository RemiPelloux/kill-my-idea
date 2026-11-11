#!/usr/bin/env python3
"""Check build/plan.json against the verdict, then render the starter kit from it.

    python3 scripts/build-kit.py ideas/<folder>           check, then render
    python3 scripts/build-kit.py --check ideas/<folder>   check only, plus the files the model writes

The model writes plan.json (data) and the prose docs. This script writes everything that is
computed or templated: the user stories, sprints, Definition of Done, the 12-month business
plan (the math is done here, never by the model), the ads and storyboard docs, .env.example,
the Pelloux coding guidelines,
the design tokens and the video project (a fixed Remotion template fed with src/props.json).
It never overwrites a file the model writes. Stdlib only.
"""
import csv
import io
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VIDEO_TEMPLATE = ROOT / "skills" / "build" / "video"
GUIDELINES = ROOT / "skills" / "build" / "pelloux-guidelines.md"
SMARTTEST = "@tkmremi/smarttest@1.2.0"  # selects the tests a change can affect

SCENE_KINDS = {"hook", "problem", "stat", "product", "proof", "cta"}
FORMATS = {"1080x1920", "1080x1080", "1920x1080", "1200x628"}
CHANNELS = {"meta", "tiktok", "instagram", "youtube", "google", "linkedin", "reddit", "x", "pinterest", "email", "other"}
PRIORITIES = ("must", "should", "could")
POINTS = {1, 2, 3, 5, 8, 13}
SCENARIOS = ("Pessimistic", "Base", "Optimistic")
BASES = {"verdict", "sourced", "estimate"}
INPUTS = {
    # input key -> verdict metric it must equal when basis is "verdict"
    "revenue_per_customer_month": "price",
    "variable_cost_per_customer_month": "variable_cost_per_unit",
    "cac": "cac",
    "churn_monthly_pct": "churn_monthly_pct",
    "fixed_costs_month": "fixed_costs_month",
    "start_cash": None,
}
MODEL_FILES = ("README.md", "CLAUDE.md", "docs/prd.md", "docs/architecture.md",
               "docs/decisions.md", "docs/test-plan.md")
HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
ENV_NAME = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
SAFE_PATH = re.compile(r"^[A-Za-z0-9._\-/\[\]()@+]+$")
STORY_ID = re.compile(r"^US-\d{2,3}$")
AD_ID = re.compile(r"^AD-\d{1,2}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
UNSAFE = re.compile(r"<\s*/?\s*(script|iframe|object|embed|style)|javascript:|data:text/html", re.I)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


# ---------- checks ----------

def text(rep, where, val, max_len=300, required=True):
    if val is None or val == "":
        if required:
            rep.err(f"{where}: missing")
        return False
    if not isinstance(val, str):
        rep.err(f"{where}: must be a string")
        return False
    if len(val) > max_len:
        rep.err(f"{where}: {len(val)} characters, at most {max_len}")
    if UNSAFE.search(val):
        rep.err(f"{where}: contains markup or a script URL; plain text only")
    return True


def num(rep, where, val, lo=None, hi=None):
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        rep.err(f"{where}: must be a number")
        return False
    if lo is not None and val < lo or hi is not None and val > hi:
        rep.err(f"{where}: {val} is outside {lo}..{hi}")
        return False
    return True


def url(rep, where, val, required=True):
    if not val:
        if required:
            rep.err(f"{where}: needs a source URL")
        return
    if not isinstance(val, str) or not re.match(r"^https?://", val):
        rep.err(f"{where}: URL must start with http")


def luminance(hex_color):
    def chan(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def metric_value(v, key):
    m = (v.get("metrics") or {}).get(key)
    return m.get("value") if isinstance(m, dict) else None


def lifetime_profit(inputs):
    """Gross profit of one customer over their life, capped at 36 months."""
    rev = inputs["revenue_per_customer_month"]["value"]
    var = inputs["variable_cost_per_customer_month"]["value"]
    churn = inputs["churn_monthly_pct"]["value"] / 100
    months = min(36.0, 1 / churn) if churn > 0 else 36.0
    return (rev - var) * months


def check_plan(plan, verdict, rep):
    if plan.get("schema_version") != "1.0":
        rep.err('schema_version: must be "1.0"')
    if plan.get("slug") != verdict.get("slug"):
        rep.err(f"slug: {plan.get('slug')!r} is not the verdict's {verdict.get('slug')!r}")
    if not DATE.match(str(plan.get("generated", ""))):
        rep.err("generated: must be YYYY-MM-DD")

    b = plan.get("based_on") or {}
    if b.get("verdict") != verdict.get("verdict") or b.get("score") != verdict.get("score"):
        rep.err(f"based_on: {b.get('verdict')} {b.get('score')} does not match the verdict "
                f"{verdict.get('verdict')} {verdict.get('score')}")
    path = b.get("path")
    rescue = verdict.get("rescue") or []
    if path == "original":
        if b.get("change"):
            rep.err("based_on.change: must be null for the original idea")
    elif isinstance(path, str) and re.fullmatch(r"rescue-\d", path):
        n = int(path.split("-")[1])
        if not 1 <= n <= len(rescue):
            rep.err(f"based_on.path: {path} but the verdict has {len(rescue)} rescue path(s)")
        elif b.get("change") != rescue[n - 1].get("change"):
            rep.err(f"based_on.change: must copy rescue[{n - 1}].change exactly")
    else:
        rep.err('based_on.path: "original" or "rescue-N"')
    if verdict.get("verdict") == "NO-GO":
        rep.warn("the verdict is NO-GO: BUILD.md and README.md must say so at the top")

    p = plan.get("product") or {}
    for k, n in (("name", 60), ("one_liner", 160), ("customer", 300), ("problem", 300)):
        text(rep, f"product.{k}", p.get(k), n)
    km = p.get("key_metric") or {}
    text(rep, "product.key_metric.name", km.get("name"), 80)
    text(rep, "product.key_metric.target", km.get("target"), 80)
    if not DATE.match(str(km.get("deadline", ""))):
        rep.err("product.key_metric.deadline: YYYY-MM-DD")

    s = plan.get("stack") or {}
    text(rep, "stack.choice", s.get("choice"), 120)
    text(rep, "stack.why", s.get("why"), 500)
    comps = s.get("components") or []
    if not comps:
        rep.err("stack.components: at least 1")
    total = 0
    for i, c in enumerate(comps):
        w = f"stack.components[{i}]"
        text(rep, f"{w}.name", c.get("name"), 60)
        text(rep, f"{w}.tool", c.get("tool"), 80)
        if num(rep, f"{w}.cost_month", c.get("cost_month"), 0):
            total += c["cost_month"]
            if c["cost_month"] > 0:
                url(rep, f"{w}.source", c.get("source"))
    if len(s.get("alternatives") or []) < 2:
        rep.err("stack.alternatives: at least 2, each with why_not")
    for i, a in enumerate(s.get("alternatives") or []):
        text(rep, f"stack.alternatives[{i}].name", a.get("name"), 80)
        text(rep, f"stack.alternatives[{i}].why_not", a.get("why_not"), 300)

    for i, e in enumerate(plan.get("env") or []):
        if not ENV_NAME.match(str(e.get("name", ""))):
            rep.err(f"env[{i}].name: UPPER_SNAKE_CASE")
        if "value" in e or "default" in e:
            rep.err(f"env[{i}]: never put a value in the plan; .env.example stays empty")
        text(rep, f"env[{i}].purpose", e.get("purpose"), 160)
        url(rep, f"env[{i}].where", e.get("where"), required=False)

    structure = plan.get("structure") or []
    if len(structure) < 3:
        rep.err("structure: at least 3 paths")
    for i, it in enumerate(structure):
        sp = str(it.get("path", ""))
        if not SAFE_PATH.match(sp) or sp.startswith("/") or ".." in sp.split("/"):
            rep.err(f"structure[{i}].path: relative to build/app/, no '..'")
        text(rep, f"structure[{i}].purpose", it.get("purpose"), 160)

    personas = plan.get("personas") or []
    names = {x.get("name") for x in personas}
    if not 1 <= len(personas) <= 3:
        rep.err("personas: 1 to 3")
    for i, x in enumerate(personas):
        text(rep, f"personas[{i}].name", x.get("name"), 60)
        text(rep, f"personas[{i}].role", x.get("role"), 160)
        text(rep, f"personas[{i}].pain", x.get("pain"), 300)
        if x.get("quote"):
            text(rep, f"personas[{i}].quote", x["quote"], 300)
            url(rep, f"personas[{i}].quote_url", x.get("quote_url"))

    sprints = plan.get("sprints") or []
    numbers = [x.get("number") for x in sprints]
    if numbers != list(range(len(sprints))) or not 3 <= len(sprints) <= 5:
        rep.err("sprints: 3 to 5, numbered 0, 1, 2…")
    for i, x in enumerate(sprints):
        text(rep, f"sprints[{i}].name", x.get("name"), 60)
        text(rep, f"sprints[{i}].goal", x.get("goal"), 300)
        text(rep, f"sprints[{i}].exit", x.get("exit"), 300)
        num(rep, f"sprints[{i}].weeks", x.get("weeks"), 1, 2)
        if x.get("exit") and not re.search(r"\d", x["exit"]):
            rep.err(f"sprints[{i}].exit: needs a number (a measurable exit)")

    stories = plan.get("stories") or []
    if len(stories) < 6:
        rep.err("stories: at least 6")
    ids = set()
    used = set()
    for i, st in enumerate(stories):
        w = f"stories[{i}]"
        sid = st.get("id", "")
        if not STORY_ID.match(str(sid)) or sid in ids:
            rep.err(f"{w}.id: unique, like US-01")
        ids.add(sid)
        if st.get("persona") not in names:
            rep.err(f"{w}.persona: {st.get('persona')!r} is not a persona name")
        text(rep, f"{w}.want", st.get("want"), 200)
        text(rep, f"{w}.so_that", st.get("so_that"), 200)
        if st.get("priority") not in PRIORITIES:
            rep.err(f"{w}.priority: must, should or could")
        if st.get("points") not in POINTS:
            rep.err(f"{w}.points: one of {sorted(POINTS)}")
        if st.get("sprint") not in numbers:
            rep.err(f"{w}.sprint: {st.get('sprint')} is not a sprint number")
        used.add(st.get("sprint"))
        acc = st.get("acceptance") or []
        if len(acc) < 2:
            rep.err(f"{w}.acceptance: at least 2 criteria")
        for j, a in enumerate(acc):
            text(rep, f"{w}.acceptance[{j}]", a, 200)
    for n in numbers:
        if n not in used:
            rep.err(f"sprint {n} has no story")

    dod = plan.get("dod") or []
    if len(dod) < 5:
        rep.err("dod: at least 5 items")
    for i, d in enumerate(dod):
        text(rep, f"dod[{i}]", d, 200)

    check_business(plan, verdict, rep)
    check_brand(plan, rep)
    check_motion(plan, rep)
    check_ads(plan, names, rep)


def check_business(plan, verdict, rep):
    bp = plan.get("business_plan") or {}
    text(rep, "business_plan.currency", bp.get("currency"), 3)
    inputs = bp.get("inputs") or {}
    for key, metric in INPUTS.items():
        it = inputs.get(key)
        w = f"business_plan.inputs.{key}"
        if not isinstance(it, dict):
            rep.err(f"{w}: missing")
            continue
        num(rep, f"{w}.value", it.get("value"), 0, 100 if key == "churn_monthly_pct" else None)
        basis = it.get("basis")
        if basis not in BASES:
            rep.err(f"{w}.basis: verdict, sourced or estimate")
        elif basis == "verdict":
            if metric is None:
                rep.err(f"{w}: no verdict metric for this input; use sourced or estimate")
            elif metric_value(verdict, metric) != it.get("value"):
                rep.err(f"{w}: {it.get('value')} but verdict metrics.{metric} is "
                        f"{metric_value(verdict, metric)}")
        elif basis == "sourced":
            url(rep, f"{w}.source", it.get("source"))
        else:
            text(rep, f"{w}.reasoning", it.get("reasoning"), 300)
    sc =bp.get("scenarios") or []
    if [x.get("name") for x in sc] != list(SCENARIOS):
        rep.err("business_plan.scenarios: exactly Pessimistic, Base, Optimistic, in that order")
    for i, x in enumerate(sc):
        nc = x.get("new_customers")
        if not (isinstance(nc, list) and len(nc) == 12
                and all(isinstance(n, int) and not isinstance(n, bool) and n >= 0 for n in nc)):
            rep.err(f"business_plan.scenarios[{i}].new_customers: 12 whole numbers, month 1 to 12")
        text(rep, f"business_plan.scenarios[{i}].note", x.get("note"), 300)
    if len(sc) == 3 and all(isinstance(x.get("new_customers"), list) for x in sc):
        tot = [sum(x["new_customers"]) for x in sc if all(isinstance(n, int) for n in x["new_customers"])]
        if len(tot) == 3 and not tot[0] <= tot[1] <= tot[2]:
            rep.err("business_plan.scenarios: Pessimistic ≤ Base ≤ Optimistic in total new customers")
    for i, m in enumerate(bp.get("milestones") or []):
        num(rep, f"business_plan.milestones[{i}].month", m.get("month"), 1, 12)
        text(rep, f"business_plan.milestones[{i}].what", m.get("what"), 160)


def check_brand(plan, rep):
    br = plan.get("brand") or {}
    text(rep, "brand.name", br.get("name"), 40)
    text(rep, "brand.tagline", br.get("tagline"), 80)
    tone = br.get("tone") or []
    if not 3 <= len(tone) <= 5:
        rep.err("brand.tone: 3 to 5 words")
    cols = br.get("colors") or {}
    ok = True
    for k in ("bg", "fg", "accent", "muted"):
        if not HEX.match(str(cols.get(k, ""))):
            rep.err(f"brand.colors.{k}: #rrggbb")
            ok = False
    if ok:
        if contrast(cols["fg"], cols["bg"]) < 7:
            rep.err(f"brand.colors: fg on bg contrast {contrast(cols['fg'], cols['bg']):.1f}, needs 7+")
        if contrast(cols["muted"], cols["bg"]) < 4.5:
            rep.err(f"brand.colors: muted on bg contrast {contrast(cols['muted'], cols['bg']):.1f}, needs 4.5+")
        if contrast(cols["bg"], cols["accent"]) < 3:
            rep.err(f"brand.colors: bg on accent contrast {contrast(cols['bg'], cols['accent']):.1f}, needs 3+ "
                    "(the video and ads put bg-coloured text on accent)")


def check_motion(plan, rep):
    mo = plan.get("motion") or {}
    if mo.get("format") not in FORMATS:
        rep.err(f"motion.format: one of {sorted(FORMATS)}")
    if mo.get("fps") not in (24, 25, 30, 60):
        rep.err("motion.fps: 24, 25, 30 or 60")
    scenes = mo.get("scenes") or []
    if not 3 <= len(scenes) <= 8:
        rep.err("motion.scenes: 3 to 8")
    total = 0
    for i, sc in enumerate(scenes):
        w = f"motion.scenes[{i}]"
        if sc.get("kind") not in SCENE_KINDS:
            rep.err(f"{w}.kind: one of {sorted(SCENE_KINDS)}")
        if num(rep, f"{w}.duration_s", sc.get("duration_s"), 1.5, 8):
            total += sc["duration_s"]
        text(rep, f"{w}.text", sc.get("text"), 60)
        text(rep, f"{w}.sub", sc.get("sub"), 90, required=False)
        text(rep, f"{w}.voiceover", sc.get("voiceover"), 200, required=False)
        if sc.get("kind") == "stat":
            num(rep, f"{w}.stat", sc.get("stat"), 0)
            url(rep, f"{w}.source", sc.get("source"))
    if scenes and scenes[-1].get("kind") != "cta":
        rep.err("motion.scenes: the last scene is the cta")
    if scenes and not 15 <= total <= 30:
        rep.err(f"motion.scenes: {total:g} s in total, needs 15 to 30")
    text(rep, "motion.music", mo.get("music"), 200)


def check_ads(plan, names, rep):
    ads = plan.get("ads") or []
    if not 3 <= len(ads) <= 9:
        rep.err("ads: 3 to 9")
    ids = set()
    inputs = (plan.get("business_plan") or {}).get("inputs") or {}
    try:
        ceiling = lifetime_profit(inputs)
    except (KeyError, TypeError, ZeroDivisionError):
        ceiling = None
    angles = set()
    for i, a in enumerate(ads):
        w = f"ads[{i}]"
        if not AD_ID.match(str(a.get("id", ""))) or a.get("id") in ids:
            rep.err(f"{w}.id: unique, like AD-1")
        ids.add(a.get("id"))
        if a.get("channel") not in CHANNELS:
            rep.err(f"{w}.channel: one of {sorted(CHANNELS)}")
        if a.get("persona") not in names:
            rep.err(f"{w}.persona: not a persona name")
        if a.get("format") not in FORMATS:
            rep.err(f"{w}.format: one of {sorted(FORMATS)}")
        for k, n in (("angle", 80), ("hook", 70), ("headline", 60), ("primary_text", 300),
                     ("cta", 24), ("visual", 400), ("proof", 160)):
            text(rep, f"{w}.{k}", a.get(k), n)
        angles.add(a.get("angle"))
        url(rep, f"{w}.proof_source", a.get("proof_source"))
        if num(rep, f"{w}.target_cpa", a.get("target_cpa"), 0) and ceiling is not None:
            if a["target_cpa"] > ceiling:
                rep.err(f"{w}.target_cpa: {a['target_cpa']} is more than a customer's lifetime gross "
                        f"profit ({ceiling:.0f}); this ad would lose money on every sale")
            elif a["target_cpa"] > ceiling / 3:
                rep.warn(f"{w}.target_cpa: {a['target_cpa']} leaves LTV:CAC under 3")
    if len(angles) < 3 and ads:
        rep.err("ads: at least 3 different angles")
    t = plan.get("ad_test") or {}
    num(rep, "ad_test.budget", t.get("budget"), 0)
    num(rep, "ad_test.days", t.get("days"), 1, 30)
    text(rep, "ad_test.kill_rule", t.get("kill_rule"), 200)
    if t.get("kill_rule") and not re.search(r"\d", t["kill_rule"]):
        rep.err("ad_test.kill_rule: needs a number")


# ---------- business plan math ----------

def project(bp):
    """12 months per scenario. Returns {name: {"rows": [...], "summary": {...}}}."""
    i = {k: v["value"] for k, v in bp["inputs"].items()}
    churn = i["churn_monthly_pct"] / 100
    out = {}
    for sc in bp["scenarios"]:
        active, cash, rows = 0.0, float(i["start_cash"]), []
        for m, new in enumerate(sc["new_customers"], 1):
            active = active * (1 - churn) + new
            revenue = active * i["revenue_per_customer_month"]
            gross = active * (i["revenue_per_customer_month"] - i["variable_cost_per_customer_month"])
            marketing = new * i["cac"]
            net = gross - marketing - i["fixed_costs_month"]
            cash += net
            rows.append({"month": m, "new": new, "active": active, "revenue": revenue, "gross_profit": gross,
                         "marketing": marketing, "fixed": i["fixed_costs_month"], "net": net, "cash": cash})
        low = min(rows, key=lambda r: r["cash"])
        # Break-even: the first month from which net stays at 0 or above until month 12.
        be = None
        for r in reversed(rows):
            if r["net"] < 0 or r["active"] <= 0:
                break
            be = r["month"]
        out[sc["name"]] = {"rows": rows, "note": sc.get("note", ""), "summary": {
            "break_even_month": be,
            "lowest_cash": low["cash"], "lowest_cash_month": low["month"],
            "funding_needed": max(0.0, -low["cash"]),
            "m12_customers": rows[-1]["active"], "m12_mrr": rows[-1]["revenue"],
            "revenue_12m": sum(r["revenue"] for r in rows), "net_12m": sum(r["net"] for r in rows),
        }}
    return out


# ---------- rendering ----------

def cell(s):
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")


def money(x, cur):
    sign = "-" if x < 0 else ""
    return f"{sign}{cur} {abs(x):,.0f}"


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def header(plan, title):
    b = plan["based_on"]
    built = "the original idea" if b["path"] == "original" else f"{b['path']}: {b['change'].rstrip('.')}"
    return (f"# {title}: {plan['product']['name']}\n\n"
            f"Generated by kill-my-idea:build on {plan['generated']} from the {b['verdict']} {b['score']}/100 "
            f"verdict, building {built}.\n")


def render_stories(plan):
    out = [header(plan, "User stories"), "## Personas\n"]
    for p in plan["personas"]:
        out.append(f"- **{p['name']}**: {p['role']}. Pain: {p['pain']}")
        if p.get("quote"):
            out.append(f"  > \"{p['quote']}\" ([source]({p['quote_url']}))")
    for prio in PRIORITIES:
        group = [s for s in plan["stories"] if s["priority"] == prio]
        if not group:
            continue
        out.append(f"\n## {prio.capitalize()} have\n")
        for s in group:
            out.append(f"### {s['id']} · {s['points']} pts · sprint {s['sprint']}\n")
            out.append(f"As **{s['persona']}**, I want {s['want']}, so that {s['so_that']}.\n")
            out.append("Acceptance criteria:\n")
            out += [f"- [ ] {a}" for a in s["acceptance"]]
            out.append("")
    return "\n".join(out) + "\n"


def render_sprints(plan):
    out = [header(plan, "Sprints"),
           f"Key metric: **{plan['product']['key_metric']['name']}**, target "
           f"{plan['product']['key_metric']['target']} by {plan['product']['key_metric']['deadline']}.\n"]
    for sp in plan["sprints"]:
        stories = [s for s in plan["stories"] if s["sprint"] == sp["number"]]
        pts = sum(s["points"] for s in stories)
        out.append(f"## Sprint {sp['number']}: {sp['name']} ({sp['weeks']} week{'s' if sp['weeks'] > 1 else ''}, {pts} pts)\n")
        out.append(f"**Goal:** {sp['goal']}\n")
        out.append(f"**Exit (measured):** {sp['exit']}\n")
        out += [f"- [ ] {s['id']} ({s['points']} pts): {s['want']}" for s in stories]
        out.append("")
    return "\n".join(out) + "\n"


def render_dod(plan):
    out = [header(plan, "Definition of Done"), "A story is done when every box is ticked:\n"]
    out += [f"- [ ] {d}" for d in plan["dod"]]
    return "\n".join(out) + "\n"


def render_business(plan, proj):
    bp = plan["business_plan"]
    cur = bp["currency"]
    out = [header(plan, "Business plan"),
           "The model chose the inputs; `scripts/build-kit.py` did the math. Change an input in "
           "`plan.json` and rerun the script to update every number here.\n", "## Inputs\n"]
    rows = []
    for k, it in bp["inputs"].items():
        basis = it["basis"]
        if basis == "verdict":
            ev = f"verdict metric `{INPUTS[k]}`"
        elif basis == "sourced":
            ev = f"[source]({it['source']})"
        else:
            ev = f"(estimate) {it.get('reasoning', '')}"
        rows.append([k.replace("_", " "), f"{it['value']:,}", ev])
    out.append(table(["Input", "Value", "Evidence"], rows))
    lp = lifetime_profit(bp["inputs"])
    out.append(f"\nLifetime gross profit per customer: **{money(lp, cur)}** "
               f"(LTV:CAC {lp / bp['inputs']['cac']['value']:.1f})." if bp["inputs"]["cac"]["value"] else "")
    out.append("\n## 12 months, 3 scenarios\n")
    rows = []
    for name, p in proj.items():
        s = p["summary"]
        rows.append([name, f"{sum(r['new'] for r in p['rows'])}", f"{s['m12_customers']:.0f}", money(s["m12_mrr"], cur),
                     money(s["revenue_12m"], cur), money(s["net_12m"], cur),
                     f"month {s['break_even_month']}" if s["break_even_month"] else "not in 12 months",
                     money(s["funding_needed"], cur)])
    out.append(table(["Scenario", "New customers", "Customers M12", "MRR M12", "Revenue 12 m", "Net 12 m",
                      "Break-even", "Cash needed"], rows))
    for name, p in proj.items():
        out.append(f"\n### {name}\n\n{p['note']}\n")
        out.append(table(["Month", "New", "Active", "Revenue", "Gross profit", "Marketing", "Fixed", "Net", "Cash"],
                         [[r["month"], r["new"], f"{r['active']:.1f}", money(r["revenue"], cur),
                           money(r["gross_profit"], cur), money(r["marketing"], cur), money(r["fixed"], cur),
                           money(r["net"], cur), money(r["cash"], cur)] for r in p["rows"]]))
    if bp.get("milestones"):
        out.append("\n## Milestones\n")
        out += [f"- Month {m['month']}: {m['what']}" for m in bp["milestones"]]
    out.append("\nAll months in `business-plan.csv`.")
    return "\n".join(out) + "\n"


def render_csv(proj):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["scenario", "month", "new", "active", "revenue", "gross_profit", "marketing", "fixed", "net", "cash"])
    for name, p in proj.items():
        for r in p["rows"]:
            w.writerow([name, r["month"], r["new"]] + [f"{r[k]:.2f}" for k in
                                                        ("active", "revenue", "gross_profit", "marketing", "fixed",
                                                         "net", "cash")])
    return buf.getvalue()


def render_ads(plan):
    cur = plan["business_plan"]["currency"]
    t = plan["ad_test"]
    out = [header(plan, "Creative ads"),
           f"Test budget **{money(t['budget'], cur)}** over {t['days']} days. Kill rule: {t['kill_rule']}\n",
           "Images: `cd video && npm install && npm run ads` renders one PNG per ad into `video/out/ads/`.\n",
           "Nothing here is published or paid for. You launch the ads yourself.\n"]
    for a in plan["ads"]:
        out.append(f"## {a['id']} · {a['channel']} · {a['format']}\n")
        out.append(f"- **Angle:** {a['angle']} (for {a['persona']})")
        out.append(f"- **Hook:** {a['hook']}")
        out.append(f"- **Headline:** {a['headline']}")
        out.append(f"- **Primary text:** {a['primary_text']}")
        out.append(f"- **CTA:** {a['cta']}")
        out.append(f"- **Proof:** {a['proof']} ([source]({a['proof_source']}))")
        out.append(f"- **Visual brief:** {a['visual']}")
        out.append(f"- **Target CPA:** {money(a['target_cpa'], cur)}\n")
    return "\n".join(out) + "\n"


def render_motion(plan):
    mo = plan["motion"]
    total = sum(s["duration_s"] for s in mo["scenes"])
    out = [header(plan, "Motion design"),
           f"Format {mo['format']}, {mo['fps']} fps, {total:g} s. Music: {mo['music']}\n",
           "Render: `cd video && npm install && npm run video` writes `video/out/promo.mp4`. "
           "`npm run studio` opens it in the Remotion editor.\n", "## Storyboard\n"]
    t, rows = 0.0, []
    for i, s in enumerate(mo["scenes"], 1):
        on_screen = s["text"] + (f" / {s['sub']}" if s.get("sub") else "")
        if s["kind"] == "stat":
            on_screen = f"{s['stat']:,}{s.get('stat_suffix', '')}: {on_screen} ([source]({s['source']}))"
        rows.append([i, f"{t:g}–{t + s['duration_s']:g} s", s["kind"], on_screen, s.get("voiceover", "")])
        t += s["duration_s"]
    out.append(table(["#", "Time", "Scene", "On screen", "Voice-over"], rows))
    out.append("\nMotion: words spring in one by one, numbers count up, the accent bar grows, "
               "each scene fades and zooms 4% over its length. Problem and CTA scenes invert to the accent colour.")
    return "\n".join(out) + "\n"


def render_brand(plan):
    br = plan["brand"]
    c = br["colors"]
    out = [header(plan, "Brand"), f"**{br['name']}**: {br['tagline']}\n", f"Tone: {', '.join(br['tone'])}.\n",
           "## Colours\n",
           table(["Token", "Hex", "Use"], [["bg", c["bg"], "background"], ["fg", c["fg"], "text"],
                                           ["accent", c["accent"], "buttons, highlights"],
                                           ["muted", c["muted"], "secondary text"]]),
           f"\nContrast: text {contrast(c['fg'], c['bg']):.1f}:1, secondary {contrast(c['muted'], c['bg']):.1f}:1, "
           f"text on accent {contrast(c['bg'], c['accent']):.1f}:1.\n",
           "Tokens: `design-tokens.json` and `design-tokens.css`."]
    return "\n".join(out) + "\n"


def render_env(plan):
    out = [f"# {plan['product']['name']}: copy to .env and fill in. Never commit .env.", ""]
    for e in plan.get("env") or []:
        out.append(f"# {e['purpose']}{' (required)' if e.get('required') else ' (optional)'}")
        if e.get("where"):
            out.append(f"# Get it: {e['where']}")
        out.append(f"{e['name']}=")
        out.append("")
    return "\n".join(out)


def render_tokens(plan):
    c = plan["brand"]["colors"]
    tokens = {"color": {k: {"value": v} for k, v in c.items()},
              "font": {"family": {"value": "Inter, 'Helvetica Neue', Arial, sans-serif"}}}
    css = ":root {\n" + "".join(f"  --color-{k}: {v};\n" for k, v in c.items()) + \
          "  --font-family: Inter, 'Helvetica Neue', Arial, sans-serif;\n}\n"
    return json.dumps(tokens, indent=2) + "\n", css


def video_props(plan):
    w, h = (int(x) for x in plan["motion"]["format"].split("x"))
    br = plan["brand"]
    scenes = []
    for s in plan["motion"]["scenes"]:
        d = {"kind": s["kind"], "duration_s": s["duration_s"], "text": s["text"]}
        for k in ("sub", "stat", "stat_suffix"):
            if s.get(k) is not None:
                d[k] = s[k]
        scenes.append(d)
    ads = []
    for a in plan["ads"]:
        aw, ah = (int(x) for x in a["format"].split("x"))
        ads.append({"id": a["id"], "width": aw, "height": ah, "hook": a["hook"], "headline": a["headline"],
                    "cta": a["cta"], "proof": a["proof"]})
    return {"brand": {"name": br["name"], "tagline": br["tagline"], "colors": br["colors"]},
            "motion": {"width": w, "height": h, "fps": plan["motion"]["fps"], "scenes": scenes}, "ads": ads}


def render_index(plan, proj):
    b = plan["based_on"]
    base = proj["Base"]["summary"]
    cur = plan["business_plan"]["currency"]
    warn = ""
    if b["verdict"] == "NO-GO":
        warn = ("> ☠️ **This idea scored NO-GO.** You asked for the build kit anyway. Run the 7-day test "
                "before writing code, and stop when its kill criteria hit.\n")
    out = [f"# Build kit: {plan['product']['name']}\n", warn,
           f"{plan['product']['one_liner']}\n",
           f"Verdict: **{b['verdict']} {b['score']}/100**. Building "
           f"{'the original idea' if b['path'] == 'original' else b['path'] + ': ' + b['change'].rstrip('.')}.\n",
           f"Key metric: **{plan['product']['key_metric']['name']}**, {plan['product']['key_metric']['target']} "
           f"by {plan['product']['key_metric']['deadline']}.\n",
           f"Base case: {base['m12_customers']:.0f} customers and {money(base['m12_mrr'], cur)} MRR at month 12, "
           f"{'break-even in month ' + str(base['break_even_month']) if base['break_even_month'] else 'no break-even in 12 months'}, "
           f"cash needed {money(base['funding_needed'], cur)}.\n",
           "## Start here\n",
           "1. Read `README.md` and `docs/prd.md`.",
           "2. `cp .env.example .env` and fill it in.",
           f"3. Sprint 0 in `docs/sprints.md`: {plan['sprints'][0]['goal']}",
           "4. Code goes in `app/` (see `docs/architecture.md`), following `pelloux-guidelines.md`.",
           f"5. Tests with SmartTest (Node 22.12+), in `app/`: `npm install -D {SMARTTEST}`, "
           "`npx smarttest init --dry-run` then `--yes`, `npx smarttest hook install`. "
           "After that, `npx smarttest run` runs only the tests your change can affect.",
           "6. Video and ads: `cd video && npm install && npm run video && npm run ads`.\n",
           "## What's where\n",
           table(["File", "What"], [
               ["README.md", "the project README"], ["CLAUDE.md", "rules for an AI agent building it"],
               ["pelloux-guidelines.md", "coding discipline, mandatory for everyone"],
               ["docs/prd.md", "product requirements"], ["docs/architecture.md", "stack and structure"],
               ["docs/decisions.md", "decision log (ADR)"], ["docs/test-plan.md", "how it is tested"],
               ["docs/user-stories.md", f"{len(plan['stories'])} stories with acceptance criteria"],
               ["docs/sprints.md", f"{len(plan['sprints'])} sprints with measured exits"],
               ["docs/definition-of-done.md", "Definition of Done"],
               ["docs/business-plan.md", "12-month plan, 3 scenarios (+ business-plan.csv)"],
               ["docs/brand.md", "name, tone, colours"], ["docs/motion.md", "video storyboard"],
               ["docs/ads.md", f"{len(plan['ads'])} ads with target CPA"],
               ["design-tokens.json / .css", "colour and font tokens"],
               ["video/", "Remotion project: promo video + ad images"],
               ["app/", "the product's code"], ["plan.json", "the data all of this comes from"]]),
           "\nRerun `python3 <plugin>/scripts/build-kit.py ideas/<folder>` after editing `plan.json`. "
           "It never overwrites README.md, CLAUDE.md, the prose docs or `app/`.\n",
           "<sub>Generated by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>"]
    return "\n".join(out) + "\n"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render(folder, plan):
    b = folder / "build"
    proj = project(plan["business_plan"])
    write(b / "BUILD.md", render_index(plan, proj))
    write(b / "docs" / "user-stories.md", render_stories(plan))
    write(b / "docs" / "sprints.md", render_sprints(plan))
    write(b / "docs" / "definition-of-done.md", render_dod(plan))
    write(b / "docs" / "business-plan.md", render_business(plan, proj))
    write(b / "docs" / "business-plan.csv", render_csv(proj))
    write(b / "docs" / "ads.md", render_ads(plan))
    write(b / "docs" / "motion.md", render_motion(plan))
    write(b / "docs" / "brand.md", render_brand(plan))
    write(b / ".env.example", render_env(plan))
    tj, tc = render_tokens(plan)
    write(b / "design-tokens.json", tj)
    write(b / "design-tokens.css", tc)
    write(b / "pelloux-guidelines.md", GUIDELINES.read_text(encoding="utf-8"))
    gi = b / ".gitignore"
    if not gi.exists():
        write(gi, ".env\nnode_modules/\nvideo/out/\n.smarttest/\n")
    for it in plan["structure"]:
        if it["path"].endswith("/"):
            d = b / "app" / it["path"]
            d.mkdir(parents=True, exist_ok=True)
            if not any(d.iterdir()):
                (d / ".gitkeep").touch()
    v = b / "video"
    for src in VIDEO_TEMPLATE.rglob("*"):
        rel = src.relative_to(VIDEO_TEMPLATE)
        if src.is_file() and "node_modules" not in rel.parts and "out" not in rel.parts \
                and rel != pathlib.Path("src/props.json"):
            write(v / rel, src.read_text(encoding="utf-8"))
    write(v / "src" / "props.json", json.dumps(video_props(plan), ensure_ascii=False, indent=2) + "\n")
    return proj


def load(folder, rep):
    out = {}
    for name, p in (("plan", folder / "build" / "plan.json"), ("verdict", folder / "verdict.json")):
        try:
            out[name] = json.loads(p.read_text(encoding="utf-8"))
        except FileNotFoundError:
            rep.err(f"{p}: not found")
        except json.JSONDecodeError as e:
            rep.err(f"{p}: not valid JSON ({e})")
    return out.get("plan"), out.get("verdict")


def check_files(folder, plan, rep):
    b = folder / "build"
    for f in MODEL_FILES:
        p = b / f
        if not p.exists():
            rep.err(f"build/{f}: missing (the model writes it)")
        elif len(p.read_text(encoding="utf-8").strip()) < 200:
            rep.err(f"build/{f}: under 200 characters")
    readme = b / "README.md"
    if readme.exists():
        t = readme.read_text(encoding="utf-8")
        for h in ("## Run", "## Structure"):
            if h not in t:
                rep.err(f"build/README.md: needs a '{h}' section")
        if plan.get("based_on", {}).get("verdict") == "NO-GO" and "NO-GO" not in t[:1500]:
            rep.err("build/README.md: a NO-GO idea must say NO-GO near the top")
    for f in ("README.md", "docs/test-plan.md"):
        p = b / f
        if p.exists() and "smarttest" not in p.read_text(encoding="utf-8").lower():
            rep.err(f"build/{f}: must set up and use SmartTest (npx smarttest ...)")
    claude = b / "CLAUDE.md"
    if claude.exists() and "pelloux-guidelines.md" not in claude.read_text(encoding="utf-8"):
        rep.err("build/CLAUDE.md: must tell the agent to follow pelloux-guidelines.md")
    if not (b / "pelloux-guidelines.md").exists():
        rep.err("build/pelloux-guidelines.md: missing (rerun build-kit.py)")
    for it in plan.get("structure") or []:
        sp = it.get("path", "")
        if sp and not sp.endswith("/") and not (b / "app" / sp).exists():
            rep.warn(f"build/app/{sp}: listed in structure but not written")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    only_check = "--check" in argv
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    rep = Report()
    plan, verdict = load(folder, rep)
    if plan is not None and verdict is not None:
        check_plan(plan, verdict, rep)
        if only_check:
            check_files(folder, plan, rep)
    for w in rep.warnings:
        print(f"warning: {w}")
    if rep.errors:
        for e in rep.errors:
            print(f"error: {e}")
        print(f"FAIL {folder}: {len(rep.errors)} error(s)")
        return 1
    if only_check:
        print(f"OK {folder}/build")
        return 0
    proj = render(folder, plan)
    s = proj["Base"]["summary"]
    print(f"OK rendered {folder}/build: base case {s['m12_customers']:.0f} customers, "
          f"MRR {s['m12_mrr']:,.0f} at month 12, break-even "
          f"{'month ' + str(s['break_even_month']) if s['break_even_month'] else 'not in 12 months'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
