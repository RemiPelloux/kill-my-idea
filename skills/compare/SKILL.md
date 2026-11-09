---
name: compare
description: Rank all the ideas evaluated with kill-my-idea in this project, from their verdict.json files, and recommend which ONE to focus on this week. Use when the user says "compare my ideas", "which idea should I do", "rank my ideas", "what should I focus on", or has evaluated 2 or more ideas.
---

# Compare Ideas

1. **Find the verdicts.** Read every `ideas/*/verdict.json` (and `idea.json`) in the
   current project.
   - Fewer than 2 found → say so, and suggest `/kill-my-idea:kill`.
   - A verdict older than 90 days is **stale**: mark it and suggest `/kill-my-idea:deepdive`.
   - A verdict whose `confidence.level` is `low` is marked **low confidence**: its rank is
     provisional.
2. **Build the ranking table.** Sort by score, then by `time_to_first_revenue_weeks` (the
   faster one wins), then by confidence (`high` before `medium` before `low`).

   | # | Idea | Verdict | Score | Confidence | Best rescue (score, difficulty) | LTV : CAC | Break-even | Time to first revenue | Primary kill shot |
   |---|------|---------|-------|------------|----------------------------------|-----------|------------|-----------------------|-------------------|

   Read the values from `verdict.json`: `rescue[0]`, `metrics.ltv_cac`,
   `metrics.break_even_customers_per_month`, `metrics.time_to_first_revenue_weeks`,
   `primary_kill_shot`. A missing metric is `unknown`, never a guess. Mark a score that
   `rules_applied` capped ("69, capped: no channel"). Show the last `history` entry when a
   verdict changed ("42 → 47").
   Add a column per country when ideas target different markets.
3. **Decide like a co-founder:**
   - **Focus** on ONE idea this week, with the reason, its first action and a deadline.
     Prefer a lower score with `high` confidence over a higher score with `low` confidence,
     and say so.
   - **Pause:** what to park, and why. A NO-GO with a `doable` rescue path above 60 is a
     pause, not a kill.
   - **Kill:** NO-GOs that are still in `ideas/` and should be archived.
   - **Opportunity cost:** what the focus idea beats the others on, in one line.
4. **Write `ideas/RANKING.md`** with the table, the decision and today's date.
5. **Answer in chat** with the table and the decision. Keep it short.

Do not re-research the ideas. Only compare what the verdicts contain.
