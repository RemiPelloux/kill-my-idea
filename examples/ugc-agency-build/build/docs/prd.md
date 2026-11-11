# PRD: Hookline Studio

Built from rescue path 1 of the PIVOT 56/100 verdict (2026-11-11). Rescue score: 60.

## Problem

Small US DTC brands running paid social need 3-5 fresh product videos a month because ad creatives fatigue every 4-8 weeks and CPA rises. Self-serve platforms (Billo from $99, Insense from about $400/month, JoinBrands at 8-15%) give them footage, but leave the brief, the hooks and the creator management to the founder.

The original idea, a 20% commission for matchmaking, failed on pricing power and bypass: brands rebook creators directly after the first deal. This PRD sells the result instead: a fixed monthly package where the studio owns the brief and the hooks.

## Customer

US Shopify brands spending $5-30K a month on Meta or TikTok ads, with no in-house creative team. Today they pay Collabstr creators about $154 per video, Billo from $99 or Fiverr gigs from $35. Budget: about $460-1,000 a month.

Personas: Maya (DTC founder, the buyer), Jordan (UGC creator, the supplier), Sam (the solo operator, 15 h/week).

## Goals

- Prove brands pay for briefed, hook-led videos: 1 or more paid $799 pilot by 2026-11-25.
- Deliver the pilot at 2 hours or less of coordination per video.
- Convert pilots to the $1,200/month package for 8 videos.
- Reach 2 package clients inside 15 hours a week (sprint 3).

## Non-goals

- No marketplace, platform or client portal.
- No commission model.
- No AI-generated videos (that is rescue path 2).
- No paid ads before a pilot case study exists.
- No promise of ad results (ROAS, CPA) to clients.

## Must-have stories

US-01 offer page and pilot payment link · US-02 list of 100 brands · US-03 3 creators on fixed rates · US-04 100 cold emails and 30 LinkedIn messages, logged · US-05 briefs with 3 hooks approved by the client · US-06 hours per video tracked · US-07 4 ad-ready videos in 10 days · US-08 $1,200/month proposal · US-11 monthly calendar for 2 clients.

Details and acceptance criteria: `user-stories.md`.

## Success metric

**Paid $799 pilots: 1 or more by 2026-11-25** (day 14).

## The 7-day test (sprint 0)

| When | Step | Pass if |
|---|---|---|
| Day 1 | Pick one vertical; list 100 Shopify brands running Meta ads (Meta Ad Library) | 100 brands with an active ad and a founder email |
| Day 2 | Recruit 3-5 creators from r/UGCcreators at a fixed $100-150 per video | 3 creators agree to the rate in writing |
| Day 2 | One-page offer: $799 pilot for 4 ad-ready videos with hooks; Stripe payment link | Page and payment link live |
| Day 3-6 | Send 100 personalised cold emails plus 30 LinkedIn messages | 3 or more positive replies |
| Day 7 | Ask every positive reply for a paid pilot | 1 or more paid deposit |

## Kill criteria (from the verdict)

- Fewer than 3 positive replies from 100 cold emails by day 7 -> stop.
- 0 paid pilots by day 14 -> stop.
- More than 2 h of coordination per video on the first order -> stop, the hourly rate is under $20.
- First client rebooks a creator directly within 60 days -> drop the commission model (here: enforce the no-direct-hire clause and check the package still holds).

`app/ops/tracker.py report` prints the first three as STOP flags.

## Open questions

- Real coordination hours per video: the verdict's 1.5-2 h is an estimate; the pilot measures it.
- Will brands accept $1,200/month when Billo sells single videos from $99? Only the sprint 2 conversion answers it.
- Creator rate: the plan assumes $100 per video (low end of $100-150), which leaves about $365 a month per client after creators and card fees. At $150 per video, 8 videos cost $1,200 and the package loses about $35 a month. Recruit at about $100, or raise the package price.
- Which single vertical to start with (the verdict suggests one, e.g. skincare).
- Churn: 8%/month is an estimate between the 1.6% retainer benchmark and small-brand reality.
