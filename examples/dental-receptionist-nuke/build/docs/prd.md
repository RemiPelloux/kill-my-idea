# PRD: LunchLine

## Problem
Independent dental practices miss 20-38% of incoming calls, and 75% of missed calls come after hours (vendor data: Convirza, DentalBase). Missed new-patient calls are lost revenue. Today these practices rely on voicemail, an overloaded front desk, Weave's bundle (12-month contracts), or answering services that cost $175-700/month.

## Customer
Owner-dentists and office managers of independent 1-3 location US practices that run Open Dental and are not on Weave.

## Goals
- Answer missed calls, offer real Open Dental slots and write the booking back.
- Get 5 paying clinics at $199/month by 2027-02-28.
- Stay HIPAA-covered (BAA chain) and play a recording and AI disclosure on every call.

## Non-goals
- Dentrix or Eaglesoft support (Dentrix access is about $10k plus royalties).
- Outbound AI reminder calls (TCPA risk).
- SMS marketing.

## Must-have stories
US-01, US-02 (sprint 0, the test), US-03, US-04, US-05, US-06, US-07.

## Success metric
5 paying clinics by 2027-02-28, with monthly churn under 6%.

## 7-day test (sprint 0)
- Day 1: put up the one-page site and demo line.
- Day 2: call 40 practices at lunch and after 5 pm. Pass if 10 or more go unanswered.
- Day 3: build the Retell demo agent. Pass if 5 test calls are booked correctly.
- Day 4: send 150 audit emails. Pass if 6 or more owners reply.
- Day 6: hold demos. Pass if there are 3 or more.
- Day 7: count paid pilots. Pass if there are 2 or more pilots or letters of intent.

## Kill criteria
- Fewer than 8 of 40 test calls go unanswered by 2026-11-14: stop.
- Fewer than 3 demo bookings from 150 emails by 2026-11-19: stop.
- 0 paid pilots from 5 demos by 2026-11-22: stop.
- AI booking accuracy under 90% on 100 test calls by 2027-01-15: stop, or fall back to request-only booking.
- Fewer than 5 paying clinics by 2027-02-28: stop.

## Open questions
- Is Retell's self-serve BAA really free on pay-as-you-go? Confirm before the first pilot.
- What share of target practices run Open Dental?
- How many minutes does a clinic really use? The plan assumes 450.
- The base case needs about $2,782 of cash, which is more than the $2,000 budget. Either the first pilots must be prepaid, or ads have to be cut.
