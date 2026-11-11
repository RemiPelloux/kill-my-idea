<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟡 PIVOT · 51/100
> **AI receptionist for US dental clinics' missed calls**
>
> `█████░░░░░` 51 / 100 · confidence high, 34 sources
>
> - ❌ The ADA endorsed **Weave**, whose package includes an always-on AI receptionist for missed calls (2026-03), so the main channel to dentists is taken ([ADA News](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/))
> - ❌ Variable cost is about $101 on $199, a **49% margin** (estimate). With founder-led sales, LTV:CAC is **1.3** ([Retell pricing](https://www.retellai.com/it/pricing))
> - ✅ Demand is real and rising: "AI receptionist" searches are up 86% year on year, and Flossy reports ~$4M ARR at $500 per location ([FindSkill](https://findskill.ai/learn/ai-receptionist/), [Latka](https://getlatka.com/interviews/flossy-miles-beckett-2026))
>
> **Could be saved:** sell a white-label Open Dental connector to dental marketing agencies → 57/100 (hard)
> **Cheapest test:** call 40 offices after hours to measure the voicemail rate, then pitch 20 dental agencies. Stop if you have fewer than 2 paid pilots by day 7.
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 51/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2051%2F100-yellow)

# AI receptionist for US dental clinics' missed calls: kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill) |
| **Verdict** | PIVOT · 51/100 (raw 51.0) |
| **Confidence** | high: 16 sourced sub-scores of 21, 34 sources (13 primary) |
| **Countries** | US |
| **Assumptions** | Budget $2,000; 10 h/week; goal: side income; edge: developer. The customer is narrowed to independent 1–3 location general practices. Booking means writing into the PMS, starting with Open Dental. Founder time is valued at $50/h. Each clinic sends ~200 calls × 2.5 min a month. |

## 0. Executive summary

**Answer:** **PIVOT, 51/100.** Demand is real and rising. But **20+ funded competitors** and an ADA-endorsed incumbent (Weave) leave a solo developer working 10 h/week with no cheap channel and an LTV:CAC near 1.3.

**Key findings**
1. **The ADA endorsed the incumbent**: ADA Member Advantage endorsed **Weave**, whose package includes an always-on AI receptionist for missed calls (2026-03). ([source](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/))
2. **20+ direct competitors already sell this**: they include Arini (YC W24), Flossy, Dentina, Viva, TensorLinks, SmileDial and DentiVoice. Dentina charges **$299–$399/month** per location. ([source](https://www.cloudtalk.io/blog/dentina-ai-pricing/))
3. **Unit economics barely clear 1**: ~$101 of variable cost on $199 gives a **49% margin**. At 30 sales hours per clinic, LTV:CAC is **1.3** (estimate). ([source](https://www.retellai.com/it/pricing))

**Steelman:** Clinics lose new patients to voicemail and already pay $299–$899/month for fixes, and a developer can build a cheaper agent that runs natively on Open Dental in weeks. The evidence supports both halves (demand and build effort). It does not answer **who sells it**.

**Recommendation:** Do not build the $199 SaaS. Run the 7-day agency test. If 2 dental marketing agencies pay for a white-label pilot, build the Open Dental connector for them. Otherwise, archive the idea.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Could not reach dentists cheaply: cold outreach booked too few demos against Weave and 20 others | no_distribution | H | Fewer than 3 demos from 50 cold contacts in 30 days |
| 2 | Clinics that bought saw no clear edge over Weave or Dentina and churned | strong_competitor | H | Prospects say "we already have Weave" in 5+ of 10 calls |
| 3 | Voice minutes and support ate the $199, so each clinic earned less than the hours it cost | ltv_cac | M | A pilot clinic uses 800+ minutes or 3+ support hours in month 1 |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell a white-label Open Dental voice connector to dental marketing agencies, who resell it to their clinics | no_distribution, channel_readiness: agencies already own the dentist relationship, which lowers CAC | 57/100 (estimate) | hard | 6–8 weeks build + agency deals | ~$1,000 | 2–3 agencies willing to pilot; a HIPAA-ready stack |
| 2 | Done-for-you service: set up and tune an AI receptionist for Open Dental practices, $500 setup + $299/month | pricing_power, ltv_cac: service work wins on trust, which features alone can't do against 20+ products | 56/100 (estimate) | hard | 4–6 weeks + local sales | ~$500 | In-person local sales; more than 10 h/week once clinics need support |

Neither path reaches GO. Both still face Weave and the HIPAA work.

## 2. Next step: 7-day test

**Cheapest test:** Call 40 local dental offices at lunch and after 5 pm to measure the voicemail rate. Then pitch 20 dental marketing agencies a white-label pilot. Stop if you have fewer than 2 paid pilots by day 7.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Call 40 local dental offices at 12:30 and after 17:00; log who reaches voicemail | 10+ of 40 calls unanswered |
| 2 | Write a one-page offer: white-label Open Dental AI receptionist for agencies, pilot at $199/clinic | Page live with a booking link |
| 3–5 | Email 20 dental marketing agencies and 30 Open Dental practices with the voicemail data | 3+ discovery calls booked |
| 6 | Run the calls; demo a scripted voice prototype (no PMS write yet) | 2+ ask for pricing or a pilot |
| 7 | Ask for a paid pilot or a signed LOI | 2+ paid pilots or LOIs at $199+/month |

**Stop if:**
- Fewer than 10 of 40 test calls reach voicemail by day 1: the missed-call pain is too small.
- Fewer than 3 discovery calls from 20 agency emails by day 5: drop the agency path.
- Fewer than 2 paid pilots or signed LOIs at $199+/month by day 7: archive the idea.

## 3. Source

> An AI receptionist that answers missed calls for US dental clinics and books appointments, $199/month. Just go: launch country US, budget $2,000, 10 hours a week, goal side income, edge: I am a developer. Do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | clear | Quo includes 10 free AI calls/month on paid plans and Weave bundles its receptionist. Neither books into the PMS. | [Quo help](https://support.quo.com/hc/en-us/articles/30808928416151-FAQs-about-Sona-the-OpenPhone-AI-Agent) |
| 2 | Strong direct competitor | **hit** | Weave is the ADA-endorsed platform (2026-03) and expanded its AI Receptionist in 2026-07. Flossy reports ~$4M ARR. | [Weave](https://www.getweave.com/press-releases/weave-named-exclusive-patient-engagement-platform-endorsed-for-american-dental-association-members/), [Business Wire](https://www.businesswire.com/news/home/20260714657155/en/) |
| 3 | Graveyard | clear | No dental voice-agent startup that shut down was found. Flossy pivoted *into* this category. Olympia (not dental) wound down at $1.9k MRR. | [HackerNoon](https://hackernoon.com/winding-down-olympia-what-we-built-what-i-learned-and-why) |
| 4 | No distribution channel | **hit** | No audience. First-year gross profit per clinic (~$1,176) is below the founder-led CAC ($1,500, estimate). Dental clicks average $7.85. | [Netpeak](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) |
| 5 | Costs eat the margin | **hit** | Voice AI at ~$0.11/min × 500 min, plus the Open Dental API ($35) and fees, comes to ~$101/month on $199: a 49% margin (estimate). | [Retell](https://www.retellai.com/it/pricing), [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |
| 6 | Weak or falling demand | clear | "AI receptionist" searches are up 86% YoY to ~4,400/month (2026; tertiary keyword data). | [FindSkill](https://findskill.ai/learn/ai-receptionist/) |
| 7 | Legal / platform risk | **hit** | Calls carry PHI, so BAAs are needed across telephony, LLM, TTS and storage. Outbound AI-voice calls fall under the TCPA (FCC, 2024-02). | [FCC](https://WWW.FCC.GOV/document/fcc-makes-ai-generated-voices-robocalls-illegal), [Aira](https://www.getaira.io/hipaa) |
| 8 | Saturated wave | not checked | There are 8+ dental AI receptionists on Product Hunt, but most launch dates are not shown, so the 10-launches-in-12-months threshold could not be verified. | [Product Hunt](https://www.producthunt.com/p/dentivoice) |

**Primary kill shot:** strong competitor. Weave holds the ADA channel, and 20+ products already sell this.

## 6. Market

- **Target customer:** owner-dentists of independent 1–3 location US general practices on Open Dental.
- **Pain:** missed calls at lunch and after hours go to voicemail. Vendors estimate a 20–35% missed-call rate, with ~75% of misses after hours. These are vendor data, not a representative sample ([Viva](https://getviva.ai/reduce-missed-calls-dental-practice), [Convirza](https://www.convirza.com/content-hub/missed-dental-calls-after-hours/)).
- **Demand signals:** paid dental-specific tools at $299–$899/month ([DentalBase](https://www.dentalbase.ai/blogs/ai-dental-receptionist-cost-2026-pricing-breakdown), tertiary), and Flossy at ~$4M ARR ([Latka](https://getlatka.com/interviews/flossy-miles-beckett-2026), self-reported).
- **Trend:** rising: +86% YoY search interest (2026, tertiary). A 5-year Google Trends check was not done.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $331.9M/year | estimate | 138,982 dental office locations (BLS via [StartBusinessByState](https://startbusinessbystate.com/dental-office-jobs/), Q1 2026) × $199 × 12. [IBISWorld](https://www.ibisworld.com/united-states/number-of-businesses/dental-offices/1557/) counts 180,742, so this is the low end. |
| SAM | unknown | unknown | No source for the share of practices on an open-API PMS without an AI phone tool |
| SOM (year 1) | $35,820/year | estimate | 15 clinics × $199 × 12. At 10 h/week and ~30 h per sale, that is ~1.3 sales/month at most. |

### Why now: late

| What changed | When | Source |
|--------------|------|--------|
| The FCC ruled that AI voices count as "artificial" voices under the TCPA: outbound AI calls need consent | 2024-02 | [FCC](https://WWW.FCC.GOV/document/fcc-makes-ai-generated-voices-robocalls-illegal) |
| ADA Member Advantage endorsed Weave, including an AI receptionist for missed calls | 2026-03 | [ADA News](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/) |
| Weave expanded its AI Receptionist across voice and text | 2026-07 | [Business Wire](https://www.businesswire.com/news/home/20260714657155/en/) |
| "AI receptionist" searches up 86% YoY to ~4,400/month | 2026 | [FindSkill](https://findskill.ai/learn/ai-receptionist/) |

Voice AI made the product buildable, but the leader now holds the ADA channel. The window for a generic $199 product is closing.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Owner-dentist of an independent 1–3 location general practice on Open Dental, with 1–2 front-desk staff and no AI phone tool yet |
| **Where to reach them** | Dentaltown forums, state dental association events, dental marketing agencies, the Open Dental user community, local practices (walk-in) |
| **Pays for today** | Front-desk staff, voicemail, human answering at $0.75–$1.50/min, or Weave bundles |
| **Budget** | $299–$899/month per location for dental AI receptionists (DentalBase, 2026) |
| **Trigger** | A front-desk employee quits. 55% of dentists find admin hiring extremely or very hard (ADA HPI via [Becker's](https://www.beckersdental.com/staffing-issues/how-dentists-are-faring-against-workforce-shortages/), 2025) |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | After-hours and lunch overflow answering with booking | Practice owner | 4–6 weeks |
| 2 | **White-label connector resold by dental marketing agencies** | Agency (passes the cost to clinics) | 6–8 weeks |
| 3 | Missed-call text-back only (no voice) | Practice owner | 1–2 weeks |

**Best option:** #2. It is the only one where someone else already owns the distribution.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| [Weave AI Receptionist](https://www.getweave.com/press-releases/weave-named-exclusive-patient-engagement-platform-endorsed-for-american-dental-association-members/) | US | Patient engagement suite with an AI receptionist | unknown | 5 | Bundled; books only into qualified PMS |
| [Flossy (Fiona)](https://getlatka.com/interviews/flossy-miles-beckett-2026) | US | Dental AI receptionist | $500/month per location (2026) | 4 | 2.5× the $199 price |
| [Dentina AI](https://www.cloudtalk.io/blog/dentina-ai-pricing/) | US | Dental AI receptionist | $299–$399/month per location, annual (2026-09) | 3 | Annual billing required |
| [Arini](https://ycombinator.com/companies/arini) | US | Dental AI receptionist, YC W24, ~$500K raised ([VCBacked](https://www.vcbacked.co/company/arini)) | unknown | 3 | Pricing not public |
| [Quo Sona](https://www.quo.com/answering-service) | US | Generic AI phone agent | $25–$199/month (2026) | 4 | No dental PMS booking |
| [TensorLinks AI FrontDesk](https://www.producthunt.com/p/tensorlinks-ai-frontdesk) | unknown | Books into Dentrix, Eaglesoft, Open Dental + 15 PMS | unknown | 1 | Already claims broad integrations |
| [Viva AI](https://www.producthunt.com/posts/974669) | US | Calls, texts, booking, insurance checks (launched 2025-06) | unknown | 2 | Broader scope |

Also found: SmileDial, DentiVoice, OrapexAI, TalkScaled, DentaBot (Product Hunt), Heygent, Trillet, Dialzara, Smith.ai, and NexHealth, a dental scheduling platform valued at $1B ([NexHealth](https://www.nexhealth.com/resources/series-c)).

- **Free alternatives:** Quo's 10 free AI calls/month on paid plans. There is also a DIY route: Dental Economics argues most products are "overpriced versions" of what practices can build ([Dental Economics](https://www.dentaleconomics.com/science-tech/artificial-intelligence/article/55291712/ai-dental-receptionists-hype-reality-and-how-to-build-one-yourself)).
- **Edge:** none that buyers see. Being a developer lowers build cost, but that doesn't make the product better than theirs. The only lever is price.
- **First 10 customers would come from:** local walk-ins and cold calls, or (better) 2–3 dental marketing agencies.

## 8. What customers say

No verbatim dentist quotes were collected. Secondhand: a Dentaltown author calls AI receptionists "the latest grift" (he runs a competing agency) ([Dentaltown](https://www.dentaltown.com/blog/post/22270/ai-dental-receptionists-the-latest-grift)). A dentist reported that an AI writing into the schedule without rules did real damage ([eesel](https://www.eesel.ai/blog/ai-receptionist-for-dentists)).

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $199/month | user input | Stated price |
| Variable cost per unit | $101/month | estimate | 500 min × $0.11 voice ($55) + Open Dental API $35 + Stripe ($6) + number/SMS $5 |
| Gross margin % | 49.2% | estimate | (199 − 101) ÷ 199 |
| Churn / lifetime | 5% / 20 months | estimate | SMB SaaS 3–7%/month; 6.2% in 2026 ([Visionary Marketing](https://visionary-marketing.co.uk/blog/saas-churn-benchmarks-2026), [Lenny's](https://www.lennysnewsletter.com/p/monthly-churn-benchmarks)) |
| Conversion rate | 2% | estimate | 1 paid clinic per 50 cold contacts |
| CAC | $1,500 | estimate | 30 founder hours × $50/h |
| LTV | $1,958 | estimate | 199 × 49.2% × 20 |
| LTV : CAC | 1.31 | estimate | 1,958 ÷ 1,500 |
| Payback (months) | 15.3 | estimate | 1,500 ÷ 98 |
| Fixed costs / month | $100 | estimate | Hosting $50 + domain/email $20 + HIPAA-eligible storage/logging $30 |
| Break-even (customers / month) | 2 | estimate | 100 ÷ 98 → 2 clinics |
| Time to first revenue (weeks) | 8 | estimate | 4–6 weeks build + 2 weeks sale and PMS access |

| Cost item | Monthly | Source |
|-----------|---------|--------|
| Voice AI (infra $0.055/min + LLM + TTS + telephony $0.015/min) | ~$55 per clinic | [Retell](https://www.retellai.com/it/pricing) |
| Open Dental API (top tier) | up to $35 per location | [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) (tertiary) |
| Dentrix API (if needed) | $5,000 read + $5,000 write, one-time | [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) (tertiary) |

| Scenario | Customers / month | Revenue / month | Costs / month | Margin | Note |
|----------|-------------------|-----------------|---------------|--------|------|
| Pessimistic | 2 | $398 | $302 | $96 | 2 clinics by month 6; covers the tools, not your time |
| Base | 8 | $1,592 | $908 | $684 | 8 clinics by month 12 at ~1 sale/month after churn |
| Optimistic | 25 | $4,975 | $2,625 | $2,350 | Agency resale works; 10 h/week is no longer enough for support |

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | Scripted voice demo in days; real Open Dental booking in 4–6 weeks at 10 h/week |
| Skills missing | Dental workflows, HIPAA compliance, B2B sales to dentists |
| Key dependencies | Voice AI vendor (Retell or similar), PMS API access granted per practice, BAA-signing vendors |
| Legal / compliance | HIPAA BAAs across the whole call path; TCPA consent for AI-voice callbacks |

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | The AI books a wrong slot or mishandles an upset patient, and the clinic churns | M | H | Book into held slots only; staff confirm | [eesel](https://www.eesel.ai/blog/ai-receptionist-for-dentists) |
| 2 | HIPAA breach or a missing BAA in the voice stack | M | H | Use only BAA-signing vendors; minimum-necessary PMS scope | [Aira](https://www.getaira.io/hipaa) |
| 3 | Incumbents (Weave) bundle the feature at no extra cost | H | H | Target practices outside the Weave base | [Business Wire](https://www.businesswire.com/news/home/20260714657155/en/) |
| 4 | Dentrix/Eaglesoft practices are out of reach because of integration fees | H | M | Open Dental only at first | [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|--------------------|-----------|-------|---------------|--------|
| Profit potential (25) | gross margin | 2 | ~49% margin (estimate). R5 cap: costs_eat_margin hit (2.5 → 2) | [Retell](https://www.retellai.com/it/pricing) |
| | LTV : CAC | 1.5 | LTV $1,958 vs founder-led CAC $1,500 = 1.3 (estimate) | [Visionary Marketing](https://visionary-marketing.co.uk/blog/saas-churn-benchmarks-2026) |
| | pricing power | 2 | Undercuts $299–$899 dental tools; generic Quo Sona tops out at $199 | [DentalBase](https://www.dentalbase.ai/blogs/ai-dental-receptionist-cost-2026-pricing-breakdown) |
| Feasibility (20) | build effort | 2.5 | Voice API + Open Dental slot/booking API: ~4–6 weeks at 10 h/week | [Nirmitee](https://nirmitee.io/healthcare-interoperability/open-dental-api-integration/) |
| | skills match | 3 | Developer covers the build; dental, HIPAA and sales are new | — |
| | capital needed | 3 | $2,000 covers an Open Dental pilot; Dentrix write access costs $10,000 | [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |
| Time to first revenue (15) | time to MVP | 2.5 | First paid pilot ~8 weeks out (estimate) | — |
| | sales cycle | 2.5 | Demo, trust in an AI touching the schedule, PMS access: weeks per deal | [eesel](https://www.eesel.ai/blog/ai-receptionist-for-dentists) |
| | channel readiness | 2 | No audience; dental clicks average $7.85; the ADA channel belongs to Weave | [Netpeak](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) |
| Market demand (15) | search demand | 3.5 | ~4,400 US searches/month for "AI receptionist" | [FindSkill](https://findskill.ai/learn/ai-receptionist/) |
| | trend | 4.5 | +86% YoY | [FindSkill](https://findskill.ai/learn/ai-receptionist/) |
| | willingness to pay | 4 | Flossy ~$4M ARR at $500/location | [Latka](https://getlatka.com/interviews/flossy-miles-beckett-2026) |
| Competitive room (10) | free alternatives | 3 | Quo includes 10 free AI calls; Weave bundles it; neither does PMS booking | [Quo help](https://support.quo.com/hc/en-us/articles/30808928416151-FAQs-about-Sona-the-OpenPhone-AI-Agent) |
| | competitor density | 1 | 20+ direct competitors | [Product Hunt](https://www.producthunt.com/p/tensorlinks-ai-frontdesk) |
| | differentiation | 1.5 | Lower price only | [CloudTalk](https://www.cloudtalk.io/blog/dentina-ai-pricing/) |
| Risk (10, 5 = low) | legal / regulatory | 2.5 | BAAs across the stack; TCPA for AI-voice callbacks | [Aira](https://www.getaira.io/hipaa) |
| | platform dependency | 2.5 | Per-practice PMS API access; one voice-AI vendor's pricing | [Ainora](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |
| | market risk | 4 | Durable need; admin hiring is hard for 55% of dentists | [Becker's](https://www.beckersdental.com/staffing-issues/how-dentists-are-faring-against-workforce-shortages/) |
| Founder fit (5) | skills | 3 | Builds software; no dental or sales track record stated | — |
| | assets | 1 | No audience, network or data stated | — |
| | interest | 1.5 | Goal stated as side income | — |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 1.83 | 9.17 |
| Feasibility (20) | 2.83 | 11.33 |
| Time to first revenue (15) | 2.33 | 7.00 |
| Market demand (15) | 4.00 | 12.00 |
| Competitive room (10) | 1.83 | 3.67 |
| Risk (10) | 3.00 | 6.00 |
| Founder fit (5) | 1.83 | 1.83 |
| **Raw total** | | **51.0** |
| **Rules applied** | R5: costs_eat_margin hit → gross_margin 2.5 → 2 | |
| **Final score** | | **51 / 100** |

## 13. Sources

34 sources from 31 domains: 13 primary, 10 secondary, 11 tertiary. All accessed 2026-11-11.

1. [DentalBase, AI dental receptionist cost 2026](https://www.dentalbase.ai/blogs/ai-dental-receptionist-cost-2026-pricing-breakdown): $299–$899/month range (tertiary, 2026)
2. [CloudTalk, Dentina AI pricing](https://www.cloudtalk.io/blog/dentina-ai-pricing/): Dentina $299/$399 (secondary, 2026-09)
3. [Viva, Reduce missed calls](https://getviva.ai/reduce-missed-calls-dental-practice): 35% missed-call rate, vendor (tertiary)
4. [Convirza, missed dental calls after hours](https://www.convirza.com/content-hub/missed-dental-calls-after-hours/): 75.2% after hours (secondary)
5. [Y Combinator, Arini](https://ycombinator.com/companies/arini): YC W24 dental AI receptionist (primary)
6. [VCBacked, Arini](https://www.vcbacked.co/company/arini): ~$500K raised, 2024-02 (secondary)
7. [StartBusinessByState, dental office jobs](https://startbusinessbystate.com/dental-office-jobs/): 138,982 locations, BLS Q1 2026 (secondary)
8. [IBISWorld, dental offices](https://www.ibisworld.com/united-states/number-of-businesses/dental-offices/1557/): 180,742 businesses, 2026 (secondary)
9. [Aira, HIPAA and AI receptionists](https://www.getaira.io/hipaa): BAA required (tertiary)
10. [Weave press release, ADA endorsement](https://www.getweave.com/press-releases/weave-named-exclusive-patient-engagement-platform-endorsed-for-american-dental-association-members/) (primary, 2026-03)
11. [ADA News, ADA endorses Weave](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/) (primary, 2026-03)
12. [Business Wire, Weave expands AI Receptionist](https://www.businesswire.com/news/home/20260714657155/en/) (primary, 2026-07)
13. [Product Hunt, Viva AI](https://www.producthunt.com/posts/974669) (primary, 2025-06)
14. [Product Hunt, TensorLinks AI FrontDesk](https://www.producthunt.com/p/tensorlinks-ai-frontdesk) (primary)
15. [Product Hunt, SmileDial](https://www.producthunt.com/products/smiledial/launches) (primary, 2024-08)
16. [Product Hunt, DentiVoice](https://www.producthunt.com/p/dentivoice) (primary)
17. [Retell AI pricing](https://www.retellai.com/it/pricing): voice-AI component rates (primary, 2026)
18. [Ainora, Open Dental vs Dentrix API](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026): API fees (tertiary, 2026)
19. [Nirmitee, Open Dental API guide](https://nirmitee.io/healthcare-interoperability/open-dental-api-integration/): slots and booking endpoints (tertiary)
20. [FCC, AI-generated voices in robocalls](https://WWW.FCC.GOV/document/fcc-makes-ai-generated-voices-robocalls-illegal) (primary, 2024-02)
21. [Orrick, Did the FCC ban AI voice calls?](https://www.orrick.com/insights/2024/02/Did-the-FCC-Really-Ban-AI-Generated-Voice-Calls-No-But-Restrictions-Apply) (secondary, 2024-02)
22. [Latka, Flossy founder interview](https://getlatka.com/interviews/flossy-miles-beckett-2026): ~$4M ARR, $500/location (secondary, 2026)
23. [Netpeak, dental CPC](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/): $7.85 average (tertiary, 2025)
24. [Quo, AI answering service](https://www.quo.com/answering-service): Sona tiers (primary, 2026)
25. [Quo help, Sona FAQ](https://support.quo.com/hc/en-us/articles/30808928416151-FAQs-about-Sona-the-OpenPhone-AI-Agent): 10 included calls (primary, 2026)
26. [Lenny's Newsletter, churn benchmarks](https://www.lennysnewsletter.com/p/monthly-churn-benchmarks) (secondary)
27. [Visionary Marketing, SaaS churn 2026](https://visionary-marketing.co.uk/blog/saas-churn-benchmarks-2026): SMB 6.2%/month (tertiary, 2026)
28. [Becker's Dental, workforce shortages](https://www.beckersdental.com/staffing-issues/how-dentists-are-faring-against-workforce-shortages/): ADA HPI hiring data (secondary, 2025)
29. [FindSkill, AI receptionist](https://findskill.ai/learn/ai-receptionist/): +86% YoY searches (tertiary, 2026)
30. [Dentaltown, the latest grift](https://www.dentaltown.com/blog/post/22270/ai-dental-receptionists-the-latest-grift) (tertiary, 2025-03)
31. [Dental Economics, hype and reality](https://www.dentaleconomics.com/science-tech/artificial-intelligence/article/55291712/ai-dental-receptionists-hype-reality-and-how-to-build-one-yourself) (secondary, 2025)
32. [eesel, AI receptionist for dentists](https://www.eesel.ai/blog/ai-receptionist-for-dentists) (tertiary, 2026)
33. [HackerNoon, Winding down Olympia](https://hackernoon.com/winding-down-olympia-what-we-built-what-i-learned-and-why) (tertiary, 2025)
34. [NexHealth, Series C](https://www.nexhealth.com/resources/series-c): $125M at a $1B valuation (primary, 2022-04)
