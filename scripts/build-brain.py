#!/usr/bin/env python3
"""Build the idea dashboard and the brain note from every verdict in ideas/.

    python3 scripts/build-brain.py [ideas]
    python3 scripts/build-brain.py --no-brain docs/gallery   # dashboard only, e.g. a public gallery

Reads ideas/*/verdict.json and idea.json (or the copies embedded in report-data.js), plus
the optional ideas/focus.json written by compare, then writes:

- ideas/board-data.js  the data for the dashboard (window.KMI_BOARD = {...};)
- ideas/board.html     a copy of skills/compare/board.html
- ideas/BRAIN.md       one note for all ideas. Only the block between the kmi:auto markers is
                       rewritten; the "Me" profile and everything else you write is kept.

Everything is computed from the verdicts, never invented: the ranking, the kill-shot
patterns, the score changes and the lessons. Python stdlib only.
"""
import datetime
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOARD_HTML = ROOT / "skills" / "compare" / "board.html"
KILL_SHOTS = {"free_alternative": "Free alternative", "strong_competitor": "Strong direct competitor",
              "graveyard": "Failed attempts before", "no_distribution": "No distribution channel",
              "costs_eat_margin": "Costs eat the margin", "weak_demand": "Weak or falling demand",
              "legal_platform_risk": "Legal or platform risk",
              "saturated_wave": "Saturated wave of look-alike launches"}
CONF = {"high": 3, "medium": 2, "low": 1}
START, END = "<!-- kmi:auto:start", "<!-- kmi:auto:end -->"
DATA_RX = re.compile(r"^\s*window\.KMI_DATA\s*=\s*(\{.*\})\s*;?\s*$", re.S)
DATE_RX = re.compile(r"^\d{4}-\d{2}-\d{2}$")

BRAIN_HEAD = """# Idea brain

One note for all your ideas. kill-my-idea reads **Me** before it asks you anything, and
rewrites only the block between the `kmi:auto` markers after each run. Write anywhere else:
it is kept.

## Me

- Country:
- Budget:
- Time per week:
- Goal:
- Edge (skills, audience, network, assets):
- Languages:

"""
BRAIN_TAIL = """
## Notes

"""


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def load_folder(folder):
    """(verdict, idea, narrative) from the JSON files, or from report-data.js when they are missing."""
    v, idea, narrative = read_json(folder / "verdict.json"), read_json(folder / "idea.json"), {}
    rd, rj = folder / "report-data.js", folder / "report-data.json"
    data = None
    if rj.exists():
        data = read_json(rj) or {}
    elif rd.exists():
        m = DATA_RX.match(rd.read_text(encoding="utf-8").lstrip("\ufeff"))
        if m:
            try:
                data = json.loads(m.group(1))
            except json.JSONDecodeError:
                data = {}
    if isinstance(data, dict):
        v = v or data.get("verdict")
        idea = idea or data.get("idea")
        narrative = data.get("narrative") or {}
    if not isinstance(v, dict) or not isinstance(v.get("score"), int):
        return None
    return v, idea if isinstance(idea, dict) else {}, narrative if isinstance(narrative, dict) else {}


def metric(v, key):
    m = (v.get("metrics") or {}).get(key)
    val = m.get("value") if isinstance(m, dict) else None
    return val if isinstance(val, (int, float)) and not isinstance(val, bool) else None


def collect(ideas_dir, today):
    out = []
    for folder in sorted(p for p in ideas_dir.iterdir() if p.is_dir()):
        got = load_folder(folder)
        if not got:
            continue
        v, idea, narrative = got
        ev = v.get("evaluated") if DATE_RX.match(str(v.get("evaluated"))) else None
        countries = [c for c in (idea.get("countries") or []) if isinstance(c, str) and re.match(r"^[A-Z]{2}$", c)]
        lc = v.get("launch_country")
        if lc in countries:
            countries = [lc] + [c for c in countries if c != lc]
        r = (v.get("rescue") or [None])[0]
        hist = [{"evaluated": h["evaluated"], "score": h["score"]} for h in (v.get("history") or [])
                if isinstance(h, dict) and DATE_RX.match(str(h.get("evaluated"))) and isinstance(h.get("score"), int)]
        if ev:
            hist.append({"evaluated": ev, "score": v["score"]})
        ks = v.get("kill_shots") or {}
        out.append({
            "slug": v.get("slug") or folder.name, "title": idea.get("title") or v.get("slug") or folder.name,
            "verdict": v.get("verdict"), "score": v["score"],
            "confidence": (v.get("confidence") or {}).get("level"), "evaluated": ev,
            "time_to_first_revenue_weeks": metric(v, "time_to_first_revenue_weeks"),
            "ltv_cac": metric(v, "ltv_cac"), "primary_kill_shot": v.get("primary_kill_shot"),
            "best_rescue": {"change": r["change"], "score_after": r["score_after"], "difficulty": r["difficulty"]}
            if isinstance(r, dict) and {"change", "score_after", "difficulty"} <= set(r) else None,
            "countries": countries, "report": f"{folder.name}/report.html",
            "stale": bool(ev) and (today - datetime.date.fromisoformat(ev)).days > 90,
            "history": hist[-10:],
            "hits": [k for k in KILL_SHOTS if ks.get(k) is True],
            "_checked": [k for k in KILL_SHOTS if ks.get(k) in (True, False)],
            "_folder": folder.name, "_lesson": narrative.get("lesson"),
        })
    out.sort(key=lambda x: (-x["score"], x["time_to_first_revenue_weeks"] if x["time_to_first_revenue_weeks"] is not None else 1e9,
                            -CONF.get(x["confidence"], 0)))
    return out


def patterns(ideas):
    rows = []
    for k in KILL_SHOTS:
        checked = sum(k in x["_checked"] for x in ideas)
        hits = sum(k in x["hits"] for x in ideas)
        if checked:
            rows.append({"kill_shot": k, "hits": hits, "checked": checked})
    return sorted(rows, key=lambda r: (-r["hits"], -r["checked"]))


def load_focus(ideas_dir, slugs):
    f = read_json(ideas_dir / "focus.json")
    if not isinstance(f, dict):
        return None
    if f.get("slug") not in slugs:
        print(f"WARN   focus.json: slug {f.get('slug')!r} is not one of the ideas; focus ignored")
        return None
    keep = {k: str(f[k])[:300] for k in ("slug", "why", "first_action", "deadline", "decided") if f.get(k)}
    return keep


def md(s):
    """Plain text for one Markdown table cell or line: no markers, HTML, links or line breaks."""
    s = re.sub(r"\s+", " ", str(s))
    s = re.sub(r"<!--|-->|kmi:auto", "", s, flags=re.I)
    for ch, rep in (("\\", "\\\\"), ("|", "\\|"), ("<", "&lt;"), (">", "&gt;"), ("[", "\\["), ("]", "\\]"), ("(", "\\("), (")", "\\)"), ("`", "\\`")):
        s = s.replace(ch, rep)
    return s.strip()[:300]


def brain_block(ideas, pats, focus, today):
    L = [f"{START} (generated by kill-my-idea on {today}; edits inside this block are overwritten) -->", ""]
    by_slug = {x["slug"]: x for x in ideas}
    L.append("## Focus this week")
    L.append("")
    if focus:
        x = by_slug[focus["slug"]]
        L.append(f"**{md(x['title'])}**, {md(x['verdict'])} {int(x['score'])}/100 ([report]({md(x['report'])}))")
        for k, label in (("why", "Why"), ("first_action", "First action"), ("deadline", "Deadline")):
            if focus.get(k):
                L.append(f"- {label}: {md(focus[k])}")
    else:
        L.append("No focus picked yet. Run `/kill-my-idea:compare` to choose one.")
    L += ["", f"## All ideas ({len(ideas)})", "",
          "| # | Idea | Verdict | Score | Confidence | Evaluated | Primary kill shot | Best rescue |",
          "|---|------|---------|-------|------------|-----------|-------------------|-------------|"]
    for i, x in enumerate(ideas, 1):
        r = x["best_rescue"]
        rescue = f"{md(r['change'])} → {int(r['score_after'])} ({md(r['difficulty'])})" if r else "none"
        stale = " (stale)" if x["stale"] else ""
        verdict = x["verdict"] if x["verdict"] in ("GO", "PIVOT", "NO-GO") else "unknown"
        conf = x["confidence"] if x["confidence"] in ("high", "medium", "low") else "unknown"
        L.append(f"| {i} | [{md(x['title'])}]({md(x['report'])}) | {verdict} | {int(x['score'])} | "
                 f"{conf} | {x['evaluated'] or 'unknown'}{stale} | "
                 f"{KILL_SHOTS.get(x['primary_kill_shot'], 'none')} | {rescue} |")
    L += ["", "## What keeps killing your ideas", ""]
    hit = [p for p in pats if p["hits"]]
    if hit:
        for p in hit:
            L.append(f"- {KILL_SHOTS[p['kill_shot']]}: hit in {p['hits']} of {p['checked']} ideas checked")
        top = hit[0]
        if top["hits"] >= 2:
            L += ["", f"Check **{KILL_SHOTS[top['kill_shot']].lower()}** first on your next idea: "
                      f"it hit {top['hits']} of your {len(ideas)} ideas."]
    else:
        L.append("No kill shot has hit yet.")
    moved = [x for x in ideas if len(x["history"]) > 1]
    if moved:
        L += ["", "## Score changes", ""]
        for x in moved:
            h = x["history"]
            L.append(f"- {md(x['title'])}: " + " → ".join(str(e["score"]) for e in h)
                     + f" ({h[0]['evaluated']} → {h[-1]['evaluated']})")
    lessons = [x for x in ideas if isinstance(x["_lesson"], str) and x["_lesson"].strip()]
    if lessons:
        L += ["", "## Lessons", ""]
        for x in lessons:
            L.append(f"- {md(x['title'])}: {md(x['_lesson'])}")
    L += ["", END]
    return "\n".join(L) + "\n"


def write_brain(path, block):
    if path.exists():
        text = path.read_text(encoding="utf-8")
        a = text.find(START)
        b = text.rfind(END)  # the real end is the last marker: titles can't contain one (md strips it)
        if a != -1 and b > a:
            text = text[:a] + block + text[b + len(END):].lstrip("\n")
        else:
            text = text.rstrip("\n") + "\n\n" + block
    else:
        text = BRAIN_HEAD + block + BRAIN_TAIL
    path.write_text(text, encoding="utf-8")


def main(argv):
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    brain = "--no-brain" not in argv
    argv = [a for a in argv if a != "--no-brain"]
    ideas_dir = pathlib.Path(argv[0]) if argv else pathlib.Path("ideas")
    if not ideas_dir.is_dir():
        print(f"{ideas_dir}: not a folder")
        return 1
    today = datetime.date.today()
    ideas = collect(ideas_dir, today)
    if not ideas:
        print(f"no verdict under {ideas_dir}/*/ (run /kill-my-idea:kill first)")
        return 1
    pats = patterns(ideas)
    focus = load_focus(ideas_dir, {x["slug"] for x in ideas})
    board = {"schema_version": "1.0", "generated": today.isoformat(), "brain": brain, "focus": focus, "patterns": pats,
             "ideas": [{k: v for k, v in x.items() if not k.startswith("_")} for x in ideas]}
    payload = json.dumps(board, ensure_ascii=False).replace("<", "\\u003c")
    (ideas_dir / "board-data.js").write_text(f"window.KMI_BOARD = {payload};\n", encoding="utf-8")
    shutil.copyfile(BOARD_HTML, ideas_dir / "board.html")
    if brain:
        write_brain(ideas_dir / "BRAIN.md", brain_block(ideas, pats, focus, today.isoformat()))
    print(f"{len(ideas)} ideas -> {ideas_dir}/board.html, board-data.js" + (", BRAIN.md" if brain else "")
          + (f" (focus: {focus['slug']})" if focus else " (no focus.json yet)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
