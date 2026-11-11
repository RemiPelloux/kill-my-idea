"""scripts/check-idea.py: the score formula and the fixed rules R1-R6."""
import unittest

from helpers import IdeaCopy, load

chk = load("check-idea")


def errors(folder, legacy=False):
    return chk.check_folder(folder, legacy).errors


class Fixtures(unittest.TestCase):
    def test_real_runs_pass(self):
        for name in ("dental", "pet"):
            with self.subTest(name):
                c = IdeaCopy(name)
                self.assertEqual(errors(c.dir), [])
                c.close()


class Formula(unittest.TestCase):
    def test_round_half_up(self):
        self.assertEqual(chk.round_half_up(60.5), 61)
        self.assertEqual(chk.round_half_up(60.49), 60)
        self.assertEqual(chk.round_half_up(48.5), 49)

    def test_band(self):
        self.assertEqual(chk.band(70), "GO")
        self.assertEqual(chk.band(69), "PIVOT")
        self.assertEqual(chk.band(50), "PIVOT")
        self.assertEqual(chk.band(49), "NO-GO")

    def test_tampered_score_is_caught(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["score"] += 5
        c.save(v)
        self.assertTrue(any("recomputes to" in e for e in errors(c.dir)))
        c.close()

    def test_verdict_must_match_band(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["verdict"] = "GO"
        c.save(v)
        self.assertTrue(any("does not match score" in e for e in errors(c.dir)))
        c.close()

    def test_sub_score_must_be_half_points(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["criteria_detail"]["demand"]["trend"]["score"] = 3.3
        c.save(v)
        self.assertTrue(any("half points" in e for e in errors(c.dir)))
        c.close()


class Rules(unittest.TestCase):
    def test_r6_required_when_no_channel_and_ltv_cac_below_1(self):
        c = IdeaCopy("pet")
        v = c.verdict()
        v["rules_applied"] = [r for r in v["rules_applied"] if r["rule"] != "R6_unprofitable_no_channel"]
        v["score"], v["verdict"] = 53, "PIVOT"
        c.save(v)
        errs = errors(c.dir)
        self.assertTrue(any("R6_unprofitable_no_channel" in e for e in errs), errs)
        c.close()

    def test_r6_not_triggered_with_ltv_cac_above_1(self):
        c = IdeaCopy("dental")  # no channel, but LTV:CAC 1.31
        self.assertGreater(c.verdict()["metrics"]["ltv_cac"]["value"], 1)
        self.assertEqual(errors(c.dir), [])
        c.close()

    def test_r2_caps_at_69(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        for crit in v["criteria_detail"].values():
            for sub in crit.values():
                sub["score"] = 5
        v["metrics"]["ltv_cac"]["value"] = 3
        c.save(v)
        errs = errors(c.dir)
        self.assertTrue(any("R2_no_channel" in e or "capped at 69" in e for e in errs), errs)
        c.close()

    def test_r5_kill_shot_must_show_in_sub_scores(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["criteria_detail"]["time_to_first_revenue"]["channel_readiness"]["score"] = 4
        c.save(v)
        self.assertTrue(any("R5" in e for e in errors(c.dir)))
        c.close()


class Versions(unittest.TestCase):
    def test_fixtures_are_1_0(self):
        c = IdeaCopy("pet")
        self.assertEqual(c.verdict().get("schema_version"), chk.SCHEMA_VERSION)
        c.close()

    def test_unknown_major_version_is_refused(self):
        c = IdeaCopy("pet")
        v = c.verdict()
        v["schema_version"] = "2.0"
        c.save(v)
        self.assertTrue(any("schema_version" in e for e in errors(c.dir)))
        c.close()

    def test_missing_version_is_only_a_warning(self):
        c = IdeaCopy("pet")
        v = c.verdict()
        del v["schema_version"]
        c.save(v)
        rep = chk.check_folder(c.dir)
        self.assertTrue(any("schema_version" in w for w in rep.warnings))
        c.close()


class Safety(unittest.TestCase):
    def test_code_in_report_data_is_refused(self):
        c = IdeaCopy("dental")
        p = c.dir / "report-data.js"
        p.write_text(p.read_text().replace("window.KMI_DATA = ", "window.KMI_DATA = (function(){})() || ", 1))
        self.assertTrue(any("plain data literal" in e or "one statement" in e for e in errors(c.dir)))
        c.close()

    def test_legacy_mode_keeps_safety_errors(self):
        c = IdeaCopy("dental")
        p = c.dir / "report-data.js"
        p.write_text(p.read_text() + "\nalert(1);")
        v = c.verdict()
        v["score"] += 3
        c.save(v)
        rep = chk.check_folder(c.dir, True)
        self.assertTrue(rep.errors, "safety errors must stay errors in --legacy mode")
        self.assertFalse(any("recomputes to" in e for e in rep.errors), "rule errors become warnings in --legacy mode")
        self.assertTrue(any("recomputes to" in w for w in rep.warnings))
        c.close()


if __name__ == "__main__":
    unittest.main()
