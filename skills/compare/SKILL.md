---
name: compare
description: Rank all the ideas evaluated with kill-my-idea in this project, from their verdict.json files, and recommend which ONE to focus on this week. Use when the user says "compare my ideas", "which idea should I do", "rank my ideas", "what should I focus on", or has evaluated 2 or more ideas.
---

# Compare Ideas

1. **Find the verdicts.** Read every `ideas/*/verdict.json` (and `idea.json`) in the
   current project.
   - Fewer than 2 found → say so, and suggest `/kill-my-idea:kill`.
2. **Build the ranking table.** Sort by score, then by time to first € (ties: the faster one wins).

   | # | Idea | Verdict | Score | LTV : CAC | Break-even | Time to first € | Biggest kill shot |
   |---|------|---------|-------|-----------|------------|-----------------|-------------------|

   Read the values from `verdict.json`. A missing metric is `unknown`, never a guess.
   Add a column per country when ideas target different markets.
3. **Decide like a co-founder:**
   - **Focus** on ONE idea this week, with the reason and its first action and a deadline.
   - **Pause:** what to park, and why.
   - **Kill:** NO-GOs that are still in `ideas/` and should be archived.
   - **Opportunity cost:** what the focus idea beats the others on, in one line.
4. **Write `ideas/RANKING.md`** with the table, the decision and today's date.
5. **Answer in chat** with the table and the decision. Keep it short.

Do not re-research the ideas. Only compare what the verdicts contain, and flag any verdict
older than 90 days as stale (suggest `/kill-my-idea:deepdive`).
