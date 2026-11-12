#!/usr/bin/env python3
"""Check a full /kill-my-idea:nuke run (nuke.json) and write NUKE.md, the one page that ties it together.

    python3 scripts/nuke-kit.py ideas/<folder>           check, write NUKE.md, add the Full run summary to the report
    python3 scripts/nuke-kit.py --check ideas/<folder>   check only

nuke.json lists the six steps in order (kill, deepdive, fix, validate, build, share) with
done / skipped / stopped and why. The script holds the run to its rules: deepdive runs only when
kill scored a PIVOT (50-69); fix runs unless the idea is already a GO; when the fixed idea still
projects under 50 the run stops there unless the founder chose to go on; every step marked done
must have its file, and that file must pass its own checker. Stdlib only.
"""
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fk, vk, sk = _load("fix-kit"), _load("validate-kit"), _load("share-kit")
Report, text = fk.Report, fk.text
ORDER = ["kill", "deepdive", "fix", "validate", "build", "share"]
STATUS = {"done", "skipped", "stopped"}
FILES = {"kill": "verdict.json", "deepdive": "verdict.json", "fix": "fix.json", "validate": "validate.json",
         "build": "build/plan.json", "share": "share.json"}
STOP_BELOW = 50


def script_ok(name, folder, *extra):
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / name), *extra, str(folder)],
                       capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]


def check_nuke(nuke, folder, verdict, rep):
    if nuke.get("schema_version") != "1.0":
        rep.error('schema_version: must be "1.0"')
    if nuke.get("slug") != verdict.get("slug"):
        rep.error(f"slug: {nuke.get('slug')!r} is not the verdict's {verdict.get('slug')!r}")
    steps = nuke.get("steps") or []
    names = [s.get("step") for s in steps]
    if names != ORDER:
        rep.error(f"steps: all six, in this order: {', '.join(ORDER)}")
        return {}
    st = {s["step"]: s for s in steps}
    for s in steps:
        if s.get("status") not in STATUS:
            rep.error(f"steps.{s['step']}.status: done, skipped or stopped")
        if s.get("status") != "done":
            text(rep, f"steps.{s['step']}.why", s.get("why"), 200)
    ks = nuke.get("kill_score")
    if not isinstance(ks, int) or not 0 <= ks <= 100:
        rep.error("kill_score: the score kill gave, before any deepdive (0-100)")
        return st
    if st["kill"].get("status") != "done":
        rep.error("steps.kill: every nuke starts with a kill")
    want_deep = 50 <= ks <= 69
    if want_deep and st["deepdive"].get("status") != "done":
        rep.error(f"steps.deepdive: kill scored {ks} (PIVOT), so deepdive runs")
    if not want_deep and st["deepdive"].get("status") == "done":
        rep.error(f"steps.deepdive: kill scored {ks}; deepdive runs only for a PIVOT (50-69)")
    if st["deepdive"].get("status") != "done" and verdict.get("score") != ks:
        rep.error(f"kill_score: {ks}, but verdict.json says {verdict.get('score')} and no deepdive ran")
    if st["deepdive"].get("status") == "done" and verdict.get("mode") != "deepdive":
        rep.error("steps.deepdive: marked done, but verdict.json is not a deepdive verdict")
    is_go = verdict.get("verdict") == "GO"
    if not is_go and st["fix"].get("status") != "done":
        rep.error("steps.fix: the idea isn't a GO, so fix runs")
    # the stop rule
    fix = None
    if st["fix"].get("status") == "done" and (folder / "fix.json").exists():
        fix = json.loads((folder / "fix.json").read_text(encoding="utf-8"))
        after = ((fix.get("fixed") or {}).get("score"))
        if isinstance(after, int) and after < STOP_BELOW:
            cont = nuke.get("continued_past_stop")
            if cont is not True:
                for k in ("validate", "build", "share"):
                    if st[k].get("status") != "stopped":
                        rep.error(f"steps.{k}: the fixed idea projects to {after} (under {STOP_BELOW}), so the run "
                                  "stops after fix unless the founder chose to go on (continued_past_stop: true)")
            else:
                text(rep, "continued_why", nuke.get("continued_why"), 200)
    if nuke.get("continued_past_stop") is True and not (fix and (fix.get("fixed") or {}).get("score", 100) < STOP_BELOW):
        rep.error("continued_past_stop: only when the fixed score is under 50")
    seen_stop = False
    for k in ORDER:
        if st[k].get("status") == "stopped":
            seen_stop = True
        elif seen_stop:
            rep.error(f"steps.{k}: comes after a stopped step, so it is stopped too")
    # every done step has its file, and the file passes its checker
    for k in ORDER:
        if st[k].get("status") != "done":
            continue
        if not (folder / FILES[k]).exists():
            rep.error(f"steps.{k}: done, but {FILES[k]} is missing")
            continue
        sub = Report()
        if k == "kill":
            ok, last = script_ok("check-idea.py", folder)
            if not ok:
                rep.error(f"steps.kill: check-idea.py fails ({last[0]})")
        elif k == "fix":
            fk.check_fix(fix, verdict, sub)
        elif k == "validate":
            vk.check_validate(json.loads((folder / "validate.json").read_text(encoding="utf-8")), verdict, sub)
        elif k == "build":
            ok, last = script_ok("build-kit.py", folder, "--check")
            if not ok:
                rep.error(f"steps.build: build-kit.py --check fails ({last[0]})")
        elif k == "share":
            sk.check_share(json.loads((folder / "share.json").read_text(encoding="utf-8")), verdict, sub,
                           sk.known_scores(folder, verdict))
        for x in sub.errors:
            rep.error(f"steps.{k}: {FILES[k]}: {x}")
    for k, lim in (("cost_usd", 100), ("minutes", 600)):
        v = nuke.get(k)
        if v is not None and (isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 <= v <= lim):
            rep.error(f"{k}: a number from 0 to {lim}, or null")
    return st


def read(folder, name):
    p = folder / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def summary(nuke, folder, verdict):
    """What the report's Full run section and NUKE.md show."""
    out = {"kill_score": nuke["kill_score"], "score": verdict["score"], "verdict": verdict["verdict"],
           "steps": [{k: s.get(k) for k in ("step", "status", "why")} for s in nuke["steps"]],
           "cost_usd": nuke.get("cost_usd"), "minutes": nuke.get("minutes")}
    done = {s["step"] for s in nuke["steps"] if s["status"] == "done"}
    if "fix" in done:
        f = read(folder, "fix.json")
        out["fix"] = {"summary": f["summary"], "score_after": f["fixed"]["score"], "reachable": f["reachable"]}
    if "validate" in done:
        v = read(folder, "validate.json")
        out["validate"] = {"hypothesis": v["hypothesis"], "targets": len(v["targets"]),
                           "validated": (v.get("results") or {}).get("rescored", {}).get("score")}
    if "build" in done:
        p = read(folder, "build/plan.json")
        out["build"] = {"name": p["product"]["name"], "one_liner": p["product"]["one_liner"],
                        "key_metric": p["product"].get("key_metric", {}).get("name")}
    if "share" in done:
        out["share"] = [x["place"] for x in read(folder, "share.json")["posts"]]
    return out


def nuke_md(s, verdict):
    lines = [f"# Full run: {verdict['verdict']} {verdict['score']}/100", ""]
    if s["kill_score"] != s["score"]:
        lines.append(f"Kill scored {s['kill_score']}; the deepdive moved it to {s['score']}.")
    else:
        lines.append(f"Kill scored {s['kill_score']}.")
    if s.get("minutes") or s.get("cost_usd"):
        lines.append(f"Run: {s.get('minutes') or '?'} minutes, about ${s.get('cost_usd') or '?'} of plan usage.")
    lines += ["", "| Step | Status | Why / where |", "|---|---|---|"]
    where = {"kill": "report.html", "deepdive": "report.html", "fix": "fix.md, report.html#fix",
             "validate": "validate/ (landing, interview, outreach, tracker)", "build": "build/BUILD.md",
             "share": "share/posts.md, share/card.svg"}
    for st in s["steps"]:
        lines.append(f"| {st['step']} | {st['status']} | {st.get('why') or where[st['step']]} |")
    lines.append("")
    if s.get("fix"):
        f = s["fix"]
        lines += ["## Path to GO", "", f"{f['summary']}", "",
                  f"Projected: {verdict['score']} → {f['score_after']}"
                  f"{'' if f['reachable'] else ' (GO out of reach)'}.", ""]
    if s.get("validate"):
        v = s["validate"]
        lines += ["## The 7-day test", "", f"Hypothesis: {v['hypothesis']}", "",
                  f"{v['targets']} targets in validate/tracker.csv. "
                  + (f"Validated score: {v['validated']}." if v.get("validated") is not None else
                     "Run the test, fill in the tracker, then `/kill-my-idea:validate --results`."), ""]
    if s.get("build"):
        b = s["build"]
        lines += ["## The starter kit", "", f"**{b['name']}**: {b['one_liner']}", "",
                  f"Key metric: {b.get('key_metric') or 'see BUILD.md'}. Start at build/BUILD.md.", ""]
    if s.get("share"):
        lines += ["## Posts", "", "Drafts for " + ", ".join(s["share"]) + " in share/posts.md. Nothing was posted.", ""]
    lines += ["Nothing was published, bought or sent during this run.", ""]
    return "\n".join(lines)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    rep = Report()
    nuke, verdict = fk.load(folder / "nuke.json", rep), fk.load(folder / "verdict.json", rep)
    if nuke is not None and verdict is not None:
        check_nuke(nuke, folder, verdict, rep)
    if rep.errors:
        for x in rep.errors:
            print(f"error: {x}")
        print(f"FAIL {folder}: {len(rep.errors)} error(s)")
        return 1
    done = [s["step"] for s in nuke["steps"] if s["status"] == "done"]
    line = f"{verdict['verdict']} {verdict['score']}, steps done: {', '.join(done)}"
    if "--check" in argv:
        print(f"OK {folder}/nuke.json: {line}")
        return 0
    s = summary(nuke, folder, verdict)
    (folder / "NUKE.md").write_text(nuke_md(s, verdict), encoding="utf-8")
    data_path = folder / "report-data.json"
    if data_path.exists():
        data = json.loads(data_path.read_text(encoding="utf-8"))
        data.setdefault("narrative", {})["nuke"] = s
        data_path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-report.py"), str(folder)], check=True,
                       stdout=subprocess.DEVNULL)
    print(f"OK {folder}: {line}; NUKE.md written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
