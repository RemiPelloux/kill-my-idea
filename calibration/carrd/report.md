> ## 🟡 PIVOT · 64/100
> **One-page websites, free, Pro at $19/year**
>
> `██████░░░░` 64 / 100 · confidence high, 37 sources
>
> - ❌ Squarespace already sells one-page sites at **$3/month** (Nov 2015), and Wix has **77M users** ([Squarespace](https://prnewswire.com/news-releases/squarespace-takes-on-growing-customer-needs-with-two-new-product-offerings-300171455.html), [Wix](https://rss.globenewswire.com/news-release/2016/02/10/809175/29041/en/Wix-com-Reports-Fourth-Quarter-and-Full-Year-2015-Results.html))
> - ❌ At $19/year and **3–7% monthly SMB churn**, LTV is about $36, so paid acquisition can't pay back ([Tunguz](https://www.tomtunguz.com/saas-innovators-dilemma/index.md))
> - ✅ Demand is rising (Wix revenue **+43%** in 2015) and gross margin is about 90%
>
> **Could be saved:** a 2-week template-only MVP launched on Show HN and Product Hunt → 68/100 (doable)
> **Cheapest test:** a landing page with 3 demo sites and a $19 Pro pre-order, posted for 7 days; continue only with 10+ pre-orders
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 64/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2064%2F100-yellow)

# Carrd: one-page websites, free with a $19/year Pro plan — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **as of 2016-03-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 64/100 (raw 63.8) |
| **Confidence** | high: 15 sourced sub-scores of 21, 37 sources (17 primary) |
| **Countries** | US |
| **Assumptions** | Solo developer, USD 1,000, side project (~10 h/week), no existing audience. Customer assumed: US freelancers, designers, indie makers and job seekers. Pro includes custom domains. Headless run, so no questions were asked. |

## 0. Executive summary

**Answer:** PIVOT at 64. Margins are excellent and demand is rising, but **Wix and Squarespace** already give the job away free or at $3/month. A founder with **no audience** has only launch-day spikes to reach users.

**Key findings**
1. **Incumbents already sell one-page sites**: Squarespace launched **Cover Pages at $3/month** in Nov 2015, backed by $78.5M raised, and Wix has **77M users** ([source](https://prnewswire.com/news-releases/squarespace-takes-on-growing-customer-needs-with-two-new-product-offerings-300171455.html)).
2. **The price leaves no room for paid acquisition**: at $19/year and **3–7% monthly SMB churn**, LTV is about **$36** (estimate), so only free channels can pay back ([source](https://www.tomtunguz.com/saas-innovators-dilemma/index.md)).
3. **Demand is rising and margins are near 90%**: Wix grew **43%** in 2015. Serving a static page costs cents, so Stripe's **$0.85** per charge is the main cost ([source](https://rss.globenewswire.com/news-release/2016/02/10/809175/29041/en/Wix-com-Reports-Fourth-Quarter-and-Full-Year-2015-Results.html)).

**Steelman:** Full builders are overkill for one page. A fast, ultra-simple tool at **$19/year** (half Squarespace's $36) with about 90% margin and viral free sites can win a niche that incumbents underprice. The evidence supports the margin and the price gap; the channel is unproven.

**Recommendation:** Don't build the full builder yet. Ship a 2-week, template-only MVP with a $19 Pro pre-order and launch it on Show HN and Product Hunt. Continue only with 10+ pre-orders in 7 days.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Launch-day traffic faded and no owned channel replaced it, so sign-ups stalled | channel_readiness | H | Fewer than 20 organic sign-ups a day by week 3 |
| 2 | Free users never upgraded: $19/year bought too little over free tiers | ltv_cac | M | Free-to-Pro conversion under 1% after 30 days |
| 3 | Squarespace or Wix cut one-page pricing and out-marketed a solo founder | strong_competitor | M | An incumbent price cut or free custom-domain offer within 30 days |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Cut scope to a 2-week MVP (fixed templates, no drag-and-drop, Pro = custom domain), then launch on Product Hunt and Show HN | time_to_mvp 2 → 4, build_effort 2.5 → 4 | 68/100 (estimate) | doable | 2 weeks | under $100 | Discipline to ship a narrow product |
| 2 | Build distribution first: free one-page templates and a "made with" badge on every free site | channel_readiness 2.5 → 4, assets 1.5 → 3 | 66/100 (estimate) | hard | 3–6 months | $0–200 | Design skill to make templates people share |
| 3 | Niche down to one ICP (freelance designers or job seekers) with a tailored Pro bundle | differentiation 2.5 → 3.5, channel_readiness 2.5 → 3 | 65/100 (estimate) | doable | 2 weeks | under $100 | Access to one community (Dribbble, r/web_design) |

No path reaches GO (70) without proof of a channel. Every path stays a PIVOT until the 7-day test supplies it.

## 2. Next step: 7-day test

**Cheapest test:** a landing page with 3 demo one-page sites and a $19/year Pro pre-order button, posted to Show HN, Product Hunt and r/web_design for 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Landing page with 3 demo sites and a $19/year Pro pre-order via Stripe | Page live, checkout tested with 1 real charge |
| 2 | Post Show HN; share in r/web_design and r/webdev | 500+ visitors, 100+ waitlist sign-ups |
| 3–4 | Launch on Product Hunt; reply to every comment | 300+ total sign-ups |
| 5–6 | Email the waitlist the pre-order offer | 10+ paid pre-orders |
| 7 | Count pre-orders; interview 5 buyers | 10+ pre-orders and 3+ repeat use cases → build the 2-week MVP |

**Stop if:**
- fewer than 300 waitlist sign-ups within 7 days;
- fewer than 10 paid pre-orders by day 7;
- free-to-Pro conversion below 1% after 60 days live.

## 3. Source

> Carrd: one-page websites, free with a Pro plan at $19 per year, launch country US. Score it as of 2016-03-01: use only evidence published on or before that date (set verdict.as_of). Founder: a solo developer with $1,000, side project. Just go: do not ask questions. Use the slug carrd.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | hit | Weebly (30M sites built), about.me (~5M users) and Wix's free plan publish a one-page site for $0 (2015) | [TechCrunch](https://techcrunch.com/2015/10/01/weebly-carbon/) |
| 2 | Strong direct competitor | **hit** | Wix: 77M users, $203.5M revenue in 2015. Squarespace Cover Pages from $3/month since Nov 2015 | [Wix](https://rss.globenewswire.com/news-release/2016/02/10/809175/29041/en/Wix-com-Reports-Fourth-Quarter-and-Full-Year-2015-Results.html) |
| 3 | Graveyard | hit | Jux closed citing "slow growth" (2013). GeoCities (2009), Google Page Creator and Posterous (2013) were shut by their owners | [TNW](https://thenextweb.com/news/jux-closing-down-citing-slow-growth) |
| 4 | No distribution channel | clear | A Product Hunt feature brings thousands of visitors at $0, and free sites can carry a badge. Pre-2016 CPC is unknown | [Businesses Grow](https://businessesgrow.com/2015/07/30/product-hunt/) |
| 5 | Costs eat the margin | clear | Stripe takes $0.85 of $19; a $5/month server hosts static pages, so margin is about 90% | [5pm Web](https://blog.5pmweb.com/2013/02/25/stripe-vs-paypal) |
| 6 | Weak or falling demand | clear | Wix revenue +43% in 2015; 55% of US very small businesses had no website | [Wix](https://rss.globenewswire.com/news-release/2016/02/10/809175/29041/en/Wix-com-Reports-Fourth-Quarter-and-Full-Year-2015-Results.html), [GoDaddy survey](https://domainnamewire.com/2015/09/16/godaddy-survey/) |
| 7 | Legal / platform risk | clear (real work) | Free subdomain hosts carried 14% of phishing attacks in 1H2014; safe harbor requires a DMCA agent filing | [APWG](https://docs.apwg.org/reports/APWG_GlobalPhishingSurvey_1H2014.pdf) |
| 8 | Saturated wave (6 look-alikes, 2015-03 to 2016-03) | clear | OnePager, Resume Builder, Lead Pages, Tilda, PageCloud and Squarespace Cover Pages: below the 10 threshold | [Product Hunt](https://www.producthunt.com/products/onepager/awards) |

**Primary kill shot:** strong_competitor (Squarespace and Wix).

## 6. Market

- **Target customer:** US freelancers, creatives, indie makers and job seekers who need one page on a custom domain (assumed).
- **Pain:** full builders are slow and priced for multi-page sites. Today these people use about.me, a free Wix or Weebly subdomain, or Squarespace Cover Page at $36/year.
- **Demand signals:** Wix had 77M registered users and 1.77M premium subscriptions (FY2015). More than 25% of small businesses have no website ([Clutch, 2015](https://clutch.co/press-releases/survey-shows-opportunity-small-businesses-improve-web-presence)).
- **Trend:** rising. Wix revenue was $141.8M in 2014 and $203.5M in 2015.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $203.5M/year (Wix alone, a floor) | sourced | Wix FY2015 |
| SAM | $3.4M/year | estimate | 10% of 1.77M premium subscriptions are single-page × $19 |
| SOM (year 1) | $10k/year | estimate | 0.3% of SAM ≈ 530 Pro customers |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Google ranks mobile-friendly pages higher on mobile search | 2015-04 | [Google](https://search.googleblog.com/2015/04/ranking-change-to-help-you-find-mobile_21.html) |
| Let's Encrypt offers free SSL to anyone | 2015-12 | [Let's Encrypt](https://letsencrypt.org/2015/11/12/public-beta-timing.html) |
| 64% of US adults own a smartphone | 2015-04 | [Pew](https://www.pewresearch.org/internet/2015/04/01/chapter-one-a-portrait-of-smartphone-ownership) |
| Squarespace prices a one-page product at $3/month | 2015-11 | [Squarespace](https://prnewswire.com/news-releases/squarespace-takes-on-growing-customer-needs-with-two-new-product-offerings-300171455.html) |

Free SSL and mobile ranking pressure make cheap, responsive custom-domain pages easy to offer, but incumbents are entering the same niche.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US freelancers, designers, indie makers and job seekers who need one page on a custom domain |
| **Where to reach them** | Product Hunt, Hacker News (Show HN), r/web_design and r/webdev, Designer News, Dribbble |
| **Pays for today** | Squarespace Cover Page at $3/month billed annually ($36/year), or free about.me / Wix pages |
| **Budget** | under $40/year (estimate) |
| **Trigger** | Launching a side project, starting a job search, needing a profile link |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Product or app landing page | Indie makers | Low |
| 2 | Personal profile / link page | Freelancers, job seekers | Low |
| 3 | Portfolio one-pager | Designers, photographers | Medium |

**Best option:** product landing pages. Makers launch often, gather on Product Hunt and Hacker News, and each live page advertises the tool.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| Squarespace Cover Pages | US | One-page tier of a full builder | $36–60/year (2015-11) | 5 | About 2× the price |
| Wix | IL | Free and premium site builder | free + premium (2015) | 5 | Heavy multi-page editor, ads on free sites |
| Weebly | US | Free and paid site builder | free + paid | 5 | Not focused on one page |
| about.me | US | Free profile pages | free | 4 | Fixed profile layout only |
| Strikingly | US | One-page builder (YC W13) | unknown as of 2016 | 3 | Pricing undocumented |
| PageCloud | CA | Visual site builder | $99 pre-order (2016-02) | 3 | Multi-page, pricier |
| Tilda Publishing | RU | Block-based page builder | unknown | 2 | Broader scope |

- **Free alternatives:** Wix, Weebly and about.me cover the basic job. A custom domain on a single page is not free anywhere I found.
- **Edge:** price ($19/year vs $36/year) and simplicity. That is one real difference, not a moat.
- **First 10 customers** come from Show HN, Product Hunt and r/web_design.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $19/year | estimate | founder's stated price |
| Variable cost per unit | $1.85/year | estimate | Stripe 2.9% + $0.30 = $0.85, hosting ~$0.50, support ~$0.50 |
| Gross margin % | 90% | estimate | (19 − 1.85) / 19 |
| Churn / lifetime | 4%/month, 25 months | estimate | Tunguz 3–7% SMB, Point Nine 5.4% median (2015) |
| Conversion rate | 2.3% free → Pro | estimate | Wix FY2015: 1.77M / 77M |
| CAC | $21.7 | estimate | 40 h × $25 / (2,000 sign-ups × 2.3%) |
| LTV | $35.7 | estimate | 19 × 0.90 × 25/12 |
| LTV : CAC | 1.65 | estimate | 35.7 / 21.7 |
| Payback (months) | 15.2 | estimate | 21.7 / 1.43; annual upfront billing returns $17.15 on day 1 |
| Fixed costs / month | $15 | estimate | $5 server + storage/CDN + domain/email |
| Break-even | ~11 Pro customers | estimate | 15 / 1.43 |
| Time to first revenue | 10 weeks | estimate | side-project build to a Pro tier |

| Scenario | Customers | Revenue / month | Costs / month | Margin | Note |
|----------|-----------|-----------------|---------------|--------|------|
| Pessimistic | 50 | $79 | $15 | $64 | One launch spike |
| Base | 300 | $475 | $25 | $450 | ~13,000 free users × 2.3% |
| Optimistic | 1,500 | $2,375 | $60 | $2,315 | Viral free sites compound |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 7-day landing page; about 10 weeks to a full Pro builder, 2 weeks for a template-only MVP |
| Skills missing | Design taste, marketing |
| Key dependencies | Commodity hosting, Stripe |
| Legal / compliance | DMCA designated agent ($105 filing), abuse and phishing moderation |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Phishing abuse gets the domain blocklisted | H | M | Moderation, abuse reports | [APWG](https://docs.apwg.org/reports/APWG_GlobalPhishingSurvey_1H2014.pdf) |
| 2 | No DMCA agent filing means no safe harbor | L | H | File before launch | [Plagiarism Today](https://www.plagiarismtoday.com/?p=9309) |
| 3 | Incumbent cuts its one-page price | M | H | Stay cheaper, own a niche | [TNW](https://thenextweb.com/news/squarespace-launches-two-new-pricing-tiers-for-its-splash-page-and-e-commerce-customers) |
| 4 | Low free-to-paid conversion | M | M | Put custom domains behind Pro | [TNW](https://thenextweb.com/news/the-future-of-evernote-from-memory-machine-to-time-machine) |

**Type checks (saas):** churn_benchmark is a **hit**: SMB churn of 3–7% a month caps LTV near $36, which shows in ltv_cac = 2. switching_cost is **clear**: the target users have no site yet.

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 5 | ~90% after Stripe fees and hosting |
| | LTV : CAC | 2 | 1.65 (estimate) |
| | pricing power | 2 | Free tiers anchor near $0 |
| Feasibility (20) | build effort | 2.5 | 2–3 months to a full builder |
| | skills match | 3.5 | Developer; design and marketing unproven |
| | capital needed | 4.5 | $5/month hosting |
| Time to revenue (15) | time to MVP | 2 | ~10 weeks |
| | sales cycle | 4.5 | $19 impulse purchase |
| | channel readiness | 2.5 | Product Hunt exists; no own audience |
| Demand (15) | search demand | 4 | 77M Wix users; 55% of very small businesses have no site |
| | trend | 4.5 | Wix +43% |
| | willingness to pay | 3 | 2.3% pay |
| Competition (10) | free alternatives | 2 | R5 coherence cap |
| | competitor density | 2 | 9 found, incl. Squarespace |
| | differentiation | 2.5 | Price only |
| Risk (10) | legal / regulatory | 3 | DMCA, phishing abuse |
| | platform dependency | 4 | Commodity hosting |
| | market risk | 4 | Durable need |
| Fit (5) | skills | 3.5 | Developer |
| | assets | 1.5 | No audience |
| | interest | 3 | Side project |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 3.0 | 15.0 |
| Feasibility (20) | 3.5 | 14.0 |
| Time to revenue (15) | 3.0 | 9.0 |
| Demand (15) | 3.83 | 11.5 |
| Competition (10) | 2.17 | 4.3 |
| Risk (10) | 3.67 | 7.3 |
| Fit (5) | 2.67 | 2.7 |
| **Raw total** | | **63.8** |
| **Rules applied** | none changed a score (the R5 caps were already met) | |
| **Final score** | | **64 / 100** |

## 13. Sources

37 sources, all published on or before 2016-03-01: 17 primary, 20 secondary. Full list with tiers and dates is in `report-data.json` and `report.html`. Excluded for hindsight or missing dates: Picnic (undated), the Storemapper Q1 2016 post, the Wix export help page, and Squarespace plan pages updated after 2016-03.
