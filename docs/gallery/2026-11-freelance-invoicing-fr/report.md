<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## ☠️ NO-GO · 49/100
> **€9 invoicing + URSSAF app for auto-entrepreneurs**
>
> `█████░░░░░` 49 / 100 · confidence high, 30 sources
>
> - ❌ Free plans already do the whole job: Abby, Indy, Henrri and Qonto offer unlimited free invoicing with e-invoicing ([Abby](https://abby.fr/pour-qui/auto-entreprise))
> - ❌ Funded incumbents own the segment: Indy has raised €86M and passed 100,000 users ([Le Journal des Entreprises](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853))
> - ✅ A big, growing market with a legal obligation: 3.186M registered micro-entrepreneurs, +204,000 in a year
>
> **Could be saved:** sell e-invoicing integration to small French software publishers → 60/100 (doable)
> **Cheapest test:** 30 cold emails offering fixed-price Factur-X + PA integration; 2+ discovery calls in 7 days or stop
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: NO-GO 49/100](https://img.shields.io/badge/kill--my--idea-NO--GO%2049%2F100-red)

# Simple invoicing + VAT/URSSAF app for French auto-entrepreneurs — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | NO-GO · 49/100 (raw 51.7) · capped at 49: no channel and LTV:CAC below 1 (R6) |
| **Confidence** | high: 14 sourced sub-scores of 21, 30 sources (10 primary). Most prices come from vendor or comparison pages. |
| **Countries** | FR |
| **Assumptions** | Budget €1,000, 10 h/week, goal side income, edge developer (from the input). Price read as €9/month excl. VAT; target = service micro-entrepreneurs (BNC); no existing audience; questions skipped at the user's request |

## 0. Executive summary

**Answer:** NO-GO. **Free** plans from funded incumbents (Abby, Indy, Henrri, Qonto) already invoice and e-invoice, and URSSAF's own app files for free. A solo €9 clone has no channel and an LTV:CAC near **0.6**. Sell your developer skill as e-invoicing integration instead.

**Key findings**
1. **Free tools already do the whole job**: Abby, Indy, Henrri and Qonto offer **free unlimited** invoicing with e-invoicing; URSSAF's app files declarations free ([Abby](https://abby.fr/pour-qui/auto-entreprise), [Qonto](https://qonto.com/fr/invoicing/freelance))
2. **Funded incumbents own the segment**: Indy raised **€86M** and passed 100,000 users in 2024; Abby has raised over €4M since 2023 ([LJDE](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853), [Indy](https://indy.fr/wp-content/uploads/2024-07-04-Indy-passe-les-100-000-utilisateurs.pdf))
3. **Compliance raises the floor**: from **Sept 2027** micro-entrepreneurs issue invoices through an approved platform (PA); becoming one requires an ISO 27001 certificate ([demarche.numerique.gouv.fr](https://demarche.numerique.gouv.fr/commencer/immatpdp))

**Steelman:** 3.19M micro-entrepreneurs, +204k a year, and a reform that forces every one of them to change tools: a big, growing market in motion. True, but the switching wave flows to incumbents that are already **free and compliant**, so the market size does not reach a new €9 app.

**Recommendation:** Do not build the app. Spend 7 days testing a fixed-price e-invoicing integration offer for small French software publishers.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Nobody finds the app: Abby/Indy guides fill page 1 and ads cost more than a customer is worth | no_distribution | H | Fewer than 300 visitors and 10 sign-ups in 30 days after launch |
| 2 | Trial users compare with free Abby/Indy plans and never pay €9 | free_alternative | H | Trial-to-paid below 3% on the first 50 sign-ups |
| 3 | PA partner costs or URSSAF API accreditation delay the 2027-compliant version | legal_platform_risk | M | No PA quote under €1 per customer-month within 30 days |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell fixed-price e-invoicing integration (Factur-X + PA connection) to small French software publishers before Sept 2027 | free_alternative, no_distribution, ltv_cac (€1,500+ per deal, outbound CAC) | 60/100 (estimate) | doable | 1 week to package | €0–100 | A public Factur-X demo repo, LinkedIn/Malt profile, 30 cold emails |
| 2 | Niche app: invoicing + URSSAF *avance immédiate* (API Tiers de prestation) for home-service micro-entrepreneurs | differentiation, channel via trade associations | 54/100 (estimate) | hard | 3–4 months | €300–1,000 | URSSAF API habilitation, a PA partner, an association partner |

## 2. Next step: 7-day test (rescue path 1)

**Cheapest test:** 30 cold emails offering fixed-price Factur-X + PA integration to small French software publishers.

| Day | Step | Verify |
|-----|------|--------|
| 1 | One-page offer: Factur-X + PA connection, fixed €1,500 | Page live with 1 clear price |
| 2 | Publish a small open-source Factur-X generation demo | Repo public with a working sample invoice |
| 3–4 | List 30 small French SaaS/ERP publishers serving SMEs; send 30 personal emails | 30 emails sent |
| 5–6 | Follow up once; post the offer on LinkedIn and Malt | 5+ replies |
| 7 | Count discovery calls | 2+ calls booked, else stop |

**Stop if:** fewer than 2 discovery calls from 30 emails by day 7 · no signed quote at €1,000+ by day 30 · (if you build the app anyway) fewer than 3 paid users out of 100 sign-ups by week 12.

## 3. Source

> A simple invoicing app for French freelancers (auto-entrepreneurs) that handles VAT and URSSAF declarations, 9 EUR a month. Launch country FR, budget 1,000 EUR, 10 hours a week, goal side income, edge: I am a developer. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | Abby, Indy, Henrri, Qonto: free unlimited invoicing with e-invoicing; official URSSAF app declares and pays free | [Abby](https://abby.fr/pour-qui/auto-entreprise), [Swim](https://www.swim.legal/blog/application-auto-entrepreneur-urssaf-guide-declaration-cotisations) |
| 2 | Strong direct competitor | **hit** | Indy €86M raised (2023), 100k users (2024-07); Abby €3M round (2025-09) | [LJDE](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853) |
| 3 | Graveyard | clear | Searched closures; found consolidation (Henrri acquiring, 2026), no notable shutdown | [LJDE](https://www.lejournaldesentreprises.com/article/apres-le-rachat-des-parts-dardian-rivalis-henrri-signe-sa-premiere-croissance-externe-2145828) |
| 4 | No distribution channel | **hit** | No audience; SEO filled by vendor guides; France CPC €0.50–3.00 (2025) → CAC ~€250 vs LTV €144 (estimate) | [Copeps](https://copeps.fr/actualites/adwords-clic-comptabilise/) |
| 5 | Costs eat the margin | clear | ~€1.8 variable cost on €9 → ~80% gross margin (estimate) | — |
| 6 | Weak or falling demand | clear | 3.186M registered micro-entrepreneurs end June 2025, +204,000 in 12 months | [Optigest+](https://optigestplus.org/2026/05/10/auto-entrepreneur-en-france-le-bilan-2025-en-chiffres-statistiques-ca-secteurs/) |
| 7 | Legal / platform risk | **hit** | Sept 2027: invoices through an approved platform (ISO 27001 required to become one); URSSAF third-party filing API is restricted | [Immat PA](https://demarche.numerique.gouv.fr/commencer/immatpdp), [data.gouv](https://www.data.gouv.fr/dataservices/api-tierce-declaration-auto-entrepreneur) |
| 8 | Saturated wave (3 look-alikes, 2025-11 to 2026-11: fiftie, FactuDevis, Invoicer) | clear | Fewer than 10 confirmed in 12 months | [Product Hunt](https://www.producthunt.com/p/fiftie-invoice-in-12s/fiftie) |

**Primary kill shot:** free alternative.

## 6. Market

- **Target customer:** French service micro-entrepreneurs (BNC), solo, first 2 years.
- **Pain:** compliant invoices, monthly/quarterly URSSAF declaration, VAT threshold tracking, now e-invoicing. Today: free Abby/Indy/Henrri/Qonto plus the free URSSAF app; some pay Freebe (€11.90 HT) or Indy (€9–12 HT) for automatic filing.
- **Demand signals:** 3.186M registered, only 49.8% economically active in Q2 2025 ([TPE Actu](https://tpeactu.fr/2026/01/29/auto-entrepreneurs-chiffre-affaires-urssaf-2025/)).
- **Trend:** rising, about +7%/year in registrations.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | €344M/year | estimate | 3.186M × €9 × 12 |
| SAM | €172M/year | estimate | 49.8% active = 1.59M × €108 |
| SOM (year 1) | €34k/year | estimate | 0.02% of 1.59M ≈ 318 customers × €108 (below 0.1% because free plans cap conversion) |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| DGFiP published the first list of approved e-invoicing platforms | 2026-01 | [impots.gouv.fr](https://impots.gouv.fr/actualite/facturation-electronique-publication-de-la-liste-des-plateformes-agreees) |
| Micro-entrepreneurs must receive e-invoices; issuance from Sept 2027 | 2026-09 | [Stripe](https://stripe.com/us/resources/more/invoicing-as-a-freelancer-france) |
| Registered micro-entrepreneurs reach 3.186M (+204k) | 2025-06 | [Optigest+](https://optigestplus.org/2026/05/10/auto-entrepreneur-en-france-le-bilan-2025-en-chiffres-statistiques-ca-secteurs/) |
| VAT franchise cut to €37,500 rejected by deputies | 2025-11 | [Legifiscal](https://www.legifiscal.fr/actualites-fiscales/4339-plf-2026-rejet-deputes-hausse-seuil-franchise-base-tva.html) |

The reform opened a switching window, but incumbents filled it with **free compliant** plans before Sept 2026.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Service micro-entrepreneurs (BNC), first 2 years, solo, under the €37,500 VAT franchise |
| **Where to reach them** | Facebook auto-entrepreneur groups, Malt community, Reddit r/vosfinances, URSSAF/CCI creation workshops, coworkings |
| **Pays for today** | €0 (free plans) or €9–12/month for automatic URSSAF filing |
| **Budget** | €0–12/month |
| **Trigger** | First client invoice, first URSSAF deadline, Sept 2026 e-invoice reception rule |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | €9/month app for all micro-entrepreneurs | Micro-entrepreneur | 2–3 months |
| 2 | **Fixed-price e-invoicing integration for small publishers** | Software publisher | 1 week to offer |
| 3 | Avance-immédiate invoicing for home services | Home-service micro-entrepreneur | 3–4 months |

**Best option:** #2 — it sells the reform to buyers with budget, through a channel (outbound) you can run alone.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| Abby | FR | Micro-entrepreneur invoicing, declarations | €0 / 9.90–39.90 HT/month (2026-03, [Codeur](https://www.codeur.com/comparatif/logiciel-facturation/abby)) | 4 | Free plan covers the job |
| Indy | FR | Invoicing + accounting | €0 / 9 / 12 HT/month (2026-06, [Selectra](https://selectra.info/finance/guides/banque-pro/logiciel-facturation/auto-entrepreneur)) | 5 | URSSAF filing on paid tier |
| Freebe | FR | Micro-entrepreneur tool, URSSAF filing | €11.90 HT/month (date unknown, [review](https://www.dixmilleheures.fr/avis/freebe)) | 3 | Paid only |
| Henrri | FR | Free invoicing, PA via Pennylane | €0 (2026, [LFdN](https://www.lafabriquedunet.fr/logiciels/gestion/facturation/facturation-usage-gratuit)) | 3 | Less micro-specific |
| Qonto invoicing | FR | Free invoicing, with or without account | €0 (2026-11, [Qonto](https://qonto.com/fr/invoicing/freelance)) | 5 | Bank-led |
| fiftie | FR | "Invoice in 12s" | €5.90/month (2026, [PH](https://www.producthunt.com/p/fiftie-invoice-in-12s/fiftie)) | 1 | Same pitch, cheaper |
| FactuDevis | FR | Free invoicing, Factur-X | €0 ([Capterra](https://www.capterra.co.uk/software/1095729/FactuDevis)) | 1 | Look-alike |
| URSSAF app | FR | Official declaration and payment | €0 ([Swim](https://www.swim.legal/blog/application-auto-entrepreneur-urssaf-guide-declaration-cotisations)) | 5 | No invoicing |

- **Free alternatives:** Abby, Indy, Henrri, Qonto, FactuDevis, the URSSAF app.
- **Edge:** "I am a developer" is not a market edge here: every competitor has developers, and Indy has €86M.
- **First 10 customers** would come from personal network and forums, slowly; no scalable channel identified.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | €9/month | sourced | User's price; matches Indy Plus €9 HT ([Indy](https://www.indy.fr/guide/facturation/logiciel/gratuit/)) |
| Variable cost per unit | €1.80/month | estimate | Stripe 1.5% + €0.25 = 0.39 + PA fee ~1.00 (assumed) + hosting/support 0.41 |
| Gross margin % | 80% | estimate | (9 − 1.8) / 9 |
| Churn / lifetime | 5%/month · 20 months | estimate | Half of registered micro-entrepreneurs inactive; 1 / 0.05 |
| Conversion rate | 1% | estimate | Paid search next to free plans |
| CAC | €250 | estimate | CPC ~€2.50 / 1% |
| LTV | €144 | estimate | 9 × 0.80 × 20 |
| LTV : CAC | 0.58 | estimate | 144 / 250 |
| Payback (months) | 34.7 | estimate | 250 / 7.20 |
| Fixed costs / month | €80 | estimate | Hosting 20 + tools 10 + PA base fee 50 (assumed) |
| Break-even (customers) | 12 | estimate | 80 / 7.20 |
| Time to first revenue | 10 weeks | estimate | 6–8 weeks MVP at 10 h/week + 2 weeks |

| Scenario (month 12) | Customers | Revenue / month | Costs / month | Margin | Note |
|----------|-----------|-----------------|---------------|--------|------|
| Pessimistic | 5 | €45 | €89 | −€44 | Free plans absorb trials |
| Base | 40 | €360 | €152 | €208 | ~€10k of CAC if acquired by ads |
| Optimistic | 150 | €1,350 | €350 | €1,000 | Needs organic reach that beats Abby/Indy SEO |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Invoicing MVP 6–8 weeks at 10 h/week; Factur-X + PA connection more |
| Skills missing | French tax/URSSAF rules, URSSAF third-party accreditation |
| Key dependencies | An approved platform (PA) partner; URSSAF API access |
| Legal / compliance | E-invoicing via a PA from Sept 2027; liability for filing errors |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Free plans block conversion | H | H | Do not compete on generic invoicing | [Abby](https://abby.fr/pour-qui/auto-entreprise) |
| 2 | PA partner cost or terms change | M | H | Get 2 PA quotes before building | [impots.gouv.fr](https://impots.gouv.fr/actualite/facturation-electronique-publication-de-la-liste-des-plateformes-agreees) |
| 3 | Liability for wrong filings | M | M | Pre-fill only; user confirms | [data.gouv](https://www.data.gouv.fr/dataservices/api-tierce-declaration-auto-entrepreneur) |
| 4 | VAT threshold rules change again | M | L | Thresholds as config | [Legifiscal](https://www.legifiscal.fr/actualites-fiscales/4339-plf-2026-rejet-deputes-hausse-seuil-franchise-base-tva.html) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit (25) | gross margin | 3.5 | ~80%; lowered 4 → 3.5 by R4 |
| | LTV : CAC | 1 | 144 vs ~250 = 0.58 |
| | pricing power | 1.5 | Free plans anchor price at €0 |
| Feasibility (20) | build effort | 3 | 1–2 months MVP |
| | skills match | 3 | Dev, but no URSSAF accreditation |
| | capital needed | 3.5 | Fits €1,000 if renting a PA |
| Time to revenue (15) | time to MVP | 2.5 | 6–8 weeks |
| | sales cycle | 4 | Self-serve |
| | channel readiness | 1.5 | No audience (R5) |
| Demand (15) | search demand | 4.5 | 3.186M registered |
| | trend | 4 | +204k/year |
| | willingness to pay | 2.5 | Core job free; filing is the upsell |
| Competition (10) | free alternatives | 1 | Whole job free (R1) |
| | competitor density | 1 | 20+ tools |
| | differentiation | 1.5 | "Simple" = better UX (R1) |
| Risk (10) | legal / regulatory | 2 | PA mandatory from 2027 |
| | platform dependency | 2 | PA + restricted URSSAF API |
| | market risk | 4.5 | Durable legal obligation |
| Fit (5) | skills | 3 | Software yes, tax no |
| | assets | 1.5 | None stated |
| | interest | 1.5 | Side income goal |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit (25) | 2.00 | 10.0 |
| Feasibility (20) | 3.17 | 12.7 |
| Time to revenue (15) | 2.67 | 8.0 |
| Demand (15) | 3.67 | 11.0 |
| Competition (10) | 1.17 | 2.3 |
| Risk (10) | 2.83 | 5.7 |
| Fit (5) | 2.00 | 2.0 |
| **Raw total** | | **51.7** |
| **Rules applied** | R1 (competition → 1.0), R4 (profit → 2.0), R5 (channel, legal coherence), R6 (52 capped at 49) | |
| **Final score** | | **49 / 100** |

## 13. Sources

30 sources from 25 domains: 10 primary, 12 secondary, 8 tertiary. All accessed 2026-11-11.

1. [Abby, auto-entrepreneur invoicing](https://abby.fr/pour-qui/auto-entreprise) — free plan — primary
2. [Codeur.com, Abby pricing](https://www.codeur.com/comparatif/logiciel-facturation/abby) — Abby prices — secondary — 2026-03
3. [Indy, free invoicing guide](https://www.indy.fr/guide/facturation/logiciel/gratuit/) — Indy free invoicing — primary
4. [Selectra, free invoicing tools](https://selectra.info/finance/guides/banque-pro/logiciel-facturation/auto-entrepreneur) — Indy tiers — secondary — 2026-06
5. [Dix mille heures, Freebe review](https://www.dixmilleheures.fr/avis/freebe) — Freebe price — tertiary
6. [Freebe help, URSSAF declaration](https://freebe.helpscoutdocs.com/collection/37-declaration-urssaf) — URSSAF filing — primary
7. [Qonto, freelance invoicing](https://qonto.com/fr/invoicing/freelance) — free invoicing — primary
8. [DGFiP, list of approved platforms](https://impots.gouv.fr/actualite/facturation-electronique-publication-de-la-liste-des-plateformes-agreees) — PA list — primary — 2026-01
9. [Stripe, freelance invoicing in France](https://stripe.com/us/resources/more/invoicing-as-a-freelancer-france) — e-invoicing dates — secondary
10. [PA registration procedure](https://demarche.numerique.gouv.fr/commencer/immatpdp) — ISO 27001 — primary
11. [Swim.legal, PA data security](https://www.swim.legal/blog/plateforme-agreee-securite-donnees) — PA security rules — tertiary
12. [data.gouv.fr, API Tierce Déclaration](https://www.data.gouv.fr/dataservices/api-tierce-declaration-auto-entrepreneur) — restricted API — primary
13. [TPE Actu, URSSAF 2025](https://tpeactu.fr/2026/01/29/auto-entrepreneurs-chiffre-affaires-urssaf-2025/) — 49.8% active — secondary
14. [Optigest+, 2025 in figures](https://optigestplus.org/2026/05/10/auto-entrepreneur-en-france-le-bilan-2025-en-chiffres-statistiques-ca-secteurs/) — 3.186M — tertiary
15. [LJDE, Indy €40M](https://www.lejournaldesentreprises.com/article/indy-leve-40-millions-deuros-pour-accompagner-les-independants-dans-la-gestion-de-leurs-activites-2074853) — €86M total — secondary
16. [Indy, 100,000 users](https://indy.fr/wp-content/uploads/2024-07-04-Indy-passe-les-100-000-utilisateurs.pdf) — users — primary — 2024-07
17. [LJDE, Abby €1.2M](https://www.lejournaldesentreprises.com/article/la-start-up-nanceienne-abby-boucle-une-levee-de-fonds-de-12-million-deuros-2059811) — Abby funding — secondary
18. [Comparateurbanque, Abby €3M](https://www.comparateurbanque.com/?p=164678) — Abby 2025 round — tertiary
19. [La Fabrique du Net, free invoicing after the reform](https://www.lafabriquedunet.fr/logiciels/gestion/facturation/facturation-usage-gratuit) — Henrri free — secondary
20. [Legifiscal, PLF 2026 VAT threshold](https://www.legifiscal.fr/actualites-fiscales/4339-plf-2026-rejet-deputes-hausse-seuil-franchise-base-tva.html) — VAT reform rejected — secondary
21. [Copeps, Google Ads CPC](https://copeps.fr/actualites/adwords-clic-comptabilise/) — France CPC — tertiary
22. [Product Hunt, fiftie](https://www.producthunt.com/p/fiftie-invoice-in-12s/fiftie) — look-alike — primary
23. [Capterra UK, FactuDevis](https://www.capterra.co.uk/software/1095729/FactuDevis) — look-alike — secondary
24. [GetApp, Invoicer](https://www.getapp.com/all-software/a/invoicer-1/) — look-alike — secondary
25. [Swim.legal, URSSAF app](https://www.swim.legal/blog/application-auto-entrepreneur-urssaf-guide-declaration-cotisations) — free official app — tertiary
26. [Dougs, e-invoicing](https://www.dougs.fr/blog/facturation-electronique-auto-entrepreneur/) — timeline — secondary
27. [Independant.io, API Tiers de prestation](https://independant.io/logiciel-api-tiers-prestation-avance-immediate/) — rescue niche — tertiary
28. [LJDE, Rivalis-Henrri acquisition](https://www.lejournaldesentreprises.com/article/apres-le-rachat-des-parts-dardian-rivalis-henrri-signe-sa-premiere-croissance-externe-2145828) — no graveyard — secondary
29. [Indy blog, €40M](https://www.indy.fr/blog/indy-leve-40-millions-euros/) — funding — primary
30. [Tool-advisor, 2026 comparison](https://tool-advisor.fr/logiciel-facturation/comparatif/autoentrepreneur/) — free plans — tertiary
