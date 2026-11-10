"""Pin each HTML template's inline script in its Content-Security-Policy.

Run after any change to skills/kill/report.html or skills/compare/board.html:
    python3 scripts/update-csp.py            # rewrite stale hashes (files already correct are not written)
    python3 scripts/update-csp.py --check    # exit 1 if any hash is stale (CI)

Each template must have exactly one attribute-less inline <script> and one CSP meta tag.
"""
import base64
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = [ROOT / "skills" / "kill" / "report.html", ROOT / "skills" / "compare" / "board.html"]
CSP = ("default-src 'none'; script-src 'self' file: '{hash}'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; img-src 'self' data: blob:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'")
META_RX = re.compile(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(">)')


def pin(path):
    """Return (current_html, expected_html, digest) for one template."""
    html = path.read_text(encoding="utf-8")
    inline = re.findall(r"<script>(.*?)</script>", html, re.S)
    if len(inline) != 1:
        raise SystemExit(f"{path.relative_to(ROOT)}: expected exactly one inline <script>, found {len(inline)}")
    digest = "sha256-" + base64.b64encode(hashlib.sha256(inline[0].encode("utf-8")).digest()).decode()
    policy = CSP.format(hash=digest)
    expected, n = META_RX.subn(lambda m: m.group(1) + policy + m.group(3), html)
    if n != 1:
        raise SystemExit(f"{path.relative_to(ROOT)}: expected one CSP meta tag, found {n}")
    return html, expected, digest


def main(argv):
    check = "--check" in argv
    stale = []
    for path in TEMPLATES:
        rel = path.relative_to(ROOT)
        html, expected, digest = pin(path)
        if html == expected:
            print(f"ok     {rel}  {digest}")
            continue
        if check:
            stale.append(rel)
            print(f"STALE  {rel}  expected {digest}")
        else:
            path.write_text(expected, encoding="utf-8")
            print(f"pinned {rel}  {digest}")
    if stale:
        print(f"{len(stale)} stale CSP hash(es). Run: python3 scripts/update-csp.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
