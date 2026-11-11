#!/usr/bin/env python3
"""Check fix.json (the path to GO) against the verdict, then put it in the report.

    python3 scripts/fix-kit.py ideas/<folder>           check, add narrative.fix, rebuild report.html
    python3 scripts/fix-kit.py --check ideas/<folder>   check only

The model writes fix.json: the levers (price, features, customer, channel…), each with the
sub-scores it moves and its prerequisites, and the fixed idea's 21 sub-scores. This script
re-scores the fixed idea with the same formula and rules as check-idea.py, refuses any sub-score
that changed without a lever, computes how many points each lever adds and where the points are
lost, then writes a summary into report-data.json (narrative.fix). verdict.json is never touched:
a fixed score is a projection, not a verdict. Stdlib only.
"""
import copy
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check_idea", ROOT / "scripts" / "check-idea.py")
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)

KINDS = {"price", "features", "customer", "channel", "model", "country", "cost", "other"}
PREREQ = {"skill", "money", "time", "partner", "legal", "data", "audience"}
HAVE = {"yes", "no", "unknown"}
POSITIONS = {"undercut", "match", "premium"}
DIFFICULTY = {"doable", "hard", "very-hard"}
LEVER_ID = re.compile(r"^L\d{1,2}$")
UNSAFE = re.compile(r"<\s*/?\s*(script|iframe|object|embed|style)|javascript:|data:text/html", re.I)
SUB_OF = {s: c for c, subs in chk.SUBS.items() for s in subs}
GO = 70


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def legacy(self, what):
        self.errors.append(f"fix.json fixed: {what} is required")


def text(rep, where, val, max_len=300, required=True):
    if val in (None, ""):
        if required:
            rep.error(f"{where}: missing")
        return
    if not isinstance(val, str):
        rep.error(f"{where}: must be a string")
    elif len(val) > max_len:
        rep.error(f"{where}: {len(val)} characters, at most {max_len}")
    elif UNSAFE.search(val):
        rep.error(f"{where}: markup or a script URL; plain text only")


def url(rep, where, val):
    if not isinstance(val, str) or not re.match(r"^https?://", val):
        rep.error(f"{where}: needs an http(s) source URL")


def sub_score(cd, sub):
    return ((cd.get(SUB_OF[sub]) or {}).get(sub) or {}).get("score")


def points(sub, score):
    """Points a sub-score is worth in the total: weight × score / 15."""
    return chk.WEIGHTS[SUB_OF[sub]] * score / 15


def gaps(verdict):
    """Where the points are lost, biggest first."""
    out = []
    for sub, c in SUB_OF.items():
        sc = sub_score(verdict.get("criteria_detail") or {}, sub)
        if isinstance(sc, (int, float)) and sc < 5:
            out.append({"criterion": c, "sub": sub, "score": sc,
                        "points_lost": round(points(sub, 5 - sc), 1)})
    return sorted(out, key=lambda g: -g["points_lost"])


def check_pricing(rep, fix):
    p = fix.get("pricing") or {}
    comps = p.get("competitors") or []
    if len(comps) < 3:
        rep.error("pricing.competitors: at least 3, from their pricing pages")
    for i, c in enumerate(comps):
        text(rep, f"pricing.competitors[{i}].name", c.get("name"), 60)
        chk_num(rep, f"pricing.competitors[{i}].amount", c.get("amount"))
        text(rep, f"pricing.competitors[{i}].period", c.get("period"), 20)
        url(rep, f"pricing.competitors[{i}].source", c.get("source"))
    rec = p.get("recommended") or {}
    chk_num(rep, "pricing.recommended.amount", rec.get("amount"))
    text(rep, "pricing.recommended.period", rec.get("period"), 20)
    text(rep, "pricing.recommended.why", rec.get("why"), 300)
    pos = rec.get("position")
    if pos not in POSITIONS:
        rep.error("pricing.recommended.position: undercut, match or premium")
        return
    same = [c["amount"] for c in comps if c.get("period") == rec.get("period")
            and isinstance(c.get("amount"), (int, float))]
    a = rec.get("amount")
    if len(same) >= 2 and isinstance(a, (int, float)):
        lo, hi = min(same), max(same)
        wrong = (pos == "undercut" and a >= lo) or (pos == "premium" and a <= hi) or \
                (pos == "match" and not lo <= a <= hi)
        if wrong:
            rep.error(f"pricing.recommended: {a} is not '{pos}' against competitors at {lo}–{hi} per {rec.get('period')}")


def chk_num(rep, where, val):
    if isinstance(val, bool) or not isinstance(val, (int, float)) or val < 0:
        rep.error(f"{where}: a number, 0 or more")


def check_features(rep, fix):
    f = fix.get("features") or {}
    must = f.get("must") or []
    if not 1 <= len(must) <= 8:
        rep.error("features.must: 1 to 8")
    for i, x in enumerate(must):
        text(rep, f"features.must[{i}].feature", x.get("feature"), 100)
        text(rep, f"features.must[{i}].why", x.get("why"), 200)
        url(rep, f"features.must[{i}].source", x.get("source"))
    for i, x in enumerate(f.get("cut") or []):
        text(rep, f"features.cut[{i}].feature", x.get("feature"), 100)
        text(rep, f"features.cut[{i}].why", x.get("why"), 200)
    d = f.get("differentiator") or {}
    text(rep, "features.differentiator.feature", d.get("feature"), 100)
    text(rep, "features.differentiator.why", d.get("why"), 200)
    url(rep, "features.differentiator.source", d.get("source"))


def check_levers(rep, fix, verdict):
    """Returns {sub: (from, to, lever id)} for every move."""
    levers = fix.get("levers") or []
    if not 1 <= len(levers) <= 6:
        rep.error("levers: 1 to 6")
    vcd = verdict.get("criteria_detail") or {}
    vks = verdict.get("kill_shots") or {}
    moves, ids = {}, set()
    for i, lv in enumerate(levers):
        w = f"levers[{i}]"
        lid = lv.get("id")
        if not LEVER_ID.match(str(lid)) or lid in ids:
            rep.error(f"{w}.id: unique, like L1")
        ids.add(lid)
        if lv.get("kind") not in KINDS:
            rep.error(f"{w}.kind: one of {sorted(KINDS)}")
        if lv.get("difficulty") not in DIFFICULTY:
            rep.error(f"{w}.difficulty: doable, hard or very-hard")
        for k, n in (("change", 200), ("evidence", 300), ("effort", 60), ("cost", 80)):
            text(rep, f"{w}.{k}", lv.get(k), n)
        url(rep, f"{w}.source", lv.get("source"))
        if not lv.get("moves") and not lv.get("clears"):
            rep.error(f"{w}: moves no sub-score and clears no kill shot")
        for j, m in enumerate(lv.get("moves") or []):
            sub = m.get("sub")
            if sub not in SUB_OF:
                rep.error(f"{w}.moves[{j}].sub: {sub!r} is not one of the 21 sub-scores")
                continue
            if m.get("from") != sub_score(vcd, sub):
                rep.error(f"{w}.moves[{j}]: {sub} from {m.get('from')} but the verdict has {sub_score(vcd, sub)}")
            if sub in moves:
                rep.error(f"{w}.moves[{j}]: {sub} is already moved by {moves[sub][2]}; one lever per sub-score")
            moves[sub] = (m.get("from"), m.get("to"), lid)
            text(rep, f"{w}.moves[{j}].why", m.get("why"), 200)
        for k in lv.get("clears") or []:
            if vks.get(k) is not True:
                rep.error(f"{w}.clears: {k!r} did not hit in the verdict")
        pre = lv.get("prerequisites") or []
        if not pre:
            rep.error(f"{w}.prerequisites: at least 1 (what it takes to make this change)")
        for j, x in enumerate(pre):
            text(rep, f"{w}.prerequisites[{j}].what", x.get("what"), 160)
            if x.get("kind") not in PREREQ:
                rep.error(f"{w}.prerequisites[{j}].kind: one of {sorted(PREREQ)}")
            if x.get("have") not in HAVE:
                rep.error(f"{w}.prerequisites[{j}].have: yes, no or unknown")
            text(rep, f"{w}.prerequisites[{j}].cost", x.get("cost"), 80, required=False)
    return moves


def rescore(rep, fix, verdict, moves):
    """Re-score the fixed idea with check-idea.py's own rules."""
    fx = fix.get("fixed") or {}
    cd = fx.get("criteria_detail") or {}
    vcd = verdict.get("criteria_detail") or {}
    for sub in SUB_OF:
        before, after = sub_score(vcd, sub), sub_score(cd, sub)
        if sub in moves:
            if after != moves[sub][1]:
                rep.error(f"fixed.{sub}: {after} but lever {moves[sub][2]} moves it to {moves[sub][1]}")
        elif after != before:
            rep.error(f"fixed.{sub}: {before} → {after} with no lever; every change needs a lever")
    vks = verdict.get("kill_shots") or {}
    fks = fx.get("kill_shots") or {}
    cleared = {k for lv in fix.get("levers") or [] for k in lv.get("clears") or []}
    for k in chk.KILL_SHOTS:
        if vks.get(k) is True and fks.get(k) is not True and k not in cleared:
            rep.error(f"fixed.kill_shots.{k}: no longer hits, but no lever clears it")
        if vks.get(k) is not True and fks.get(k) is True:
            rep.warn(f"fixed.kill_shots.{k}: a fix introduces a new kill shot")
    pseudo = copy.deepcopy(verdict)
    pseudo.update({k: fx.get(k) for k in ("criteria_detail", "kill_shots", "rules_applied", "score", "score_raw",
                                          "verdict")})
    if isinstance((fx.get("metrics") or {}).get("ltv_cac"), dict):
        pseudo.setdefault("metrics", {})["ltv_cac"] = fx["metrics"]["ltv_cac"]
    pseudo["criteria"] = {c: round(sum(sub_score(cd, s) or 0 for s in subs) / 3 * 2) / 2
                          for c, subs in chk.SUBS.items()}
    sub_rep = Report()
    chk.check_scores(sub_rep, pseudo)
    for e in sub_rep.errors:
        rep.error("fixed: " + e.replace("verdict.json: ", ""))
    score = fx.get("score")
    if isinstance(score, int):
        if fix.get("reachable") is not (score >= GO):
            rep.error(f"reachable: must be {score >= GO} for a projected score of {score}")
        if score < GO and not fix.get("blockers"):
            rep.error("blockers: GO is out of reach, so say what blocks it (at least 1)")
    for i, b in enumerate(fix.get("blockers") or []):
        text(rep, f"blockers[{i}]", b, 200)


def check_fix(fix, verdict, rep):
    if fix.get("schema_version") != "1.0":
        rep.error('schema_version: must be "1.0"')
    if fix.get("slug") != verdict.get("slug"):
        rep.error(f"slug: {fix.get('slug')!r} is not the verdict's {verdict.get('slug')!r}")
    b = fix.get("based_on") or {}
    if b.get("verdict") != verdict.get("verdict") or b.get("score") != verdict.get("score"):
        rep.error("based_on: must copy the verdict's verdict and score")
    text(rep, "summary", fix.get("summary"), 200)
    check_pricing(rep, fix)
    check_features(rep, fix)
    moves = check_levers(rep, fix, verdict)
    rescore(rep, fix, verdict, moves)
    plan = fix.get("plan") or []
    if not 3 <= len(plan) <= 7:
        rep.error("plan: 3 to 7 steps")
    for i, s in enumerate(plan):
        text(rep, f"plan[{i}].when", s.get("when"), 30)
        text(rep, f"plan[{i}].step", s.get("step"), 200)
        text(rep, f"plan[{i}].verify", s.get("verify"), 160)
    kc = fix.get("kill_criteria") or []
    if not kc:
        rep.error("kill_criteria: at least 1, with a number and a date")
    for i, k in enumerate(kc):
        text(rep, f"kill_criteria[{i}]", k, 200)
        if isinstance(k, str) and not re.search(r"\d", k):
            rep.error(f"kill_criteria[{i}]: needs a number")


def rule_ids(rules):
    return [r.get("rule") if isinstance(r, dict) else r for r in rules or []]


def narrative(fix, verdict):
    """The report section's data: copied from fix.json, plus points the script computes."""
    levers = []
    for lv in fix["levers"]:
        gain = sum(points(m["sub"], m["to"] - m["from"]) for m in lv.get("moves") or [])
        levers.append({k: lv.get(k) for k in ("id", "kind", "change", "evidence", "source", "difficulty", "effort",
                                             "cost", "clears", "prerequisites")} |
                      {"points": round(gain, 1), "moves": lv.get("moves") or []})
    fx = fix["fixed"]
    return {"summary": fix["summary"], "score_before": verdict["score"], "score_after": fx["score"],
            "verdict_after": fx["verdict"], "reachable": fix["reachable"], "blockers": fix.get("blockers") or [],
            "rules_after": rule_ids(fx.get("rules_applied")),
            "rules_lifted": [r for r in rule_ids(verdict.get("rules_applied")) if r not in rule_ids(fx.get("rules_applied"))],
            "gaps": gaps(verdict)[:6], "levers": levers, "pricing": fix["pricing"], "features": fix["features"],
            "plan": fix["plan"], "kill_criteria": fix["kill_criteria"]}


def load(path, rep):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        rep.error(f"{path}: not found")
    except json.JSONDecodeError as e:
        rep.error(f"{path}: not valid JSON ({e})")
    return None


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    rep = Report()
    fix, verdict = load(folder / "fix.json", rep), load(folder / "verdict.json", rep)
    if fix is not None and verdict is not None:
        check_fix(fix, verdict, rep)
    for w in rep.warnings:
        print(f"warning: {w}")
    if rep.errors:
        for e in rep.errors:
            print(f"error: {e}")
        print(f"FAIL {folder}: {len(rep.errors)} error(s)")
        return 1
    fx = fix["fixed"]
    line = (f"{verdict['score']} {verdict['verdict']} → {fx['score']} {fx['verdict']} (projected)"
            f"{'' if fix['reachable'] else ', GO out of reach'}")
    if "--check" in argv:
        print(f"OK {folder}/fix.json: {line}")
        return 0
    data_path = folder / "report-data.json"
    if data_path.exists():
        data = json.loads(data_path.read_text(encoding="utf-8"))
        data.setdefault("narrative", {})["fix"] = narrative(fix, verdict)
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-report.py"), str(folder)], check=True,
                       stdout=subprocess.DEVNULL)
        print(f"OK {folder}: {line}; report.html has the Path to GO section")
    else:
        print(f"OK {folder}: {line}; no report-data.json, so no report section")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
