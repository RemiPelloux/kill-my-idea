<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. -->

> ## 🟡 PIVOT · 59/100
> **On-demand pickup, packing and shipping for $5**
>
> `██████░░░░` 59 / 100 · confidence high, 25 sources
>
> - ❌ Each order loses an estimated **$3.38**: $6.32 revenue vs ~$9.70 courier, packing and card cost, and the fee is waived for 2+ items ([TechCrunch, 2013-09](https://techcrunch.com/2013/09/27/shyp-raises-2-1m-to-pick-up-and-ship-your-stuff/))
> - ❌ USPS already picks up for **free** and mails free boxes ([USPS, 2013-12](https://about.usps.com/news/state-releases/ny/2013/ny_2013_1226d.htm))
> - ✅ Rising demand with no direct rival: USPS parcels +6% (FY2013), US e-commerce +16.9% (2013)
>
> **Could be saved:** scheduled pickups for SF online sellers → 67/100 (hard)
> **Cheapest test:** 7 days of batched 1-hour pickup windows at a per-item fee over 200 beta orders, measuring contribution per order
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 59/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2059%2F100-yellow)

# Shyp: tap an app, a courier picks up, packs and ships — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **scored as of 2014-03-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 59/100 (raw 59.0) |
| **Confidence** | high: 18 sourced sub-scores of 21, 25 sources (7 primary) |
| **Countries** | US (San Francisco) |
| **Assumptions** | Launch city is San Francisco, where the beta runs. Full-time seed-funded team (USD 2.1M). Average postage about USD 12. Couriers are per-pickup contractors, as reported in 2013 |

## 0. Executive summary

**Answer:** **PIVOT** at 59. Demand and timing are real: parcels +6%, e-commerce +16.9%. But at $5, with packing included and the fee waived for 2+ items, each order **loses money** until route density arrives. Courier classification is also a California legal risk.

**Key findings**
1. **Each order loses money at launch**: estimated **$6.32** revenue per order against ~$9.70 for courier, packing and card fees, and the fee is waived for 2+ items (estimate) ([TechCrunch, 2013-09-27](https://techcrunch.com/2013/09/27/shyp-raises-2-1m-to-pick-up-and-ship-your-stuff/))
2. **Free USPS pickup anchors the price**: USPS picks up **free** for Click-N-Ship labels and mails free boxes, so what Shyp really charges for is the packing and not needing a printer ([USPS, 2013-12-26](https://about.usps.com/news/state-releases/ny/2013/ny_2013_1226d.htm))
3. **Courier classification is a live risk**: Shyp pays contracted couriers per pickup, while a class of ~**3,700** delivery drivers (Velocity Express) won certification in 2013 ([Sommers Schwartz, 2013-10](https://www.sommerspc.com/blog/2013/10/sommers-schwartz-attorneys-obtain-nationwide-class-certification-for-delivery-drivers/))

**Steelman:** Parcel volume and e-commerce are growing fast, nobody bundles pickup with packing, and a well-funded team can win on density. At **3+ pickups per courier-hour**, the economics turn positive. The evidence supports the demand, but Shyp's density is unproven.

**Recommendation:** Keep the beta, but don't scale consumer on-demand yet. Charge per item, batch pickups into 1-hour windows, and test a scheduled-pickup offer for SF online sellers for 7 days.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Courier and packing cost per order stays above the $5 fee, so burn grows with every order | costs_eat_margin | H | Fewer than 2 pickups per courier-hour |
| 2 | A misclassification claim forces couriers onto payroll, raising cost per pickup by 20–30% | legal_platform_risk | M | Courier pay complaints, or turnover above 30% a month |
| 3 | Consumers ship only a few times a year, so CAC is never recovered | ltv_cac | M | Under 20% of first-time users order again within 30 days |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell scheduled daily pickups to SF eBay/Etsy sellers and small shops instead of on-demand consumers | costs_eat_margin, ltv_cac: dense, recurring routes | 67/100 (estimate) | hard | 2–3 months | USD 50–100k | B2B sales motion, seller-community partnerships |
| 2 | Charge per item (drop the 2+ item waiver), add a packing fee, batch pickups into 1-hour windows | gross_margin: contribution goes from about -$3.4 to +$1 per order | 62/100 (estimate) | doable | 2 weeks | near zero | Routing logic, price test on beta users |
| 3 | Hire couriers as part-time W-2 employees from launch | legal_platform_risk | 60/100 (estimate) | hard | 1–2 months | +20–30% courier cost | Payroll, workers' comp, density to absorb the cost |

## 2. Next step: 7-day test

**Cheapest test:** 7 days of batched 1-hour pickup windows at a per-item fee over 200 beta orders, measuring contribution per order and pickups per courier-hour.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Switch beta pricing to $5 per item plus a $2 packing fee, and announce 1-hour pickup windows | At least 50 beta users see the new price |
| 2–5 | Batch pickups by neighborhood and log courier time per order | 3+ pickups per courier-hour |
| 3 | Offer scheduled daily pickups to 30 SF eBay/Etsy sellers | 5+ sellers sign up |
| 6–7 | Compute contribution per order over 200 orders | Contribution above USD 0 per order |

**Stop if:**
- fewer than 3 pickups per courier-hour by day 7 → stop expansion and rework routing;
- contribution below USD 0 per order after 200 orders → don't raise more for consumer on-demand;
- under 20% repeat within 30 days → stop paid acquisition.

## 3. Source

"Shyp: tap an app and a courier picks up, packs and ships any item for $5 plus postage, launch country US. Score it as of 2014-03-01 … Founder: a seed-funded startup."

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear (partial) | USPS gives free pickup for Click-N-Ship labels and free Priority boxes (2013-12), but the user still packs and prints | [USPS](https://about.usps.com/news/state-releases/ny/2013/ny_2013_1226d.htm) |
| 2 | Strong direct competitor | clear | No direct US pickup-pack-ship rival found before 2014-03. Postmates, TaskRabbit, Zipments and the eBay pilots are adjacent | [TechCrunch](https://techcrunch.com/2013/09/27/shyp-raises-2-1m-to-pick-up-and-ship-your-stuff/) |
| 3 | Graveyard | **hit** | Kozmo.com closed 9 markets (2001-04). Exec shut its errands service (2013-09): it lost money and "haven't been able to figure out a great way to scale it beyond SF" | [TechCrunch](https://techcrunch.com/2013/09/10/rip-lazy-times) |
| 4 | No distribution channel | clear | SF tech press, investor audiences, and iPhone loyal users at $1.33–1.90 (Fiksu, 2013) | [GlobeNewswire](https://www.globenewswire.com/news-release/2013/06/27/1033422/0/en/Mobile-App-Downloads-Climb-While-Costs-Drop-Find-New-Fiksu-Indexes.html?print=1) |
| 5 | Costs eat the margin | **hit** | $6.32 revenue per order vs ~$9.70 cost (estimate) | [Federal Register](https://www.govinfo.gov/content/pkg/FR-2013-11-20/html/2013-27728.htm) |
| 6 | Weak or falling demand | clear | USPS packages +6% in FY2013; e-commerce +16.9% in 2013 | [USPS](https://about.usps.com/news/national-releases/2013/pr13_087.pdf) |
| 7 | Legal / platform risk | **hit** | Contracted couriers paid per pickup in California amid delivery-driver class actions; the packer also has to screen for hazmat | [Sommers Schwartz](https://www.sommerspc.com/blog/2013/10/sommers-schwartz-attorneys-obtain-nationwide-class-certification-for-delivery-drivers/) |
| 8 | Saturated wave (0 look-alikes, 2013-03 to 2014-02) | clear | No near-identical consumer pickup-and-ship launches found | — |

**Primary kill shot:** costs eat the margin.

## 6. Market

- **Target customer:** SF smartphone owners aged 25–34 (81% own one, Pew 2013), and small online sellers shipping 1–10 parcels a month.
- **Pain:** finding a box, packing it, printing a label and queuing at the post office. Today they use the post office counter, carrier stores, or free USPS pickup and pack themselves.
- **Demand signals:** USPS Shipping and Package Services reached $12.5B in FY2013 ([USPS](https://about.usps.com/news/national-releases/2013/pr13_087.pdf)).
- **Trend:** rising. US e-commerce was $263.3B in 2013, up 16.9% ([Census](https://www2.census.gov/historical/ecomm/13q4.pdf)).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | USD 12.5B/year | sourced | USPS Shipping and Package Services, FY2013 |
| SAM | USD 28M/year | estimate | 840k SF residents × 56% smartphone × 1 parcel/month × $5 × 12 |
| SOM (year 1) | USD 0.5M/year | estimate | 4.7k–14k early users × 1 order/month × $5 × 12 |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| 56% of US adults own a smartphone (81% of ages 25–34) | 2013-06 | [Pew](https://www.pewresearch.org/internet/2013/06/05/smartphone-ownership-2013/) |
| US e-commerce reached $263.3B, up 16.9% | 2014-02 | [Census](https://www2.census.gov/historical/ecomm/13q4.pdf) |
| USPS package volume grew 6% while letter mail fell | 2013-11 | [USPS](https://about.usps.com/news/national-releases/2013/pr13_087.pdf) |
| Postmates raised a $16M Series B | 2014-02 | [TechCrunch](https://techcrunch.com/2014/02/18/postmates-16m-spark-capital) |
| Shyp raised $250k on AngelList in 53 minutes under the new general solicitation rules | 2013-09 | [TechCrunch](https://techcrunch.com/2013/09/27/shyp-raises-2-1m-to-pick-up-and-ship-your-stuff/) |

Smartphones went mainstream and on-demand delivery is drawing venture money, so the window is open.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | SF smartphone owners aged 25–34 and small eBay/Etsy sellers shipping 1–10 parcels a month, with no printer or boxes |
| **Where to reach them** | SF tech press · investor audiences (Tim Ferriss, Homebrew) · eBay and Etsy seller forums · Craigslist SF · SF offices and co-working spaces |
| **Pays for today** | Retail postage at the post office or carrier stores (packing fees unknown), or free USPS pickup with Click-N-Ship |
| **Budget** | unknown |
| **Trigger** | Needing to return or send an item, facing a box hunt and a queue |

**Best use:** scheduled pickups for online sellers, because they bring recurring volume and dense routes.

## 7. Competition

| Competitor | Country | What they do | Price (date) | Traction /5 | Gap |
|------------|---------|--------------|--------------|-------------|-----|
| USPS Package Pickup + free boxes | US | Free pickup of labeled parcels | $0 (2013-12) | 5 | No packing; the user needs a printer and a box |
| TaskRabbit Deliver Now | US | Local on-demand delivery in SF | $10 flat (2012-06) | 4 | No carrier shipping or packing |
| Postmates | US | On-demand courier, ~900 SF couriers | unknown | 4 | Local only, no packing |
| Zipments | US | B2B same-day courier platform, NYC | unknown | 3 | B2B, not consumer shipping |
| eBay home pickup pilots | US | Pickup and same-day pilots in SF and NYC | unknown | 5 | Pilot, for eBay sellers only |

- **Free alternatives:** USPS pickup and free boxes cover part of the job.
- **Edge:** the only bundle of pickup, packing, best carrier rate and $10k insurance. Postmates could copy it.
- **First 10 customers** come from the SF beta, tech press and investor audiences.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $5 per pickup + postage | sourced | TechCrunch 2013-09 (waived for 2+ items) |
| Variable cost per unit | $8.38 net | estimate | courier $4.9 + packing $4 + card $0.79 − $1.32 postage spread (11% Commercial Base × $12) |
| Gross margin % | −68% | estimate | ($5 − $8.38) / $5 |
| Lifetime | ~6 orders per year | estimate | Localytics 2013: 34% of users open an app 11+ times |
| Conversion rate | unknown | unknown | — |
| CAC | ~$30 | estimate | Fiksu loyal user $1.33–1.90 × 15–20 to reach a paying repeat customer |
| LTV | −$20 | estimate | 6 × −$3.38 |
| LTV : CAC | −0.68 | estimate | −$20 / $30 |
| Payback | never at current unit economics | estimate | negative monthly gross profit |
| Fixed costs / month | ~$100k | estimate | $2.1M seed / ~21 months |
| Break-even | 50,000 orders/month | estimate | only if contribution reaches +$2: $100k / $2 |
| Time to first revenue | 0 weeks | sourced | paid beta live by 2013-09 |

| Scenario | Orders / month | Revenue / month | Costs / month | Note |
|----------|----------------|-----------------|---------------|------|
| Pessimistic | 2,000 | $12,640 | $125,000 | unbatched, ~$12.5 per order |
| Base | 5,000 | $31,600 | $148,500 | $9.70 per order |
| Optimistic | 15,000 | $94,800 | $178,000 | dense routes, ~$5.2 per order |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Done: private beta live with ~10 couriers |
| Skills missing | Logistics operations at scale |
| Key dependencies | Carrier rates and terms (UPS +4.9% in 2014); courier labor supply |
| Legal / compliance | California courier classification; hazmat (lithium batteries banned in international mail); liability for $10k insurance |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Courier misclassification claim | M | H | Part-time W-2 couriers | [Sommers Schwartz](https://www.sommerspc.com/blog/2013/10/sommers-schwartz-attorneys-obtain-nationwide-class-certification-for-delivery-drivers/) |
| 2 | Lithium batteries and hazmat in "any item" | M | M | Intake screening | [USPS PB 22336](https://about.usps.com/postal-bulletin/2012/pb22336/html/updt_012.htm) |
| 3 | Carrier rate rises | H | L | Volume tiers | [Ordoro](https://blog.ordoro.com/2013/11/22/ups-2014-rate-increase/) |
| 4 | Postmates or TaskRabbit copy the bundle | M | H | Win density and seller contracts first | [The Register](https://www.theregister.co.uk/2014/02/18/postmates_funding/) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 1 | Estimated −$3.4 per order; costs_eat_margin hit |
| | LTV : CAC | 1 | Negative LTV against an estimated $30 CAC |
| | pricing power | 2.5 | Free USPS pickup anchors pickup at $0; fee waived for 2+ items |
| Feasibility (20) | build effort | 3 | App, courier operations and a packing hub; beta already live |
| | skills match | 3.5 | Seed team running a beta; ops scaling unproven |
| | capital needed | 3.5 | $2.1M covers one city |
| Time to first revenue (15) | time to MVP | 4.5 | Paid beta live by 2013-09 |
| | sales cycle | 5 | Impulse, same-day purchase |
| | channel readiness | 3.5 | Press, investor audiences, cheap iPhone installs |
| Market demand (15) | search demand | 3 | ~3.7B USPS parcels a year; no app keyword data |
| | trend | 4 | Parcels +6%, e-commerce +16.9% |
| | willingness to pay | 2.5 | Pickup is free from USPS; no paid waitlist |
| Competitive room (10) | free alternatives | 3 | USPS covers part of the job |
| | competitor density | 4 | No direct rival |
| | differentiation | 3 | Bundle is specific but copyable |
| Risk (10) | legal / regulatory | 2 | Courier classification in California; hazmat |
| | platform dependency | 3.5 | Carrier rates; no Apple cut |
| | market risk | 3.5 | Durable need; on-demand errands stalled |
| Founder fit (5) | skills | 3 | No logistics track record found |
| | assets | 3 | Investor network |
| | interest | 3 | Not documented |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 1.5 | 7.5 |
| Feasibility (20) | 3.33 | 13.33 |
| Time to first revenue (15) | 4.33 | 13.0 |
| Market demand (15) | 3.17 | 9.5 |
| Competitive room (10) | 3.33 | 6.67 |
| Risk (10) | 3.0 | 6.0 |
| Founder fit (5) | 3.0 | 3.0 |
| **Raw total** | | **59.0** |
| **Rules applied** | none (R5 coherence already satisfied) | |
| **Final score** | | **59 / 100** |

## 13. Sources

25 sources from 14 domains: 7 primary, 17 secondary, 1 tertiary. All were published on or before 2014-03-01 and accessed 2026-11-11. The full list, with tiers and dates, is in `report.html` and `verdict.json`.
