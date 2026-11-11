<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 41/100
> **Invoicing + URSSAF app for French micro-entrepreneurs**
>
> `████░░░░░░` 41 / 100 · confidence high, 48 sources
>
> - ❌ Abby already sells invoicing **plus URSSAF filing at 9 EUR HT/month** and claims 150,000+ users ([pricing page](https://abby.fr/tarifs/?aedrop=bot_detected))
> - ❌ Indy (86 MEUR raised), Tiime, Shine and Qonto give invoicing and e-invoicing away for 0 EUR ([source](https://ma-facture-electronique.org/logiciels/auto-entrepreneur/))
> - ✅ Huge, growing need: 1.66M active micro-entrepreneurs and a mandatory e-invoicing switch in 2027-09
>
> **Could be saved:** 79 EUR done-for-you e-invoicing switch service → 61/100 (doable)
> **Cheapest test:** 7-day pre-sale of the 79 EUR switch service in 3 communities; fewer than 3 paid → stop
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 41/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2041%2F100-red)

# Invoicing app for French micro-entrepreneurs with VAT and URSSAF declarations: kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 41/100 (raw 50.5) · R7 unprofitable model −10, R6 cap 49 |
| **Confidence** | high: 16 sourced sub-scores of 21, 48 sources (20 primary). Several facts come from search snippets. |
| **Countries** | FR |
| **Assumptions** | Budget EUR 1,000, 10 h/week, goal side income, edge "developer". Assumed: no audience, no validation, CPC ~3 EUR, connect to an existing PA instead of registering as one. |

## 0. Executive summary

**Answer:** **NO-GO**. Abby already sells exactly this (invoicing plus URSSAF filing) at **9 EUR/month** to 150,000+ users, and free tools cover the rest. Without a channel, each paid customer costs about 460 EUR and brings in about 100 EUR.

**Key findings**
1. **Abby already sells this at 9 EUR**: Abby Start includes URSSAF declaration and payment at 9 EUR HT/month. Its free plan covers invoicing and VAT-threshold alerts. ([source](https://abby.fr/tarifs/?aedrop=bot_detected))
2. **Funded incumbents give e-invoicing away**: Indy has raised **86 MEUR** and offers e-invoicing for free as a registered plateforme agréée (PA). Tiime, Shine and Qonto also invoice for 0 EUR. ([source](https://ma-facture-electronique.org/logiciels/auto-entrepreneur/))
3. **No channel, and CAC is far above LTV**: incumbents and comparison sites hold SEO. CAC is about **460 EUR** against an LTV of about **100 EUR** (estimate). ([source](https://userpilot.com/blog/free-trial-conversion-rate/))

**Steelman:** The market is large and growing: **1.66M** active micro-entrepreneurs, record creations, and a 2027-09 e-invoicing mandate that forces all of them to change tools. But incumbents registered as PAs early and made the switch **free**. The demand exists; the margin does not.

**Recommendation:** Do not build the app. Test a 79 EUR done-for-you e-invoicing switch service for 7 days, and stop if fewer than 3 people pre-pay.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Nobody finds the app: SEO and the big Facebook groups belong to Abby, Indy and comparison sites, and paid clicks cost more than a user ever pays | no_distribution | H | Fewer than 100 visitors and 0 paid users in 30 days |
| 2 | Visitors pick a free tier over a 9 EUR unknown app that does the same job | free_alternative | H | Signup-to-paid below 2%; "why not free?" in 20 conversations |
| 3 | URSSAF API approval or the PA partner contract drags on | legal_platform_risk | M | No sandbox access 30 days after applying; no written PA quote |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a done-for-you e-invoicing switch (79 EUR one-off) before 2027-09, built on a free PA tool | ltv_cac, pricing_power | 61/100 (estimate) | doable | 1 week to test, 1 h per client | < 100 EUR | Learn the PA onboarding of 1–2 free tools; post in communities |
| 2 | Build for one trade the free tools serve poorly (quotes with deposits and progress invoices) | differentiation, channel_readiness | 57/100 (estimate) | hard | 3 months | < 1,000 EUR | Access to a niche community; a written PA API quote |

## 2. Next step: 7-day test

**Cheapest test:** a 7-day pre-sale of the 79 EUR e-invoicing switch service.

| Day | Step | Verify |
|-----|------|--------|
| 1 | One-page offer, "Ready for e-invoicing in 1 hour, 79 EUR", with a Stripe payment link | Page live, payment link tested |
| 2–3 | Post a useful 2027 e-invoicing checklist in 3 micro-entrepreneur communities (where rules allow) | 100+ visitors by day 5 |
| 2–6 | Send 40 direct messages asking how people plan the 2027 switch | 10+ replies by day 6 |
| 7 | Count paid pre-sales and log objections | 3+ paid pre-sales |

**Stop if:**
- fewer than 100 visitors by day 5;
- fewer than 10 replies to 40 messages by day 6;
- fewer than 3 paid pre-sales at 79 EUR by day 7.

## 3. Source

"A simple invoicing app for French freelancers (auto-entrepreneurs) that handles VAT and URSSAF declarations, 9 EUR a month. Launch country FR, budget 1,000 EUR, 10 hours a week, goal side income, edge: I am a developer."

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | Abby, Indy, Tiime, Shine, Qonto and Henrri invoice for 0 EUR. Abby's free plan adds URSSAF estimates (2026-11). | [Abby](https://abby.fr/tarifs/?aedrop=bot_detected) |
| 2 | Strong direct competitor | **hit** | Indy: 86 MEUR raised, 700k users claimed. Abby: 604 Capterra reviews. | [JdE](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853) |
| 3 | Graveyard | clear | Found consolidation only (Qonto bought Regate in 2024; Henrri MBO), no closures | [Siècle Digital](https://siecledigital.fr/2024/03/08/la-fintech-francaise-qonto-rachete-regate/) |
| 4 | No distribution channel | **hit** | Incumbents and comparison sites hold SEO. The 2 largest Facebook groups (61k and 54k) are run by competitors. | [Tool-Advisor](https://tool-advisor.fr/blog/groupe-facebook-entrepreneur/) |
| 5 | Costs eat the margin | clear | Stripe takes about 0.45 EUR and PA fees add 0.20–0.50 EUR per invoice: gross margin about 84% (estimate) | [Stripe](https://stripe.com/fr/pricing) |
| 6 | Weak demand | clear | Record 758,600 micro-entreprise creations in 2025 (+6%) | [INSEE](https://www.insee.fr/fr/statistiques/fichier/8721354/IP2092.pdf) |
| 7 | Legal / platform risk | **hit** | From 2027-09, B2B e-invoices must go through a PA. URSSAF filing needs restricted API access and user mandates. | [impots.gouv](https://www.impots.gouv.fr/node/25455) |
| 8 | Saturated wave (2 launches, 2025-11 to 2026-11: fiftie, Facturons) | clear | Both have almost no traction | [Product Hunt](https://www.producthunt.com/products/fiftie-invoice-in-12s/launches/fiftie) |

**Primary kill shot:** free alternative. The job is already done for 0 EUR, or for 9 EUR by Abby.

## 6. Market

- **Target customer:** service micro-entrepreneurs (BNC/BIC services) under the VAT franchise who invoice businesses.
- **Pain** and how they solve it today: compliant invoices, URSSAF declarations and the 2027 e-invoicing switch. Today they use free tiers (Indy, Abby, Tiime, Shine), bank invoicing (Qonto), Excel, and the free URSSAF site.
- **Demand signals:** 3.031M URSSAF accounts and 1.66M economically active at end-2025, averaging 5,156 EUR revenue per quarter ([TPE Actu, 2026](https://tpeactu.fr/2026/07/24/auto-entrepreneurs-55-pourcent-chiffre-affaires-fin-2025/)).
- **Trend:** rising. Creations grew +7% in 2024 and +6% in 2025 ([INSEE, 2026](https://www.insee.fr/fr/statistiques/fichier/8721354/IP2092.pdf)) and are still rising in 2026 ([INSEE](https://www.insee.fr/fr/statistiques/fichier/version-html/9025111/IR170_CreaE_juin26.pdf)).

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | 179 MEUR/year | estimate | 1.66M active × 108 EUR/year |
| SAM | 93 MEUR/year | estimate | 52% service sellers (assumed) = 863k × 108 |
| SOM (year 1) | 93 kEUR/year | estimate | 0.1% of SAM ≈ 860 users; optimistic without a channel |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| All businesses must be able to receive e-invoices via a PA | 2026-09 | [impots.gouv](https://www.impots.gouv.fr/node/25455) |
| Micro-entreprises must issue e-invoices and e-report | 2027-09 | [JDN](https://www.journaldunet.com/fintech/1557199-facture-electronique-ce-que-les-auto-entrepreneurs-devront-vraiment-faire-en-septembre-2027/) |
| Cut of the VAT franchise threshold to 25,000 EUR dropped (MPs voted 239–0) | 2025-11 | [Legifiscal](https://www.legifiscal.fr/actualites-fiscales/4141-vote-unanime-deputes-abandon-seuil-franchise-tva-25000.html) |
| Abby registered as a PA | 2026-01 | [Abby](https://abby.fr/guide/facturation-electronique/facture-electronique-septembre-2026) |
| Indy bought Coover's invoicing software ahead of the reform | 2025-08 | [FrenchWeb](https://www.frenchweb.fr/indy-soffre-la-facturation-de-coover-pour-accelerer-avant-la-reforme-de-2026/456697) |

The mandate is a real trigger. But incumbents registered as PAs in 2025–2026 and made it free, so the window has closed.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Newly registered service micro-entrepreneur under the VAT franchise who invoices B2B clients |
| **Where to reach them** | FB "La communauté des auto-entrepreneurs" (~61k), FB "Entraide auto/micro-entrepreneurs" (~54k), Malt, r/vosfinances, Bpifrance Création |
| **Pays for today** | Mostly 0 EUR. Some pay Abby Start (9 EUR HT) or Freebe (12.50 EUR HT/month) |
| **Budget** | About 1,720 EUR revenue per month, so 9 EUR is about 0.5% of it, but buyers anchor at 0 |
| **Trigger** | First invoice, first URSSAF declaration, or the 2027-09 e-invoicing obligation |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Invoicing + URSSAF SaaS at 9 EUR/month (the idea) | Micro-entrepreneur | 2–3 months + approvals |
| 2 | Done-for-you e-invoicing switch, 79 EUR | Micro-entrepreneur facing 2027-09 | 1 week to test |
| 3 | Vertical invoicing for one trade | Artisan micro-entrepreneur | 3 months |

**Best option:** #2. It sells help with the deadline, not a thirteenth invoicing app, and it can be tested this week.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| Abby | FR | Invoicing, URSSAF/VAT filing, PA | 0–33 EUR HT/month (2026-11) | 4 | None: it already sells this at 9 EUR |
| Indy | FR | Accounting, invoicing, PA | 0–15 EUR/month (2026-10) | 5 | Free plan has no URSSAF filing |
| Tiime | FR | Invoicing and accounting, PA | 0–9.99 EUR/month (2026-10) | 4 | None visible |
| Shine Facture | FR | Neobank invoicing, PA | 0 EUR (2026-10) | 4 | Pushes its bank account |
| Qonto | FR | Neobank invoicing, PA | 0–39 EUR/month (2026-11) | 5 | Bank add-on |
| Freebe | FR | Freelancer invoicing | 12.50–15 EUR/month (2026-11) | 3 | Pricier |
| Henrri | FR | Free invoicing | 0 EUR (2026-11) | 4 | No URSSAF filing |
| fiftie | FR | Indie invoicing | 0–5.90 EUR/month (2026-02) | 1 | Look-alike, cheaper |

- **Free alternatives:** Abby, Indy, Tiime, Shine, Qonto and Henrri. The URSSAF site also files declarations for free.
- **Edge:** none specific. Development skill builds the product but does not win customers.
- **First 10 customers would come from:** community posts and direct messages. Paid search is too expensive at this LTV.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | 9 EUR/month | estimate | Founder's price; equals Abby Start |
| Variable cost per unit | 1.45 EUR/month | estimate | Stripe 0.45 + PA 5 invoices × 0.20 |
| Gross margin % | 84% | estimate | (9 − 1.45) ÷ 9 |
| Churn / lifetime | 7.5%/month · 13.3 months | estimate | Midpoint of 6.8% and 8.9% for 0–10 USD ARPA ([TechCrunch](https://techcrunch.com/2022/04/20/study-up-on-churn-rate-basics-to-set-customer-and-revenue-benchmarks/)) |
| Conversion rate | 0.65% | estimate | 3.5% visit→trial × 18.5% trial→paid |
| CAC | 460 EUR | estimate | Assumed CPC 3 EUR ÷ 0.0065 |
| LTV | 100 EUR | estimate | 9 × 0.84 × 13.3 |
| LTV : CAC | 0.22 | estimate | 100 ÷ 460 |
| Payback (months) | 61 | estimate | 460 ÷ 7.56 |
| Fixed costs / month | 20 EUR | estimate | VPS, email, domain |
| Break-even (customers) | 3 (135 for 1,000 EUR/month net) | estimate | 20 ÷ 7.56; (1,000 + 20) ÷ 7.56 |
| Time to first revenue (weeks) | 10 | estimate | 8 weeks build + 2 weeks; URSSAF approval may add more |

| Scenario (month 12) | Customers | Revenue | Costs | Margin | Note |
|----------|-----------|---------|-------|--------|------|
| Pessimistic | 5 | 45 EUR | 27 EUR | 18 EUR | Organic only; visitors choose free tiers |
| Base | 30 | 270 EUR | 64 EUR | 206 EUR | 1,000 EUR in ads, 7.5% churn |
| Optimistic | 120 | 1,080 EUR | 194 EUR | 886 EUR | An SEO page ranks; still short of 1,000 EUR net |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 6–10 weeks at 10 h/week for invoicing; filing depends on URSSAF API approval |
| Skills missing | French tax and e-invoicing rules, SaaS marketing |
| Key dependencies | A PA partner API (priced on request) and the URSSAF Tierce Déclaration API (restricted access) |
| Legal / compliance | PA routing from 2027-09, user mandates for filing, 10-year invoice retention, GDPR |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | URSSAF API access not granted, or slow | M | H | Apply before building | [data.gouv](https://www.data.gouv.fr/dataservices/api-tierce-declaration-auto-entrepreneur) |
| 2 | PA API quoted above budget | M | H | Get 2 written quotes first | [MFE](https://ma-facture-electronique.org/plateforme-agreee/prix-tarifs/) |
| 3 | Liability for a wrong filing | M | M | Terms of use plus user confirmation | [Légifrance](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000032364676) |
| 4 | High churn as micro-businesses stop trading (28% survive 5 years) | H | M | Annual plans | [INSEE](https://www.insee.fr/fr/statistiques/9022618) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 4 | About 84% after Stripe and PA fees (estimate) |
| | LTV : CAC | 1 | About 0.2, with no organic channel (R4) |
| | pricing power | 1 | Free tiers; Abby at the same 9 EUR (R4) |
| Feasibility (20) | build effort | 2.5 | 6–10 weeks plus approvals |
| | skills match | 3.5 | Developer; missing tax and marketing skills |
| | capital needed | 3 | PA API priced on request |
| Time to revenue (15) | time to MVP | 2.5 | About 8–10 weeks |
| | sales cycle | 4 | Self-serve, same day |
| | channel readiness | 1.5 | No audience; channels held by incumbents |
| Demand (15) | search demand | 4.5 | 1.66M active micro-entrepreneurs |
| | trend | 4 | Record creations, +6%/year |
| | willingness to pay | 2 | Anchored at 0 EUR |
| Competition (10) | free alternatives | 1 | Free tools do the whole job (R1) |
| | competitor density | 1 | 12+ tools, 149 PAs |
| | differentiation | 1 | Same job, same price (R1) |
| Risk (10) | legal / regulatory | 2 | PA mandate, URSSAF mandates |
| | platform dependency | 2 | One PA partner plus URSSAF API |
| | market risk | 5 | Legal, recurring obligation |
| Fit (5) | skills | 3.5 | Builder, no domain track record |
| | assets | 1 | No audience |
| | interest | 1.5 | Side income |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 2.0 | 10.0 |
| Feasibility (20) | 3.0 | 12.0 |
| Time to revenue (15) | 2.67 | 8.0 |
| Demand (15) | 3.5 | 10.5 |
| Competition (10) | 1.0 | 2.0 |
| Risk (10) | 3.0 | 6.0 |
| Fit (5) | 2.0 | 2.0 |
| **Raw total** | | **50.5** |
| **Rules applied** | R1 competition ≤ 1.5 · R4 pricing power 1.5→1, profit 2.0 · R7 51 − 10 = 41 · R6 cap 49 (no change) | |
| **Final score** | | **41 / 100** |

## 13. Sources

48 sources from 33 domains: 20 primary, 13 secondary, 15 tertiary. The full list, with tiers and what each source supports, is in `report.html` and `report-data.json`. Key sources:

1. [Abby, pricing page](https://abby.fr/tarifs/?aedrop=bot_detected): plans and users. Primary, accessed 2026-11-11.
2. [INSEE Première 2092](https://www.insee.fr/fr/statistiques/fichier/8721354/IP2092.pdf): 758,600 creations in 2025. Primary, published 2026-01.
3. [impots.gouv.fr, plateformes agréées](https://www.impots.gouv.fr/node/25455): PA obligation. Primary.
4. [data.gouv.fr, URSSAF API Tierce Déclaration](https://www.data.gouv.fr/dataservices/api-tierce-declaration-auto-entrepreneur): restricted API, mandates. Primary.
5. [Stripe France pricing](https://stripe.com/fr/pricing): payment fees. Primary.
6. [INSEE Première 2118](https://www.insee.fr/fr/statistiques/9022618): 28% five-year survival. Primary, published 2026-07.
7. [Le Journal des Entreprises, Indy raises 40 MEUR](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853): 86 MEUR total. Secondary, published 2023.
8. [Ma Facture Électronique, software for micro-entrepreneurs](https://ma-facture-electronique.org/logiciels/auto-entrepreneur/): free tiers, PA list. Tertiary, published 2026-10.
