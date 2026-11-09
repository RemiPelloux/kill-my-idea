# Changelog

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
