#!/usr/bin/env python3
"""See whether the score tells ideas apart, across many verdicts.

    python3 scripts/calibrate.py docs/gallery [ideas ...]
    python3 scripts/calibrate.py calibration --outcomes calibration/outcomes.json

Prints, for every idea folder found (a folder with verdict.json or report data):
- the score distribution (min, median, max, standard deviation, 10-point bins, verdict counts);
- how many scores sit exactly on a cap (49 from R6, 69 from R2);
- how often each fixed rule fired and each kill shot hit. A kill shot that hits more than 2 of
  every 3 ideas no longer tells them apart, and is flagged.

With --outcomes, a JSON object {"<slug>": "worked" | "failed"}, it also checks the 1.0
calibration targets: the ideas that worked score a median of 60 or more, the failures a median
under 50, and at least one idea reaches GO. Exit code 1 when a target is missed.
--weights '{"feasibility": 15, ...}' recomputes every score with other weights (what if?).
Python stdlib only.
"""
import argparse
import importlib.util
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chk, brain = _load("check-idea"), _load("build-brain")


def verdicts(roots):
    out = []
    for root in roots:
        for folder in sorted(p for p in pathlib.Path(root).iterdir() if p.is_dir()):
            got = brain.load_folder(folder)
            if got:
                out.append(got[0])
    return out


def rescore(v, weights):
    """The score with other weights, the same rounding and the same total caps (R2, R6)."""
    cd = v.get("criteria_detail")
    if not isinstance(cd, dict):
        return None
    total = 0
    for c, w in weights.items():
        subs = [cd.get(c, {}).get(s, {}).get("score") for s in chk.SUBS[c]]
        if not all(isinstance(x, (int, float)) for x in subs):
            return None
        total += w * (sum(subs) / 3) / 5
    total = total * 100 / sum(weights.values())
    score = chk.round_half_up(total)
    ks = v.get("kill_shots") or {}
    lc = ((v.get("metrics") or {}).get("ltv_cac") or {}).get("value")
    if ks.get("no_distribution") is True:
        score = min(score, 69)
        if isinstance(lc, (int, float)) and lc < 1:
            score = min(score, 49)
    return score


def report(vs, weights=None):
    scores = [rescore(v, weights) if weights else v["score"] for v in vs]
    pairs = [(v, s) for v, s in zip(vs, scores) if s is not None]
    scores = [s for _, s in pairs]
    if not scores:
        print("no verdicts found")
        return {}
    n = len(scores)
    print(f"{n} verdicts" + (" (rescored with the --weights given)" if weights else ""))
    print(f"score  min {min(scores)}  median {statistics.median(scores):g}  max {max(scores)}  stdev {statistics.pstdev(scores):.1f}")
    bands = {b: sum(chk.band(s) == b for s in scores) for b in ("GO", "PIVOT", "NO-GO")}
    print("verdicts  " + "  ".join(f"{b} {c}" for b, c in bands.items()))
    for lo in range(0, 100, 10):
        c = sum(lo <= s < lo + 10 or (lo == 90 and s == 100) for s in scores)
        if c:
            print(f"  {lo:2d}-{lo + 9:2d} {'#' * c} {c}")
    r6 = sum(any((r.get("rule") if isinstance(r, dict) else r) == "R6_unprofitable_no_channel" for r in v.get("rules_applied") or []) for v, _ in pairs)
    print(f"exactly 49: {scores.count(49)} (capped there by R6: {r6}) · exactly 69: {scores.count(69)}")
    rules = {}
    for v, _ in pairs:
        for r in v.get("rules_applied") or []:
            rid = r.get("rule") if isinstance(r, dict) else r
            rules[rid] = rules.get(rid, 0) + 1
    print("rules fired: " + (", ".join(f"{k} {c}/{n}" for k, c in sorted(rules.items(), key=lambda x: -x[1])) or "none"))
    print("kill shots (hit / checked):")
    flagged = []
    for k in chk.KILL_SHOTS:
        hit = sum((v.get("kill_shots") or {}).get(k) is True for v, _ in pairs)
        checked = sum((v.get("kill_shots") or {}).get(k) in (True, False) for v, _ in pairs)
        too = checked >= 6 and hit * 3 > checked * 2
        flagged += [k] if too else []
        print(f"  {k:22s} {hit:3d}/{checked:<3d}" + ("  <- hits more than 2 in 3: no longer tells ideas apart" if too else ""))
    return {"scores": dict((v.get("slug"), s) for v, s in pairs), "flagged": flagged, "bands": bands}


def targets(res, outcomes):
    worked = [s for slug, s in res["scores"].items() if outcomes.get(slug) == "worked"]
    failed = [s for slug, s in res["scores"].items() if outcomes.get(slug) == "failed"]
    missing = [s for s in outcomes if s not in res["scores"]]
    ok = True
    print("\ncalibration targets:")
    if missing:
        print(f"  missing verdicts for: {', '.join(missing)}")
        ok = False
    for name, vals, test, goal in (("worked", worked, lambda m: m >= 60, "median >= 60"),
                                   ("failed", failed, lambda m: m < 50, "median < 50")):
        if not vals:
            print(f"  {name}: no verdicts")
            ok = False
            continue
        m = statistics.median(vals)
        good = test(m)
        ok &= good
        print(f"  {name:6s} median {m:g} ({goal})  {'PASS' if good else 'FAIL'}  scores {sorted(vals)}")
    go = res["bands"]["GO"] >= 1
    ok &= go
    print(f"  at least one GO: {'PASS' if go else 'FAIL'}")
    return ok


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("roots", nargs="+", type=pathlib.Path)
    ap.add_argument("--outcomes", type=pathlib.Path)
    ap.add_argument("--weights")
    a = ap.parse_args(argv)
    weights = None
    if a.weights:
        weights = dict(chk.WEIGHTS)
        weights.update(json.loads(a.weights))
    res = report(verdicts(a.roots), weights)
    if a.outcomes and res:
        return 0 if targets(res, json.loads(a.outcomes.read_text(encoding="utf-8"))) else 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
