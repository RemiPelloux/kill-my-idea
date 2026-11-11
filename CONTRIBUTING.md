# Contributing

Thanks for helping kill more bad ideas.

## Good contributions

- **New kill shots**: a check that has killed real ideas. Add it to the table in `skills/kill/SKILL.md` §3
  (with what counts as a hit and the searches to run), the R5 coherence rule in §5 if it maps to a sub-score,
  `kill_shots` in `skills/kill/verdict.schema.json`, `KILL_SHOTS` / `COHERENCE` in `scripts/check-idea.py`,
  `KS` (and its French label) in `skills/kill/report.html`, and the table in `skills/kill/report-template.md`.
- **Rubric anchors**: a sharper, sourced threshold for one of the 21 sub-scores (`SKILL.md` §5).
- **Country guides**: local competitors, channels, laws or payment habits that change verdicts.
- **Better metrics**: a formula or benchmark, with its source.
- **Real example verdicts**: your own idea, card + sources, in `examples/`.

## Rules

- Every number needs a source, or is labelled *(estimate)* with its reasoning.
- Keep the skills short and readable: they are prompts, so every line costs tokens.
- Test your change locally before opening a PR:

  ```sh
  claude plugin validate .
  claude --plugin-dir .   # then: kill my idea: <something>
  ```

- Changed `skills/kill/report.html`? Run `python3 scripts/update-csp.py` (it re-pins the CSP hash), then
  copy it over `docs/reports/*/index.html` and `examples/*/report.html` so the live reports match.
- Changed the scoring (weights, rubric, rules) in `skills/kill/SKILL.md`? Change `scripts/check-idea.py`,
  `skills/kill/verdict.schema.json` and the scoring note in `report.html` in the same PR: they must agree.
- Check a run with `python3 scripts/check-idea.py ideas/<folder>` (or `--all`). It must pass with no ERROR.
- Run the tests: `cd tests && python3 -m unittest`.

## Changing the scoring

Weights, rubric anchors and fixed rules decide every verdict, so a change needs evidence, not taste.

1. **Say what is wrong, with runs.** Name the verdicts that are off and why (for example: "6 ideas with
   no channel and LTV:CAC under 1 scored PIVOT"; that is how R6 was found).
2. **Measure before and after** with `python3 scripts/calibrate.py docs/gallery` (and
   `--outcomes calibration/outcomes.json` on the calibration set). For weights, try the change first:
   `--weights '{"feasibility": 15}'` rescores every verdict without a new run.
3. **Change the rule everywhere at once:** `skills/kill/SKILL.md` §5, `scripts/check-idea.py`,
   `skills/kill/verdict.schema.json`, the scoring note in `skills/kill/report.html`, and
   [`docs/scoring.md`](docs/scoring.md).
4. **Update the golden runs on purpose.** If `tests/test_golden.py` fails, the change moved real
   scores: update `EXPECTED` and list every moved score in the PR ("youtube-summary-extension 58 → 52").
5. **Put the calibrate output, before and after, in the PR description.** A change that makes the
   calibration targets worse is not merged.
- One change per PR, with a [Conventional Commit](https://www.conventionalcommits.org) title (`feat(kill): add pricing-page kill shot`).
