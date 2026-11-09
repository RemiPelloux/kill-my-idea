"""Pin the report's inline script in its Content-Security-Policy.

Run after any change to skills/kill/report.html:
    python3 scripts/update-csp.py
"""
import base64
import hashlib
import pathlib
import re

PATH = pathlib.Path(__file__).resolve().parent.parent / "skills" / "kill" / "report.html"
CSP = ("default-src 'none'; script-src 'self' file: '{hash}'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; img-src 'self' data: blob:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'")

html = PATH.read_text(encoding="utf-8")
inline = re.findall(r"<script>(.*?)</script>", html, re.S)
if len(inline) != 1:
    raise SystemExit(f"expected exactly one inline <script>, found {len(inline)}")
digest = base64.b64encode(hashlib.sha256(inline[0].encode("utf-8")).digest()).decode()
policy = CSP.format(hash=f"sha256-{digest}")
html, n = re.subn(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)', lambda m: m.group(1) + policy + m.group(2), html)
if n != 1:
    raise SystemExit("CSP meta tag not found")
PATH.write_text(html, encoding="utf-8")
print(f"CSP pinned: sha256-{digest}")
