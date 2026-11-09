---
name: deepdive
description: Deep-dive due diligence on a business idea, after or instead of a quick kill-my-idea verdict. It runs parallel research tracks (market size, competitor teardown, customer voice from reviews and forums, pricing, channels, regulation per country) with 20 or more sources, then updates the metrics, the score and the verdict. Use when the user says "deep dive", "go deeper", "full analysis", "due diligence", or wants more evidence before spending money on an idea.
---

# Deep Dive

The quick `kill` verdict is a smoke test. A deep dive is the due diligence you do before
spending real money or months of work.

## Steps

1. **Load or create the idea.**
   - If `ideas/*-<slug>/idea.json` and `verdict.json` exist, read them.
   - Otherwise run sections 1–2 of `${CLAUDE_PLUGIN_ROOT}/skills/kill/SKILL.md` first:
     the brief extraction and the questions. Country matters even more here.
2. **Run 6 research tracks in parallel**, one subagent each when available.
   - Every track returns its facts with source links, its estimates with their reasoning,
     and its unknowns.
   - Search in the language of each target country.

   | Track | Must find |
   |-------|-----------|
   | Market | TAM / SAM / SOM from at least 2 independent sources, growth rate, 5-year trend |
   | Competitor teardown | Top 5 (global + local): offer, price tiers, traction (traffic, reviews, funding, headcount), positioning, weakest point |
   | Customer voice | 15 or more real quotes or complaints from reviews (G2, Trustpilot, app stores, Amazon), Reddit or forums, grouped by pain. Exact words only, each with a link |
   | Pricing | The price ladder in the market, willingness to pay, the most common model |
   | Channels | 3 acquisition channels with a cost estimate (CPC, CPM, creator rates) and real examples of companies using them |
   | Regulation & platform | Per-country laws, licences, taxes (VAT, OSS), terms-of-service risks, dependency on one platform |

3. **Update the numbers.**
   - Recompute the metrics table (section 4 of the kill skill), one column per country.
   - Re-score with the same weights and hard rules.
   - A verdict may change. Say what moved it, and by how many points.
4. **Write `deepdive.md`** next to `report.md`, with these sections:
   1. Updated card.
   2. What changed since the quick verdict.
   3. Market.
   4. Competitor teardown table.
   5. Customer voice: pains ranked by frequency, with quotes.
   6. Pricing ladder.
   7. Channels with costs.
   8. Country comparison and a recommended launch country.
   9. Risks.
   10. Updated 7-day test and kill criteria.
   11. Sources (at least 20, each with its access date).
5. **Update `verdict.json` and the HTML report.**
   - In `verdict.json`: set `mode` to `"deepdive"`, and refresh the metrics, score, rescue paths and sources.
   - Rewrite `report-data.js` (kill skill §6). Add `customer_voice`, the full competitor list with
     `price_low` and `traction`, and the `by_country` breakdown.
   - Copy `report.html` from `${CLAUDE_PLUGIN_ROOT}/skills/kill/` if it isn't there yet.
     The HTML then shows the deep-dive version.
6. **Answer in chat**:
   - the updated card;
   - the score change ("42 → 47, because…");
   - the 3 most surprising findings;
   - the launch country;
   - the path to `report.html` (open it in a browser) and to `deepdive.md`.

Evidence rules are the same as in the kill skill: every number is sourced or marked (estimate),
unknowns stay unknown, quotes are verbatim. Never publish anything, spend money, or contact anyone.
