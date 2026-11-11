<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 46/100
> **AI LinkedIn post writer in your voice, $19/month**
>
> `█████░░░░░` 46 / 100 · confidence high, 48 sources
>
> - ❌ Every customer loses money: non-branded clicks cost $12.48, so CAC is ~$950 against an LTV of ~$223 (estimate) ([source](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010))
> - ❌ Free tools already do it: a free extension saves your writing style, with 10 free generations a day ([source](https://chromewebstore.google.com/detail/hnefnjlocpafjnaodllefndjkepldcfl))
> - ✅ Cheap to build: about 3 weeks for a developer, with a ~94% gross margin
>
> **Could be saved:** a $300/month done-for-you post service for consultants → 61/100 (hard)
> **Cheapest test:** pre-sell that service to 50 US consultants by LinkedIn DM in 7 days; 2 paid pilots or stop
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 46/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2046%2F100-red)

# AI LinkedIn post writer in your voice, $19/month — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 46/100 (raw 56.2): R7 −10 points, R6 cap at 49 |
| **Confidence** | high: 15 of 21 sub-scores sourced, 48 sources (21 primary) |
| **Countries** | US |
| **Assumptions** | $1,000 budget, 10 h/week, goal side income, edge: developer. No audience or validation stated, so both are assumed to be zero (headless run, no questions asked). Customer assumed to be US consultants and solo B2B founders. The voice is learned from posts the user pastes in, not from scraping LinkedIn. Stripe US card fee assumed at 2.9% + $0.30. |

## 0. Executive summary

**Answer:** NO-GO at 46/100. **Customer acquisition** costs about $950, while a $19 customer is worth about $223, and **free tools** already write in your voice. LinkedIn is now cutting the reach of AI posts.

**Key findings**
1. **Every customer loses money**: non-branded clicks cost **$12.48**. At 1.3% visitor-to-paid, CAC is ~$950, against an LTV of ~**$223** (estimate). ([source](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010))
2. **Free tools do the core job**: a free Chrome extension **saves your writing style** and gives 10 free posts a day. ContentIn's generator needs no login. ([source](https://chromewebstore.google.com/detail/hnefnjlocpafjnaodllefndjkepldcfl))
3. **LinkedIn is turning against AI posts**: LinkedIn gives AI slop **40% fewer views**, and its slop button got 1M+ clicks in its first 2 weeks (CNN, 2026-10). ([source](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/10/18/even-linkedin-is-getting-tired-of-your-ai-written-posts/))

**Steelman:** a developer can ship this in 3 weeks for under $100, at a **94% gross margin**, and 78% of long LinkedIn posts are already AI-assisted. The evidence agrees that demand is real. But free tools already serve that demand, and paid acquisition costs about 4× what a customer brings in.

**Recommendation:** don't build the $19 SaaS. If you want this market, spend 7 days pre-selling a $300/month done-for-you service, and build only if 2 consultants pay.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | No channel: launch posts and a $1,000 ad test bring a few trials and almost no paying users | no_distribution | H | Fewer than 3 paid users after $500 of ads (~40 clicks) |
| 2 | Trial users go back to ChatGPT with their own pasted samples | free_alternative | H | More than 15% of the first cohort cancel in month 1 |
| 3 | LinkedIn's AI-slop classifiers cut reach, so users blame the tool and leave | legal_platform_risk | M | Users report impressions down 30%+ against their own baseline |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell done-for-you, voice-matched posts to US consultants at $300/month, using the tool internally; find them with 50 LinkedIn DMs a week | ltv_cac, pricing_power: buyers already pay ghostwriters $500–$1,500/month | 61/100 (estimate) | hard | 5–8 h/week for 4 clients | under $100 | Writing and editing skill; about 4 clients is the ceiling at 10 h/week |
| 2 | Multi-client voice workspace for LinkedIn ghostwriters and small agencies, $79/month per writer | pricing_power, differentiation | 54/100 (estimate) | hard | 6–8 weeks | under $500 | Direct sales into a small niche; 20+ interviews first |
| 3 | Developer niche: turn GitHub commits, changelogs and blog posts into LinkedIn posts for dev advocates and engineering leads | differentiation, channel (Show HN, dev communities) | 50/100 (estimate) | doable | 2–3 weeks | under $100 | Proof that dev advocates will pay; at $19, LTV:CAC stays thin |

## 2. Next step: 7-day test

**Cheapest test:** pre-sell a $300/month done-for-you post package to 50 US consultants by LinkedIn DM within 7 days. 2 paid pilots, or stop.

| Day | Step | Verify |
|-----|------|--------|
| 1 | List 100 US consultants who post 1–2×/week with low engagement | 100 named profiles in a sheet |
| 2 | Write 2 sample posts in the voice of each of 10 of them (ChatGPT plus manual edits) | 20 samples done in under 5 hours |
| 3–4 | DM 50 of them: a free sample post, then an offer of 8 posts/month for $300 | 10+ replies out of 50 |
| 5–6 | Send a payment link to every positive reply | 5+ calls or positive replies |
| 7 | Count the paid pilots | 2+ paid at $300 → continue; fewer → stop |

**Stop if:**
- Fewer than 2 paid pilots from 50 DMs by day 7.
- Fewer than 10 replies by day 5.
- You build the SaaS anyway and have fewer than 5 paying users at $19 after 60 days.

## 3. Source

> An AI tool that writes LinkedIn posts in your voice, $19 a month. Launch country US, budget $1,000, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions. Use the slug linkedin-ai-writer.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | hit | The LinkedIn Copilot extension saves your style and gives 10 free generations a day. ContentIn has a free generator with no login. ChatGPT with pasted samples does the same job. | [Chrome Web Store](https://chromewebstore.google.com/detail/hnefnjlocpafjnaodllefndjkepldcfl), [ContentIn](https://contentin.io/ai-linkedin-post-generator/) |
| 2 | Strong direct competitor | hit | Taplio ($39–$199/month) claims $8M ARR together with Tweet Hunter (a tertiary founder claim; Latka estimated $420K in 2023) | [founder claim](https://appviewlite.bsky.bad-example.com/@tmaker.io), [Taplio pricing](https://taplio.com/blog/taplio-pricing) |
| 3 | Graveyard | hit | PostDew, a LinkedIn post generator, had 0 paying customers after 3 weeks (2026). After ChatGPT, Jasper cut its ARR forecast by 30%+ and laid off staff (2023). | [Indie Hackers](https://www.indiehackers.com/post/i-built-a-saas-in-10-days-3-weeks-live-0-paying-customers-heres-the-data-7cb6b6accf), [Maginative](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/) |
| 4 | No distribution channel | hit | No audience. Non-branded Google clicks cost $12.48 and LinkedIn Ads clicks $11.12, so CAC is ~$950 against ~$223 LTV (estimate) | [Search Engine Land](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010) |
| 5 | Costs eat the margin | clear | GPT-5 mini ($0.25/M input, $2/M output) costs ~$0.16 per user per month; margin ~94% | [OpenAI](https://developers.openai.com/docs/models/gpt-5-mini) |
| 6 | Weak or falling demand | clear | The share of long LinkedIn posts rated likely-AI rose from 54% (2024-10) to 78% (2026-09) | [Originality.ai](https://originality.ai/blog/social-media-tracker-september) |
| 7 | Legal / platform risk | hit | LinkedIn bans scraping and automation extensions, decides at its discretion who gets posting-API access, and gives AI-slop posts 40% fewer views | [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387), [Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access) |
| 8 | Saturated wave (5 look-alike launches, 2026-01 to 2026-07, Product Hunt) | clear, barely | [Postking](https://www.producthunt.com/products/postking/launches), [Post AI](https://www.producthunt.com/products/post-ai-2/launches), [beamio](https://www.producthunt.com/products/beamio/launches), [Sayso](https://www.producthunt.com/products/sayso/launches), [VoiceMoat](https://www.producthunt.com/products/voicemoat/launches). Below the 10-launch threshold; the full count is unknown | Product Hunt |

**Primary kill shot:** no distribution. Without an audience, no channel brings a $19 customer for less than they are worth.

## 6. Market

- **Target customer:** US consultants, solo founders and B2B sellers who post on LinkedIn weekly to win clients (assumed).
- **Pain and today's fix:** writing posts that sound like them takes hours, and generic AI output gets recognised. Today they use ChatGPT, Taplio or Supergrow, or a freelance ghostwriter at $500–$1,500/month ([Sproutworth](https://www.sproutworth.com/linkedin-ghostwriting-for-b2b-saas-founders/), tertiary).
- **Demand signals:** 78% of long LinkedIn posts rated likely AI ([Originality.ai](https://originality.ai/blog/social-media-tracker-september), 2026-10); r/linkedin has ~170k members ([GummySearch](https://gummysearch.com/r/linkedin), tertiary).
- **Trend:** usage is rising while the platform's tolerance falls. Google Trends was not checked.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $2.3B (2024), global AI writing assistants | sourced | [Global Industry Analysts](https://www.marketresearch.com/Global-Industry-Analysts-v1039/Artificial-Intelligence-Writing-Assistant-Software-40887194); 360iResearch says [$1.13B](https://www.giiresearch.com/report/ires1718126-ai-writing-assistant-software-market-by-product.html) |
| SAM | unknown | unknown | No source splits out US LinkedIn post writing |
| SOM (year 1) | $11,400/year | estimate | 50 customers × $19 × 12 |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| LinkedIn stops recommending flagged AI-slop posts outside the poster's network | 2026-05 | [Neil Patel](https://neilpatel.com/blog/linkedin-ai-slop-crackdown-content-strategy/) (tertiary) |
| LinkedIn drops its AI rewrite button and adds slop classifiers | 2026-07 | [SiliconANGLE](https://siliconangle.com/2026/07/31/linkedin-cracks-users-posting-ai-slop-previously-encouraging/) |
| 40% fewer views for AI slop; the slop button got 1M+ clicks | 2026-10 | [CNN via KEYT](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/10/18/even-linkedin-is-getting-tired-of-your-ai-written-posts/) |
| GPT-5 mini at $0.25/M input makes this kind of wrapper cheap for anyone to build | 2026-11 | [OpenAI](https://developers.openai.com/docs/models/gpt-5-mini) |
| 5+ "learns your voice" LinkedIn writers launched on Product Hunt | 2026-01 to 2026-07 | [VoiceMoat](https://www.producthunt.com/products/voicemoat/launches) |

Cheap models opened this window years ago. In 2026, the platform and a crowd of clones are closing it.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US consultants, solo founders and B2B sellers who post on LinkedIn weekly to win clients |
| **Where to reach them** | LinkedIn itself, r/linkedin (~170k members), Indie Hackers, Product Hunt |
| **Pays for today** | Freelance ghostwriters at $500–$1,500/month, Taplio AI at $69/month, or ChatGPT Plus at $20/month |
| **Budget** | Tools: $15–$99/month (competitor prices, 2026); services: $500+/month |
| **Trigger** | unknown (not sourced; likely starting a consultancy, a fundraise or a job search) |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Self-serve $19 SaaS | Consultants, job seekers | 3 weeks to build, no channel |
| 2 | **Done-for-you posts, with the tool used internally** | Consultants, founders ($300+/month) | Manual, 1–2 h per client per week |
| 3 | Multi-voice workspace for ghostwriters | Ghostwriters, small agencies | 6–8 weeks, plus sales |

**Best option:** #2. Buyers already pay humans $500+ a month, so one client is worth more than a paid CAC.

## 7. Competition

| Competitor | What they do | Price (period, date) | Traction /5 | Gap |
|------------|--------------|----------------------|-------------|-----|
| Taplio | LinkedIn AI writing, scheduling, CRM | $39–$199/month (2026) | 4 | AI only from the $69 tier |
| Supergrow | AI LinkedIn writer | $39–$199/month (2026-11); dropped its $19 tier | 2 | No free tier |
| EasyGen | AI LinkedIn writer | $49.99–$59.99/month (2026) | 2 | One high-priced plan |
| Kleo | AI LinkedIn writer | $83–$99/month (2026-08) | 2 | Expensive |
| ContentIn | AI writer with a free generator | from $15/month (2026-05) | 2 | Already below $19 |
| AuthoredUp | Formatting and analytics | $14.95–$19.95/month (2026) | 3 (~30K Chrome users) | No AI writer |
| LinkedIn Copilot (extension) | Style-saving generator | free, 10 posts/day (2026-11) | 1 | Free |

- **Free alternatives:** ChatGPT or Claude with 10 pasted posts; free extensions; ContentIn's free generator.
- **Edge:** none specific. Being a developer helps you build it, not sell it.
- **First 10 customers:** no identified source. Paid ads cost ~$950 per customer (estimate).

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $19/month | estimate | The founder's price |
| Variable cost per unit | $1.14/month | estimate | LLM $0.16 ([OpenAI](https://developers.openai.com/docs/models/gpt-5-mini)) + Stripe $0.85 + Billing $0.13 ([Stripe](https://stripe.com/pricing)) |
| Gross margin % | 94% | estimate | (19 − 1.14) / 19 |
| Churn / lifetime | 8%/month / 12.5 months | estimate | B2C SaaS at 5.8% ([Focus Digital](https://focus-digital.co/average-churn-rate-subscription-services/)) × 1.3, because AI apps churn 30% more ([RevenueCat](https://www.revenuecat.com/blog/growth/ai-app-retention-study.md)) |
| Conversion rate | 1.3% visitor → paid | estimate | 7.1% visitor-to-trial × 18.5% trial-to-paid ([Shno](https://www.shno.co/marketing-statistics/free-trial-conversion-statistics)) |
| CAC | ~$950 | estimate | $12.48 CPC / 1.3% ([SEL](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010)); range $267–$2,200 |
| LTV | ~$223 | estimate | $17.86 × 12.5 |
| LTV : CAC | 0.23 | estimate | 223 / 950 |
| Payback (months) | 53 | estimate | 950 / 17.86, longer than the 12.5-month lifetime |
| Fixed costs / month | $27 | estimate | Supabase Pro $25 ([Supabase](https://supabase.com/pricing)) + domain ~$2 |
| Break-even (customers / month) | 2 (56 for $1,000/month of side income) | estimate | 27 / 17.86 |
| Time to first revenue (weeks) | 5 | estimate | 3 weeks to build + 2 weeks to launch |

| Scenario | Customers / month | Revenue / month | Costs / month | Note |
|----------|-------------------|-----------------|---------------|------|
| Pessimistic | 3 | $57 | $110 | $1,000 of ads buys about 1 customer |
| Base | 12 | $228 | $41 | Organic launches only; 8% churn caps growth |
| Optimistic | 56 | $1,064 | $91 | Needs a viral PH or HN launch; must replace 4–5 churned users a month |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | About 3 weeks at 10 h/week (estimate) |
| Skills missing | Marketing, copywriting, distribution |
| Key dependencies | LLM API; LinkedIn posting API (gated) if auto-posting |
| Legal / compliance | Light: below CCPA thresholds; the FTC fake-review rule does not apply to ghostwriting your own posts |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | No affordable channel | H | H | Pre-sell by DM before building | [SEL](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010) |
| 2 | Churn to ChatGPT or free extensions | H | H | Multi-voice or done-for-you angle | [RevenueCat](https://www.revenuecat.com/blog/growth/ai-app-retention-study.md) |
| 3 | LinkedIn down-ranks AI-assisted posts | M | H | Position as editing that keeps your voice | [CNN via KEYT](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/10/18/even-linkedin-is-getting-tired-of-your-ai-written-posts/) |
| 4 | Scraping LinkedIn to learn voice breaks its terms | L | H | Use pasted posts or the user's own data export | [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387) |
| 5 | Posting-API access refused or capped | M | M | Copy to clipboard instead of auto-posting | [Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access) |

**Type checks (SaaS):** churn_benchmark **hit** (estimate 6–10%/month; only 6.1% of monthly AI subscriptions are still active after a year). switching_cost **hit** (a stored voice profile is the only lock-in).

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 4 | ~94% margin; lowered from 5 by the R4 cap |
| | LTV : CAC | 1 | 0.23 (estimate) |
| | pricing power | 1 | Free tools set the floor; Supergrow dropped its $19 tier |
| Feasibility (20) | build effort | 4 | 2–3 weeks at 10 h/week |
| | skills match | 4 | Developer; marketing is learnable |
| | capital needed | 4.5 | ~$27/month fixed |
| Time to first revenue (15) | time to MVP | 4 | ~3 weeks |
| | sales cycle | 4.5 | Self-serve card purchase |
| | channel readiness | 1.5 | No audience; R5 |
| Market demand (15) | search demand | 3.5 | 78% of long posts AI-assisted; r/linkedin ~170k members |
| | trend | 3 | Usage rising, but LinkedIn penalises AI slop |
| | willingness to pay | 2.5 | Paid rivals exist; free tiers abound; churn is high |
| Competitive room (10) | free alternatives | 1 | R1 |
| | competitor density | 2 | 8+ paid tools, 5+ PH launches |
| | differentiation | 1.5 | "In your voice" is every rival's pitch |
| Risk (10, 5 = low) | legal / regulatory | 4 | CCPA and FTC not triggered |
| | platform dependency | 2 | Scraping ban, gated API, AI-slop down-ranking |
| | market risk | 2.5 | AI-slop backlash |
| Founder fit (5) | skills | 3 | Builds, but no sales track record |
| | assets | 1 | No audience |
| | interest | 1.5 | Doing it for side income |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 2.0 | 10.0 |
| Feasibility (20) | 4.0 (4.17) | 16.7 |
| Time to first revenue (15) | 3.5 (3.33) | 10.0 |
| Market demand (15) | 3.0 | 9.0 |
| Competitive room (10) | 1.5 | 3.0 |
| Risk (10) | 3.0 (2.83) | 5.7 |
| Founder fit (5) | 2.0 (1.83) | 1.8 |
| **Raw total** | | **56.2** |
| **Rules applied** | R1 (competition capped at 1.5) · R4 (profit capped at 2) · R5 (coherence) · R6 (capped at 49) · R7 (56 − 10 = 46) | |
| **Final score** | | **46 / 100** |

## 13. Sources

48 sources: 21 primary, 9 secondary, 18 tertiary. The full list with tiers and dates is in `report-data.json` and `report.html`. Main ones:

1. [Search Engine Land, LinkedIn vs Google CPC](https://searchengineland.com/linkedin-ads-cpc-benchmarks-how-costs-compare-with-google-ads-481010): CPC benchmarks. Secondary, 2026.
2. [CNN via KEYT, LinkedIn tired of AI posts](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/10/18/even-linkedin-is-getting-tired-of-your-ai-written-posts/): 40% fewer views. Secondary, 2026-10-18.
3. [SiliconANGLE, LinkedIn AI-slop crackdown](https://siliconangle.com/2026/07/31/linkedin-cracks-users-posting-ai-slop-previously-encouraging/). Secondary, 2026-07-31.
4. [Originality.ai tracker](https://originality.ai/blog/social-media-tracker-september): 78% likely-AI posts. Primary, 2026-10-25.
5. [Supergrow pricing](https://supergrow.ai/pricing). Primary, 2026-11.
6. [Taplio pricing](https://taplio.com/blog/taplio-pricing). Primary, 2026.
7. [Chrome Web Store, LinkedIn Copilot](https://chromewebstore.google.com/detail/hnefnjlocpafjnaodllefndjkepldcfl). Primary, accessed 2026-11-11.
8. [LinkedIn Help, prohibited software](https://www.linkedin.com/help/linkedin/answer/a1341387). Primary.
9. [Microsoft Learn, LinkedIn API access](https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access). Primary, 2026-10-19.
10. [RevenueCat, AI app retention](https://www.revenuecat.com/blog/growth/ai-app-retention-study.md). Secondary, 2026-08-18.
11. [OpenAI, GPT-5 mini pricing](https://developers.openai.com/docs/models/gpt-5-mini). Primary, 2026-11.
12. [Indie Hackers, PostDew at 0 paying customers](https://www.indiehackers.com/post/i-built-a-saas-in-10-days-3-weeks-live-0-paying-customers-heres-the-data-7cb6b6accf). Tertiary, 2026.

No fetched page tried to give instructions.
