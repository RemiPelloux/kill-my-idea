<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟡 PIVOT · 68/100
> **Email marketing for bloggers who sell info products**
>
> `███████░░░` 68 / 100 · confidence high, 27 sources
>
> - ❌ Funded incumbents own the field: Constant Contact had 555,000 paying customers at end-2012 ([10-K FY2012](https://www.sec.gov/Archives/edgar/data/0001405277/000119312513084678/d442306d10k.htm)), Infusionsoft $71M raised ([TechCrunch, 2013-01](https://techcrunch.com/?p=731324))
> - ❌ A small email-newsletter service already died here: Wildbit closed Newsberry on 2012-01-02 ([Wildbit, 2011](https://www.wildbit.com/blog/2011/11/08/a-difficult-day))
> - ✅ Rising niche at about 86% gross margin: SES at $0.10 per 1,000 emails ([Amazon, 2011](https://press.aboutamazon.com/2011/1/amazon-web-services-launches-amazon-simple-email-service)), blogger ebooks earning $20k in two weeks ([TNW, 2012](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks))
>
> **Could be saved:** pre-sell 10 blogger peers with hand-migrated lists → 71/100 (doable)
> **Cheapest test:** email 30 blogger peers a $29/month founding plan with free migration; count pre-payments in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 68/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2068%2F100-yellow)

# ConvertKit: email marketing for bloggers who sell courses and ebooks — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **as of 2013-06-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 68/100 (raw 68.2) |
| **Confidence** | high: 15 sourced sub-scores of 21, 27 sources (8 primary) |
| **Countries** | US |
| **Assumptions** | Budget USD 5,000; full time; channel = own blog + blogger peers; audience under 10k readers; founder sells his own ebooks; churn 5%/month (unsourced) |

## 0. Executive summary

**Answer:** **PIVOT**: real demand and **86%** margins, but a crowded field (Constant Contact 555k customers, Infusionsoft $71M raised) means it lives or dies on pre-selling blogger peers before building.

**Key findings**
1. **Funded incumbents own the category**: Constant Contact had **555,000** paying customers at end-2012 and Infusionsoft raised **$54M** in 2013-01. ([source](https://www.sec.gov/Archives/edgar/data/0001405277/000119312513084678/d442306d10k.htm))
2. **Info-product sellers are a rising niche**: designer-bloggers made **$20,000** in two weeks from one ebook (TNW, 2012); Udemy raised $12M (2012). ([source](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks))
3. **Unit economics work on Amazon SES**: SES at **$0.10 per 1,000** emails plus Stripe fees leave about **86%** gross margin at $29/month (estimate). ([source](https://press.aboutamazon.com/2011/1/amazon-web-services-launches-amazon-simple-email-service))

**Steelman:** Bloggers selling ebooks are a rising, underserved niche: MailChimp turns away affiliate marketers and Infusionsoft is overkill. A developer who is his own customer can ship a focused tool on SES at **86%** margin. The evidence supports demand and margin, not the channel.

**Recommendation:** Pre-sell before building: get 10 blogger peers to pay $29/month for a hand-migrated founding plan within 7 days, or drop the idea.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Stuck at a few dozen accounts: peers liked it but stayed on AWeber or MailChimp | channel_readiness | H | fewer than 5 of 30 peers pre-pay |
| 2 | $29 lost against MailChimp free and $19 AWeber; small lists saw no reason to pay more | pricing_power | M | more than half of prospects ask for a free tier |
| 3 | Build and deliverability work took 6 months, burning the $5,000 runway first | build_effort | M | beta not sending live campaigns by week 12 |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Pre-sell 10 blogger peers at $29 and migrate their lists by hand before building the full app | channel_readiness, time_to_mvp, differentiation | 71/100 (estimate) | doable | 2 weeks | under $200 | 10 peers with lists over 1,000 and a product to sell |
| 2 | Narrow to course sellers: tagging plus sales sequences at $49+/month, priced against Infusionsoft not AWeber | pricing_power, differentiation | 70/100 (estimate) | hard | 3–4 months | about $1,000 | Automation and checkout integrations (Gumroad, Stripe) |

## 2. Next step: 7-day test

**Cheapest test:** Email 30 blogger peers who sell ebooks: offer a $29/month founding plan with hands-on list migration; count pre-payments in 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | List 30 blogger peers who sell ebooks or courses to a list | 30 names with list size noted |
| 2 | One-page offer: $29/month founding plan, free hand migration | page live with a Stripe payment link |
| 3–5 | Email and message each peer personally | at least 15 replies |
| 6–7 | Ask for the first month up front | 5 or more pre-payments, or stop |

**Stop if:** fewer than 5 of 30 peers commit to pay $29/month by day 7 · fewer than 3 lists over 1,000 subscribers migrated by day 30 · under $1,000 MRR by month 6.

## 3. Source

> ConvertKit: email marketing for bloggers who sell courses and ebooks, $29 per month, launch country US. Score it as of 2013-06-01: use only evidence published on or before that date (set verdict.as_of). Founder: a solo blogger-developer bootstrapping with $5,000. Just go: do not ask questions. Use the slug convertkit.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear (partial) | MailChimp free covers broadcasts for small lists; Sendy is $40 one-off on SES; neither targets course-sales sequences | [TNW, 2012-08](https://thenextweb.com/news/this-self-hosted-newsletter-app-is-100x-cheaper-than-mailchimp-and-campaign-monitor) |
| 2 | Strong direct competitor | **hit** | Constant Contact 555,000 paying customers (FY2012); Infusionsoft $71M total funding (2013-01) | [SEC 10-K](https://www.sec.gov/Archives/edgar/data/0001405277/000119312513084678/d442306d10k.htm) |
| 3 | Graveyard | **hit** | Wildbit closed Newsberry on 2012-01-02, idle in a crowded field; iContact sold to Vocus for $169M (2012) | [Wildbit, 2011-11](https://www.wildbit.com/blog/2011/11/08/a-difficult-day) |
| 4 | No distribution channel | clear | Own blog plus peer bloggers who launch to their lists are a credible route to 10 customers; paid-search CPC for "email marketing" in 2013 unknown | [TNW, 2012-10](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks) |
| 5 | Costs eat the margin | clear | SES $0.10/1,000 emails + Stripe 2.9% + $0.30 → ~86% gross margin | [Amazon, 2011-01](https://press.aboutamazon.com/2011/1/amazon-web-services-launches-amazon-simple-email-service) |
| 6 | Weak or falling demand | clear | Udemy $12M Series B (2012-12), Gumroad (2011), $20k ebook launches (2012) | [TNW, 2012-12](https://thenextweb.com/news/education-marketplace-udemy-raises-12-million-to-expand-its-content-and-explore-new-platforms) |
| 7 | Legal / platform risk | clear | CAN-SPAM is routine; Gmail Promotions tab (2013-05-29) and SES dependency are risks, not blockers | [AllTopStartups, 2013-05](https://alltopstartups.com/2013/05/29/gmail-users-are-getting-a-brand-new-inbox-with-a-social-tab/) |
| 8 | Saturated wave (5 adjacent launches, 2012-06 to 2013-05) | clear | Show HN: Userfox, Dead Simple Email Collection, Sendy; none a direct clone | [HN, 2012-10](https://news.ycombinator.com/item?id=4715237) |

**Primary kill shot:** strong_competitor.

## 6. Market

- **Target customer:** US bloggers selling their own ebooks and courses to a list of 1k–20k subscribers.
- **Pain:** generic ESPs make it hard to segment buyers and run launch sequences; Infusionsoft is expensive and complex. Today: AWeber or MailChimp plus Gumroad or e-junkie.
- **Demand signals:** $20k two-week ebook launches ([TNW, 2012](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks)); ~$10k/month non-SPI income ([Smart Passive Income, 2013-01](https://www.smartpassiveincome.com/blog/my-december-2012-monthly-income-report/)).
- **Trend:** rising ([Udemy, 2012-12](https://thenextweb.com/news/education-marketplace-udemy-raises-12-million-to-expand-its-content-and-explore-new-platforms)).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $2.4B/year US email marketing spend (2016 forecast) | sourced | [Forrester via MarketingProfs, 2011](https://www.marketingprofs.com/charts/2011/5820/forrester-interactive-spending-to-reach-766b-by-2016) |
| SAM | $10.4M/year | estimate | 30,000 US info-product bloggers (assumed) × $29 × 12 |
| SOM (year 1) | $52k/year | estimate | 0.5% of SAM = 150 accounts |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Amazon SES: $0.10 per 1,000 emails | 2011-01 | [Amazon](https://press.aboutamazon.com/2011/1/amazon-web-services-launches-amazon-simple-email-service) |
| Gumroad: sell digital goods with a link | 2011-04 | [TNW](https://thenextweb.com/news/gumroad-sell-digital-goods-with-a-link-no-storefront-needed) |
| Stripe: card billing with no setup or monthly fees | 2011-09 | [TechCrunch](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) |
| Blogger ebook launches earn $10k–$20k in weeks | 2012-10 | [TNW](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks) |
| Udemy $12M Series B | 2012-12 | [TNW](https://thenextweb.com/news/education-marketplace-udemy-raises-12-million-to-expand-its-content-and-explore-new-platforms) |

Cheap sending, easy billing and a booming info-product niche open the window.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US bloggers selling their own ebooks or courses, list of 1k–20k subscribers |
| **Where** | Smart Passive Income community, Hacker News, Twitter designer/developer circles, ProBlogger, Gumroad sellers |
| **Pays for today** | AWeber (~$19/month entry, unverified for 2013) or MailChimp, plus Gumroad at 5% + 30¢ per sale ([TechCrunch, 2011](https://techcrunch.com/2011/12/14/gumroad-lets-you-sell-anything-you-make/amp/)) |
| **Budget** | about $20–$50/month (estimate) |
| **Trigger** | Planning a launch and finding the current ESP can't segment buyers or run a launch sequence |

## 7. Competition

| Competitor | Country | What they do | Price (date) | Traction /5 | Gap |
|------------|---------|--------------|--------------|-------------|-----|
| MailChimp | US | DIY newsletters, free tier | $0 entry | 5 (~1M users, HN 2013-05) | Turns away affiliate marketers |
| Constant Contact | US | SMB email | ~$15/month (unverified) | 5 (555,000 customers) | Built for local businesses |
| Infusionsoft | US | CRM + marketing automation | unknown | 5 ($71M raised) | Expensive, complex |
| AWeber | US | Autoresponders | ~$19/month (unverified) | 4 | Weak segmentation (unverified) |
| iContact | US | SMB email | unknown | 4 (sold for $169M) | Generic |
| Sendy | AU | Self-hosted on SES | $40 one-off (2012-08) | 2 | Self-hosting, no sales automation |

- **Free alternatives:** MailChimp free (2,000-subscriber cap confirmed only by a 2014 capture, so excluded); Sendy near-free.
- **Edge:** founder is the customer; a tool built for selling info products, not generic newsletters. It can be copied.
- **First 10 customers:** blogger peers in the founder's network, hand-migrated.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $29/month | estimate | founder's price |
| Variable cost per unit | $4.14/month | estimate | Stripe 0.029 × 29 + 0.30 = 1.14; SES 30,000 emails × $0.10/1,000 = 3.00 |
| Gross margin % | 85.7% | estimate | (29 − 4.14) / 29 |
| Churn / lifetime | 5%/month / 20 months | estimate | assumed; Skok flags >2%/month ([For Entrepreneurs, 2012](https://forentrepreneurs.com/saas-survey)) |
| Conversion rate | 2% | estimate | assumed |
| CAC | $120 | estimate | 8 h organic outreach × $15/h |
| LTV | $497 | estimate | 29 × 0.857 × 20 |
| LTV : CAC | 4.1 | estimate | 497 / 120 (paid CAC unknown) |
| Payback | 4.8 months | estimate | 120 / 24.86 |
| Fixed costs / month | $150 | estimate | hosting ~$100 + tools ~$50 |
| Break-even | 7 customers (207 to pay a $5,000/month salary) | estimate | 150 / 24.86 |
| Time to first revenue | 12 weeks | estimate | 8–12 weeks build + beta |

| Scenario | Customers | Revenue / month | Costs / month | Note |
|----------|-----------|-----------------|---------------|------|
| Pessimistic | 30 | $870 | $274 | Peers only |
| Base | 150 | $4,350 | $771 | SOM year 1 |
| Optimistic | 500 | $14,500 | $2,220 | Word of mouth |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Pre-sale: days. Usable ESP beta: 2–3 months |
| Skills missing | Deliverability and abuse operations |
| Key dependencies | Amazon SES, Stripe, Gmail inbox placement |
| Legal / compliance | CAN-SPAM: unsubscribe, postal address, honour opt-outs ([FTC guide, 2013](https://webarchive.library.unt.edu/web/20130214054537/http://business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business)) |

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|------------|--------|------------|
| 1 | Peers don't switch from AWeber/MailChimp | H | H | Hand-migrate lists free |
| 2 | One spammy sender hurts shared reputation | M | H | Vet customers, double opt-in |
| 3 | Gmail Promotions tab lowers launch opens | M | M | Plain-text, personal emails |
| 4 | $5,000 runs out before ~207 accounts | H | H | Keep consulting income; annual pre-sales |

**Type checks (SaaS):** churn_benchmark: unknown (no pre-2013 monthly benchmark for $29 no-contract SMB SaaS). switching_cost: unknown (lists and sequences must move; no dated source on import rules).

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 4.5 | ~86% (estimate) |
| | LTV : CAC | 3.5 | 4.1 organic estimate; paid CAC unknown |
| | pricing power | 2.5 | $29 above $19 AWeber and MailChimp free |
| Feasibility (20) | build effort | 2.5 | 2–3 months to a usable beta |
| | skills match | 4 | developer + blogger; deliverability new |
| | capital needed | 3.5 | $5,000 fits, no salary runway |
| Time to revenue (15) | time to MVP | 2.5 | 8–12 weeks |
| | sales cycle | 4 | self-serve monthly card |
| | channel readiness | 3.5 | own blog + peers, size assumed |
| Demand (15) | search demand | 4 | $2.4B US spend forecast |
| | trend | 4 | rising info-product economy |
| | willingness to pay | 4 | 555,000 paying CC customers |
| Competition (10) | free alternatives | 2.5 | MailChimp free partially covers |
| | competitor density | 1.5 | 20+ ESPs, several funded |
| | differentiation | 3 | info-product focus, copyable |
| Risk (10) | legal / regulatory | 3.5 | CAN-SPAM routine |
| | platform dependency | 3 | SES, Gmail tabs |
| | market risk | 4 | durable channel |
| Fit (5) | skills | 4 | both halves of the job |
| | assets | 3 | modest audience (assumed) |
| | interest | 4 | own customer (assumed) |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 3.50 | 17.50 |
| Feasibility (20) | 3.33 | 13.33 |
| Time to revenue (15) | 3.33 | 10.00 |
| Demand (15) | 4.00 | 12.00 |
| Competition (10) | 2.33 | 4.67 |
| Risk (10) | 3.50 | 7.00 |
| Fit (5) | 3.67 | 3.67 |
| **Raw total** | | **68.2** |
| **Rules applied** | none | |
| **Final score** | | **68 / 100** |

## 13. Sources

27 sources from 19 domains: 8 primary, 11 secondary, 8 tertiary. All published on or before 2013-06-01; accessed 2026-11-11. Excluded as later than the cutoff: MailChimp's 2014 pricing capture, later AWeber/AWS pricing pages, and Tunguz (2013-09).

1. [Wildbit: A difficult day](https://www.wildbit.com/blog/2011/11/08/a-difficult-day) — graveyard — primary — 2011-11-08
2. [Vocus 8-K: iContact acquisition](https://capedge.com/filing/1329919/0001299933-12-000493/8K/file/6) — consolidation — primary — 2012
3. [TNW: designers selling ebooks](https://thenextweb.com/news/designers-share-tips-tricks-writing-selling-ebooks) — demand — secondary — 2012-10-02
4. [TNW: Udemy raises $12M](https://thenextweb.com/news/education-marketplace-udemy-raises-12-million-to-expand-its-content-and-explore-new-platforms) — trend — secondary — 2012-12-07
5. [Smart Passive Income: Dec 2012 report](https://www.smartpassiveincome.com/blog/my-december-2012-monthly-income-report/) — demand — primary — 2013-01-15
6. [MarketingProfs: Forrester forecast](https://www.marketingprofs.com/charts/2011/5820/forrester-interactive-spending-to-reach-766b-by-2016) — TAM — secondary — 2011
7. [TNW: Gumroad launch](https://thenextweb.com/news/gumroad-sell-digital-goods-with-a-link-no-storefront-needed) — why now — secondary — 2011-04-09
8. [Blog: MailChimp vs affiliate marketing](https://businesscard-size.blogspot.com/2011/10/war-against-affiliate-marketing.html) — gap — tertiary — 2011-10-27
9. [TechCrunch: Infusionsoft $54M](https://techcrunch.com/?p=731324) — competitor — secondary — 2013-01-07
10. [PR Newswire: Infusionsoft $54M](https://prnewswire.com/news-releases/goldman-sachs-leads-54-million-investment-in-infusionsoft-185857522.html) — competitor — primary — 2013-01-07
11. [Fortune: VC deals](https://fortune.com/2013/01/08/venture-capital-deals-270/) — competitor — secondary — 2013-01-08
12. [TNW: Sendy](https://thenextweb.com/news/this-self-hosted-newsletter-app-is-100x-cheaper-than-mailchimp-and-campaign-monitor) — near-free alternative — secondary — 2012-08-03
13. [HN: Userfox](https://news.ycombinator.com/item?id=4715237) — wave — tertiary — 2012-10-29
14. [HN: Dead Simple Email Collection](https://news.ycombinator.com/item?id=4493746) — wave — tertiary — 2012-09-08
15. [Amazon: SES launch](https://press.aboutamazon.com/2011/1/amazon-web-services-launches-amazon-simple-email-service) — costs — primary — 2011-01-25
16. [TechCrunch: Stripe launches](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) — costs — secondary — 2011-09-30
17. [TechCrunch: Gumroad fees](https://techcrunch.com/2011/12/14/gumroad-lets-you-sell-anything-you-make/amp/) — ICP — secondary — 2011-12-14
18. [AllTopStartups: Gmail tabs](https://alltopstartups.com/2013/05/29/gmail-users-are-getting-a-brand-new-inbox-with-a-social-tab/) — platform risk — secondary — 2013-05-29
19. [For Entrepreneurs: SaaS survey](https://forentrepreneurs.com/saas-survey) — churn — secondary — 2012 (inferred)
20. [SEC: Constant Contact 10-K FY2012](https://www.sec.gov/Archives/edgar/data/0001405277/000119312513084678/d442306d10k.htm) — competitor — primary — 2013-02
21. [Constant Contact: FY2012 results](https://news.constantcontact.com/press-release-constant-contact-announces-fourth-quarter-and-full-year-2012-financial-results) — competitor — primary — 2013-02
22. [HN: MailChimp hits 1 million users](https://news.ycombinator.com/item?id=5773360) — free alternative scale — tertiary — 2013-05-27
23. [Blog: MailChimp announces 1 million](https://minimalistwordpressthemes.blogspot.com/2013/02/mailchimp-announces-1-million.html) — free alternative scale — tertiary — 2013-02-02
24. [Chaotic Flow: OPEXEngine churn](https://chaotic-flow.com/?p=4525) — churn (unverified) — tertiary — 2012-01
25. [MarketingProfs: AdWords CPC infographic](https://marketingprofs.com/chirp/2012/9431/google-adwords-cpc-ctr-ad-impressions-conversion-rates-infographic) — distribution — secondary — 2012
26. [Blog: MailChimp DIY email provider](https://my-guarava-prya.blogspot.com/2012/01/mailchimp-do-it-yourself-email-provider.html) — free alternative — tertiary — 2012-01-24
27. [FTC: CAN-SPAM guide (archived 2013-02-14)](https://webarchive.library.unt.edu/web/20130214054537/http://business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business) — legal — primary — 2013-02-14
