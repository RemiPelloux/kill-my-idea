#!/usr/bin/env python3
"""Upgrade idea folders to the 1.0 file format.

    python3 scripts/migrate.py ideas/2026-11-my-idea [more folders...]
    python3 scripts/migrate.py --all [ideas]          # every ideas/*/ folder
    python3 scripts/migrate.py --dry-run --all

A folder is upgraded only when it already passes check-idea.py under today's rules (0.7+
verdicts usually do): then `schema_version` is added to idea.json, verdict.json and
report-data.js, and nothing else changes. A folder that fails is left untouched and listed as
"re-run needed": its verdict was made under older rules, and a new run is the only honest fix.
Python stdlib only.
"""
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("check_idea", HERE / "check-idea.py")
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)
VERSION = chk.SCHEMA_VERSION
DATA_RX = re.compile(r"^\s*window\.KMI_DATA\s*=\s*(\{.*\})\s*;?\s*$", re.S)


def stamp(obj):
    """schema_version first, the rest unchanged."""
    if not isinstance(obj, dict):
        return obj
    out = {"schema_version": VERSION}
    out.update({k: v for k, v in obj.items() if k != "schema_version"})
    return out


def migrate(folder, dry):
    rep = chk.check_folder(folder)
    if rep.errors:
        return f"re-run needed ({len(rep.errors)} errors under today's rules, e.g. {rep.errors[0][:90]})"
    v = json.loads((folder / "verdict.json").read_text(encoding="utf-8")) if (folder / "verdict.json").exists() else None
    if v is not None and v.get("schema_version") == VERSION:
        return "already 1.0"
    if dry:
        return "would upgrade"
    for name in ("idea.json", "verdict.json"):
        p = folder / name
        if p.exists():
            p.write_text(json.dumps(stamp(json.loads(p.read_text(encoding="utf-8"))), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rd = folder / "report-data.js"
    if rd.exists():
        data = json.loads(DATA_RX.match(rd.read_text(encoding="utf-8").lstrip("﻿")).group(1))
        data = stamp(data)
        data["idea"], data["verdict"] = stamp(data.get("idea")), stamp(data.get("verdict"))
        payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
        rd.write_text(f"window.KMI_DATA = {payload};\n", encoding="utf-8")
    after = chk.check_folder(folder)
    return "upgraded" if not after.errors else f"upgraded but now fails: {after.errors[0]}"


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    dry = "--dry-run" in argv
    argv = [a for a in argv if a != "--dry-run"]
    if argv and argv[0] == "--all":
        root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("ideas")
        folders = sorted(p.parent for p in root.glob("*/verdict.json"))
    else:
        folders = [pathlib.Path(a) for a in argv]
    bad = 0
    for f in folders:
        res = migrate(f, dry)
        bad += res.startswith(("re-run", "upgraded but"))
        print(f"{f.name}: {res}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
