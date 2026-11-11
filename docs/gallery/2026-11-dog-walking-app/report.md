<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 41/100
> **Uber-style on-demand dog walking app, 20% cut**
>
> `████░░░░░░` 41 / 100 · confidence high, 39 sources
>
> - ❌ Rover already dominates UK walking and charges 15%, or 5% on recurring care, which is below your 20% ([Rover UK](https://support-uk.rover.com/hc/en-gb/articles/360000909143))
> - ❌ The "Uber for dog walking" raised USD 300M and still filed for Chapter 11 in July 2025 ([Chapter11Cases](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership))
> - ✅ About 77% gross margin on each walk, and no App Store fee on physical services ([Apple 3.1.3(e)](https://developer.apple.com/app-store/review/guidelines/))
>
> **Could be saved:** a GBP 19/month booking and payments tool for existing walkers → 54/100 (doable)
> **Cheapest test:** pre-sell 3 founding seats to London walkers in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 41/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2041%2F100-red)

# Uber-style on-demand dog walking app (GB): kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 41/100 (raw 50.5) · R7 unprofitable model: −10, capped at 49 |
| **Confidence** | high: 15 sourced sub-scores of 21, 39 sources (22 primary) |
| **Countries** | GB |
| **Assumptions** | Budget GBP 5,000, 15 h/week, goal startup, edge: developer. Assumed: working dog owners in inner London first; GBP 14.19 walk (Rover London average); no audience, walker network or validation; neutral domain interest. Headless run, so no questions were asked. |

## 0. Executive summary

**Answer:** **NO-GO**. Rover already owns UK dog walking at a 15% fee, 5% on recurring walks, so a 20% on-demand app is undercut on price and loses its regulars off-platform. **LTV:CAC of 0.65** means every customer costs more than they bring.

**Key findings**
1. **Rover undercuts the 20% take**: Rover UK charges **15%** on one-off bookings and **5%** on weekly recurring care, so your fee would be the highest in the market ([Rover UK Help](https://support-uk.rover.com/hc/en-gb/articles/360000909143)).
2. **On-demand dog walking already failed**: Wag, the original "Uber for dog walking", filed a prepackaged **Chapter 11** in July 2025 after losing money every year ([Chapter11Cases](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership)).
3. **Customers cost more than they earn**: a net take of GBP 2.18 per walk at 1.5 walks a month gives an LTV of about GBP 26, against a CAC of about GBP 40. That is **LTV:CAC 0.65** (estimate; fees from [Stripe Connect](https://stripe.com/gb/connect/pricing)).

**Steelman:** UK dog ownership is near a record (**15.5M dogs**, 2026), and hybrid work creates short-notice gaps that a developer could fill cheaply. The evidence cuts against it: owners want a trusted regular walker, not speed, and Rover already handles short-notice bookings.

**Recommendation:** Do not build the on-demand app. Spend 7 days pre-selling a GBP 19/month booking and payments tool to existing UK dog walkers, and build it only if 3 of them pay.

**Premortem:** 12 months later, the idea failed. The most likely causes come first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Walkers and owners met on the app, then moved regular walks to bank transfer to avoid the 20% fee | pricing_power | H | Fewer than 30% of first-time owners book a second walk in the app within 30 days |
| 2 | Too few idle walkers per district, so on-demand requests went unfilled and owners left | channel_readiness | H | Under 70% of requests filled within 60 minutes in the launch area |
| 3 | Owners already on Rover saw no reason to switch to a pricier app with fewer walkers | strong_competitor | M | Fewer than 20 owner sign-ups from 1,000 local ad clicks |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a GBP 19/month booking, payments and walk-report tool to existing UK walkers instead of running a marketplace | liquidity, disintermediation, ltv_cac, pricing_power | 54/100 (estimate) | doable | 1 week to a pre-sale page | under GBP 100 | Access to walker groups (NarpsUK Sitters Forum) |
| 2 | Run a managed walking service in one London postcode: 3–5 walkers, recurring weekly packages | channel_readiness, disintermediation (becomes a service, not a startup) | 50/100 (estimate) | doable | 2 weeks | GBP 500–1,000 | More than 15 h/week once it grows |
| 3 | Build a cover network where walkers hand off clients when sick or on holiday, for a fee per covered walk | liquidity (partly) | 46/100 (estimate) | hard | 2–3 months | GBP 1,000–2,000 | A dense walker community in one city |

## 2. Next step: 7-day test

**Cheapest test:** a landing page plus 20 DMs offering existing UK walkers a GBP 19/month booking-and-payments tool, with founding seats pre-sold within 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | One-page offer: booking, Stripe payments and GPS walk reports for walkers at GBP 19/month, with a pre-sale button | Page live with a working Stripe payment link |
| 2–3 | Post in the NarpsUK Sitters Forum and 5 local walker Facebook groups; DM 40 London walkers | At least 5 replies asking for a call |
| 4–5 | 5 calls: what they use today for bookings and payments, and what it costs | At least 3 of 5 name a paid tool or a pain they would pay to remove |
| 6–7 | Ask each interested walker to pay for a founding seat | At least 3 paid seats at GBP 19/month |

**Stop if any of these happen:**
- fewer than 5 walker calls booked from 40 messages by day 5;
- fewer than 3 paid founding seats by day 7;
- fewer than 10 waitlist sign-ups by day 7.

## 3. Source

> An Uber-style app for on-demand dog walking that takes 20% of each walk. Launch country GB, budget 5,000 GBP, 15 hours a week, goal startup, edge: I am a developer. Just go: do not ask questions. Use the slug dog-walking-app.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | hit | UK owners are told to find walkers through local Facebook groups and a free meet-and-greet. BorrowMyDoggy has free volunteer walkers and a free basic tier | [Mumsnet](https://www.mumsnet.com/talk/the_doghouse/4202132-Stuggling-to-find-dog-walker) |
| 2 | Strong direct competitor | hit | Rover UK: 4.9 from 27k ratings on the UK App Store, bought by Blackstone for about USD 2.3bn (2024). Tailster, BorrowMyDoggy and Airtasker also serve the market | [App Store](https://apps.apple.com/gb/app/id547320928) |
| 3 | Graveyard | hit | Wag filed for Chapter 11 in July 2025 after a USD 17.6M net loss in 2024. London's DogBuddy was absorbed by Rover in October 2018 | [Chapter11Cases](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership), [Tech.eu](https://tech.eu/2018/10/31/rover-dogbuddy/) |
| 4 | No distribution channel | clear | The first 10 owners can come from local Facebook groups and Nextdoor at almost no cost. Paid CAC of GBP 30–150 (CPC GBP 1.50–3) is more than an occasional user is worth | [LOCALiQ UK](https://localiq.co.uk/wp-content/uploads/2025/04/2025-UK-Paid-Advertising-Benchmark-Report.pdf) |
| 5 | Costs eat the margin | clear | Stripe UK fees (1.5% + 20p, plus Connect payouts) leave about 77% of the GBP 2.84 take | [Stripe](https://stripe.com/gb/pricing) |
| 6 | Weak or falling demand | clear (mixed) | UK Pet Food counts 15.5M dogs (2026); PDSA counts 10.2M, down from 11.1M (2026) | [PDSA](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits) |
| 7 | Legal / platform risk | clear, with friction | Borough licences cap dogs at 4–6 per walker. Uber v Aslam (2021) creates a worker-status risk for Uber-style control | [Tower Hamlets](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx) |
| 8 | Saturated wave (about 9 launches, 2025-11 to 2026-11) | clear | PetMeet and other dog apps launched, but only 2–4 are walker marketplaces | [Product Hunt](https://www.producthunt.com/products/petmeet/launches) |

**Type checks (marketplace):**
- **Liquidity: hit.** On-demand dispatch needs an idle walker within about 15 minutes in every district ([Built In](https://builtin.com/operations/gig-economy-apps-covid-wag)).
- **Disintermediation: hit.** Rover cut its fee to 5% on recurring care, and sitters take clients off-platform ([Rover Community](https://www.rover.com/community/question/33215/why-are-sitters-screwing-rover)).

**Primary kill shot:** strong_competitor. Rover sets the price below yours.

## 6. Market

- **Target customer:** working dog owners in inner London on hybrid schedules.
- **Pain** and how they solve it today: they need walks on office days or when the regular walker cancels. Today they keep a regular walker found through Facebook groups, Nextdoor or Rover, at GBP 12–15 per 30-min walk.
- **Demand signals:**
  - 41% of UK households own a dog, and 49% in London ([UK Pet Food, 2026](https://www.ukpetfood.org/resource/britain-s-dog-ownership-boom-as-15-5-million-dogs-now-live-in-uk-homes.html)).
  - IBISWorld publishes a UK dog walking report ([IBISWorld](https://www.ibisworld.com/united-kingdom/industry/dog-walking-services/5170/)), but its market size is paywalled.
- **Trend:** mixed. UK Pet Food reports a record; PDSA reports a fall from 11.1M to 10.2M dogs (2026).

| Market | Value | Basis | Formula |
|--------|-------|-------|---------|
| TAM | GBP 690M–3.6bn / year | estimate | 10.2–15.5M dogs × 5–10% walked by a paid walker × 2–3 walks/week × 52 × GBP 13–15 |
| SAM | GBP 20.7M / year | estimate | GBP 690M × 15% London share (assumed) × 20% take |
| SOM (year 1) | GBP 20.7k / year | estimate | 0.1% of SAM |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| Wag filed for Chapter 11 and was taken private by its lender | 2025-07 | [Chapter11Cases](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership) |
| Blackstone took Rover private for about USD 2.3bn | 2024-02 | [Blackstone](https://www.blackstone.com/news/press/blackstone-completes-acquisition-of-rover/) |
| Tower Hamlets introduced a GBP 240 walker licence with a 4–6 dog cap | 2026-04 | [Tower Hamlets](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx) |
| UK Pet Food reported 15.5M dogs; PDSA reported 10.2M | 2026-03 | [UK Pet Food](https://www.ukpetfood.org/resource/britain-s-dog-ownership-boom-as-15-5-million-dogs-now-live-in-uk-homes.html) |
| NarpsUK says hybrid work increases short-notice walk requests (no figures) | 2025-10 | [NarpsUK](https://www.narpsuk.co.uk/blog/back-to-office-pet-sitting-dog-walking-demand-uk) |

The on-demand wave peaked in 2015–2019. Its leader has since gone bankrupt and the category has consolidated, so the window is closed.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Working dog owners aged 25–44 in inner London on hybrid schedules, with one dog and no regular walker |
| **Where to reach them** | Local Facebook dog groups, Nextdoor, Mumsnet The Doghouse, Rover UK, park and vet noticeboards |
| **Pays for today** | GBP 12–15 per 30-min walk on Rover in London, or about GBP 450/month for 5 walks a week |
| **Budget** | GBP 50–450/month on walks |
| **Trigger** | Going back to the office on set days, or the regular walker cancels |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Last-minute walk when the regular walker cancels | Owner, per walk | High: needs dense idle supply |
| 2 | Recurring weekday walks for office days | Owner, weekly | Medium, but walkers take it off-platform |
| 3 | Booking, payments and walk reports for walkers | Walker, monthly | Low: only one side to win |

**Best option:** #3. It sells to one side, earns a subscription the walker keeps paying, and avoids the liquidity problem.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| [Rover UK](https://www.rover.com/uk/blog/london-uk-dog-walking-price/) | GB | Sitter and walker marketplace | GBP 12–22.52 per walk, London (2026-11); 15% fee, 5% on recurring | 5 | Not instant dispatch |
| [Wag!](https://www.sec.gov/Archives/edgar/data/1842356/000184235625000029/pet-20241231.htm) | US | On-demand walking app | unknown | 4 | US only; Chapter 11 in 2025 |
| [Tailster](https://uk.trustpilot.com/review/tailster.com?page=2) | GB | Pet-care marketplace | unknown | 3 | About 1,050 Trustpilot reviews at 3.5; payout complaints |
| [BorrowMyDoggy](https://support.borrowmydoggy.com/en/article/ca209c) | GB | Volunteer dog borrowing | GBP 12.99–48.99 / year (2026-11) | 3 | Volunteers, not reliable paid walks |
| [Airtasker UK](https://www.airtasker.com/uk/dog-walkers) | GB | General task marketplace | GBP 5–25 per walk (2026-11) | 3 | Not specialised |
| Local Facebook groups / Nextdoor | GB | Free word of mouth | free | 4 | No payments, vetting or tracking |

- **Free alternatives:** local Facebook groups, Nextdoor, word of mouth, and BorrowMyDoggy's free basic tier.
- **Edge:** being a developer cuts build cost but gives no moat. White-label "dog walk clone" scripts are already on sale ([Miracuves](https://miracuves.com/dog-walk-clone.md)).
- **First 10 customers would come from:** local Facebook groups and Nextdoor in one London borough.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price (platform take) | GBP 2.84 per walk | estimate | 20% × GBP 14.19 ([Rover London](https://www.rover.com/uk/blog/london-uk-dog-walking-price/)) |
| Variable cost per unit | GBP 0.66 | estimate | card fee 1.5% × 14.19 + 0.20 = 0.41; payout 0.25% × 11.35 + 0.10 = 0.13; account fee GBP 2 ÷ 20 walks = 0.10; maps 0.02 ([Stripe Connect](https://stripe.com/gb/connect/pricing)) |
| Gross margin % | 77% | estimate | (2.84 − 0.66) ÷ 2.84 |
| Churn / lifetime | 12.5% a month / 8 months | estimate | assumed: occasional users, plus regulars leaving the platform |
| Conversion rate | 2% | estimate | click → first booking, unknown brand |
| CAC | GBP 40 | estimate | Meta ~GBP 0.50/click ÷ 2% = 25, plus GBP 15 for walker acquisition ([WordStream](https://www.wordstream.com/blog/facebook-ads-benchmarks-2026)) |
| LTV | GBP 26.2 | estimate | 2.18 × 1.5 walks/month × 8 months |
| LTV : CAC | 0.65 | estimate | 26.2 ÷ 40 |
| Payback (months) | 12.2 | estimate | 40 ÷ 3.27, which is longer than the 8-month lifetime |
| Fixed costs / month | GBP 50 | estimate | Apple developer fee + hosting + tools |
| Break-even (customers / month) | 16 active owners | estimate | 50 ÷ 3.27; this ignores acquisition spend, which never pays back |
| Time to first revenue (weeks) | 12 | estimate | ~150 h build at 15 h/week + 2 weeks of walker vetting |

| Cost item | Cost | Source |
|-----------|------|--------|
| Basic DBS check per walker | GBP 20 once | [GOV.UK](https://www.gov.uk/government/news/dbs-reduces-fees-for-checks-and-update-service-from-5-october-2026) |
| Walker insurance | from GBP 5.05/month | [Simply Business](https://www.simplybusiness.co.uk/insurance/dog-walkers/) |
| Stripe Connect active account | GBP 2/month per walker | [Stripe Connect](https://stripe.com/gb/connect/pricing) |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 10 | GBP 43 | GBP 450 | −GBP 407 | Liquidity never reached |
| Base | 40 | GBP 170 | GBP 650 | −GBP 480 | Budget gone in about 10 months |
| Optimistic | 150 | GBP 639 | GBP 1,050 | −GBP 411 | Still losing money before founder time |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 2–4 months for a two-sided app with GPS, Stripe Connect and dispatch |
| Skills missing | Walker recruitment, vetting, local operations |
| Key dependencies | App Store / Play, Stripe Connect, insured and DBS-checked walkers |
| Legal / compliance | Borough licences and dog caps, worker status, GDPR for location tracking |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Recurring walks move off-platform | H | H | Charge walkers a subscription, not a per-walk cut | [Rover Community](https://www.rover.com/community/question/33215/why-are-sitters-screwing-rover) |
| 2 | Worker-status claim | M | H | Let walkers set prices and accept jobs freely | [CMS](https://cms.law/en/gbr/legal-updates/the-supreme-court-rules-that-uber-drivers-are-workers) |
| 3 | A dog is lost or injured on a walk | M | H | Require care, custody and control insurance | [Simply Business](https://www.simplybusiness.co.uk/insurance/dog-walkers/) |
| 4 | Licence rules differ by borough | H | M | Launch in one borough and check walkers' licences | [Royal Parks](https://royalparks.org.uk/commercial-licences/dog-walking-licences/professional-dog-walking-licence-tcs) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 4 | About 77% of the GBP 2.84 take after Stripe fees |
| | LTV : CAC | 1 | 0.65 (estimate); R4 applied |
| | pricing power | 1 | Rover takes 15%, or 5% on recurring care; off the app the take is zero; R4 applied |
| Feasibility (20) | build effort | 2 | 2–4 months at 15 h/week |
| | skills match | 3 | Build yes, operations no |
| | capital needed | 3 | GBP 5k covers one area, with little for ads |
| Time to first revenue (15) | time to MVP | 2 | ~12 weeks |
| | sales cycle | 4 | Owners book the same day |
| | channel readiness | 2 | No audience; liquidity type check hit |
| Market demand (15) | search demand | 3.5 | 10.2–15.5M dogs; on-demand demand unproven |
| | trend | 3 | Mixed (UK Pet Food vs PDSA) |
| | willingness to pay | 3 | GBP 12–15 per walk is paid to the walker, not for speed |
| Competitive room (10) | free alternatives | 2 | Facebook groups and Nextdoor handle matching |
| | competitor density | 2.5 | Rover dominant, plus 4 others |
| | differentiation | 1.5 | "On-demand" already failed (Wag) |
| Risk (10) | legal / regulatory | 2.5 | Borough licences, worker status |
| | platform dependency | 3.5 | App stores, but no in-app purchase fee |
| | market risk | 3.5 | Durable need, fragile format |
| Founder fit (5) | skills | 3 | Developer, no marketplace operations experience |
| | assets | 1 | No audience or network |
| | interest | 2 | Goal is a startup; no domain interest stated |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 2.00 | 10.0 |
| Feasibility (20) | 2.67 | 10.7 |
| Time to first revenue (15) | 2.67 | 8.0 |
| Market demand (15) | 3.17 | 9.5 |
| Competitive room (10) | 2.00 | 4.0 |
| Risk (10) | 3.17 | 6.3 |
| Founder fit (5) | 2.00 | 2.0 |
| **Raw total** | | **50.5** |
| **Rules applied** | R4: profit 2.5 → 2.0 (LTV:CAC 0.65, regulars leave the platform). R7: 51 − 10 = 41 | |
| **Final score** | | **41 / 100** |

## 13. Sources

39 sources from 30+ domains: 22 primary, 10 secondary, 7 tertiary. The full list with tiers and dates is in `report-data.json` and `report.html`. Key ones:

1. [Rover UK Help Centre, service fees](https://support-uk.rover.com/hc/en-gb/articles/360000909143): 15% / 5% fees. Primary; accessed 2026-11-11.
2. [Chapter11Cases, Wag prepackaged bankruptcy](https://chapter11cases.com/blogs/news/pet-services-platform-wag-files-for-prepackaged-bankruptcy-secured-lender-to-take-ownership): Chapter 11 filing. Secondary; published 2025-07.
3. [Wag! Group 10-K FY2024, SEC](https://www.sec.gov/Archives/edgar/data/1842356/000184235625000029/pet-20241231.htm): losses and going-concern warning. Primary; published 2025-03.
4. [Stripe Connect UK pricing](https://stripe.com/gb/connect/pricing): platform fees. Primary.
5. [UK Pet Food, dog ownership 2026](https://www.ukpetfood.org/resource/britain-s-dog-ownership-boom-as-15-5-million-dogs-now-live-in-uk-homes.html): 15.5M dogs. Primary; published 2026-03.
6. [PDSA PAW Report, pet populations](https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/uk-pet-populations-of-dogs-cats-and-rabbits): 10.2M dogs. Primary; published 2026.
7. [Tower Hamlets, dog walker licence FAQs](https://www.towerhamlets.gov.uk/lgnl/environment_and_waste/animal_welfare/Professional-Dog-Walkers-License-FAQs.aspx): GBP 240 licence. Primary.
8. [Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): 3.1.3(e). Primary.
9. [Rover UK, London walking prices](https://www.rover.com/uk/blog/london-uk-dog-walking-price/): GBP 14.19 average. Primary.
10. [CMS, Uber drivers are workers](https://cms.law/en/gbr/legal-updates/the-supreme-court-rules-that-uber-drivers-are-workers): worker status. Secondary; published 2021-02.

Two research fetches (the Rover UK help page and a Rover community thread) returned HTTP 403. Their figures come from search snippets.
