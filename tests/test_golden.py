"""Golden runs: 5 real verdicts frozen from the gallery. A rubric or rule change that moves their
score fails here, so every score change is deliberate: update the golden file and say why in the
changelog."""
import json
import pathlib
import unittest

from helpers import load

chk = load("check-idea")
GOLDEN = pathlib.Path(__file__).resolve().parent / "golden"
# R7 (0.11): every golden verdict has Profit potential 2 or less, so each lost 10 points, capped at 49:
# youtube-summary-extension 58 -> 48, vending-machine-route 49 -> 39, ai-history-channel 43 -> 33,
# ugc-agency-dtc 53 -> 43, ai-headshot-generator 49 -> 47.
EXPECTED = {"youtube-summary-extension": 48, "vending-machine-route": 39, "ai-history-channel": 33,
            "ugc-agency-dtc": 43, "ai-headshot-generator": 47}


class Golden(unittest.TestCase):
    def test_scores_do_not_move(self):
        for slug, want in EXPECTED.items():
            with self.subTest(slug):
                v = json.loads((GOLDEN / f"{slug}.json").read_text(encoding="utf-8"))
                rep = chk.Report(GOLDEN)
                chk.check_scores(rep, v)
                self.assertEqual(v["score"], want)
                self.assertEqual([e for e in rep.errors if "recomputes" in e or "rules_applied" in e], [], rep.errors)


if __name__ == "__main__":
    unittest.main()
