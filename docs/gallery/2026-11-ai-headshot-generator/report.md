<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 49/100
> **$29 AI LinkedIn headshots from 10 selfies**
>
> `█████░░░░░` 49 / 100 · confidence high, 42 sources
>
> - ❌ Each customer costs ~$286 to acquire (at a $5.71 CPC and 2% conversion) and returns $25 ([SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/))
> - ❌ HeadshotPro already sells this offer at $29 and reports $10M+ in revenue ([HeadshotPro](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing))
> - ✅ ~79% gross margin, and a developer can ship it in 1–2 weeks
>
> **Could be saved:** team headshots for real-estate brokerages, sold by outreach → 58/100 (doable)
> **Cheapest test:** email 100 US brokerages a $250 team pilot offer; stop if fewer than 5 reply by day 5
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 49/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2049%2F100-red)

# AI LinkedIn headshot generator, $29 for 40 photos — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 49/100 (raw 57.2) · capped at 49 (R6: loses money, no channel) |
| **Confidence** | high: 17 sourced sub-scores of 21, 42 sources (24 primary) |
| **Countries** | US |
| **Assumptions** | Budget USD 2,000; 10 h/week; goal side income; edge: developer. Self-serve web app with no audience; inference through a hosted API (fal.ai or similar); paid search or SEO as the main channel, since no channel was given. |

## 0. Executive summary

**Answer:** **NO-GO** at 49/100. This is a $29 clone of HeadshotPro at the same price. Free Gemini does the same job, and there is **no channel**: each paid customer costs about $286 to win and returns $25.

**Key findings**
1. **Acquisition costs 11x what a customer pays**: at a **$5.71 CPC** and 2% conversion, CAC is about $286 against a **$25 LTV** (estimate). HeadshotPro holds the SEO for this keyword, which has a keyword difficulty of 74. ([SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/))
2. **The leader sells the same offer at $29**: HeadshotPro Basic is **$29 for 30 headshots**, and the company reports **$10M+** in lifetime revenue. ([HeadshotPro pricing](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing), [About](https://www.headshotpro.com/about))
3. **Free tools do the whole job**: Gemini's **Nano Banana** and BetterPic's **free plan** produce LinkedIn headshots at $0. ([BetterPic](https://www.betterpic.io/blog/introduction-free-ai-linkedin-photo-generator), [DEV](https://dev.to/gbti-network/how-to-generate-professional-linkedin-headshots-using-nano-banana-16n4))

**Steelman:** The demand is real and large. The keyword gets 22K–35K searches a month, buyers pay $29–75, and one solo developer (Danny Postma) built HeadshotPro to $10M+. The evidence cuts the other way for a newcomer: he started in 2023 and won on early SEO. A 2026 entrant faces 31+ rivals, free Gemini and a $5.71 CPC.

**Recommendation:** Do not build the $29 consumer app. Test **team headshots for real-estate brokerages** with 100 outreach emails over 7 days.

**Premortem:** It is 12 months later and the idea failed. The most likely causes come first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Paid ads cost about $286 per customer against $23 gross profit, and SEO never ranks against HeadshotPro (KD 74). | no_distribution | H | Fewer than 3 sales from the first $300 of Google Ads |
| 2 | Buyers try free Gemini or BetterPic's free plan first and never pay $29. | free_alternative | H | The landing page converts under 1% of 500 visitors |
| 3 | An Illinois user files a BIPA claim because face data was processed without written consent. | legal_regulatory | L | No written biometric consent and deletion policy live at launch |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell branded team headshots to US real-estate brokerages (10–50 agents) by direct outreach, at $250 per 10 agents | no_distribution: a countable list of buyers to email. ltv_cac: $250 deals, with CAC paid in hours. A consistent team look is something free Gemini doesn't give. | 58/100 (estimate) | doable | 2 weeks | under $100 | Cold outreach at 10 h/week; written biometric consent from every agent |
| 2 | Sell a done-for-you headshot gig on Fiverr/Upwork, using your own pipeline plus manual retouching | no_distribution: marketplace search brings the buyers. pricing_power: human QA versus free tools. | 51/100 (estimate) | doable | 1 week | $0 + 20% marketplace fee | Marketplace reviews to rank; trades hours for money, which caps income |

Neither path reaches GO. Path 1 is the only one with B2B deal sizes.

## 2. Next step: 7-day test (rescue path 1)

**Cheapest test:** Email 100 US real-estate brokerages offering a $250 team headshot pilot. Stop if fewer than 5 reply by day 5.

| Day | Step | Verify |
|-----|------|--------|
| 1 | List 100 US real-estate brokerages with 10–50 agents, with the broker's email | 100 named contacts in a sheet |
| 2 | Generate a sample team set from 3 friends who consent; write a one-page offer with a $250 / 10 agents Stripe link | Page live with 3 before/after examples |
| 3–5 | Send 100 personal emails or LinkedIn DMs with the sample | 5+ replies (5% reply rate) |
| 6–7 | Offer a paid pilot to everyone who replies; deliver within 48 h | 2+ paid pilots ($500+) |

**Stop if:**
- fewer than 5 replies to 100 outreach emails by day 5;
- 0 paid pilots ($250+) by day 7, then archive the idea;
- for the consumer version: fewer than 3 sales from the first $300 of ads within 14 days.

## 3. Source

> An AI headshot generator: upload 10 selfies, get 40 professional LinkedIn headshots for $29. Launch country US, budget $2,000, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | hit | Gemini Nano Banana makes LinkedIn headshots for free. BetterPic's free plan gives 10 headshots at 4K, and Magic Hour needs no sign-up. | [BetterPic](https://www.betterpic.io/blog/introduction-free-ai-linkedin-photo-generator), [Magic Hour](https://magichour.ai/products/ai-headshot-generator/linkedin) |
| 2 | Strong direct competitor | hit | HeadshotPro sells 30 headshots for $29 and reports $10M+ in lifetime revenue. Aragon sells 40 for $35. 31+ generators are tracked by traffic. | [HeadshotPro](https://www.headshotpro.com/about), [OneLittleWeb](https://onelittleweb.com/digital-market-intelligence/ai-tools/headshot-generators/) |
| 3 | Graveyard | hit (stalled) | Clones are up for sale. One Acquire.com listing made $342 last month and another $1,902. A Flippa SaaS says its revenue peaked above $50K/month in 2025, and it cut its asking price 20%. | [Acquire](https://app.acquire.com/public/n2lus03i2a-ai-headshot-generator-for-professionals-to-create-studio-quality-photos-from-selfies-in-60-seconds), [Flippa](https://flippa.com/12258350-saas-ai-headshot-platform-with-287k-revenue-150k-profit-81-gross-margins-fully-automated-with-b2b-upside) |
| 4 | No distribution channel | hit | "ai headshot generator" has a $5.71 CPC and a keyword difficulty of 74. At 2% conversion, CAC is about $286 against a $25 LTV. No audience was named. | [SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/) |
| 5 | Costs eat the margin | clear | fal.ai charges $2 per LoRA training run. Adding Stripe's 2.9% + $0.30 still leaves about 79% gross margin (estimate). | [fal.ai](https://www.fal.ai/models/fal-ai/flux-lora-fast-training), [Stripe](https://stripe.com/us/pricing?locale=fr) |
| 6 | Weak or falling demand | clear | 22K–35K monthly searches, up 30% over 2 years, but down about 10% in early 2026. | [AI Journal](https://aijourn.com/are-ai-headshots-good-enough-for-linkedin/) |
| 7 | Legal / platform risk | hit | Selfies yield face geometry. BIPA allows $1,000–5,000 per violation, and Lensa and Grok have been sued under it. Texas CUBI requires notice and consent. | [PetaPixel](https://petapixel.com/2023/03/16/lawsuit-alleges-lensa-ai-app-illegally-took-users-biometric-data), [Texas AG](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/enforcing-privacy-and-data-security-laws-protect-texans/biometric-identifier-act) |
| 8 | Saturated wave (10 look-alike launches, 2025-11 to 2026-11) | hit | 8 Product Hunt launches dated in the window ([Headshotly](https://www.producthunt.com/products/headshotly-ai/launches), [Professional Headshot AI](https://www.producthunt.com/products/professional-headshot-ai-2/launches), [AI Headshot Generator](https://www.producthunt.com/products/ai-headshot-generator-7/launches), [ProHeadshot AI](https://www.producthunt.com/products/proheadshot-ai/launches), [AI Profile Photo Maker, $9.99](https://www.producthunt.com/products/ai-profile-photo-maker/launches/ai-profile-photo-maker)…) plus Portrifi and VISAGE ($9), whose launch dates aren't shown. An open-source MIT [Next.js template](https://vercel.com/templates/next.js/headshot-ai) makes a clone a weekend's work. | Product Hunt |

**Primary kill shot:** no_distribution. You enter at the leader's price with no audience, and paid acquisition loses about $260 per customer.

## 6. Market

- **Target customer:** US LinkedIn users (job seekers and professionals) without a recent studio photo.
- **Pain** and how they solve it today: a studio shoot costs $150–400, and a selfie looks unprofessional. Today they use HeadshotPro, Aragon, BetterPic or free Gemini.
- **Demand signals:** 22K–35K monthly searches ([SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/), [Semrush](https://sv.semrush.com/website/headshotpro.com/overview)). The US has 252M+ LinkedIn members ([Originality.ai](https://originality.ai/blog/linkedin-statistics)). In a Ringover study, 76.5% of recruiters preferred AI headshots when they didn't know which were AI ([Tech.co](https://tech.co/news/recruiters-prefer-ai-headshots)).
- **Trend:** searches rose 30% from Dec 2023 to Dec 2025, then fell about 10% in early 2026 ([AI Journal, 2026-04](https://aijourn.com/are-ai-headshots-good-enough-for-linkedin/)).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $420M / year (2025) | sourced (vendor data, tertiary) | [Morphed](https://morphed.app/stats/ai-headshot-statistics); BetterPic gives $350–500M ([BetterPic](https://content.betterpic.io/blog/ai-headshot-generator-market-size-research)) |
| SAM | $168M / year | estimate | TAM $420M × 40% US share |
| SOM (year 1) | $168K / year | estimate | SAM × 0.1% for a solo founder with no channel |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| Google made Nano Banana image editing free in Gemini; free use was so heavy that it was capped | 2025-11 | [Engadget](https://www.engadget.com/ai/google-limits-free-nano-banana-pro-image-generation-usage-due-to-high-demand-223442929.html?src=rss) |
| HeadshotPro cut pack sizes (Executive went from 200 to 70 photos) at the same prices | 2026 | [HeadshotPro](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing) |
| A Flippa AI headshot SaaS says its revenue peaked above $50K/month in 2025, and it cut its asking price 20% | 2026 | [Flippa](https://flippa.com/12258350-saas-ai-headshot-platform-with-287k-revenue-150k-profit-81-gross-margins-fully-automated-with-b2b-upside) |
| Search interest fell about 10% in early 2026 | 2026-04 | [AI Journal](https://aijourn.com/are-ai-headshots-good-enough-for-linkedin/) |
| Texas TRAIGA amended its biometric rules, and BIPA suits are hitting photo AI | 2025-06 | [BCLP](https://www.bclplaw.com/en-US/events-insights-news/us-biometric-laws-and-pending-legislation-tracker.html), [ID Tech](https://idtechwire.com/grok-faces-second-illinois-biometric-privacy-lawsuit-over-photo-processing/) |

The window opened in 2023. By 2026 the leader holds the SEO, free models match the quality and clones sell at $9.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US job seekers and mid-career professionals updating LinkedIn, ages 25–45, without a recent studio photo |
| **Where to reach them** | r/linkedin and r/resumes; LinkedIn itself; Google search for "ai headshot generator"; TikTok career creators; university career centers |
| **Pays for today** | HeadshotPro at $29–59 or Aragon at $35–75, one-off; a studio shoot at $150–400 |
| **Budget** | USD 0–60, one-off |
| **Trigger** | Starting a job search, a new role or a promotion announcement |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Consumer LinkedIn headshots, self-serve at $29 | Individual job seekers | 1–2 weeks |
| 2 | **Team headshots for real-estate brokerages** | Broker-owner or office manager | 2 weeks + outreach |
| 3 | Done-for-you gig on Fiverr/Upwork | Individuals and small teams | 1 week |

**Best option:** #2. It is the only one with a deal size ($250+) that pays for direct outreach. A matched team look across 10–50 people is also hard to get from free Gemini.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| HeadshotPro | US | AI headshots for individuals and teams | $29–59 one-off ([pricing](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing), 2026-11) | 5 | None at $29: the same offer |
| Aragon AI | US | AI headshots, team plans | $35–75 one-off ([Toolradar](https://toolradar.com/tools/aragon-ai/pricing), 2026-10) | 4 | Slightly above $29 |
| BetterPic | — | AI headshots, free plan | $0 / $35+ ([BetterPic](https://www.betterpic.io/blog/introduction-free-ai-linkedin-photo-generator), 2026-11) | 4 | The free queue takes 1–3 months |
| Google Gemini (Nano Banana) | US | General image editing, free | $0, 2 Pro images/day ([LDS](https://letsdatascience.com/news/google-cuts-free-nano-banana-pro-image-generation-to-two-ima-175236df), 2026-03) | 5 | Needs prompting |
| Magic Hour | US | One-photo headshot, free | $0 ([Magic Hour](https://magichour.ai/products/ai-headshot-generator/linkedin), 2026-11) | 3 | Lower likeness |
| AI Profile Photo Maker | — | AI headshots | $9.99 ([Product Hunt](https://www.producthunt.com/products/ai-profile-photo-maker/launches/ai-profile-photo-maker), 2026-02) | 2 | 66% cheaper than $29 |
| VISAGE | — | AI headshots, multilingual | $9 ([Product Hunt](https://www.producthunt.com/products/visage-2/makers), 2026-11) | 2 | Cheaper than $29 |

- **Free alternatives:** Gemini Nano Banana, BetterPic's free plan, Magic Hour.
- **Edge:** none specific. "Developer" is a build skill, and the build is the easy part: a free MIT template exists ([Vercel](https://vercel.com/templates/next.js/headshot-ai)).
- **First 10 customers would come from:** friends and LinkedIn posts. Nothing repeatable after that.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $29 one-off | estimate | User's price; the same as HeadshotPro Basic |
| Variable cost per unit | $6.00 | estimate | Training $2.00 ([fal.ai](https://www.fal.ai/models/fal-ai/flux-lora-fast-training)) + 40 images × $0.035 = $1.40 + Stripe $1.14 ([Stripe](https://stripe.com/us/pricing?locale=fr)) + 5% refund reserve $1.45 |
| Gross margin % | 79% | estimate | (29 − 6) ÷ 29; Flippa peers report 81–88% ([Flippa](https://flippa.com/13401678-profitable-ai-photo-platform-across-dating-and-professional-headshots-about-0-79m-arr-at-88-gross-margin)) |
| Churn / lifetime | 1.1 purchases | estimate | One-off; about 10% buy again or pay for a redo |
| Conversion rate | 2% | estimate | Paid-search landing page benchmark of 1–3% |
| CAC | $285.5 | estimate | CPC $5.71 ([SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/)) ÷ 2% |
| LTV | $25.2 | estimate | 29 × 0.79 × 1.1 |
| LTV : CAC | 0.09 | estimate | 25.2 ÷ 285.5 |
| Payback (months) | never | estimate | $23 one-off gross profit never repays $285.5 |
| Fixed costs / month | $45 | estimate | Hosting about $20 + database about $25 (plan prices not re-checked) |
| Break-even (customers / month) | 2 | estimate | $45 ÷ $23, before acquisition cost |
| Time to first revenue (weeks) | 3 | estimate | 2 weeks to build + 1 week of launch posts |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 3 | $87 | $363 | −$276 | $300/month in Google Ads |
| Base | 15 | $435 | $135 | $300 | Organic only, about $7.50/hour for 10 h/week |
| Optimistic | 60 | $1,740 | $405 | $1,335 | Long-tail SEO pages rank by month 9 |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 1–2 weeks with the MIT Next.js headshot template and a hosted LoRA trainer |
| Skills missing | Growth: SEO, paid ads, content, sales |
| Key dependencies | Hosted model API (fal.ai / Replicate / Astria), Stripe |
| Legal / compliance | Written consent and a retention policy for face data (BIPA in Illinois, CUBI in Texas, RCW 19.375 in Washington) |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | BIPA class action over face data from selfies | L | H | Written consent, deletion within 30 days, no reuse for training | [PetaPixel](https://petapixel.com/2023/03/16/lawsuit-alleges-lensa-ai-app-illegally-took-users-biometric-data) |
| 2 | The model API changes its price or terms | M | M | Abstract the provider; keep 2 backends | [fal.ai](https://fal.ai/models/fal-ai/flux-lora-portrait-trainer/llms.txt) |
| 3 | Free Gemini quality pulls the price to $0 | H | H | Sell B2B consistency and service, not images | [Engadget](https://www.engadget.com/ai/google-limits-free-nano-banana-pro-image-generation-usage-due-to-high-demand-223442929.html?src=rss) |
| 4 | Refunds and chargebacks over poor likeness | M | M | Free redo, an upload guide, a 5% reserve | [Stripe](https://stripe.com/us/pricing?locale=fr) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|--------------------|-----------|-------|---------------|--------|
| Profit potential (25) | gross margin | 4 | ~79% (estimate); Flippa peers report 81–88% | [Flippa](https://flippa.com/12258350-saas-ai-headshot-platform-with-287k-revenue-150k-profit-81-gross-margins-fully-automated-with-b2b-upside) |
| | LTV : CAC | 1 | $25 vs $286: 0.09 (R4) | [SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/) |
| | pricing power | 1 | Free tools and $9 clones set the floor (R4) | [BetterPic](https://www.betterpic.io/blog/introduction-free-ai-linkedin-photo-generator) |
| Feasibility (20) | build effort | 4 | MIT starter template + hosted training | [Vercel](https://vercel.com/templates/next.js/headshot-ai) |
| | skills match | 4 | Developer; growth skills missing | — |
| | capital needed | 4.5 | ~$6/order, ~$45/month fixed | [fal.ai](https://www.fal.ai/models/fal-ai/flux-lora-fast-training) |
| Time to first revenue (15) | time to MVP | 4.5 | 1–2 weeks | [Vercel](https://vercel.com/templates/next.js/headshot-ai) |
| | sales cycle | 5 | Impulse purchase | [HeadshotPro](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing) |
| | channel readiness | 1.5 | No audience; KD 74; CPC $5.71 (R5) | [SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/) |
| Market demand (15) | search demand | 4 | 22K–35K searches/month | [SEOJuice](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/) |
| | trend | 3 | +30% over 2 years, then −10% in 2026 | [AI Journal](https://aijourn.com/are-ai-headshots-good-enough-for-linkedin/) |
| | willingness to pay | 3.5 | $29–75 paid; leader at $10M+ | [HeadshotPro](https://www.headshotpro.com/about) |
| Competitive room (10) | free alternatives | 1 | Gemini, BetterPic free, Magic Hour (R1, R5) | [DEV](https://dev.to/gbti-network/how-to-generate-professional-linkedin-headshots-using-nano-banana-16n4) |
| | competitor density | 1 | 31+ tracked; 10 PH look-alikes (R3, R5) | [OneLittleWeb](https://onelittleweb.com/digital-market-intelligence/ai-tools/headshot-generators/) |
| | differentiation | 1 | Same price and offer as the leader (R3) | [HeadshotPro](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing) |
| Risk (10, 5 = low) | legal / regulatory | 2.5 | BIPA, CUBI consent (R5) | [Texas AG](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/enforcing-privacy-and-data-security-laws-protect-texans/biometric-identifier-act) |
| | platform dependency | 2.5 | Hosted model API + Stripe | [fal.ai](https://fal.ai/models/fal-ai/flux-lora-portrait-trainer/llms.txt) |
| | market risk | 2.5 | Free AI erodes paid demand | [Engadget](https://www.engadget.com/ai/google-limits-free-nano-banana-pro-image-generation-usage-due-to-high-demand-223442929.html?src=rss) |
| Founder fit (5) | skills | 3.5 | Can build; no record selling consumer software | — |
| | assets | 1 | No audience, data or network | — |
| | interest | 1.5 | Stated as side income | — |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 2.0 | 10.0 |
| Feasibility (20) | 4.17 | 16.7 |
| Time to first revenue (15) | 3.67 | 11.0 |
| Market demand (15) | 3.5 | 10.5 |
| Competitive room (10) | 1.0 | 2.0 |
| Risk (10) | 2.5 | 5.0 |
| Founder fit (5) | 2.0 | 2.0 |
| **Raw total** | | **57.2** |
| **Rules applied** | R1 and R3 (Competitive room 1.0), R4 (pricing power 1.5 → 1, Profit 2.17 → 2.0), R5 (coherence caps), R6 (57 capped at 49) | |
| **Final score** | | **49 / 100** |

## 13. Sources

42 sources from 25+ domains: 24 primary, 11 secondary, 7 tertiary. Accessed 2026-11-11. Prices and volumes were read from search results and listing pages; the pages were not opened in a browser.

1. [HeadshotPro, Credits and pricing](https://www.headshotpro.com/docs/individual/billing/credits-and-pricing) — $29/$39/$59 packs — primary
2. [HeadshotPro, About](https://www.headshotpro.com/about) — $10M+ lifetime revenue — primary
3. [Toolradar, Aragon AI pricing](https://toolradar.com/tools/aragon-ai/pricing) — $35–75 — secondary — 2026-10
4. [BetterPic, Free AI LinkedIn photo generator](https://www.betterpic.io/blog/introduction-free-ai-linkedin-photo-generator) — free plan — primary
5. [Magic Hour, LinkedIn headshot generator](https://magichour.ai/products/ai-headshot-generator/linkedin) — free tool — primary
6. [DEV, LinkedIn headshots with Nano Banana](https://dev.to/gbti-network/how-to-generate-professional-linkedin-headshots-using-nano-banana-16n4) — free workflow — tertiary
7. [TechRepublic, Gemini portrait prompts](https://www.techrepublic.com/article/news-gemini-ai-portrait-prompts/) — free alternative — secondary
8. [Engadget, Nano Banana Pro limits](https://www.engadget.com/ai/google-limits-free-nano-banana-pro-image-generation-usage-due-to-high-demand-223442929.html?src=rss) — free demand — secondary — 2025-11
9. [Let's Data Science, free Nano Banana Pro cut](https://letsdatascience.com/news/google-cuts-free-nano-banana-pro-image-generation-to-two-ima-175236df) — 2 images/day — tertiary
10. [fal.ai, Flux LoRA portrait trainer](https://fal.ai/models/fal-ai/flux-lora-portrait-trainer/llms.txt) — training cost — primary
11. [fal.ai, Flux LoRA fast training](https://www.fal.ai/models/fal-ai/flux-lora-fast-training) — $2/run — primary
12. [fal.ai, Turbo Flux trainer](https://fal.ai/models/fal-ai/turbo-flux-trainer/llms.txt) — $2.40/run — primary
13. [Stripe, US pricing](https://stripe.com/us/pricing?locale=fr) — 2.9% + 30¢ — primary
14. [SEOJuice, AI & ML keywords](https://seojuice.com/keyword-research/technology/AI-&-Machine-Learning/worldwide/) — volume, KD, CPC — tertiary
15. [Semrush, headshotpro.com overview](https://sv.semrush.com/website/headshotpro.com/overview) — volume ~33K — secondary — 2025-10
16. [AI Journal, AI headshots for LinkedIn](https://aijourn.com/are-ai-headshots-good-enough-for-linkedin/) — trend — secondary — 2026-04
17. [Flippa, $287K AI headshot SaaS](https://flippa.com/12258350-saas-ai-headshot-platform-with-287k-revenue-150k-profit-81-gross-margins-fully-automated-with-b2b-upside) — 2025 peak, 81% margin — primary
18. [Flippa, $0.79M ARR AI photo platform](https://flippa.com/13401678-profitable-ai-photo-platform-across-dating-and-professional-headshots-about-0-79m-arr-at-88-gross-margin) — 88% margin — primary
19. [Acquire.com, $17.2K TTM clone](https://app.acquire.com/startup/lmjwgd3trs-ai-headshot-generator-92-gross-margin-17-200-ttm-revenue-1-902-last-month-revenue) — graveyard — primary
20. [Acquire.com, $1.5K TTM clone](https://app.acquire.com/public/n2lus03i2a-ai-headshot-generator-for-professionals-to-create-studio-quality-photos-from-selfies-in-60-seconds) — graveyard — primary
21. [PetaPixel, Lensa BIPA suit](https://petapixel.com/2023/03/16/lawsuit-alleges-lensa-ai-app-illegally-took-users-biometric-data) — legal — secondary — 2023-03
22. [ID Tech, Grok BIPA suit](https://idtechwire.com/grok-faces-second-illinois-biometric-privacy-lawsuit-over-photo-processing/) — legal — secondary
23. [Texas AG, CUBI](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/enforcing-privacy-and-data-security-laws-protect-texans/biometric-identifier-act) — consent law — primary
24. [BCLP, US biometric laws tracker](https://www.bclplaw.com/en-US/events-insights-news/us-biometric-laws-and-pending-legislation-tracker.html) — state laws — secondary
25–34. Product Hunt launches: [AI Headshot Generator 7](https://www.producthunt.com/products/ai-headshot-generator-7/launches), [AI Headshot Generator 8](https://www.producthunt.com/products/ai-headshot-generator-8/launches), [AI Profile Photo Maker](https://www.producthunt.com/products/ai-profile-photo-maker/launches/ai-profile-photo-maker), [ProHeadshot AI](https://www.producthunt.com/products/proheadshot-ai/launches), [Professional Headshot AI](https://www.producthunt.com/products/professional-headshot-ai-2/launches), [Frameworth](https://www.producthunt.com/@frameworth), [Nothron](https://www.producthunt.com/@nothron), [Headshotly](https://www.producthunt.com/products/headshotly-ai/launches), [Portrifi](https://www.producthunt.com/posts/1048397), [VISAGE](https://www.producthunt.com/products/visage-2/makers) — saturated wave — primary
35. [OneLittleWeb, 31+ AI headshot generators](https://onelittleweb.com/digital-market-intelligence/ai-tools/headshot-generators/) — competitor count — secondary — 2026-06
36. [Vercel, Headshot AI template](https://vercel.com/templates/next.js/headshot-ai) — open-source clone kit — primary
37. [Morphed, AI headshot statistics](https://morphed.app/stats/ai-headshot-statistics) — TAM $420M — tertiary
38. [BetterPic, market size](https://content.betterpic.io/blog/ai-headshot-generator-market-size-research) — TAM $350–500M — tertiary
39. [Originality.ai, LinkedIn statistics](https://originality.ai/blog/linkedin-statistics) — 252M US members — tertiary
40. [Tech.co, recruiters prefer AI headshots](https://tech.co/news/recruiters-prefer-ai-headshots) — buyer acceptance — secondary
41. [Starter Story, HeadshotPro breakdown](https://www.starterstory.com/stories/headshotpro-breakdown) — leader history — secondary
42. [Atlas Cloud, Aragon pricing page](https://www.atlascloud.ai/blog/guides/aragon-ai-headshots) — team pricing $0.45/photo — secondary — 2026-08

Excluded: a dev.to page titled "debug-test-title" with unclear authorship. It contained no instructions, but it was not used.
