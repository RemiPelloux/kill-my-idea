> ## ☠️ NO-GO · 45/100
> **AI YouTube summarizer Chrome extension, $5/month**
>
> `█████░░░░░` 45 / 100 · confidence high, 46 sources
>
> - ❌ Gemini in Chrome summarizes YouTube videos **free** for all US desktop users since 2025-09 ([TechCrunch](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/))
> - ❌ LTV ~$18 at ~21%/month AI-app churn vs ~$1,250 paid CAC (estimate from [RevenueCat](https://www.revenuecat.com/blog/growth/ai-app-retention-study))
> - ✅ Cheap and fast to build: ~$0.002 of LLM cost per summary, MVP in 1-2 weeks for a developer
>
> **Could be saved:** sell a creator tool (chapters + show notes from their own videos, $15/month) → 56/100 (hard)
> **Cheapest test:** 7-day pre-order page for the creator tool + 100 DMs to small YouTubers
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 45/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2045%2F100-red)

# AI YouTube video summarizer Chrome extension — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 45/100 (raw 54.8) · R7: unprofitable model (−10, at most 49) |
| **Confidence** | high: 14 sourced sub-scores of 21, 46 sources (18 primary) |
| **Countries** | US |
| **Assumptions** | Budget $500, 10 h/week, goal side income, edge: developer, no audience. Customer segment not stated: assumed US students and knowledge workers who watch long videos. Channel not stated: assumed Chrome Web Store search plus free organic posts; no existing audience. Transcripts fetched in the user's browser or via a paid transcript API, summaries via a cheap LLM API. Headless run ('just go'): no intake or follow-up questions asked. |

## 0. Executive summary

**Answer:** **NO-GO** (45/100). Google gives this away **free**: Gemini in Chrome summarizes YouTube videos for every US desktop user, Glasp's free extension has 1M users, and at $5/month with ~21% monthly churn no paid channel pays back.

**Key findings**
1. **Google does it free**: Gemini in Chrome reached **all US desktop users** in 2025-09 and summarizes videos with timestamps, so the price anchor is **$0**. ([source](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/))
2. **Unit economics cannot pay for growth**: LTV **~$18** (21%/month AI-app churn) vs paid CAC **~$1,250** at 0.8% install-to-paid (estimate). ([source](https://www.revenuecat.com/blog/growth/ai-app-retention-study))
3. **No allowed transcript access**: captions.download needs **edit permission** on the video; Developer Policies bar scraping, and YouTube blocks cloud IPs. ([source](https://developers.google.com/youtube/v3/docs/captions/download))

**Steelman:** Search interest is **rising** (49.5K volume, +167%) and costs are tiny (~$0.002 per summary), so a developer can ship fast. True, but the same cheap tech lets **Google** ship it free inside Chrome and YouTube, which removes the reason to pay.

**Recommendation:** Do not build the $5 viewer extension. If you want to keep the skill set, test the creator-side tool (chapters + show notes from their own videos, $15/month) with a 7-day pre-order page.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|---|---|---|---|
| 1 | Users try it once, then use free Gemini in Chrome or Glasp; almost nobody upgrades to $5. | free_alternative | H | Free-to-paid below 0.5% after the first 500 installs |
| 2 | Store search buries a new listing under 1M-user incumbents; installs never reach the ~1,000 needed for 8 payers. | no_distribution | H | Under 10 installs a day by week 3 |
| 3 | YouTube blocks transcript fetching or Chrome review rejects the extension; summaries break. | legal_platform_risk | M | Over 5% of summaries fail on transcript fetch in week 1 |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|---|---|---|---|---|---|---|
| 1 | Sell to YouTubers, not viewers: auto chapters, show notes and SEO descriptions from their own videos at $15/month. | Fixes legal_platform_risk (captions API allowed on own videos), pricing_power and free_alternative; channel still unproven. | 56/100 (estimate) | hard | 2 weeks build, months of creator outreach | under $100 | Reaching small creators (r/NewTubers, X) by hand; competing with vidIQ/TubeBuddy features |
| 2 | Niche study tool: lecture videos to Anki flashcards and exam notes for med and nursing students, $8/month. | Fixes differentiation and willingness_to_pay with a job Gemini does not do; channel is student communities. | 52/100 (estimate) | hard | 2-3 weeks build, ongoing community work | under $100 | Credibility in r/medicalschool-type communities; still depends on transcripts |

No rescue path reaches PIVOT comfortably; both are hard because distribution is still unproven.

## 2. Next step: 7-day test

**Cheapest test:** Rescue path 1: a landing page for YouTubers (auto chapters + show notes, $15/month pre-order) and 100 DMs to small channels in 7 days.

| Day | Step | Verify |
|---|---|---|
| Day 1 | One-page site for the creator tool: auto chapters + show notes, $15/month pre-order via Stripe link | Page live, checkout works |
| Day 2-3 | Hand-make chapters + show notes for 10 small channels' latest videos and DM them | 10+ replies from 100 DMs |
| Day 4-5 | Post a before/after in r/NewTubers and creator Discords | 200+ visitors, 5%+ sign up |
| Day 6-7 | Ask every warm lead to pre-order | 5+ paid pre-orders at $15/month |

**Stop if:** Fewer than 5 pre-orders at $15/month by day 7 -> stop; Fewer than 10 replies to 100 creator DMs by day 5 -> stop; Landing page visitor-to-signup below 5% on 200+ visitors by day 7 -> stop.

## 3. Source

> A Chrome extension that summarizes YouTube videos with AI, $5 a month. Launch country US, budget $500, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions. Use the slug youtube-summary-extension.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|---|---|---|---|
| 1 | Free alternative | hit | Gemini in Chrome (free for US desktop users since 2025-09) summarizes videos with timestamps; Glasp, NoteGPT free tier and NotebookLM also do it. | [link](https://www.techrepublic.com/article/news-google-gemini-chrome-upgrade/) |
| 2 | Strong direct competitor | hit | Glasp's free extension shows 1,000,000 users; Eightify est. 100,000+ users and ~$45K/month (Starter Story, 2024-05, estimate). | [link](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli) |
| 3 | Graveyard | hit | summarize.tech returned 'DEPLOYMENT_PAUSED' in 2026-08; Glasp's Firefox add-on reported broken; Summarify.me stalled at ~$220 MRR after 8 months. | [link](https://scrimba.com/articles/best-ai-video-summarizers-2026/) |
| 4 | No distribution channel | hit | No audience; paid CAC ~$1,250 vs LTV ~$18 (estimate); store search ranks by installs and ratings, which favors 1M-user incumbents. | [link](https://developer.chrome.com/docs/webstore/discovery) |
| 5 | Costs eat the margin | clear | Clear: ~$1.24 variable cost per heavy paid user (LLM $0.19, transcripts $0.57, Stripe $0.445) leaves ~75% margin (estimate). | [link](https://www.developersdigest.tech/models/gemini-3-1-flash-lite) |
| 6 | Weak or falling demand | clear | Clear: 'youtube summarizer' at 49.5K search volume, +167% growth; paid standalone demand is eroding but searches rise. | [link](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG) |
| 7 | Legal / platform risk | hit | captions.download requires edit permission; Developer Policies bar scraping (III.E.6); YouTube blocks cloud-IP transcript requests (2025-2026). | [link](https://developers.google.com/youtube/terms/developer-policies) |
| 8 | Saturated wave (7 launches, 2025-11 to 2026-11) | clear | 7 dated look-alike launches found (InsightTube, YouTube Summarizer, Tube Insights, DeepTube, Transcription.video, 2 store listings); below the 10 threshold, but a lower bound. | [link](https://www.producthunt.com/products/insighttube/launches) |

**Primary kill shot:** free alternative (Gemini in Chrome and YouTube Ask).

## 6. Market

- **Target customer:** US students and knowledge workers with long video backlogs (assumed)
- **Pain** and how they solve it today: Hours of video to get a few key points; Free Gemini in Chrome, YouTube Ask, Glasp, or pasting a link into ChatGPT/Claude
- **Demand signals:** 'youtube summarizer' 49.5K search volume, +167% ([Exploding Topics](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG)); Glasp 1M users ([Chrome Web Store](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli))
- **Trend:** search rising; paid standalone demand flat to falling as Google bundles it (estimate).

| Market | Value | Basis | Source / formula |
|---|---|---|---|
| TAM | $2,160,000,000/year | estimate | Video AI content summarization market $2.16B in 2025 (TBRC via GII); single vendor report, broad scope, not triangulated. |
| SAM | $2,700,000/year | estimate | About 10 paid summarizer players x ~$0.54M/yr (Eightify estimate, Starter Story) x 50% US share. |
| SOM (year 1) | $2,700/year | estimate | 0.1% of SAM $2.7M = $2,700/yr, about 45 paying subscribers at $5/month. |

### Why now: late

| What changed | When | Source |
|---|---|---|
| YouTube tests a conversational AI with 'Summarize video' for US Premium on Android. | 2024-09 | [link](https://9to5google.com/2024/09/24/youtube-conversational-ai-premium-subscribers/) |
| Gemini in Chrome rolls out free to all US Mac and Windows desktop users. | 2025-09 | [link](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/) |
| YouTube rolls out a Gemini-powered Ask button that summarizes videos. | 2025-11 | [link](https://www.indiatvnews.com/technology/news/youtube-rolls-out-new-gemini-powered-ask-feature-how-it-works-2025-11-11-1017019) |
| Ask YouTube conversational search tested, then launched to US Premium. | 2026-04 | [link](https://www.iphoneincanada.ca/2026/04/28/google-testing-ask-youtube-ai-search/) |
| Gemini 3.1 Flash-Lite at $0.25/$1.50 per 1M tokens: summaries cost ~$0.002. | 2026-10 | [link](https://www.developersdigest.tech/models/gemini-3-1-flash-lite) |

Every dated change since 2024 moves the feature into **free Google products**; cheaper LLMs help incumbents as much as you.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US college and grad students who study from long lecture and tutorial videos |
| **Where to reach them** | r/college, r/GradSchool, r/studytips, Study TikTok, Discord study servers |
| **Pays for today** | ChatGPT Plus ($20/month) or Gemini, which already summarize a pasted link or transcript |
| **Budget** | unknown (estimate $3-10/month) |
| **Trigger** | Exam week with hours of lecture video to review |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|---|---|---|
| 1 | Viewer summaries, $5/month (the idea) | Students, knowledge workers | 1-2 weeks |
| 2 | Creator tool: chapters, show notes, SEO from own videos | Small YouTubers | 2 weeks |
| 3 | Lecture videos to flashcards for med students | Med and nursing students | 2-3 weeks |

**Best option:** the creator tool, because creators own their videos (captions API allowed) and already pay for tools like vidIQ and TubeBuddy.

## 7. Competition

| Competitor | Price (USD/month) | Traction /5 | Note | Gap |
|---|---|---|---|---|
| [Gemini in Chrome](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/) | 0–0 ([source](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/), 2025-09) | 5 | Built into Chrome for all US desktop users | None for basic summaries |
| [Glasp YouTube Summary with ChatGPT & Claude](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli) | 0–0 ([source](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli), 2026-11) | 5 | 1,000,000 users on Chrome Web Store | Needs a ChatGPT/Claude account |
| [Eightify](https://www.starterstory.com/stories/eightify-breakdown) | 4.99–9.99 ([source](https://you-tldr.com/blog/youtldr-vs-eightify-comparison), 2026-11) | 4 | 100,000+ users, ~$45K/month (Starter Story estimate, 2024-05) | Own pricing page reportedly gone |
| [NoteGPT](https://notegpt.io/pricing?type=team) | 9–69 ([source](https://notegpt.io/pricing?type=team), 2026-11) | 3 | Called most popular in comparisons; no count found | Free tier capped at 15 summaries/month |
| [Monica](https://flowith.io/blog/monica-ai-pricing-2026-free-vs-pro-vs-pro-plus) | 8.3–82.9 ([source](https://flowith.io/blog/monica-ai-pricing-2026-free-vs-pro-vs-pro-plus), 2026-03) | 3 | All-in-one AI assistant; count unknown | YouTube is one feature of many |
| [Sider](https://overchat.ai/ai-hub/best-merlin-ai-alternatives) | 4.99–10 ([source](https://overchat.ai/ai-hub/best-merlin-ai-alternatives), 2026-11) | 3 | All-in-one sidebar; count unknown | Generalist |
| [Merlin](https://overchat.ai/ai-hub/best-merlin-ai-alternatives) | 15–29 ([source](https://overchat.ai/ai-hub/best-merlin-ai-alternatives), 2026-11) | 3 | Free tier ~51-100 queries/day; count unknown | Pricier |
| [HARPA AI](https://www.softwares.com/software/harpa-ai/pricing) | 0–15 ([source](https://www.softwares.com/software/harpa-ai/pricing), 2026-11) | 2 | Count unknown | Automation focus |
| [Recall](https://chatyt.io/alternatives) | 0–7 ([source](https://chatyt.io/alternatives), 2026-11) | 2 | Count unknown | Knowledge base angle |
| [summarize.tech](https://scrimba.com/articles/best-ai-video-summarizers-2026/) | 9.99–14.99 ([source](https://chatyt.io/alternatives), 2026-11) | 1 | Deployment paused (HTTP 503) 2026-08 | Apparently dead |

- **Free alternatives:** Gemini in Chrome, YouTube Ask, Glasp, NotebookLM, NoteGPT free tier, pasting a link into ChatGPT/Claude.
- **Edge:** none specific; being a developer lowers build cost but every competitor can build this too.
- **First 10 customers** come from: unproven; Chrome Web Store search and free Reddit/TikTok posts.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|---|---|---|---|
| Price | 5 USD/month | estimate | The founder's stated price; matches Eightify's annual rate ($4.99). |
| Variable cost per unit | 1.24 USD/paid user/month | estimate | Heavy user 100 summaries: LLM 100 x $0.0019 + transcripts 100 x $0.0057 + Stripe $0.445 = $1.24. |
| Gross margin % | 75 % | estimate | (5 - 1.24) / 5 = 75%. |
| Churn (monthly) | 21 % | estimate | 1 - 0.061^(1/12) = 21%: 6.1% of AI-app monthly subs retained at 12 months (RevenueCat 2026). ([source](https://www.revenuecat.com/blog/growth/ai-app-retention-study)) |
| Lifetime | 4.8 months | estimate | 1 / 0.21 = 4.8 months. |
| Conversion rate (install to paid) | 0.8 % | sourced | ([source](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga)) |
| CAC (paid search) | 1250 USD | estimate | Paid search: $3 CPC / (30% click-to-install x 0.8% install-to-paid) = $1,250. |
| LTV | 18 USD | estimate | 5 x 0.75 x 4.8 months = $18. |
| LTV : CAC | 0.014 ratio | estimate | 18 / 1,250 = 0.014 on paid ads; unpaid channels have unknown CAC. |
| Payback (months) | 332 months | estimate | 1,250 / (5 - 1.24) = 332 months. |
| Fixed costs / month | 27 USD/month | estimate | Supadata Pro $17 + hosting/domain ~$10. |
| Break-even (customers) | 8 customers | estimate | 27 / 3.76 gross profit per customer = 7.2, rounded up to 8. |
| Time to first revenue (weeks) | 6 weeks | estimate | 2 weeks build + 1 week store review + ~3 weeks to first organic payer. |

| Cost item | Monthly | Source |
|---|---|---|
| Transcript API (Supadata Pro, 3,000 credits) | $17 | [SocialCrawl](https://www.socialcrawl.dev/blog/best-youtube-data-apis-2026) |
| LLM (Gemini 3.1 Flash-Lite, ~$0.0019/summary) | variable | [Developers Digest](https://www.developersdigest.tech/models/gemini-3-1-flash-lite) |
| Stripe (2.9% + $0.30, US standard rate, unverified this run) | ~$0.445/payment | estimate |
| Hosting + domain | ~$10 | estimate |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|---|---|---|---|---|---|
| Pessimistic | 3 | $15 | $31 | $-16 | Store listing buried; 3 payers |
| Base | 15 | $75 | $46 | $29 | ~1,900 installs x 0.8%; $27 fixed + 15 x $1.24 |
| Optimistic | 80 | $400 | $126 | $274 | One viral Reddit/TikTok post; still under $300/month profit |

## 11. Feasibility and risks

| Factor | Assessment |
|---|---|
| Build effort to a test | 1-2 weeks for an MV3 extension + Stripe (estimate) |
| Skills missing | Distribution, copywriting, community building |
| Key dependencies | YouTube transcripts, Chrome Web Store review, LLM API |
| Legal / compliance | YouTube Developer Policies bar scraping; privacy policy and consent required ([CWS policies](https://developer.chrome.com/docs/webstore/program-policies/policies)) |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|---|---|---|---|---|
| 1 | Free Google features (Gemini in Chrome, YouTube Ask) cap willingness to pay | H | H | Pick a job Google does not do (creator tools, flashcards) | [link](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/) |
| 2 | YouTube blocks transcript access | M | H | Fetch in the user's browser, or use own-channel captions API | [link](https://github.com/jdepoix/youtube-transcript-api/issues/592) |
| 3 | Breach of YouTube Developer Policies (scraping, derived data, UI changes) | M | M | Avoid the API for third-party videos; legal review | [link](https://developers.google.com/youtube/terms/developer-policies) |
| 4 | Chrome Web Store rejection or user distrust of new AI extensions | M | M | Minimal permissions, clear privacy policy | [link](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html) |
| 5 | High churn (~21%/month) erases MRR growth | H | M | Annual plans; saved summary library | [link](https://www.revenuecat.com/blog/growth/ai-app-retention-study) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|---|---|---|---|---|
| profit (25) | gross_margin | 3.5 | About 75% after LLM, transcript API and Stripe on $5 (estimate); Stripe is the biggest cost. | [link](https://www.developersdigest.tech/models/gemini-3-1-flash-lite) |
| profit (25) | ltv_cac | 1.5 | LTV ~$18 at 21% AI-app churn vs ~$1,250 paid CAC; only unpaid channels can work, unproven (estimate). | [link](https://www.revenuecat.com/blog/growth/ai-app-retention-study) |
| profit (25) | pricing_power | 1 | Gemini in Chrome and Glasp do it free; free sets the anchor at $0. | [link](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/) |
| feasibility (20) | build_effort | 4 | A developer can ship an MV3 extension plus Stripe in 1-2 weeks (estimate). | — |
| feasibility (20) | skills_match | 4 | Has the build skills; lacks distribution and copywriting skills. | — |
| feasibility (20) | capital_needed | 4.5 | About $27/month fixed (transcript API, hosting) fits a $500 budget. | [link](https://www.socialcrawl.dev/blog/best-youtube-data-apis-2026) |
| time_to_first_revenue (15) | time_to_mvp | 4 | MVP in 1-2 weeks at 10 h/week, plus Chrome Web Store review (estimate). | — |
| time_to_first_revenue (15) | sales_cycle | 4.5 | $5/month consumer impulse buy, no committee. | — |
| time_to_first_revenue (15) | channel_readiness | 2 | No audience; store search ranks by installs and ratings, led by 1M-user free incumbents. | [link](https://developer.chrome.com/docs/webstore/discovery) |
| demand (15) | search_demand | 3.5 | 'youtube summarizer' shows 49.5K search volume. | [link](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG) |
| demand (15) | trend | 3.5 | Search interest +167% (Exploding Topics); paid standalone demand eroded by free built-ins. | [link](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG) |
| demand (15) | willingness_to_pay | 2 | Reviewers advise staying on free tiers; users expect it free. | [link](https://tldv.io/blog/notegpt-review/) |
| competition (10) | free_alternatives | 1 | Gemini in Chrome (free, US) summarizes videos with timestamps; does the whole job. | [link](https://www.techrepublic.com/article/news-google-gemini-chrome-upgrade/) |
| competition (10) | competitor_density | 1.5 | 20+ direct tools: Glasp 1M users, Eightify, NoteGPT, Sider, Monica, Merlin, HARPA, Recall. | [link](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli) |
| competition (10) | differentiation | 1 | 'I am a developer' is not a product edge; no data, audience or cost advantage. | [link](https://www.producthunt.com/products/insighttube/launches) |
| risk (10) | legal_regulatory | 3 | Privacy policy and consent required by Chrome Web Store; copyright risk low for short summaries. | [link](https://developer.chrome.com/docs/webstore/program-policies/policies) |
| risk (10) | platform_dependency | 1.5 | Captions API needs edit rights; scraping is barred and blocked; YouTube ships its own Ask. | [link](https://developers.google.com/youtube/v3/docs/captions/download) |
| risk (10) | market_risk | 2 | Google is absorbing the feature into YouTube and Chrome. | [link](https://www.indiatvnews.com/technology/news/youtube-rolls-out-new-gemini-powered-ask-feature-how-it-works-2025-11-11-1017019) |
| fit (5) | skills | 3.5 | Developer skills cover the build; no marketing track record stated. | — |
| fit (5) | assets | 1 | No audience, list or data stated. | — |
| fit (5) | interest | 1.5 | Goal stated as side income, not domain passion. | — |

| Criterion | Mean | Points |
|---|---|---|
| profit (25) | 2.00 | 10.00 |
| feasibility (20) | 4.17 | 16.67 |
| time_to_first_revenue (15) | 3.50 | 10.50 |
| demand (15) | 3.00 | 9.00 |
| competition (10) | 1.17 | 2.33 |
| risk (10) | 2.17 | 4.33 |
| fit (5) | 2.00 | 2.00 |
| **Raw total** | | **54.8** |
| **Rules applied** | R7: total 55 − 10 = 45; R6 cap 49 (no further change) | |
| **Final score** | | **45 / 100** |

## 13. Sources

46 sources from 37 domains: 18 primary, 14 secondary, 14 tertiary.

1. [TechCrunch, Gemini in Chrome rolls out to all US users](https://techcrunch.com/2025/09/18/google-brings-gemini-in-chrome-to-us-users-unveils-agentic-browsing-capabilities-and-more/) — Gemini in Chrome free for US Mac/Windows desktop users — secondary — published 2025-09 — accessed 2026-11-11
2. [TechRepublic, Gemini Chrome upgrade](https://www.techrepublic.com/article/news-google-gemini-chrome-upgrade/) — Gemini in Chrome summarizes YouTube videos with key points and timestamps — secondary — published 2025-09 — accessed 2026-11-11
3. [Scrimba, Best AI video summarizers 2026](https://scrimba.com/articles/best-ai-video-summarizers-2026/) — Free alternatives; Eightify pricing; summarize.tech paused deployment — tertiary — published 2026-08 — accessed 2026-11-11
4. [Search Engine Journal, Google tests Ask YouTube](https://www.searchenginejournal.com/google-tests-ask-youtube-conversational-search-experiment/573175/) — YouTube conversational AI search test — secondary — published 2026 — accessed 2026-11-11
5. [iPhone in Canada, Google testing Ask YouTube AI search](https://www.iphoneincanada.ca/2026/04/28/google-testing-ask-youtube-ai-search/) — Ask YouTube tested April 2026 — secondary — published 2026-04 — accessed 2026-11-11
6. [India TV News, YouTube rolls out Gemini-powered Ask feature](https://www.indiatvnews.com/technology/news/youtube-rolls-out-new-gemini-powered-ask-feature-how-it-works-2025-11-11-1017019) — YouTube Ask button summarizes videos — secondary — published 2025-11 — accessed 2026-11-11
7. [9to5Google, YouTube conversational AI for Premium](https://9to5google.com/2024/09/24/youtube-conversational-ai-premium-subscribers/) — YouTube 'Summarize video' for US Premium on Android — secondary — published 2024-09 — accessed 2026-11-11
8. [Chrome Web Store, YouTube Summary with ChatGPT & Claude (Glasp)](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli) — Free extension, 1,000,000 users — primary — published unknown — accessed 2026-11-11
9. [Starter Story, Eightify breakdown](https://www.starterstory.com/stories/eightify-breakdown) — Eightify est. $45K/month, 100,000+ users, $4.95/month (estimate, not founder-reported) — secondary — published 2024-05 — accessed 2026-11-11
10. [NoteGPT, pricing](https://notegpt.io/pricing?type=team) — NoteGPT from $9/month annual — primary — published 2026 — accessed 2026-11-11
11. [Flowith, Monica AI pricing 2026](https://flowith.io/blog/monica-ai-pricing-2026-free-vs-pro-vs-pro-plus) — Monica $8.3-82.9/month — tertiary — published 2026-03 — accessed 2026-11-11
12. [Overchat, Merlin AI alternatives](https://overchat.ai/ai-hub/best-merlin-ai-alternatives) — Sider $4.99, Merlin ~$15/month — tertiary — published 2026 — accessed 2026-11-11
13. [Softwares.com, HARPA AI pricing](https://www.softwares.com/software/harpa-ai/pricing) — HARPA AI free / ~$15 premium — tertiary — published 2026 — accessed 2026-11-11
14. [ChatYT, alternatives comparison](https://chatyt.io/alternatives) — Recall free/$7; summarize.tech $9.99-14.99 — tertiary — published 2026 — accessed 2026-11-11
15. [Product Hunt, InsightTube launch](https://www.producthunt.com/products/insighttube/launches) — Look-alike launch 2026-01-22 — primary — published 2026-01 — accessed 2026-11-11
16. [Product Hunt, YouTube Summarizer launch](https://www.producthunt.com/products/youtube-summarizer-5/launches) — Look-alike launch 2026-01-20 — primary — published 2026-01 — accessed 2026-11-11
17. [Product Hunt, Tube Insights launch](https://www.producthunt.com/products/tubeinsights/launches) — Look-alike launch 2026-01-28 — primary — published 2026-01 — accessed 2026-11-11
18. [Product Hunt, DeepTube launch](https://www.producthunt.com/products/deeptube/launches) — Look-alike launch 2026-01-05 — primary — published 2026-01 — accessed 2026-11-11
19. [Product Hunt, Transcription.video launch](https://www.producthunt.com/products/transcription-video/launches) — Look-alike launch 2026-02-10 — primary — published 2026-02 — accessed 2026-11-11
20. [Product Hunt, YTSummarizer](https://www.producthunt.com/products/ytsummarizer/launches) — YTSummarizer $29 one-time — primary — published 2026 — accessed 2026-11-11
21. [Chromeboard, 'Youtube Summary With Chat' listing](https://www.chromeboard.com/extension/youtube-summary-with-chat-cmohfjnlbonnegncdgnbcfcnjageeilk) — New look-alike listed 2026-04-13 with 83 users — tertiary — published 2026-04 — accessed 2026-11-11
22. [Indie Hackers, AI wrapper: 8 months, $4K revenue, $220 MRR](https://www.indiehackers.com/post/simple-ai-wrapper-in-auto-mode-8-months-4k-in-revenue-220-in-mrr-6d418c5a8e) — Summarify.me ~$220 MRR after 8 months — tertiary — published 2024 — accessed 2026-11-11
23. [TrustMRR, YouTube to Transcript listing](https://trustmrr.com/startup/youtube-to-transcript) — $200 MRR with 10k+ active users — tertiary — published unknown — accessed 2026-11-11
24. [Mozilla Add-ons, Glasp YouTube Summary (Firefox)](https://addons.mozilla.org/addon/2890360/) — Reviews report it stopped working; 4,908 users — primary — published unknown — accessed 2026-11-11
25. [Dictanote, YouTube Summary changelog](https://dictanote.co/youtube-summary/new/) — Removed transcript display citing YouTube API restrictions — primary — published unknown — accessed 2026-11-11
26. [tl;dv, NoteGPT review](https://tldv.io/blog/notegpt-review/) — Free tier is enough; advises not paying — tertiary — published 2026 — accessed 2026-11-11
27. [Exploding Topics, 'youtube summarizer'](https://explodingtopics.com/topic/youtube-summarizer-HMc3g3XG) — 49.5K search volume, +167% growth — secondary — published 2026 — accessed 2026-11-11
28. [Google for Developers, YouTube Data API captions.download](https://developers.google.com/youtube/v3/docs/captions/download) — Requires permission to edit the video; 200 quota units — primary — published unknown — accessed 2026-11-11
29. [Google for Developers, YouTube API Services Developer Policies](https://developers.google.com/youtube/terms/developer-policies) — No scraping; no derived data; no UI interference — primary — published unknown — accessed 2026-11-11
30. [GitHub, youtube-transcript-api issue #592](https://github.com/jdepoix/youtube-transcript-api/issues/592) — YouTube blocks cloud-IP transcript requests — tertiary — published 2026 — accessed 2026-11-11
31. [Chrome for Developers, Web Store program policies](https://developer.chrome.com/docs/webstore/program-policies/policies) — Single purpose, user-data disclosure, no unauthorized access — primary — published unknown — accessed 2026-11-11
32. [Chrome for Developers, CWS payments deprecation](https://developer.chrome.com/webstore/cws-payments-deprecation) — Must bring own payment processor — primary — published 2020-09 — accessed 2026-11-11
33. [Chrome for Developers, Web Store discovery](https://developer.chrome.com/docs/webstore/discovery) — Store ranking uses popularity, ratings, installs vs uninstalls — primary — published unknown — accessed 2026-11-11
34. [RevenueCat, AI app retention study](https://www.revenuecat.com/blog/growth/ai-app-retention-study) — 6.1% of AI monthly subs retained at 12 months — primary — published 2026-08 — accessed 2026-11-11
35. [ChartMogul, churn cheat sheet](https://chartmogul.com/resources/churn-cheat-sheet) — 8.9% median monthly churn for ARPA $0-10 — primary — published unknown — accessed 2026-11-11
36. [ChartMogul, SaaS conversion report](https://chartmogul.com/reports/saas-conversion-report/) — Freemium conversion 3-5% good — secondary — published unknown — accessed 2026-11-11
37. [DEV, freemium Chrome extension monetization after 6 months](https://dev.to/ktg0215/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga) — 0.8% install-to-paid on 5 extensions — tertiary — published 2026 — accessed 2026-11-11
38. [Search Engine Land, Google Ads costs rising 2025](https://searchengineland.com/google-ads-costs-rising-but-conversion-rates-improved-in-2025-477927) — Average CPC about $5.42 — secondary — published 2025 — accessed 2026-11-11
39. [Developers Digest, Gemini 3.1 Flash-Lite pricing](https://www.developersdigest.tech/models/gemini-3-1-flash-lite) — $0.25 / $1.50 per 1M tokens — tertiary — published 2026-10 — accessed 2026-11-11
40. [Supadata docs, get transcript](https://docs.supadata.ai/get-transcript) — 1 credit per existing transcript — primary — published unknown — accessed 2026-11-11
41. [SocialCrawl, best YouTube data APIs 2026](https://www.socialcrawl.dev/blog/best-youtube-data-apis-2026) — Supadata Pro $17 for 3,000 credits — tertiary — published 2026-07 — accessed 2026-11-11
42. [Mental Floss, words per minute people speak](https://www.mentalfloss.com/language/how-many-words-per-minute-do-people-speak) — ~150 spoken words per minute — secondary — published unknown — accessed 2026-11-11
43. [The Business Research Company via GII, video AI content summarization market](https://www.gii.tw/report/tbrc1994531-content-summarization-video-ai-global-market.html) — $2.16B (2025) to $6.54B (2030) — secondary — published 2026 — accessed 2026-11-11
44. [The Hacker News, Chrome extensions caught stealing AI chats](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html) — AI-extension trust climate — secondary — published 2026-01 — accessed 2026-11-11
45. [Malwarebytes, fake AI Chrome extensions](https://www.malwarebytes.com/blog/news/2025/01/google-chrome-ai-extensions-deliver-info-stealing-malware-in-broad-attack) — Google removed fake AI-assistant extensions — secondary — published 2025-01 — accessed 2026-11-11
46. [YouTLDR, YouTLDR vs Eightify](https://you-tldr.com/blog/youtldr-vs-eightify-comparison) — Eightify $4.99/month on annual billing — tertiary — published 2026 — accessed 2026-11-11
