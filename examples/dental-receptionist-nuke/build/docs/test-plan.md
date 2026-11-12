# Test plan

## Levels
- **Unit:** pure functions in `src/slots.js` (slot finding, overlap checks, business hours), run with `node --test`.
- **Integration:** `src/openDental.js` against the Open Dental sandbox with synthetic patients. This needs `OPEN_DENTAL_*` env vars and is run manually.
- **Acceptance:** one manual pass per story, on real calls to the Retell demo line, using the story's acceptance criteria.

## Runner
`node --test` (Node 22 built-in). Run `npm test` from `app/`.

## Sprint exits
- Sprint 0: count from `validate/tracker.csv`. Pass with 2 or more paid pilots or letters of intent.
- Sprint 1: 50 scripted test calls with 0 overlapping slots offered.
- Sprint 2: 100 test bookings, checked in Open Dental. Pass at 95% or more correct.
- Sprint 3: Stripe shows 2 clinics paying, and the call log shows a hang-up rate under 20%.

## SmartTest
[SmartTest](https://github.com/RemiPelloux/SmarttyTest) runs only the tests a change can affect, through `node --test`.

Setup, from `app/`:
```bash
npm install -D @tkmremi/smarttest@1.2.0
npx smarttest init --dry-run
npx smarttest init --yes
npx smarttest hook install      # pre-commit hook: affected tests on every commit
```
- While coding: `npx smarttest run`
- Before a release: `npx smarttest run --all`
- In CI: `npx smarttest ci`
