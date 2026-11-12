# Fix: AI receptionist for US dental clinics

**Fixed idea:** An Open Dental-native, HIPAA-covered AI receptionist for independent practices, $199/month with no contract, sold by missed-call audits.

**Score:** 56 PIVOT → **60 PIVOT** (projected, raw 60.0). GO reachable: **no**.

## Levers (in order)

### L1 · features: Book straight into Open Dental (write API) under a signed BAA, with a warm hand-off to the front desk

Evidence: Users complain AI receptionists 'state they book but never do' and that Weave is 'not very compatible with Open Dental'; Open Dental sells write access at $30-35 per location ([source](https://www.opendental.com/site/apipermissions.html)). Difficulty hard, effort 6-8 weeks at 10 h/week, cost $30-35/clinic/month.

- differentiation: 1.5 → 3 (One real, specific difference: native Open Dental booking that generic and $29 tools lack)
- free_alternatives: 2 → 3 (Free text-back covers part of the job; nothing free books into a PMS under a BAA)
- Prerequisites: Open Dental API developer key and write tier (data, $30-35/clinic/month, have: no); Retell self-serve BAA (legal, $0 (vendor claim), have: unknown)

### L2 · channel: Missed-call audit outreach: call practices at lunch, then email the owner the result; first 3 pilots won locally in person

Evidence: 75.2% of missed dental calls are after hours and 20-38% go unanswered, so a personal audit gives a concrete hook; NPPES lists are free ([source](https://www.convirza.com/content-hub/missed-dental-calls-after-hours/)). Difficulty doable, effort 5 h/week ongoing, cost ~$100/month tools.

- channel_readiness: 2 → 3 (A channel exists with an estimated CAC (~$600) under first-year gross profit ($1,428))
- ltv_cac: 2.5 → 3 (CAC falls from ~$800 to ~$600 with a higher-reply audit hook: LTV:CAC ≈ 3.3)
- Clears: no_distribution
- Prerequisites: 5 hours a week for calls and emails (time, half the weekly budget, have: yes); Cold email domain and inboxes (money, ~$100/month, have: yes)

### L3 · model: Month-to-month with a paid 30-day pilot at $199; cancel by email

Evidence: Contract and cancellation complaints are the most repeated pain in Weave and Smith.ai reviews ([source](https://www.capterra.com/p/141842/Weave/reviews/?page=2)). Difficulty doable, effort 1 day, cost $0.

- sales_cycle: 3 → 3.5 (No contract and a paid pilot shorten the decision to about a week)
- Prerequisites: Stripe billing with cancel link (skill, $0 + fees, have: yes)

### L4 · other: Compliance pack: BAA chain (Retell; no OpenAI or Twilio direct without BAA), recording and AI disclosure on every call, state checklist

Evidence: HIPAA requires BAAs with business associates; ~11 states need all-party consent; CA, TX and UT require AI disclosure ([source](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/)). Difficulty doable, effort 20-30 hours, cost $0-500.

- legal_regulatory: 2 → 2.5 (Known compliance work, done before the first pilot)
- Prerequisites: HIPAA risk assessment template (legal, $0-300, have: no)

## Price

| Competitor | Price | Source | As of |
|---|---|---|---|
| Smith.ai AI (dental) | $285/month | [link](https://smith.ai/industries/dentists-answering-service) | 2026-11-12 |
| Dentina AI | $299/month | [link](https://www.cloudtalk.io/blog/dentina-ai-pricing/) | 2026-09-11 |
| Viva AI | $350/month | [link](https://www.getviva.ai/exciting-update-new-viva-ai-demo-promotional-pricing-350-month-no-contract/) | 2026-11-12 |
| Arini | $499/month | [link](https://www.capterra.com/p/10036210/Arini/reviews/) | 2026-11-12 |

**Recommended:** $199/month (undercut). 30-60% under dental tools with PMS booking ($285-499) while keeping ~60% gross margin and LTV:CAC near 3; generic $29-129 tools lack HIPAA or PMS depth, so no need to go lower.

## Features

**Must have**
- Real write-back booking into Open Dental: Top AI complaint: says it books but doesn't ([source](https://ca.trustpilot.com/review/smith.ai?page=4))
- Warm hand-off or forward to the front desk: Reviewers value calls routed to the right person ([source](https://ca.trustpilot.com/review/smith.ai?page=4))
- Month-to-month billing, cancel by email: Contract complaints lead competitor reviews ([source](https://www.capterra.com/p/141842/Weave/reviews/?page=2))
- Signed BAA and recording plus AI disclosure: HIPAA business associate rules and state consent laws ([source](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/))

**Cut**
- Outbound AI reminder calls: TCPA treats AI voices as artificial voices; consent risk for no core value
- Dentrix and Eaglesoft support: Dentrix access costs ~$10k plus royalties, 5x the budget
- SMS marketing campaigns: 10DLC vetting and scope creep; text-back only

**The one difference:** Native Open Dental booking, month to month. Weave books only on qualified PMS inside a 12-month bundle; generic tools don't integrate ([source](https://www.opendental.com/site/apipermissions.html))

## Plan

- **Week 1:** Run the 7-day missed-call audit test: 40 calls, 150 emails, 5 demos → verify: 2 or more paid $199 pilots or signed letters of intent
- **Week 2:** Sign the Retell BAA, get an Open Dental developer key, write the compliance pack → verify: BAA signed and test booking written into an Open Dental sandbox
- **Weeks 3-8:** Build the Open Dental booking agent and onboard the pilots → verify: 95% of AI bookings correct over 100 test calls
- **Weeks 9-12:** Audit outreach at 300 emails a week → verify: 5 paying clinics, under 20% call hang-up rate
- **Month 6:** Review churn and CAC; pitch 1 dental agency for white-label → verify: 12 clinics, monthly churn under 6%

## Kill criteria

- Fewer than 2 paid pilots from the audit test by 2026-11-20 -> stop
- AI booking accuracy under 90% on 100 test calls by 2027-01-15 -> stop or go request-only
- Fewer than 5 paying clinics by 2027-02-28 -> stop
- Monthly churn above 10% across 10+ clinics by 2027-05-31 -> stop

## Blockers (why not GO)

- Founder fit: no dental network, no healthcare compliance track record, 10 h/week (fit 1.7 of 5)
- A saturated field: Weave (40,000+ locations, ADA-endorsed) and 15+ rivals keep competitor density at 1
- Legal and platform exposure stays: HIPAA chain, state AI-disclosure laws and PMS access cap risk near 2.8
- Time to MVP stays ~8 weeks at 10 h/week; a team or full-time founder would move it

## Sources (accessed 2026-11-12)

- https://ca.trustpilot.com/review/smith.ai?page=4
- https://smith.ai/industries/dentists-answering-service
- https://www.capterra.com/p/10036210/Arini/reviews/
- https://www.capterra.com/p/141842/Weave/reviews/?page=2
- https://www.cloudtalk.io/blog/dentina-ai-pricing/
- https://www.convirza.com/content-hub/missed-dental-calls-after-hours/
- https://www.getviva.ai/exciting-update-new-viva-ai-demo-promotional-pricing-350-month-no-contract/
- https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/
- https://www.opendental.com/site/apipermissions.html
