"""Golden runs: 5 real verdicts frozen from the gallery. A rubric or rule change that moves their
score fails here, so every score change is deliberate: update the golden file and say why in the
changelog."""
import json
import pathlib
import unittest

from helpers import load

chk = load("check-idea")
GOLDEN = pathlib.Path(__file__).resolve().parent / "golden"
EXPECTED = {"youtube-summary-extension": 58, "vending-machine-route": 49, "ai-history-channel": 43,
            "ugc-agency-dtc": 53, "ai-headshot-generator": 49}


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
