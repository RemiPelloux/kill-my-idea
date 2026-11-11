<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟡 PIVOT · 59/100
> **On-demand laundry and dry-cleaning pickup by app**
>
> `██████░░░░` 59 / 100 · confidence medium, 27 sources
>
> - ❌ About **17%** gross margin per 15-lb order once the partner cleaner and an LA driver at $13.21/hr are paid (estimate; [BLS, 2011](https://webarchive.library.unt.edu/web/20120921092933/http:/www.bls.gov/oes/current/oes435021.htm))
> - ❌ Errand delivery has failed before: MyLackey, which picked up dry cleaning, burned $8M in 16 months and laid off 85 people ([Everett Herald, 2000](https://www.heraldnet.com/news/seattle-based-mylackey-com-to-shut-down/))
> - ✅ A weekly need worth about $22B a year, and almost no app-first competitor before June 2013 (SpotlessCity: $200k seed, NYC only)
>
> **Could be saved:** dry cleaning first, a flat delivery fee and batched routes in 2–3 dense zip codes → 64/100 (hard)
> **Cheapest test:** a 7-day concierge pilot in one LA zip code with one partner cleaner and the founders driving; it must reach 2+ orders per driver-hour
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 59/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2059%2F100-yellow)

# Washio: on-demand laundry and dry-cleaning pickup by app — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **scored as of 2013-06-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 59/100 (raw 59.3) |
| **Confidence** | medium: 13 sourced sub-scores of 21, 27 sources (5 primary) |
| **Countries** | US (Los Angeles assumed) |
| **Assumptions** | Seed-funded team with roughly USD 0.5–1.5M. Launch city Los Angeles. Outsourced model: partner cleaners and contractor drivers. Orders of 15 lb at $1.75/lb, $0.85/lb wholesale, 0.5 driver-hour per order. Headless run, no questions asked. |

## 0. Executive summary

**Answer:** PIVOT at **59**. Demand is real and the field is nearly empty, but outsourced cleaning plus a paid driver leaves about **17%** gross margin. Prove route density and pricing in one zip code before spending the seed round.

**Key findings**
1. **The driver eats the margin**: estimated **17%** gross margin per 15-lb order ($4.51 of $26.25), with LA couriers at $13.21/hr (BLS, 2011). At 1 order per driver-hour it falls to 2%. ([source](https://webarchive.library.unt.edu/web/20120921092933/http:/www.bls.gov/oes/current/oes435021.htm))
2. **Errand delivery has failed before**: MyLackey burned **$8M in 16 months** and laid off 85 people (2000), and Kozmo closed all 9 of its markets (2001). ([source](https://www.heraldnet.com/news/seattle-based-mylackey-com-to-shut-down/))
3. **Open field, and smartphones are here**: the only direct player found was SpotlessCity ($200k seed, 3 NYC neighborhoods), while **46%** of US adults owned a smartphone (Pew, 2012). ([source](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/))

**Steelman:** The need is weekly and worth more than $20B a year, smartphone ownership has reached 46%, and no funded app-first competitor exists in LA. A same-day purchase with Uber-style referral credits could take a whole city. The evidence supports the demand and the timing. It does not yet support the unit economics.

**Recommendation:** Run a 7-day concierge pilot in one dense LA zip code. Build the full app and spend on ads only if drivers reach **2+ orders per hour** at $6+ gross profit per order.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Driver time per order kept contribution margin near zero, so growth burned the seed round | costs_eat_margin | H | Fewer than 2 orders per driver-hour by week 3 |
| 2 | Customers went back to their cleaner's free delivery or their own washer once promo credits ran out | differentiation | M | Under 30% of first-time customers reorder within 30 days |
| 3 | A driver misclassification claim put employee costs on every order | legal_platform_risk | M | Drivers working 30+ hours a week only for the platform, in its branded gear |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Lead with dry cleaning in 2–3 dense LA zip codes, add a flat $5.99 delivery fee and batch pickups into fixed time windows | gross_margin, ltv_cac (costs_eat_margin) | 64/100 (estimate) | hard | 2–3 months of route and price tests | within the seed budget | Dispatch software, density data, a partner cleaner with volume pricing |
| 2 | Sell through luxury apartment buildings and office perk programs instead of paid ads | channel_readiness, route density (liquidity) | 63/100 (estimate) | doable | 2 weeks to sign 2 pilot buildings | under USD 5k | Introductions to property managers, a concierge drop box |
| 3 | Run its own small cleaning plant instead of paying partner wholesale | gross_margin, but raises capital_needed | 61/100 (estimate) | very-hard | 6+ months | USD 250k+ | Plant operator, permits, environmental compliance |

## 2. Next step: 7-day test

**Cheapest test:** a 7-day concierge pilot in one dense LA zip code: a landing page, ordering by SMS, one partner cleaner, and the founders driving. Measure orders per driver-hour and margin.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Sign one partner cleaner at a fixed wholesale rate per lb and per item | Signed rate sheet at or below $0.85/lb |
| 2 | Launch a landing page with SMS ordering and a $5.99 delivery fee | Page live, payments working |
| 3 | Spend $300 on Facebook ads targeted at the zip code, and flyer 2 apartment buildings | CAC under $30 per first order |
| 4–6 | Founders run pickups in two fixed evening windows and log every minute | 2+ orders per driver-hour |
| 7 | Compute gross profit per order and the intent to reorder | 30+ paid orders, $6+ gross profit per order |

**Stop if:**
- Fewer than 30 paid orders by day 7.
- Fewer than 2 orders per driver-hour by day 14: stop scaling and redesign the routes.
- Fewer than 30% of customers reorder by day 30.
- Gross profit is under USD 6 per order by day 30: raise the price or stop.

## 3. Source

"Washio: on-demand laundry and dry-cleaning pickup and delivery ordered by app, launch country US. Score it as of 2013-06-01: use only evidence published on or before that date (set verdict.as_of). Founder: a seed-funded startup. Just go: do not ask questions. Use the slug washio."

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear | DIY laundry, laundromats and cleaners' free delivery cover part of the job, but dry cleaning still needs a paid professional | [1-800-DryClean, 2008](https://franchisors.franchising.com/news/20081212_1800dryclean_franchise_adds_free_office_pick_up_an.html) |
| 2 | Strong direct competitor | clear | SpotlessCity raised only $200k (2012-05). No player showed $5M+ raised or 100k users | [TechCrunch](https://techcrunch.com/2012/05/22/spotlesscity-just-brought-the-dry-cleaning-industry-online) |
| 3 | Graveyard | **hit** | MyLackey (errands, including dry-cleaning pickup): $8M burned, 85 laid off (2000-10). Kozmo closed 9 markets (2001-04). Streamline closed | [Everett Herald](https://www.heraldnet.com/news/seattle-based-mylackey-com-to-shut-down/), [CNNMoney](https://money.cnn.com/2001/04/12/technology/kozmo/index.htm) |
| 4 | No distribution channel | clear | Facebook CPC ~$0.55 ÷ 2% conversion ≈ $27.50 CAC (estimate), below the ~$108 first-year gross profit (estimate). Referral credits also work | [Spruce Media, 2013-01](https://www.globenewswire.com/news-release/2013/01/29/1146983/0/en/In-Advance-of-Facebook-s-Q4-2012-Earnings-Call-Spruce-Media-Releases-State-of-Facebook-Advertising-Report-2012.html?print=1) |
| 5 | Costs eat the margin | **hit** | Estimated 17%: $26.25 order − $12.75 wholesale − $7.93 driver − $1.06 card fees | [BLS OES](https://webarchive.library.unt.edu/web/20120921092933/http:/www.bls.gov/oes/current/oes435021.htm) |
| 6 | Weak or falling demand | not checked | No dated trend for US cleaning spend before 2013. Every source on the casual-dress decline was published after 2013, so they were excluded | — |
| 7 | Legal / platform risk | **hit** | Estrada v. FedEx Ground (CA, 2007): contractor drivers were held to be employees, and review was denied in 2007-11 | [Proskauer](https://calemploymentlawupdate.proskauer.com/2007/09/fedex-drivers-were-employees-for-purposes-of-obtaining-reimbursement-for-expenses/), [Law.com](https://law.com/corpcounsel/2007/11/29/california-supreme-court-denies-fedex-appeal) |
| 8 | Saturated wave (0 look-alike launches, 2012-06 to 2013-06) | clear | SpotlessCity launched in 2012-01, before the window. No other launch could be dated inside it | [TechCrunch](https://techcrunch.com/2012/03/28/spotlesscity-will-pick-up-your-soiled-dirty-laundry/amp/) |

**Primary kill shot:** costs_eat_margin.

**Type checks (marketplace):**
- **Liquidity: unknown.** Cleaners with spare capacity are easy to sign. No benchmark was found for how many orders a neighborhood needs before routes pay.
- **Disintermediation: hit.** Cleaners already offered free pickup and delivery ([1-800-DryClean, 2008](https://franchisors.franchising.com/news/20081212_1800dryclean_franchise_adds_free_office_pick_up_an.html)).

## 6. Market

- **Target customer:** professionals aged 25–40 in dense LA neighborhoods who rent without an in-unit washer (assumption).
- **Pain:** cleaners' opening hours clash with work, and laundry takes hours every week. Today they drop off at a cleaner or laundromat, or use their own washer.
- **Demand signals:** about 41,906 cleaning establishments and ~$20.4B in receipts (2002 Census, via [American Laundry News, 2007](https://americanlaundrynews.com/node/66017)).
- **Trend:** unknown. No dated pre-2013 source was found.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | ~$22.4B/year | estimate | $20.4B employer receipts (2002) + ~$2.0B nonemployer receipts (2007, [Statistical Abstract 2012](https://webarchive.library.unt.edu/web/20120916202359/http://www.census.gov/prod/2011pubs/12statab/services.pdf)) |
| SAM | ~$2.2B/year | estimate | 10% of TAM: smartphone-owning urban households (assumption) |
| SOM (year 1) | ~$2.2M | estimate | 0.1% of SAM, one-city launch |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| US smartphone ownership went from 35% to 46% of adults | 2011-05 to 2012-02 | [Pew](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/) |
| On-demand errand apps got funded (Exec, in a round led by Sam Altman) | 2012-05 | [TechCrunch](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) |
| Give-get referral credits proved themselves as a launch channel | 2012-06 | [Uber](https://www.uber.com/us/en/newsroom/personal-promo-code) |
| Facebook CPC averaged ~$0.55 | Q4 2012 | [Spruce Media](https://www.globenewswire.com/news-release/2013/01/29/1146983/0/en/In-Advance-of-Facebook-s-Q4-2012-Earnings-Call-Spruce-Media-Releases-State-of-Facebook-Advertising-Report-2012.html?print=1) |

MyLackey had no smartphones and no cheap mobile ads in 2000. Both exist in 2013. What a driver costs has not changed.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Professionals aged 25–40 in Santa Monica, West Hollywood and Downtown LA who rent without an in-unit washer (assumption) |
| **Where to reach them** | Facebook ads by zip code, luxury apartment buildings and their concierges, office perk programs, Yelp, the iPhone App Store |
| **Pays for today** | Drop-off dry cleaning and wash & fold. Dated 2012 LA prices are unknown |
| **Budget** | unknown |
| **Trigger** | A busy week, a trip, or a suit needed on Monday morning |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Consumer on-demand wash & fold and dry cleaning | Individual renters | Medium |
| 2 | Building amenity: pickup from the apartment concierge | Residents | Low: one stop, many orders |
| 3 | Employee perk at offices | Employees or employer | Medium |

**Best option:** the building amenity. Many orders per stop is the only lever that fixes the driver cost.

## 7. Competition

| Competitor | Country | What they do | Price (date) | Traction /5 | Gap |
|------------|---------|--------------|--------------|-------------|-----|
| [SpotlessCity](https://techcrunch.com/2012/05/22/spotlesscity-just-brought-the-dry-cleaning-industry-online) | US | Web marketplace connecting customers to local cleaners, NYC | ~10% commission from cleaners (2012-05) | 2 | NYC only, web-first |
| [1-800-DryClean](https://franchisors.franchising.com/news/20081212_1800dryclean_franchise_adds_free_office_pick_up_an.html) | US | Franchise with free pickup and delivery | free delivery (2008-12) | 3 | Scheduled routes, no app |
| [Exec](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) | US | On-demand errands and cleaning | unknown | 3 | Not specialized in laundry |
| [Laundry Locker](https://www.crunchbase.com/organization/laundry-locker) | US | 24/7 locker drop-off, SF | unknown | 2 | No door pickup |
| Do it yourself | US | Own washer or laundromat | $0 extra | 5 | Takes hours, can't dry clean |

- **Free alternatives:** home washers and cleaners' free delivery. Both cover part of the job.
- **Edge:** on-demand timing through the app. It is real but easy to copy. The only real moat is route density.
- **First 10 customers** come from one apartment building, a zip-code-targeted Facebook campaign, and referral credits.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $26.25/order | estimate | 15 lb × $1.75/lb (assumption) |
| Variable cost per unit | $21.74 | estimate | 12.75 wholesale + 7.93 driver (0.5 h × $13.21 × 1.2) + 1.06 card fees |
| Gross margin % | 17% | estimate | 4.51 ÷ 26.25. 2% at 1 order per driver-hour, 27% at $2.00/lb |
| Churn / lifetime | 12 orders | estimate | ~6 months at 2 orders a month (assumption) |
| Conversion rate | 2% | estimate | click to first order (assumption) |
| CAC | $27.50 | estimate | $0.55 CPC ÷ 2% |
| LTV | $54.10 | estimate | 12 × $4.51 |
| LTV : CAC | 1.97 | estimate | 54.1 ÷ 27.5 |
| Payback (months) | 3.0 | estimate | 27.5 ÷ (2 × 4.51) |
| Fixed costs / month | $40,000 | estimate | 4-person team at ~$8k loaded each + $8k overhead (assumption) |
| Break-even (customers / month) | ~4,435 active | estimate | 40,000 ÷ 9.02 |
| Time to first revenue (weeks) | 2 | estimate | concierge pilot |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 500 | $26,250 | $61,740 | −$35.5k | 1 order per driver-hour, ~2% gross margin |
| Base | 1,500 | $78,750 | $105,220 | −$26.5k | 17% gross margin |
| Optimistic | 4,500 | $270,000 | $237,000 | +$33k | more dry cleaning, $2/lb, 3 orders per driver-hour |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | About 1 week for a concierge SMS version, 1–2 months for an app |
| Skills missing | Logistics, dispatch and route operations (assumption) |
| Key dependencies | Partner cleaners, driver supply, Apple App Store (orders paid outside in-app purchase, so no 30% cut) |
| Legal / compliance | California contractor law (Borello, Estrada), liability for lost or damaged garments |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Low route density: driver time eats the margin | H | H | Fixed windows, one zip code at a time | [BLS](https://webarchive.library.unt.edu/web/20120921092933/http:/www.bls.gov/oes/current/oes435021.htm) |
| 2 | Drivers reclassified as employees | M | H | Courier firms or W-2 drivers | [Proskauer](https://calemploymentlawupdate.proskauer.com/2007/09/fedex-drivers-were-employees-for-purposes-of-obtaining-reimbursement-for-expenses/) |
| 3 | Customers bypass the app for the cleaner's own delivery | M | M | Unbranded bags, exclusive partners | [1-800-DryClean](https://franchisors.franchising.com/news/20081212_1800dryclean_franchise_adds_free_office_pick_up_an.html) |
| 4 | Unclear liability for lost or damaged garments | M | M | Written partner terms, insurance | — |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 1.5 | Estimated 17% after wholesale, driver and card fees. Kill shot costs_eat_margin (R5 ≤ 2) |
| | LTV : CAC | 2.5 | LTV $54 vs CAC ~$27.50: ~2.0 |
| | pricing power | 2 | Cleaners already deliver free |
| Feasibility (20) | build effort | 3.5 | Concierge version in about a week |
| | skills match | 3 | Can build the app; operations unproven |
| | capital needed | 3 | Seed money covers one city. MyLackey burned $8M in 16 months |
| Time to first revenue (15) | time to MVP | 3.5 | Paid orders within 1–2 weeks |
| | sales cycle | 4.5 | Same-day consumer purchase |
| | channel readiness | 2.5 | Channels exist, no audience yet |
| Market demand (15) | search demand | 4 | ~42k establishments, ~$20.4B in receipts |
| | trend | 3 | No dated trend; treated as flat |
| | willingness to pay | 3.5 | People already pay for cleaning; a delivery premium is unproven |
| Competitive room (10) | free alternatives | 2.5 | Home washers and free delivery cover part of the job |
| | competitor density | 4 | Few direct players before June 2013 |
| | differentiation | 2.5 | On-demand timing is easy to copy |
| Risk (10) | legal / regulatory | 2.5 | Contractor-driver precedent (Estrada) |
| | platform dependency | 3.5 | Orders are paid outside Apple in-app purchase; web booking is an alternative |
| | market risk | 4.5 | Durable weekly need |
| Founder fit (5) | skills | 3 | Logistics record unknown |
| | assets | 2 | Capital only |
| | interest | 3 | Not stated |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 2.00 | 10.0 |
| Feasibility (20) | 3.17 | 12.7 |
| Time to first revenue (15) | 3.50 | 10.5 |
| Market demand (15) | 3.50 | 10.5 |
| Competitive room (10) | 3.00 | 6.0 |
| Risk (10) | 3.50 | 7.0 |
| Founder fit (5) | 2.67 | 2.7 |
| **Raw total** | | **59.3** |
| **Rules applied** | none changed a score (R5 is satisfied: gross_margin 1.5 ≤ 2, legal 2.5 ≤ 2.5) | |
| **Final score** | | **59 / 100** |

## 13. Sources

27 sources, 5 primary. Every source is dated on or before 2013-06-01, or has no date (3: the two Supermarket News items and Crunchbase). Sources published after 2013, such as later Washio and Prim coverage, the casual-dress decline and current price pages, were excluded on purpose.

1. [Everett Herald: MyLackey.com to shut down](https://www.heraldnet.com/news/seattle-based-mylackey-com-to-shut-down/) — graveyard — secondary — 2000-10-23
2. [Salon: MyLackey](https://salon.com/2000/06/05/mylackey) — graveyard — secondary — 2000-06-05
3. [CNNMoney: Kozmo](https://money.cnn.com/2001/04/12/technology/kozmo/index.htm) — graveyard — secondary — 2001-04-12
4. [Georgetown Voice: Kozmo closes](https://georgetownvoice.com/2001/04/19/kozmo-delivery-service-closes/) — graveyard — tertiary — 2001-04-19
5. [Supermarket News: Streamline](https://www.supermarketnews.com/archive/streamline-close-victim-losses-tight-capital) — graveyard — secondary — undated
6. [Supermarket News: ShopLink](https://supermarketnews.com/grocery-operations/funding-woes-abruptly-shut-down-shoplink) — graveyard — secondary — undated
7. [American Laundry News: Census](https://americanlaundrynews.com/node/66017) — market size — secondary — 2007-10-18
8. [US Census Statistical Abstract 2012](https://webarchive.library.unt.edu/web/20120916202359/http://www.census.gov/prod/2011pubs/12statab/services.pdf) — nonemployer receipts — primary — 2011
9. [Pew: smartphone owners](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners/) — why now — primary — 2012-03-01
10. [Pew: Sept 2012 update](https://www.pewresearch.org/internet/2012/09/11/smartphone-ownership-update-september-2012/markdown) — why now — primary — 2012-09-11
11. [TechCrunch: Exec](https://techcrunch.com/2012/05/31/exec-the-mobile-app-for-errands-adds-messaging-oh-and-sam-altman-led-their-round/amp/) — competitor, why now — secondary — 2012-05-31
12. [TechCrunch: Exec San Diego](https://techcrunch.com/2013/02/05/exec-redesign-san-diego-launch) — competitor — secondary — 2013-02-05
13. [Tech.co: Exec expands cleaning](https://tech.co/news/execs-expands-on-demand-cleaning-2013-03) — competitor — secondary — 2013-03
14. [The Next Web: Exec company accounts](https://thenextweb.com/news/errand-running-service-exec-launches-company-accounts-to-offer-employee-perks) — B2B channel — secondary — 2012-03-26
15. [TechCrunch: SpotlessCity funding](https://techcrunch.com/2012/05/22/spotlesscity-just-brought-the-dry-cleaning-industry-online) — competitor — secondary — 2012-05-22
16. [TechCrunch: SpotlessCity launch](https://techcrunch.com/2012/03/28/spotlesscity-will-pick-up-your-soiled-dirty-laundry/amp/) — competitor — secondary — 2012-03-28
17. [Crunchbase: Laundry Locker](https://www.crunchbase.com/organization/laundry-locker) — competitor — tertiary — undated
18. [Proskauer: Estrada v. FedEx](https://calemploymentlawupdate.proskauer.com/2007/09/fedex-drivers-were-employees-for-purposes-of-obtaining-reimbursement-for-expenses/) — legal — secondary — 2007-09-01
19. [Law.com: CA Supreme Court denies FedEx appeal](https://law.com/corpcounsel/2007/11/29/california-supreme-court-denies-fedex-appeal) — legal — secondary — 2007-11-29
20. [TechCrunch: App Store guidelines](https://techcrunch.com/?p=217671) — platform — secondary — 2010-09-09
21. [1-800-DryClean free pickup](https://franchisors.franchising.com/news/20081212_1800dryclean_franchise_adds_free_office_pick_up_an.html) — free alternative, disintermediation — tertiary — 2008-12-12
22. [1-800-DryClean 2011 expansion](https://www.franchising.com/amp/news/20110110_1800drycleanr_franchise_ranks_among_the_2011_franc.html) — competitor — tertiary — 2011-01-10
23. [Fiksu Nov 2012](https://prnewswire.com/news-releases/mobile-marketing-costs-spiked-in-november-while-app-downloads-dropped-report-fiksu-indexes-185042751.html) — app acquisition cost — secondary — 2012-12-28
24. [Fiksu Jul 2012](https://prnewswire.com/news-releases/mobile-app-marketing-costs-continued-their-upward-climb-report-the-fiksu-july-indexes-168134916.html) — app acquisition cost — secondary — 2012-08
25. [Spruce Media: Facebook ads 2012](https://www.globenewswire.com/news-release/2013/01/29/1146983/0/en/In-Advance-of-Facebook-s-Q4-2012-Earnings-Call-Spruce-Media-Releases-State-of-Facebook-Advertising-Report-2012.html?print=1) — CAC — secondary — 2013-01-29
26. [Uber: personal promo codes](https://www.uber.com/us/en/newsroom/personal-promo-code) — referral channel — primary — 2012-06-06
27. [BLS OES: couriers](https://webarchive.library.unt.edu/web/20120921092933/http:/www.bls.gov/oes/current/oes435021.htm) — driver cost — primary — 2012-09-21

All accessed 2026-11-11.
