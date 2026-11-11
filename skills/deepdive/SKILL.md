---
name: deepdive
description: Deep-dive due diligence on a business idea, after or instead of a quick kill-my-idea verdict. It runs parallel research tracks (market size, competitor teardown, customer voice from reviews and forums, pricing, channels, regulation per country) with 40 or more sources, then updates the metrics, the score and the verdict. Use when the user says "deep dive", "go deeper", "full analysis", "due diligence", or wants more evidence before spending money on an idea.
---

# Deep Dive

The quick `kill` verdict is a smoke test. A deep dive is the due diligence you do before
spending real money or months of work. It follows every rule of
`${CLAUDE_PLUGIN_ROOT}/skills/kill/SKILL.md` (safety §0, source rules §3, metrics §4,
rubric and fixed rules §5) with higher minimums.

## Steps

1. **Load or create the idea.**
   - If `ideas/*-<slug>/idea.json` and `verdict.json` exist, read them. Keep the old
     `score`, `verdict`, `mode`, `evaluated` and source count: they go into `history`.
   - Otherwise run sections 1–2 of the kill skill first: the brief extraction and the
     questions. Country matters even more here.
2. **Run 6 research tracks in parallel**, one subagent each when available.
   - Every track returns its facts with source links (URL, title, publisher, date, tier),
     its estimates with their formula, and its unknowns.
   - Search in the language of each target country, on local sites.

   | Track | Must find |
   |-------|-----------|
   | Market | TAM / SAM / SOM from at least 2 independent sources (1 primary), growth rate, 5-year trend |
   | Competitor teardown | Top 10 (global + local): offer, price tiers from the pricing page (dated), traction (traffic, reviews, funding, headcount), positioning, weakest point |
   | Customer voice | 15 or more verbatim quotes or complaints from reviews (G2, Trustpilot, app stores, Amazon), Reddit or forums, grouped by pain and ranked by frequency. Exact words only, each with a link and a date |
   | Pricing | The price ladder in the market, willingness to pay, the most common model, and the price elasticity signals (discounts, churn complaints about price) |
   | Channels | 3 acquisition channels with a cost estimate (CPC, CPM, creator rates, from sourced benchmarks) and real examples of companies using them. Where the ICP gathers (communities, platforms, events). For a mobile app: App Store / Google Play keyword popularity for the target keywords (Apple's floor is 5: all keywords at 5 means search brings almost no one) |
   | Regulation & platform | Per-country laws, licences, taxes (VAT, OSS), terms-of-service risks, dependency on one platform, with links to the legal text or the platform page. Recent changes (tech, law, platform, price) for why now |

3. **Update the numbers.**
   - Recompute the metrics table (kill skill §4), one `by_country` set per country, and
     pick the `launch_country` with its `launch_reason`.
   - Re-score all 21 sub-scores with the rubric, the formula and the fixed rules.
   - Recompute `confidence`. A deep dive should reach `high`; if it doesn't, say why.
   - The verdict may change. Say what moved it, which sub-scores, and by how many points.
   - Rewrite the premortem, why now and ICP (kill skill §3 and §5) from the new evidence.
     Every premortem cause links to a kill shot or sub-score of the updated verdict.
4. **Write `deepdive.md`** next to `report.md`, with these sections:
   1. Updated card.
   2. What changed since the quick verdict (score before → after, the sub-scores that moved).
   3. Market, why now and ICP.
   4. Competitor teardown table.
   5. Customer voice: pains ranked by frequency, with quotes.
   6. Pricing ladder.
   7. Channels with costs.
   8. Country comparison and the launch country.
   9. Risks and premortem.
   10. Updated rescue paths, 7-day test and kill criteria.
   11. Sources: **at least 40 from 15 domains**, each with its tier and access date.
5. **Update `verdict.json` and the HTML report.**
   - In `verdict.json`: append the previous evaluation to `history`, set `mode` to
     `"deepdive"` and `evaluated` to today, and refresh the metrics, sub-scores, score,
     rules, confidence, rescue paths and sources.
   - Rewrite `report-data.json` (kill skill §6). Add `customer_voice`, the full competitor list
     with `price_low`, `price_source` and `traction`, the `by_country` breakdown, and the
     updated `premortem`, `why_now` and `icp`.
   - Rebuild `report.html` with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build-report.py" ideas/<folder>`
     (kill skill §6). An older folder with `report-data.js` is moved to JSON first with
     `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/migrate.py" --json ideas/<folder>`. The HTML then shows
     the deep-dive version, with the score history.
6. **Update the brain**: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/build-brain.py" ideas`
   when Bash is available (kill skill §8).
7. **Self-check** with `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-idea.py" ideas/<folder>`
   when Bash is available; fix every error before answering.
8. **Answer in chat**:
   - the updated card;
   - the score change ("42 → 47, because…") and the confidence level;
   - the 3 most surprising findings;
   - the launch country;
   - the path to `report.html` (open it in a browser) and to `deepdive.md`.

Evidence rules are the same as in the kill skill: every number is sourced or marked (estimate)
with its formula, unknowns stay unknown, quotes are verbatim. Never publish anything, spend
money, or contact anyone.
