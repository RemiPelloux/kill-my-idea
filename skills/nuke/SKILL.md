---
name: nuke
description: Run every kill-my-idea step on one idea in a single command - kill, a deep dive when it scores a PIVOT, fix (the path to GO), the 7-day test kit, the starter kit, and the share drafts - then write NUKE.md, one page that ties it all together. Stops after fix when even the fixed idea stays under 50, unless the user wants to go on. Use when the user says "nuke my idea", "do everything", "the full run", "run it all", "full pipeline", or runs /kill-my-idea:nuke.
---

# Nuke

One command, the whole pipeline, one folder. Each step is the existing skill, run as written: read
its SKILL.md and follow it. Nothing is copied or shortened here, and nuke adds only the order, the
stop rule and the summary.

`${CLAUDE_PLUGIN_ROOT}` is the plugin folder.

## Before starting

Say what the run does and what it costs, then ask once (in a headless run, "Just go" counts as yes):

> Full run: kill, a deep dive if it scores 50 to 69, fix, a 7-day test kit, a starter kit and post
> drafts. About 15 to 25 minutes and $5 to $10 of plan usage on Opus. Nothing is published, bought
> or sent. Go?

Ask the kill skill's questions (country, budget, goal…) in the same message, so the run doesn't
stop again. Note the start time.

## The steps, in order

1. **kill**: `${CLAUDE_PLUGIN_ROOT}/skills/kill/SKILL.md`. Write down `kill_score`, the score it gives.
2. **deepdive**, only when `kill_score` is 50 to 69 (a PIVOT, where more evidence can change the
   verdict): `${CLAUDE_PLUGIN_ROOT}/skills/deepdive/SKILL.md`. Otherwise `skipped`, with why.
3. **fix**: `${CLAUDE_PLUGIN_ROOT}/skills/fix/SKILL.md`, unless the verdict is already a GO (`skipped`).
4. **Stop rule.** When the fixed idea still projects under 50, stop here: mark validate, build and
   share `stopped` with why, and ask the user whether to go on anyway. If they say yes, set
   `continued_past_stop: true` and `continued_why`. In a headless run, stop.
5. **validate** (kit mode): `${CLAUDE_PLUGIN_ROOT}/skills/validate/SKILL.md`. Test the fixed idea
   when there is one.
6. **build**: `${CLAUDE_PLUGIN_ROOT}/skills/build/SKILL.md`, with `--fix` when fix ran.
7. **share**: `${CLAUDE_PLUGIN_ROOT}/skills/share/SKILL.md`. Posts for the places the user named, or
   one fitting subreddit and X.

Each step's own script must pass before the next step starts. A step that fails twice is `stopped`
with the error as why, and so is everything after it.

## Finish

1. Write `nuke.json` (format below), with `minutes` and `cost_usd` when you know them (else `null`).
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/nuke-kit.py" ideas/<folder>`. It checks the run
   against the rules above and every step's file against its own checker, then writes `NUKE.md`
   and the "Full run" section at the top of the report. Fix every error and rerun.
3. **Answer in chat**, short: the verdict card from kill, then one line per step (the fixed score
   and whether GO is reachable, the test's hypothesis and first target, the kit's name and key
   metric, where the posts are), then the one thing to do today. Point to `NUKE.md` and
   `report.html`.

## nuke.json

```json
{
  "schema_version": "1.0", "slug": "<verdict.slug>", "generated": "YYYY-MM-DD",
  "kill_score": 0,
  "steps": [
    {"step": "kill", "status": "done", "why": ""},
    {"step": "deepdive", "status": "done | skipped", "why": ""},
    {"step": "fix", "status": "done | skipped", "why": ""},
    {"step": "validate", "status": "done | skipped | stopped", "why": ""},
    {"step": "build", "status": "done | skipped | stopped", "why": ""},
    {"step": "share", "status": "done | skipped | stopped", "why": ""}
  ],
  "continued_past_stop": null, "continued_why": "",
  "minutes": null, "cost_usd": null
}
```

`why` is required for every step that isn't done.
