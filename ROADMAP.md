# Roadmap to 1.0.0

1.0.0 is a quality bar, not a date. All the work happens in **one sprint**, the [1.0.0 sprint](https://github.com/RemiPelloux/kill-my-idea/milestone/4) milestone (19 issues), and 1.0.0 ships when it is closed.

**What 1.0 means**

1. **You can trust the score.** It separates good ideas from bad ones on a known test set, and a GO is reachable.
2. **The formats are stable.** Every file has a versioned schema. After 1.0, a breaking change needs a major version.
3. **Everything is tested.** The scripts and the rules have tests in CI, not only the example runs.
4. **Nothing in the default output runs code** written by the model.

Each item below has why (the evidence), effort (S = under a day, M = a few days, L = a week or more) and done when.

---

## Work order

Do the items top to bottom; each one builds on the ones before it. The paid steps (the calibration
set, the regenerated examples and the gallery re-run) are real runs: at most 3 at a time, with the cost stated first.

**Foundations: build what everything else needs**

1. [#10](https://github.com/RemiPelloux/kill-my-idea/issues/10) Test suite
2. [#9](https://github.com/RemiPelloux/kill-my-idea/issues/9) Add schema_version to every file
3. [#12](https://github.com/RemiPelloux/kill-my-idea/issues/12) No executable data by default
4. [#5](https://github.com/RemiPelloux/kill-my-idea/issues/5) Add scripts/calibrate.py
5. [#8](https://github.com/RemiPelloux/kill-my-idea/issues/8) Hindsight guard

**The score: calibrate it, then freeze it**

6. [#4](https://github.com/RemiPelloux/kill-my-idea/issues/4) Calibration set
7. [#6](https://github.com/RemiPelloux/kill-my-idea/issues/6) Strong competitor threshold
8. [#7](https://github.com/RemiPelloux/kill-my-idea/issues/7) Weights review
9. [#11](https://github.com/RemiPelloux/kill-my-idea/issues/11) Golden runs
10. [#13](https://github.com/RemiPelloux/kill-my-idea/issues/13) Regenerate the examples

**Speed and docs**

11. [#14](https://github.com/RemiPelloux/kill-my-idea/issues/14) Cost and time in the report
12. [#16](https://github.com/RemiPelloux/kill-my-idea/issues/16) Parallel research by default
13. [#15](https://github.com/RemiPelloux/kill-my-idea/issues/15) Quick mode
14. [#17](https://github.com/RemiPelloux/kill-my-idea/issues/17) Write a "How scoring works" page
15. [#18](https://github.com/RemiPelloux/kill-my-idea/issues/18) Rubric-change process

**Freeze**

16. [#21](https://github.com/RemiPelloux/kill-my-idea/issues/21) Release checklist
17. [#19](https://github.com/RemiPelloux/kill-my-idea/issues/19) Compatibility promise
18. [#20](https://github.com/RemiPelloux/kill-my-idea/issues/20) Security review
19. [#22](https://github.com/RemiPelloux/kill-my-idea/issues/22) Gallery re-run

---

## Trust the score

The evidence: of 19 real runs (7 examples, 12 new runs in the gallery), **none scored GO**. The
12 gallery runs range from 43 to 58 (standard deviation 3.3), and 8 of them score exactly 49, 6 of
those because of the R6 cap. A score that never leaves 43–58 is not telling ideas apart.

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Calibration set** | Without known answers, nobody can tell whether a score is too harsh or too soft. | L | 10 ideas with a known outcome: 5 that clearly worked and 5 that clearly failed (Juicero, Quibi…). Each is scored "as of" its launch date, using only sources from before that date. The 5 that worked score a median of 60 or more, the 5 failures under 50, and at least one reaches GO. |
| **`scripts/calibrate.py`** | Clustering is only visible once you look at all runs together. | S | It prints the score distribution, how often each rule fired, and how often each kill shot hit, across any set of verdicts. CI runs it on the gallery. |
| **"Strong competitor" threshold** | It hit 13 of 14 gallery ideas. A kill shot that hits nearly everything tells you nothing. | M | The rubric defines "clear traction" with numbers (revenue, reviews or funding). On the gallery it hits at most 2 of every 3 ideas. |
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

## Faster, cheaper, clearer

The evidence: across the gallery runs, a kill run took a median of 6 minutes and $2.50 of plan usage (range $2.00–4.50).

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Cost and time in the report** | Users can't see what a run cost. | S | `verdict.json` records the duration and the number of searches. The report footer shows them. |
| **Quick mode** | Not every idea needs 20+ sources. | M | `--quick`: 10 sources, about half the time, and the confidence is forced to low and labelled as such. It is never used for a GO. |
| **Parallel research by default** | 16 of the 18 gallery runs used no subagent: all of their 16–23 searches ran one after another in the main thread. | M | The kill shots are searched by parallel subagents. The median run time drops by at least 30% at the same source count. |
| **"How scoring works" page** | The rules are spread across SKILL.md, the README and the report footnote. | S | One page with a worked example from raw score to rules to verdict, linked from the report. |
| **Rubric-change process** | Users will want to reweight the scores. | S | CONTRIBUTING explains how to propose a rubric change: run calibrate.py before and after, and include the diff. |

## Freeze

| Item | Why | Effort | Done when |
|---|---|---|---|
| **Compatibility promise** | Users keep verdicts in their own repos. | S | The README states that 1.x reads every 1.x file and that migrate.py upgrades older ones. |
| **Security review** | The templates and scripts changed a lot between 0.5 and 0.12. | M | A fresh review of the report, the dashboard and the scripts, with the injection tests rerun and SECURITY.md updated. |
| **Release checklist** | Releases are manual today, and one v0.9.0 tag was briefly pushed on the wrong commit. | S | `scripts/release.py --check` verifies the version, the changelog entry, the pinned CSP, the tests and the tag before anything is pushed. |
| **Gallery re-run** | The public verdicts must match the 1.0 rules. | M | The gallery is rebuilt with 1.0, and calibrate.py's output is published next to it. |

## Not before 1.0

- A hosted web version, or anything with accounts or payment.
- More report languages beyond English and French (labels only, when someone asks).
- New kill shots, unless the calibration set shows a gap.
- Integrations (Notion, Linear and so on).

Ideas and feedback are welcome in [issues](https://github.com/RemiPelloux/kill-my-idea/issues).
