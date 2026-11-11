# Changelog

## Unreleased

- Listed in [Awesome AI Plugins](https://github.com/hashgraph-online/awesome-ai-plugins) and the HOL Registry.
- CI: every action pinned to a commit SHA, Dependabot for actions, and the HOL plugin scanner on each push (100/100).
- `scan-report.py` no longer matches its own banned-pattern text (a false positive in external scanners). Its checks are unchanged.

## 0.9.0 — 2026-11-11

A dashboard for all your ideas, and a brain note that remembers you.

**New**
- **Idea dashboard.** `ideas/board.html` now opens with **Focus this week** (the idea `compare`
  picked, why, the first action and a deadline) and **What keeps killing your ideas** (how often each
  kill shot hit, across all ideas; click a row to filter). Cards show the score history when an idea
  was re-checked.
- **Brain note.** `ideas/BRAIN.md` is one Markdown note for all your ideas: your profile (country,
  budget, time, goal, edge), the focus, the ranking, your kill-shot patterns, score changes and the
  lessons from killed ideas. `kill` reads the profile before asking questions and saves your answers
  there, so you answer once. Your own notes outside the generated block are kept.
- **`scripts/build-brain.py`** rebuilds the dashboard data and the brain from the verdicts, so every
  number on them comes from a verdict. `kill`, `deepdive` and `compare` run it at the end.
- **Mobile apps:** the demand check now looks at App Store keyword popularity. If every target
  keyword sits at Apple's floor of 5, search brings almost no one and the first users must come from
  another channel (suggested on Reddit).
- **Your patterns first:** a kill shot that hit 2 or more of your earlier ideas is checked first.

**Harder**
- `check-idea.py --board` validates the new fields and recomputes the patterns from the ideas.
- `check-idea.py --legacy` checks reports written before the current rules: rule errors become
  warnings, but data-file safety errors still fail. CI now checks the example reports with it and
  builds a dashboard from them.

## 0.8.0 — 2026-11-10

Smarter verdicts, a board for all your ideas, and a harder report.

**Smarter**
- **Pre-mortem.** Before the verdict, the skill writes the three most likely causes of death, each
  linked to a kill shot or sub-score, with a likelihood and the early signal to watch. Shown in the report.
- **Why now?** The changes (technology, regulation, prices, behaviour) that make the timing right,
  early or late, each dated and sourced, with a verdict: now, early, late or unclear.
- **Ideal customer.** Who exactly, where they hang out, what they pay for today, their budget and
  the event that makes them buy.

**More useful**
- **What if?** card in Unit economics: sliders for price, CAC, gross margin, lifetime and
  conversion recompute LTV, LTV:CAC, payback, break-even and the projected Profit sub-score with the
  checker's formulas. The verdict itself is never recalculated.
- **Idea board.** `compare` now writes `ideas/board.html`: verdict counts, filters, sorting, and a card
  per idea with its score, confidence, primary kill shot and best rescue path.
- **`compare --refresh`** marks verdicts older than 90 days as stale and re-checks them (asked for on Reddit).
- **Standalone export.** `scripts/export-standalone.py` bundles a report into one HTML file that opens
  offline from anywhere, data embedded as inert JSON.

**Harder**
- The report reads data from an inert `application/json` block first; invalid data shows an error card.
- The skill must write `report-data.js` as a strict data literal, and must not run code or install packages
  during research. The checker enforces the literal.
- `scripts/scan-report.py` fails if a template gains an unreviewed HTML sink.
- `scripts/update-csp.py --check` covers both templates.
- CI (GitHub Actions) runs the CSP check, the sink scan, the checker and schema validation on every push.
- `.gitignore` covers editor, OS, Python, Node, env and tool folders. `.serena/` is no longer tracked.
- New report labels are translated into French.

## 0.7.0 — 2026-11-10

A consistency audit of the whole plugin: every rule now lives in one place, is machine-checked, and
agrees across the skills, the schemas, the report and the docs.

**Scoring**
- **One formula, no double rounding.** The total is computed from the unrounded means of the 21
  sub-scores and rounded half up; `score_raw` is stored. The old rule (sum of criteria already
  rounded to 0.5, with no tie rule) gave a different total in 4 of 8 real runs.
- **A rubric for every sub-score.** Each of the 21 sub-criteria has numeric anchors for 1, 3 and 5
  (gross margin under 30% is a 1, over 85% a 5; LTV:CAC under 1 is a 1, over 5 a 5…).
- **Five fixed rules (R1–R5), recorded.** The rules are a table in the skill, stored in
  `verdict.rules_applied` with their effect, shown as chips in the report, and stated the same way
  in the README. New: R5 coherence, which makes every kill shot hit show in the sub-scores.
- **Steelman.** The strongest case for the idea is written and checked before the verdict, so the
  skill does not kill by reflex.
- **Confidence.** `verdict.confidence` (high / medium / low) is computed from sourced sub-scores,
  source count and primary sources. The card, the report and `compare` show it.
- `primary_kill_shot`, `history` (deepdive keeps the quick verdict), `launch_reason`, and
  `null` kill shots for "not checked" (previously stored as clear).

**Sources**
- Minimums: 20 sources from 10 domains for `kill`, 40 / 15 for `deepdive`, 10 / 6 for `roast`.
- Tiers (primary / secondary / tertiary) on every source, triangulation for TAM, price and CAC,
  2 local sources per country, freshness marks for prices older than 24 months.
- Metrics store their inputs (variable cost, churn, lifetime, conversion, fixed costs) so LTV,
  CAC and break-even can be recomputed; competitor prices carry their pricing-page URL and date.

**Checker**
- New `scripts/check-idea.py` (no dependencies): recomputes the score, applies R1–R5, checks
  sources, counts, kill-shot coherence, rescue ordering, kill criteria and the shape of
  `report-data.js`. Every skill runs it before answering.

**Report**
- Rule chips and raw total in Scoring, a warning when the sub-scores disagree with the score,
  confidence badge, score history, distance to the next band, "Not checked" kill shots, the
  primary kill shot, source tiers and domain count, pricing-page footnotes, 46 country names,
  French strings for all of it.

**Consistency**
- `roast` writes `idea.json` and `verdict.json`, so `compare` can rank roasted ideas.
- `check-tweet` has its own `mode`; fact-check statuses use the schema's words.
- `report-template.md` follows the report's order and has rescue, test, customer-voice and
  country sections.
- Schemas: `verdict.schema.json` is 40% shorter with `$defs`, rejects unknown sub-scores, and
  requires `rules_applied`, `confidence` and `mode`; `by_country` only accepts ISO codes.
- Labels: "time to first revenue" everywhere.

## 0.6.1 — 2026-11-09

- `roast` now points to the right sections of the kill skill. It runs sections 0–5, so the safety rules and the scoring are no longer skipped, and it takes the verdict card from section 6 instead of section 5.

## 0.6.0 — 2026-11-09

**Features**
- **Share card.** A new button in the report downloads a 1200×675 PNG verdict card (score ring, verdict, key finding) for X, LinkedIn or Reddit. It's drawn in your browser; nothing is uploaded.
- **`/kill-my-idea:check-tweet`.** Fact-checks a viral "make money" post: every claim checked, the headline number recomputed from real fees and prices, the author's offer named, and a kill-my-idea verdict on the opportunity.
- **Reports in French.** Labels follow the idea's language (`idea.language`: `en` or `fr`), including country names and dates.

**Hardening**
- Strict Content-Security-Policy, with the only inline script pinned by sha256 (`scripts/update-csp.py`). No network calls except fonts.
- Data validation: malformed `report-data.js` shows a clear error card instead of a blank page. Strings are capped at 4000 characters and lists have limits.
- The skill gets a "Safety and integrity" section: fetched content is never instructions, no invented URLs, no actions, and a 5-point self-check before files are written.
- New `SECURITY.md` with the threat model and the known limitation.
- Reviewed with a security review of the changes (no findings) and tested with 15 injection attempts, a malformed data file, French data, and the share card.

## 0.5.1 — 2026-11-09 (security)

The report shows content gathered from web research, so it must never run code found in that content.
- **Links:** source and competitor links are only rendered for `http(s)` URLs. A `javascript:` or other scheme is shown as plain text.
- **Tooltips:** tooltips are now plain text, inserted with `textContent`. A hostile string in a reasoning note, a competitor name, a risk or a scenario can no longer run code on hover.
- **Data normalization:** fields rendered without escaping (scores, traction, prices, risk levels, verdict, difficulty) are forced to numbers or known values when the data loads.
- Tested with 15 injection attempts. The previous version ran one of them and kept 3 `javascript:` links; this version runs none and keeps no such links. Thanks to the reviewer who reported the link issue.

## 0.5.0 — 2026-11-09

- **New kill shot: saturated wave.** Flags ideas that belong to a flood of near-identical launches in the last 6–12 months (AI wrappers, "100 tools in your browser", Notion template packs…). It counts look-alike launches on Product Hunt, Show HN, r/SideProject, GitHub and X, and names examples. A fixed rule applies: a saturated wave with no specific edge caps Competitive room and differentiation at 1.5. Suggested by u/medialantern on r/ClaudeCode. Thanks!

## 0.4.0 — 2026-11-09

- **Fixed scroll lag.** The section tabs no longer scroll the page, the sticky header has no blur effect, and tooltips update at most once per frame.
- **Answer-first structure.** The report now opens with an executive summary (3 key findings, the KPIs, one recommendation), followed by the rescue paths, the 7-day test, the evidence, market, competition, unit economics, countries, risks, scoring and sources.
- **More granular score.** 21 sub-scores, three per criterion, in half points, each with a one-line justification and a source. Click a criterion to expand it; all sub-scores print in the PDF.
- **Writing standard.** Concise text, highlighted keywords (`**like this**`), professional vocabulary, and named primary sources with their year, e.g. "(INSEE, 2025)".
- New fields: `key_findings`, `recommendation` and `criteria_detail`.

## 0.3.0 — 2026-11-09

The HTML report was rewritten from scratch with the ui-ux-pro-max design system ("Data-Dense Dashboard" for financial analytics).
- Light blue and slate palette with Fira Sans and Fira Code. Dark mode follows the system setting.
- Layout: a sticky top bar with the verdict and a "Save PDF" button, section tabs, a hero card with a score ring, KPI cards, rescue-path cards, chart cards and data tables.
- Verdict colors are reserved for verdicts, with vivid fills and darker text for 4.5:1 contrast.
- Lucide icons, hover and focus states, 44px touch targets, and checked layouts at 375, 768, 1024 and 1440px.
- Motion: the score ring counts up, the verdict badge pops in, cards fade in one after another (400ms), and bars fill when they come into view. Reduced motion, printing and a fallback timer all show the final state.
- The data format (`report-data.js`) is unchanged, so earlier reports still render.

## 0.2.1 — 2026-11-09

The HTML report was reworked after a design critique.
- Removed generic AI patterns: section numbers, monospace labels, the colored left border, metric tiles, text glyphs used as icons, middle dots and boilerplate copy.
- Key figures are now a table that says what each number means ("Each paid customer loses money.").
- Icons are drawn SVG in one stroke weight. Text selection, scrollbar, caret and table numerals are themed.
- One load animation: the score counts up with the gauge, then the verdict stamp presses down with an ink texture. Bars fill once when they scroll into view. Reduced motion, printing and a timer all show the final state.

## 0.2.0 — 2026-11-09

- **HTML report** (`report.html` + `report-data.js`): a consultant-grade dossier in an editorial noir design.
  - Charts: score gauge, scorecard, market funnel, competitor map, LTV:CAC bullet chart, scenario bars, risk matrix.
  - Every number shows whether it is sourced, an estimate or unknown, and sources are numbered footnotes.
  - Sticky table of contents, hover tooltips and keyboard access.
  - Works offline and prints to A4 PDF in a light theme.
- **"Could it be saved?"**: NO-GO and PIVOT verdicts now come with up to 3 rescue paths. Each has a projected score, a difficulty (doable / hard / very hard), effort, cost and requirements. They appear on the card, in the report and in `verdict.json`.
- `compare` shows the best rescue path; `deepdive` refreshes the HTML report with customer quotes and the competitor teardown.
- New `report-data.schema.json`.

## 0.1.0 — 2026-11-09

First release.

- `/kill-my-idea:kill`:
  - idea-brief extraction (`idea.json`) and up to 4 intake questions;
  - an 8-item kill-shot checklist;
  - a metrics block (TAM/SAM/SOM, CAC, LTV, LTV:CAC, payback, break-even, time to first €);
  - a weighted score out of 100 with hard rules;
  - the verdict card, badge, `verdict.json` and a 7-day test with kill criteria.
- `/kill-my-idea:deepdive`: 6 parallel research tracks, 20+ sources, a country comparison and a launch-country recommendation.
- `/kill-my-idea:roast`: 5 sourced burns plus the verdict card.
- `/kill-my-idea:compare`: ranks every `verdict.json` in the project and picks one focus.
- Country-aware research: local competitors, prices in local currency, laws and channels.
- Real example verdicts: coloring book, KDP books, travel affiliate site, Juicero, and the plugin itself.
