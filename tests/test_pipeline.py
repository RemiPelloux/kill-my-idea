"""validate-kit, share-kit and nuke-kit: the 7-day test, the posts and the full run follow their rules."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

from helpers import FIXTURES, ROOT, load

vk = load("validate-kit")
sk = load("share-kit")
nk = load("nuke-kit")


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name) / "2026-11-dental"
        shutil.copytree(FIXTURES / "dental", self.dir)
        shutil.copy(ROOT / "skills" / "kill" / "report.html", self.dir / "report.html")
        self.verdict = self.read("verdict.json")

    def tearDown(self):
        self.tmp.cleanup()

    def read(self, name):
        return json.loads((self.dir / name).read_text(encoding="utf-8"))

    def write(self, name, data):
        (self.dir / name).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


class Validate(Base):
    def errors(self, v):
        rep = vk.Report()
        vk.check_validate(v, self.verdict, rep)
        return rep.errors

    def test_fixture_passes(self):
        self.assertEqual(self.errors(self.read("validate.json")), [])

    def test_kit_without_results_passes(self):
        v = self.read("validate.json")
        v["results"] = None
        self.assertEqual(self.errors(v), [])

    def test_needs_a_commitment_target(self):
        v = self.read("validate.json")
        v["targets"][0]["metric"] = "replies"
        self.assertTrue(any("signups or presales" in e for e in self.errors(v)))

    def test_leading_question_fails(self):
        v = self.read("validate.json")
        v["interview"]["questions"][0] = "Would you pay 300 USD a month for this?"
        self.assertTrue(any("what they did last time" in e for e in self.errors(v)))

    def test_link_where_links_are_banned_fails(self):
        v = self.read("validate.json")
        v["outreach"][1]["text"] += " https://example.com"
        self.assertTrue(any("doesn't allow them" in e for e in self.errors(v)))

    def test_missed_target_cannot_move_up(self):
        v = self.read("validate.json")
        v["results"]["moves"][0]["to"] = 2.5
        v["results"]["rescored"]["criteria_detail"]["profit"]["pricing_power"]["score"] = 2.5
        self.assertTrue(any("goes up, but T1 was not met" in e for e in self.errors(v)))

    def test_move_is_capped_at_2(self):
        v = self.read("validate.json")
        v["results"]["moves"][1]["to"] = 4.5
        self.assertTrue(any("2 points at most" in e for e in self.errors(v)))

    def test_every_target_needs_a_result(self):
        v = self.read("validate.json")
        v["results"]["entries"].pop()
        self.assertTrue(any("no result for T2" in e for e in self.errors(v)))

    def test_rate_needs_the_sample(self):
        t, e = {"goal": 8, "out_of": 40}, {"actual": 3, "out_of": 10}
        self.assertEqual(vk.status(t, e), "missed")  # 30% but only 10 tries out of 40
        self.assertEqual(vk.status(t, {"actual": 11, "out_of": 40}), "met")

    def test_renders_kit_and_section(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "migrate.py"), "--json", str(self.dir)],
                       check=True, stdout=subprocess.DEVNULL)
        self.assertEqual(vk.main(["validate-kit", str(self.dir)]), 0)
        page = (self.dir / "validate" / "landing.html").read_text(encoding="utf-8")
        self.assertIn("Content-Security-Policy", page)
        self.assertNotIn("<script", page)
        self.assertEqual(self.read("report-data.json")["narrative"]["validate"]["score_after"], 41)
        self.assertEqual(self.read("verdict.json")["score"], 41)


class Share(Base):
    def errors(self, s):
        rep = sk.Report()
        sk.check_share(s, self.verdict, rep, sk.known_scores(self.dir, self.verdict))
        return rep.errors

    def test_fixture_passes(self):
        self.assertEqual(self.errors(self.read("share.json")), [])

    def test_wrong_score_fails(self):
        s = self.read("share.json")
        s["posts"][0]["title"] = s["posts"][0]["title"].replace("41/100", "71/100")
        self.assertTrue(any("says 71/100" in e for e in self.errors(s)))

    def test_link_banned(self):
        s = self.read("share.json")
        s["posts"][2]["link"] = "https://github.com/RemiPelloux/kill-my-idea"
        self.assertTrue(any("doesn't allow them" in e for e in self.errors(s)))

    def test_x_length(self):
        s = self.read("share.json")
        s["posts"][1]["body"] += " 41" * 100
        self.assertTrue(any("x allows 280" in e for e in self.errors(s)))

    def test_no_lessons_no_dashes(self):
        s = self.read("share.json")
        s["posts"][0]["body"] += "\n\nWhat I learned: test first — always."
        errs = self.errors(s)
        self.assertTrue(any("What I learned" in e for e in errs))
        self.assertTrue(any("dash" in e for e in errs))

    def test_card_svg_comes_from_the_verdict(self):
        svg = sk.card_svg(self.verdict, self.read("share.json")["card"])
        self.assertIn(">41<", svg)
        self.assertIn("NO-GO", svg)


class Nuke(Base):
    def errors(self, n):
        rep = nk.Report()
        nk.check_nuke(n, self.dir, self.verdict, rep)
        return rep.errors

    def test_fixture_passes(self):
        self.assertEqual(self.errors(self.read("nuke.json")), [])

    def test_order_is_fixed(self):
        n = self.read("nuke.json")
        n["steps"][2], n["steps"][3] = n["steps"][3], n["steps"][2]
        self.assertTrue(any("in this order" in e for e in self.errors(n)))

    def test_deepdive_only_for_pivot(self):
        n = self.read("nuke.json")
        n["steps"][1] = {"step": "deepdive", "status": "done", "why": ""}
        self.assertTrue(any("only for a PIVOT" in e for e in self.errors(n)))

    def test_stop_rule(self):
        f = self.read("fix.json")
        f["fixed"]["score"] = 45
        self.write("fix.json", f)
        errs = self.errors(self.read("nuke.json"))
        self.assertTrue(any("stops after fix" in e for e in errs))

    def test_done_step_needs_its_file(self):
        (self.dir / "share.json").unlink()
        self.assertTrue(any("share.json is missing" in e for e in self.errors(self.read("nuke.json"))))

    def test_writes_nuke_md_and_section(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "migrate.py"), "--json", str(self.dir)],
                       check=True, stdout=subprocess.DEVNULL)
        self.assertEqual(nk.main(["nuke-kit", str(self.dir)]), 0)
        self.assertIn("Full run: NO-GO 41/100", (self.dir / "NUKE.md").read_text(encoding="utf-8"))
        self.assertEqual(self.read("report-data.json")["narrative"]["nuke"]["fix"]["score_after"], 60)


if __name__ == "__main__":
    unittest.main()
