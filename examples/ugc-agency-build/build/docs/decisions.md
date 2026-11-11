# Decisions: Hookline Studio

## ADR-001: Build rescue path 1, a fixed monthly package, not the 20% commission

- **Status:** accepted, 2026-11-11
- **Context:** The original idea scored PIVOT 56/100. Its primary kill shot is a strong competitor: Billo sells a video with rights from $99, JoinBrands charges 8-15%, TikTok Shop's Find Creators is free, and a solo broker has nothing that stops a brand rebooking creators directly. Rescue 1 (score 60) sells a fixed $1,200/month package of 8 ad-ready videos with hooks to Shopify brands spending $5-30K/month on Meta ads. Rescue 2 (score 59) adds AI variants in one vertical but takes 1-2 months and new tool skills.
- **Decision:** Build rescue 1. Lead with a $799 pilot of 4 videos (the verdict's cheapest test), then convert to the $1,200/month package.
- **Consequences:** Revenue per client rises from about $140 to $1,200 a month and the studio owns the brief, which is harder to bypass. In exchange, the founder must write hooks and briefs, and the sale is harder than a per-video commission (CAC assumed $300 vs the verdict's $190). Creator rates must stay near $100 per video or the package loses money.

## ADR-002: Stack: static page, Stripe Payment Links, Instantly, Python stdlib tracker

- **Status:** accepted, 2026-11-11
- **Context:** $1,000 budget, 15 hours a week, no stated coding or sales skills. The verdict's fixed tools budget is $86/month. What needs measuring is outreach replies, paid pilots and hours per video.
- **Decision:** A plain HTML offer page, Stripe Payment Links for both offers, Instantly for cold email, and a single-file Python standard-library tracker writing CSV. Rejected: a UGC platform back office (fees eat the margin, brands can go direct) and a no-code portal (time better spent selling at 1-2 clients).
- **Consequences:** Nothing to install or maintain; total tools $86/month. No client self-service: the founder handles every brief by email. Revisit at 4+ active clients (the 15 h/week ceiling).

## ADR-003: Hosting: any free static host for the offer page, no backend

- **Status:** accepted, 2026-11-11
- **Context:** The page is one HTML file and one CSS file. Payments run on Stripe's hosted checkout, so there is no server-side code or customer data on the page.
- **Decision:** Host `app/site/` on any free static host the founder already has an account with. No backend, no database, no analytics script in sprint 0. The founder picks the host and deploys; the agent does not.
- **Consequences:** $0 hosting and no security surface beyond the Stripe links. No conversion tracking on the page; replies and payments are counted in the tracker instead.

## ADR-004: Track kill criteria in code, not in the founder's head

- **Status:** accepted, 2026-11-11
- **Context:** The verdict's kill criteria are numeric (3 positive replies per 100 emails, 1 paid pilot by day 14, 2 h per video, $20/h). They are easy to rationalise away once a pilot is in progress.
- **Decision:** `ops/tracker.py report` prints them as STOP flags from the logged data, with the thresholds as constants and the hourly floor configurable.
- **Consequences:** The founder must log every outreach batch and every hour. Client and creator data stay in gitignored CSV files.
