#!/usr/bin/env python3
"""Check validate.json (the 7-day test kit and its results), render the kit, put it in the report.

    python3 scripts/validate-kit.py ideas/<folder>           check, render validate/, rebuild report.html
    python3 scripts/validate-kit.py --check ideas/<folder>   check only

The model writes validate.json: a landing page with a waitlist, an interview script, outreach
messages and the targets to hit in 7 days. Once the founder has real numbers, the model adds a
`results` block. This script checks that every target got a result, that a sub-score only goes up
on a target that was met (and only down on one that was missed), by 2 points at most, and re-scores
the idea with check-idea.py's own rules. verdict.json is never touched: the validated score sits
next to the researched one. Stdlib only.
"""
import csv
import html
import importlib.util
import io
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("fix_kit", ROOT / "scripts" / "fix-kit.py")
fk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fk)
chk = fk.chk

METRICS = {"signups", "replies", "interviews_pain", "presales", "visits", "conversion", "other"}
COMMITMENT = {"signups", "presales"}
TARGET_ID = re.compile(r"^T\d{1,2}$")
URL_IN_TEXT = re.compile(r"https?://|www\.|\]\(", re.I)
LEADING = re.compile(r"^\s*(would you|do you think|wouldn't it|don't you|how much would you pay)", re.I)
MAX_MOVE = 2
Report, text, url, sub_score, SUB_OF = fk.Report, fk.text, fk.url, fk.sub_score, fk.SUB_OF


def num(rep, where, val, positive=False):
    if isinstance(val, bool) or not isinstance(val, (int, float)) or val < 0 or (positive and val == 0):
        rep.error(f"{where}: a number{' above 0' if positive else ', 0 or more'}")
        return False
    return True


def check_landing(rep, v):
    la = v.get("landing") or {}
    for k, n in (("name", 40), ("headline", 90), ("subhead", 200), ("cta", 30)):
        text(rep, f"landing.{k}", la.get(k), n)
    b = la.get("bullets") or []
    if not 3 <= len(b) <= 5:
        rep.error("landing.bullets: 3 to 5")
    for i, x in enumerate(b):
        text(rep, f"landing.bullets[{i}]", x, 120)
    pr = la.get("price")
    if pr is not None:
        num(rep, "landing.price.amount", (pr or {}).get("amount"))
        text(rep, "landing.price.currency", (pr or {}).get("currency"), 5)
        text(rep, "landing.price.period", (pr or {}).get("period"), 20)
    proof = la.get("proof")
    if proof is not None:
        text(rep, "landing.proof.text", (proof or {}).get("text"), 200)
        url(rep, "landing.proof.source", (proof or {}).get("source"))
    fu = la.get("form_url", "")
    if fu and not re.match(r"^https://[^\s\"'<>]+$", str(fu)):
        rep.error("landing.form_url: an https URL of your form tool, or empty until you have one")


def check_interview(rep, v):
    iv = v.get("interview") or {}
    text(rep, "interview.who", iv.get("who"), 160)
    q = iv.get("questions") or []
    if not 5 <= len(q) <= 12:
        rep.error("interview.questions: 5 to 12")
    for i, x in enumerate(q):
        text(rep, f"interview.questions[{i}]", x, 200)
        if isinstance(x, str) and LEADING.search(x):
            rep.error(f"interview.questions[{i}]: asks for an opinion about the future; ask about what they did last time")
    for i, x in enumerate(iv.get("red_flags") or []):
        text(rep, f"interview.red_flags[{i}]", x, 160)


def check_outreach(rep, v):
    out = v.get("outreach") or []
    if not 1 <= len(out) <= 6:
        rep.error("outreach: 1 to 6 messages")
    for i, m in enumerate(out):
        text(rep, f"outreach[{i}].channel", m.get("channel"), 40)
        text(rep, f"outreach[{i}].where", m.get("where"), 80)
        text(rep, f"outreach[{i}].text", m.get("text"), 700)
        if not isinstance(m.get("links_allowed"), bool):
            rep.error(f"outreach[{i}].links_allowed: true or false, from the place's rules")
        elif m["links_allowed"] is False and URL_IN_TEXT.search(str(m.get("text") or "")):
            rep.error(f"outreach[{i}].text: has a link, but {m.get('where')} doesn't allow them")


def check_targets(rep, v):
    ts = v.get("targets") or []
    if not 2 <= len(ts) <= 6:
        rep.error("targets: 2 to 6")
    ids = set()
    for i, t in enumerate(ts):
        w = f"targets[{i}]"
        if not TARGET_ID.match(str(t.get("id"))) or t.get("id") in ids:
            rep.error(f"{w}.id: unique, like T1")
        ids.add(t.get("id"))
        if t.get("metric") not in METRICS:
            rep.error(f"{w}.metric: one of {sorted(METRICS)}")
        text(rep, f"{w}.label", t.get("label"), 120)
        text(rep, f"{w}.by", t.get("by"), 20)
        num(rep, f"{w}.goal", t.get("goal"), positive=True)
        if t.get("out_of") is not None:
            num(rep, f"{w}.out_of", t.get("out_of"), positive=True)
        mv = t.get("moves") or []
        if not mv:
            rep.error(f"{w}.moves: the sub-scores this evidence can change (at least 1)")
        for s in mv:
            if s not in SUB_OF:
                rep.error(f"{w}.moves: {s!r} is not one of the 21 sub-scores")
    if ts and not any(t.get("metric") in COMMITMENT for t in ts):
        rep.error("targets: at least one is signups or presales; opinions alone don't validate an idea")
    kc = v.get("kill_criteria") or []
    if not kc:
        rep.error("kill_criteria: at least 1, with a number")
    for i, k in enumerate(kc):
        text(rep, f"kill_criteria[{i}]", k, 200)
        if isinstance(k, str) and not re.search(r"\d", k):
            rep.error(f"kill_criteria[{i}]: needs a number")
    return {t.get("id"): t for t in ts}


def status(t, e):
    """met / missed for a target and its result entry."""
    if t.get("out_of") and e.get("out_of"):
        return "met" if e["actual"] / e["out_of"] >= t["goal"] / t["out_of"] and e["out_of"] >= t["out_of"] else "missed"
    return "met" if e["actual"] >= t["goal"] else "missed"


def check_results(rep, v, verdict, targets):
    res = v.get("results")
    if res is None:
        return {}
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(res.get("date"))):
        rep.error("results.date: YYYY-MM-DD")
    entries, st = {}, {}
    for i, e in enumerate(res.get("entries") or []):
        w = f"results.entries[{i}]"
        if e.get("target") not in targets:
            rep.error(f"{w}.target: {e.get('target')!r} is not a target id")
            continue
        ok = num(rep, f"{w}.actual", e.get("actual"))
        if targets[e["target"]].get("out_of") and not num(rep, f"{w}.out_of", e.get("out_of"), positive=True):
            ok = False
        text(rep, f"{w}.evidence", e.get("evidence"), 200)
        entries[e["target"]] = e
        if ok:
            st[e["target"]] = status(targets[e["target"]], e)
    for tid in targets:
        if tid not in entries:
            rep.error(f"results: no result for {tid}; enter 0 if nothing happened")
    vcd = verdict.get("criteria_detail") or {}
    moves = {}
    for i, m in enumerate(res.get("moves") or []):
        w = f"results.moves[{i}]"
        sub, tid = m.get("sub"), m.get("target")
        if sub not in SUB_OF:
            rep.error(f"{w}.sub: {sub!r} is not one of the 21 sub-scores")
            continue
        if tid not in targets:
            rep.error(f"{w}.target: {tid!r} is not a target id")
            continue
        if sub not in (targets[tid].get("moves") or []):
            rep.error(f"{w}: {tid} can't move {sub}; list it in the target's moves before the test")
        if m.get("from") != sub_score(vcd, sub):
            rep.error(f"{w}: {sub} from {m.get('from')} but the verdict has {sub_score(vcd, sub)}")
        if sub in moves:
            rep.error(f"{w}: {sub} is already moved by {moves[sub][2]}")
        a, b = m.get("from"), m.get("to")
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if abs(b - a) > MAX_MOVE:
                rep.error(f"{w}: {sub} moves {b - a:+}; one week of evidence moves a sub-score {MAX_MOVE} points at most")
            if b > a and st.get(tid) != "met":
                rep.error(f"{w}: {sub} goes up, but {tid} was not met")
            if b < a and st.get(tid) == "met":
                rep.error(f"{w}: {sub} goes down, but {tid} was met")
        text(rep, f"{w}.why", m.get("why"), 200)
        moves[sub] = (a, b, tid)
    cleared = set()
    for i, c in enumerate(res.get("clears") or []):
        k, tid = c.get("kill_shot"), c.get("target")
        if (verdict.get("kill_shots") or {}).get(k) is not True:
            rep.error(f"results.clears[{i}]: {k!r} did not hit in the verdict")
        if st.get(tid) != "met":
            rep.error(f"results.clears[{i}]: {tid!r} was not met, so it can't clear {k}")
        cleared.add(k)
    for tid, s in st.items():
        if s == "missed" and targets[tid].get("metric") in COMMITMENT and \
                not any(m[2] == tid and m[1] < m[0] for m in moves.values()):
            rep.warn(f"{tid} ({targets[tid].get('metric')}) was missed but no sub-score went down")
    fk.rescore_against(rep, verdict, res.get("rescored") or {}, moves, cleared, "results.rescored", "target")
    return st


def check_validate(v, verdict, rep):
    if v.get("schema_version") != "1.0":
        rep.error('schema_version: must be "1.0"')
    if v.get("slug") != verdict.get("slug"):
        rep.error(f"slug: {v.get('slug')!r} is not the verdict's {verdict.get('slug')!r}")
    b = v.get("based_on") or {}
    if b.get("verdict") != verdict.get("verdict") or b.get("score") != verdict.get("score"):
        rep.error("based_on: must copy the verdict's verdict and score")
    text(rep, "hypothesis", v.get("hypothesis"), 200)
    check_landing(rep, v)
    check_interview(rep, v)
    check_outreach(rep, v)
    targets = check_targets(rep, v)
    return check_results(rep, v, verdict, targets)


# ---- render -----------------------------------------------------------------------------------

def e(s):
    return html.escape(str(s or ""), quote=True)


def landing_html(v):
    la = v["landing"]
    fu = la.get("form_url") or ""
    host = re.match(r"^https://[^/]+", fu).group(0) if fu else "'none'"
    price = la.get("price")
    price_line = f'<p class="price">{e(price["amount"])} {e(price["currency"])} / {e(price["period"])}</p>' if price else ""
    proof = la.get("proof")
    proof_line = (f'<p class="proof">{e(proof["text"])} <a href="{e(proof["source"])}" rel="noopener noreferrer">source</a></p>'
                  if proof else "")
    form = (f'<form action="{e(fu)}" method="post"><label for="email">Email</label>'
            f'<input id="email" name="email" type="email" required placeholder="you@example.com">'
            f'<button type="submit">{e(la["cta"])}</button></form>') if fu else (
        f'<form><input type="email" disabled placeholder="you@example.com" aria-label="Email">'
        f'<button type="button" disabled>{e(la["cta"])}</button></form>'
        '<p class="todo">Add your form URL (Tally, Formspree, Google Forms…) as landing.form_url in validate.json, '
        'then rerun validate-kit.py.</p>')
    bullets = "".join(f"<li>{e(b)}</li>" for b in la["bullets"])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; form-action {host}; base-uri 'none'">
<title>{e(la["name"])}</title>
<style>
:root{{--bg:#f6f8fb;--fg:#0f172a;--muted:#475569;--accent:#2563eb;--card:#fff;--line:#dbe3ee}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0b1220;--fg:#e2e8f0;--muted:#94a3b8;--accent:#60a5fa;--card:#111a2e;--line:#1e293b}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,sans-serif}}
main{{max-width:640px;margin:0 auto;padding:56px 16px}}.name{{font-weight:700;color:var(--accent);letter-spacing:.02em}}
h1{{font-size:clamp(28px,6vw,42px);line-height:1.15;margin:12px 0}}.sub{{color:var(--muted);font-size:19px}}
ul{{padding:0;list-style:none}}li{{padding:10px 0 10px 28px;border-bottom:1px solid var(--line);position:relative}}
li::before{{content:"✓";position:absolute;left:0;color:var(--accent);font-weight:700}}
.price{{font-size:22px;font-weight:700}}form{{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0 8px}}
label{{position:absolute;left:-9999px}}input{{flex:1 1 220px;padding:12px;border:1px solid var(--line);border-radius:8px;font:inherit;background:var(--card);color:var(--fg)}}
button{{padding:12px 20px;border:0;border-radius:8px;background:var(--accent);color:#fff;font:inherit;font-weight:600;cursor:pointer}}
button:disabled{{opacity:.5;cursor:not-allowed}}.proof,.todo{{color:var(--muted);font-size:14px}}.todo{{border-left:3px solid var(--accent);padding-left:10px}}
a{{color:var(--accent)}}
</style></head><body><main>
<div class="name">{e(la["name"])}</div><h1>{e(la["headline"])}</h1><p class="sub">{e(la["subhead"])}</p>
<ul>{bullets}</ul>{price_line}{form}{proof_line}
</main></body></html>
"""


def interview_md(v):
    iv = v["interview"]
    q = "\n".join(f"{i}. {x}" for i, x in enumerate(iv["questions"], 1))
    flags = "\n".join(f"- {x}" for x in iv.get("red_flags") or [])
    return (f"# Interview script\n\nWho: {iv['who']}\n\nAsk about what they did, not what they would do. "
            f"Don't pitch until the last minute.\n\n{q}\n" + (f"\n## Red flags\n\n{flags}\n" if flags else ""))


def outreach_md(v):
    parts = ["# Outreach messages\n\nNothing here is sent for you. Read the place's rules before posting.\n"]
    for m in v["outreach"]:
        parts.append(f"## {m['channel']}: {m['where']}\n\n{'Links allowed.' if m['links_allowed'] else 'No links.'}\n\n"
                     f"```text\n{m['text']}\n```\n")
    return "\n".join(parts)


def tracker_csv(v):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["target", "metric", "label", "goal", "out_of", "by", "actual", "actual_out_of", "evidence"])
    res = {x["target"]: x for x in (v.get("results") or {}).get("entries") or []}
    for t in v["targets"]:
        r = res.get(t["id"], {})
        w.writerow([t["id"], t["metric"], t["label"], t["goal"], t.get("out_of") or "", t["by"],
                    r.get("actual", ""), r.get("out_of", ""), r.get("evidence", "")])
    return buf.getvalue()


def narrative(v, verdict, st):
    res = v.get("results")
    out = {"hypothesis": v["hypothesis"], "landing": {k: v["landing"].get(k) for k in ("name", "headline", "cta")},
           "score_before": verdict["score"], "kill_criteria": v["kill_criteria"],
           "targets": [{k: t.get(k) for k in ("id", "metric", "label", "goal", "out_of", "by")} |
                       {"status": st.get(t["id"], "pending")} for t in v["targets"]],
           "files": ["validate/landing.html", "validate/interview.md", "validate/outreach.md", "validate/tracker.csv"]}
    if res:
        r = {x["target"]: x for x in res.get("entries") or []}
        for t in out["targets"]:
            t["actual"] = r.get(t["id"], {}).get("actual")
            t["actual_out_of"] = r.get(t["id"], {}).get("out_of")
        rs = res["rescored"]
        out |= {"date": res["date"], "score_after": rs["score"], "verdict_after": rs["verdict"],
                "moves": res.get("moves") or [], "clears": [c["kill_shot"] for c in res.get("clears") or []]}
    return out


def render(folder, v):
    d = folder / "validate"
    d.mkdir(exist_ok=True)
    (d / "landing.html").write_text(landing_html(v), encoding="utf-8")
    (d / "interview.md").write_text(interview_md(v), encoding="utf-8")
    (d / "outreach.md").write_text(outreach_md(v), encoding="utf-8")
    (d / "tracker.csv").write_text(tracker_csv(v), encoding="utf-8")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    rep = Report()
    v, verdict = fk.load(folder / "validate.json", rep), fk.load(folder / "verdict.json", rep)
    st = check_validate(v, verdict, rep) if v is not None and verdict is not None else {}
    for w in rep.warnings:
        print(f"warning: {w}")
    if rep.errors:
        for x in rep.errors:
            print(f"error: {x}")
        print(f"FAIL {folder}: {len(rep.errors)} error(s)")
        return 1
    if v.get("results"):
        rs = v["results"]["rescored"]
        met = sum(1 for s in st.values() if s == "met")
        line = f"researched {verdict['score']} → validated {rs['score']} {rs['verdict']} ({met}/{len(st)} targets met)"
    else:
        line = f"test kit ready, {len(v['targets'])} targets, waiting for results"
    if "--check" in argv:
        print(f"OK {folder}/validate.json: {line}")
        return 0
    render(folder, v)
    data_path = folder / "report-data.json"
    if data_path.exists():
        data = json.loads(data_path.read_text(encoding="utf-8"))
        data.setdefault("narrative", {})["validate"] = narrative(v, verdict, st)
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-report.py"), str(folder)], check=True,
                       stdout=subprocess.DEVNULL)
    print(f"OK {folder}: {line}; kit in validate/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
