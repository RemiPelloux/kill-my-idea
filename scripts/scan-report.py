#!/usr/bin/env python3
"""Static safety scan of the HTML templates (report and idea board).

    python3 scripts/scan-report.py        # exit 1 on any finding

Report data comes from web research, so the templates must treat it as hostile. Fails on:
  - HTML sinks (innerHTML =, outerHTML =, insertAdjacentHTML) beyond the allowlisted count
    per file. Every allowed sink renders only esc()'d strings, Number()s and whitelisted enums.
    Convention: mark each sink with a /* safe-render */ comment on the same line. Files in
    MARKER_REQUIRED must carry the marker on every sink; adding a sink means reviewing it,
    adding the marker and raising the count below in the same change.
  - dynamic code: the e-v-a-l builtin, the Function constructor, document.write and
    setTimeout/setInterval with a string argument (patterns below are written with
    character classes so this file does not match its own rules)
  - href="${...}" that is not esc(<safe value>), where the safe value is a safeUrl()/safeRel()
    call or a variable assigned from one
  - inline event-handler attributes (on<event>=) inside HTML in the script
Python stdlib only.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# file -> number of HTML sinks allowed (reviewed render sites)
ALLOW = {"skills/kill/report.html": 2, "skills/compare/board.html": 4}
MARKER_REQUIRED = {"skills/compare/board.html"}
MARKER = "/* safe-render */"

SINK_RX = re.compile(r"\.(?:innerHTML|outerHTML)\s*\+?=(?!=)|\.insertAdjacentHTML\s*\(")
BANNED = [(re.compile(r"\be[v]al\s*\("), "dynamic code call (e-v-a-l)"),
          (re.compile(r"\bnew\s+Functio[n]\b"), "Function constructor"),
          (re.compile(r"\bdocument\.write(?:ln)?\s*\("), "document.write"),
          (re.compile(r"\bset(?:Timeout|Interval)\s*\(\s*[\"'`]"), "string timer")]
HREF_RX = re.compile(r'href="\$\{([^}]*)\}')
SAFE_FN = r"(?:safeUrl|safeRel)"
ESC_ARG_RX = re.compile(r"^\s*esc\(\s*(.+?)\s*\)\s*$")
HANDLER_RX = re.compile(r"<[a-zA-Z][^<>]*\son[a-z]+\s*=", re.S)


def inline_script(html):
    m = re.findall(r"<script>(.*?)</script>", html, re.S)
    return m[0] if len(m) == 1 else None


def scan(rel):
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    js = inline_script(html)
    if js is None:
        return [f"{rel}: expected exactly one attribute-less inline <script>"]
    offset = html[:html.index(js)].count("\n")
    lines = js.split("\n")
    issues, sinks = [], []
    safe_vars = set(re.findall(r"\b(?:const|let|var)\s+(\w+)\s*=\s*" + SAFE_FN + r"\s*\(", js))
    for i, line in enumerate(lines, 1 + offset):
        for m in SINK_RX.finditer(line):
            sinks.append(i)
            if rel in MARKER_REQUIRED and MARKER not in line:
                issues.append(f"{rel}:{i}: HTML sink without {MARKER} marker")
        for rx, name in BANNED:
            if rx.search(line):
                issues.append(f"{rel}:{i}: banned {name}")
        for m in HREF_RX.finditer(line):
            arg = ESC_ARG_RX.match(m.group(1))
            inner = arg.group(1) if arg else ""
            ok = bool(arg) and (re.match(SAFE_FN + r"\s*\(", inner) or inner in safe_vars
                                or re.sub(r"^\w+\.", "", inner) in {"href"} and _assigned_safe(js, inner))
            if not ok:
                issues.append(f'{rel}:{i}: unsafe href="${{{m.group(1)}}}" (must be esc(safeUrl(...)) or esc(<var from safeUrl/safeRel>))')
    for m in HANDLER_RX.finditer(js):
        i = 1 + offset + js[:m.start()].count("\n")
        issues.append(f"{rel}:{i}: inline event handler attribute in HTML string: {m.group(0)[-40:]!r}")
    allowed = ALLOW.get(rel, 0)
    print(f"{rel}: {len(sinks)} HTML sink(s) at lines {sinks or '-'} (allowlist {allowed})")
    if len(sinks) != allowed:
        issues.append(f"{rel}: {len(sinks)} HTML sinks, allowlist says {allowed}. Review the new/removed sink(s) and update ALLOW in scripts/scan-report.py")
    return issues


def _assigned_safe(js, expr):
    """obj.href is safe when the object literal sets href: safeUrl(...)/safeRel(...)."""
    return re.search(r"\bhref\s*:\s*" + SAFE_FN + r"\s*\(", js) is not None


def main():
    issues = []
    for rel in ALLOW:
        if not (ROOT / rel).is_file():
            issues.append(f"{rel}: missing")
            continue
        issues += scan(rel)
    for msg in issues:
        print("FAIL  " + msg)
    print("scan: " + ("FAILED" if issues else "ok"))
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
