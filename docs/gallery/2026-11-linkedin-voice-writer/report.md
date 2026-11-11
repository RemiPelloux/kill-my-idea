<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 49/100
> **AI LinkedIn post writer in your voice, $19/month**
>
> `█████░░░░░` 49 / 100 · confidence high, 37 sources
>
> - ❌ Paid ads cost ~$800 per customer worth ~$249 (LTV:CAC 0.31; US LinkedIn CPC $8–10, [WebFX](https://www.webfx.com/blog/social-media/linkedin-benchmarks/))
> - ❌ Same pitch, same price, already taken: Supergrow sells at ~$19/month with ~693 paying customers ([TinyStartups](https://www.tinystartups.com/revenue/supergrow)), plus 13 "in your voice" look-alikes
> - ✅ Cheap to build and run: ~92% gross margin, an MVP in about 2 weeks for a developer
>
> **Could be saved:** done-with-you drafting service for technical founders → 66/100 (hard)
> **Cheapest test:** 7-day fake door for a developer niche (commits → LinkedIn posts), $19 pre-sale
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 49/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2049%2F100-red)

# AI LinkedIn post writer in your voice — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 49/100 (raw 55.8) · capped at 49 by R6: loses money on paid acquisition, no cheap channel |
| **Confidence** | high: 16 sourced sub-scores of 21, 37 sources (13 primary) |
| **Countries** | US |
| **Assumptions** | Budget USD 1,000 · 10 h/week · goal side income · edge: developer. Assumed: customer = US B2B founders, consultants and job-seekers posting weekly. Paid channel = LinkedIn ads, since no audience was mentioned. Self-serve SaaS on a third-party LLM API. No questions asked ("just go"). |

## 0. Executive summary

**Answer:** **NO-GO.** You would launch the 14th "in your voice" LinkedIn writer at Supergrow's exact price, just as LinkedIn removes its own AI writer. You have no audience, so paid ads cost **~$800** per customer worth about $249.

**Key findings**
1. **No cheap way to your first customers**: US LinkedIn CPC is **$8–10**. At 1% conversion, CAC is ~$800 against an LTV of ~$249 (LTV:CAC 0.31) ([WebFX](https://www.webfx.com/blog/social-media/linkedin-benchmarks/)).
2. **LinkedIn itself is retreating from AI writing**: LinkedIn **removed its AI post writer** in August 2026, and its "Seems like AI slop" button passed 1 million uses ([IBTimes UK, 2026](https://www.ibtimes.co.uk/linkedin-removes-ai-writing-tool-ai-slop-reports-1815794)).
3. **Same pitch, same price, already taken**: Supergrow sells at **$19/month** with ~693 paying customers. I also found 13 "in your voice" look-alikes ([TinyStartups](https://www.tinystartups.com/revenue/supergrow)).

**Steelman:** Demand is real. About **41%** of long LinkedIn posts are fully AI-written (Pangram via [Fast Company, 2026](https://www.fastcompany.com/91571983/linkedin-is-the-most-ai-saturated-platform)), and Supergrow proves people pay $19. A developer can ship this in 2 weeks for under $100. The evidence supports the case on demand and cost, but not on **distribution**: nothing here gives you a cheaper channel than the incumbents already have.

**Recommendation:** **Do not build** the generic $19 tool. Run the 7-day developer-niche fake door if you want to continue; otherwise archive the idea.

**Premortem:** It is 12 months later and the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Paid ads cost ~$800 per $19/month customer and organic reach never came, so growth stalled under 20 customers | no_distribution | H | First $200 of LinkedIn ads: CPC above $6 and fewer than 2 trials |
| 2 | Prospects kept using free ChatGPT or Supergrow; "in your voice" gave them no reason to switch | free_alternative | H | Fewer than 2 of 20 trial users say it beats ChatGPT |
| 3 | LinkedIn's slop classifiers cut reach on AI-drafted posts and users churned after 1–2 months | legal_platform_risk | M | Month-1 churn above 10%, or users reporting impressions down 30% |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a done-with-you service: voice-tuned drafts plus your edit, for technical founders, at $300–500/month, sourced via 50 cold DMs | no_distribution, ltv_cac (outbound costs hours, not ads; ghostwriters charge [$500–1,500/month](https://www.sproutworth.com/linkedin-ghostwriting-for-b2b-saas-founders/)) | 66/100 (estimate) | hard | 4–6 weeks to 3 clients | ~$50/month tools | Editing and sales skills you did not mention; at 10 h/week it caps at ~4 clients |
| 2 | Niche to developers: turn commits, PRs and tech blog posts into LinkedIn posts, launched on Show HN, dev.to and GitHub | differentiation, channel_readiness (your developer edge becomes the channel) | 62/100 (estimate) | doable | 2 weeks | <$100 | Proof that developers want to post on LinkedIn at all (unverified) |

Neither path reaches GO. Both still face the wave and the platform headwind.

## 2. Next step: 7-day test

**Cheapest test:** A fake-door page for the developer niche (commits → LinkedIn posts), promoted on Show HN, dev.to and through 30 DMs, with a $19 pre-sale, run for 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Landing page: "Your commits become LinkedIn posts in your voice", with a $19 pre-sale and a waitlist | Page live with a Stripe pre-sale link |
| 2 | Write 5 sample posts from your own GitHub activity, by hand with Claude | 5 samples on the page |
| 3 | Post on Show HN, dev.to and r/SideProject | 1,000 visitors by day 5 |
| 4 | Send 30 DMs to devtool founders offering 3 free posts | 5+ replies by day 5 |
| 7 | Count pre-sales and sign-ups, then apply the kill criteria | 3+ pre-sales and 40+ sign-ups, or archive |

**Stop if:**
- fewer than 3 paid pre-sales at $19 by day 7 → archive;
- fewer than 40 waitlist sign-ups from 1,000 visitors by day 7 → archive;
- fewer than 5 replies to 30 founder DMs by day 5 → drop the service path.

## 3. Source

> An AI tool that writes LinkedIn posts in your voice, $19 a month. Launch country US, budget $1,000, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | hit | ChatGPT or Claude (free), given your past posts as examples, does the job. LinkedGrow's free plan includes voice training (3 posts/month). | [LinkedGrow](https://linkedgrow.ai/features/voice-training) |
| 2 | Strong direct competitor | hit | Taplio costs $39–199/month; with Tweet Hunter it was at ~$8M ARR when sold. Supergrow costs ~$19/month and has ~693 paying customers. | [Taplio](https://taplio.com/blog/taplio-pricing), [Yespress](https://yespress.io/tibo) |
| 3 | Graveyard | hit | LinkedIn retired its own AI post writer in August 2026, after its CEO said the feature was not popular. A proofreader replaced it. | [IBTimes](https://www.ibtimes.co.uk/linkedin-removes-ai-writing-tool-ai-slop-reports-1815794), [Entrepreneur](https://www.entrepreneur.com/business-news/linkedin-ceo-our-ai-writing-tool-isnt-very-popular/493680) |
| 4 | No distribution channel | hit | No audience. US LinkedIn CPC of $6–12 (tech $8–15) gives a CAC of ~$800, against a first-year value of ~$209. | [Stackmatix](https://www.stackmatix.com/blog/linkedin-ads-benchmarks) |
| 5 | Costs eat the margin | clear | Stripe's 2.9% + 30¢ and Haiku-class API costs leave a gross margin of ~92%. | [Stripe](https://stripe.com/pricing?Sid=1), [PricePerToken](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-5.5) |
| 6 | Weak or falling demand | clear (fragile) | ~41% of long LinkedIn posts are AI-written and paid tools have customers. Google Trends was not read. | [Fast Company](https://www.fastcompany.com/91571983/linkedin-is-the-most-ai-saturated-platform) |
| 7 | Legal / platform risk | hit | The product depends on one platform. Slop reports feed the classifiers that set reach. Browser automation breaks User Agreement §8.2; the official API is allowed. | [PCWorld](https://www.pcworld.com/article/3219069/linkedins-seems-like-ai-slop-button-has-already-been-used-1-million-times.html), [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387) |
| 8 | Saturated wave (13 look-alikes found 2026-11; launch dates partly unverified) | hit | Spark Linky, Postkid, Aaptics, VoicePost AI, Lumio, CiteVox, Postessia and others all pitch "LinkedIn posts in your voice". | [Spark Linky](https://www.producthunt.com/p/spark-linky/spark-linky), [Postkid](https://www.producthunt.com/p/postkid/postkid), [Aaptics](https://www.producthunt.com/p/self-promotion/aaptics-your-linkedin-voice-on-autopilot), [VoicePost AI](https://www.producthunt.com/products/voicepost-ai/makers), [Lumio](https://www.producthunt.com/p/lumio-6/lumio-8) |

**Primary kill shot:** no distribution. You have no audience, and paid acquisition loses ~$550 on every customer.

## 6. Market

- **Target customer** (assumed): US B2B founders, consultants and sales leads who post 2–5 times a week to generate pipeline.
- **Pain:** Posting consistently takes hours, and AI drafts sound generic. Today they use ChatGPT, Taplio, Supergrow or a ghostwriter.
- **Demand signals:** About 41% of long posts and 30% of short posts are fully AI-generated (Pangram, 1M posts, April–June 2026; [TechRadar](https://www.techradar.com/pro/ai-writing-is-now-a-problem-everywhere-on-social-media-study-finds-nearly-half-of-all-linkedin-long-posts-are-ai-generated-and-thats-only-the-start)). Supergrow reports ~$18k MRR.
- **Trend:** unknown (Google Trends not read). Qualitatively negative: LinkedIn's CEO said its AI writer was unpopular, and the feature was then retired.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $575M/year | estimate | 252M US members ([Hootsuite](https://blog.hootsuite.com/linkedin-statistics-business/)) × 1% regular posters (assumption) × $228/year |
| SAM | $57.5M/year | estimate | TAM × 10% willing to pay for a drafting tool (assumption) |
| SOM (year 1) | $57.5k/year | estimate | 0.1% of SAM ≈ 252 customers × $228/year |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| Pangram: ~41% of long LinkedIn posts are fully AI-generated | 2026-07 | [Fast Company](https://www.fastcompany.com/91571983/linkedin-is-the-most-ai-saturated-platform) |
| "Seems like AI slop" report button launched; 1M+ uses | 2026-07 | [PCWorld](https://www.pcworld.com/article/3219069/linkedins-seems-like-ai-slop-button-has-already-been-used-1-million-times.html) |
| LinkedIn retires its generative post writer in favour of a proofreader | 2026-08 | [IBTimes](https://www.ibtimes.co.uk/linkedin-removes-ai-writing-tool-ai-slop-reports-1815794) |
| Claude Haiku 5.5 at $0.10/$0.50 per 1M tokens | 2026 | [PricePerToken](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-5.5) |

Generation is now cheap for everyone, and the platform is pushing back, so the window for generic AI writers is closing.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US B2B founders, consultants and sales leads posting 2–5 times a week |
| **Where to reach them** | LinkedIn creator circles, Indie Hackers, Product Hunt, r/SideProject |
| **Pays for today** | Taplio $39/month, Supergrow ~$19/month, ChatGPT Plus $20/month, ghostwriters $500–1,500/month |
| **Budget** | $20–70/month for a tool; $500+/month for a ghostwriter |
| **Trigger** | unknown (likely a launch, a job search or a new pipeline target) |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Generic $19 self-serve voice writer | Founders, consultants | 2–3 weeks |
| 2 | Developer niche: commits and PRs turned into LinkedIn posts | Devtool founders, dev-rels | 2 weeks |
| 3 | Done-with-you drafting service | Technical founders | ~2 h per client per week |

**Best option:** #2. It is the only one where being a developer helps you reach customers. Test it before writing any code.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| [Taplio](https://taplio.com/blog/taplio-pricing) | FR | AI posts, scheduling, lead database | $39–199/month (2026-10) | 5 | Expensive; the Starter plan has no AI credits |
| [Supergrow](https://aiproductivity.ai/pricing/supergrow/) | unknown | AI LinkedIn writer with voice | ~$19–39/month (2026-11, third-party) | 4 | Same price and pitch as this idea |
| [EasyGen](https://contentin.io/alternatives/easygen/) | unknown | AI LinkedIn post generator | ~$59.99/month (2026-08, third-party) | 3 | Pricier |
| [AuthoredUp](https://authoredup.com/blog/authoredup-pricing-plans) | unknown | Formatting and analytics | $19.95/month (2026) | 4 | No AI drafting |
| [LinkedGrow](https://linkedgrow.ai/features/voice-training) | unknown | AI posts with voice training | Free plan (3 posts/month) | 2 | Free tier is capped |
| ChatGPT / Claude | US | General LLMs; custom GPT trained on your posts | $0–20/month | 5 | Needs prompting and examples |

- **Free alternatives:** ChatGPT or Claude given 10 of your past posts, and LinkedGrow's free plan ([ContentIn](https://contentin.io/blog/why-your-ai-generated-linkedin-posts-sound-like-ai-and-how-to-fix-it/)).
- **Edge:** None for the generic tool. Being a developer lowers build cost, not acquisition cost, and every competitor can build this too.
- **First 10 customers** would come from your own network and launch posts. That is unproven, because you have no audience.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $19/month | estimate | The user's price; equals Supergrow Starter |
| Variable cost per unit | $1.58/month | estimate | Stripe 0.85 + LLM ~0.23 (30 posts × 5 regenerations × ~10k tokens, Haiku 5.5) + support/hosting 0.50 |
| Gross margin % | 91.7% | estimate | (19 − 1.58) ÷ 19 |
| Churn / lifetime | 7%/month → 14.3 months | estimate | Top of the 5–7% prosumer range ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/monthly-churn-benchmarks)); low switching costs |
| Conversion rate | 1% | estimate | Cold LinkedIn ad click to paid via a 7-day trial (assumption) |
| CAC | $800 | estimate | CPC ~$8 ([WebFX](https://www.webfx.com/blog/social-media/linkedin-benchmarks/), [Stackmatix](https://www.stackmatix.com/blog/linkedin-ads-benchmarks)) ÷ 1% |
| LTV | $249 | estimate | 19 × 0.917 × 14.3 |
| LTV : CAC | 0.31 | estimate | 249 ÷ 800 |
| Payback (months) | 45.9 | estimate | 800 ÷ 17.42 |
| Fixed costs / month | $50 | estimate | Hosting ~$20 + domain/email ~$10 + tools ~$20 |
| Break-even (customers / month) | 3 | estimate | 50 ÷ 17.42 |
| Time to first revenue (weeks) | 4 | estimate | ~2 weeks of build at 10 h/week + 2 weeks of outreach |

| Cost item | Monthly | Source |
|-----------|---------|--------|
| Stripe fees | 2.9% + $0.30 per charge | [Stripe](https://stripe.com/pricing?Sid=1) |
| LLM API (Haiku 5.5) | ~$0.23 per user (estimate) | [PricePerToken](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-5.5) |
| Hosting, domain, tools | ~$50 (estimate) | — |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 5 | $95 | $58 | $37 | Organic posts only |
| Base | 30 | $570 | $97 | $473 | Launch spikes plus word of mouth; ads unprofitable |
| Optimistic | 120 | $2,280 | $240 | $2,040 | A niche channel works |

Break-even is cheap: 3 customers cover the costs. The problem is that each customer is expensive to acquire.

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | ~2 weeks; the official Posts API (`w_member_social`) allows posting ([Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)) |
| Skills missing | Copywriting, B2C marketing, an audience |
| Key dependencies | LinkedIn API and algorithm; an LLM provider |
| Legal / compliance | Use the official API only; browser automation violates the User Agreement |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Paid acquisition never pays back | H | H | Organic and niche channels only | [Stackmatix](https://www.stackmatix.com/blog/linkedin-ads-benchmarks) |
| 2 | Reach penalty on AI-drafted posts | M | H | Draft from the user's own notes; no full generation | [PCWorld](https://www.pcworld.com/article/3219069/linkedins-seems-like-ai-slop-button-has-already-been-used-1-million-times.html) |
| 3 | Account bans if automation is used | L | H | Official Posts API only | [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387) |
| 4 | Price war with free tiers | H | M | Niche to a segment free tools serve badly | [LinkedGrow](https://linkedgrow.ai/features/voice-training) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|--------------------|-----------|-------|---------------|--------|
| Profit potential (25) | gross margin | 3.5 | Real margin ~92%; lowered from 4.5 by R4 so the profit mean is 2.0 | [Stripe](https://stripe.com/pricing?Sid=1) |
| | LTV : CAC | 1 | LTV ~$249 vs paid CAC ~$800: 0.31 | [WebFX](https://www.webfx.com/blog/social-media/linkedin-benchmarks/) |
| | pricing power | 1.5 | $19 is Supergrow's Starter price; free tools anchor the price near $0 | [AI Productivity](https://aiproductivity.ai/pricing/supergrow/) |
| Feasibility (20) | build effort | 4 | 2–3 weeks at 10 h/week, official API | [Microsoft Learn](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api) |
| | skills match | 4 | Can build it; lacks copywriting and marketing | — |
| | capital needed | 4.5 | LLM cost ~$0.05–0.25 per user per month | [PricePerToken](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-5.5) |
| Time to first revenue (15) | time to MVP | 4 | ~2 weeks part-time | — |
| | sales cycle | 4.5 | Self-serve after a 7-day trial | [Taplio](https://taplio.com/blog/taplio-pricing) |
| | channel readiness | 1.5 | No audience; ads lose money (R5) | [Stackmatix](https://www.stackmatix.com/blog/linkedin-ads-benchmarks) |
| Market demand (15) | search demand | 3.5 | ~41% of long posts are AI-written | [Fast Company](https://www.fastcompany.com/91571983/linkedin-is-the-most-ai-saturated-platform) |
| | trend | 2.5 | The CEO said the AI writer was unpopular; Trends not read | [Entrepreneur](https://www.entrepreneur.com/business-news/linkedin-ceo-our-ai-writing-tool-isnt-very-popular/493680) |
| | willingness to pay | 3 | Supergrow ~693 paying customers | [TinyStartups](https://www.tinystartups.com/revenue/supergrow) |
| Competitive room (10) | free alternatives | 1.5 | ChatGPT/Claude free and LinkedGrow's free plan (R1) | [LinkedGrow](https://linkedgrow.ai/features/voice-training) |
| | competitor density | 1.5 | 20+ tools, 13 look-alikes (R3) | [Product Hunt](https://www.producthunt.com/p/spark-linky/spark-linky) |
| | differentiation | 1.5 | "In your voice" is every look-alike's headline (R3) | [Indie Hackers](https://www.indiehackers.com/post/launched-postessia-today-an-ai-tool-that-writes-linkedin-posts-in-your-actual-voice-not-generic-ai-speak-dbce81cead) |
| Risk (10, 5 = low) | legal / regulatory | 3.5 | Official API is fine; automation breaks §8.2 | [LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387) |
| | platform dependency | 2 | Single platform; slop classifiers set reach | [PCWorld](https://www.pcworld.com/article/3219069/linkedins-seems-like-ai-slop-button-has-already-been-used-1-million-times.html) |
| | market risk | 2 | LinkedIn dropped its own AI writer | [IBTimes](https://www.ibtimes.co.uk/linkedin-removes-ai-writing-tool-ai-slop-reports-1815794) |
| Founder fit (5) | skills | 3 | Can build it; no SaaS sales track record stated | — |
| | assets | 1.5 | No audience, list or following | — |
| | interest | 2 | Goal is side income only | — |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 2.0 | 10.0 |
| Feasibility (20) | 4.17 | 16.7 |
| Time to first revenue (15) | 3.33 | 10.0 |
| Market demand (15) | 3.0 | 9.0 |
| Competitive room (10) | 1.5 | 3.0 |
| Risk (10) | 2.5 | 5.0 |
| Founder fit (5) | 2.17 | 2.2 |
| **Raw total** | | **55.8** |
| **Rules applied** | R1: free_alternatives 2 → 1.5 · R3: differentiation 2 → 1.5, competition 1.5 · R4: profit 2.33 → 2.0 · R6: total 56 capped at 49 | |
| **Final score** | | **49 / 100** |

## 13. Sources

37 sources from 31 domains: 13 primary, 12 secondary, 12 tertiary. All accessed 2026-11-11.

1. [Taplio, pricing 2026](https://taplio.com/blog/taplio-pricing) — Taplio $39/$69/$199 — primary — 2026
2. [Postiv, Taplio pricing](https://postiv.ai/blog/taplio-pricing) — confirms the tiers — tertiary — 2026-10
3. [Capterra, Taplio](https://www.capterra.com/p/10015825/Taplio/) — traction — secondary — 2026
4. [AI Productivity, Supergrow pricing](https://aiproductivity.ai/pricing/supergrow/) — ~$19 Starter — tertiary — 2026
5. [TinyStartups, Supergrow revenue](https://www.tinystartups.com/revenue/supergrow) — ~$18k MRR, 693 customers — secondary — unknown
6. [AuthoredUp, pricing plans](https://authoredup.com/blog/authoredup-pricing-plans) — $19.95/month — primary — 2026
7. [ContentIn, EasyGen alternatives](https://contentin.io/alternatives/easygen/) — EasyGen ~$59.99 — tertiary — 2026
8. [LinkedGrow, voice training](https://linkedgrow.ai/features/voice-training) — free plan with voice — primary — 2026
9. [Product Hunt, Spark Linky](https://www.producthunt.com/p/spark-linky/spark-linky) — look-alike — primary
10. [Product Hunt, Postkid](https://www.producthunt.com/p/postkid/postkid) — look-alike — primary
11. [Product Hunt, Aaptics](https://www.producthunt.com/p/self-promotion/aaptics-your-linkedin-voice-on-autopilot) — look-alike — primary
12. [Product Hunt, VoicePost AI](https://www.producthunt.com/products/voicepost-ai/makers) — look-alike — primary
13. [Product Hunt, Lumio](https://www.producthunt.com/p/lumio-6/lumio-8) — look-alike — primary
14. [Product Hunt, CiteVox](https://www.producthunt.com/products/citevox) — look-alike — primary — 2026
15. [Indie Hackers, Postessia](https://www.indiehackers.com/post/launched-postessia-today-an-ai-tool-that-writes-linkedin-posts-in-your-actual-voice-not-generic-ai-speak-dbce81cead) — look-alike — tertiary
16. [IBTimes UK, LinkedIn kills its AI writer](https://www.ibtimes.co.uk/linkedin-removes-ai-writing-tool-ai-slop-reports-1815794) — retirement, August 2026 — secondary
17. [Metricool, post proofreader](https://metricool.com/linkedin-post-proofreader/) — proofreader replacement — secondary — 2026-10
18. [PCWorld, slop button 1M uses](https://www.pcworld.com/article/3219069/linkedins-seems-like-ai-slop-button-has-already-been-used-1-million-times.html) — 1M+ reports — secondary — 2026
19. [SiliconANGLE, slop crackdown](https://siliconangle.com/2026/07/31/linkedin-cracks-users-posting-ai-slop-previously-encouraging/?ref=adjacent.media) — launch 2026-07-31 — secondary
20. [Fast Company, most AI-saturated platform](https://www.fastcompany.com/91571983/linkedin-is-the-most-ai-saturated-platform) — Pangram 41% — secondary — 2026-07
21. [TechRadar, Pangram study](https://www.techradar.com/pro/ai-writing-is-now-a-problem-everywhere-on-social-media-study-finds-nearly-half-of-all-linkedin-long-posts-are-ai-generated-and-thats-only-the-start) — study scale — secondary — 2026-07
22. [Entrepreneur, CEO on the AI writer](https://www.entrepreneur.com/business-news/linkedin-ceo-our-ai-writing-tool-isnt-very-popular/493680) — low usage — secondary — 2025-06
23. [LinkedIn Help, prohibited software](https://www.linkedin.com/help/linkedin/answer/a1341387) — automation breaks §8.2 — primary
24. [Microsoft Learn, Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api) — w_member_social — primary
25. [Stackmatix, LinkedIn ads benchmarks](https://www.stackmatix.com/blog/linkedin-ads-benchmarks) — CPC $5.50–9.25 — tertiary — 2026
26. [WebFX, LinkedIn benchmarks](https://www.webfx.com/blog/social-media/linkedin-benchmarks/) — US CPC $8–10 — tertiary
27. [Stripe, pricing](https://stripe.com/pricing?Sid=1) — 2.9% + 30¢ — primary
28. [NerdWallet, Stripe fees](https://nerdwallet.com/article/small-business/stripe-fees) — confirms fees — secondary
29. [Anthropic, API pricing docs](https://docs.claude.com/en/docs/about-claude/pricing) — official pricing page — primary
30. [PricePerToken, Haiku 5.5](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-5.5) — $0.10/$0.50 per 1M tokens — tertiary
31. [Lenny's Newsletter, churn benchmarks](https://www.lennysnewsletter.com/p/monthly-churn-benchmarks) — prosumer churn — secondary
32. [NapoleonCat, US LinkedIn users](https://napoleoncat.com/stats/linkedin-users-in-united-states-of-america/) — ~287M accounts — secondary — 2026-09
33. [Hootsuite, LinkedIn statistics](https://blog.hootsuite.com/linkedin-statistics-business/) — US 256M+ — secondary
34. [Ghostwriting rates guide 2026](https://ghostwriting-blog.pages.dev/posts/linkedin-ghostwriting-rates-guide-2026.html) — $300–600 per post — tertiary
35. [Sproutworth, ghostwriting for SaaS founders](https://www.sproutworth.com/linkedin-ghostwriting-for-b2b-saas-founders/) — $500–1,500/month — tertiary
36. [Yespress, Tibo Louis-Lucas](https://yespress.io/tibo) — Taplio exit — tertiary
37. [ContentIn, why AI posts sound like AI](https://contentin.io/blog/why-your-ai-generated-linkedin-posts-sound-like-ai-and-how-to-fix-it/) — custom GPT as the free route — tertiary — 2026-01
