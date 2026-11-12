---
name: share
description: Turn a kill-my-idea verdict into a verdict card image and ready-to-post drafts for Reddit, X, LinkedIn or Hacker News, each written for that place's rules (no link where links are banned, length limits, no lessons section). Use when the user says "share my verdict", "post this", "make a post", "write a Reddit post about it", "tweet the verdict", or runs /kill-my-idea:share after a kill, fix or validate.
---

# Share

A verdict is worth more when other people see it, and every post brings the next idea in. `share`
drafts the posts; the founder posts them. It never posts, comments, votes or logs in anywhere.

## Steps

1. **Load the idea**: `verdict.json`, `report-data.json` (key findings, rescue), and `fix.json` /
   `validate.json` when they exist (their scores may be quoted).
2. **Ask where** (up to 3 places) unless the user said it. Default: one subreddit that fits the
   idea's audience, plus X.
3. **Check each place's rules** when you can read them (sidebar, posting rules): links allowed,
   self-promotion rules, required flair or format. When you can't read them, set `links_allowed`
   to `false` and say so.
4. **Write the card**: a headline (the idea, at most 60 characters) and 2–3 reasons, the most
   decisive first, each a plain fact. `after` is optional: the fixed or validated score in a few
   words. The score itself comes from `verdict.json`; the script draws it.
5. **Write the posts.** Lead with the finding, not the tool. State the verdict's score. Every
   "N/100" must be one of this idea's real scores. Write like a person: no em dashes, no hype, and
   never a "What I learned" or lessons section. X: 280 characters with the link. Reddit and HN need
   a title. Put the link in `link`, not in the body, and leave it `null` where links are banned.
6. **Write `share.json`** and run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/share-kit.py" ideas/<folder>`.
   Fix every error and rerun. It writes `share/card.svg`, `share/card.png` (when rsvg-convert or
   ImageMagick is installed) and `share/posts.md`.
7. **Answer in chat**: where the card and the drafts are, one line per place on its rules, and the
   best time to post if you know it. Remind the user that nothing was posted.

## share.json

```json
{
  "schema_version": "1.0", "slug": "<verdict.slug>", "generated": "YYYY-MM-DD",
  "card": {"headline": "", "reasons": ["", ""], "after": ""},
  "posts": [{"platform": "reddit | x | linkedin | hn | other", "place": "r/SideProject",
             "links_allowed": true, "title": "", "body": "", "link": "https://… or null"}]
}
```

Plain text in every string.
