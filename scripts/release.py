#!/usr/bin/env python3
"""Check that a release is ready before anything is tagged or pushed.

    python3 scripts/release.py --check 1.0.0

Verifies, and prints PASS / FAIL for each:
- .claude-plugin/plugin.json has this version, and CHANGELOG.md has a "## <version>" entry;
- the CSP hashes are pinned and the template scan passes;
- the unit tests pass, and the legacy examples still pass the checker in --legacy mode;
- git: on main, nothing uncommitted, HEAD pushed to origin/main, and no tag v<version> yet
  (locally or on origin). A tag on the wrong commit is the mistake this exists to stop.
Exit code 1 when anything fails. It never tags or pushes; it prints the commands to run.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def run(*cmd, cwd=ROOT):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main(argv):
    if len(argv) != 2 or argv[0] != "--check" or not re.match(r"^\d+\.\d+\.\d+$", argv[1]):
        print(__doc__)
        return 2
    ver, tag = argv[1], f"v{argv[1]}"
    results = []

    def check(name, ok, detail=""):
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f": {detail}" if detail and not ok else ""))

    pj = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    check("plugin.json version", pj.get("version") == ver, f"is {pj.get('version')}")
    cl = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    check("CHANGELOG entry", re.search(rf"^## {re.escape(ver)}\b", cl, re.M) is not None, f"no '## {ver}' heading")
    code, out = run(sys.executable, "scripts/update-csp.py", "--check")
    check("CSP pinned", code == 0, out[-200:])
    code, out = run(sys.executable, "scripts/scan-report.py")
    check("template scan", code == 0, out[-200:])
    code, out = run(sys.executable, "-m", "unittest", "-q", cwd=ROOT / "tests")
    check("unit tests", code == 0, out[-300:])
    bad = []
    for d in sorted((ROOT / "examples").glob("*-report")):
        code, out = run(sys.executable, "scripts/check-idea.py", "--legacy", str(d))
        if code:
            bad.append(d.name)
    check("examples pass the checker", not bad, ", ".join(bad))
    _, branch = run("git", "rev-parse", "--abbrev-ref", "HEAD")
    check("on main", branch == "main", f"on {branch}")
    _, dirty = run("git", "status", "--porcelain")
    check("nothing uncommitted", dirty == "", f"{len(dirty.splitlines())} changed files")
    run("git", "fetch", "-q", "origin")
    _, head = run("git", "rev-parse", "HEAD")
    _, remote = run("git", "rev-parse", "origin/main")
    check("HEAD pushed to origin/main", head == remote, "push first")
    code, _ = run("git", "rev-parse", "-q", "--verify", f"refs/tags/{tag}")
    _, remote_tags = run("git", "ls-remote", "--tags", "origin", tag)
    check(f"tag {tag} is free", code != 0 and not remote_tags.strip(), "it already exists: never move a published tag")
    if all(results):
        print(f"\nReady. Tag this exact commit ({head[:7]}) and release:\n"
              f"  git tag {tag} {head[:7]} && git push origin {tag}\n"
              f"  gh release create {tag} --notes-file <(awk '/^## {ver}/{{f=1;next}}/^## /{{f=0}}f' CHANGELOG.md)")
        return 0
    print(f"\nNot ready: {results.count(False)} check(s) failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
