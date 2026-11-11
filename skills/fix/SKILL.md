---
name: fix
description: Find the smallest set of changes that would take an idea with a kill-my-idea verdict to GO (70+), and say honestly when it can't get there. It re-prices the idea against the competitors' price pages, picks the must-have features and the one difference from competitor gaps and customer complaints, and changes the customer, channel, model or country where the evidence says so. Each change lists its prerequisites (skills, money, time, partners, legal) and the sub-scores it moves; the fixed idea is re-scored with the same rubric and rules, as a projection. Use when the user says "fix my idea", "how do I make it a GO", "what would make this work", "path to GO", "what should I change", "what price should I charge", or runs /kill-my-idea:fix after a kill or deepdive.
---

# Fix

`kill` says what's wrong. `fix` says what to change, what each change takes, and how far that gets
the score. It works from evidence, and when no honest set of changes reaches 70 it says so and
shows the best score within reach. It never edits the verdict: the fixed score is a projection.

`${CLAUDE_PLUGIN_ROOT}` is the plugin folder. Safety rules §0, source rules §3, the rubric and the
fixed rules §5 of `${CLAUDE_PLUGIN_ROOT}/skills/kill/SKILL.md` apply.

## Steps

1. **Load the idea.** `ideas/*-<slug>/` with `idea.json`, `verdict.json` and `report-data.json`
   (competitors, customer voice and personas from a deepdive live in its `narrative`), and
   `ideas/BRAIN.md` when it exists (skills, budget, time). No verdict → run `/kill-my-idea:kill` first.
2. **Find where the points go.** Each sub-score loses `weight × (5 − score) / 15` points (the
   criterion's weight, 3 sub-scores per criterion); start from the biggest losses. Also list the rules that cut the total (R2 caps at 69, R6 at 49,
   R7 takes 10 and caps at 49): lifting a rule is often worth more than any sub-score.
3. **Research the levers** (at most 10 searches and 5 page fetches, 2 subagents in parallel when
   available, in the foreground). Reuse the verdict's sources first.
   - **Price:** the current price page of at least 3 competitors (amount, period, date). Pick a
     position, `undercut`, `match` or `premium`, and justify it with margin and LTV:CAC.
   - **Features:** the must-haves (what customers complain is missing, with a link to the
     complaint or review), what to cut, and the one difference competitors don't have.
   - **Customer, channel, model, country, cost:** only where the evidence supports a change.
4. **Choose the levers** (1–6), the smallest set that gets the furthest. For each:
   - `change` in one line, `evidence` and its `source`;
   - `moves`: each sub-score it changes, `from` (the verdict's score, exactly) `to`, with why.
     Use the rubric anchors in kill skill §5. One lever per sub-score;
   - `clears`: the kill shots it removes (they must have hit in the verdict);
   - `prerequisites`: what it takes, each with `kind` (skill, money, time, partner, legal, data,
     audience), `cost`, and `have` (`yes`, `no`, `unknown` from what the user said or BRAIN.md);
   - `difficulty` (doable, hard, very-hard as in kill skill §7), `effort`, `cost`.
5. **Re-score the fixed idea.** Copy all 21 sub-scores from the verdict, apply the moves, write
   the notes for the ones that moved, set `kill_shots` (a cleared one becomes `false`), apply
   the fixed rules again (`rules_applied`, with R5 coherence), update `metrics.ltv_cac` when a
   lever changes it, then compute `score_raw`, `score` and `verdict` with the §5 formula.
   - `reachable` is `true` only when the projected score is 70 or more.
   - Not reachable → `blockers`: what still stands in the way (founder fit, a market with a
     dominant free option, a channel only a team could run…). **Never stretch a sub-score to
     reach 70.** A 62 with honest blockers is the right answer when that's what the evidence says.
6. **Plan and kill criteria.** 3–7 steps in order (`when`, `step`, `verify` with a number), the
   cheapest proof first. Kill criteria with a number and a date.
7. **Write `fix.json`** (format below), then run
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/fix-kit.py" ideas/<folder>`. It refuses a sub-score that
   changed without a lever, a `from` that isn't the verdict's, a price position that doesn't
   match the competitor prices, and a score that doesn't recompute. Fix every error and rerun.
   When it passes it adds the "Path to GO" section to `report.html` (or "How close it can get").
8. **Write `fix.md`** next to the report: the fixed idea in one line, score before → after
   (projected), the levers in order with their prerequisites, the price table, the features,
   the plan, the kill criteria, the blockers, and the sources with access dates.
9. **Answer in chat**, short: before → after (projected) and whether GO is reachable; the 2 levers
   worth the most points, each with what you need first; the recommended price against the
   competitors; the first step of the plan. End with: "Build it: `/kill-my-idea:build --fix`."

Never publish, buy, sign up or contact anyone. Never change `verdict.json` or `idea.json`.

## fix.json

```json
{
  "schema_version": "1.0",
  "slug": "<verdict.slug>",
  "generated": "YYYY-MM-DD",
  "based_on": {"verdict": "<copied>", "score": 0},
  "summary": "<the fixed idea in one line>",
  "pricing": {
    "current": {"amount": 0, "currency": "USD", "period": "month"},
    "competitors": [{"name": "", "amount": 0, "period": "month", "source": "<pricing page>", "as_of": "YYYY-MM-DD"}],
    "recommended": {"amount": 0, "period": "month", "position": "undercut | match | premium", "why": ""}
  },
  "features": {
    "must": [{"feature": "", "why": "", "source": ""}],
    "cut": [{"feature": "", "why": ""}],
    "differentiator": {"feature": "", "why": "", "source": ""}
  },
  "levers": [{
    "id": "L1", "kind": "price | features | customer | channel | model | country | cost | other",
    "change": "", "evidence": "", "source": "", "difficulty": "doable", "effort": "", "cost": "",
    "moves": [{"sub": "<one of the 21 sub-score keys>", "from": 2, "to": 3.5, "why": ""}],
    "clears": ["<kill shot key>"],
    "prerequisites": [{"what": "", "kind": "skill", "cost": "", "have": "yes | no | unknown"}]
  }],
  "fixed": {
    "criteria_detail": {"<the 21 sub-scores, verdict.json format>": {}},
    "kill_shots": {"<the 8 kill shots>": false},
    "rules_applied": [],
    "metrics": {"ltv_cac": {"value": 0, "basis": "estimate", "reasoning": ""}},
    "score": 0, "score_raw": 0.0, "verdict": "GO | PIVOT | NO-GO"
  },
  "reachable": false,
  "blockers": [""],
  "plan": [{"when": "Week 1", "step": "", "verify": "<with a number>"}],
  "kill_criteria": ["<with a number and a date>"]
}
```

Plain text in every string. Price competitors compare per the same `period`. Every URL is one you
found or fetched.
