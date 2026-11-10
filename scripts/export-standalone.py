#!/usr/bin/env python3
"""Build ONE self-contained HTML report from an idea folder.

    python3 scripts/export-standalone.py ideas/2026-11-my-idea [-o out.html]

Reads <idea>/report.html and <idea>/report-data.js, embeds the data as
<script type="application/json" id="kmi-data"> (which the report template reads first)
and drops the <script src="report-data.js"> tag. Default output:
<idea>/report-standalone.html. The data file must be a pure JSON literal assigned to
window.KMI_DATA; anything else is refused. Python stdlib only.
"""
import argparse
import json
import pathlib
import re
import sys

PREFIX_RX = re.compile(r"^﻿?\s*window\.KMI_DATA\s*=\s*")
SRC_TAG_RX = re.compile(r'<script src="report-data\.js"></script>\n?')
INLINE_RX = re.compile(r"<script>")


def load_data(path):
    text = path.read_text(encoding="utf-8")
    m = PREFIX_RX.match(text)
    if not m:
        raise SystemExit(f"{path}: must start with 'window.KMI_DATA ='")
    body = text[m.end():].rstrip()
    if body.endswith(";"):
        body = body[:-1].rstrip()
    try:
        # json.loads rejects anything that is not a pure JSON literal (code, comments, calls)
        data = json.loads(body)
    except json.JSONDecodeError as e:
        raise SystemExit(f"{path}: not a pure JSON literal ({e})")
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: KMI_DATA must be a JSON object")
    return data


def build(html, data):
    if len(INLINE_RX.findall(html)) != 1:
        raise SystemExit("report.html: expected exactly one attribute-less inline <script>")
    if '<script type="application/json" id="kmi-data">' in html:
        raise SystemExit("report.html: already contains a #kmi-data block (already standalone?)")
    html, n = SRC_TAG_RX.subn("", html)
    if n != 1:
        raise SystemExit('report.html: expected one <script src="report-data.js"></script> tag')
    # every "<" (only ever inside JSON strings) becomes \u003c: no "</script" or "<!--" can end the block early
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    block = f'<script type="application/json" id="kmi-data">{payload}</script>\n'
    return html.replace("<script>", block + "<script>", 1)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("idea_folder", type=pathlib.Path)
    ap.add_argument("-o", "--output", type=pathlib.Path)
    a = ap.parse_args(argv)
    folder = a.idea_folder
    report, data_js = folder / "report.html", folder / "report-data.js"
    for p in (report, data_js):
        if not p.is_file():
            raise SystemExit(f"missing {p}")
    out_html = build(report.read_text(encoding="utf-8"), load_data(data_js))
    out = a.output or folder / "report-standalone.html"
    out.write_text(out_html, encoding="utf-8")
    print(f"{out}  {out.stat().st_size / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
