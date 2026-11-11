#!/usr/bin/env python3
"""Build an idea's report.html from its report data, with no executable data.

    python3 scripts/build-report.py ideas/2026-11-my-idea [-o out.html]

Reads <idea>/report-data.json (strict JSON, the default since 1.0) or, for an older folder,
<idea>/report-data.js (window.KMI_DATA = {...}; it must be a pure JSON literal). Writes
<idea>/report.html: the plugin template with the data embedded as an inert
<script type="application/json" id="kmi-data"> block and the <script src="report-data.js"> tag
removed. The page then contains no script written by the model, opens from file:// and can be
sent as one file. Python stdlib only.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "skills" / "kill" / "report.html"
PREFIX_RX = re.compile(r"^﻿?\s*window\.KMI_DATA\s*=\s*")
SRC_TAG_RX = re.compile(r'<script src="report-data\.js"></script>\n?')
CSP_SRC_RX = re.compile(r"script-src 'self' file: '")
BLOCK_OPEN = '<script type="application/json" id="kmi-data">'


def _reject(name):
    raise ValueError(f"{name} is not valid JSON for a browser")


def load_data(folder):
    """The report data of an idea folder as a dict; refuses anything that is not plain data."""
    folder = pathlib.Path(folder)
    js, jf = folder / "report-data.js", folder / "report-data.json"
    if jf.exists():
        path, text = jf, jf.read_text(encoding="utf-8").lstrip("﻿")
    elif js.exists():
        path, text = js, js.read_text(encoding="utf-8")
        m = PREFIX_RX.match(text)
        if not m:
            raise SystemExit(f"{js}: must start with 'window.KMI_DATA ='")
        text = text[m.end():].rstrip()
        text = text[:-1].rstrip() if text.endswith(";") else text
    else:
        raise SystemExit(f"{folder}: no report-data.json or report-data.js")
    try:
        # json.loads rejects anything that is not a pure JSON literal (code, comments, calls)
        data = json.loads(text, parse_constant=_reject)
    except (json.JSONDecodeError, ValueError) as e:
        raise SystemExit(f"{path}: not a pure JSON literal ({e})")
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: the report data must be a JSON object")
    return data


def build(html, data):
    """The template with the data as an inert JSON block, and no data <script src> tag."""
    if len(re.findall(r"<script>", html)) != 1:
        raise SystemExit("report.html: expected exactly one attribute-less inline <script>")
    if BLOCK_OPEN in html:
        raise SystemExit("report.html: already contains a #kmi-data block (already built?)")
    html, n = SRC_TAG_RX.subn("", html)
    if n != 1:
        raise SystemExit('report.html: expected one <script src="report-data.js"></script> tag')
    # every "<" (only ever inside JSON strings) becomes <: no "</script" or "<!--" can end the block early
    try:
        payload = json.dumps(data, ensure_ascii=False, allow_nan=False).replace("<", "\\u003c")
        payload.encode("utf-8")
    except (ValueError, UnicodeEncodeError) as e:
        raise SystemExit(f"report data can't be embedded: {e}")
    # a built report loads no script file, so the CSP drops 'self' and file: and keeps only the pinned hash
    html, n = CSP_SRC_RX.subn("script-src '", html)
    if n != 1:
        raise SystemExit("report.html: expected one script-src 'self' file: in the CSP")
    return html.replace("<script>", f"{BLOCK_OPEN}{payload}</script>\n<script>", 1)


def embedded(html):
    """The data embedded in a built report, or None."""
    i = html.find(BLOCK_OPEN)
    if i == -1:
        return None
    j = html.find("</script>", i)
    return json.loads(html[i + len(BLOCK_OPEN):j])


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("idea_folder", type=pathlib.Path)
    ap.add_argument("-o", "--output", type=pathlib.Path)
    a = ap.parse_args(argv)
    out_html = build(TEMPLATE.read_text(encoding="utf-8"), load_data(a.idea_folder))
    out = a.output or a.idea_folder / "report.html"
    out.write_text(out_html, encoding="utf-8")
    print(f"{out}  {out.stat().st_size / 1024:.1f} KB, data embedded as inert JSON")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
