# How scoring works

Every verdict follows the same path: 21 sub-scores, 7 weighted criteria, a raw total, then fixed
rules that a nice pitch can't argue its way around. `scripts/check-idea.py` recomputes all of it
after every run, so the score in the report always follows these rules.

## 1. Sub-scores

Each of the 7 criteria has 3 sub-scores, scored 1–5 in half points against a rubric with numeric
anchors (the full rubric is in [`skills/kill/SKILL.md`](../skills/kill/SKILL.md) §5). For example,
a gross margin under 30% is a 1 and over 85% is a 5. Every sub-score has a one-line justification,
and a source when there is one.

| Criterion | Weight | Sub-scores |
|---|---|---|
| Profit potential | 25 | gross margin, LTV:CAC, pricing power |
| Feasibility for you | 20 | build effort, skills match, capital needed |
| Time to first revenue | 15 | time to MVP, sales cycle, channel readiness |
| Market demand | 15 | search demand, trend, willingness to pay |
| Competitive room | 10 | free alternatives, competitor density, differentiation |
| Risk (5 = low) | 10 | legal and regulatory, platform dependency, market risk |
| Founder fit | 5 | skills, assets, interest |

## 2. The total

- A criterion's value is the **mean of its 3 sub-scores**, unrounded.
- Its points are **weight × mean ÷ 5**.
- `score_raw` is the sum of the points, to one decimal.
- `score` is `score_raw` **rounded half up** (60.5 → 61). Nothing is rounded before the sum.

## 3. The fixed rules

Applied after the total, recorded in `rules_applied` with their effect:

| Rule | When | Effect |
|---|---|---|
| R1 free equivalent | A free alternative does the whole job and you have no specific edge | Competitive room ≤ 1.5 |
| R2 no channel | No credible way to reach the first 10 customers | Total capped at 69: no GO |
| R3 saturated wave | 10+ near-identical launches in 12 months, no specific edge | Competitive room and differentiation ≤ 1.5 |
| R4 LTV:CAC < 1 | Below 1 with no path to fix it | Profit potential ≤ 2 |
| R5 coherence | A kill shot hit must show in its sub-scores | e.g. no channel → channel readiness ≤ 2 |
| R6 loses money, no channel | No channel **and** LTV:CAC below 1 | Total capped at 49: NO-GO |
| R7 unprofitable model | Profit potential is 2 or less | Total minus 10, and at most 49: NO-GO |

A quick run (`--quick`) is also capped at 69, because 10 sources are not enough for a GO.

**Verdict:** GO at 70 and above, PIVOT from 50 to 69, NO-GO below 50.

## 4. A worked example

A real run from the [gallery](https://remipelloux.github.io/kill-my-idea/gallery/board.html): a
Shopify pet-products dropshipping store with TikTok ads, in the US.

| Criterion | Weight | Sub-scores | Mean | Points |
|---|---|---|---|---|
| Profit potential | 25 | 2 / 1 / 1.5 | 1.50 | 7.50 |
| Feasibility for you | 20 | 4.5 / 2.5 / 3 | 3.33 | 13.33 |
| Time to first revenue | 15 | 4.5 / 5 / 2 | 3.83 | 11.50 |
| Market demand | 15 | 4.5 / 3.5 / 3.5 | 3.83 | 11.50 |
| Competitive room | 10 | 2.5 / 1 / 1 | 1.50 | 3.00 |
| Risk | 10 | 2.5 / 2 / 3 | 2.50 | 5.00 |
| Founder fit | 5 | 2 / 1 / 1 | 1.33 | 1.33 |
| **Raw total** | | | | **53.2** |

1. The raw total rounds to **53**, which would be a PIVOT.
2. **R3** already lowered competition: 30,000+ Shopify pet stores sell the same catalogs.
3. **R5** lowered channel readiness to 2, because no channel was found.
4. **R7**: Profit potential is **1.50** (a customer costs about $57 on TikTok and brings $18 of
   lifetime profit, LTV:CAC **0.32**). The model doesn't make money: 53 − 10 = **43**.
5. **R6** would also cap it at 49 (no channel and LTV:CAC below 1). The final score is **43: NO-GO**.

Easy to start and fast to first revenue lifted the average above 50. R6 and R7 exist so that can't
happen when the model loses money.

## 5. Calibration

The rules are checked against [10 ideas with a known outcome](../calibration/README.md), each scored
as of its launch date. With R7, the 5 that worked score 64–71 (median 68, Tally reaches GO) and the
5 that failed score 39–49 (median 49). Without R7, the failures scored 49–60: their pre-mortems named
the real causes, but easy feasibility averaged the weak profit away.

## 6. Confidence

Separate from the score, every verdict says how much evidence backs it:

| Level | Sourced sub-scores | Sources | Primary sources |
|---|---|---|---|
| high | 14+ | 25+ | 5+ |
| medium | 8+ | 15+ | 2+ |
| low | otherwise | | |

## Check it yourself

```sh
python3 scripts/check-idea.py ideas/<folder>    # recompute one verdict
python3 scripts/calibrate.py ideas              # how your scores spread, and which kill shots keep hitting
```
