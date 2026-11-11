<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟡 PIVOT · 69/100
> **Cookie-free, privacy-first website analytics at $6/month**
>
> `███████░░░` 69 / 100 · confidence high, 29 sources
>
> - ❌ Two look-alikes launched first: Fathom (Product Hunt #2, 2018-06) and Simple Analytics (#3, 2018-09) ([source](https://www.producthunt.com/products/fathom-analytics/launches))
> - ❌ Free Google Analytics runs on 55.7% of all websites and sets the price anchor at zero ([source](https://w3techs.com/technologies/history_overview/traffic_analysis/all/y))
> - ✅ About 90% gross margin, near-zero capital, a beta with 60+ users, and a rising privacy tailwind (GDPR, Safari ITP 2.1)
>
> **Could be saved:** open-source it and position it as transparent EU analytics → 70/100 (doable)
> **Cheapest test:** switch on paid plans for the 60+ beta users plus a Show HN; at least 10 paying customers in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 69/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2069%2F100-yellow)

# Plausible Analytics — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **scored as of 2019-06-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 69/100 (raw 68.5) |
| **Confidence** | high: 21 sourced sub-scores of 21, 29 sources (10 primary). Many metrics are still estimates. |
| **Countries** | EE (legal base); sold worldwide in English |
| **Assumptions** | Budget near zero (under USD 1,000); 10–15 h/week per founder; side income first; no existing audience. The input says two developers, but the April 2019 launch post describes a **solo founder**. |

## 0. Executive summary

**Answer:** **PIVOT, 69/100**, one point short of GO. It is cheap to build and run, with about 90% gross margin and rising privacy demand. But Fathom and Simple Analytics launched the **same pitch** in 2018, and Google Analytics is free.

**Key findings**
1. **Two look-alikes launched first in 2018**: Fathom (Product Hunt #2 of the day, 2018-06) and Simple Analytics (#3, 2018-09) sell the same simple, private analytics to the same indie buyers ([source](https://www.producthunt.com/products/fathom-analytics/launches)).
2. **Free Google Analytics anchors the price at zero**: GA runs on **55.7%** of all websites (W3Techs, 2019-01). Matomo and Fathom are free to self-host ([source](https://w3techs.com/technologies/history_overview/traffic_analysis/all/y)).
3. **Privacy demand is rising, proof of payment is thin**: a "Migrating from Google Analytics" thread drew **352** HN points (2019-01), yet the best-documented peer had about $400 MRR from 40 customers ([source](https://news.ycombinator.com/item?id=18810035), [source](https://www.indiehackers.com/interview/how-i-started-a-business-with-two-lines-of-code-37f3d5348e)).

**Steelman:** Regulation and browsers (GDPR, Safari ITP 2.1, CCPA) are pushing site owners off GA. The product is already built and has 60+ beta users. Costs are so low that a few hundred customers would make a profitable business. The evidence supports the tailwind and the margins. It does not yet show demand beyond a few hundred dollars of MRR per player.

**Recommendation:** Launch the paid plans now, but open-source the code and position it as transparent EU analytics. Drop it if fewer than 10 beta users pay within 7 days.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Fathom and Simple Analytics own the niche, and a cheaper copy gets no word of mouth | differentiation | H | Fewer than 20 paying customers 30 days after the paid launch and Show HN |
| 2 | Free GA keeps buyers: users install it alongside GA, never pay, and leave after the trial | free_alternative | M | Trial-to-paid conversion below 10% of the 60 beta users by day 30 |
| 3 | Side-project hours stall marketing after the launch spike, and MRR plateaus at hobby level | channel_readiness | M | New sign-ups fall under 5 per week after launch week |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Open-source the code (free to self-host, paid hosted plan) and position it as transparent, EU-hosted analytics | differentiation 2 → 3, channel_readiness 3 → 3.5, assets 1.5 → 2 | 70/100 (estimate) | doable | 1–2 weeks | near zero | A licence choice (e.g. AGPL) and self-hosting docs |
| 2 | Add a multi-site agency plan at $12–36/month and sell to EU web agencies that need GDPR-safe analytics | pricing_power 2 → 2.5, willingness_to_pay 3 → 3.5 | 70/100 (estimate) | hard | 2–3 months | under $500 | Outbound sales time, a DPA template, client reports |
| 3 | Put one founder full-time on content and SEO around "Google Analytics alternative" and GDPR | channel_readiness 3 → 3.5, assets 1.5 → 2.5 | 69/100 (estimate) | hard | 6+ months | a founder's time | Writing skill and savings to cover the income gap |

## 2. Next step: 7-day test

**Cheapest test:** Switch on paid plans for the 60+ beta users and post a Show HN the same week. Count paying customers after 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Turn on billing and email the 60+ beta users with the one-third beta discount | 60 emails sent, 20+ opened |
| 2 | Post a Show HN and an Indie Hackers update with the open-source repo | 50+ HN points or 500+ landing-page visits |
| 3–5 | Reply to every comment and collect objections versus Fathom and Simple Analytics | 10+ written objections logged |
| 7 | Count paying customers and trial starts | 10+ paying → keep going; fewer → rework positioning |

**Stop if:**
- Fewer than 10 paying customers 7 days after the paid launch → rework positioning before building more.
- Under $300 MRR by day 90 → stop, or change price or segment.
- Monthly churn above 10% in the first 3 months → fix onboarding before marketing.

## 3. Source

> Plausible Analytics: privacy-friendly, cookie-free website analytics, $6 per month, launch country EE (Estonia, selling worldwide online). Score it as of 2019-06-01: use only evidence published on or before that date (set verdict.as_of). Founder: two developers bootstrapping, side project. Just go: do not ask questions. Use the slug plausible-analytics.

## 4. Fact-check

| Claim | Status | Evidence | Source |
|-------|--------|----------|--------|
| privacy-friendly | partly | Holds only if raw IPs are never stored: under Breyer (2016), a dynamic IP address can be personal data | [CJEU](https://curia.europa.eu/jcms/jcms/p1_236867/cs) |
| cookie-free | true | With no cookies, the ePrivacy art. 5(3) consent requirement should not apply; WP194 says analytics cookies do need consent | [Hogan Lovells](https://www.hoganlovells.com/en/publications/article-29-working-party-publishes-opinion-on-cookie-consent-exemptions) |
| Founder: two developers | partly | The April 2019 launch post describes a solo founder | [dev.to](https://dev.to/ukutaht/i-m-launching-plausible-17f8) |

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | GA is free on 55.7% of all sites (2019-01). Matomo (1.2% of sites) and Fathom v1 (2018-05) are free open source | [W3Techs](https://w3techs.com/technologies/history_overview/traffic_analysis/all/y) |
| 2 | Strong direct competitor | **hit** | 3+ paid tools sell to the same buyer: Fathom (PH #2, 2018-06), Simple Analytics (PH #3, 2018-09; 40+ payers), Matomo (1.2% of all websites) | [Product Hunt](https://www.producthunt.com/products/fathom-analytics/launches) |
| 3 | Graveyard | clear | Searched for analytics shut-downs and post-mortems before 2019-06; found no dated SaaS failure in this niche | — |
| 4 | No distribution channel | clear | HN and Product Hunt launches gave Simple Analytics 40+ paying customers; Plausible already has 60+ beta users from Indie Hackers | [Indie Hackers](https://www.indiehackers.com/interview/how-i-started-a-business-with-two-lines-of-code-37f3d5348e) |
| 5 | Costs eat the margin | clear | A EUR 3.79/month server and ~7.5% in Stripe fees leave ~90% gross margin on $6 | [VPSBenchmarks](https://www.vpsbenchmarks.com/trials/hetzner_performance_trial_25Feb2019) |
| 6 | Weak or falling demand | clear | HN threads about leaving GA drew 352 points (2019-01) and 284 points (2019-03) | [HN](https://news.ycombinator.com/item?id=18810035) |
| 7 | Legal / platform risk | clear (needs work) | Cookie-free avoids ePrivacy consent, but IPs can be personal data (Breyer 2016), and ad blockers (11% of users) may block the script | [CJEU](https://curia.europa.eu/jcms/jcms/p1_236867/cs) |
| 8 | Saturated wave (3 look-alikes, 2018-06 to 2019-06: Fathom, Fathom PRO, Simple Analytics) | clear | Under the 10-launch threshold | [Hunted.space](https://hunted.space/product/fathom-analytics/launches/fathom-analytics-pro) |

**Primary kill shot:** strong competitor. Plausible is the third entrant with the same positioning, and its only visible edge is a lower price.

## 6. Market

- **Target customer:** indie developers, bloggers and small SaaS founders (1–10 people), often in the EU, with 1–5 sites under 100k pageviews/month.
- **Pain** and how they solve it today: GA is heavy, needs a cookie banner under EU rules and is blocked by ad blockers. Today they use GA for free, self-host Matomo, or pay about $10/month for Fathom or Simple Analytics (estimate).
- **Demand signals:** an HN thread on migrating from GA drew 352 points and 104 comments (2019-01), and "Roll Your Own Analytics" drew 284 points (2019-03). Plausible's own beta had 60+ users ([dev.to](https://dev.to/ukutaht/i-m-launching-plausible-17f8)).
- **Trend:** rising, driven by GDPR (2018-05), Safari ITP 2.1 (2019-02) and CCPA (2018-06). GA's share is still growing (54.8% → 55.7% of sites, 2018 → 2019).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $720M/year | estimate | 10M actively maintained small sites (assumption) × $72/year |
| SAM | $7.2M/year | estimate | 1% privacy-conscious payers, anchored on Matomo's 1.2% share |
| SOM (year 1) | $72k/year | estimate | 1% of SAM ≈ 1,000 customers at $6/month |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Safari ITP 2.1 caps client-side cookies at 7 days, which breaks GA's returning-visitor counts | 2019-02 | [WebKit](https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/) |
| CCPA is signed, the second major privacy law after GDPR | 2018-06 | [Orrick](https://www.orrick.com/en/Insights/2018/06/California-Governor-Signs-Significant-Data-Privacy-Bill-into-Law) |
| The draft ePrivacy Regulation would exempt only first-party audience measurement from consent | 2017-01 | [Bird & Bird](https://twobirds.com/en/insights/2017/global/eprivacy-regulation-alert) |
| CJEU Breyer: dynamic IP addresses can be personal data | 2016-10 | [CJEU](https://curia.europa.eu/jcms/jcms/p1_236867/cs) |
| Developers publicly migrate off GA, citing ad blockers and GDPR | 2019-01 | [HN](https://news.ycombinator.com/item?id=18810035) |

The window is open, but two peers entered in 2018, so it is closing fast.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Indie developers, bloggers and small SaaS founders, often EU-based, with 1–5 small sites |
| **Where to reach them** | Hacker News (Show HN), Indie Hackers, Product Hunt, dev.to, developer Twitter |
| **Pays for today** | Mostly nothing (GA); a few pay Fathom or Simple Analytics, about $10/month (estimate) |
| **Budget** | About $5–15/month per site (estimate) |
| **Trigger** | Cookie-banner work under GDPR, an ad blocker hiding their traffic, or a privacy stance on their own product |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Indie blog and SaaS landing-page stats without a cookie banner (**best**) | Indie founder, $6/month | Paste one script |
| 2 | GDPR-safe analytics for an agency's client sites | Web agency, $12–36/month | Multi-site dashboard and reports |
| 3 | Open-source projects and docs sites | Maintainers, often unpaid | Low |

**Best option:** the indie use case. It matches the channel (HN, Indie Hackers) and sells in a single session.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| Google Analytics | US | Full analytics suite | Free | 5 (55.7% of sites, 2019-01) | Cookies, consent banner, heavy UI, blocked by ad blockers |
| Matomo (Piwik) | NZ | Open-source GA clone | Free self-hosted; cloud price not found | 4 (1.2% of sites) | Self-hosting effort; GA-like complexity |
| Fathom Analytics | CA | Simple private analytics, open source + hosted PRO | Open source free; hosted price before 2019-06 not found | 3 (PH #2, 2018-06) | Founder change (2019-03); same pitch |
| Simple Analytics | NL | Simple private analytics, hosted | ~$10/month (estimate: $400 MRR / 40 customers, 2018) | 2 | Closed source |
| Yandex.Metrica | RU | Free analytics with session recording | Free | 4 (5.1% of sites) | Worse on privacy than GA |

- **Free alternatives:** GA, Matomo and Fathom v1 (self-hosted).
- **Edge:** today, only the $6 price (the cheapest entry). Open-sourcing it plus EU hosting would make it a real, specific difference.
- **First 10 customers** come from the 60+ beta users (Indie Hackers) and a Show HN.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $6/month | sourced | [launch post, 2019-04](https://dev.to/ukutaht/i-m-launching-plausible-17f8) |
| Variable cost per unit | $0.55/month | estimate | Stripe 2.9% × 6 + €0.25 ≈ $0.45, plus ~$0.10 hosting share |
| Gross margin % | 90.8% | estimate | (6 − 0.55) ÷ 6 |
| Churn / lifetime | 6%/month, 16.7 months | estimate | Low-price subscription range 5–7% ([Recurly, 2018](https://recurly.com/blog/new-subscriber-churn-benchmarks-and-why-managing-churn-is-critical)) |
| Conversion rate | 0.1% | estimate | ~30–40 payers from ~30k HN visitors for a peer launch |
| CAC | $40 | estimate | ~1.3 founder hours per customer × $30/h |
| LTV | $90 | estimate | 6 × 0.908 × 16.7 |
| LTV : CAC | 2.25 | estimate | 90 ÷ 40 |
| Payback (months) | 7.3 | estimate | 40 ÷ 5.45 |
| Fixed costs / month | $50 | estimate | 2–3 Hetzner boxes (€3.79 each), backups, email, OÜ accounting |
| Break-even (customers / month) | 10 | estimate | 50 ÷ 5.45, costs only, no founder salary |
| Time to first revenue (weeks) | 4 | estimate | Beta is live and pricing is announced |

| Cost item | Monthly | Source |
|-----------|---------|--------|
| Hetzner CX11 server | €3.79 | [VPSBenchmarks, 2019-02](https://www.vpsbenchmarks.com/trials/hetzner_performance_trial_25Feb2019) |
| Stripe EU cards | 1.4% + €0.25 per charge (2.9% + €0.25 non-EU) | [Bank Innovation, 2015-12](https://bankinnovation.net/2015/12/adyen-might-be-to-blame-for-stripe-pricing-cuts-in-europe/) |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 30 | $180 | $67 | $113 | Only part of the beta converts; 8% churn |
| Base | 150 | $900 | $133 | $767 | Show HN + content; 6% churn |
| Optimistic | 600 | $4,800 | $500 | $4,300 | Mix shifts to $12 plans after open-sourcing |

Even the base case is **side income**, not two salaries. To pay two founders, it needs roughly 1,000+ customers.

## 10. Countries

**Launch country:** EE. Estonia is the legal base: 0% tax on retained profits and 20/80 on distributions ([PwC Estonia, 2018-01](https://www.pwc.com/ee/en/insights/assets/maksuteave/PwC_Tax_Alert_Issue35_January2018.pdf)), and an EU company helps with GDPR trust ([Andmekaitse Inspektsioon info, 2018-06](https://ehrl.ee/wp-content/uploads/2018/06/Andmekaitseteemaline-info-andmekaitseinspektsioon.pdf)). Customers are worldwide.

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Done: the beta has been live since 2019-02 |
| Skills missing | Marketing, content, sales |
| Key dependencies | Stripe, hosting, ad-block lists |
| Legal / compliance | GDPR processor duties (DPA, art. 28); store no raw IPs |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Ad-block lists add the script domain and undercount customers' traffic | M | H | Custom-domain proxy option | [PageFair](https://businesswire.com/news/home/20170131005878/en/PageFair-Reports-615-Million-Devices-World-Block) |
| 2 | The final ePrivacy text narrows the analytics exemption | M | M | Stay cookie-free, store no IPs, offer a DPA | [IAPP](https://iapp.org/news/a/the-top-5-contested-issues-in-the-eus-developing-eprivacy-regulation) |
| 3 | A peer cuts its price or adds a free tier | M | M | Compete on openness and EU hosting | [van Kooten](https://www.dannyvankooten.com/blog/2018/reviving-ana-as-fathom/) |
| 4 | Side-project hours stall support and features | H | M | Set an MRR target that triggers going full-time | — |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 4.5 | ~90%: €3.79 server, ~7% Stripe fee |
| | LTV : CAC | 2.5 | (estimate) 2.25 |
| | pricing power | 2 | GA is free on 55.7% of sites; $6 undercuts peers |
| Feasibility (20) | build effort | 4 | Beta live with 60+ users |
| | skills match | 4.5 | Developers building a developer tool |
| | capital needed | 5 | €3.79/month server |
| Time to first revenue (15) | time to MVP | 4 | MVP exists, pricing announced |
| | sales cycle | 4.5 | Self-serve card checkout |
| | channel readiness | 3 | HN/PH proven for peers; no own audience |
| Market demand (15) | search demand | 3 | 352-point HN thread |
| | trend | 4 | GDPR, ITP 2.1, new peers |
| | willingness to pay | 3 | Peers charge; ~$400 MRR proof |
| Competitive room (10) | free alternatives | 2 | GA, Matomo, Fathom OSS (R5) |
| | competitor density | 2.5 | Fathom, Simple Analytics, Matomo, GA, Clicky |
| | differentiation | 2 | Same pitch; only a lower price |
| Risk (10) | legal / regulatory | 3 | IPs are personal data; DPA work |
| | platform dependency | 3 | Ad-blocker exposure |
| | market risk | 4 | Durable need |
| Founder fit (5) | skills | 4 | Engineering yes, marketing no |
| | assets | 1.5 | No audience |
| | interest | 3.5 | Privacy mission, side project |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 3.00 | 15.0 |
| Feasibility (20) | 4.50 | 18.0 |
| Time to first revenue (15) | 3.83 | 11.5 |
| Market demand (15) | 3.33 | 10.0 |
| Competitive room (10) | 2.17 | 4.3 |
| Risk (10) | 3.33 | 6.7 |
| Founder fit (5) | 3.00 | 3.0 |
| **Raw total** | | **68.5** |
| **Rules applied** | R5: free_alternatives 2.5 → 2 (free alternative hit); competitor_density kept ≤ 3 | |
| **Final score** | | **69 / 100** |

Type checks: **churn_benchmark** is a hit (low-price subscriptions churn ~5–7%/month, estimate) and **switching_cost** is a hit (GA is free, installed everywhere, and its history is not portable).

## 13. Sources

29 sources from 25+ domains: 10 primary, 16 secondary, 3 tertiary. All were published on or before 2019-06-01. Accessed 2026-11-11.

1. [W3Techs, traffic analysis tools usage history](https://w3techs.com/technologies/history_overview/traffic_analysis/all/y): GA 55.7%, Matomo 1.2% — primary — 2019-01 row
2. [W3Techs, Web technologies of the year 2018](https://w3techs.com/blog/entry/web_technologies_of_the_year_2018) — secondary — 2019-01
3. [Danny van Kooten, Reviving Ana as Fathom](https://www.dannyvankooten.com/blog/2018/reviving-ana-as-fathom/) — primary — 2018-05-12
4. [Product Hunt, Fathom launches](https://www.producthunt.com/products/fathom-analytics/launches) — primary — 2018-06
5. [Product Hunt, Simple Analytics launches](https://www.producthunt.com/products/simple-analytics/launches) — primary — 2018-09
6. [Hunted.space, Fathom PRO launch](https://hunted.space/product/fathom-analytics/launches/fathom-analytics-pro) — tertiary — 2018-09
7. [Indie Hackers, Simple Analytics interview](https://www.indiehackers.com/interview/how-i-started-a-business-with-two-lines-of-code-37f3d5348e) — secondary — 2018
8. [Uku Taht, I'm launching Plausible](https://dev.to/ukutaht/i-m-launching-plausible-17f8) — primary — 2019-05-09
9. [Indie Hackers, Show IH: Plausible](https://www.indiehackers.com/post/show-ih-plausible-simple-privacy-focused-web-analytics-e0d8e20622) — primary — 2019-01-24
10. [HN, Migrating from Google Analytics](https://news.ycombinator.com/item?id=18810035) — tertiary — 2019-01-02
11. [HN, Roll Your Own Analytics](https://news.ycombinator.com/item?id=19388489) — tertiary — 2019-03-14
12. [PageFair via Business Wire](https://businesswire.com/news/home/20170131005878/en/PageFair-Reports-615-Million-Devices-World-Block) — secondary — 2017-01-31
13. [Hogan Lovells, WP194 cookie consent exemptions](https://www.hoganlovells.com/en/publications/article-29-working-party-publishes-opinion-on-cookie-consent-exemptions) — secondary — 2012-06
14. [WebKit, ITP 2.1](https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/) — primary — 2019-02-21
15. [MacRumors, ITP in iOS 12.2](https://www.macrumors.com/2019/02/21/safari-ios-12-2-intelligent-tracking-prevention/) — secondary — 2019-02-21
16. [Orrick, CCPA signed](https://www.orrick.com/en/Insights/2018/06/California-Governor-Signs-Significant-Data-Privacy-Bill-into-Law) — secondary — 2018-06
17. [VPSBenchmarks, Hetzner trial](https://www.vpsbenchmarks.com/trials/hetzner_performance_trial_25Feb2019) — secondary — 2019-02-25
18. [Bank Innovation, Stripe EU pricing](https://bankinnovation.net/2015/12/adyen-might-be-to-blame-for-stripe-pricing-cuts-in-europe/) — secondary — 2015-12
19. [CJEU press release, Breyer C-582/14](https://curia.europa.eu/jcms/jcms/p1_236867/cs) — primary — 2016-10-19
20. [Bird & Bird, Breyer](https://twobirds.com/en/insights/2016/global/cjeu-decision-on-dynamic-ip-addresses-touches-fundamental-dp-law-questions) — secondary — 2016-10
21. [Covington Inside Privacy, Breyer](https://www.insideprivacy.com/international/cjeu-confirms-dynamic-ip-addresses-to-be-personal-data/) — secondary — 2016-10
22. [Bird & Bird, ePrivacy Regulation alert](https://twobirds.com/en/insights/2017/global/eprivacy-regulation-alert) — secondary — 2017-01
23. [Data Protection Report, ePrivacy proposal](https://www.dataprotectionreport.com/?p=3283) — secondary — 2017
24. [IAPP, ePrivacy contested issues](https://iapp.org/news/a/the-top-5-contested-issues-in-the-eus-developing-eprivacy-regulation) — secondary — 2017
25. [EDPS, Opinion on ePrivacy Regulation](https://www.edps.europa.eu/sites/default/files/publication/17-04-24_eprivacy_en.pdf) — primary — 2017-04-24
26. [Recurly Research, churn benchmarks](https://recurly.com/blog/new-subscriber-churn-benchmarks-and-why-managing-churn-is-critical) — primary — 2018-09-05
27. [PwC Estonia, Tax Alert Issue 35](https://www.pwc.com/ee/en/insights/assets/maksuteave/PwC_Tax_Alert_Issue35_January2018.pdf) — secondary, local — 2018-01
28. [Andmekaitse Inspektsioon, data protection info](https://ehrl.ee/wp-content/uploads/2018/06/Andmekaitseteemaline-info-andmekaitseinspektsioon.pdf) — secondary, local — 2018-06
29. [KPMG, Estonia country profile 2018](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2018/06/country-profile-estonia-2018.pdf) — secondary — 2018-06

**Gaps:**
- No pre-2019-06 pricing pages for Fathom or Simple Analytics; archive.org was unreachable.
- No dated churn or CPC benchmarks.
- No Google Trends series.
- The Indie Hackers interview date (2018) is inferred from its content.
