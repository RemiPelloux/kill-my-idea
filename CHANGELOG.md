# Changelog

## 1.1.0 — 2026-11-11

- **New skill, `/kill-my-idea:build`:** turns an idea that has a verdict (or one of its rescue paths)
  into a starter kit in `ideas/<folder>/build/`: README, `CLAUDE.md` for an agent building it,
  `.env.example`, the folder structure and starter files, a PRD, architecture, decision log and test
  plan, user stories with acceptance criteria, 3–5 sprints (sprint 0 is the verdict's 7-day test, not
  code), a Definition of Done, a 12-month business plan with 3 scenarios, brand tokens, a 15–30 s
  video storyboard and 3–9 creative ads, each with a target cost per customer. Any verdict can be
  built; a NO-GO kit says so at the top.
- **Pelloux guidelines in every kit:** `build/pelloux-guidelines.md` (think of 3 approaches and pick the
  simplest, size limits, surgical changes, Make/Test/Document) is copied into every kit, and the
  check fails when `build/CLAUDE.md` doesn't tell the agent to follow it.
- **SmartTest in every kit:** the README, test plan and guidelines set up
  [SmartTest](https://github.com/RemiPelloux/SmarttyTest) (`@tkmremi/smarttest` 1.2.0), so only the
  tests a change can affect run, on every commit through its pre-commit hook. Starter tests are laid
  out so its runner collects them (Python: `pyproject.toml` + `tests/__init__.py`).
- **The numbers are computed, not written:** the model writes `build/plan.json`
  ([schema](skills/build/build-plan.schema.json)); `scripts/build-kit.py` checks it against
  `verdict.json` (inputs marked `verdict` must equal the metric, an ad's target CPA can't exceed a
  customer's lifetime gross profit, colours must pass contrast), does the projection, break-even and
  cash-needed math, and renders the docs and a CSV.
- **Video and ads with Remotion:** a fixed, pinned [Remotion](https://www.remotion.dev) template
  (4.0.538) reads only `video/src/props.json`. `npm run video` renders the promo MP4, `npm run ads`
  one PNG per ad. The model never writes the video code.
- **Example:** the UGC agency gallery idea (PIVOT 56), built from rescue path 1 in one Opus run
  (6 minutes, $1.95): [examples/ugc-agency-build](examples/ugc-agency-build/build/BUILD.md), with
  the rendered video and ads in `media/`.
- 19 new unit tests (69 in all); CI checks every example build kit.

## 1.0.0 — 2026-11-11

The 1.0 quality bar from the [roadmap](ROADMAP.md) is met: a calibrated score, versioned formats,
tests in CI, no model-written code in the default report, and a go-to-market plan in deepdive.
From here, 1.x reads every 1.x file, and a breaking format change needs 2.0.

- **Gallery re-run with the 1.0 rules:** all 14 ideas were re-run on Opus with 4 parallel research
  agents. 12 are NO-GO and 2 are PIVOT (UGC agency 56, dental AI receptionist 51), from 39 to 56.
  Every report passes the checker. `calibrate.py`'s output is published next to the gallery as
  `docs/gallery/calibration.txt`.
- **Examples regenerated:** the Notion and wedding-speech reports are fresh 1.0 runs that pass the
  checker without `--legacy`. Notion moves from PIVOT 55 to **NO-GO 43** and wedding speeches from
  48 to **NO-GO 44**: R6 and R7 now catch models that lose money on every customer. The README,
  the verdict wall, the hero image and the report screenshots follow. CI no longer needs the
  legacy step.
- **"Full verdict" badge:** a normal kill run was labelled "Quick verdict", easy to confuse with
  `--quick` mode. It now reads "Full verdict" ("Verdict complet" in French). The CSP hash is
  re-pinned.
- **Strong competitor is information:** even with a traction number required, it hits 13 of 14
  gallery ideas and 8 of 10 calibration ideas, successes included. It keeps its mild cap
  (competitor density ≤ 3) and [How scoring works](docs/scoring.md) says why. The worked example
  there uses the new pet-dropshipping run (51 raw, R7, **41**).
- **Run time:** parallel research raised the minimum sources per run from 4 to 36, but the median
  run takes 7 minutes (6 before). The speed target moves to after 1.0.

## 0.11.1 — 2026-11-11

- **Research agents run in the foreground:** kill and deepdive wait for their research subagents
  instead of starting them in the background. In the background, a run ended its turn and was woken
  once per agent (5 stops in one calibration run), which looked like the session closing and
  reopening and cost extra tokens.

## 0.11.0 — 2026-11-11

- **Calibration set:** 10 ideas with a known outcome, scored as of their launch date. Calendly,
  ConvertKit, Carrd, Plausible and Tally worked; Juicero, Quibi, Homejoy, Shyp and Washio failed. (#4)
- **New rule R7, an unprofitable model:** when Profit potential is 2 or less, the total loses 10
  points and is at most 49 (NO-GO). The calibration showed why: all 5 failures scored Profit 2.0 or
  less and all 5 successes 3.0 or more, but easy feasibility lifted the failures to 58–60. With R7
  the successes stay at 64–71 (Tally GO 71) and the failures drop to 39–49. All 3 calibration targets
  pass. Chosen over re-weighting, which moved the successes too. (#7)
- `calibrate.py` recomputes every score under today's rules, so older verdicts are judged by the
  current rules.
- The checker refuses a negative LTV:CAC (one calibration run wrote −0.68).
- Golden runs updated on purpose (all 5 have Profit 2 or less): 58 → 48, 49 → 39, 43 → 33, 53 → 43,
  49 → 47.

## 0.10.1 — 2026-11-11

- **Research budget:** each of the 4 research subagents runs at most 8 searches and 4 page fetches,
  and the main thread at most 8 more. Without it, the first calibration runs used 65–110 searches and
  cost about twice as much as a 0.9 run.
- **Calibration batch 1** (scored as of launch): Calendly 68, Carrd 64 (both worked), Juicero 49
  (failed).

## 0.10.0 — 2026-11-11

The code half of the 1.0.0 sprint: a versioned file format, reports with no executable data, idea
types and smarter questions, go to market in deepdive, calibration tooling, 48 tests and a security
review. 1.0.0 follows once the calibration set passes its targets.

- **Tests:** 25 stdlib unit tests for the checker rules (R1–R6, rounding, tampering, unsafe data),
  build-brain, the board check, the export and the CSP pins. CI runs them. (#10)
- **File format 1.0:** `idea.json`, `verdict.json`, `report-data` and `board-data.js` carry
  `schema_version`. `scripts/migrate.py` upgrades a folder that passes today's rules and lists the
  ones that need a re-run. The gallery is upgraded. (#9)
- **No executable data by default:** the skills write `report-data.json` (plain data) and
  `scripts/build-report.py` embeds it in `report.html` as an inert JSON block. The page runs no code
  written by the model, and one file is the whole report. The checker verifies that the page embeds
  exactly the data file. `report-data.js` stays only as the no-Bash fallback and for old reports
  (`migrate.py --json` converts them). The gallery is converted. SECURITY.md's known limitation is now
  limited to that fallback. (#12)
- **`scripts/calibrate.py`:** score spread, caps, rules fired and kill-shot hit rates across any set
  of verdicts, flags a kill shot that hits more than 2 ideas in 3, checks the 1.0 calibration targets
  (`--outcomes`) and rescores with other weights (`--weights`). CI prints it for the gallery. On the
  gallery today: 43–58, stdev 3.4, no GO; free alternative, strong competitor and no channel are
  flagged. (#5)
- **Hindsight guard:** `verdict.as_of` scores an idea as it looked on a past date (for example a
  famous company at launch). Only sources published by then may be used; the checker fails later
  ones and warns when most sources have no date. (#8)
- **Idea types:** every idea is classified as SaaS, marketplace, mobile app, e-commerce, content,
  service or local, and gets the 2 checks that kill that kind of business (liquidity for a
  marketplace, revenue per 1,000 views for content, permits and upfront cost for a local business…),
  stored in `verdict.type_checks` and shown in the report. (#23)
- **Smarter questions:** up to 8 questions instead of 4, picked from a bank by type, and only when the
  answer could move a sub-score by a point or flip a kill shot. Answers are saved in `idea.answers`
  with the sub-scores they feed, and the report shows them. (#24)
- **Follow-up after research:** at most 2 targeted questions when a kill shot hinges on a fact only
  the founder knows, with what each answer changed. Headless runs write them as assumptions. (#25)
- **"Strong competitor" needs proof of traction:** $1M+ revenue, 500+ reviews, $5M+ raised, 100k+
  users or a top-10 rank, with the number in the evidence. A crowded field without that proof lowers
  `competitor_density` instead. It hit 13 of 14 gallery ideas before. (#6, checked again at the gallery re-run)
- **Golden runs:** 5 real verdicts are frozen in `tests/golden/`. A rule change that moves their score
  fails CI until the golden file is updated on purpose. (#11)
- **Go to market in deepdive** (only for an idea that survives, score or best rescue 50+), built
  from the evidence already gathered and shown in a new report section:
  - **personas** (2–3), each with at least 3 linked verbatim quotes, what they pay today, the trigger
    and where to reach them (#26);
  - **ways in** (2–3 strategies: niche, country, partner, service first), each re-scored, one
    recommended with its reason (#27);
  - **promotion angles** (3–5) tied to a ranked pain and a persona, with a sourced proof, the
    competitor messages to beat, and a landing page for the 7-day test (#28);
  - **branding**: a positioning statement, 5 names checked by search only (domains, the launch
    country's trademark register, handles, with the date), and the tone. Nothing is registered or
    bought (#29).
- **Cost and time in the report:** `verdict.run` records the minutes, searches, pages read and
  research agents, and the report footer shows them. (#14)
- **Quick mode** (`--quick`): 10 sources from 6 domains in about half the time, always low
  confidence, never a GO (capped at 69), labelled in the report. (#15)
- **Parallel research by default:** kill now starts 4 research subagents in one message instead of
  searching one query at a time. 16 of the 18 gallery runs had used none. (#16, measured at the gallery re-run)
- **[How scoring works](docs/scoring.md):** one page from sub-scores to rules to verdict, with a worked
  example (the pet store: raw 53.2 → R6 → 49), linked from the report. (#17)
- **Changing the scoring:** CONTRIBUTING explains how to propose a rubric or rule change: evidence
  from runs, calibrate.py before and after, golden runs updated on purpose. (#18)
- **Compatibility promise:** every 1.x release reads every 1.x file; pre-1.0 verdicts upgrade with
  migrate.py. (#19)
- **`scripts/release.py --check <version>`:** version, changelog, CSP, scan, tests, examples, git
  state and a free tag, checked before anything is tagged. It never tags itself. (#21)
- **Security review** of every 1.0 change (no XSS found in the new sections; 3 findings, fixed): (#20)
  - a hand-edited `report.html` is now a checker error, and a built report's CSP allows no script
    file at all (only the pinned inline script);
  - an idea title can no longer break or inject into `BRAIN.md` (markers, HTML and links are
    neutralised, and verdict/confidence are whitelisted);
  - `NaN`, `Infinity` and broken Unicode in report data are refused instead of producing a page the
    browser can't read.

## 0.9.1 — 2026-11-11

**Fixed: dead ideas scored as PIVOT.** Twelve real runs for the new gallery showed it: an idea with no
channel to customers that loses money on each one (LTV:CAC 0.11 to 0.95) still scored 50–59, because
easy feasibility and fast first revenue lifted the average. New fixed rule **R6**: no channel **and**
LTV:CAC below 1 caps the total at 49, a NO-GO. The checker and the report enforce it.

**New**
- **Gallery:** 14 real runs on popular side hustles, ranked on the dashboard
  (https://remipelloux.github.io/kill-my-idea/gallery/board.html). The 6 ideas R6 changed were re-run.
- **Demo video** (50 s) of a real run: every line in the terminal part comes from the run's log.
- On a shared board (`build-brain.py --no-brain`), the dashboard hides the empty "Focus this week" panel.

## 0.11.0 — 2026-11-11

- `build-brain.py --no-brain <dir>` builds the dashboard without writing `BRAIN.md`, for public galleries.
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
