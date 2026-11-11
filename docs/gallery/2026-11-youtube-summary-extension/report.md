<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. -->

> ## 🟡 PIVOT · 58/100
> **AI YouTube summary Chrome extension, $5/month**
>
> `██████░░░░` 58 / 100 · confidence high, 34 sources
>
> - ❌ The core job is free: Glasp's free summarizer has **2,000,000 users**, and Gemini and YouTube Ask also do it at no cost ([Chrome Web Store](https://chromewebstore.google.com/publisher/glasp-inc/u2d2334c6cd4ebdc7760dc3f149abde95))
> - ❌ Only 6.1% of AI-app monthly subscribers stay 12 months, so LTV is about $21 against about $37 CAC: LTV:CAC 0.56 ([RevenueCat](https://www.revenuecat.com/blog/growth/ai-app-retention-study))
> - ✅ Demand is real (about 49.5K searches for "youtube summarizer") and a developer can ship it in 2 weeks for under $50
>
> **Could be saved:** a $19–29/month weekly YouTube channel digest for B2B marketers → 66/100 (doable)
> **Cheapest test:** a fake-door $19/month digest page, 50 cold DMs and 2 subreddit posts, 3+ pre-orders in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 58/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2058%2F100-yellow)

# AI YouTube summary Chrome extension at $5/month: kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | PIVOT · 58/100 (raw 57.5) |
| **Confidence** | high: 16 sourced sub-scores of 21, 34 sources (16 primary) |
| **Countries** | US |
| **Assumptions** | Budget $500, 10 h/week, goal side income, edge "developer" (from the user). Assumed: customer = US students and knowledge workers; channel = Chrome Web Store plus organic posts; founder time $25/h; freemium model. |

## 0. Executive summary

**Answer:** **PIVOT**, but not as pitched. Gemini, YouTube's Ask button and Glasp already summarize videos **free**, so a $5/month clone loses money on each customer (LTV:CAC 0.56). Only a niche, higher-priced job like channel monitoring survives.

**Key findings**
1. **The core job is already free**: Gemini's free tier summarizes any YouTube link, YouTube ships an Ask button, and Glasp's free extension has **2,000,000 users** ([source](https://chromewebstore.google.com/publisher/glasp-inc/u2d2334c6cd4ebdc7760dc3f149abde95)).
2. **Each customer loses money**: only **6.1%** of AI-app monthly subscribers remain after 12 months (RevenueCat, 2026). At $5 that gives an LTV of $20.9 against a CAC of $37.5 (estimate) ([source](https://www.revenuecat.com/blog/growth/ai-app-retention-study)).
3. **Google owns the platform and the feature**: YouTube blocks most **cloud IPs** from fetching transcripts, and Google is building summaries into YouTube itself ([source](https://github.com/jdepoix/youtube-transcript-api)).

**Steelman:** Demand is real and proven: "youtube summarizer" draws about **49.5K** searches, and Eightify reportedly earns about $45K/month (Starter Story, third-party estimate). That revenue was won before Gemini and YouTube made the feature **free**, though, and the evidence does not support a new $5 entrant.

**Recommendation:** Do not build the $5 summarizer. Spend 7 days testing a **$19/month weekly channel digest** for B2B marketers, using a fake-door page and 50 cold DMs.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Users try it, then go back to the free Gemini or YouTube Ask summary | free_alternative | H | Fewer than 1 paying user per 200 installs (under 0.5%) |
| 2 | The listing is buried among 20+ look-alikes and installs never take off | channel_readiness | H | Fewer than 200 installs in 30 days after the launch posts |
| 3 | Subscribers churn after one month, so each is worth less than they cost | ltv_cac | M | Month-1 churn above 25% among the first 20 payers |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a weekly digest of chosen YouTube channels (competitors, industry) to B2B marketers and analysts at $19–29/month | free_alternative, pricing_power: Gemini summarizes one video on request. It does not monitor 20 channels and email you a digest | 66/100 (estimate) | doable | 2 weeks | under $50 | Cold outreach to 50+ marketers; transcript fetching that survives cloud IP blocks |
| 2 | Ship a bring-your-own-API-key extension for a one-time $29 instead of $5/month | ltv_cac, churn: no recurring AI cost, and it matches the lifetime deals buyers prefer. Free alternatives remain | 61/100 (estimate) | doable | 2 weeks | $5 store fee | Chrome Web Store listing work; Gumroad or Lemon Squeezy checkout |

## 2. Next step: 7-day test

**Cheapest test:** a fake-door landing page for a weekly YouTube channel digest for B2B marketers at $19/month. Send 50 cold DMs, make 2 subreddit posts, and count pre-orders after 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Pick the niche (B2B SaaS marketers tracking competitor channels). Write a landing page with a $19/month pre-order | Page live with a Stripe payment link |
| 2 | Make 3 sample digests by hand from real competitor channels, using Gemini | 3 digests ready to share |
| 3–5 | Send 50 personalized DMs on LinkedIn/X; post in 2 marketing subreddits | At least 10 replies from the 50 DMs |
| 6–7 | Count sign-ups and pre-orders; interview 3 respondents | 20+ sign-ups and 3+ paid pre-orders |

**Stop if:**
- Fewer than 3 paid pre-orders ($19) by day 7: stop the digest pivot.
- Fewer than 20 waitlist sign-ups from the 50 DMs and 2 posts by day 7: stop.
- If you build the $5 extension anyway, fewer than 10 paying users by week 8: archive it.

## 3. Source

> A Chrome extension that summarizes YouTube videos with AI, $5 a month. Launch country US, budget $500, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | Gemini's free tier, YouTube Ask, and Glasp's free extension (2,000,000 users, 4.3 stars) each do the whole job (2026-11) | [Chrome Web Store](https://chromewebstore.google.com/publisher/glasp-inc/u2d2334c6cd4ebdc7760dc3f149abde95), [Tom's Guide](https://www.tomsguide.com/how-to-use-google-gemini-to-summarize-a-youtube-video) |
| 2 | Strong direct competitor | **hit** | Eightify charges $9.99/month and reportedly earns about $45K/month (third-party estimate) | [Starter Story](https://www.starterstory.com/stories/eightify-breakdown), [Softwares.com](https://www.softwares.com/software/eightify) |
| 3 | Graveyard | clear | Searched for an Eightify shutdown or pivot (2025–2026) and for summarizer post-mortems. No named closure found | — |
| 4 | No distribution channel | clear | Chrome Web Store search and Reddit can bring the first 10 customers. Crowded, but a channel exists | [DEV](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga) |
| 5 | Costs eat the margin | clear | Gemini 2.5 Flash-Lite at $0.10/$0.40 per million tokens plus Stripe's 2.9% + 30¢ leaves about 87% gross margin (estimate) | [OpenRouter](https://openrouter.ai/google/gemini-2.5-flash-lite/pricing), [Stripe](https://stripe.com/us/pricing?locale=fr) |
| 6 | Weak or falling demand | clear | About 49.5K searches for "youtube summarizer", growing (Exploding Topics, 2024-11) | [Exploding Topics](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG) |
| 7 | Legal / platform risk | **hit** | YouTube blocks most cloud IPs from fetching transcripts. Google controls the store, the data and a free rival feature | [GitHub](https://github.com/jdepoix/youtube-transcript-api), [Chrome dev blog](https://developer.chrome.com/blog/cws-policy-updates-2026?hl=pt-br) |
| 8 | Saturated wave (12+ look-alikes on Product Hunt) | **hit** | 12+ near-identical summarizers on Product Hunt, including free BYO-key ones. Launch dates not all verified | [PH 1](https://www.producthunt.com/products/youtube-summarizer-2), [PH 2](https://www.producthunt.com/products/youtube-summarizer-with-your-own-api-key/makers), [PH 3](https://www.producthunt.com/posts/youtube-ai-summarizer), [PH 4](https://www.producthunt.com/products/ai-summary-youtube-summarizer-with-ai) |

**Primary kill shot:** free alternative.

## 6. Market

- **Target customer:** US students and knowledge workers who watch long educational or podcast videos (assumed).
- **Pain:** long videos take time. Today they use free Gemini, YouTube Ask or Glasp; some pay Eightify $9.99/month.
- **Demand signals:** about 49.5K searches ([Exploding Topics](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG)); Glasp has 2M users.
- **Trend:** rising since 2023, but Google's native features now absorb it.

| Market | Value | Basis | Formula |
|--------|-------|-------|---------|
| TAM | $6M/year | estimate | ~5M installs across top summarizer extensions × 2% paying × $60/year |
| SAM | $720K/year | estimate | Glasp 2M installs × 30% US (assumption) × 2% paying × $60 |
| SOM (year 1) | $3.6K/year | estimate | 0.5% of SAM ≈ 60 paying customers × $5 × 12 |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| Gemini's free tier summarizes YouTube links on request | 2024-05 | [Lifehacker JP](https://www.lifehacker.jp/article/2405-use-gemini-summarize-youtube-videos-free/) |
| YouTube's Ask button (with "summarize the video") reached all mobile and web users | 2025 | [BGR](https://www.bgr.com/2137910/how-use-youtube-tv-ask-button/) |
| Gemini 2.5 Flash-Lite cut summary cost to $0.10 per million input tokens | 2025-06 | [SiliconANGLE](https://siliconangle.com/?p=700895) |
| YouTube blocks most cloud-provider IPs from fetching transcripts | 2026 | [GitHub](https://github.com/jdepoix/youtube-transcript-api) |
| Chrome Web Store tightened its data-collection policy, enforced from 2026-08-01 | 2026-07 | [Chrome dev blog](https://developer.chrome.com/blog/cws-policy-updates-2026?hl=pt-br) |

The tech is cheap, but Google made the feature free and native in 2024–2025, which closed the window for a generic paid tool.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US students and knowledge workers who watch 5+ hours a week of long educational or podcast videos |
| **Where to reach them** | Chrome Web Store search, r/productivity, r/GetStudying, Product Hunt, X |
| **Pays for today** | Mostly nothing (Gemini, Glasp); a minority pays Eightify $9.99/month or a $29 lifetime deal |
| **Budget** | $0–10/month |
| **Trigger** | A 1–2 hour video they need the gist of before a meeting, class or decision |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | $5/month consumer summarizer (as pitched) | Students, knowledge workers | 2 weeks |
| 2 | **Weekly channel digest for B2B marketers** | Marketing teams, analysts | 2 weeks |
| 3 | BYO-key extension, $29 one-off | Power users | 2 weeks |

**Best option:** #2. It does a job Gemini and YouTube don't (monitoring many channels and pushing a digest), sold to buyers with a budget.

## 7. Competition

| Competitor | What they do | Price (date) | Traction /5 | Gap |
|------------|--------------|--------------|-------------|-----|
| [Google Gemini](https://www.tomsguide.com/how-to-use-google-gemini-to-summarize-a-youtube-video) | Summarizes any pasted YouTube link | Free (2026-11) | 5 | On request only |
| [YouTube Ask](https://www.neowin.net/news/youtube-premium-users-in-the-us-get-a-new-ai-feature/) | Native "summarize the video" prompt | Free (2026-11) | 5 | Works inside YouTube only |
| [Glasp](https://chromewebstore.google.com/publisher/glasp-inc/u2d2334c6cd4ebdc7760dc3f149abde95) | Free summary extension | Free, 2M users | 5 | Needs your ChatGPT/Claude account |
| [Eightify](https://www.softwares.com/software/eightify) | Summary extension | $9.99/month (2026) | 4 | 3 free videos/week |
| [NoteGPT](https://notegpt.io/ja/pricing) | Notes and summaries | $9–69/month (2026) | 4 | Generalist |
| [Recall](https://www.recall.it/youtube-video-summarizer) | Summaries plus knowledge base | Free tier plus paid (2026) | 3 | Knowledge-base angle |
| [Merlin](https://www.eesel.ai/blog/merlin-ai-pricing) | Multi-feature AI extension | about $19/month (2026) | 4 | YouTube is one feature |
| [YT Summarizer](https://ytsummarizer-blog.vercel.app/blog/best-youtube-summarizer-reddit-recommendations-2026) | Summary extension | $29 lifetime (2026) | 2 | Lifetime deal |

- **Free alternatives:** Gemini, YouTube Ask, Glasp, Recall's free tier, and BYO-key extensions on Product Hunt.
- **Edge:** "I am a developer" is not a specific edge, since every competitor's founder is one too.
- **First 10 customers:** Chrome Web Store search plus posts on Reddit and Product Hunt.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $5/month | user | Stated by the user |
| Variable cost per unit | $0.65 | estimate | Stripe 0.445 + Gemini ~0.10 (100 summaries) + support/proxy 0.10 |
| Gross margin % | 87.1% | estimate | (5 − 0.645) / 5 |
| Churn / lifetime | 20.8%/month · 4.8 months | estimate | 1 − 0.061^(1/12) ([RevenueCat](https://www.revenuecat.com/blog/growth/ai-app-retention-study)) |
| Conversion rate | 0.8% install → paid | sourced | [DEV](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga) |
| CAC | $37.5 | estimate | 1.5 h organic work per payer × $25/h |
| LTV | $20.9 | estimate | 5 × 0.871 × 4.8 |
| LTV : CAC | 0.56 | estimate | 20.9 / 37.5 |
| Payback (months) | 8.6 | estimate | 37.5 / 4.355, longer than the 4.8-month lifetime |
| Fixed costs / month | $15 | estimate | Domain, email, small backend; free tiers otherwise |
| Break-even (customers / month) | 4 | estimate | 15 / 4.355 = 3.4 |
| Time to first revenue (weeks) | 4 | estimate | 2 weeks build + 1 week review and listing + 1 week to first conversion |

| Cost item | Monthly | Source |
|-----------|---------|--------|
| Chrome Web Store developer fee | $5 one-time | [Chromium Blog](https://blog.chromium.org/2020/03/new-developer-dashboard-and.html) |
| Stripe | 2.9% + 30¢ per charge | [Stripe](https://stripe.com/us/pricing?locale=fr), [NerdWallet](https://www.nerdwallet.com/business/software/learn/stripe-fees) |
| Gemini 2.5 Flash-Lite | $0.10/$0.40 per million tokens | [OpenRouter](https://openrouter.ai/google/gemini-2.5-flash-lite/pricing) |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 10 | $50 | $21.5 | $28.5 | After 3 months |
| Base | 40 | $200 | $40.8 | $159.2 | After 6 months, 5,000 installs at 0.8% |
| Optimistic | 150 | $750 | $111.8 | $638.2 | Needs about 19K installs and a top-10 listing |

Break-even is easy, but the base case is **about $160/month**, about $4/hour on 10 h/week. For comparison, a solo AI wrapper on Indie Hackers reached $220 MRR after 8 months ([Indie Hackers](https://www.indiehackers.com/post/simple-ai-wrapper-in-auto-mode-8-months-4k-in-revenue-220-in-mrr-6d418c5a8e)).

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | About 2 weeks at 10 h/week |
| Skills missing | Distribution and marketing |
| Key dependencies | YouTube captions, the Chrome Web Store, an LLM API, Stripe |
| Legal / compliance | Chrome Web Store disclosure rules and the 2026 data policy; US auto-renewal rules |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Google extends free summaries further | H | H | Serve a job Google doesn't: multi-channel monitoring | [BGR](https://www.bgr.com/2137910/how-use-youtube-tv-ask-button/) |
| 2 | YouTube blocks transcript fetching | M | H | Fetch captions client-side, in the user's browser | [GitHub](https://github.com/jdepoix/youtube-transcript-api) |
| 3 | Chrome Web Store rejection or takedown | L | H | Disclose data use in the listing and the UI | [Chrome dev blog](https://developer.chrome.com/blog/cws-policy-updates-2026?hl=pt-br) |
| 4 | Heavy users drive AI costs up | L | M | Cap summaries per month | [OpenRouter](https://openrouter.ai/google/gemini-2.5-flash-lite/pricing) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 4 | ~87% (estimate); lowered from 4.5 by R4 |
| | LTV : CAC | 1 | 0.56 |
| | pricing power | 1 | Gemini does it free; lowered from 1.5 by R4 |
| Feasibility (20) | build effort | 4 | MVP in 1–2 weeks; transcripts must be fetched client-side |
| | skills match | 4 | Developer; payments and marketing are learnable |
| | capital needed | 4.5 | $5 store fee plus free tiers |
| Time to revenue (15) | time to MVP | 4 | About 2 weeks |
| | sales cycle | 4.5 | $5 is an impulse buy |
| | channel readiness | 2.5 | Store search exists; no audience |
| Demand (15) | search demand | 4 | About 49.5K searches |
| | trend | 3.5 | Rising, but absorbed by native features |
| | willingness to pay | 2.5 | Competitors charge, but users push for free or lifetime |
| Competition (10) | free alternatives | 1.5 | Gemini, Ask, Glasp; capped by R1 |
| | competitor density | 1.5 | 20+ products |
| | differentiation | 1.5 | "Cheaper" is not a moat; capped by R3 |
| Risk (10) | legal / regulatory | 3.5 | Store policies, auto-renewal rules |
| | platform dependency | 1.5 | YouTube, Chrome Web Store and Google |
| | market risk | 2 | Google bundling summaries into YouTube |
| Founder fit (5) | skills | 3.5 | Build yes, distribution no |
| | assets | 1.5 | No audience |
| | interest | 1.5 | Side income only |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 2.0 | 10.0 |
| Feasibility (20) | 4.17 | 16.7 |
| Time to revenue (15) | 3.67 | 11.0 |
| Demand (15) | 3.33 | 10.0 |
| Competition (10) | 1.5 | 3.0 |
| Risk (10) | 2.33 | 4.7 |
| Founder fit (5) | 2.17 | 2.2 |
| **Raw total** | | **57.5** |
| **Rules applied** | R1 (free_alternatives 2 → 1.5), R3 (differentiation 2 → 1.5), R4 (profit 2.33 → 2.0) | |
| **Final score** | | **58 / 100** |

The score lands in PIVOT mainly because the idea is **easy to build** (feasibility and time to revenue make up 27.7 points). On the market criteria it scores like a NO-GO.

## 13. Sources

34 sources from 25+ domains: 16 primary, 10 secondary, 8 tertiary. All accessed 2026-11-11.

1. [Chrome Web Store, Glasp publisher page](https://chromewebstore.google.com/publisher/glasp-inc/u2d2334c6cd4ebdc7760dc3f149abde95): 2M users. Primary.
2. [Tom's Guide, Gemini summarizes YouTube](https://www.tomsguide.com/how-to-use-google-gemini-to-summarize-a-youtube-video). Secondary.
3. [Lifehacker JP, Gemini free YouTube summaries](https://www.lifehacker.jp/article/2405-use-gemini-summarize-youtube-videos-free/), 2024-05. Secondary.
4. [Chrome Web Store, YouTube Summary with Gemini AI](https://chromewebstore.google.com/detail/dafkeibjaghajkpkdjmoniifpgmbemcg). Primary.
5. [Neowin, YouTube Ask for US Premium](https://www.neowin.net/news/youtube-premium-users-in-the-us-get-a-new-ai-feature/). Secondary.
6. [BGR, YouTube Ask on TV](https://www.bgr.com/2137910/how-use-youtube-tv-ask-button/). Secondary.
7. [TechWyse, Ask YouTube test](https://www.techwyse.com/news/platform-updates/youtube-ask-youtube-conversational-search-experiment). Secondary.
8. [Softwares.com, Eightify](https://www.softwares.com/software/eightify): $9.99/month. Tertiary.
9. [Lilys AI, LilysAI vs Eightify](https://lilys.ai/blog/en/free-youtube-summarizer-for-long-videos-2026/). Tertiary.
10. [Starter Story, Eightify breakdown](https://www.starterstory.com/stories/eightify-breakdown). Secondary.
11. [NoteGPT pricing](https://notegpt.io/ja/pricing). Primary.
12. [Recall, YouTube summarizer](https://www.recall.it/youtube-video-summarizer). Primary.
13. [eesel AI, Merlin pricing](https://www.eesel.ai/blog/merlin-ai-pricing). Tertiary.
14. [YT Summarizer blog, Reddit recommendations](https://ytsummarizer-blog.vercel.app/blog/best-youtube-summarizer-reddit-recommendations-2026). Tertiary.
15. [Product Hunt, YouTube Summarizer](https://www.producthunt.com/products/youtube-summarizer-2). Primary.
16. [Product Hunt, YouTube Summarizer with your own API key](https://www.producthunt.com/products/youtube-summarizer-with-your-own-api-key/makers). Primary.
17. [Product Hunt, YouTube AI Summarizer](https://www.producthunt.com/posts/youtube-ai-summarizer). Primary.
18. [Product Hunt, AI Summary](https://www.producthunt.com/products/ai-summary-youtube-summarizer-with-ai). Primary.
19. [OpenAI Community, Who would pay $5/month?](https://community.openai.com/t/who-would-pay-5-month-for-an-ai-tool-like-eightify-that-summarizes-youtube-videos/199286). Tertiary.
20. [Chrome Web Store Program Policies](https://developer.chrome.com/docs/webstore/program-policies). Primary.
21. [Chrome developer blog, 2026 policy updates](https://developer.chrome.com/blog/cws-policy-updates-2026?hl=pt-br). Primary.
22. [Chromium Blog, $5 developer fee](https://blog.chromium.org/2020/03/new-developer-dashboard-and.html), 2020-03. Primary.
23. [GitHub, youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api). Primary.
24. [TranscriptAPI, IP blocks](https://transcriptapi.com/blog/fix-youtube-transcript-api-errors). Tertiary.
25. [OpenRouter, Gemini 2.5 Flash-Lite pricing](https://openrouter.ai/google/gemini-2.5-flash-lite/pricing). Primary.
26. [SiliconANGLE, Flash-Lite preview](https://siliconangle.com/?p=700895), 2025-06. Secondary.
27. [Stripe US pricing](https://stripe.com/us/pricing?locale=fr). Primary.
28. [NerdWallet, Stripe fees](https://www.nerdwallet.com/business/software/learn/stripe-fees). Secondary.
29. [RevenueCat, AI app retention study](https://www.revenuecat.com/blog/growth/ai-app-retention-study), 2026-03. Primary.
30. [TechCrunch, AI apps struggle with retention](https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows), 2026-03. Secondary.
31. [DEV Community, freemium extension numbers](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga). Tertiary.
32. [Exploding Topics, youtube summarizer](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG), 2024-11. Secondary.
33. [Indie Hackers, AI wrapper $220 MRR](https://www.indiehackers.com/post/simple-ai-wrapper-in-auto-mode-8-months-4k-in-revenue-220-in-mrr-6d418c5a8e). Tertiary.
34. [Chrome Web Store, SummarizeYT reviews](https://chromewebstore.google.com/detail/dlhkccijmkgmbmiognpmoplbpldbaoej/reviews?hl=en). Primary.
