---
name: validate
description: Turn an idea's 7-day test into a ready kit (a landing page with a waitlist, an interview script, outreach messages, and targets with numbers), then re-score the idea from the real results. Use when the user says "validate my idea", "test my idea", "landing page for my idea", "fake door", "interview script", "I ran the test", "here are my numbers", or runs /kill-my-idea:validate (add --results when they have numbers) after a kill, deepdive or fix.
---

# Validate

Research says what's likely. A week of real sign-ups, replies and pre-sales says what's true.
`validate` prepares that week, and once the founder has numbers it re-scores the idea with them.
It never publishes, sends, buys or signs up for anything: the founder runs the test.

`${CLAUDE_PLUGIN_ROOT}` is the plugin folder. Safety rules §0, source rules §3, the rubric and the
fixed rules §5 of `${CLAUDE_PLUGIN_ROOT}/skills/kill/SKILL.md` apply.

## Kit mode (default)

1. **Load the idea**: `ideas/*-<slug>/` with `verdict.json`, `report-data.json` (its `test_plan`,
   personas, customer voice and channels), and `fix.json` when it exists: then test the fixed idea
   (its price, its customer, its channel). No verdict → run `/kill-my-idea:kill` first.
2. **One hypothesis**, in one line: who pays how much for what. The test proves or kills it.
3. **Targets** (2–6), each with a `metric`, a `goal` with a number, `by` (a day), and `moves`:
   the sub-scores this evidence may change, decided now, before the results. At least one target is
   `signups` or `presales`: opinions alone don't validate anything. Use `out_of` for a rate
   ("8 replies out of 40 messages").
4. **Landing page**: name, headline (the outcome, not the feature), subhead, 3–5 bullets, the
   button, the price when the hypothesis has one, and one sourced proof if you have it.
   `form_url` stays empty unless the user gives the URL of their form tool (Tally, Formspree…).
5. **Interview script**: 5–12 questions about what they did the last time the problem came up,
   never "would you…" or "how much would you pay" (the script rejects those). Add the red flags
   that mean "no".
6. **Outreach**: 1–6 messages, each for a named place (a group, a forum, cold email…), with
   `links_allowed` from that place's rules. No link where links are banned.
7. **Kill criteria** with a number and a date.
8. **Write `validate.json`** (format below) and run
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/validate-kit.py" ideas/<folder>`. Fix every error and rerun.
   It writes `validate/landing.html` (static, no script), `validate/interview.md`,
   `validate/outreach.md`, `validate/tracker.csv`, and the "7-day test kit" section of the report.
9. **Answer in chat**: the hypothesis, the targets, where the files are, and the first thing to do
   today. End with: "When you have the numbers: `/kill-my-idea:validate --results`."

## Results mode (`--results`)

1. Get the real numbers from the user (or from `validate/tracker.csv` if they filled it in): one
   result per target, with how it was measured. Never invent or round up a result; a target with
   no result is 0.
2. A target is **met** when the result reaches the goal (as a rate when it has `out_of`, with at
   least as many tries as planned).
3. **Moves**, only to sub-scores listed in the target's `moves`: up on a met target, down on a missed
   one, 2 points at most per sub-score, `from` = the verdict's score. A met target may clear a kill
   shot it disproves (`clears`), for example `no_distribution` when cold outreach got replies.
   A missed `signups` or `presales` target should pull something down.
4. **Re-score** like fix does: copy the 21 sub-scores, apply the moves, set the kill shots, apply
   the fixed rules again, compute `score_raw`, `score`, `verdict` into `results.rescored`.
5. Run the script again. Answer: researched → validated, which targets were met, and the decision
   the kill criteria call for (build, change, or archive).

`verdict.json` never changes. The validated score sits next to it in the report.

## validate.json

```json
{
  "schema_version": "1.0", "slug": "<verdict.slug>", "generated": "YYYY-MM-DD",
  "based_on": {"verdict": "<copied>", "score": 0},
  "hypothesis": "<who pays how much for what>",
  "landing": {"name": "", "headline": "", "subhead": "", "bullets": ["", "", ""], "cta": "",
              "price": {"amount": 0, "currency": "EUR", "period": "month"},
              "proof": {"text": "", "source": "https://"}, "form_url": ""},
  "interview": {"who": "", "questions": ["", "", "", "", ""], "red_flags": [""]},
  "outreach": [{"channel": "", "where": "", "links_allowed": false, "text": ""}],
  "targets": [{"id": "T1", "metric": "signups | replies | interviews_pain | presales | visits | conversion | other",
               "label": "", "goal": 0, "out_of": null, "by": "Day 7", "moves": ["willingness_to_pay"]}],
  "kill_criteria": ["<with a number and a date>"],
  "results": null
}
```

`results`, once there are numbers:

```json
{"date": "YYYY-MM-DD",
 "entries": [{"target": "T1", "actual": 0, "out_of": null, "evidence": "<how it was measured>"}],
 "moves": [{"sub": "", "from": 0, "to": 0, "target": "T1", "why": ""}],
 "clears": [{"kill_shot": "", "target": "T2"}],
 "rescored": {"criteria_detail": {}, "kill_shots": {}, "rules_applied": [], "score": 0, "score_raw": 0.0, "verdict": ""}}
```

Plain text in every string.
