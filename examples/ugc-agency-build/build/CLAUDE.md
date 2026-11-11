# Rules for an agent working on Hookline Studio

1. Follow `pelloux-guidelines.md` on every change: it is mandatory (3 approaches then the simplest, size limits, surgical changes, Make/Test/Document).
2. Before any work, read `docs/prd.md` and the current sprint in `docs/sprints.md`. Sprint 0 is a sales test, not code: do not build features before its exit is met.
3. Work one story at a time, by ID from `docs/user-stories.md`. Do not start a story from a later sprint while the current sprint's exit is unmet.
4. A story is done only when every item in `docs/definition-of-done.md` passes, including the check on the real thing and the customer's answer.
5. `plan.json` is the source of truth for numbers, prices and sprints. Change it there and rerun `build-kit.py`; never hand-edit the rendered files (BUILD.md, docs/user-stories.md, docs/sprints.md, docs/definition-of-done.md, docs/business-plan.*, docs/brand.md, docs/motion.md, docs/ads.md, .env.example, design-tokens.*, video/).
6. Keep `app/` on the Python standard library and plain HTML/CSS unless an ADR in `docs/decisions.md` says otherwise.
7. Never commit `.env`, API keys, client data or creator personal data. `app/ops/data/` stays gitignored.
8. Keep the README's Run section true: if a command changes, update it in the same change, and run `python3 -m unittest discover -s tests` in `app/`.
9. No spending, sending, publishing, deploying, signing up or signing contracts without the founder's explicit yes. That includes cold emails, ads, Stripe links in live mode and domain purchases.
10. No product claims in briefs, ads or the site that the client has not approved and that are not true. Creators disclose paid relationships.
11. Apply the kill criteria in `docs/prd.md` as written; report them to the founder, never soften them.
