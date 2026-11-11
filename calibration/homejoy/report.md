> ## 🟡 PIVOT · 58/100
> **Online booking for vetted home cleaners, $20/hour**
>
> `██████░░░░` 58 / 100 · confidence high, 34 sources
>
> - ❌ At $20/hour a 3-hour clean leaves ~$12.36 (20.6%) after SF cleaner pay ([BLS, May 2011](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm))
> - ❌ TaskRabbit ($24.5M raised) and Exec ($25/h, cleaning focus) already sell this ([TechCrunch](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond))
> - ✅ A mass, recurring need: 877,980 US maids, smartphones at 46% of adults
>
> **Could be saved:** Price at $25-30/hour on a recurring biweekly plan with the same insured cleaner, instead of 'cheapest from $20' → 63/100 (doable)
> **Cheapest test:** 7-day fake-door booking page for one SF zip cluster at $20 vs $28/hour, $1,000 of ads plus a deal, 10 vetted cleaners on call; measure bookings, contribution and 14-day rebooking.
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 58/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2058%2F100-yellow)

# Homejoy — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **as of 2012-07-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 58/100 (raw 58.0) |
| **Confidence** | high: 14 sourced sub-scores of 21, 34 sources (8 primary) |
| **Countries** | US |
| **Assumptions** | Scored as of 2012-07-01 with evidence published on or before that date; Seed round of roughly $1-2M, full-time team (not stated); Launch metros SF Bay Area and NYC; Typical job 3 hours ($60); platform pays cleaners near the local mean wage; Take rate not stated; modelled from price minus cleaner pay; Headless run: no questions asked |

## 0. Executive summary

**Answer:** **PIVOT**. Demand is huge and the tech easy, but at **$20/hour** the platform keeps about $12 a job after paying a Bay Area cleaner. Fund-raised rivals and the 2011 misclassification crackdown also squeeze it. Price up and win one city before scaling.

**Key findings**
1. **$20/hour leaves almost nothing**: A 3-hour $60 clean minus **$45.60** SF cleaner pay (BLS mean $15.20/h) and $2.04 Stripe leaves **$12.36**, 20.6% (estimate). ([source](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm))
2. **Funded rivals already sell cleaning**: TaskRabbit raised **$24.5M** and takes 13-30%; Exec charges $25/h and focuses on cleaning; Home Depot bought Redbeacon. ([source](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond))
3. **Contractor cleaners face a 2011 crackdown**: DOL and IRS signed a misclassification MOU on **2011-09-19**; California joined and AB 889 for housekeepers was pending. ([source](https://www.dol.gov/newsroom/releases/whd/whd20110919?lang=ko))

**Steelman:** A **mass, recurring** need (877,980 maids) meets 46% smartphone adoption, and Exec's $25/h cleaning demand proves people book online. Whoever owns repeat cleaning in one dense city could build a frequent, high-LTV habit. The evidence backs demand; it does not back the $20 margin.

**Recommendation:** Run a 7-day SF test at $20 vs $28/hour with 10 vetted cleaners; only raise or spend more if **30%+** of first-time customers rebook and contribution exceeds $10 a job.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal |
|---|---|---|---|---|
| 1 | Customers and cleaners go direct after a few cleans, so retained jobs per customer stay far below the 6 the model needs. | ltv_cac | H | Fewer than 30% of first-time customers rebook through the site within 14 days |
| 2 | Discounted first cleans (deals, promo codes) cost more than repeat jobs earn back, burning the seed round. | costs_eat_margin | H | Contribution per job under $10, or CAC above $60 per retained customer, in the first 30 days |
| 3 | A cleaner lawsuit or state ruling reclassifies 1099 cleaners as employees, adding payroll costs the $20 price can't carry. | legal_platform_risk | M | Cleaners asking about hours, overtime or W-2 status in the first 30 days |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|---|---|---|---|---|---|---|
| 1 | Price at $25-30/hour on a recurring biweekly plan with the same insured cleaner, instead of 'cheapest from $20' | Fixes gross_margin and pricing_power (costs_eat_margin): contribution rises from ~$12 to ~$25 per job, and the plan gives a reason not to go direct | 63/100 (estimate) | doable | 1-2 weeks: new pricing page and plan | near zero | Retention data showing customers keep a $25+/h plan |
| 2 | Make cleaners W-2 employees (or a staffing partner's) in one city, sold as the only insured, employed-staff option | Defuses legal_platform_risk (2011 misclassification push, AB 889) and creates a real difference | 61/100 (estimate) | hard | 2-3 months: payroll, insurance, hiring | payroll taxes ~10% + workers' comp | Employment counsel, workers' comp, a price that carries employer costs |
| 3 | Sell to employers as a perk (company accounts), like Exec's corporate offer | Fixes channel_readiness and CAC: one contract brings dozens of households | 61/100 (estimate) | hard | months of B2B sales | sales time | Pilot with 2-3 SF companies |

## 2. Next step: 7-day test

**Cheapest test:** 7-day fake-door booking page for one SF zip cluster at $20 vs $28/hour, $1,000 of ads plus a deal, 10 vetted cleaners on call; measure bookings, contribution and 14-day rebooking.

| Day | Step | Verify |
|---|---|---|
| Day 1 | Landing page for 5 SF zip codes with two prices: $20 and $28/hour | Page live with Stripe checkout |
| Day 2 | Recruit and vet 10 cleaners via job posts at $16-18/hour | 10 cleaners vetted and on call |
| Day 3 | Spend $1,000 on search ads and a forum or deal offer | 500+ visitors |
| Day 5 | Deliver the first cleans; collect ratings | 20+ paid bookings, rating 4.5+ |
| Day 7 | Offer every customer a biweekly plan | 30%+ book a second clean; contribution above $10/job |

**Stop if:** Fewer than 20 paid bookings from $1,000 of ads and deals by day 7 -> stop; Fewer than 30% of first-time customers rebook within 14 days -> stop; Contribution per job below $10 after cleaner pay and fees by day 7 -> raise price or stop; Fewer than 10 vetted cleaners willing to work at the offered pay by day 5 -> stop

## 3. Source

> Homejoy: book a vetted home cleaner online in 60 seconds, from $20 per hour, the platform takes a cut of each booking, launch country US. Score it as of 2012-07-01: use only evidence published on or before that date (set verdict.as_of). Founder: a seed-funded startup. Just go: do not ask questions. Use the slug homejoy.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|---|---|---|---|
| 1 | Free alternative | clear | Searched Craigslist, forums, word of mouth: cleaners advertise free on neighbourhood forums (Brownstoner, 2010), but none vet or book; partial, not the whole job. | [link](https://www.brownstoner.com/forum-archive/2010/08/great-cleaners) |
| 2 | Strong direct competitor | hit | TaskRabbit raised **$24.5M** (2011-12) with 2,000 Runners; Exec $3.3M at $25/h focused on cleaning; Zaarly $14.1M; Home Depot bought Redbeacon (2012-01). | [link](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) |
| 3 | Graveyard | clear | No closed online cleaning-booking company found before 2012-07; nearest is Kozmo, an on-demand local service that shut in 2001 (adjacent, not the same job). | [link](https://money.cnn.com/2001/04/12/technology/kozmo/index.htm) |
| 4 | No distribution channel | clear | Channels exist: deal sites (Groupon keeps ~50%), paid search (cleaning not among 2011's costliest CPCs), forums and employer perks; costly but credible. | [link](https://blog.agrawals.org/2011/06/07/an-analysis-of-the-groupon-merchant-agreement/) |
| 5 | Costs eat the margin | hit | $60 clean − $45.60 SF cleaner pay (BLS May 2011) − $2.04 Stripe = **$12.36** (20.6%) before insurance and support (estimate). | [link](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) |
| 6 | Weak or falling demand | clear | Clear: 877,980 maids employed (BLS May 2011), TaskRabbit 9,000 tasks/month, smartphones up 11 points in a year. | [link](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) |
| 7 | Legal / platform risk | hit | DOL-IRS misclassification MOU (2011-09-19), California joined, NY Domestic Workers' Bill of Rights (2010), CA AB 889 pending. | [link](https://www.dol.gov/newsroom/releases/whd/whd20110919?lang=ko) |
| 8 | Saturated wave (4 look-alikes, 2011-07 to 2012-07) | clear | About 1-4 look-alike launches (Exec, Zaarly NY, TaskRabbit expansion, Redbeacon) in the 12 months to 2012-07, far below 10. | [link](https://techcrunch.com/2012/02/29/exec-justin-tv/) |

**Primary kill shot:** costs_eat_margin — the $20/hour price leaves too little after paying cleaners at Bay Area wages.

**Type checks (marketplace):**
- **liquidity**: hit — Supply first: cleaners must be recruited and vetted before demand spend, and 75% annual turnover (up to 400%) means recruiting never stops. ([source](https://www.cleanlink.com/cp/article/Finders-Keepers--10917))
- **disintermediation**: hit — Recurring same-cleaner jobs: at a 20% cut a weekly client pays ~$624/year in fees, a strong reason to go direct; agencies rely on non-hire clauses. ([source](https://www.studicata.com/summaries/united-states-district-court-northern-district-of-illinois/janice-doty-unlimited-inc-v-stoecker-1988-dry3hw/))

## 6. Market

- **Target customer:** Busy professionals in SF and NYC
- **Pain:** Finding a trustworthy cleaner takes referrals, calls and vetting; paying one directly makes you a household employer
- **Today:** Word of mouth, Craigslist, agencies, or Exec at $25/hour
- **Trend:** rising — smartphones 35% → 46% of adults (Pew, 2012); TaskRabbit 9,000 tasks/month (2011)

| Market | Value | Basis | Source / formula |
|---|---|---|---|
| TAM | $3,500,000,000 | sourced | https://india.franchising.com/news/20090119_the_cleanest_sector_of_the_us_economy.html |
| SAM | $350,000,000 | estimate | TAM $3.5B × ~10% share for the SF Bay Area + NYC metros (dense, high-wage, high smartphone use) |
| SOM | $3,500,000 | estimate | 1% of SAM $350M in year 1 |

### Why now: now

| What changed | When | Source |
|---|---|---|
| Smartphone ownership rose from 35% to **46%** of US adults in about a year | 2012-03 | [link](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/) |
| Stripe launched: card payments by API at 2.9% + $0.30 | 2011-09 | [link](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) |
| TaskRabbit raised $17.8M to expand on-demand tasks to 5 cities | 2011-12 | [link](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) |
| Exec launched $25/hour on-demand help in SF and raised $3.3M | 2012-05 | [link](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |

The tools and the consumer habit arrived in 2011-12; the same window is open to funded rivals.

### ICP

| | |
|---|---|
| **Who** | Dual-income professionals in SF and NYC apartments with no time to clean, $75k+ household income |
| **Where** | Exec and TaskRabbit users, Neighbourhood forums (Brownstoner, Berkeley Parents Network), Groupon / LivingSocial deal subscribers, Company perk programmes |
| **Pays for today** | Exec at $25/hour, or an independent cleaner found by word of mouth (price unknown for 2012) |
| **Budget** | unknown (2012 client prices not found) |
| **Trigger** | Moving into a new apartment, a regular cleaner quits, or guests are coming |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|---|---|---|
| 1 | One-off deep clean before guests or a move | Household | low |
| 2 | Recurring biweekly clean with the same cleaner (best) | Household | medium |
| 3 | Cleaning as an employee perk | Employer | high |

**Best option:** recurring biweekly cleans, the only use case where LTV can beat CAC.

## 7. Competition

| Competitor | Country | Price | Traction /5 | Gap |
|---|---|---|---|---|
| [Exec](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) | US | $25/h (2012-05) | 3 | General errands, $25/h |
| [TaskRabbit](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) | US | unknown | 4 | Bid-based, no standard cleaning product |
| [Zaarly](https://siliconprairienews.com/2011/10/zaarly-raises-14-1m-series-a-adds-former-ebay-exec-whitman-to-board) | US | unknown | 3 | Generic local requests |
| [Redbeacon (The Home Depot)](https://ir.homedepot.com/news-releases/2012/01-20-2012) | US | unknown | 3 | Quote marketplace, not instant booking |
| [Molly Maid / Merry Maids franchises](https://www.franchising.com/news/20110118_molly_maid_ranked_in_top_100_franchises_by_allbusi.html) | US | unknown | 4 | Phone quotes, no online instant booking |
| [Craigslist / word of mouth](https://www.brownstoner.com/forum-archive/2010/08/great-cleaners) | US | unknown | 5 | No vetting, no insurance, no booking |

- **Free alternatives:** Craigslist, neighbourhood forums, word of mouth.
- **Edge:** price and 60-second booking only; neither is defensible.
- **First 10 customers:** paid search, a deal offer, neighbourhood forums in 5 SF zip codes.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|---|---|---|---|
| Price | 60 USD/job | estimate | Founder's stated $20/hour × typical job of 3 hours (assumed) = $60 |
| Variable cost per job | 47.64 USD/job | estimate | 3 h × $15.20 SF mean cleaner wage (BLS May 2011) = $45.60 + Stripe 2.9% × $60 + $0.30 = $2.04 |
| Gross margin % | 20.6 % | estimate | ($60 − $47.64) ÷ $60 = 20.6% of booking value, before insurance, background checks and support |
| Churn (monthly) | 36 % | estimate | 1 ÷ lifetime 2.77 months (6 jobs at 2.17 biweekly jobs/month) |
| Lifetime | 6 jobs per customer | estimate | Assumed: an average customer books 6 cleans; no 2012 benchmark found |
| Conversion (rebook) | 50 % deal buyers who rebook | estimate | Assumed half of Groupon first-time buyers book a second clean |
| CAC | 61.2 USD | estimate | Groupon: $60 clean sold at $30, Groupon keeps 50% → $15 in; cleaner paid $45.60 → $30.60 loss; ÷ 50% rebook = $61.20 per retained customer |
| LTV | 74.16 USD | estimate | 6 jobs × $12.36 contribution per job |
| LTV : CAC | 1.21 ratio | estimate | $74.16 ÷ $61.20 |
| Payback (months) | 2.3 months | estimate | $61.20 ÷ ($12.36 × 2.17 jobs/month = $26.78) |
| Fixed costs / month | 50000 USD/month | estimate | Seed team of ~5 in SF at ~$8k/month each + $10k ops, insurance, tools |
| Break-even | 1867 active customers | estimate | $50,000 ÷ $26.78 monthly contribution per active customer |
| Time to first revenue | 3 weeks | estimate | 2 weeks to build a booking page and recruit 10 cleaners, 1 week to the first paid clean |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|---|---|---|---|---|---|
| Pessimistic | 300 | $9,360 | $51,328 | $-41,968 | 300 active customers × 2.17 jobs × $14.40 net of cleaner pay; fixed $50k + Stripe |
| Base | 1000 | $31,200 | $54,427 | $-23,227 | 1,000 active customers; still below the 1,867 break-even |
| Optimistic | 3000 | $93,600 | $63,280 | $30,320 | 3,000 active customers in 2 metros; profitable before CAC |

## 11. Feasibility and risks

| Factor | Assessment |
|---|---|
| Build effort to a test | 2-3 weeks: booking page, Stripe, manual dispatch |
| Skills missing | Field operations, cleaner recruiting, employment law |
| Key dependencies | Cleaner supply at the offered pay; paid acquisition |
| Legal / compliance | Contractor vs employee status; NY and pending CA domestic-worker rules |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|---|---|---|---|---|
| 1 | Cleaner misclassification claim or audit | M | H | Employment counsel; W-2 option in CA | [link](https://www.dol.gov/newsroom/releases/whd/whd20110919?lang=ko) |
| 2 | Disintermediation of recurring clients | H | H | Plan pricing, insurance, replacement guarantee, non-hire clause | [link](https://www.studicata.com/summaries/united-states-district-court-northern-district-of-illinois/janice-doty-unlimited-inc-v-stoecker-1988-dry3hw/) |
| 3 | Cleaner churn breaks quality and supply | H | M | Pay above mean wage; steady schedules | [link](https://www.cleanlink.com/cp/article/Finders-Keepers--10917) |
| 4 | Funded rival copies the 60-second booking | H | M | Win density in one city first | [link](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|---|---|---|---|---|
| profit (25) | gross_margin | 2 | $60 job − $45.60 SF cleaner pay − $2.04 Stripe = 20.6% of the booking (estimate). R5: costs kill shot holds it at 2. | [link](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) |
|  | ltv_cac | 2 | LTV $74 vs CAC ~$61 = 1.2 (estimate): thin, but repeat cleans could lift it. | [link](https://blog.agrawals.org/2011/06/07/an-analysis-of-the-groupon-merchant-agreement/) |
|  | pricing_power | 1.5 | Positioned as the cheapest: $20/h under Exec's $25/h. Competes on price, no premium. | [link](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |
| feasibility (20) | build_effort | 3.5 | A booking page plus manual dispatch is weeks of work; the real build is cleaner ops. | — |
|  | skills_match | 3 | Seed-funded tech team assumed; field ops and labour-law skills not stated. | — |
|  | capital_needed | 3 | Seed covers a 1-city test; peers needed $3.3M-$24.5M to scale. | [link](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) |
| time_to_first_revenue (15) | time_to_mvp | 4 | Landing page, Stripe and 10 cleaners can go live in 2-3 weeks (estimate). | [link](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) |
|  | sales_cycle | 4.5 | Consumer, same-day purchase of a $60 clean. | — |
|  | channel_readiness | 2.5 | Paid search and Groupon exist, costs unproven; no owned audience. Liquidity hit caps at 2.5. | [link](https://blog.agrawals.org/2011/06/07/an-analysis-of-the-groupon-merchant-agreement/) |
| demand (15) | search_demand | 4 | 877,980 maids employed in the US (BLS, May 2011): a mass, recurring need. | [link](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) |
|  | trend | 3.5 | Smartphones 35% to 46% of adults in a year; TaskRabbit at 9,000 tasks/month. | [link](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/) |
|  | willingness_to_pay | 3.5 | People already pay Exec $25/h and agencies; demand is proven but price-sensitive. | [link](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |
| competition (10) | free_alternatives | 2.5 | Craigslist, forums and word of mouth find cheap cleaners free; no vetting or booking. | [link](https://www.brownstoner.com/forum-archive/2010/08/great-cleaners) |
|  | competitor_density | 2.5 | TaskRabbit ($24.5M), Exec, Zaarly, Redbeacon (Home Depot), franchises. R5 ≤ 3. | [link](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) |
|  | differentiation | 2 | Lowest price + 60-second booking: easy to copy, no data or cost moat. | [link](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |
| risk (10) | legal_regulatory | 2 | 1099 cleaners face the 2011 DOL/IRS misclassification push; CA AB 889 pending. | [link](https://www.dol.gov/newsroom/releases/whd/whd20110919?lang=ko) |
|  | platform_dependency | 4 | Owns the site and customer data; paid channels have alternatives. | — |
|  | market_risk | 4 | Cleaning is a durable, recurring household need, not a fad. | [link](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) |
| fit (5) | skills | 3 | Startup skills assumed; no stated cleaning or marketplace ops track record. | — |
|  | assets | 2.5 | Seed capital; no audience, cleaner network or contracts stated. | — |
|  | interest | 3 | Founder motivation not stated; scored neutral. | — |

| Criterion | Mean | Points |
|---|---|---|
| profit (25) | 1.83 | 9.17 |
| feasibility (20) | 3.17 | 12.67 |
| time_to_first_revenue (15) | 3.67 | 11.00 |
| demand (15) | 3.67 | 11.00 |
| competition (10) | 2.33 | 4.67 |
| risk (10) | 3.33 | 6.67 |
| fit (5) | 2.83 | 2.83 |
| **Raw total** | | **58.0** |
| **Rules applied** | none changed a score (R5 caps already met) | |
| **Final score** | | **58 / 100** |

## 13. Sources

34 sources from 27 domains: 8 primary, 19 secondary, 7 tertiary. All published on or before 2012-07-01. The two BLS pages are archived copies captured 2012-09 of data released 2012-03.

1. [TechCrunch: Exec adds messaging, Sam Altman led their round](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) — Exec $25/hour, $3.3M raised, ~100 Execs in SF, focus on cleaning — secondary — published 2012-05-31 — accessed 2026-11-11
2. [TechCrunch: Exec launches (Justin Kan)](https://techcrunch.com/2012/02/29/exec-justin-tv/) — Exec launch in SF, compared to TaskRabbit, Zaarly, Postmates — secondary — published 2012-02-29 — accessed 2026-11-11
3. [The Next Web: Exec aims to be the outsourcing app for busy professionals](https://thenextweb.com/news/giving-a-nod-to-uber-exec-aims-to-be-the-outsourcing-app-for-busy-professionals) — Exec targets busy professionals, Uber-like model — secondary — published 2012-02-29 — accessed 2026-11-11
4. [The Next Web: Exec launches company accounts](https://thenextweb.com/news/errand-running-service-exec-launches-company-accounts-to-offer-employee-perks) — Exec sells to companies as an employee perk — secondary — published 2012-03-26 — accessed 2026-11-11
5. [TechCrunch: TaskRabbit gets $17.8M](https://techcrunch.com/2011/12/13/taskrabbit-gets-17-8m-for-aggressive-expansion-wants-to-grow-internationally-and-beyond) — TaskRabbit $24.5M total, 2,000 Runners, 9,000 tasks/month, 13-30% fee — secondary — published 2011-12-13 — accessed 2026-11-11
6. [Silicon Prairie News: Zaarly raises $14.1M Series A](https://siliconprairienews.com/2011/10/zaarly-raises-14-1m-series-a-adds-former-ebay-exec-whitman-to-board) — Zaarly $14.1M Series A, local services marketplace — secondary — published 2011-10 — accessed 2026-11-11
7. [GlobeNewswire: Mayor Bloomberg welcomes Zaarly to New York](https://www.globenewswire.com/news-release/2011/12/02/1303487/0/en/Mayor-Michael-Bloomberg-Welcomes-Zaarly-to-New-York.html) — Zaarly launched in New York — primary — published 2011-12-02 — accessed 2026-11-11
8. [The Home Depot: acquires Redbeacon](https://ir.homedepot.com/news-releases/2012/01-20-2012) — Home Depot owns a marketplace of background-checked house cleaners — primary — published 2012-01-20 — accessed 2026-11-11
9. [CNN Money: Kozmo.com shuts down](https://money.cnn.com/2001/04/12/technology/kozmo/index.htm) — On-demand local service shut down in 2001 — secondary — published 2001-04-12 — accessed 2026-11-11
10. [Georgetown Voice: Kozmo delivery service closes](https://georgetownvoice.com/2001/04/19/kozmo-delivery-service-closes/) — Kozmo closed April 11, 2001 — secondary — published 2001-04-19 — accessed 2026-11-11
11. [Pew Internet: Nearly half of American adults are smartphone owners](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/) — 46% of US adults own a smartphone, up from 35% in May 2011 — primary — published 2012-03-01 — accessed 2026-11-11
12. [BLS OES May 2011: Maids and housekeeping cleaners (37-2012)](https://webarchive.library.unt.edu/web/20120926112148/http:/www.bls.gov/oes/current/oes372012.htm) — 877,980 employed; mean $10.31/h; SF division $15.20/h; NY $16.06/h (archived copy) — primary — published 2012-03 — accessed 2026-11-11
13. [BLS OES May 2011: Services to buildings and dwellings](https://webarchive.library.unt.edu/web/20120925124456/http:/www.bls.gov/oes/current/naics4_561700.htm) — 93,520 maids in NAICS 5617, median $9.13/h (archived copy) — primary — published 2012-03 — accessed 2026-11-11
14. [TechCrunch: Stripe launches](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) — Payments at 2.9% + $0.30 per charge — secondary — published 2011-09-30 — accessed 2026-11-11
15. [Agrawals blog: An analysis of the Groupon merchant agreement](https://blog.agrawals.org/2011/06/07/an-analysis-of-the-groupon-merchant-agreement/) — Groupon keeps ~50% of deal revenue, pays in thirds — tertiary — published 2011-06-07 — accessed 2026-11-11
16. [arXiv: A Month in the Life of Groupon](https://arxiv.org/pdf/1105.0903.pdf) — Groupon reportedly retains about half the revenue — secondary — published 2011-05 — accessed 2026-11-11
17. [WordStream: Most expensive AdWords keywords](https://www.wordstream.com/blog/ws/2011/07/18/most-expensive-keywords-google-adwords) — Top CPC categories in 2011; home cleaning not in the top 20 — secondary — published 2011-07-18 — accessed 2026-11-11
18. [Search Engine Watch: The 20 most expensive AdWords keyword categories](https://www.searchenginewatch.com/2011/07/19/how-google-makes-its-billions-the-20-most-expensive-adwords-keyword-categories/) — Confirms 2011 top CPC categories — secondary — published 2011-07-19 — accessed 2026-11-11
19. [HomeWork Solutions: Nanny taxes and the weekly cleaning lady](https://info.homeworksolutions.com/blog/bid/60122/Nanny-Taxes-and-the-Weekly-Cleaning-Lady) — Paying a cleaner directly makes the household an employer ($1,700 threshold) — tertiary — published 2011-02-28 — accessed 2026-11-11
20. [HomeWork Solutions: IRS and DOL misclassification enforcement steps up](https://info.homeworksolutions.com/blog/bid/76871/IRS-and-DOL-Worker-Misclassification-Enforcement-Steps-Up) — IRS Voluntary Classification Settlement Program, 2011 — tertiary — published 2011-10 — accessed 2026-11-11
21. [US DOL: Wage and Hour Division and IRS sign misclassification MOU](https://www.dol.gov/newsroom/releases/whd/whd20110919?lang=ko) — Federal misclassification initiative, 2011-09-19 — primary — published 2011-09-19 — accessed 2026-11-11
22. [Wisconsin Law Journal: Labor Dept, IRS, states join to combat misclassification](https://wislawjournal.com/2011/09/23/u-s-labor-dept-irs-states-join-to-combat-worker-misclassifications/) — 7 states sign misclassification MOUs — secondary — published 2011-09-23 — accessed 2026-11-11
23. [Holland & Knight: DOL and IRS join forces on misclassification](https://www.hklaw.com/en/insights/publications/2011/10/dol-and-irs-join-forces-to-combat-worker-misclassification) — Legal analysis of the 2011 enforcement push — secondary — published 2011-10-13 — accessed 2026-11-11
24. [Simpson Thacher: New York enacts the Domestic Workers' Bill of Rights](https://www.stblaw.com/about-us/publications/view/2010/09/02/new-york-state-enacts-the-domestic-workers-bill-of-rights) — NY overtime, weekly rest and paid days off for housekeepers — secondary — published 2010-09-02 — accessed 2026-11-11
25. [CBS New York: Paterson signs domestic worker rights bill](https://www.cbsnews.com/newyork/news/paterson-signs-domestic-worker-rights-bill) — NY law covers nannies, caregivers and housekeepers — secondary — published 2010-09-01 — accessed 2026-11-11
26. [theGrio: Paterson signs historic domestic worker rights bill](https://thegrio.com/2010/09/01/paterson-signs-historic-domestic-worker-rights-bill/) — NY domestic worker law signed — secondary — published 2010-09-01 — accessed 2026-11-11
27. [California Assembly: AB 889 committee analysis](https://www.leginfo.ca.gov/pub/11-12/bill/asm/ab_0851-0900/ab_889_cfa_20110510_150633_asm_comm.html) — CA domestic worker bill pending (overtime, breaks for housekeepers) — primary — published 2011-05-10 — accessed 2026-11-11
28. [California Senate: AB 889 committee analysis](https://www.leginfo.ca.gov/pub/11-12/bill/asm/ab_0851-0900/ab_889_cfa_20110815_140841_sen_comm.html) — AB 889 still moving through the Senate — primary — published 2011-08-15 — accessed 2026-11-11
29. [KQED Forum: A domestic worker bill of rights](https://ww2.kqed.org/forum/2011/08/12/a-domestic-worker-bill-of-rights/) — Bay Area debate on AB 889 — secondary — published 2011-08-12 — accessed 2026-11-11
30. [CleanLink Contracting Profits: Finders Keepers](https://www.cleanlink.com/cp/article/Finders-Keepers--10917) — Cleaning turnover: 75% commonly cited, up to 400% — secondary — published 2009-05-28 — accessed 2026-11-11
31. [Studicata: Janice Doty Unlimited v. Stoecker (N.D. Ill. 1988)](https://www.studicata.com/summaries/united-states-district-court-northern-district-of-illinois/janice-doty-unlimited-inc-v-stoecker-1988-dry3hw/) — Domestic staffing agencies rely on non-hire clauses against clients poaching staff — tertiary — published 1988 — accessed 2026-11-11
32. [Franchising.com: The cleanest sector of the U.S. economy](https://india.franchising.com/news/20090119_the_cleanest_sector_of_the_us_economy.html) — Residential cleaning sized at $3-4B; franchise segment growing — tertiary — published 2009-01-19 — accessed 2026-11-11
33. [Franchising.com: Molly Maid ranked in top 100 franchises](https://www.franchising.com/news/20110118_molly_maid_ranked_in_top_100_franchises_by_allbusi.html) — Incumbent franchise brands with national awareness — tertiary — published 2011-01-18 — accessed 2026-11-11
34. [Brownstoner forum: Great cleaners looking for more work](https://www.brownstoner.com/forum-archive/2010/08/great-cleaners) — Cleaners found free via neighbourhood forums and word of mouth — tertiary — published 2010-08 — accessed 2026-11-11
