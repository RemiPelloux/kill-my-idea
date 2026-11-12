#!/usr/bin/env python3
"""Check share.json (posts about a verdict) and render the verdict card.

    python3 scripts/share-kit.py ideas/<folder>           check, write share/card.svg (+ .png) and share/posts.md
    python3 scripts/share-kit.py --check ideas/<folder>   check only

The model writes share.json: the card's lines and one post per place (Reddit, X, LinkedIn, Hacker
News…). This script checks each post against the place: length limits, no link where links are
banned, no "What I learned" section, no em dashes, and every "N/100" must be a score this idea
really has (the verdict, the projected fix, the validated score). It draws the card itself, so
the score on the image always comes from verdict.json. Nothing is posted. Stdlib only; the PNG
needs rsvg-convert or ImageMagick, otherwise only the SVG is written.
"""
import html
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("fix_kit", ROOT / "scripts" / "fix-kit.py")
fk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fk)
Report, text = fk.Report, fk.text

# platform: (title max, title required, body max, a link counts as)
LIMITS = {"reddit": (300, True, 10000, None), "x": (0, False, 280, 23), "linkedin": (0, False, 3000, None),
          "hn": (80, True, 2000, None), "other": (300, False, 5000, None)}
URL_IN_TEXT = re.compile(r"https?://\S+|www\.\S+|\]\(", re.I)
LESSONS = re.compile(r"what i learn(ed|t)|lessons? learn(ed|t)|key takeaways", re.I)
DASHES = re.compile("[–—]")
SCORE_REF = re.compile(r"\b(\d{1,3})\s?/\s?100\b")
COLORS = {"GO": "#16a34a", "PIVOT": "#d97706", "NO-GO": "#dc2626"}


def known_scores(folder, verdict):
    s = {verdict.get("score")}
    for name, path in (("fix.json", ("fixed", "score")), ("validate.json", ("results", "rescored", "score"))):
        p = folder / name
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            for k in path:
                d = (d or {}).get(k) if isinstance(d, dict) else None
            if isinstance(d, int):
                s.add(d)
    return s


def clean(rep, where, val):
    if isinstance(val, str):
        if DASHES.search(val):
            rep.error(f"{where}: has an em or en dash; use a comma, a colon or a period")
        if LESSONS.search(val):
            rep.error(f"{where}: no 'What I learned' or lessons section in posts")


def check_share(share, verdict, rep, scores):
    if share.get("schema_version") != "1.0":
        rep.error('schema_version: must be "1.0"')
    if share.get("slug") != verdict.get("slug"):
        rep.error(f"slug: {share.get('slug')!r} is not the verdict's {verdict.get('slug')!r}")
    card = share.get("card") or {}
    text(rep, "card.headline", card.get("headline"), 60)
    clean(rep, "card.headline", card.get("headline"))
    rs = card.get("reasons") or []
    if not 2 <= len(rs) <= 3:
        rep.error("card.reasons: 2 or 3 short lines")
    for i, r in enumerate(rs):
        text(rep, f"card.reasons[{i}]", r, 90)
        clean(rep, f"card.reasons[{i}]", r)
    text(rep, "card.after", card.get("after"), 60, required=False)
    clean(rep, "card.after", card.get("after"))
    card_text = " ".join([card.get("headline") or "", card.get("after") or ""] + [r for r in rs if isinstance(r, str)])
    for r in sorted({int(m) for m in SCORE_REF.findall(card_text)} - scores):
        rep.error(f"card: says {r}/100, but this idea's scores are {sorted(x for x in scores if x is not None)}")
    posts = share.get("posts") or []
    if not 1 <= len(posts) <= 6:
        rep.error("posts: 1 to 6")
    for i, p in enumerate(posts):
        w = f"posts[{i}]"
        plat = p.get("platform")
        if plat not in LIMITS:
            rep.error(f"{w}.platform: one of {sorted(LIMITS)}")
            continue
        tmax, treq, bmax, link_len = LIMITS[plat]
        text(rep, f"{w}.place", p.get("place"), 60)
        title, body, link = p.get("title") or "", p.get("body") or "", p.get("link")
        if treq and not title:
            rep.error(f"{w}.title: {plat} needs a title")
        if title and not tmax:
            rep.error(f"{w}.title: {plat} posts have no title; put it in the body")
        if title and tmax and len(title) > tmax:
            rep.error(f"{w}.title: {len(title)} characters, {plat} allows {tmax}")
        size = len(body) + ((link_len or len(link)) + 1 if link else 0)
        if not body and plat != "hn":
            rep.error(f"{w}.body: missing")
        if size > bmax:
            rep.error(f"{w}.body: {size} characters with the link, {plat} allows {bmax}")
        if not isinstance(p.get("links_allowed"), bool):
            rep.error(f"{w}.links_allowed: true or false, from the place's rules")
        elif not p["links_allowed"]:
            if link or URL_IN_TEXT.search(title + " " + body):
                rep.error(f"{w}: has a link, but {p.get('place')} doesn't allow them")
        if link and not re.match(r"^https://[^\s\"'<>]+$", str(link)):
            rep.error(f"{w}.link: an https URL")
        for where, val in ((f"{w}.title", title), (f"{w}.body", body)):
            clean(rep, where, val)
            if UNSAFE_MARKUP.search(val):
                rep.error(f"{where}: markup or a script URL; plain text only")
        refs = {int(m) for m in SCORE_REF.findall(title + " " + body)}
        for r in sorted(refs - scores):
            rep.error(f"{w}: says {r}/100, but this idea's scores are {sorted(x for x in scores if x is not None)}")
        if str(verdict.get("score")) not in re.findall(r"\d+", title + " " + body):
            rep.error(f"{w}: doesn't state the verdict's score ({verdict.get('score')}); an honest post gives it")


UNSAFE_MARKUP = fk.UNSAFE


def wrap(s, width):
    lines, cur = [], ""
    for word in s.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    return lines + ([cur] if cur else [])


def card_svg(verdict, card):
    e = lambda s: html.escape(str(s), quote=True)
    v, score = verdict["verdict"], verdict["score"]
    col = COLORS.get(v, "#475569")
    filled = round(score / 100 * 560)
    head = wrap(card["headline"], 34)[:2]
    y = 250
    head_svg = ""
    for ln in head:
        head_svg += f'<text x="72" y="{y}" font-size="46" font-weight="700" fill="#0f172a">{e(ln)}</text>'
        y += 56
    y += 18
    reasons = ""
    for r in card["reasons"]:
        for j, ln in enumerate(wrap(r, 58)[:2]):
            mark = f'<circle cx="80" cy="{y - 9}" r="6" fill="{col}"/>' if j == 0 else ""
            reasons += f'{mark}<text x="100" y="{y}" font-size="26" fill="#334155">{e(ln)}</text>'
            y += 34
        y += 8
    after = (f'<text x="72" y="566" font-size="24" font-weight="600" fill="#2563eb">{e(card["after"])}</text>'
             if card.get("after") else "")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" font-family="Inter, 'Helvetica Neue', Arial, sans-serif">
<rect width="1200" height="630" fill="#f8fafc"/><rect width="1200" height="12" fill="{col}"/>
<text x="72" y="120" font-size="30" font-weight="700" fill="{col}" letter-spacing="2">{e(v)}</text>
<text x="1128" y="150" font-size="120" font-weight="800" fill="#0f172a" text-anchor="end">{score}<tspan font-size="44" fill="#64748b">/100</tspan></text>
<rect x="72" y="150" width="560" height="14" rx="7" fill="#e2e8f0"/><rect x="72" y="150" width="{filled}" height="14" rx="7" fill="{col}"/>
{head_svg}{reasons}{after}
<text x="1128" y="596" font-size="22" fill="#64748b" text-anchor="end">kill-my-idea · sourced research, scored by a script</text>
</svg>
"""


def to_png(svg_path):
    png = svg_path.with_suffix(".png")
    for cmd in (["rsvg-convert", "-o", str(png), str(svg_path)], ["magick", str(svg_path), str(png)]):
        if shutil.which(cmd[0]):
            if subprocess.run(cmd, capture_output=True).returncode == 0 and png.exists():
                return png
    return None


def posts_md(share):
    out = ["# Posts\n\nNothing here is posted for you. Post the card image with each one.\n"]
    for p in share["posts"]:
        out.append(f"## {p['platform']}: {p['place']}\n\n{'Links allowed.' if p['links_allowed'] else 'No links.'}\n")
        if p.get("title"):
            out.append(f"Title:\n\n```text\n{p['title']}\n```\n")
        body = p.get("body") or ""
        if p.get("link"):
            body = f"{body}\n\n{p['link']}".strip()
        out.append(f"Body:\n\n```text\n{body}\n```\n")
    return "\n".join(out)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = pathlib.Path(args[0])
    rep = Report()
    share, verdict = fk.load(folder / "share.json", rep), fk.load(folder / "verdict.json", rep)
    if share is not None and verdict is not None:
        check_share(share, verdict, rep, known_scores(folder, verdict))
    if rep.errors:
        for x in rep.errors:
            print(f"error: {x}")
        print(f"FAIL {folder}: {len(rep.errors)} error(s)")
        return 1
    line = f"{len(share['posts'])} post(s) for " + ", ".join(p["place"] for p in share["posts"])
    if "--check" in argv:
        print(f"OK {folder}/share.json: {line}")
        return 0
    d = folder / "share"
    d.mkdir(exist_ok=True)
    svg = d / "card.svg"
    svg.write_text(card_svg(verdict, share["card"]), encoding="utf-8")
    png = to_png(svg)
    (d / "posts.md").write_text(posts_md(share), encoding="utf-8")
    print(f"OK {folder}: {line}; share/card.svg{' + card.png' if png else ' (no PNG: install rsvg-convert)'}, share/posts.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
