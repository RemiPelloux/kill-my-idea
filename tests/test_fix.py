"""fix-kit.py: the path to GO is re-scored with the real rules and every change needs a lever."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

from helpers import FIXTURES, ROOT, load

fk = load("fix-kit")
kit = load("build-kit")


class Fix(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name) / "2026-11-dental"
        shutil.copytree(FIXTURES / "dental", self.dir)
        self.verdict = json.loads((self.dir / "verdict.json").read_text(encoding="utf-8"))

    def tearDown(self):
        self.tmp.cleanup()

    def fix(self):
        return json.loads((self.dir / "fix.json").read_text(encoding="utf-8"))

    def errors(self, fix):
        rep = fk.Report()
        fk.check_fix(fix, self.verdict, rep)
        return rep.errors

    def test_fixture_passes_and_is_honest(self):
        f = self.fix()
        self.assertEqual(self.errors(f), [])
        self.assertEqual((f["fixed"]["score"], f["reachable"]), (60, False))

    def test_sub_score_changed_without_a_lever_fails(self):
        f = self.fix()
        f["fixed"]["criteria_detail"]["fit"]["assets"]["score"] = 4
        self.assertTrue(any("with no lever" in e for e in self.errors(f)))

    def test_move_must_start_from_the_verdict(self):
        f = self.fix()
        f["levers"][0]["moves"][0]["from"] = 3
        self.assertTrue(any("but the verdict has" in e for e in self.errors(f)))

    def test_inflated_score_fails_the_recompute(self):
        f = self.fix()
        f["fixed"]["score"], f["fixed"]["verdict"], f["reachable"] = 72, "GO", True
        self.assertTrue(any("recomputes to 60" in e for e in self.errors(f)))

    def test_unreachable_needs_blockers(self):
        f = self.fix()
        f["blockers"] = []
        self.assertTrue(any(e.startswith("blockers") for e in self.errors(f)))

    def test_price_position_must_match_competitors(self):
        f = self.fix()
        f["pricing"]["recommended"]["amount"] = 600  # competitors 300-500 per month, "undercut"
        self.assertTrue(any("is not 'undercut'" in e for e in self.errors(f)))

    def test_cleared_kill_shot_needs_a_lever(self):
        f = self.fix()
        f["fixed"]["kill_shots"]["legal_platform_risk"] = False
        self.assertTrue(any("no lever clears it" in e for e in self.errors(f)))

    def test_lifting_r7_needs_profit_above_2(self):
        f = self.fix()
        for m in f["levers"][0]["moves"]:
            m["to"] = m["from"]
        for c, s in (("profit", "gross_margin"), ("profit", "ltv_cac"), ("profit", "pricing_power")):
            f["fixed"]["criteria_detail"][c][s]["score"] = self.verdict["criteria_detail"][c][s]["score"]
        self.assertTrue(any("R7" in e for e in self.errors(f)))

    def test_points_and_gaps(self):
        n = fk.narrative(self.fix(), self.verdict)
        self.assertEqual([lv["points"] for lv in n["levers"]], [5.8, 2.0, 1.0])
        self.assertEqual(n["gaps"][0]["sub"], "ltv_cac")
        self.assertIn("R7_unprofitable_model", n["rules_lifted"])

    def test_report_gets_the_section(self):
        shutil.copy(ROOT / "skills" / "kill" / "report.html", self.dir / "report.html")
        subprocess.run([sys.executable, str(ROOT / "scripts" / "migrate.py"), "--json", str(self.dir)],
                       check=True, stdout=subprocess.DEVNULL)
        self.assertEqual(fk.main(["fix-kit", str(self.dir)]), 0)
        data = json.loads((self.dir / "report-data.json").read_text(encoding="utf-8"))
        self.assertEqual(data["narrative"]["fix"]["score_after"], 60)
        self.assertEqual(json.loads((self.dir / "verdict.json").read_text(encoding="utf-8"))["score"], 41)

    def test_build_can_use_the_fix(self):
        plan = json.loads((self.dir / "build" / "plan.json").read_text(encoding="utf-8"))
        plan["based_on"]["path"], plan["based_on"]["change"] = "fix", self.fix()["summary"]
        rep = kit.Report()
        kit.check_plan(plan, self.verdict, rep, self.fix())
        self.assertEqual(rep.errors, [])
        rep = kit.Report()
        kit.check_plan(plan, self.verdict, rep, None)
        self.assertTrue(any("no fix.json" in e for e in rep.errors))


if __name__ == "__main__":
    unittest.main()
