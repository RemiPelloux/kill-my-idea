> ## 🟡 PIVOT · 54/100
> **AI receptionist for US dental clinics, $199/month**
>
> `█████░░░░░` 54 / 100 · confidence high, 56 sources
>
> - ❌ Weave already bundles an AI receptionist for **40,000+** practice locations, ADA-endorsed since 2026-03 ([source](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/))
> - ❌ No channel: r/SideProject and X reach founders, and dental CPC ~$7.85 puts Google Ads CAC near **$1,960** ([source](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/))
> - ✅ Dentists already pay $285-799/month for AI answering, and Retell at ~$0.10/min leaves a ~65% margin at $199
>
> **Could be saved:** Become the Open Dental-native receptionist: write-back booking and setup done for the clinic, sold through Open Dental consultants and dental IT providers → 61/100 (hard)
> **Cheapest test:** 7 days: call 40 clinics to measure missed calls, email 150 owners with the result, demo a Retell agent, ask for $199 paid pilots.
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 54/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2054%2F100-yellow)

# AI receptionist for US dental clinics — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-12 (kill) |
| **Verdict** | PIVOT · 54/100 (raw 54.2) |
| **Confidence** | high: 14 sourced sub-scores of 21, 56 sources (23 primary) |
| **Countries** | US |
| **Assumptions** | Headless run ('just go'): no questions asked; every gap below is an assumption. · Booking writes into the clinic's practice-management system through Open Dental's API or NexHealth; Dentrix direct integration is out of budget. · A clinic sends about 450 AI-handled minutes a month (300-600 range); not measured. · Monthly churn 6%, from SMB SaaS benchmarks (3-7%) and a critic's 3-6 month stays. · The voice stack is Retell with its BAA; Vapi's HIPAA add-on (~$1,000-2,000/month) is not used. · Goal of 5k USD MRR means about 26 paying clinics at 199 USD. |

## 0. Executive summary

**Answer:** **PIVOT at 54.** Dentists pay for this, but Weave bundles an AI receptionist from $199 with ADA endorsement, 10 look-alikes launched in a year, and a founder with **no dental network** has no channel to 26 clinics.

**Key findings**
1. **The incumbent already bundles it**: Weave serves **40,000+** practice locations, starts at $199/month, added an AI receptionist and won ADA endorsement in 2026-03. ([source](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/))
2. **No channel to dentists**: r/SideProject and X reach founders; dental CPC is ~$7.85, so Google Ads CAC is about **$1,960**, near the LTV. ([source](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/))
3. **Margins work at $199**: Retell parts cost about **$0.098/min**, so a 450-minute clinic costs ~$70 and leaves a 65% gross margin. ([source](https://www.retellai.com/pricing?utm_category=ai))

**Steelman:** A missed new-patient call is worth $850-1,800 in year one, so $199 pays back with one booking a month; voice AI at ~$0.10/min leaves a 65% margin, and dentists already pay $285-799 for this. The evidence supports the value; it does not support the founder's channel.

**Recommendation:** Don't build the generic product. Run the 7-day missed-call test in one metro; build only if 2 clinics pay for a pilot, and then pick a channel partner (Open Dental consultants or a dental agency).

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|---|---|---|---|
| 1 | No channel reached dentists: r/SideProject and X brought founders, cold email brought too few demos | no_distribution | H | Fewer than 3 demos from 150 cold emails in the first 30 days |
| 2 | Clinics cancelled after 3-6 months when patients hung up on the AI or bookings needed manual fixes | ltv_cac | M | More than 20% of AI calls end in a hang-up in pilot logs |
| 3 | Weave and phone vendors bundled the same feature at no extra cost, so prospects said 'we already have it' | strong_competitor | M | 3 of the first 10 prospects already use Weave or Mango AI |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|---|---|---|---|---|---|---|
| 1 | Become the Open Dental-native receptionist: write-back booking and setup done for the clinic, sold through Open Dental consultants and dental IT providers | Fixes no_distribution and differentiation: a partner channel and one specific difference | 61/100 (estimate) | hard | 3-4 months at 10 h/week | $30-35/clinic/month API + ~$500 | 2-3 reseller partners; Open Dental write API; BAA chain |
| 2 | Sell white-label to dental marketing agencies, who resell it to their clinics at $199+ | Fixes no_distribution: one agency brings 10-50 clinics; lowers CAC | 59/100 (estimate) | hard | 2-3 months | under $500 | agency partner, white-label dashboard, revenue share |
| 3 | Go local: walk-in and phone outreach to 200 independent dentists in one metro, concierge setup | Fixes channel_readiness with a cheap, direct channel; trust beats the wave | 57/100 (estimate) | doable | 4-6 weeks | under $300 | evenings for calls and visits; a demo line |

## 2. Next step: 7-day test

**Cheapest test:** 7 days: call 40 clinics to measure missed calls, email 150 owners with the result, demo a Retell agent, ask for $199 paid pilots.

| Day | Step | Verify |
|---|---|---|
| Day 1 | One-page site: 'We answer the calls your front desk misses, $199/month', with a booking link and a demo number | Page and demo line live, under $30 spent |
| Day 2 | Call 40 independent practices at lunch and after 5 pm; log which go unanswered | 10 or more of 40 calls unanswered |
| Day 3 | Build a Retell demo agent that answers as a sample practice and takes a booking request | 5 test calls booked correctly |
| Day 4 | Email 150 owners, including those you called: 'I called your office at 12:40 and nobody answered' | 6 or more replies |
| Day 6 | Run demos; offer a 30-day paid pilot at $199 | 3 or more demos held |
| Day 7 | Count pilots and objections (HIPAA, PMS, voice quality) | 2 or more paid pilots or signed letters of intent |

**Stop if:** Fewer than 8 of 40 test calls to clinics go unanswered by day 2 -> the pain is weak, stop; Fewer than 3 demo bookings from 150 cold emails by day 7 -> stop; 0 paid pilots ($199 first month) from 5 demos by day 10 -> stop

## 3. Source

> AI receptionist that answers missed calls and books appointments for US dental clinics, 199 USD a month per clinic. Country: United States. Budget: 2000 USD. Goal: a side business reaching 5k USD MRR within 12 months. Founder: solo developer, 10 hours a week, no dental network. Places to post: r/SideProject and X. Just go: do not ask questions.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|---|---|---|---|
| 1 | Free alternative | clear | Free missed-call text-back (Solvea, RingCentral + Zapier) covers part of the job, but nothing free answers and books into a PMS. | [link](https://solvea.cx/tools/missed-call-text-back) |
| 2 | Strong direct competitor | hit | Weave serves 40,000+ practice locations (2026-11) and bundles an AI receptionist; Arini (YC W24) and Smith.ai also sell to dentists. | [link](https://www.usecarly.com/blog/weave-ai-receptionist/) |
| 3 | Graveyard | hit | Breezy AI receptionist shut down on 2026-07-25; Air.ai stopped operating and faced an FTC suit (2025-08, allegations). | [link](https://www.getnextphone.com/blog/breezy-alternative) |
| 4 | No distribution channel | hit | No dental network; r/SideProject and X reach founders; dental CPC ~$7.85 gives a Google Ads CAC near $1,960 (estimate). | [link](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) |
| 5 | Costs eat the margin | clear | Retell parts ~$0.098/min and Twilio $0.0085/min leave ~65% gross margin at 450 min/month (estimate). | [link](https://www.retellai.com/pricing?utm_category=ai) |
| 6 | Weak or falling demand | clear | Demand is rising: RingCentral's AI receptionist went from 2,000+ to 11,800+ organizations by 2026-05. | [link](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/) |
| 7 | Legal / platform risk | hit | PHI on calls requires a BAA chain (HHS); ~11 all-party recording states; Dentrix integration reportedly $10k plus royalties. | [link](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/) |
| 8 | Saturated wave | hit | 10 near-identical AI receptionist launches found (Product Hunt and others), e.g. AI Recepts, Ringuzu, Catch.ai, OnCallClerk, Solvea. | [link](https://www.producthunt.com/products/ai-recepts/launches) |

**Primary kill shot:** no_distribution

## 6. Market

- **Target customer:** Independent US general dental practices, 1-3 locations
- **Pain:** 20-38% of calls go unanswered, mostly after hours, and missed new-patient calls are lost revenue
- **Today:** Voicemail, a busy front desk, Weave's bundle, or a paid answering service

| Market | Value | Basis | Source / formula |
|---|---|---|---|
| TAM | 323,200,000 USD/year | estimate | 135,333 US dental offices (Census 2020 via naicslist) x $199 x 12 = $323.2M |
| SAM | 193,900,000 USD/year | estimate | 60% of offices assumed independent and without a bundled AI receptionist: 81,200 x $2,388 = $193.9M |
| SOM | 38,200 USD/year | estimate | 16 clinics (0.02% of SAM offices) x $2,388 = $38.2k in year 1 |

### Why now: late

| What changed | When | Source |
|---|---|---|
| OpenAI Realtime API went GA with phone calling, about 20% cheaper | 2025-08 | [link](https://www.implicator.ai/openai-pushes-voice-agents-toward-enterprise-with-production-api-launch/) |
| Weave agreed to buy TrueLark and extended its AI receptionist across voice and text | 2026-04 | [link](https://www.businesswire.com/news/home/20260417125956/en/) |
| RingCentral AI Receptionist grew from 2,000+ to 11,800+ organizations | 2026-05 | [link](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/) |
| ElevenLabs launched Reception, a $29/month self-serve receptionist | 2026-09 | [link](https://runtimewire.com/article/elevenlabs-reception-ai-receptionist-small-business) |

Cheap voice AI opened the window in 2024-25; by late 2026 incumbents and $29 tools are closing it.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | Owner-dentist of an independent 1-3 location general practice on Open Dental, not on Weave |
| **Where to reach them** | Dentaltown forums, r/Dentistry, AADOM (office managers), state dental association meetings, dental office manager Facebook groups |
| **Pays for today** | Front-desk staff, voicemail, or answering services from $285/month (Smith.ai) to $800-2,500/month (live) |
| **Budget** | About $200-500 a month for call coverage (estimate from competitor prices) |
| **Trigger** | A front-desk employee quits, or call tracking shows new-patient calls going to voicemail |

## 7. Competition

| Competitor | Price (USD, period, date) | Traction /5 | Gap |
|---|---|---|---|
| [Weave](https://www.getweave.com/press-releases/weaves-latest-platform-enhancements-power-smarter-growth-for-healthcare-practices/) | 199/month (2026-11) | 5 (40,000+ practice locations; ADA endorsed) | Bundle with 12-month contract; AI books directly only on qualified PMS |
| [Arini](https://ycombinator.com/companies/arini) | 499-799/month (2026-11) | 3 (YC W24, 17 staff, $500K seed) | Priced 2.5-4x above $199; moving to a broad ops platform |
| [Smith.ai (dental)](https://smith.ai/industries/dentists-answering-service) | 285/month (2026-11) | 4 (Established answering service with AI tier) | Generalist, not dental-PMS native |
| [Viva AI](https://www.getviva.ai/viva-ai-pricing-which-plan-is-right-for-your-dental-office/) | 349/month (2025-06) | 2 (Dental-only; no review counts found) | Credit overages $0.08-0.10 |
| [Dentina AI](https://www.cloudtalk.io/blog/dentina-ai-pricing/) | 299-399/month (2026-09) | 2 (No G2 or Capterra profile) | Annual billing |
| [ElevenLabs Reception](https://runtimewire.com/article/elevenlabs-reception-ai-receptionist-small-business) | 29/month (2026-09) | 4 (Big voice-AI brand, self-serve) | Generic SMB; no dental PMS booking or BAA claim found |
| [My AI Front Desk](https://schedulingkit.com/pricing-guides/my-ai-front-desk-pricing) | 79-99/month (2026) | 2 (General SMB AI receptionist) | 200 minutes, then $0.25/min; not dental-specific |
| [Solvea missed-call text-back](https://solvea.cx/tools/missed-call-text-back) | 0/month (2026-11) | 2 (227 upvotes on Product Hunt launch day) | Text-back only, no voice booking |

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|---|---|---|---|
| competitors_found | 15 competitors | estimate | Counted: Weave, Arini, Viva, Dentina, Smith.ai, Mango Margo, Annie, Patientdesk, VoiceStack, RingCentral, My AI Front Desk, Trillet, ElevenLabs, Solvea, Catch.ai |
| competitor_price_range | 29-799 USD/month | estimate | Low: ElevenLabs Reception $29 (runtimewire); high: Arini Growth $799 (Capterra); dental-specific cluster $285-399 |
| demand_trend | rising  | sourced | https://www.cloudtalk.io/blog/ai-voice-agent-statistics/ |
| price | 199 USD/month | estimate | The founder's stated price: 199 USD per clinic per month |
| variable_cost_per_unit | 70 USD/clinic/month | estimate | 450 min x $0.098 (Retell parts) = $44 + number $2 + NexHealth ~$15 + card fees 3% $6 + 10DLC ~$3 = $70 |
| gross_margin_pct | 65 % | estimate | (199 - 70) / 199 = 64.8% |
| churn_monthly_pct | 6 % | estimate | SMB SaaS 3-7% monthly (UserJot) and a Dentaltown critic's 3-6 month stays: take 6% |
| expected_lifetime | 16.7 months | estimate | 1 / 0.06 = 16.7 months |
| conversion_rate_pct | 0.2 % of cold emails | estimate | 3% reply x 45% positive x ~15% close = 0.2% of sends (Ciela healthcare benchmark) |
| cac | 1000 USD | estimate | 500 emails per customer: ~15 h prospecting, demo and setup x $50/h = $750 + $250 tools and lead data |
| ltv | 2150 USD | estimate | $129 gross profit/month x 16.7 months = $2,150 |
| ltv_cac | 2.2 ratio | estimate | 2,150 / 1,000 = 2.15; with Google Ads CAC ~$1,960 it falls to 1.1 |
| payback_months | 7.8 months | estimate | 1,000 / 129 = 7.8 |
| fixed_costs_month | 150 USD/month | estimate | Cold email tool ~$100 + domain, hosting and DB ~$30 + misc $20 |
| break_even_customers_per_month | 2 customers | estimate | 150 / 129 = 1.2, rounded up to 2 clinics |
| time_to_first_revenue_weeks | 11 weeks | estimate | 8 weeks to a BAA-covered pilot at 10 h/week + 3 weeks of outreach and demo |

| Scenario | Clinics | Revenue / month | Costs / month | Note |
|---|---|---|---|---|
| Pessimistic | 6 | $1,194 | $570 | Cold email only; 6 clinics by month 12, churn 6% |
| Base | 15 | $2,985 | $1,200 | Cold email plus local outreach; 15 clinics by month 12 |
| Optimistic | 26 | $5,174 | $1,970 | One reseller partner brings 10+ clinics; hits the 5k MRR goal |

## 11. Risks

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|---|---|---|---|---|
| 1 | A HIPAA gap in the vendor chain (voice, LLM, telephony) exposes patient data | M | H | Use only vendors that sign BAAs; log and encrypt; no PHI in prompts beyond need | [link](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/) |
| 2 | Recording calls in all-party consent states without disclosure | M | M | Play a recording and AI disclosure on every call | [link](https://ktslaw.com/en/Blog/GlobalPrivacy-and-CybersecurityLaw/2024/7/Wiretap-Laws-in-the-United-States) |
| 3 | PMS integration cost or access blocks booking (Dentrix ~$10k) | H | M | Start with Open Dental or NexHealth; request-only booking elsewhere | [link](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |
| 4 | Weave or phone vendors bundle the feature for free | H | H | Target clinics not on Weave; sell on setup and results | [link](https://www.getweave.com/press-releases/weaves-latest-platform-enhancements-power-smarter-growth-for-healthcare-practices/) |
| 5 | Patients hang up on an AI voice; clinics churn in 3-6 months | M | H | Measure hang-up rate in pilots; human handoff to the front desk | [link](https://www.dentaltown.com/blog/post/22270/ai-dental-receptionists-the-latest-grift) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification | Source |
|---|---|---|---|---|
| profit (25) = 2.5 | gross_margin | 3 | About **65%** at 450 min/month: Retell ~$0.098/min plus number, NexHealth and fees ≈ $70 per clinic | [link](https://www.retellai.com/pricing?utm_category=ai) |
|  | ltv_cac | 2.5 | LTV ≈ $2,150 (6% churn) vs CAC ≈ $1,000 by cold outreach: **2.2**; Google Ads CAC ~$1,960 would be ~1.1 | [link](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) |
|  | pricing_power | 2.5 | $199 sits between $29 ElevenLabs Reception and $299-799 dental tools; Weave bundles AI from **$199** | [link](https://runtimewire.com/article/elevenlabs-reception-ai-receptionist-small-business) |
| feasibility (20) = 3.0 | build_effort | 3 | Voice stack is off the shelf (Retell); PMS write booking and HIPAA setup take 1-2 months at 10 h/week | [link](https://www.opendental.com/site/apipermissions.html) |
|  | skills_match | 3 | Developer can build it; HIPAA compliance and selling to dentists are skills the founder lacks |  |
|  | capital_needed | 3 | Fits $2,000 with Retell BAA and Open Dental; Dentrix ($10k) or a Vapi HIPAA add-on would not | [link](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) |
| time_to_first_revenue (15) = 2.5 | time_to_mvp | 2.5 | About 8 weeks to a booking-capable, BAA-covered pilot at 10 h/week (estimate) |  |
|  | sales_cycle | 3 | Owner dentist signs; demo plus HIPAA questions means 2-6 weeks per clinic (estimate) |  |
|  | channel_readiness | 1.5 | R5: no dental network; r/SideProject and X reach founders, not dentists; dental CPC ~$7.85 | [link](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) |
| demand (15) = 4.0 | search_demand | 3.5 | 135k US dental offices and live Dentaltown threads on missed new-patient calls | [link](https://www.dentaltown.com/channel/post/20099/why-an-average-dental-practice-converts-only-1-3rd-of-new-patient-calls-to-appointments) |
|  | trend | 4 | RingCentral AI Receptionist grew from **2,000 to 11,800** orgs in 11 months | [link](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/) |
|  | willingness_to_pay | 4 | Dentists already pay $285 (Smith.ai) to $799 (Arini) a month for AI answering | [link](https://www.capterra.com/p/10036210/Arini/reviews/) |
| competition (10) = 1.5 | free_alternatives | 2 | R3: free missed-call text-back (Solvea, Zapier) and $29 ElevenLabs cover part of the job | [link](https://solvea.cx/tools/missed-call-text-back) |
|  | competitor_density | 1 | R3/R5: 15+ rivals and 10 look-alike launches in 12 months; Weave serves 40,000+ locations | [link](https://www.usecarly.com/blog/weave-ai-receptionist/) |
|  | differentiation | 1.5 | R3: nothing specific yet; a cheaper generic AI receptionist is what the wave already sells |  |
| risk (10) = 3.0 | legal_regulatory | 2.5 | R5: PHI on calls needs a BAA chain; all-party recording consent in ~11 states; Utah AI disclosure | [link](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/) |
|  | platform_dependency | 2.5 | Booking depends on PMS access (Open Dental, NexHealth); Dentrix charges ~$10k plus royalties | [link](https://synchronizer.nexhealth.com/pricing) |
|  | market_risk | 3.5 | Missed calls are a durable need (75% after hours), but incumbents are absorbing the feature | [link](https://www.convirza.com/content-hub/missed-dental-calls-after-hours/) |
| fit (5) = 1.5 | skills | 2.5 | Builds software; no healthcare compliance or B2B dental sales track record |  |
|  | assets | 1 | No dental network, audience or data (stated) |  |
|  | interest | 1.5 | Stated goal is a side business at $5k MRR: money first, no dental interest stated |  |

**Total:** raw 54.2 → **54/100**. Rules applied: R5_kill_shot_coherence (no_distribution -> channel_readiness 1.5; saturated_wave -> competitor_density 1; legal_platform_risk -> legal 2.5); R3_saturated_wave (competition 2.2 -> 1.5, differentiation 2 -> 1.5 (10 look-alikes in 12 months, no specific edge))

## Sources

1. [Weave press release: platform enhancements (AI receptionist)](https://www.getweave.com/press-releases/weaves-latest-platform-enhancements-power-smarter-growth-for-healthcare-practices/) · primary · accessed 2026-11-12 · published 2026-04
2. [Business Wire: Weave AI receptionist expansion](https://www.businesswire.com/news/home/20260417125956/en/) · primary · accessed 2026-11-12 · published 2026-04-17
3. [ADA News: ADA Member Advantage endorses Weave](https://adanews.ada.org/ada-news/2026/march/ada-member-advantage-endorses-weave-as-patient-engagement-platform/) · secondary · accessed 2026-11-12 · published 2026-03
4. [Carly: Weave AI receptionist review](https://www.usecarly.com/blog/weave-ai-receptionist/) · tertiary · accessed 2026-11-12 · published 2026-11-04
5. [Y Combinator: Arini company page](https://ycombinator.com/companies/arini) · primary · accessed 2026-11-12 · published 2026-11
6. [Signalbase: Arini raises $500K seed](https://www.trysignalbase.com/news/funding/arini-raises-500k-seed-funding) · tertiary · accessed 2026-11-12 · published 2024-02
7. [Capterra: Arini reviews and pricing](https://www.capterra.com/p/10036210/Arini/reviews/) · secondary · accessed 2026-11-12 · published 2026
8. [Viva AI pricing: which plan is right for your dental office](https://www.getviva.ai/viva-ai-pricing-which-plan-is-right-for-your-dental-office/) · primary · accessed 2026-11-12 · published 2025-06-05
9. [CloudTalk: Dentina AI pricing](https://www.cloudtalk.io/blog/dentina-ai-pricing/) · secondary · accessed 2026-11-12 · published 2026-09-11
10. [Mango Voice: dental practices](https://mangovoice.com/dental/practices) · primary · accessed 2026-11-12 · published 2026
11. [SchedulingKit: My AI Front Desk pricing](https://schedulingkit.com/pricing-guides/my-ai-front-desk-pricing) · tertiary · accessed 2026-11-12 · published 2026
12. [Trillet: best AI phone system for dental office](https://www.trillet.ai/blogs/best-ai-phone-system-for-dental-office) · tertiary · accessed 2026-11-12 · published 2026
13. [DentalBase: dental virtual receptionist buyer's guide 2026](https://www.dentalbase.ai/blogs/dental-virtual-receptionist-buyers-guide-2026) · tertiary · accessed 2026-11-12 · published 2026
14. [DentalBase: dental AI receptionist options guide](https://www.dentalbase.ai/blogs/dental-ai-receptionist-options-guide) · tertiary · accessed 2026-11-12 · published 2026
15. [RingCentral: AI receptionist for small business](https://www.ringcentral.com/us/en/blog/ai-receptionist-for-small-business/) · primary · accessed 2026-11-12 · published 2026
16. [Zapier: send SMS for new missed calls in RingCentral](https://zapier.com/apps/ringcentral/integrations/sms/255591004/send-sms-for-new-missed-calls-in-ringcentral-with-sms-by-zapier) · primary · accessed 2026-11-12
17. [VoiceStack: missed-call automations for dental phones](https://voicestack.com/dental-phones/features/missed-call-automations) · primary · accessed 2026-11-12
18. [Solvea: free missed-call text-back tool](https://solvea.cx/tools/missed-call-text-back) · primary · accessed 2026-11-12
19. [Product Hunt: AI Recepts launches](https://www.producthunt.com/products/ai-recepts/launches) · primary · accessed 2026-11-12 · published 2026-02-17
20. [Product Hunt: Ringuzu AI Receptionist](https://www.producthunt.com/products/ringuzu-ai-receptionist/launches) · primary · accessed 2026-11-12 · published 2026-01-14
21. [Product Hunt: Catch.ai](https://www.producthunt.com/products/catch-ai/launches/catchai) · primary · accessed 2026-11-12 · published 2026-05-14
22. [Product Hunt: OnCallClerk 2.0](https://www.producthunt.com/products/oncallclerk/launches/oncallclerk-2-0-sounds-human) · primary · accessed 2026-11-12 · published 2026-05-01
23. [Hunted.space: Solvea launch stats](https://hunted.space/dashboard/solvea/launches/solvea) · tertiary · accessed 2026-11-12 · published 2026-03-31
24. [NextPhone: Breezy alternative (Breezy shutting down)](https://www.getnextphone.com/blog/breezy-alternative) · tertiary · accessed 2026-11-12 · published 2026
25. [Comparison page: Air.ai no longer operational](https://ai-main.pages.dev/compare/vs-air-ai) · tertiary · accessed 2026-11-12 · published 2025
26. [Dentaltown: AI Dental Receptionists - The Latest Grift](https://www.dentaltown.com/blog/post/22270/ai-dental-receptionists-the-latest-grift) · tertiary · accessed 2026-11-12 · published 2025-03-07
27. [ADA HPI: dentist workforce](https://www.ada.org/en/resources/research/health-policy-institute/dentist-workforce) · primary · accessed 2026-11-12 · published 2025
28. [NAICS 621210 offices of dentists](https://naicslist.com/naics/621210) · tertiary · accessed 2026-11-12 · published 2020
29. [Dental Economics: the economics of missed calls](https://dentaleconomics.com/practice/article/55385634/the-economics-of-missed-calls-quantifying-revenue-loss-in-dental-practices) · secondary · accessed 2026-11-12 · published 2025
30. [DentalBase: 38% of calls go unanswered](https://www.dentalbase.ai/blogs/38-percent-calls-go-unanswered-lost-revenue) · tertiary · accessed 2026-11-12 · published 2025
31. [ADA News: staffing shortages top expected challenges](https://adanews.ada.org/new-dentist/2025/march/staffing-shortages-top-expected-challenges-this-year) · primary · accessed 2026-11-12 · published 2025-03
32. [Market.us: AI receptionist market report](https://market.us/report/ai-receptionist-market/) · secondary · accessed 2026-11-12 · published 2026-08
33. [CloudTalk: AI voice agent statistics](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/) · tertiary · accessed 2026-11-12 · published 2026-07
34. [Implicator: OpenAI Realtime API goes GA](https://www.implicator.ai/openai-pushes-voice-agents-toward-enterprise-with-production-api-launch/) · secondary · accessed 2026-11-12 · published 2025-08
35. [Techsy: AI voice agent pricing](https://techsy.io/en/blog/ai-voice-agent-pricing) · tertiary · accessed 2026-11-12 · published 2026
36. [RuntimeWire: ElevenLabs launches Reception](https://runtimewire.com/article/elevenlabs-reception-ai-receptionist-small-business) · secondary · accessed 2026-11-12 · published 2026-09-16
37. [Retell AI pricing](https://www.retellai.com/pricing?utm_category=ai) · primary · accessed 2026-11-12 · published 2026-11
38. [Retell AI healthcare](https://www.retellai.com/healthcare) · primary · accessed 2026-11-12 · published 2026-11
39. [HappyRobot: Vapi AI pricing](https://happyrobot.ai/hub/vapi-ai-pricing) · tertiary · accessed 2026-11-12 · published 2026
40. [Twilio voice pricing US](https://www.twilio.com/voice/pricing/us) · primary · accessed 2026-11-12 · published 2026-11
41. [NexHealth Synchronizer pricing](https://synchronizer.nexhealth.com/pricing) · primary · accessed 2026-11-12 · published 2026-11
42. [Open Dental API permissions and pricing](https://www.opendental.com/site/apipermissions.html) · primary · accessed 2026-11-12 · published 2020-09
43. [Smith.ai dental answering service](https://smith.ai/industries/dentists-answering-service) · primary · accessed 2026-11-12 · published 2026-11
44. [Netpeak: average CPC for dental ads on Google 2025](https://netpeak.us/blog/the-average-cpc-for-dental-ads-on-google-in-2025-defined/) · secondary · accessed 2026-11-12 · published 2025
45. [Ciela: cold email benchmarks by industry 2026](https://ciela.ai/blogs/cold-email-open-rate-benchmarks-by-industry-2026) · tertiary · accessed 2026-11-12 · published 2026
46. [Convirza: missed dental calls after hours](https://www.convirza.com/content-hub/missed-dental-calls-after-hours/) · tertiary · accessed 2026-11-12 · published 2026
47. [Dentaltown: practices convert only a third of new-patient calls](https://www.dentaltown.com/channel/post/20099/why-an-average-dental-practice-converts-only-1-3rd-of-new-patient-calls-to-appointments) · tertiary · accessed 2026-11-12
48. [HHS: sample business associate agreement provisions](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/) · primary · accessed 2026-11-12
49. [Cooley: FCC rules AI-generated robocalls fall under TCPA](https://www.cooley.com/news/insight/2024/2024-02-15-fcc-ai-generated-robocalls-illegal-under-the-tcpa) · secondary · accessed 2026-11-12 · published 2024-02-15
50. [Kilpatrick: wiretap laws in the United States](https://ktslaw.com/en/Blog/GlobalPrivacy-and-CybersecurityLaw/2024/7/Wiretap-Laws-in-the-United-States) · secondary · accessed 2026-11-12 · published 2024-07
51. [DWT: Utah enacts AI and bot disclosure law](https://dwt.com/blogs/artificial-intelligence-law-advisor/2024/04/utah-enacts-ai-and-bot-business-disclosure-law) · secondary · accessed 2026-11-12 · published 2024-04
52. [Twilio: A2P 10DLC campaign vetting FAQ](https://support.twilio.com/hc/en-us/articles/11587910480155-A2P-10DLC-Campaign-Vetting-FAQ) · primary · accessed 2026-11-12 · published 2025-08
53. [Ainora: Denticon vs Open Dental vs Dentrix for AI](https://ainora.lt/blog/denticon-vs-open-dental-vs-dentrix-ai-comparison-2026) · tertiary · accessed 2026-11-12 · published 2026-08-26
54. [UserJot: SaaS churn rate benchmarks](https://userjot.com/blog/saas-churn-rate-benchmarks) · tertiary · accessed 2026-11-12 · published 2025
55. [Capterra: Weave reviews](https://www.capterra.com/p/141842/Weave/reviews/?page=9) · tertiary · accessed 2026-11-12 · published 2026
56. [Listicler: Weave pricing deep dive](https://listicler.com/blog/weave-pricing-deep-dive-small-healthcare-practices) · tertiary · accessed 2026-11-12 · published 2026

<sub>Run: 14 min, 33 searches, 15 fetches, 4 subagents.</sub>
