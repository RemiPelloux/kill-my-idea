<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 49/100
> **$699 Wi-Fi juicer with subscription produce packs**
>
> `█████░░░░░` 49 / 100 · confidence high, 42 sources
>
> - ❌ Each $6.50 pack keeps an estimated **28%** margin after produce and cold-chain delivery; bottled juice targets ~60% ([Goodnature, 2014](https://goodnature.com/blog/calculating-food-costs-for-cold-pressed-juice))
> - ❌ Locked-pod machines are stalling: Keurig's CEO blamed pod DRM for a **23%** sales drop ([TechCrunch, 2015-05](https://techcrunch.com/2015/05/08/keurig-ceo-blames-coffee-pod-drm-for-falling-sales/amp/))
> - ✅ Demand is real: super-premium cold-pressed juice grew 130.5% a year ([IRI via Evolution Fresh, 2015-04](https://perishablenews.com/?p=121471))
>
> **Could be saved:** drop the press, sell HPP bottled juice through grocery → 56/100 (hard)
> **Cheapest test:** 7-day Bay Area fake-door: $699 pre-order with $50 deposit, plus a hand-delivered pack trial to 20 households
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 49/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2049%2F100-red)

# Juicero — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **as of 2016-03-01**: only evidence published on or before that date |
| **Verdict** | NO-GO · 49/100 (raw 48.8) |
| **Confidence** | high: 16 sourced sub-scores of 21, 42 sources (8 primary) |
| **Countries** | US |
| **Assumptions** | Pack price $6.50 (midpoint of $5–8); pack yield ~8 oz; 5 packs a week; direct online channel; funded hardware team; no questions asked ("just go") |

## 0. Executive summary

**Answer:** **NO-GO** at 49. Cold-pressed demand is real and rising, but each $6.50 pack keeps an estimated **28%** margin after cold-chain delivery, and Keurig just showed buyers resist pricey locked-pod machines.

**Key findings**
1. **Packs keep an estimated 28% margin**: at ~10 oz of juice per lb of produce, an 8oz pack costs **$4.70** to make and ship cold, against $6.50; bottled juice targets ~60% ([Goodnature, 2014-09](https://goodnature.com/blog/calculating-food-costs-for-cold-pressed-juice))
2. **Cheaper juice is everywhere and falling**: Suja cut its 16oz to $7.99 and launched **$3.99** bottles; Costco sells it at $0.17/oz; juicers cost $70–$400 ([FoodNavigator, 2015-01](https://www.foodnavigator.com/Article/2015/01/22/HPP-cold-pressed-Suja-Juice-predicts-2015-revenues-of-70-80m))
3. **Locked-pod machines are stalling**: Keurig's CEO blamed pod DRM for a **23%** sales drop; its $369 Kold drew price criticism ([TechCrunch, 2015-05](https://techcrunch.com/2015/05/08/keurig-ceo-blames-coffee-pod-drm-for-falling-sales/amp/))

**Steelman:** Affluent buyers already pay up to $10 a bottle and cold-pressed grows 75–130% a year; a home press could own a daily habit the way Keurig owned coffee. The evidence: Keurig's own pod model is stalling, and pack margins look thin.

**Recommendation:** Do not build the $699 press as specified. If the team proceeds, test a 7-day Bay Area pre-order and measured cold-chain box cost before tooling.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Packs cost nearly what they sell for once cold-chain delivery is paid, so growth deepens losses | costs_eat_margin | H | Cold-chain cost above $10 per weekly box |
| 2 | Buyers balk at $699 when a $260 juicer or a $3.99 bottle does most of the job | pricing_power | H | Under 0.5% of landing-page visitors pre-order |
| 3 | The pack lock and Wi-Fi check trigger Keurig-style backlash or bricked machines | legal_platform_risk | M | Over 5% of support tickets about rejected packs or offline machines |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Drop the press: sell the same organic juice as HPP bottles through grocery | costs_eat_margin (~60% bottled margin), build_effort; still faces Suja | 56/100 (estimate) | hard | 6 months | USD 2–5M | Beverage distribution contacts, a brand that beats Suja on shelf |
| 2 | Sell the press to offices, gyms and cafés with daily pack volume | contribution_margin: one cold-chain drop serves 30+ packs a day | 52/100 (estimate) | hard | 3–6 months | USD 0.5–1M | B2B sales and a delivery route in one metro |
| 3 | Open the system: no pack lock, packs as convenience in one metro | legal_platform_risk, Keurig 2.0 graveyard pattern | 50/100 (estimate) | hard | 3 months | USD 0.5M | Accepting a lower pack attach rate |

## 2. Next step: 7-day test

**Cheapest test:** 7-day Bay Area fake-door: $699 pre-order with a $50 refundable deposit, plus a hand-delivered pack trial to 20 households.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Landing page: $699 pre-order, $50 refundable deposit, $6.50 packs | 1,000 targeted visitors from $300 of Facebook ads |
| 1–2 | Hand-deliver 7 prototype packs a week to 20 recruited households | 20 households enrolled |
| 3–4 | Track pack use and ask willingness to pay per pack | ≥3 packs used per household per week |
| 5 | Ship one real cold-chain box by courier, log full cost | Box cost under $10 for 7 packs |
| 7 | Count deposits, compute CAC per deposit | 300+ deposits, or CAC per deposit under $100 |

**Stop if:** fewer than 300 deposits by day 7; cold-chain cost above $10 per box on day 5; fewer than 3 packs a week per household by day 7.

## 3. Source

> Juicero: a $699 Wi-Fi juicer that presses proprietary produce packs sold by subscription at $5 to $8 each, launch country US. Score it as of 2016-03-01. Founder: a funded hardware startup.

Note: no source published on or before 2016-03-01 confirms the $699 or $5–8 prices; they come from the brief.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear | No free equivalent; home juicers $70–$400 (2015-06) | [Tasting Table](https://www.tastingtable.com/690658/best-juicers-2015-hurom-omega-hamilton-beach) |
| 2 | Strong direct competitor | **hit** | Suja $45M revenue 2014; Coca-Cola paid $90M for 30% (2015-08) | [BeverageDaily](https://www.beveragedaily.com/Article/2015/08/19/Coca-Cola-makes-90m-investment-in-Suja-Juice-to-take-30-stake) |
| 3 | Graveyard | **hit** | Keurig 2.0 DRM cut sales 23% (2015-05); Kold at $369 criticised; Quirky bankrupt (2015-09); Organic Avenue closed (2015-10) | [TechCrunch](https://techcrunch.com/2015/05/08/keurig-ceo-blames-coffee-pod-drm-for-falling-sales/amp/) |
| 4 | No distribution channel | clear | Direct online + tech press; est. CAC $200 vs ~$470 first-year gross profit | [Retail Dive](https://www.retaildive.com/news/facebooks-mobile-network-delivers-lower-costs-for-advertisers/402152) |
| 5 | Costs eat the margin | **hit** | Est. $4.70 per 8oz pack leaves 28% at $6.50 | [Goodnature](https://goodnature.com/blog/calculating-food-costs-for-cold-pressed-juice) |
| 6 | Weak or falling demand | clear | Cold-pressed +130.5% YoY (IRI, to 2015-03) | [PerishableNews](https://perishablenews.com/?p=121471) |
| 7 | Legal / platform risk | **hit** | Raw-produce plant under 2015 FSMA rules; Keurig lock antitrust suits (2014-02); Wink hubs bricked (2015-04) | [Federal Register](https://www.govinfo.gov/content/pkg/FR-2015-09-17/html/2015-21920.htm) |
| 8 | Saturated wave (0 connected juicers, 2015-03 to 2016-03) | clear | ~6 other connected-kitchen launches (June, Teforia, Whirlpool), none a juicer | [Fortune](https://fortune.com/2016/01/06/home-appliances-ces-2016/) |

**Primary kill shot:** costs eat the margin.

**Type checks (ecommerce):** contribution_margin **hit**: est. ~$15 (33%) per box at 7 packs, ~$0 at 3 packs, since cold-chain shipping is fixed per box ([Fortune, 2015-08](https://fortune.com/2015/08/03/freshrealm-cold-delivery/)). returns_shipping clear: est. 15% × ~$245 ≈ $37 per press (5% of price) ([Channel Insider](https://www.channelinsider.com/news-and-trends/consumer-electronics-industry-faces-a-projected-17-billion-product-returns-bill-accenture/)).

## 6. Market

- **Target customer:** affluent, health-focused urban households (Bay Area, NYC, LA) buying cold-pressed juice several times a week.
- **Pain:** $8–12 bottles add up; home juicing is slow and messy.
- **Demand signals:** US juice bars $2.2B, +3.8% in 2014 (IBISWorld, 2014-05); Suja $18M → $45M (2013–2014).
- **Trend:** rising; HPP/organic juice +75.2% (IRI/SPINS, 2014-11), cold-pressed +130.5% (IRI, 2015-03).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $1.6B/yr US super-premium juice | sourced | [IRI via PerishableNews, 2015-04](https://perishablenews.com/?p=121471) |
| SAM | $844.6M/yr cold-pressed + flash-pasteurized | sourced | same |
| SOM (year 1) | $11.9M | estimate | 5,000 households × ($699 + 260 packs × $6.50) |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Super-premium cold-pressed juice +130.5% a year | 2015-03 | [PerishableNews](https://perishablenews.com/?p=121471) |
| Blue Apron ships 3M meals a month, $2B valuation | 2015-06 | [TechCrunch](https://techcrunch.com/2015/06/09/blue-apron-cooks-up-135-million-in-series-d-funding) |
| Coca-Cola pays $90M for 30% of Suja | 2015-08 | [BeverageDaily](https://www.beveragedaily.com/Article/2015/08/19/Coca-Cola-makes-90m-investment-in-Suja-Juice-to-take-30-stake) |
| Connected kitchen at CES 2016 (Whirlpool, Samsung, Bosch) | 2016-01 | [Fortune](https://fortune.com/2016/01/06/home-appliances-ces-2016/) |

Demand and subscription habits are in place, but Suja moving to $3.99 shows the premium window is narrowing.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Affluent, health-focused urban households already buying cold-pressed juice several times a week |
| **Where to reach them** | Pressed Juicery and Juice Press stores; Whole Foods juice aisles; boutique fitness studios; tech and wellness press; juice-cleanse communities |
| **Pays for today** | Up to $10 per 16oz bottle (HuffPost, 2014-03); ~$65/day delivered cleanse |
| **Budget** | unknown; a daily $8–10 habit implies $2,000–3,600/yr (estimate) |
| **Trigger** | Starting a cleanse or health reset, or tiring of $10 bottles and juicer cleanup |

## 7. Competition

| Competitor | Country | What they do | Price (date) | Traction /5 | Gap |
|------------|---------|--------------|--------------|-------------|-----|
| Suja | US | HPP cold-pressed bottles | $3.99–7.99 (2015-01) | 5 | Bottled, not fresh at home |
| Evolution Fresh (Starbucks) | US | Grocery cold-pressed | $3.99–4.79 (2015-04) | 4 | Mass-market bottles |
| Jamba cold-pressed | US | In-store bottles | $5.39 (2014-09) | 4 | Store visit needed |
| Pressed Juicery | US | Juice chain + delivery | ~$10 (2011-07, dated) | 3 | Premium price |
| Omega J8004 | US | Masticating juicer | $260–300 (2015-06) | 4 | Prep and cleanup |
| Hurom Elite | US | Masticating juicer | $400 (2015-06) | 3 | Prep and cleanup |
| Hamilton Beach Big Mouth | US | Centrifugal juicer | $70 (2015-06) | 4 | Lower juice quality |

- **Free alternatives:** none does the whole job; an owned blender or juicer covers part of it.
- **Edge:** the only connected juicer found; fresh-pressed at home with no cleanup.
- **First 10 customers:** Bay Area tech-press coverage and the founders' investor network.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $6.50/pack | estimate | midpoint of $5–8 |
| Variable cost per unit | $4.70/pack | estimate | produce $1.75 + pouch/labor $0.75 + cold chain $2.00 + spoilage $0.20 |
| Gross margin % | 27.7% | estimate | (6.50 − 4.70) / 6.50 |
| Churn / lifetime | 10%/month, 10 months | estimate | assumption, no pre-2016 benchmark |
| Conversion rate | 0.75% | estimate | US e-commerce 3.06% (Monetate 2015), lowered for a $699 purchase |
| CAC | $200 | estimate | CPC $0.31–2.32 ÷ 0.5–1% |
| LTV | $390 | estimate | 21.65 packs × $6.50 × 27.7% × 10 months |
| LTV : CAC | 1.95 | estimate | 390 / 200, before any press subsidy |
| Payback (months) | 5.1 | estimate | 200 / 39 |
| Fixed costs / month | $1,000,000 | estimate | ~50 staff × $15k + facility |
| Break-even | 25,641 subscribers | estimate | 1,000,000 / 39 |
| Time to first revenue | 12 weeks | estimate | not on sale as of 2016-03-01 |

| Scenario | Subscribers | Revenue / month | Costs / month | Margin | Note |
|----------|-------------|-----------------|---------------|--------|------|
| Pessimistic | 2,000 | $281,400 | $1,203,500 | −$922,100 | $101.8 variable each + $1M fixed |
| Base | 10,000 | $1,407,000 | $2,018,000 | −$611,000 | below 25,641 break-even |
| Optimistic | 30,000 | $4,221,000 | $4,054,000 | +$167,000 | ignores CAC and press subsidy |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Custom high-force press plus a produce-pack plant; over 2 years since seed with no product on sale |
| Skills missing | Food safety, fresh-produce sourcing, cold chain |
| Key dependencies | Cold-chain couriers, organic produce supply, servers for pack checks |
| Legal / compliance | FSMA preventive controls (compliance from 2016-09); antitrust exposure of a pack lock |

| # | Risk | L | I | Mitigation | Source |
|---|------|---|---|------------|--------|
| 1 | Cold chain erases pack margin | H | H | Measure box cost in a one-metro pilot | [Fortune](https://fortune.com/2015/08/03/freshrealm-cold-delivery/) |
| 2 | Pathogens in raw cut-produce packs | M | H | FSMA controls and lot testing | [Federal Register](https://www.govinfo.gov/content/pkg/FR-2015-09-17/html/2015-21920.htm) |
| 3 | Backlash against locked packs | M | H | Freshness check only, allow offline pressing | [TechCrunch](https://techcrunch.com/2015/05/08/keurig-ceo-blames-coffee-pod-drm-for-falling-sales/amp/) |
| 4 | Server outage bricks presses | M | M | Offline fallback | [Engadget](https://www.engadget.com/2015/04/19/wink-hub-bricked-dns-fix/) |
| 5 | Cold-pressed fad fades | M | H | Position on produce intake, not cleanses | [Yahoo/Eater](https://www.yahoo.com/lifestyle/organic-avenue-to-close-all-locations-183331812.html) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 1.5 | Est. 28% per pack after cold chain (R5: costs_eat_margin) |
| | LTV : CAC | 2 | Est. 1.95 before hardware subsidy |
| | pricing power | 1.5 | Suja at $3.99, Costco $0.17/oz |
| Feasibility (20) | build effort | 1 | Press + food plant, >6 months |
| | skills match | 3 | Hardware yes; food and cold chain new |
| | capital needed | 3 | ~$20M raised, ~$120M being raised |
| Time to revenue (15) | time to MVP | 1 | Over 2 years since seed, not on sale |
| | sales cycle | 3 | $699 considered purchase |
| | channel readiness | 2.5 | Online + press; CAC unproven |
| Demand (15) | search demand | 3.5 | $2.2B juice bar industry |
| | trend | 4.5 | Cold-pressed +130.5% YoY |
| | willingness to pay | 3 | $10 bottles, prices being cut |
| Competition (10) | free alternatives | 2.5 | $70–400 juicers, cheap bottles |
| | competitor density | 2.5 | Suja + Coca-Cola (R5: strong_competitor) |
| | differentiation | 3 | Only connected juicer found |
| Risk (10) | legal / regulatory | 2.5 | FSMA, raw-produce pathogens |
| | platform dependency | 3 | Server check per pack |
| | market risk | 2 | Organic Avenue closure: fad risk |
| Fit (5) | skills | 3.5 | Funded hardware team |
| | assets | 3.5 | Kleiner Perkins, Campbell's |
| | interest | 3 | Not documented: neutral |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 1.67 | 8.33 |
| Feasibility (20) | 2.33 | 9.33 |
| Time to revenue (15) | 2.17 | 6.50 |
| Demand (15) | 3.67 | 11.00 |
| Competition (10) | 2.67 | 5.33 |
| Risk (10) | 2.50 | 5.00 |
| Fit (5) | 3.33 | 3.33 |
| **Raw total** | | **48.8** |
| **Rules applied** | none changed a score (R5 constraints already met) | |
| **Final score** | | **49 / 100** |

## 13. Sources

42 sources: 8 primary, 31 secondary, 3 tertiary. All published on or before 2016-03-01; full list with tiers and dates in `report-data.json` and `report.html`. Excluded as hindsight: Juicero's $70M round coverage (2016-03-31) and all later reporting.
