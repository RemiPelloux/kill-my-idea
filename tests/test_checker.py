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
        v["rules_applied"] = [r for r in v["rules_applied"] if r["rule"] not in ("R6_unprofitable_no_channel", "R7_unprofitable_model")]
        for sub in v["criteria_detail"]["profit"].values():
            sub["score"] = 3  # keep R7 out of the way: this tests R6 alone
        v["score"], v["verdict"] = 59, "PIVOT"
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


class Hindsight(unittest.TestCase):
    def _with_as_of(self, as_of, published):
        c = IdeaCopy("pet")
        v = c.verdict()
        v["as_of"] = as_of
        c.save(v)
        p = c.dir / "report-data.js"
        text = p.read_text()
        import json as _j
        data = _j.loads(text[text.index("{"):text.rindex("}") + 1])
        data["verdict"] = v
        for s in data["narrative"]["sources"]:
            s["published"] = published
        p.write_text("window.KMI_DATA = " + _j.dumps(data) + ";")
        return c

    def test_later_source_fails(self):
        c = self._with_as_of("2016-03-01", "2026-05")
        self.assertTrue(any("hindsight" in e for e in errors(c.dir)))
        c.close()

    def test_earlier_sources_pass(self):
        c = self._with_as_of("2026-11-01", "2025-06")
        self.assertFalse(any("hindsight" in e for e in errors(c.dir)))
        c.close()


class TypesAndAnswers(unittest.TestCase):
    def _typed(self, checks=None, answers=None):
        import json as _j
        c = IdeaCopy("pet")
        p = c.dir / "report-data.js"
        text = p.read_text()
        data = _j.loads(text[text.index("{"):text.rindex("}") + 1])
        idea, v = data["idea"], data["verdict"]
        idea["type"] = "ecommerce"
        if answers is not None:
            idea["answers"] = answers
        v["type_checks"] = checks if checks is not None else [
            {"check": "contribution_margin", "result": "hit", "note": "loses money per order", "source": "https://example.com/a"},
            {"check": "returns_shipping", "result": "unknown", "note": "not found"}]
        (c.dir / "idea.json").write_text(_j.dumps(idea))
        c.save(v)
        p.write_text("window.KMI_DATA = " + _j.dumps(data) + ";")
        return c

    def test_typed_idea_passes(self):
        c = self._typed(answers=[{"question": "Average order?", "answer": "$35", "feeds": ["contribution_margin"], "stage": "intake"}])
        self.assertEqual(errors(c.dir), [])
        c.close()

    def test_wrong_type_checks_fail(self):
        c = self._typed(checks=[{"check": "liquidity", "result": "clear", "note": "x"}])
        self.assertTrue(any("needs exactly" in e for e in errors(c.dir)))
        c.close()

    def test_hit_needs_a_source(self):
        c = self._typed(checks=[{"check": "contribution_margin", "result": "hit", "note": "x"},
                                {"check": "returns_shipping", "result": "clear", "note": "y"}])
        self.assertTrue(any("source" in e for e in errors(c.dir)))
        c.close()

    def test_answers_rules(self):
        bad = [{"question": f"q{i}", "answer": "a", "feeds": ["trend"], "stage": "intake"} for i in range(9)]
        c = self._typed(answers=bad)
        self.assertTrue(any("at most 8" in e for e in errors(c.dir)))
        c.close()
        c = self._typed(answers=[{"question": "q", "answer": "a", "feeds": ["made_up"], "stage": "intake"}])
        self.assertTrue(any("unknown feeds" in e for e in errors(c.dir)))
        c.close()
        c = self._typed(answers=[{"question": "q", "answer": "a", "feeds": ["no_distribution"], "stage": "follow_up"}])
        self.assertTrue(any("needs an effect" in e for e in errors(c.dir)))
        c.close()


class GoToMarket(unittest.TestCase):
    """deepdive: personas, strategies, promotion and branding are validated when present."""

    def _gtm(self, fixture="dental", **narr):
        import json as _j
        c = IdeaCopy(fixture)
        p = c.dir / "report-data.js"
        text = p.read_text()
        data = _j.loads(text[text.index("{"):text.rindex("}") + 1])
        data["narrative"].update(narr)
        p.write_text("window.KMI_DATA = " + _j.dumps(data) + ";")
        return c

    Q = [{"quote": f"q{i}", "url": "https://example.com/q"} for i in range(3)]

    def test_persona_needs_3_quotes(self):
        c = self._gtm(personas=[{"name": "A", "role": "r", "trigger": "t", "where": ["x"], "pain_quotes": self.Q[:2]}])
        self.assertTrue(any("at least 3 linked quotes" in e for e in errors(c.dir)))
        c.close()

    def test_exactly_one_recommended_strategy(self):
        st = [{"name": n, "segment": "s", "channel": "c", "score_after": 55, "recommended": True, "why": "w"} for n in "AB"]
        c = self._gtm(strategies=st)
        self.assertTrue(any("exactly one recommended" in e for e in errors(c.dir)))
        c.close()

    def test_five_checked_names(self):
        names = [{"name": f"n{i}", "domain_com": "taken", "trademark": "unknown", "checked": "2026-11-11"} for i in range(4)]
        c = self._gtm(branding={"positioning": {"for": "a", "category": "b", "difference": "c"}, "names": names})
        self.assertTrue(any("exactly 5 names" in e for e in errors(c.dir)))
        c.close()

    def test_no_plan_for_a_dead_idea(self):
        c = self._gtm("pet", personas=[{"name": "A", "role": "r", "trigger": "t", "where": ["x"], "pain_quotes": self.Q}])
        v = c.verdict()
        for r in v.get("rescue") or []:
            r["score_after"] = min(r["score_after"], 49)
        c.save(v)
        import json as _j
        p = c.dir / "report-data.js"
        text = p.read_text()
        data = _j.loads(text[text.index("{"):text.rindex("}") + 1])
        data["verdict"] = v
        p.write_text("window.KMI_DATA = " + _j.dumps(data) + ";")
        self.assertTrue(any("only for an idea that survives" in e for e in errors(c.dir)))
        c.close()


class QuickAndRun(unittest.TestCase):
    def test_quick_needs_low_confidence(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["quick"] = True
        c.save(v)
        self.assertTrue(any("quick run's confidence must be low" in e for e in errors(c.dir)))
        c.close()

    def test_quick_is_never_go(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["quick"] = True
        v["kill_shots"]["no_distribution"] = False
        for crit in v["criteria_detail"].values():
            for sub in crit.values():
                sub["score"] = 5
        v["score"], v["verdict"] = 100, "GO"
        c.save(v)
        self.assertTrue(any("recomputes to 69" in e for e in errors(c.dir)))
        c.close()

    def test_bad_run_numbers(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["run"] = {"minutes": -3, "searches": 19}
        c.save(v)
        self.assertTrue(any("run.minutes" in e for e in errors(c.dir)))
        c.close()


class R7(unittest.TestCase):
    def test_r7_required_when_profit_is_2_or_less(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["rules_applied"] = [r for r in v["rules_applied"] if r["rule"] != "R7_unprofitable_model"]
        c.save(v)
        self.assertTrue(any("R7_unprofitable_model" in e for e in errors(c.dir)))
        c.close()

    def test_negative_ltv_cac_is_refused(self):
        c = IdeaCopy("dental")
        v = c.verdict()
        v["metrics"]["ltv_cac"]["value"] = -0.68
        c.save(v)
        self.assertTrue(any("can't be negative" in e for e in errors(c.dir)))
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
