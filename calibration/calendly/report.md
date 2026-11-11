<!-- kill-my-idea report. Every number cites a source or is labelled (estimate) with its formula. Data: idea.json + verdict.json. Same order as report.html. -->

> ## 🟡 PIVOT · 68/100
> **Booking links that end scheduling email ping-pong**
>
> `███████░░░` 68 / 100 · confidence high, 38 sources
>
> - ❌ Free tools set the price: Doodle MeetMe and Google appointment slots give a booking page away, and Atlas plans its Pro link at $5/month ([TNW, 2013-05](https://thenextweb.com/news/atlas-launches-to-reduce-the-stress-of-scheduling-helping-you-organize-group-meetings-on-the-go))
> - ❌ It runs on Google's Calendar API, and Google dropped deprecation guarantees for many APIs ([Google, 2012-04](https://developers.googleblog.com/2012/04/changes-to-deprecation-policies-and-api.html))
> - ✅ Mass-market demand that spreads itself: Doodle has 10M monthly users, 98% of them invited by another user ([TNW, 2011-10](https://thenextweb.com/news/its-not-sexy-but-it-sure-is-popular-group-scheduling-tool-doodle-hits-10m-monthly-users))
>
> **Could be saved:** sell to outbound salespeople first, with a team plan → 71/100 (doable)
> **Cheapest test:** landing page + hand-run concierge links for 50 sales reps, $8 pre-order button, 7 days
>
> <sub>Killed by [kill-my-idea](https://github.com/RemiPelloux/kill-my-idea)</sub>

![kill-my-idea: PIVOT 68/100](https://img.shields.io/badge/kill--my--idea-PIVOT%2068%2F100-yellow)

# Calendly: personal scheduling links (as of 2013-06-01) — kill-my-idea report

| | |
|---|---|
| **Evaluated** | 2026-11-11 (kill), **scored as of 2013-06-01**: only evidence published on or before that date |
| **Verdict** | PIVOT · 68/100 (raw 67.5) |
| **Confidence** | high: 16 sourced sub-scores of 21, 38 sources (14 primary) |
| **Countries** | US |
| **Assumptions** | USD 5,000, full time, solo developer; goal = startup; ICP = US salespeople and independent professionals; channel = the link's own viral loop; no audience; churn 4%/month (estimate) |

## 0. Executive summary

**Answer:** **PIVOT, 68/100.** Demand is real and rising (Doodle has **10M monthly users**), costs are tiny, and the link spreads itself. But free tools from Doodle and Google hold the price near $0, so a solo founder's $8 plan needs a niche that pays.

**Key findings**
1. **Free tools anchor the price at zero**: Doodle MeetMe (2011) and Google appointment slots (2011) give a **free** booking page, and Atlas plans its Pro link at **$5/month** ([TNW](https://thenextweb.com/news/arrange-one-to-one-meetings-with-ease-using-doodles-new-meetme))
2. **Demand is mass-market and viral**: Doodle has **10M monthly users**, 2M in the US, and **98%** found it through an invitation ([TNW, 2011](https://thenextweb.com/news/its-not-sexy-but-it-sure-is-popular-group-scheduling-tool-doodle-hits-10m-monthly-users))
3. **The closest rival just died**: RIM shut down Tungle.me on **2012-12-03**, leaving salespeople who put a booking link in their **email signature** without a tool ([TechCrunch](https://techcrunch.com/2012/09/18/rim-to-shut-down-tungle-me-team-will-focus-on-blackberry-10-calendar-app))

**Steelman:** A booking link spreads itself with every invite, as Doodle did (**98%** of its users came from invitations). It costs almost nothing to run, and Tungle's exit left the best use case unserved. The evidence backs the demand and the margin. It does not yet show that individuals will pay.

**Recommendation:** Do not launch a generic $8 consumer plan. Launch for outbound salespeople and former Tungle users, and pre-sell 10 paid seats in 7 days before building anything beyond an MVP.

**Premortem:** 12 months later, the idea failed. Most likely causes first.

| # | Cause | Linked to | Likelihood | Early signal (first 30 days) |
|---|-------|-----------|------------|------------------------------|
| 1 | Users love the free tier but under 1% upgrade, because Doodle and Google already give the core job away | free_alternative | H | Fewer than 2 upgrades per 100 active free users by day 30 |
| 2 | Nothing sets it apart from Atlas, Meetin.gs and Doodle MeetMe: a launch spike, then flat sign-ups | differentiation | M | Under 30% of new sign-ups come from invitee links after week 2 |
| 3 | A Google Calendar API change, or a free Google feature, undercuts the product | legal_platform_risk | L | Google announces booking features or API quota cuts; over 5% of syncs fail in a week |

## 1. Could it be saved?

| # | Change | Fixes | Score after | Difficulty | Effort | Cost | Requires |
|---|--------|-------|-------------|------------|--------|------|----------|
| 1 | Sell to outbound salespeople and recruiters first: booking link in the email signature, team plan at $10/user/month | pricing_power, willingness_to_pay, differentiation | 71/100 (estimate) | doable | 1 week | under $200 | Lists of sales reps on LinkedIn, team billing in Stripe |
| 2 | Win over former Tungle.me users and list on the Google Apps Marketplace at launch | channel_readiness | 69/100 (estimate) | doable | 2 weeks | near $0 | Marketplace listing, migration page for Tungle users |
| 3 | Support Outlook/Exchange and iCal alongside Google Calendar from v1 | platform_dependency | 68/100 (estimate) | hard | 2–3 extra months | time only | Exchange Web Services skills |

## 2. Next step: 7-day test

**Cheapest test:** a landing page plus a hand-run concierge link (Google appointment slots behind your domain) for 50 sales reps, with an $8/month pre-order button, run for 7 days.

| Day | Step | Verify |
|-----|------|--------|
| 1 | Landing page: "Put a booking link in your signature", with an $8/month pre-order button | Page live, analytics tracking 3 events |
| 2–3 | Message 500 US sales reps and former Tungle users on LinkedIn and Twitter | 100+ visits, 40+ sign-ups |
| 4–5 | Concierge: give 30 sign-ups a hand-set appointment-slot link on your domain | 20+ use it; 3+ invitees per link |
| 6–7 | Ask each user to pre-pay $8 for the first month | 10+ paid pre-orders |

**Stop if:**
- Fewer than 100 sign-ups from 500 targeted reps by day 7: stop, or re-target.
- Fewer than 10 people say they would pay $8/month by day 7: drop the paid plan.
- Fewer than 20% of beta users send their link to 3+ invitees in week 1: the viral loop doesn't exist, so stop.

## 3. Source

> Calendly: scheduling links so people book a meeting without email back-and-forth, freemium with a paid plan at $8 per month, launch country US. Score it as of 2013-06-01: use only evidence published on or before that date (set verdict.as_of). Founder: a solo developer with $5,000 and full time. Just go: do not ask questions. Use the slug calendly.

## 5. Kill shots

| # | Kill shot | Status | Evidence | Source |
|---|-----------|--------|----------|--------|
| 1 | Free alternative | **hit** | Doodle MeetMe (2011-02), Google appointment slots (2011-06) and Atlas (2013-05) are free; they cover part of the job, not all of it, so R1 is not applied | [TNW](https://thenextweb.com/news/arrange-one-to-one-meetings-with-ease-using-doodles-new-meetme) |
| 2 | Strong direct competitor | **hit** | Doodle: 10M monthly users and BookMe at €45/month; TimeBridge: 500,000+ users; TimeTrade raised $5.6M | [TNW](https://thenextweb.com/news/swiss-simple-scheduler-doodle-launches-bookme-appointment-service-online-bookings) |
| 3 | Graveyard | **hit** | Tungle.me was bought by RIM (2011-04) and shut down on 2012-12-03, a decision driven by the acquirer rather than by demand; TimeBridge sold to MerchantCircle (2010) | [TechCrunch](https://techcrunch.com/2012/09/18/rim-to-shut-down-tungle-me-team-will-focus-on-blackberry-10-calendar-app) |
| 4 | No distribution channel | clear | Every invitee sees the product (98% of Doodle's growth came from invitations); the Google Apps Marketplace reaches 2M+ businesses | [TNW](https://thenextweb.com/news/its-not-sexy-but-it-sure-is-popular-group-scheduling-tool-doodle-hits-10m-monthly-users) |
| 5 | Costs eat the margin | clear | Stripe takes ~$0.53 of each $8 charge and Heroku costs $0.05/hour: about 87% gross margin (estimate) | [Heroku](https://www.heroku.com/blog/2x-dynos-beta/) |
| 6 | Weak or falling demand | clear | Doodle's US base grew ~4x in two years to 2M (2011), and Doodle still had 10M monthly users in 2012-07 | [TNW](https://thenextweb.com/news/doodles-new-ipad-app-makes-scheduling-easier-for-its-10-million-monthly-users) |
| 7 | Legal / platform risk | **hit** | Built on the Google Calendar API; Google removed many API deprecation guarantees (2012-04) and had closed 70 products by 2013-03 | [Google](https://developers.googleblog.com/2012/04/changes-to-deprecation-policies-and-api.html) |
| 8 | Saturated wave (5 launches, 2012-06 to 2013-06) | clear | Doodle BookMe, MyTime, the Meetin.gs relaunch, Atlas and ScheduleOnce's push for Tungle users: fewer than 10 | [TNW](https://thenextweb.com/news/atlas-launches-to-reduce-the-stress-of-scheduling-helping-you-organize-group-meetings-on-the-go) |

**Primary kill shot:** free alternative.

## 6. Market

- **Target customer:** US outbound salespeople, recruiters and consultants who book 10+ external 1:1 meetings a week from Google Calendar.
- **Pain** and how they solve it today: several emails to agree on a time, plus prospects lost when replies stall. Today they use email, Doodle polls, Google slots or ScheduleOnce.
- **Demand signals:** Doodle has 10M monthly users, 2M in the US ([TNW, 2011](https://thenextweb.com/news/its-not-sexy-but-it-sure-is-popular-group-scheduling-tool-doodle-hits-10m-monthly-users)). US smartphone ownership is at 46% ([Pew, 2012](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners)), and sales is the 2nd-largest US occupational group ([BLS, 2013](https://www.bls.gov/news.release/archives/ocwage_03292013.htm)).
- **Trend:** rising. Doodle's US user base grew ~4x in 2 years.

| Market | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| TAM | $1.62B/year | estimate | 16.9M US independent workers ([MBO, 2012](https://www.mbopartners.com/wp-content/uploads/2019/02/2012-MBO_Partners_State_of_Independence_Report.pdf)) × $96/year |
| SAM | $192M/year | estimate | 2M US Doodle users × $96/year |
| SOM (year 1) | $0.19M/year | estimate | 0.1% of SAM ≈ 2,000 paying users |

### Why now: now

| What changed | When | Source |
|--------------|------|--------|
| Google Calendar API v3 (JSON, better recurring events) | 2011-11 | [Google](https://gsuite-developers.googleblog.com/2011/11/introducing-next-version-of-google.html) |
| Stripe public launch: 2.9% + 30¢, self-serve billing | 2011-09 | [TechCrunch](https://techcrunch.com/2011/09/30/sequoia-backed-stripe-launches-to-disrupt-the-online-payments-industry-with-a-developer-friendly-platform) |
| 46% of US adults own a smartphone | 2012-03 | [Pew](https://www.pewresearch.org/internet/2012/03/01/nearly-half-of-american-adults-are-smartphone-owners) |
| 5M+ businesses on Google Apps | 2012-07 | [Google](https://cloud.googleblog.com/2012/07/a-new-future-hitting-refresh-on.html) |
| Tungle.me shut down | 2012-12 | [TechCrunch](https://techcrunch.com/2012/09/18/rim-to-shut-down-tungle-me-team-will-focus-on-blackberry-10-calendar-app) |

Calendar APIs, payments and mobile all matured in 2011–2012, and Tungle's exit opened a gap. The risk is the free incumbents, not the timing.

### Ideal customer profile (ICP)

| | |
|---|---|
| **Who** | US outbound salespeople, recruiters and consultants booking 10+ external 1:1 meetings a week |
| **Where to reach them** | LinkedIn sales/recruiting groups · former Tungle.me users · Google Apps Marketplace · Hacker News / TechCrunch · sales blogs |
| **Pays for today** | Mostly nothing (email, free Doodle); small businesses pay Bookfresh $19.95/month or Doodle BookMe €45/month |
| **Budget** | unknown; sales tools are usually expensed per seat |
| **Trigger** | Their scheduling tool shuts down (Tungle, 2012-12), or they start a high-volume outreach role |

### Ways to use it

| # | Use case | Who pays | Effort |
|---|----------|----------|--------|
| 1 | Sales rep booking demos from a link in the email signature | Rep or sales manager | Low |
| 2 | Recruiter booking candidate screens | Recruiting team | Low |
| 3 | Consultant or coach booking client calls | The professional | Low |
| 4 | Small business taking customer appointments | Owner | Medium |

**Best option:** #1. It has a buyer with a budget, a proven use (Tungle in the email signature) and the strongest viral loop, because every prospect sees the link.

## 7. Competition

| Competitor | Country | What they do | Price (period, date) | Traction /5 | Gap |
|------------|---------|--------------|----------------------|-------------|-----|
| Doodle (polls + MeetMe) | CH | Group polls, personal booking page | free (2011-02) | 5 | Poll-first; the link is a side feature |
| Doodle BookMe | CH | Business appointment booking | €45 ≈ $58/month (2012-09) | 4 | Priced for businesses |
| Google appointment slots | US | Booking slots in Google Calendar | free (2011-06) | 4 | Clunky; possibly discontinued 2012-01 (unverified) |
| Bookfresh | US | SMB booking | $19.95/month (2012-02) | 3 | Built for shops |
| TimeBridge | US | Meeting scheduling | free core (2010-09) | 3 | Acquired, little focus |
| Groupon Scheduler | US | Merchant booking | free (2012-03) | 3 | Merchants only |
| TimeTrade | US | Enterprise appointments | unknown | 4 | Enterprise sales only |
| Meetin.gs | FI | Meeting pages | freemium (2013-04) | 2 | 22,000 users |
| Atlas | – | Free Tungle replacement | free, Pro planned at $5 (2013-05) | 1 | Almost the same idea |

- **Free alternatives:** Doodle MeetMe, Google appointment slots, TimeBridge, Atlas, Groupon Scheduler.
- **Edge:** none yet beyond execution. The specific opening is the signature-link workflow for salespeople that Tungle left behind.
- **First 10 customers:** former Tungle users and LinkedIn sales reps, reached by direct outreach.

## 9. Unit economics

| Metric | Value | Basis | Source / formula |
|--------|-------|-------|------------------|
| Price | $8/month | estimate | the founder's price |
| Variable cost per unit | $1.00/month | estimate | Stripe $0.53 ([Fortune, 2012](https://dc.fortune.com/2012/10/24/stripe-wants-to-reboot-online-payments/)) + ~$0.47 infrastructure/email, including free users |
| Gross margin % | 87.5% | estimate | (8 − 1) ÷ 8 |
| Churn / lifetime | 4%/month · 25 months | estimate | above the 3% "killer" threshold ([Cummings, 2012](https://davidcummings.org/2012/08/19/the-1-enemy-of-saas-churn/)) |
| Conversion rate | 2% free → paid | estimate | Evernote 0.5–4% ([2012](https://onemanandhisblog.com/2012/06/phil_libin_evernote_by_the_numbers)) |
| CAC | $50 | estimate | ~1 founder hour per paying user at $50/hour; AdWords ruled out (Dropbox CPA $233–388, [2010](https://www.slideshare.net/slideshow/dropbox-startup-lessons-learned-3836587/3836587)) |
| LTV | $175 | estimate | 8 × 0.875 × 25 |
| LTV : CAC | 3.5 | estimate | 175 ÷ 50 |
| Payback (months) | 7.1 | estimate | 50 ÷ 7.00 |
| Fixed costs / month | $100 | estimate | Heroku dyno ~$36 + database ~$50 + email/domain ~$14 |
| Break-even (customers / month) | 15 | estimate | 100 ÷ 7.00, no founder salary |
| Time to first revenue (weeks) | 10 | estimate | ~8 weeks to MVP + 2 |

| Cost item | Monthly | Source |
|-----------|---------|--------|
| Heroku 1X dyno, always on | ~$36 | [Heroku, 2013-04](https://www.heroku.com/blog/2x-dynos-beta/) |
| AWS m1.small (alternative) | ~$47 | [AWS, 2012-10](https://aws.amazon.com/about-aws/whats-new/2012/10/31/announcing-amazon-ec2-m3-instances-and-m1-price-drop/) |
| Transactional email | $0.10 per 1,000 | [TechCrunch, 2011](https://techcrunch.com/2011/05/10/email-delivery-system-sendgrid-announces-new-pricing-model-now-you-can-pay-as-you-go) |

| Scenario (month 12) | Customers | Revenue | Costs | Margin | Note |
|----------|-----------|---------|-------|--------|------|
| Pessimistic | 20 | $160 | $100 | $60 | 1,000 free users, 2% paid |
| Base | 150 | $1,200 | $150 | $1,050 | 7,500 free users via the invitee loop |
| Optimistic | 600 | $4,800 | $300 | $4,500 | sales-team niche, team plans, 4% paid |

Even the base case pays no salary at month 12. The $5,000 covers infrastructure, not the founder's rent.

## 11. Feasibility and risks

| Factor | Assessment |
|--------|------------|
| Build effort to a test | 1–2 months for a solid MVP; a concierge test takes 1 day |
| Skills missing | go-to-market and sales |
| Key dependencies | Google Calendar API v3, Stripe |
| Legal / compliance | CAN-SPAM only; transactional emails are mostly exempt ([FTC](https://webarchive.library.unt.edu/web/20130214054537/http://business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business)) |

Type checks (SaaS): **churn benchmark: unknown.** No dated benchmark for prosumer tools exists, so churn is modelled at 4%. **Switching cost: clear.** The incumbent is email, and Tungle users moved to other tools within weeks.

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|------|------------|--------|------------|--------|
| 1 | Free tools stop individuals from upgrading | H | H | Charge for team and sales features, not for the link | [TNW](https://thenextweb.com/news/arrange-one-to-one-meetings-with-ease-using-doodles-new-meetme) |
| 2 | Google Calendar API change or deprecation | M | H | Add Exchange and iCal sync | [Google](https://developers.googleblog.com/2012/04/changes-to-deprecation-policies-and-api.html) |
| 3 | Google ships a better free booking feature | M | H | Win on cross-calendar, branded links | [Google](https://workspaceupdates.googleblog.com/2011/06/manage-your-availability-with.html) |
| 4 | Churn above 3% a month at $8 | M | M | Annual plans, team seats | [Cummings](https://davidcummings.org/2012/08/19/the-1-enemy-of-saas-churn/) |
| 5 | Runway runs out before traction | M | H | Pre-sell seats; keep infrastructure under $100/month | [Heroku](https://www.heroku.com/blog/2x-dynos-beta/) |

## 12. Scorecard

| Criterion (weight) | Sub-score | Score | Justification |
|--------------------|-----------|-------|---------------|
| Profit potential (25) | gross margin | 4.5 | ~87% after Stripe and infrastructure (estimate) |
| | LTV : CAC | 3.5 | $175 vs ~$50 = 3.5 (estimate) |
| | pricing power | 2 | Free tools and Atlas set a $0–5 anchor |
| Feasibility (20) | build effort | 3 | 1–2 month solo build on Calendar API v3 |
| | skills match | 4 | Developer; marketing is the missing half |
| | capital needed | 4.5 | ~$50–100/month of infrastructure |
| Time to first revenue (15) | time to MVP | 2.5 | ~8 weeks to reliable sync plus billing |
| | sales cycle | 4.5 | Self-serve card payment, same day |
| | channel readiness | 3 | Viral loop exists; founder has no audience |
| Market demand (15) | search demand | 4 | Doodle: 10M monthly users |
| | trend | 4.5 | US base ~4x in 2 years |
| | willingness to pay | 2.5 | Small businesses pay; individuals expect free |
| Competitive room (10) | free alternatives | 2 | MeetMe and Google slots cover much of the job |
| | competitor density | 2 | 12+ tools |
| | differentiation | 2.5 | Tungle's gap; edge is execution only |
| Risk (10) | legal / regulatory | 4.5 | CAN-SPAM only |
| | platform dependency | 2.5 | Single Google API, no deprecation guarantee |
| | market risk | 4.5 | Durable daily need |
| Founder fit (5) | skills | 3.5 | Builds well; no sales track record |
| | assets | 1.5 | None stated |
| | interest | 2.5 | Not stated |

| Criterion | Mean | Points |
|-----------|------|--------|
| Profit potential (25) | 3.33 | 16.67 |
| Feasibility (20) | 3.83 | 15.33 |
| Time to first revenue (15) | 3.33 | 10.00 |
| Market demand (15) | 3.67 | 11.00 |
| Competitive room (10) | 2.17 | 4.33 |
| Risk (10) | 3.83 | 7.67 |
| Founder fit (5) | 2.50 | 2.50 |
| **Raw total** | | **67.5** |
| **Rules applied** | none (the R5 caps were already met) | |
| **Final score** | | **68 / 100** |

## 13. Sources

38 sources from 22 domains: 14 primary, 21 secondary, 3 tertiary. All were published on or before 2013-06-01. Later facts were excluded: Square buying Bookfresh (2014), Pew's 56% smartphone figure (2013-06-05), and every current pricing page. The full list, with tiers, is in `report.html` and `report-data.json`.
