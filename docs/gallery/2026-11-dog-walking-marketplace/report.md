<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 49/100
> **Uber for dog walks, 20% cut, UK**
>
> `█████░░░░░` 49 / 100 · confidence high, 38 sources
>
> - ❌ Rover already takes only **15%** on one-off UK walks and **5%** on weekly recurring ones, so walkers would pay you more than they pay the market leader ([Rover UK Help](https://support-uk.rover.com/hc/en-gb/articles/360000909143))
> - ❌ Wag!, the company that started on-demand dog walking, **filed for Chapter 11 in 2025-07**. Its shareholders were wiped out ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/09/02/3142423/0/en/Wag-Group-Co-Successfully-Completes-Pre-Packaged-Chapter-11-Plan-of-Reorganization.html))
> - ✅ The demand is real: **11.1m UK dogs**, and owners already pay GBP 12–20 a walk ([PDSA](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits))
>
> **Could be saved:** an admin and booking tool for independent walkers → 61/100 (hard)
> **Cheapest test:** interview 15 UK independent walkers and pre-sell a GBP 12/month tool in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 49/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2049%2F100-red)

# Uber-style on-demand dog walking app, 20% commission — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 49/100 (raw 48.7) |
| **Confidence** | high: 15 sourced sub-scores of 21, 38 sources (20 primary) |
| **Countries** | GB |
| **Assumptions** | Budget GBP 5,000, 15 h/week, goal: startup, edge: developer (all stated). Assumed: an average walk of GBP 14, a launch in one city first, no co-founder, no audience. |

## 0. Executive summary

**Answer:** **NO-GO** at 49/100. A 20% fee is higher than Rover's 15% (5% on recurring walks). Each owner costs about GBP 83 to acquire and brings in about **GBP 14** before the walker takes them off the app. Wag!, the US original, went bankrupt in 2025.

**Key findings**
1. **You would be the most expensive platform**: Rover charges UK walkers **15%** on one-off bookings and **5%** on weekly recurring care ([Rover UK Help](https://support-uk.rover.com/hc/en-gb/articles/360000909143))
2. **The US original went bankrupt**: Wag! filed for **Chapter 11** in 2025-07. Its equity was cancelled and its lender took control ([GlobeNewswire, 2025-09](https://www.globenewswire.com/news-release/2025/09/02/3142423/0/en/Wag-Group-Co-Successfully-Completes-Pre-Packaged-Chapter-11-Plan-of-Reorganization.html))
3. **Each owner costs more than they earn you**: about GBP 2.50 per click at a 3% conversion rate gives a **GBP 83** CAC, against about GBP 14 of lifetime contribution (estimate) ([Wired Media](https://www.wiredmedia.co.uk/?p=65617))

**Steelman:** The demand is real: there are **11.1m dogs** in the UK, and owners pay GBP 12–20 a walk. But Rover already serves that demand at a lower fee. The strongest case therefore points to serving walkers, not to competing for owners.

**Recommendation:** Do not build the marketplace. Spend 7 days interviewing 15 independent UK dog walkers and pre-selling a **GBP 12/month** admin tool.

**Premortem:** 12 months later, the idea has failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Owners booked one walk, then booked the same walker directly by phone. You paid GBP 83 per owner and earned about GBP 14 | ltv_cac | H | Under 30% of owners rebook in the app within 30 days |
| 2 | There was no cheap way to reach owners: paid search against Rover spent the GBP 5,000 on about 60 owners | no_distribution | H | CAC above GBP 50 after the first GBP 500 of ads |
| 3 | Walkers stayed on Rover at 15% or 5% and refused to pay 20%, so requests went unfilled | strong_competitor | M | Fewer than 10 of 50 walkers contacted sign up within 2 weeks |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a scheduling, GPS-report and invoicing tool to independent UK walkers at GBP 12–15/month | strong_competitor, ltv_cac, differentiation: you serve the walkers who leave Rover, and your dev skill becomes the product | 61/100 (estimate) | hard | 6–10 weeks to an MVP | < GBP 500 | 15 walker interviews first. Existing walker software was **not researched** here: check it before building |
| 2 | Run a concierge recurring-walk service in one postcode: 3–5 subcontracted walkers, weekly packs, no app | no_distribution, time_to_mvp: leaflets, vets and local groups reach owners within days, and recurring packs reduce leakage | 59/100 (estimate) | doable | 1–2 weeks to the first paid walk | ~GBP 300 | Local presence, walker recruitment, contracts that hold up under worker-status rules |

## 2. Next step: 7-day test

**Cheapest test:** Interview 15 UK independent dog walkers and pre-sell a GBP 12/month admin tool from a landing page within 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | List 40 independent walkers in one city from local Facebook groups, NARPS and Google Maps | 40 names with contact details |
| 2–4 | Run 15 calls of 20 minutes on how they book, invoice and report walks | 10 of 15 rank admin in their top-3 pains |
| 5 | Put up a landing page: booking, GPS reports and invoicing for GBP 12/month | Page live and shown to the 15 walkers |
| 6–7 | Ask each walker to pre-pay month 1 through a Stripe payment link | 3 or more pre-payments |

**Stop if:** fewer than 10 of the 15 walkers name admin as a top-3 pain by day 5, or fewer than 3 pre-pay by day 7.

## 3. Source

> An Uber-style app for on-demand dog walking that takes 20% of each walk. Launch country GB, budget 5,000 GBP, 15 hours a week, goal startup, edge: I am a developer. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear | BorrowMyDoggy volunteers and family cover part of the job, but they don't give reliable on-demand walks | [BorrowMyDoggy](https://borrowmydoggy.com/dog-walking) |
| 2 | Strong direct competitor | **hit** | Rover (taken private by Blackstone for USD 2.3bn in 2024-02), Pawshake, Tailster (~30,000 UK carers) and thousands of local walkers | [Blackstone](https://www.blackstone.com/news/press/blackstone-completes-acquisition-of-rover/) |
| 3 | Graveyard | **hit** | Wag! filed for Chapter 11 in 2025-07 after its H1 2025 revenue fell 23.8%. DogBuddy, the former UK leader, was absorbed by Rover in 2018-10 | [Chapter11Cases](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership), [Tech.eu](https://tech.eu/2018/10/31/rover-dogbuddy/) |
| 4 | No distribution channel | **hit** | Paid search costs about GBP 2.50 a click against Rover's brand. The resulting CAC (~GBP 83) is higher than an owner's first-year value (~GBP 14) | [Wired Media](https://www.wiredmedia.co.uk/?p=65617) (tertiary) |
| 5 | Costs eat the margin | clear | After Stripe's 1.5% + 20p and vetting, about 64% of the GBP 2.80 commission remains | [Stripe UK](https://stripe.com/gb/pricing?locale=fr) |
| 6 | Weak or falling demand | clear | 11.1m dogs (2025). The 2026 dip is small, and the number of walking businesses grew 29% in 2023–25 | [PDSA](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits), [Protectivity](https://www.protectivity.com/?p=12657) |
| 7 | Legal / platform risk | clear | Council PSPOs cap the number of dogs per walker and require licences. Apple takes no in-app purchase cut on walks. This means compliance work, not a blocker | [Tower Hamlets](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx) |
| 8 | Saturated wave (2 look-alike launches, 2025-11 to 2026-11) | clear | Both are trackers (Walk with Coco, cre8pet). No marketplace clones found | [Product Hunt](https://www.producthunt.com/products/walk-with-coco/launches) |

**Primary kill shot:** no distribution. Every owner you acquire loses money, because Rover owns the search terms and repeat walks leave the app.

## 6. Market

- **Target customer:** working dog owners in one dense UK city who need midday walks at short notice.
- **Pain** and how they solve it today: no one is free to walk the dog midday. Today they use Rover, Pawshake, a local walker paid directly, BorrowMyDoggy volunteers or family.
- **Demand signals:** 30% of UK adults own a dog ([PDSA](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits)). "Dog walker" had 14,800 UK searches a month in 2017 (dated) ([Protectivity](https://www.protectivity.com/knowledge-centre/revealed-the-best-towns-to-become-a-dog-walker)). About 1 in 40 owners use a professional walker (tertiary) ([Dogster](https://www.dogster.com/lifestyle/dog-walking-statistics-uk)).
- **Trend:** flat. The dog population fell in 2026 after the 2025 record ([PDSA PAW 2026](https://pdsa.org.uk/pawreport)).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | GBP 81m/year commission | estimate | 11.1m dogs × 1/40 = 277k dogs × 2 walks/week × 52 × GBP 14 = GBP 403m in bookings × 20% |
| SAM | GBP 2.4m/year | estimate | One large city (Greater Manchester, ~3% of the UK) = GBP 12m in bookings × 20% |
| SOM (year 1) | GBP 12k/year | estimate | 0.5% of SAM |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| Blackstone took Rover private for about USD 2.3bn | 2024-02 | [Blackstone](https://www.blackstone.com/news/press/blackstone-completes-acquisition-of-rover/) |
| Rover cut its UK fee on weekly recurring care to 5% | 2025 | [Rover UK Help](https://support-uk.rover.com/hc/en-gb/articles/360000909143) |
| Wag! filed for Chapter 11 | 2025-07 | [Bloomberg](https://www.bloomberg.com/news/articles/2025-07-22/dog-walking-app-wag-gets-nod-to-try-for-speedy-bankruptcy-exit) |
| The UK dog population fell after the 2025 record | 2026 | [PDSA](https://pdsa.org.uk/pawreport) |

The window has closed: the market has a funded leader charging a lower fee, and the category's pioneer went bankrupt.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Working dog owners in one dense UK city who need ad-hoc midday walks |
| **Where to reach them** | Local Facebook groups and Nextdoor, vets and groomers, dog parks, Rover and Pawshake (competitors) |
| **Pays for today** | Rover or Pawshake walkers at GBP 12–20 per walk, or a local walker paid directly |
| **Budget** | About GBP 50–100 a week for daily walks (estimate: 5 × GBP 12–20) |
| **Trigger** | A return to the office, a new puppy, or the regular walker cancelling |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | On-demand walks marketplace (the idea) | Walkers, 20% of each walk | 3–4 months |
| 2 | Admin tool for independent walkers | Walkers, GBP 12–15/month | 6–10 weeks |
| 3 | Concierge recurring walks in one postcode | Owners, weekly packs | 1–2 weeks |

**Best option:** #2. It turns your developer edge into the product, and it sells to the walkers who already resent platform fees ([Trustpilot](https://uk.trustpilot.com/review/rover.com?page=2), tertiary).

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| [Rover](https://support-uk.rover.com/hc/en-gb/articles/360000909143) | GB | Pet-care marketplace | 15% one-off, 5% recurring (2026-11) | 5 | Fees on both sides; the app became clunky after the Cat in a Flat merger |
| [Pawshake](https://www.pawshake.co.uk/dog-walking) | GB | Pet-care marketplace | GBP 9–20 per walk (2026-11) | 3 | Fee not shown publicly |
| [Tailster](https://content.tailster.com/pet-businesses/dog-walkers) | GB | Carer marketplace, part-owned by Pets at Home | unknown | 3 | Low visibility since 2019 |
| [BorrowMyDoggy](https://borrowmydoggy.com/dog-walking) | GB | Volunteer matching | GBP 13–45/year | 4 | No guaranteed same-day walk |
| [Wag!](https://www.globenewswire.com/news-release/2025/09/02/3142423/0/en/Wag-Group-Co-Successfully-Completes-Pre-Packaged-Chapter-11-Plan-of-Reorganization.html) | US | On-demand walks | n/a | 3 | Not in the UK; went through Chapter 11 |
| Local independent walkers | GB | Direct service | GBP 10–25/hour ([Protectivity](https://www.protectivity.com/?p=12657)) | 4 | No booking tech; admin runs on WhatsApp |

- **Free alternatives:** BorrowMyDoggy volunteers, neighbours, family.
- **Edge:** none specific. "On-demand" is a feature Rover already has, and being a developer is not a moat against a USD 2.3bn incumbent.
- **First 10 customers** would come from local Facebook groups and leaflets. That is possible, but it doesn't scale at your CAC.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | GBP 2.80 per walk (net) | estimate | 20% × GBP 14 average walk ([Rover Manchester](https://www.rover.com/uk/blog/manchester-england-dog-walking-price/), [Reading](https://www.rover.com/uk/blog/reading-england-dog-walking-price/)) |
| Variable cost per unit | GBP 1.01 | estimate | Stripe 0.41 + vetting/support 0.30 + guarantee reserve 0.30 |
| Gross margin % | 64% | estimate | (2.80 − 1.01) ÷ 2.80 |
| Churn / lifetime | 8 walks on the app | estimate | Repeat walks leak off the app; Rover's 5% recurring fee exists to stop this |
| Conversion rate | 3% | estimate | Local-services benchmark of 2–5% |
| CAC | GBP 83 | estimate | GBP 2.50 CPC ÷ 3% |
| LTV | GBP 14.32 | estimate | 8 × GBP 1.79 |
| LTV : CAC | **0.17** | estimate | 14.32 ÷ 83 |
| Payback (months) | 23 | estimate | 83 ÷ (2 walks × 1.79), longer than the owner stays |
| Fixed costs / month | GBP 60 | estimate | Hosting/maps 25 + Apple developer fee 6.6 + insurance/tools 28 |
| Break-even (customers / month) | 17 active owners | estimate | 60 ÷ 3.58, **excluding marketing** |
| Time to first revenue (weeks) | 14 | estimate | 12 weeks to build + 2 weeks to recruit walkers |

| Scenario | Owners / month | Revenue / month | Costs / month | Margin | Note |
|----------|----------------|-----------------|---------------|--------|------|
| Pessimistic | 20 | GBP 112 | GBP 860 | −GBP 748 | GBP 800 ads |
| Base | 60 | GBP 336 | GBP 1,060 | −GBP 724 | GBP 1,000 ads; the GBP 5,000 lasts ~7 months |
| Optimistic | 200 (3 walks each) | GBP 1,680 | GBP 1,560 | +GBP 120 | Break-even only |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 3–4 months at 15 h/week (two-sided app, payments, vetting, tracking) |
| Skills missing | Supply recruitment, trust and safety, local operations |
| Key dependencies | Walker supply density in one area; Stripe Connect |
| Legal / compliance | Council PSPO caps and licences ([Richmond, GBP 141.67](https://www.richmond.gov.uk/services/parks_and_open_spaces/pspos_and_byelaws/apply_for_a_professional_dog_walking_licence)); walker insurance; worker-status reform ([Brodies](https://brodies.com/insights/employment-and-immigration/employment-status-an-update/)) |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Repeat bookings move off the app | H | H | A recurring discount, which wipes out your margin | [Rover](https://support-uk.rover.com/hc/en-gb/articles/360000909143) |
| 2 | Dog incident (loss, injury, bite) on your platform | M | H | Vetting, walker insurance (from GBP 5.41/month), a guarantee fund | [Protectivity](https://www.protectivity.com/?p=1241) |
| 3 | PSPO rules vary by borough | M | L | Cap walks at 4 dogs | [Tower Hamlets](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx) |
| 4 | Worker-status reform reclassifies platform walkers | L | M | Walkers set their own prices and can send a substitute | [Brodies](https://brodies.com/insights/employment-and-immigration/employment-status-an-update/) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 3 | 64% of net revenue after Stripe, vetting and reserve |
| | LTV : CAC | 1 | 0.17; walkers take repeat clients off the app |
| | pricing power | 1.5 | 20% is above Rover's 15% / 5% |
| Feasibility (20) | build effort | 2 | 3–4 months at 15 h/week |
| | skills match | 3 | You can build it, but marketplace operations are new to you |
| | capital needed | 2 | GBP 5,000 ≈ 60 owners at GBP 83, before any walker acquisition |
| Time to first revenue (15) | time to MVP | 2 | ~12 weeks |
| | sales cycle | 3.5 | Days, after a free meet-and-greet |
| | channel readiness | 2 | No audience; GBP 2.50 clicks against Rover (R5: no_distribution) |
| Market demand (15) | search demand | 4 | 11.1m dogs; 14,800 searches/month (2017) |
| | trend | 3 | Flat: 2026 dip after the 2025 peak |
| | willingness to pay | 3.5 | GBP 12–20 per walk already paid |
| Competitive room (10) | free alternatives | 2.5 | BorrowMyDoggy and family cover part of the job |
| | competitor density | 1.5 | Rover, Pawshake, Tailster, thousands of local walkers |
| | differentiation | 1 | "On-demand" is already in Rover's app |
| Risk (10) | legal / regulatory | 3 | PSPO licences, insurance, status reform |
| | platform dependency | 3.5 | No Apple cut on walks; leakage is the real dependency |
| | market risk | 3.5 | Durable need; on-demand demand fell with remote work |
| Founder fit (5) | skills | 3 | Covers the build only |
| | assets | 1 | No audience or network |
| | interest | 2.5 | No stated passion for the domain |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 1.83 | 9.17 |
| Feasibility (20) | 2.33 | 9.33 |
| Time to first revenue (15) | 2.50 | 7.50 |
| Market demand (15) | 3.50 | 10.50 |
| Competitive room (10) | 1.67 | 3.33 |
| Risk (10) | 3.33 | 6.67 |
| Founder fit (5) | 2.17 | 2.17 |
| **Raw total** | | **48.7** |
| **Rules applied** | none changed a score (R4's limit on Profit ≤ 2 was already met; R5 limits already met) | |
| **Final score** | | **49 / 100** |

## 13. Sources

38 sources from 30 domains: 20 primary, 11 secondary, 7 tertiary. All accessed 2026-11-11. The full list with tiers and what each source supports is in `report-data.js` and `report.html`. The main ones:

1. [Rover UK Help, sitter service fees](https://support-uk.rover.com/hc/en-gb/articles/360000909143) — 15% / 5% fees — primary
2. [GlobeNewswire, Wag! completes Chapter 11](https://www.globenewswire.com/news-release/2025/09/02/3142423/0/en/Wag-Group-Co-Successfully-Completes-Pre-Packaged-Chapter-11-Plan-of-Reorganization.html) — graveyard — primary — 2025-09
3. [SEC EDGAR, Wag! Q1 2025 earnings](https://www.sec.gov/Archives/edgar/data/1842356/000184235625000059/exhibit991q12025earningsre.htm) — Wag! services revenue — primary — 2025-05
4. [Blackstone, acquisition of Rover](https://www.blackstone.com/news/press/blackstone-completes-acquisition-of-rover/) — USD 2.3bn — primary — 2024-02
5. [PDSA, UK pet populations](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits) — 11.1m dogs — primary — 2025
6. [PDSA, PAW Report 2026](https://pdsa.org.uk/pawreport) — dog population fall — primary — 2026
7. [Stripe UK pricing](https://stripe.com/gb/pricing?locale=fr) — 1.5% + 20p — primary
8. [Rover UK, Manchester prices](https://www.rover.com/uk/blog/manchester-england-dog-walking-price/) — GBP 12 per 30 min — primary — 2025-09
9. [Tower Hamlets, dog walker licence FAQs](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx) — PSPO caps — primary
10. [Richmond Council, dog walking licence](https://www.richmond.gov.uk/services/parks_and_open_spaces/pspos_and_byelaws/apply_for_a_professional_dog_walking_licence) — GBP 141.67 — primary
11. [Wired Media, PPC for pet care](https://www.wiredmedia.co.uk/?p=65617) — GBP 2.50 CPC — tertiary
12. [Protectivity, Dog walking prices 2026](https://www.protectivity.com/?p=12657) — rates, +29% businesses — secondary — 2026
