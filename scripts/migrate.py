#!/usr/bin/env python3
"""Upgrade idea folders to the 1.0 file format.

    python3 scripts/migrate.py ideas/2026-11-my-idea [more folders...]
    python3 scripts/migrate.py --all [ideas]          # every ideas/*/ folder
    python3 scripts/migrate.py --dry-run --all
    python3 scripts/migrate.py --json --all [ideas]   # also move report-data.js to report-data.json

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


def to_json(folder):
    """report-data.js -> report-data.json, then rebuild report.html with the data embedded as inert JSON."""
    rd = folder / "report-data.js"
    if not rd.exists() or (folder / "report-data.json").exists():
        return False
    data = json.loads(DATA_RX.match(rd.read_text(encoding="utf-8").lstrip("\ufeff")).group(1))
    (folder / "report-data.json").write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
    br = chk._build_report()
    (folder / "report.html").write_text(br.build(br.TEMPLATE.read_text(encoding="utf-8"), data), encoding="utf-8")
    rd.unlink()
    return True


def migrate(folder, dry, json_too=False):
    rep = chk.check_folder(folder)
    if rep.errors:
        return f"re-run needed ({len(rep.errors)} errors under today's rules, e.g. {rep.errors[0][:90]})"
    v = json.loads((folder / "verdict.json").read_text(encoding="utf-8")) if (folder / "verdict.json").exists() else None
    if v is not None and v.get("schema_version") == VERSION:
        if json_too and not dry and to_json(folder):
            return "already 1.0; moved to report-data.json"
        return "already 1.0"
    if dry:
        return "would upgrade"
    for name in ("idea.json", "verdict.json"):
        p = folder / name
        if p.exists():
            p.write_text(json.dumps(stamp(json.loads(p.read_text(encoding="utf-8"))), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rj, rd = folder / "report-data.json", folder / "report-data.js"
    if rj.exists():
        data = stamp(json.loads(rj.read_text(encoding="utf-8")))
        data["idea"], data["verdict"] = stamp(data.get("idea")), stamp(data.get("verdict"))
        rj.write_text(json.dumps(data, ensure_ascii=False) + "\n", encoding="utf-8")
        br = chk._build_report()
        (folder / "report.html").write_text(br.build(br.TEMPLATE.read_text(encoding="utf-8"), data), encoding="utf-8")
    elif rd.exists():
        data = json.loads(DATA_RX.match(rd.read_text(encoding="utf-8").lstrip("﻿")).group(1))
        data = stamp(data)
        data["idea"], data["verdict"] = stamp(data.get("idea")), stamp(data.get("verdict"))
        payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
        rd.write_text(f"window.KMI_DATA = {payload};\n", encoding="utf-8")
    moved = json_too and to_json(folder)
    after = chk.check_folder(folder)
    return ("upgraded" + ("; moved to report-data.json" if moved else "")) if not after.errors else f"upgraded but now fails: {after.errors[0]}"


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    dry, json_too = "--dry-run" in argv, "--json" in argv
    argv = [a for a in argv if a not in ("--dry-run", "--json")]
    if argv and argv[0] == "--all":
        root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("ideas")
        folders = sorted(p.parent for p in root.glob("*/verdict.json"))
    else:
        folders = [pathlib.Path(a) for a in argv]
    bad = 0
    for f in folders:
        res = migrate(f, dry, json_too)
        bad += res.startswith(("re-run", "upgraded but"))
        print(f"{f.name}: {res}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
