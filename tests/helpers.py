"""Shared helpers: load the hyphenated scripts as modules and copy fixtures to a temp folder."""
import importlib.util
import json
import pathlib
import shutil
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"


def load(name):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class IdeaCopy:
    """A fixture idea folder copied to a temp dir, with the current report template next to it."""

    def __init__(self, fixture):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.tmp.name) / fixture
        shutil.copytree(FIXTURES / fixture, self.dir)
        shutil.copy(ROOT / "skills" / "kill" / "report.html", self.dir / "report.html")

    def verdict(self):
        return json.loads((self.dir / "verdict.json").read_text(encoding="utf-8"))

    def save(self, v):
        (self.dir / "verdict.json").write_text(json.dumps(v, ensure_ascii=False), encoding="utf-8")

    def close(self):
        self.tmp.cleanup()
