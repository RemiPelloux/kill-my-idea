# Examples

Real runs of kill-my-idea, mostly on ideas we were about to spend time or money on.

| Example | Command | Verdict | What it shows |
|---|---|---|---|
| [AI receptionist for US dental clinics, full run](dental-receptionist-nuke/NUKE.md) | `nuke` | PIVOT 56 (kill 54) | Every step in one command, 16 min and $8.97 on Opus: deep dive, path to GO (60, out of reach), 7-day test kit, starter kit, card and posts |
| [Notion templates for French real-estate agents](notion-real-estate-report/) ([live](https://remipelloux.github.io/kill-my-idea/reports/notion-real-estate/)) | `kill` | NO-GO 43 | The full HTML report: 21 sub-scores, rescue paths, France vs Belgium |
| [AI wedding-speech app](wedding-speeches.md) ([full report](wedding-speeches-report/), [live](https://remipelloux.github.io/kill-my-idea/reports/wedding-speeches/)) | `kill` | NO-GO 44 | The verdict card, US vs France, and a look-alike's verified revenue |
| [Plain Claude on the same idea](plain-claude-wedding.md) | none | — | The unedited baseline answer used in the README comparison |
| [Viral KDP "$3k/month" thread](kdp-books.md) | `kill` (now `check-tweet`) | PIVOT 52 | A money-tweet fact-check: the real math and the author's incentive |
| [Printable advent coloring book](coloring-book.md) | `kill` | NO-GO 42 | The idea that started the project (built before checking) |
| [Bilingual travel affiliate blog](travel-affiliate.md) | `kill` | NO-GO 41 | A breaking channel (affiliate programs, AI Overviews) |
| [Juicero, roasted](juicero-roast.md) | `roast` | NO-GO 27 | Five sourced burns about a famous failure |
| [kill-my-idea itself](kill-my-idea.md) | `kill` | PIVOT 63 | The plugin rating its own launch |

To open an HTML report locally, download `report.html` and open it in a browser. It is one self-contained file: the report data (`report-data.json`) is embedded in it.

The two report folders (`notion-real-estate-report/` and `wedding-speeches-report/`) were re-run with the 1.0 rules and pass `scripts/check-idea.py` with no errors. The other `.md` examples predate 0.7.0, so they don't carry the rubric-based sub-scores, source tiers, confidence or `rules_applied`. They are kept as they were run.
