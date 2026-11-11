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

**Known limit:** the model may already know how these companies ended. `as_of` stops later sources
from being used, and the checker fails any source published after it, but it can't erase what the
model remembers. Treat a pass as necessary, not as proof.
