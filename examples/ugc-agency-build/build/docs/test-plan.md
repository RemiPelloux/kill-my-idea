# Test plan: Hookline Studio

Most of this product is a service, so most tests are manual checks on real things. Code tests cover the tracker, because it applies the kill criteria.

## Unit tests

Tool: Python `unittest` (standard library). Run in `app/`: `python3 -m unittest discover -s tests`.

| Function | What is tested |
|---|---|
| `card_fee` | 2.9% + $0.30: $1,200 gives $35.10 |
| `outreach_status` | Under 100 emails is RUNNING; fewer than 3 positive per 100 is STOP; 3+ is PASS |
| `order_metrics` | More than 2 h per video is flagged; USD per hour under the floor is flagged; a healthy pilot has no flag |
| `pay_delay_days` | Days between approval and payment; missing date gives none |

## SmartTest

The tests run through [SmartTest](https://github.com/RemiPelloux/SmarttyTest) (`@tkmremi/smarttest` 1.2.0), which reads the code, finds the tests a change can reach and runs only those, through `unittest`. Every skipped test comes with the reason (`npx smarttest explain <test>`).

- **Setup**, once, in `app/`: `npm install -D @tkmremi/smarttest@1.2.0`, `npx smarttest init --yes`, `npx smarttest hook install`. `app/pyproject.toml` and `tests/__init__.py` are what let it find the Python project and collect the tests.
- **While coding:** `npx smarttest run`. A change to `ops/tracker.py` selects `tests/test_tracker.py` (7 tests).
- **On every commit:** the pre-commit hook runs the affected tests; a failure blocks the commit.
- **Before a release or a pilot invoice:** `npx smarttest run --all`.
- **In CI:** `npx smarttest ci`.
- Python is a preview in SmartTest: when it can't prove a test unrelated, it runs it. `python3 -m unittest discover -s tests` still works without Node.

## Integration test

`Commands.test_round_trip_report` writes outreach, an order and hours to a temporary data folder through the CLI, then checks the report prints PASS, the paid pilot count and hours per video.

## Manual acceptance, per story

Each story's acceptance criteria in `user-stories.md` are checked on the real thing and ticked there, with the evidence noted:

| Story | Manual check |
|---|---|
| US-01 | Open the page on a phone and a laptop; both prices, 4 videos, 2 revisions and 10 days visible; the pilot button opens Stripe checkout; a test-mode payment succeeds |
| US-02 | Open 10 random rows of the brand list in the Meta Ad Library: each has an ad active in the last 30 days |
| US-03 | 3 signed creator agreements on file, each with rate, licence scope and duration, disclosure clause |
| US-04 | Instantly shows 100 sent; tracker report matches the counts |
| US-05 | 4 filled briefs and the client's written approval, dated before shipping |
| US-06 | Tracker report shows hours per video and USD per hour for the pilot; unit tests pass |
| US-07 | Play the 4 files: 1080x1920, captions, hook in 3 s; delivery date within 10 days of product receipt |
| US-08 | Proposal email sent within 3 days of delivery; subscription link works in test mode |
| US-09 | Recap lists spend, CTR and CPA per video from client numbers and names 8 hooks |
| US-10 | Signed client agreement on file before production starts |
| US-11 | Calendar has 16 videos with 4 dates each; tracker shows 2 h or less per video for the month |
| US-12 | Tracker shows every creator paid 7 days or less after approval |
| US-13 | Written client permission for the case study numbers; case study visible on the page |

## Sprint exits, and how each is measured

| Sprint | Exit | Measured by |
|---|---|---|
| 0 | 3+ positive replies from 100 emails by day 7; 1+ paid $799 deposit by day 14 | `tracker.py report` (outreach line, paid pilots line) and the Stripe dashboard |
| 1 | 4 videos delivered within 10 days of product receipt, 2 h or less per video (8 h total) | Delivery email dates; `tracker.py report` hours per video for the pilot order |
| 2 | 1 client on the $1,200/month package, first month paid | Stripe subscription payment; order logged as `package` |
| 3 | 2 active package clients, 16 videos scheduled, 2 h or less per video, creators paid within 7 days | Calendar; `tracker.py report` with no STOP or LATE line |

Any STOP line in the report is a kill criterion from the verdict: stop and review before the next sprint.
