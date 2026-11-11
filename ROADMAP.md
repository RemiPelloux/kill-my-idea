# Roadmap to 1.0.0

1.0.0 is a quality bar, not a date. **Status (2026-11-11): shipped.** All 26 items of the [1.0.0 sprint](https://github.com/RemiPelloux/kill-my-idea/milestone/4) are closed. Two targets were missed and are recorded as such: "strong competitor" still hits almost every idea (it is now documented as information, see [How scoring works](docs/scoring.md)), and parallel research made runs more reliable, not faster (moved to [after 1.0](#after-10)).

**What 1.0 means**

1. **You can trust the score.** It separates good ideas from bad ones on a known test set, and a GO is reachable.
2. **The formats are stable.** Every file has a versioned schema. After 1.0, a breaking change needs a major version.
3. **Everything is tested.** The scripts and the rules have tests in CI, not only the example runs.
4. **Nothing in the default output runs code** written by the model.
5. **A surviving idea gets a plan.** Deepdive turns its evidence into personas, market strategies, promotion angles and a checked name, all sourced.

Each item below has why (the evidence), effort (S = under a day, M = a few days, L = a week or more) and done when.

---

## Work order

Do the items top to bottom; each one builds on the ones before it. The paid steps (the calibration
set, the regenerated examples and the gallery re-run) are real runs: at most 3 at a time, with the cost stated first.

**Foundations: build what everything else needs**

1. ✅ [#10](https://github.com/RemiPelloux/kill-my-idea/issues/10) Test suite
2. ✅ [#9](https://github.com/RemiPelloux/kill-my-idea/issues/9) Add schema_version to every file
3. ✅ [#12](https://github.com/RemiPelloux/kill-my-idea/issues/12) No executable data by default
4. ✅ [#5](https://github.com/RemiPelloux/kill-my-idea/issues/5) Add scripts/calibrate.py
5. ✅ [#8](https://github.com/RemiPelloux/kill-my-idea/issues/8) Hindsight guard

**The score: better input, then calibrate and freeze it**

6. ✅ [#23](https://github.com/RemiPelloux/kill-my-idea/issues/23) Idea types
7. ✅ [#24](https://github.com/RemiPelloux/kill-my-idea/issues/24) Smarter questions
8. ✅ [#25](https://github.com/RemiPelloux/kill-my-idea/issues/25) Follow-up after research
9. ✅ [#4](https://github.com/RemiPelloux/kill-my-idea/issues/4) Calibration set
10. ✅ [#6](https://github.com/RemiPelloux/kill-my-idea/issues/6) Strong competitor threshold
11. ✅ [#7](https://github.com/RemiPelloux/kill-my-idea/issues/7) Weights review
12. ✅ [#11](https://github.com/RemiPelloux/kill-my-idea/issues/11) Golden runs
13. ✅ [#13](https://github.com/RemiPelloux/kill-my-idea/issues/13) Regenerate the examples

**Go to market (deepdive)**

14. ✅ [#26](https://github.com/RemiPelloux/kill-my-idea/issues/26) Deepdive: personas
15. ✅ [#27](https://github.com/RemiPelloux/kill-my-idea/issues/27) Deepdive: market strategy options
16. ✅ [#28](https://github.com/RemiPelloux/kill-my-idea/issues/28) Deepdive: promotion axes
17. ✅ [#29](https://github.com/RemiPelloux/kill-my-idea/issues/29) Deepdive: branding

**Speed and docs**

18. ✅ [#14](https://github.com/RemiPelloux/kill-my-idea/issues/14) Cost and time in the report
19. ✅ [#16](https://github.com/RemiPelloux/kill-my-idea/issues/16) Parallel research by default
20. ✅ [#15](https://github.com/RemiPelloux/kill-my-idea/issues/15) Quick mode
21. ✅ [#17](https://github.com/RemiPelloux/kill-my-idea/issues/17) Write a "How scoring works" page
22. ✅ [#18](https://github.com/RemiPelloux/kill-my-idea/issues/18) Rubric-change process

**Freeze**

23. ✅ [#21](https://github.com/RemiPelloux/kill-my-idea/issues/21) Release checklist
24. ✅ [#19](https://github.com/RemiPelloux/kill-my-idea/issues/19) Compatibility promise
25. ✅ [#20](https://github.com/RemiPelloux/kill-my-idea/issues/20) Security review
26. ✅ [#22](https://github.com/RemiPelloux/kill-my-idea/issues/22) Gallery re-run

---

## Trust the score

The evidence: of 19 real runs (7 examples, 12 new runs in the gallery), **none scored GO**. The
12 gallery runs range from 43 to 58 (standard deviation 3.3), and 8 of them score exactly 49, 6 of
those because of the R6 cap. A score that never leaves 43–58 is not telling ideas apart.

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Idea types** | Ideas fail in different ways: a marketplace dies on liquidity, an app on App Store discovery, a content business on revenue per 1,000 views, a local business on location and permits. Today every idea gets the same 8 kill shots and metrics. | M | The skill classifies each idea as one of 7 types (SaaS, marketplace, mobile app, e-commerce, content or creator, service or agency, physical or local) and stores it as `idea.type`. Each type adds 1–2 type-specific checks and the metrics that matter for it (liquidity for a marketplace, RPM for content, a location's foot traffic for local). The checker validates the type and its checks. |
| **Smarter questions** | The verdict depends on facts only the founder knows: who pays and how much, an existing audience or customers, demand already validated, how fast they can ship. Today the skill asks at most 4 generic questions (country, budget, goal, edge), and headless runs asked none. | M | A question bank per idea type, chosen by impact: ask up to 8 questions, only those whose answer could move a sub-score by 1 point or more, or flip a kill shot, with likely answers as options. Answers go to `idea.answers`, each linked to the sub-scores it feeds. The report shows "Your answers" and the assumptions still open. The founder profile (BRAIN.md) still skips anything already known. |
| **Follow-up after research** | Some kill shots hinge on one fact the research can't find, like "do you already have 1,000 followers in this niche?". Today that becomes a silent assumption. | S | After research, when a kill shot or a capped rule depends on a founder fact, the skill asks at most 2 targeted follow-ups before scoring, then records which answer changed what ("no channel → channel clear, +6"). In headless mode they become explicit assumptions in the report. |
| **Calibration set** | Without known answers, nobody can tell whether a score is too harsh or too soft. | L | 10 ideas with a known outcome: 5 that clearly worked and 5 that clearly failed (Juicero, Quibi…). Each is scored "as of" its launch date, using only sources from before that date. The 5 that worked score a median of 60 or more, the 5 failures under 50, and at least one reaches GO. |
| **`scripts/calibrate.py`** | Clustering is only visible once you look at all runs together. | S | It prints the score distribution, how often each rule fired, and how often each kill shot hit, across any set of verdicts. CI runs it on the gallery. |
| **"Strong competitor" threshold** | It hit 13 of 14 gallery ideas. A kill shot that hits nearly everything tells you nothing. | M | The rubric defines "clear traction" with numbers (revenue, reviews or funding). **Result:** done, but it still hits 13 of 14 gallery ideas and 8 of 10 calibration ideas, successes included. Real markets almost always have a leader, so it stays as information with a mild cap (competitor density ≤ 3), documented in docs/scoring.md. |
| **Weights review** | R6 was needed because easy feasibility and fast first revenue lifted dead ideas above 50. | M | Feasibility and time to first revenue are re-weighted, or capped when Profit is 2 or lower. The change is checked against the calibration set, and the old and new scores are published in the changelog. |
| **Hindsight guard** | Scoring a famous company with today's sources leaks the outcome into the score. | S | Roast and calibration runs take an `as_of` date. Sources dated after it are flagged by the checker. |

## Stable formats and tests

| Item | Why | Effort | Done when |
|---|---|---|---|
| **`schema_version` everywhere** | Nothing in `idea.json`, `verdict.json`, `report-data.js` or `board-data.js` says which rules wrote it. Old reports are told apart today only by missing fields ("legacy" warnings). | M | Every file carries `schema_version`. `scripts/migrate.py` upgrades 0.7+ files, and the checker reports the version it validated. |
| **Test suite** | CI checks templates and examples but not the logic: rules R1–R6, rounding, the dashboard patterns and the export. | M | `python3 -m unittest` (stdlib only) covers check-idea (one fixture per rule, plus edge cases), build-brain (patterns, focus, keeping the user's notes), export-standalone and update-csp, and it runs in CI. |
| **Golden runs** | A prompt or rubric change can shift every score without anyone noticing. | S | 5 gallery verdicts are frozen as fixtures. CI fails if the checker's recomputed score for them changes. |
| **No executable data by default** | SECURITY.md lists one known limitation: `report-data.js` is JavaScript written by the model. | M | The skill writes `report-data.json`, and a script embeds it as an inert `application/json` block (the export already does this). The default report contains no model-written script, and SECURITY.md's known limitation is closed. |
| **Regenerate the examples** | The two example reports only pass the checker in `--legacy` mode. | M | Every example passes the checker without `--legacy`. `--legacy` remains for users' old files only. |

## Go to market (deepdive)

A verdict says whether to build. When the idea survives, the next questions are who exactly to
sell to, with what message, where, and under what name. Deepdive already collects 15+ verbatim
customer quotes, the channels with their costs, and the competitors' positioning. Today that
evidence stops at the verdict.

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Personas** | "Small businesses" is not a customer. Deepdive's customer voice already holds the raw material. | M | 2–3 personas, each built from the customer-voice quotes and the ICP: role, context, the pain in their own words (verbatim, linked), what they use today and pay for it, the trigger that makes them look, objections, and where to reach them. Every field is sourced or marked as an estimate. A persona without at least 3 linked quotes is not written. Shown as cards in the report. |
| **Market strategy options** | There is usually more than one way in: a niche first, another country first, a service before the product, a partner channel. Today only the rescue paths hint at this. | M | 2–3 strategies (for example: beachhead niche, launch country, partner or reseller, service first). Each has the first customer segment, the entry channel, the price point, the cost to the first 10 customers and the risks, re-scored with the same rubric. One is recommended and the choice is explained. |
| **Promotion axes** | The pains ranked by frequency are the best ad and landing-page copy, and they are already in the data. | S | 3–5 messaging angles, each tied to a ranked pain and a persona, with a headline, a proof point (sourced), the channel it fits, and the competitor messages it must beat (quoted from their sites). Plus one landing-page outline for the 7-day test. |
| **Branding** | A name that is taken, or a position that copies the leader, costs months later. | M | A positioning statement (for whom, the category, the one difference, proof). 5 name ideas, each checked by search only: .com and local domain, a trademark search in the launch country's register, App Store and social handles, with the result and the date of the check. The tone of voice comes from how the personas talk. Nothing is registered or bought. |

## Faster, cheaper, clearer

The evidence: across the gallery runs, a kill run took a median of 6 minutes and $2.50 of plan usage (range $2.00–4.50).

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Cost and time in the report** | Users can't see what a run cost. | S | `verdict.json` records the duration and the number of searches. The report footer shows them. |
| **Quick mode** | Not every idea needs 20+ sources. | M | `--quick`: 10 sources, about half the time, and the confidence is forced to low and labelled as such. It is never used for a GO. |
| **Parallel research by default** | 16 of the 18 gallery runs used no subagent: all of their 16–23 searches ran one after another in the main thread. | M | The kill shots are searched by parallel subagents. **Result:** every gallery run now uses 4 subagents. The minimum source count rose from 4 to 36 (median 34 → 39.5), but the median run takes 7 minutes against 6. The speed target moves to after 1.0. |
| **"How scoring works" page** | The rules are spread across SKILL.md, the README and the report footnote. | S | One page with a worked example from raw score to rules to verdict, linked from the report. |
| **Rubric-change process** | Users will want to reweight the scores. | S | CONTRIBUTING explains how to propose a rubric change: run calibrate.py before and after, and include the diff. |

## Freeze

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Compatibility promise** | Users keep verdicts in their own repos. | S | The README states that 1.x reads every 1.x file and that migrate.py upgrades older ones. |
| **Security review** | The templates and scripts changed a lot between 0.5 and 0.12. | M | A fresh review of the report, the dashboard and the scripts, with the injection tests rerun and SECURITY.md updated. |
| **Release checklist** | Releases are manual today, and one v0.9.0 tag was briefly pushed on the wrong commit. | S | `scripts/release.py --check` verifies the version, the changelog entry, the pinned CSP, the tests and the tag before anything is pushed. |
| **Gallery re-run** | The public verdicts must match the 1.0 rules. | M | The gallery is rebuilt with 1.0, and calibrate.py's output is published next to it. |

## After 1.0

- **Faster runs:** the 30% speed target from #16. Measure where the 7 minutes go (subagent start-up, the research budget, report writing) before cutting.

## Not before 1.0

- A hosted web version, or anything with accounts or payment.
- More report languages beyond English and French (labels only, when someone asks).
- New kill shots, unless the calibration set shows a gap.
- Integrations (Notion, Linear and so on).

Ideas and feedback are welcome in [issues](https://github.com/RemiPelloux/kill-my-idea/issues).
