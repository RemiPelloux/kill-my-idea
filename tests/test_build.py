"""build-kit.py: the plan check against the verdict, the business-plan math and the rendered kit."""
import copy
import json
import pathlib
import shutil
import tempfile
import unittest

from helpers import FIXTURES, ROOT, load

kit = load("build-kit")


class Kit:
    """The dental fixture (NO-GO 41, with build/plan.json) copied to a temp dir."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name) / "2026-11-dental"
        shutil.copytree(FIXTURES / "dental", self.dir)
        self.b = self.dir / "build"

    def plan(self):
        return json.loads((self.b / "plan.json").read_text(encoding="utf-8"))

    def save(self, plan):
        (self.b / "plan.json").write_text(json.dumps(plan), encoding="utf-8")

    def errors(self, plan=None):
        rep = kit.Report()
        verdict = json.loads((self.dir / "verdict.json").read_text(encoding="utf-8"))
        kit.check_plan(plan or self.plan(), verdict, rep)
        return rep.errors

    def write_prose(self, readme_extra=""):
        body = "x" * 220
        for f in kit.MODEL_FILES:
            p = self.b / f
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(f"# {f}\n\nFollow pelloux-guidelines.md. Test with npx smarttest run.\n\n{body}\n",
                         encoding="utf-8")
        (self.b / "README.md").write_text(
            f"# FrontDesk Fill\n\nNO-GO 41: no channel.{readme_extra}\n\n## Run\n\n`npx smarttest run`\n\n"
            f"## Structure\n\n{body}\n", encoding="utf-8")
        (self.b / "app" / "service").mkdir(parents=True, exist_ok=True)
        (self.b / "app" / "service" / "main.py").write_text("print('ok')\n", encoding="utf-8")


class Check(unittest.TestCase):
    def setUp(self):
        self.k = Kit()

    def tearDown(self):
        self.k.tmp.cleanup()

    def test_fixture_plan_passes(self):
        self.assertEqual(self.k.errors(), [])

    def test_verdict_basis_must_match_the_metric(self):
        p = self.k.plan()
        p["business_plan"]["inputs"]["churn_monthly_pct"]["value"] = 2
        self.assertTrue(any("churn_monthly_pct" in e and "verdict metrics" in e for e in self.k.errors(p)))

    def test_based_on_must_copy_the_verdict(self):
        p = self.k.plan()
        p["based_on"]["score"] = 71
        self.assertTrue(any(e.startswith("based_on") for e in self.k.errors(p)))
        p = self.k.plan()
        p["based_on"]["change"] = "Something else"
        self.assertTrue(any("rescue[1].change" in e for e in self.k.errors(p)))

    def test_ad_that_loses_money_fails(self):
        p = self.k.plan()
        p["ads"][0]["target_cpa"] = 5000  # lifetime gross profit is (299-101) x 20 = 3,960
        self.assertTrue(any("lose money" in e for e in self.k.errors(p)))

    def test_env_values_and_bad_names_fail(self):
        p = self.k.plan()
        p["env"][0]["value"] = "sk-live-123"
        p["env"][1]["name"] = "open dental key"
        errs = self.k.errors(p)
        self.assertTrue(any("never put a value" in e for e in errs))
        self.assertTrue(any("UPPER_SNAKE_CASE" in e for e in errs))

    def test_markup_and_path_traversal_fail(self):
        p = self.k.plan()
        p["ads"][0]["hook"] = "<script>alert(1)</script>"
        p["structure"][0]["path"] = "../../etc/"
        errs = self.k.errors(p)
        self.assertTrue(any("ads[0].hook" in e for e in errs))
        self.assertTrue(any("structure[0].path" in e for e in errs))

    def test_low_contrast_fails(self):
        p = self.k.plan()
        p["brand"]["colors"]["fg"] = "#1a2233"
        self.assertTrue(any("contrast" in e for e in self.k.errors(p)))

    def test_video_length_and_last_scene(self):
        p = self.k.plan()
        p["motion"]["scenes"] = p["motion"]["scenes"][:3]  # 11 s, ends on a stat
        errs = self.k.errors(p)
        self.assertTrue(any("15 to 30" in e for e in errs))
        self.assertTrue(any("last scene" in e for e in errs))

    def test_sprints_and_stories_link_up(self):
        p = self.k.plan()
        p["stories"][0]["sprint"] = 9
        p["stories"][1]["persona"] = "Nobody"
        p["sprints"][1]["exit"] = "pilots go well"
        errs = self.k.errors(p)
        self.assertTrue(any("not a sprint number" in e for e in errs))
        self.assertTrue(any("not a persona name" in e for e in errs))
        self.assertTrue(any("measurable exit" in e for e in errs))

    def test_scenarios_must_be_ordered(self):
        p = self.k.plan()
        sc = p["business_plan"]["scenarios"]
        sc[0]["new_customers"], sc[2]["new_customers"] = sc[2]["new_customers"], sc[0]["new_customers"]
        self.assertTrue(any("Pessimistic ≤ Base" in e for e in self.k.errors(p)))


class Projection(unittest.TestCase):
    def test_base_case_numbers(self):
        plan = json.loads((FIXTURES / "dental" / "build" / "plan.json").read_text(encoding="utf-8"))
        s = kit.project(plan["business_plan"])["Base"]["summary"]
        self.assertAlmostEqual(s["m12_customers"], 13.15, places=1)
        self.assertEqual(round(s["m12_mrr"]), 3931)
        self.assertEqual(s["break_even_month"], 10)
        self.assertEqual(round(s["funding_needed"]), 1960)

    def test_break_even_must_hold_to_month_12(self):
        bp = {"inputs": {k: {"value": v} for k, v in {
            "revenue_per_customer_month": 100, "variable_cost_per_customer_month": 0, "cac": 1000,
            "churn_monthly_pct": 0, "fixed_costs_month": 0, "start_cash": 0}.items()},
            "scenarios": [{"name": "Base", "new_customers": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}]}
        s = kit.project(bp)["Base"]["summary"]
        self.assertIsNone(s["break_even_month"])  # month 12 is negative again


class Render(unittest.TestCase):
    def setUp(self):
        self.k = Kit()

    def tearDown(self):
        self.k.tmp.cleanup()

    def test_render_writes_the_kit_and_keeps_prose(self):
        self.k.write_prose()
        mine = (self.k.b / "README.md").read_text(encoding="utf-8")
        self.assertEqual(kit.main(["build-kit", str(self.k.dir)]), 0)
        for f in ("BUILD.md", ".env.example", "design-tokens.css", "docs/business-plan.csv", "docs/ads.md",
                  "docs/motion.md", "docs/user-stories.md", "docs/sprints.md", "video/src/Promo.tsx",
                  "video/package.json"):
            self.assertTrue((self.k.b / f).exists(), f)
        self.assertEqual((self.k.b / "README.md").read_text(encoding="utf-8"), mine)
        self.assertIn("NO-GO", (self.k.b / "BUILD.md").read_text(encoding="utf-8")[:300])
        env = (self.k.b / ".env.example").read_text(encoding="utf-8")
        self.assertIn("RETELL_API_KEY=\n", env)
        self.assertEqual(kit.main(["build-kit", "--check", str(self.k.dir)]), 0)

    def test_props_match_the_template_shape(self):
        kit.main(["build-kit", str(self.k.dir)])
        props = json.loads((self.k.b / "video" / "src" / "props.json").read_text(encoding="utf-8"))
        self.assertEqual(set(props), {"brand", "motion", "ads"})
        self.assertEqual((props["motion"]["width"], props["motion"]["height"]), (1080, 1920))
        self.assertEqual(props["ads"][1]["width"], 1200)
        self.assertNotIn("voiceover", props["motion"]["scenes"][0])

    def test_guidelines_are_copied_and_required(self):
        self.k.write_prose()
        kit.main(["build-kit", str(self.k.dir)])
        g = (self.k.b / "pelloux-guidelines.md").read_text(encoding="utf-8")
        self.assertIn("Pick the simplest fix", g)
        self.assertNotIn("playground", g.lower())
        (self.k.b / "CLAUDE.md").write_text("# Rules\n\n" + "z" * 300 + "\n", encoding="utf-8")
        self.assertEqual(kit.main(["build-kit", "--check", str(self.k.dir)]), 1)

    def test_smarttest_is_required(self):
        self.k.write_prose()
        kit.main(["build-kit", str(self.k.dir)])
        self.assertIn("@tkmremi/smarttest@", (self.k.b / "BUILD.md").read_text(encoding="utf-8"))
        self.assertIn(".smarttest/", (self.k.b / ".gitignore").read_text(encoding="utf-8"))
        (self.k.b / "docs" / "test-plan.md").write_text("# Tests\n\n" + "w" * 300 + "\n", encoding="utf-8")
        self.assertEqual(kit.main(["build-kit", "--check", str(self.k.dir)]), 1)

    def test_check_needs_the_prose_files(self):
        kit.main(["build-kit", str(self.k.dir)])
        self.assertEqual(kit.main(["build-kit", "--check", str(self.k.dir)]), 1)

    def test_no_go_readme_must_say_so(self):
        self.k.write_prose()
        (self.k.b / "README.md").write_text("# FrontDesk Fill\n\n" + "y" * 300 + "\n\n## Run\n\n## Structure\n")
        self.assertEqual(kit.main(["build-kit", "--check", str(self.k.dir)]), 1)

    def test_template_sample_props_are_valid(self):
        props = json.loads((ROOT / "skills" / "build" / "video" / "src" / "props.json").read_text(encoding="utf-8"))
        self.assertEqual(set(props), {"brand", "motion", "ads"})


if __name__ == "__main__":
    unittest.main()
