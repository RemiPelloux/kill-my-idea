# LunchLine

An AI receptionist that answers the calls a dental front desk misses and books them into Open Dental.
Built from the **fixed** idea (kill-my-idea: PIVOT 56, projected 60 after fix). `LunchLine` is a working name; the domain and trademark are not checked yet.

## Idea

Independent dental practices miss 20-38% of calls, mostly at lunch and after hours. LunchLine answers those calls under a signed BAA, offers real open slots from Open Dental and writes the appointment back. It costs $199/month with no contract.

## Customer

Owner-dentists and office managers of independent 1-3 location US practices on Open Dental.

## Key metric

5 paying clinics at $199/month by 2027-02-28. If you don't hit it, stop (see `docs/prd.md`).

## Run

From a clean clone (Node 22.12+; the app has no dependencies):

```bash
cd app
cp ../.env.example .env        # fill in the values; never commit .env
npm test                       # node --test
npm start                      # webhook server on $PORT (default 8080)
```

Testing with SmartTest (run from `app/`):

```bash
npm install -D @tkmremi/smarttest@1.2.0   # a package.json is created if there is none
npx smarttest init --dry-run              # shows what it detected and what it would write
npx smarttest init --yes
npx smarttest hook install                # affected tests on every commit
npx smarttest run                         # affected tests while coding; --all before a release
```

## Structure

```
app/
├── package.json        scripts: start, test
├── src/
│   ├── config.js       env vars and named constants
│   ├── slots.js        pure slot-finding functions
│   ├── openDental.js   thin Open Dental API client
│   └── server.js       webhooks Retell calls: availability, book, hand-off
└── test/
    └── slots.test.js   unit tests (node --test)
```

## Status

Sprint 0 (the 7-day missed-call test) has not started. Don't write booking code until 2 practices pay for a pilot.

Start here: [BUILD.md](BUILD.md).
