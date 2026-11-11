# Hookline Studio

8 ad-ready UGC videos a month, with the hooks written for you, for a fixed $1,200. Start with a $799 pilot of 4 videos.

> Built from **rescue path 1** of a **PIVOT 56/100** verdict (rescue scored 60). The original idea, a 20% matchmaking commission, has no pricing power against Billo ($99 per video) and JoinBrands (8-15% fees), and brands bypass the broker after the first deal. This kit builds the fixed monthly package instead.
>
> "Hookline Studio" is a **working name, not checked** (domain, trademark, social handles). Check it before you buy anything with it.

## Idea

A small studio that owns the brief and the hooks, not just the introduction: vetted creators film the client's real product at a fixed rate, the studio writes 3 hooks per video, edits, delivers and sends a monthly recap of which hooks won.

## Customer

US Shopify brands spending $5-30K a month on Meta or TikTok ads, with no in-house creative team. Their trigger is ad fatigue: rising CPA forces a creative refresh every 4-8 weeks.

## Key metric

**Paid $799 pilots: 1 or more by day 14 (2026-11-25).** Stop if there are fewer than 3 positive replies from 100 cold emails by day 7, or 0 paid pilots by day 14.

## Run

From a clean clone, with Python 3.9+ and nothing to install:

```bash
cd build/app
python3 -m unittest discover -s tests       # tracker tests
python3 ops/tracker.py report                # outreach, pilots, hours per video, kill flags
python3 -m http.server 8000 --directory site # offer page at http://localhost:8000
```

Optional settings: `cp build/.env.example build/.env`, fill it in, then load it before running the tracker with `set -a; . ../.env; set +a`.

Log as you go:

```bash
python3 ops/tracker.py outreach --channel email --sent 20 --positive 1
python3 ops/tracker.py order P1 --client "Brand" --kind pilot --price 799 --videos 4 --creator-cost 400
python3 ops/tracker.py hours P1 1.5 --note "briefs"
python3 ops/tracker.py video P1 1 --approved 2026-12-01 --paid 2026-12-05
```

Tests with [SmartTest](https://github.com/RemiPelloux/SmarttyTest), which runs only the tests a change can affect (Node 22.12+; you run these, they install a package):

```bash
cd build/app
npm install -D @tkmremi/smarttest@1.2.0   # creates a package.json
npx smarttest init --dry-run              # shows what it detected: unittest, 1 test file
npx smarttest init --yes
npx smarttest hook install                # affected tests on every commit
npx smarttest run                         # affected tests while coding; --all before a release
```

Video and ads (you run these; they install packages): `cd build/video && npm install && npm run video && npm run ads`.

## Structure

```
app/
├── site/
│   ├── index.html            offer page: $799 pilot and $1,200/month package (paste the Stripe links in)
│   └── styles.css            brand colours from design-tokens.css
├── templates/
│   ├── cold-email.md         cold email, follow-up and LinkedIn templates
│   ├── creative-brief.md     brief per video: product, angle, 3 hooks, shot list
│   ├── creator-agreement.md  fixed rate, usage rights, FTC disclosure
│   └── client-agreement.md   pilot and package terms, 30-day notice, no direct hire
├── ops/
│   ├── tracker.py            outreach, orders, hours, creator payments, kill criteria
│   └── data/                 CSV data (gitignored)
└── tests/
    └── test_tracker.py
```

## Status

Sprint 0 (the 7-day test) has not started. Nothing is deployed, bought or sent. The agreements are templates, not legal advice.

Start with [BUILD.md](BUILD.md).
