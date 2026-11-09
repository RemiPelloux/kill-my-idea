<div align="center">

<img src="assets/hero.svg" alt="Your idea, checked against the evidence. An AI wedding-speech app scored 48 out of 100, stamped NO-GO, with 18 sources." width="100%">

```text
/plugin marketplace add RemiPelloux/kill-my-idea
/plugin install kill-my-idea@kill-my-idea
```

[Live reports](https://remipelloux.github.io/kill-my-idea/) &nbsp;·&nbsp; [Examples](examples/README.md) &nbsp;·&nbsp; [Security](SECURITY.md) &nbsp;·&nbsp; [Changelog](CHANGELOG.md) &nbsp;·&nbsp; [Sponsor](https://github.com/sponsors/RemiPelloux)

[![MIT license](https://img.shields.io/badge/license-MIT-EFE8DC?labelColor=15120F)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/RemiPelloux/kill-my-idea?style=flat&color=E5383B&labelColor=15120F)](https://github.com/RemiPelloux/kill-my-idea/stargazers)

</div>

Ask an AI whether your idea is good and it will usually find a way to say yes. kill-my-idea does
the opposite. It looks for a free alternative, competitors, people who already failed, and the
numbers that don't add up. Then it gives you a score out of 100, a GO / PIVOT / NO-GO verdict, the
ways the idea could still be saved, and a report where every number has a source.

## Paste a "$10k/month" tweet

The most common use: you see a viral thread promising easy money. Paste it in:

```text
kill my idea: <paste the thread>
```

It checks every claim, names what the author is selling, redoes the math and gives a verdict.
Real example, a viral thread about AI-written Amazon KDP books:

| The thread said | The check found |
|---|---|
| "$3,000 a month from 5 sales a day" | **About $1,380** in royalties once printing costs are counted ([KDP royalty rules](https://kdp.amazon.com/en_US/help/topic/G201834330)) |
| "Anyone can do it" | About 300k new books a month compete for the same shelf ([AI Policy Desk](https://www.aipolicydesk.com/blog/amazon-kdp-ai-generated-content-surge-enforcement-2026)) |
| "$3M from books" | No evidence ever shown. The author **sells KDP coaching** |
| Verdict | **PIVOT, 52/100.** Run a 1-week niche test before writing a word ([full card](examples/kdp-books.md)) |

## Same idea, two answers

We asked plain Claude and kill-my-idea about the same idea: an AI app that writes wedding speeches, at $19 each.

| | Claude, no plugin | kill-my-idea |
|---|---|---|
| Verdict | "It's a decent small business." | **NO-GO, 48/100** |
| Sources | None | 18, linked |
| Competition | "Several AI speech tools exist." | 14 named, priced $0–34. One live competitor made **$32.75 in 30 days** |
| Unit economics | "Margins are almost entirely marketing." | LTV $18 vs CAC $35 on paid search (estimates, reasoning shown). Every sale loses money |
| What to do next | Spend about $200 on ads and see | Don't build the app. List a human-polished speech on Fiverr at $49–99. Fewer than 3 paid orders in 7 days: archive it |

Plain Claude's full answer is [here, unedited](examples/plain-claude-wedding.md). The kill-my-idea version is a [live report](https://remipelloux.github.io/kill-my-idea/reports/wedding-speeches/).

## Seven ideas it has checked

<a href="https://remipelloux.github.io/kill-my-idea/"><img src="assets/verdict-wall.svg" alt="Seven real verdicts: Juicero 27, a travel blog 41, a coloring book 42, wedding speeches 48, KDP paperbacks 52, Notion templates 55, and kill-my-idea itself 63" width="100%"></a>

All seven are real runs, mostly ideas we were about to spend time or money on. The coloring book is
why this exists: we built it first, three versions and a day of work, and a five-minute search then
found the same book for free. The plugin also checked itself: 63, because fifteen open-source idea
validators already exist.

## The report

Every run writes `report.html`, a report you open in a browser and can print as an A4 PDF.

<a href="https://remipelloux.github.io/kill-my-idea/reports/notion-real-estate/"><img src="assets/report-cover.png" alt="Report cover for Notion templates for French real-estate agents: the answer, a score ring at 55, a PIVOT badge, and Share card and Save PDF buttons" width="100%"></a>

It opens with the answer, then shows what would change it:

<a href="https://remipelloux.github.io/kill-my-idea/reports/notion-real-estate/#rescue"><img src="assets/report-rescue.png" alt="Could it be saved: three changes to the Notion-template idea, each with a projected score, a difficulty, the effort and the cost" width="100%"></a>

It goes on to cover:
- the score breakdown: 21 sub-scores you can expand, the raw total, and which fixed rules capped it;
- a confidence level (high, medium or low) and the distance to the next verdict band;
- each kill shot, with its evidence, marked hit, clear or not checked, and the one that weighs most;
- market size;
- a map of competitors by price and traction;
- a country comparison;
- LTV:CAC against healthy thresholds;
- monthly scenarios and a risk matrix;
- a 7-day test with the conditions for stopping it;
- numbered sources, each tagged primary, secondary or tertiary.

Every number shows whether it was sourced, estimated (hover for the formula) or not found.
After a deep dive, the report shows how the score moved since the quick verdict.
One click on **Share card** downloads a PNG verdict card for social media, and reports follow your language (English or French).

## Commands

| Command | What it does |
|---|---|
| `/kill-my-idea:kill` | The verdict, report and 7-day test. Accepts one line, a pasted tweet, a URL or a long document |
| `/kill-my-idea:deepdive` | Six research tracks in parallel, 40+ sources: market size, competitor teardown, real customer quotes, pricing, channels, regulation per country |
| `/kill-my-idea:check-tweet` | Fact-checks a viral "make money" post: every claim, the real math, what the author sells, then a verdict |
| `/kill-my-idea:roast` | The same verdict as five sourced one-liners, sized for a screenshot ([Juicero](examples/juicero-roast.md)). Also saved for `compare` |
| `/kill-my-idea:compare` | Ranks every idea you've checked by score, speed and confidence, and picks the one to work on this week |

You can also just write "kill my idea: …", "is this worth building?" or "which idea should I do?".

<details>
<summary><strong>How the score works</strong></summary>

<br>

1. **Extract.** It turns your input into a brief: problem, customer, solution, price, channel, countries, claims.
2. **Ask once.** At most four questions (country, budget and time, goal, your edge), and only the ones that would change the verdict. Say "just go" to skip them.
3. **Look for kill shots**, searching in the target country's language, with at least 20 sources
   from 10 domains, each tagged primary, secondary or tertiary:
   - a free alternative;
   - direct competitors;
   - people who already failed;
   - no way to reach customers;
   - costs that eat the margin;
   - weak demand;
   - legal or platform risk;
   - for "I make $10k a month" posts, what the author is selling;
   - a saturated wave of look-alike launches in the last 6–12 months.
4. **Measure:**
   - market size (TAM / SAM / SOM);
   - competitor prices and demand trend;
   - gross margin, CAC, LTV and LTV:CAC;
   - churn, conversion, payback, break-even and time to first revenue.
5. **Score.** Seven weighted criteria:

   | Criterion | Weight |
   |---|---|
   | Profit | 25 |
   | Feasibility for you | 20 |
   | Time to first revenue | 15 |
   | Demand | 15 |
   | Competition | 10 |
   | Risk | 10 |
   | Fit | 5 |

   Each criterion is the mean of three sub-scores (21 in all), each scored 1–5 against a fixed
   rubric with numeric anchors (a gross margin under 30% is a 1, over 85% a 5). The total is
   rounded half up, then five fixed rules stop it from rescuing a bad idea:
   - a free equivalent with no edge caps Competitive room at 1.5;
   - no channel caps the total at 69, so no GO;
   - a saturated wave of look-alike launches caps Competitive room and differentiation at 1.5;
   - an LTV:CAC below 1 caps Profit at 2;
   - every kill shot that hit must show in the sub-scores.

   GO at 70 and above, PIVOT from 50 to 69, NO-GO below 50. Every verdict carries a
   confidence level (high, medium or low) computed from how many sub-scores and sources back it.
6. **Rescue.** Up to three changes that would fix the kill shots, each re-scored and rated doable, hard or very hard.
7. **Test.** The cheapest way to get real proof in seven days, with numbers that tell you to stop.

The whole method is one readable file, [`skills/kill/SKILL.md`](skills/kill/SKILL.md). Fork it and change the weights.
After each run, `scripts/check-idea.py` recomputes the score, applies the rules and checks every source, so the
verdict you read is the one the sub-scores give.

</details>

<details>
<summary><strong>Files it writes</strong></summary>

<br>

Everything goes into `ideas/<YYYY-MM>-<slug>/` in your current folder.

| File | Contents |
|---|---|
| `report.html` + `report-data.js` | The designed report. Works offline and prints to PDF |
| `report.md` | The same report as plain text |
| `idea.json` | The extracted brief ([schema](skills/kill/idea.schema.json)) |
| `verdict.json` | Score, 21 sub-scores, rules applied, confidence, metrics with their sources, countries, rescue paths ([schema](skills/kill/verdict.schema.json)) |
| `deepdive.md` | The deep-dive write-up (`deepdive` only) |
| `roast.md` | The roast (`roast` only) |
| `ideas/RANKING.md` | The ranking of all your ideas (`compare`) |

Check any run yourself:

```sh
python3 scripts/check-idea.py ideas/<folder>   # or --all for every idea
```

It recomputes the score from the sub-scores, applies the fixed rules, and checks every source and
count. `ERROR` lines mean the verdict doesn't follow its own rules.

</details>

<details>
<summary><strong>Questions</strong></summary>

<br>

**Isn't this just a prompt?**
It's a method with a scoring rubric, fixed rules, source minimums, a schema for every output, a
checker that recomputes the score, and tests run on real ideas. You can read all of it. The comparison above shows the difference in practice.

**Does it cost anything?**
No. It's MIT-licensed and runs on your own Claude Code plan. It never publishes anything, spends
money or contacts anyone for you.

**Can I share my verdict?**
Yes. Paste the badge it gives you into your README, or post the card in the
[verdict gallery](https://github.com/RemiPelloux/kill-my-idea/issues/new?template=share-verdict.yml).

**Does it work outside Claude Code?**
The skills follow the open [Agent Skills](https://agentskills.io) format. The `/plugin` install is Claude Code only.

</details>

## Support

If it saved you a weekend, a star helps other people find it. Sponsoring on
[GitHub Sponsors](https://github.com/sponsors/RemiPelloux) pays for new kill shots, country guides and better reports.

Contributions are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

The code is [MIT](LICENSE). The name "kill-my-idea" and the logo are trademarks of Remi Pelloux, not covered by the MIT License; see [TRADEMARK.md](TRADEMARK.md).
