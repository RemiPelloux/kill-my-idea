<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟢 GO · 71/100
> **A form builder you type like a doc**
>
> `███████░░░` 71 / 100 · confidence medium, 34 sources
>
> - ❌ Typeform made ~$1.6M a month with ~40,000 customers (2018) and raised $52M+ ([Latka](https://getlatka.com/companies/typeform/interviews/typeform-david-okuniev-2018), [TechCrunch](https://techcrunch.com/2017/09/11/typeform-a-platform-for-conversational-data-collection-raises-35m/embed/))
> - ❌ Google Forms does basic forms free with unlimited responses ([blog, 2017](https://julie-young.squarespace.com/blog/2017/1/4/market-research-tools-using-google-forms-for-surveys-screeners))
> - ✅ Mass, rising demand: SurveyMonkey revenue +21% to $307M in FY2019 ([SVMK 10-K](https://www.sec.gov/Archives/edgar/data/1739936/000156459020007349/svmk-10k_20191231.htm)), and a free "powered by" badge loop is a proven channel ([TNW](https://thenextweb.com/news/why-typeform-is-awesome))
>
> **Cheapest test:** landing page + 60-second doc-style demo on Indie Hackers, r/nocode and Makerpad: 300 sign-ups and 10 Pro pre-orders in 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: GO 71/100](https://img.shields.io/badge/kill--my--idea-GO%2071%2F100-brightgreen)

# Tally: a form builder that works like a doc — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), scored **as of 2020-06-01** (only evidence published on or before that date) |
| **Verdict** | GO · 71/100 (raw 71.2) |
| **Confidence** | medium: 12 sourced sub-scores of 21, 34 sources (13 primary) |
| **Countries** | BE (base), selling worldwide online |
| **Assumptions** | Pro at $29/month; bootstrapped, near-zero budget; goal is a startup paying two salaries; no existing audience; organic channel (Product Hunt, communities, "Made with Tally" badge). No questions asked ("just go"). |

## 0. Executive summary

**Answer:** **GO**, barely. Demand is mass and rising, margins are software-grade and two developers can build it cheaply; the risk is a **crowded field** led by Typeform and free Google Forms, so the free plan must become the channel.

**Key findings**
1. **Mass, rising demand for forms**: SurveyMonkey grew revenue 21% to $307M in FY2019 and Jotform hit 5M users (2019-07). ([SVMK 10-K](https://www.sec.gov/Archives/edgar/data/1739936/000156459020007349/svmk-10k_20191231.htm))
2. **Leaders are strong, one is free**: Typeform made ~$1.6M a month (2018) on $52M+ raised; Google Forms does basic forms for free. ([Latka](https://getlatka.com/companies/typeform/interviews/typeform-david-okuniev-2018))
3. **The badge loop is the channel**: Typeform's "powered by" button was its top traffic source, a free channel a generous free plan can copy. ([TNW, 2017](https://thenextweb.com/news/why-typeform-is-awesome))

**Steelman:** Typeform doubled revenue on a free-form badge loop while its users complain about rising prices; a doc-style builder with a generous free plan rides the same loop at near-zero CAC, in the year Notion made doc-style editing mainstream ($2B, 2020-04). No sub-score contradicts it.

**Recommendation:** Build it, but ship the free plan with a "Made with Tally" badge from day one and launch on Product Hunt; stop if free-to-paid stays under 1% after 90 days.

**Premortem:**

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | The generous free plan covers almost every need, so under 1% of users ever upgrade to Pro | pricing_power | H | Fewer than 5 Pro upgrades per 1,000 active free users |
| 2 | Launch noise fades among 10+ form tools; Typeform and Google Forms keep the makers | strong_competitor | M | Fewer than 300 sign-ups from the Product Hunt launch week |
| 3 | Pro users churn 7%+ a month after one-off projects, so revenue plateaus | ltv_cac | M | More than 10% of month-1 Pro users cancel before month 2 |

## 1. How to make it stronger

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | "Made with Tally" badge on every free form + launch on Product Hunt, Indie Hackers, Notion/no-code communities | channel_readiness, ltv_cac | 74/100 (estimate) | doable | 1–2 weeks | ~$0 | A shipped free plan and a launch post |
| 2 | Gate a few high-value features (remove branding, custom domain, uploads, team) in Pro | pricing_power, conversion | 73/100 (estimate) | doable | 1 week | ~$0 | Usage data on which features free users hit |

## 2. Next step: 7-day test

**Cheapest test:** landing page with a 60-second doc-style demo, posted to Indie Hackers, r/nocode and Makerpad.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Record the demo; landing page with a waitlist | Page live, demo under 60 s |
| 2 | Post on Indie Hackers, r/nocode, Makerpad, Twitter #nocode | 100+ visits per post |
| 3–5 | Reply to every comment; offer an annual Pro pre-order | 150+ waitlist sign-ups |
| 6 | Interview 10 sign-ups on what they pay for forms today | 6 of 10 pay or have paid |
| 7 | Count against the kill criteria | 300 sign-ups, 10 pre-orders |

**Stop if:** fewer than 150 sign-ups by day 7 (rework the pitch); fewer than 5 Pro pre-orders at $29/month by day 14 (rethink the paid plan); free-to-paid below 1% after 90 days of launch (change the Pro gate).

## 3. Source

> Tally: a form builder that works like a doc, free with a paid Pro plan, launch country BE (Belgium, selling worldwide online). Score it as of 2020-06-01. Founder: two bootstrapped developers.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | Google Forms free with unlimited responses (2017); TellForm open-source Typeform alternative (2018-12) | [blog](https://julie-young.squarespace.com/blog/2017/1/4/market-research-tools-using-google-forms-for-surveys-screeners), [PH](https://www.producthunt.com/products/tellform/launches) |
| 2 | Strong direct competitor | **hit** | Typeform ~$1.6M/month, ~40k customers (2018), $52M+ raised; SurveyMonkey $307M (FY2019); Jotform 5M users (2019-07) | [Latka](https://getlatka.com/companies/typeform/interviews/typeform-david-okuniev-2018) |
| 3 | Graveyard | clear | No form-builder shutdown or post-mortem found before 2020; Wufoo sold for a reported $35M (2011), an exit | [TechCrunch](https://techcrunch.com/2011/04/25/wufoo-35-million-surveymonkey) |
| 4 | No distribution channel | clear | Typeform's "powered by" button was its top traffic source (2017); Wispform got 174 PH upvotes (2019-08) | [TNW](https://thenextweb.com/news/why-typeform-is-awesome) |
| 5 | Costs eat the margin | clear | Stripe 1.4% + €0.25 EU cards; hosting from $25/dyno/month: ~93% gross margin (estimate) | [Fortune](https://fortune.com/2016/06/08/stripe-payments-france/), [Heroku](https://www.heroku.com/blog/dynos-pricing-ga/) |
| 6 | Weak or falling demand | clear | SurveyMonkey revenue +21% (FY2019); Jotform 4M → 5M users in 10 months | [SVMK](https://surveymonkey.com/newsroom/fourth-quarter-fiscal-year-2019-financial-results) |
| 7 | Legal / platform risk | clear | GDPR Art. 28 processor duties (APD avis 98/2019), EU VAT MOSS; Schrems II pending: host in the EU | [APD](https://www.autoriteprotectiondonnees.be/publications/avis-n-98-2019.pdf), [SPF Finances](https://blog.forumforthefuture.be/fr/article/tva-sur-les-services-electroniques-transfrontaliers-le-mini-guichet-unique-moss/6138) |
| 8 | Saturated wave (4 look-alike launches, 2019-06 to 2020-06) | clear | Wispform, Tripetto for WordPress, Form-Builder, Webiny Form Builder | [PH](https://www.producthunt.com/products/wispform/launches) |

**Primary kill shot:** strong competitor.

**Type checks (SaaS):** churn benchmark **hit**: SMB self-serve SaaS churns 5–8% a month (Baremetrics 7.7%, 2017), so lifetime is ~17 months. Switching cost **clear**: a new form takes minutes to rebuild; incumbents hold users through existing embeds and integrations (estimate).

## 6. Market

- **Target customer:** makers, indie founders and no-code builders building waitlists, surveys and applications, already in Notion.
- **Pain:** polished forms cost ~$40/month (Typeform ASP, 2018); free ones (Google Forms) look plain.
- **Demand signals:** Typeform ~50M form landings a month (2018); Jotform 5M users; SurveyMonkey 720,921 paying users.
- **Trend:** rising (SurveyMonkey +21% FY2019; Typeform ~2x mid-2017 to mid-2018).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | ~$380M/year | estimate | SurveyMonkey $307M + Jotform ~$54M + Typeform ~$19M, a lower bound; no usable market report ([Orbis](https://orbisresearch.com/reports/index/global-form-builder-software-market-growth-status-and-outlook-2019-2024) has placeholders) |
| SAM | ~$100M/year | estimate | Self-serve maker/SMB form builders, excluding enterprise surveys |
| SOM (year 1) | ~$100k ARR | estimate | 0.1% of SAM |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Notion reaches a $2B valuation: doc-style block editing becomes a mainstream habit | 2020-04 | [TechCrunch](https://techcrunch.com/2020/04/01/notion-hits-2-billion-valuation-in-new-raise/embed/) |
| Notion sees surging use as work moves home (COVID-19) | 2020-04 | [Axios](https://www.axios.com/2020/04/02/notes-app-notion-raises-money-at-2-billion-valuation) |
| Webflow raises $72M: no-code draws money and makers | 2019-08 | [AppMaster](https://appmaster.io/news/webflow-secures-whopping-72m-series-a-funding-no-code-movement-gains-momentum) |
| Typeform users complain of constant price increases and a shrinking free plan | 2020-05 | [QuestionScout](https://www.questionscout.com/blog/typeform-alternatives-for-2020-top-10-typeform-alternatives) |

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Makers, indie founders and no-code builders who already work in Notion |
| **Where** | Product Hunt, Indie Hackers, Makerpad / Twitter #nocode, r/nocode and r/SideProject, Notion communities |
| **Pays for today** | Typeform at ~$40/month average (2018), or Google Forms for free |
| **Budget** | $0–40/month (estimate) |
| **Trigger** | Hitting Typeform's free-plan limit or needing to remove branding on a launch form |

## 7. Competition

| Competitor | Country | Price | Traction /5 | Gap |
|------------|---------|-------|-------------|-----|
| Typeform | ES | ~$40/month ASP (2018) | 5 | Expensive, limited free plan |
| Google Forms | US | free | 5 | Plain design, little branding |
| Jotform | US | unknown (no dated page) | 5 | Cluttered, feature-heavy |
| SurveyMonkey / Wufoo | US | ARPU $450/year (FY2019) | 5 | Survey/enterprise focus |
| Wispform | — | unknown | 2 | Cheaper Typeform clone |
| TellForm | — | free, open source | 1 | Self-hosted |

- **Free alternatives:** Google Forms, TellForm.
- **Edge:** doc-style typing instead of drag-and-drop, plus a free plan with unlimited forms; real but copyable.
- **First 10 customers:** Product Hunt / Indie Hackers launch and the badge on free forms.

## 8. What customers say

| Pain | Quote (verbatim) | Source, date |
|------|------------------|--------------|
| Typeform price rises | "Constantly Increasing pricing" | [QuestionScout](https://www.questionscout.com/blog/typeform-alternatives-for-2020-top-10-typeform-alternatives), 2020-05 (competitor blog) |
| Shrinking free plan | "They keep removing features from their free and cheaper plan, making it impossible to use for free users" | same |
| Price for occasional use | "But expensive if you don't use it often" | [TrustRadius](https://www.trustradius.com/reviews/typeform-2019-02-19-23-49-18), 2019-02 |

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $29/month | estimate | Assumed, below Typeform's ~$40 ASP |
| Variable cost | $1.9/month | estimate | Stripe ~3.1% blended ($0.9) + ~$1 infra/support |
| Gross margin | 93% | estimate | (29 − 1.9) / 29 |
| Churn / lifetime | 6% / 16.7 months | estimate | Baremetrics 7.7% (2017), ProfitWell 3–4% (2019) |
| Conversion | 0.2% visitor → paid | estimate | 10% sign-up × 2% free-to-paid (Jotform implied < 3%) |
| CAC | ~$60 organic | estimate | ~200 h × $30/h per 100 customers; paid search ~$4,900 |
| LTV | ~$452 | estimate | 29 × 0.93 × 16.7 |
| LTV : CAC | ~7.5 organic | estimate | 452 / 60; below 0.1 on paid search |
| Payback | 2.2 months | estimate | 60 / 27 |
| Fixed costs | ~$150/month | estimate | 2 Heroku dynos ($50) + database (~$50) + tools (~$50) |
| Break-even | 6 customers (costs); ~220 for two salaries | estimate | 150 / 27; €6k / 27 |
| Time to first revenue | ~14 weeks | estimate | 8–10 weeks build + ~4 weeks to first upgrades |

| Scenario | Customers | Revenue / month | Costs / month | Note |
|----------|-----------|-----------------|---------------|------|
| Pessimistic | 40 | $1,160 | $300 | 0.5% of 8k free users |
| Base | 200 | $5,800 | $600 | 2% of 10k free users |
| Optimistic | 600 | $17,400 | $1,500 | 3% of 20k free users, badge loop working |

## 11. Feasibility and risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|------------|--------|------------|
| 1 | Free plan too generous: conversion under 1% | H | H | Gate branding removal, custom domains, uploads |
| 2 | Typeform or Google copies doc-style editing | M | M | Ship faster, own the maker community |
| 3 | Phishing forms on the free plan hurt domain reputation | M | M | Abuse reporting and takedown from day one |
| 4 | US hosting transfer risk (Schrems II pending) | M | L | Host in the EU |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 4.5 | ~93% software margin (estimate) |
| | LTV : CAC | 3.5 | ~7.5 organic, fails on paid search |
| | pricing power | 2.5 | Free anchors low; must undercut ~$40 ASP |
| Feasibility (20) | build effort | 3 | ~2 months to a usable beta |
| | skills match | 4.5 | Two developers build it themselves |
| | capital needed | 5 | Near zero |
| Time to revenue (15) | time to MVP | 2.5 | 8–10 weeks |
| | sales cycle | 4.5 | Self-serve card checkout |
| | channel readiness | 3 | Badge loop and PH exist; no audience yet |
| Demand (15) | search demand | 4.5 | Mass need (5M Jotform users) |
| | trend | 4 | SurveyMonkey +21%, Typeform ~2x |
| | willingness to pay | 4 | 40k Typeform payers despite price rises |
| Competition (10) | free alternatives | 2 | Google Forms free (R5) |
| | competitor density | 2 | 10+, strong leaders (R5) |
| | differentiation | 2.5 | Doc-style UX: real but copyable |
| Risk (10) | legal / regulatory | 3 | GDPR processor duties, VAT MOSS |
| | platform dependency | 4 | Owns product and badge channel |
| | market risk | 4 | Durable recurring need |
| Fit (5) | skills | 4 | Build yes, selling unproven |
| | assets | 1.5 | No audience stated |
| | interest | 3 | Not stated |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 3.50 | 17.50 |
| Feasibility (20) | 4.17 | 16.67 |
| Time to revenue (15) | 3.33 | 10.00 |
| Demand (15) | 4.17 | 12.50 |
| Competition (10) | 2.17 | 4.33 |
| Risk (10) | 3.67 | 7.33 |
| Fit (5) | 2.83 | 2.83 |
| **Raw total** | | **71.2** |
| **Rules applied** | R5 coherence (no score change) | |
| **Final score** | | **71 / 100** |

## 13. Sources

34 sources from 28 domains: 13 primary, 14 secondary, 7 tertiary. All published on or before 2020-06-01; accessed 2026-11-11. Full list with tiers and dates in `report-data.json` and `report.html`.
