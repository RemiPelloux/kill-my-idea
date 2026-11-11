"""build-brain.py, the --board check, export-standalone.py and update-csp.py."""
import json
import pathlib
import shutil
import tempfile
import unittest

from helpers import FIXTURES, ROOT, load

brain = load("build-brain")
build = load("build-report")
cal = load("calibrate")
chk = load("check-idea")
export = load("export-standalone")
csp = load("update-csp")


class Workspace:
    """A temp ideas/ folder holding both fixtures."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ideas = pathlib.Path(self.tmp.name) / "ideas"
        for name in ("dental", "pet"):
            dst = self.ideas / f"2026-11-{name}"
            shutil.copytree(FIXTURES / name, dst)
            shutil.copy(ROOT / "skills" / "kill" / "report.html", dst / "report.html")

    def board(self):
        text = (self.ideas / "board-data.js").read_text(encoding="utf-8")
        return json.loads(text[text.index("{"):text.rindex("}") + 1])


class BuildBrain(unittest.TestCase):
    def setUp(self):
        self.w = Workspace()

    def tearDown(self):
        self.w.tmp.cleanup()

    def test_board_is_valid_and_ranked(self):
        self.assertEqual(brain.main([str(self.w.ideas)]), 0)
        self.assertEqual(chk.check_board(self.w.ideas).errors, [])
        scores = [x["score"] for x in self.w.board()["ideas"]]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_patterns_count_hits(self):
        brain.main([str(self.w.ideas)])
        pats = {p["kill_shot"]: p for p in self.w.board()["patterns"]}
        self.assertEqual(pats["no_distribution"]["hits"], 2)  # both fixtures have no channel

    def test_tampered_patterns_fail_the_board_check(self):
        brain.main([str(self.w.ideas)])
        p = self.w.ideas / "board-data.js"
        p.write_text(p.read_text().replace('"hits": 2', '"hits": 1', 1))
        self.assertTrue(chk.check_board(self.w.ideas).errors)

    def test_brain_keeps_user_notes(self):
        brain.main([str(self.w.ideas)])
        b = self.w.ideas / "BRAIN.md"
        b.write_text(b.read_text().replace("- Country:", "- Country: FR") + "\nmy own line\n")
        brain.main([str(self.w.ideas)])
        text = b.read_text()
        self.assertIn("- Country: FR", text)
        self.assertIn("my own line", text)
        self.assertEqual(text.count("kmi:auto:start"), 1)

    def test_no_brain_flag(self):
        brain.main(["--no-brain", str(self.w.ideas)])
        self.assertFalse((self.w.ideas / "BRAIN.md").exists())
        self.assertFalse(self.w.board()["brain"])

    def test_unknown_focus_is_ignored(self):
        (self.w.ideas / "focus.json").write_text('{"slug": "nope", "why": "x"}')
        brain.main([str(self.w.ideas)])
        self.assertIsNone(self.w.board()["focus"])

    def test_html_in_titles_is_escaped(self):
        p = self.w.ideas / "2026-11-dental" / "idea.json"
        idea = json.loads(p.read_text())
        idea["title"] = "</script><script>alert(1)</script>"
        p.write_text(json.dumps(idea))
        brain.main([str(self.w.ideas)])
        self.assertNotIn("</script>", (self.w.ideas / "board-data.js").read_text())


class Export(unittest.TestCase):
    def test_embeds_inert_json(self):
        html = (ROOT / "skills" / "kill" / "report.html").read_text(encoding="utf-8")
        data = export.load_data(FIXTURES / "dental" / "report-data.js")
        data["idea"]["title"] = "</script><img src=x onerror=alert(1)>"
        out = export.build(html, data)
        self.assertIn('<script type="application/json" id="kmi-data">', out)
        self.assertNotIn('src="report-data.js"', out)
        block = out[out.index('id="kmi-data">'):]
        block = block[:block.index("</script>")]
        self.assertNotIn("<img", block)

    def test_refuses_code(self):
        with tempfile.TemporaryDirectory() as t:
            p = pathlib.Path(t) / "report-data.js"
            p.write_text("window.KMI_DATA = {\"a\": alert(1)};")
            with self.assertRaises(SystemExit):
                export.load_data(p)


class BuildReport(unittest.TestCase):
    """1.0 default: report-data.json embedded in report.html as inert JSON."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name) / "pet"
        shutil.copytree(FIXTURES / "pet", self.dir)
        text = (self.dir / "report-data.js").read_text()
        (self.dir / "report-data.json").write_text(text[text.index("{"):text.rindex("}") + 1])
        (self.dir / "report-data.js").unlink()
        build.main([str(self.dir)])

    def tearDown(self):
        self.tmp.cleanup()

    def test_built_folder_passes(self):
        self.assertEqual(chk.check_folder(self.dir).errors, [])
        html = (self.dir / "report.html").read_text()
        self.assertNotIn('src="report-data.js"', html)
        self.assertEqual(build.embedded(html), json.loads((self.dir / "report-data.json").read_text()))

    def test_stale_html_is_caught(self):
        p = self.dir / "report-data.json"
        d = json.loads(p.read_text())
        d["narrative"]["answer"] = "changed after the build"
        p.write_text(json.dumps(d))
        self.assertTrue(any("rebuild" in e for e in chk.check_folder(self.dir).errors))

    def test_code_cannot_hide_in_json(self):
        (self.dir / "report-data.json").write_text('{"idea": alert(1)}')
        with self.assertRaises(SystemExit):
            build.load_data(self.dir)


class Calibrate(unittest.TestCase):
    def test_targets(self):
        import contextlib
        import io
        w = Workspace()
        with contextlib.redirect_stdout(io.StringIO()):
            res = cal.report(cal.verdicts([w.ideas]))
            ok = cal.targets(res, {"pet-dropshipping-tiktok": "failed", "dental-ai-receptionist": "worked"})
        self.assertEqual(sorted(res["scores"].values()), [49, 51])
        self.assertFalse(ok)
        w.tmp.cleanup()

    def test_rescore_matches_checker_with_default_weights(self):
        w = Workspace()
        for v in cal.verdicts([w.ideas]):
            self.assertEqual(cal.rescore(v, dict(chk.WEIGHTS)), v["score"])
        w.tmp.cleanup()


class Csp(unittest.TestCase):
    def test_templates_are_pinned(self):
        self.assertEqual(csp.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main()
