# Calibration set

10 ideas whose outcome is known: 5 that clearly worked and 5 that clearly failed. Each is scored
**as of its launch date** (`verdict.as_of`), with only evidence published before then, so the score
can be compared with what really happened.

| Slug | As of | Pitch at the time | Outcome |
|---|---|---|---|
| calendly | 2013-06-01 | Scheduling links so people book a meeting without email back-and-forth, freemium, $8/month (US) | worked |
| convertkit | 2013-06-01 | Email marketing for bloggers who sell courses and ebooks, $29/month (US) | worked |
| carrd | 2016-03-01 | One-page websites, free with a $19/year Pro plan (US) | worked |
| plausible-analytics | 2019-06-01 | Privacy-friendly, cookie-free website analytics, $6/month (EU) | worked |
| tally-forms | 2020-06-01 | A form builder that works like a doc, free with paid Pro (BE) | worked |
| juicero | 2016-03-01 | A $699 Wi-Fi juicer that presses $5–8 produce packs, sold by subscription (US) | failed |
| quibi | 2020-03-01 | Premium 10-minute shows made for phones, $4.99/month (US) | failed |
| homejoy | 2012-07-01 | Book a home cleaner online in 60 seconds, from $20/hour, marketplace (US) | failed |
| shyp | 2014-03-01 | Tap an app and a courier picks up, packs and ships any item, $5 + postage (US) | failed |
| washio | 2013-06-01 | On-demand laundry and dry-cleaning pickup and delivery by app (US) | failed |

Run each with `/kill-my-idea:kill <pitch> as of <date>`, then:

```sh
python3 scripts/calibrate.py calibration --outcomes calibration/outcomes.json
```

**1.0 targets:** the ideas that worked score a median of 60 or more, the failures a median under 50,
and at least one idea reaches GO.

## Results (2026-11-11)

Runs made with 0.10.1; `calibrate.py` recomputes every score from the sub-scores under today's rules.

| Idea | Outcome | Score as written | With R7 (0.11) |
|---|---|---|---|
| tally-forms | worked | GO 71 | GO 71 |
| plausible-analytics | worked | 69 | 69 |
| calendly | worked | 68 | 68 |
| convertkit | worked | 68 | 68 |
| carrd | worked | 64 | 64 |
| quibi | failed | 60 | 49 |
| shyp | failed | 59 | 49 |
| washio | failed | 59 | 49 |
| homejoy | failed | 58 | 48 |
| juicero | failed | 49 | 39 |

Targets: worked median 68 (≥ 60) **pass**, failed median 49 (< 50) **pass**, one GO **pass**.
Before R7 the failures' median was 59: the score ranked every success above every failure, but
didn't push the failures below 50. The verdicts here were written before R7, so their own files
show the older score; the checker would ask them for R7.

**Known limit:** the model may already know how these companies ended. `as_of` stops later sources
from being used, and the checker fails any source published after it, but it can't erase what the
model remembers. Treat a pass as necessary, not as proof.
