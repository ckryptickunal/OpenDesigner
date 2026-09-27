"""Read-only project board smoke and boundary tests."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("project_board", Path(__file__).with_name("project_board.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BoardTest(unittest.TestCase):
    def test_statuses_and_no_false_lineage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "opendesigner").mkdir()
            (root / "opendesigner/state.json").write_text(json.dumps({
                "name": "Example", "answers": {"Q-scope-01": {"value": "app", "set_by": "chosen", "decision": "D-0002"}},
                "hooks": {"H-logo": {"status": "have", "files": ["logo.svg"]}}
            }), encoding="utf-8")
            (root / "opendesigner/decisions.md").write_text(
                "# Decisions\n\n## D-0002 · answers.Q-scope-01 = \"app\"\n"
                "- set_by: chosen · locked: no · date: 2026-09-25 · supersedes: none · source_ref: none\n"
                "- reason: user said it\n", encoding="utf-8")
            (root / "DESIGN.md").write_text("sample", encoding="utf-8")
            data = module.board(root, questions=[
                {"id": "Q-scope-01", "ask": "Scope?"}, {"id": "Q-aud-01", "ask": "Audience?"},
                {"id": "Q-type-03", "ask": "More type?"}],
                hooks=[{"id": "H-logo", "kind": "asset", "name": "Logo", "questions": ["Q-brand-03"]}])
            self.assertEqual([r["status"] for r in data["inputs"]], ["received", "needed", "unrecorded"])
            self.assertEqual(data["assets"][0]["status"], "have")
            self.assertTrue(data["assets"][0]["file_presence_not_checked"])
            self.assertEqual(data["outputs"][0]["status"], "made")
            self.assertEqual(data["outputs"][3]["status"], "missing")
            self.assertEqual(data["decisions"][0]["reason"], "user said it")
            self.assertFalse((root / "opendesigner/board.json").exists())
            before = (root / "opendesigner/decisions.md").read_text(encoding="utf-8")
            self.assertEqual((root / "opendesigner/decisions.md").read_text(encoding="utf-8"), before)
            self.assertEqual(data["work"]["system"][0]["link"], "unlinked")
            view = module.markdown_board(data)
            self.assertIn("Audience?", view)
            self.assertIn("Logo: have (supplied)", view)

    def test_example_project(self):
        root = Path(__file__).resolve().parents[1] / "examples/devtool-dense"
        data = module.board(root)
        self.assertEqual(data["schema"], "opendesigner-project-board/1")
        self.assertTrue(any(x["id"] == "H-logo" for x in data["assets"]))
        self.assertTrue(any(x["status"] == "made" for x in data["outputs"]))

    def test_missing_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                module.board(tmp)

    def test_sketch_ids_come_from_the_catalog(self):
        self.assertEqual(module.sketch_ids({"zoom0": ["Q-only"]}), {"Q-only"})
        self.assertNotEqual(module.sketch_ids({"zoom0": ["Q-only"]}), module.SKETCH)
        catalog = json.loads(module.QUESTIONS.read_text(encoding="utf-8"))
        self.assertEqual(module.sketch_ids(catalog), set(catalog["zoom0"]))

    def test_declined_asset_and_superseded_decision_stay_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "opendesigner").mkdir()
            (root / "opendesigner/state.json").write_text(json.dumps({
                "name": "Example", "answers": {},
                "hooks": {"H-logo": {"status": "not-needed", "files": []}},
            }), encoding="utf-8")
            (root / "opendesigner/decisions.md").write_text(
                "# Decisions\n\n## D-0001 · raw.brandColor = \"#112233\"\n"
                "- set_by: chosen · locked: no · date: 2026-09-25 · supersedes: none · source_ref: none\n"
                "- reason: first\n\n## D-0002 · raw.brandColor = \"#445566\"\n"
                "- set_by: chosen · locked: no · date: 2026-09-25 · supersedes: D-0001 · source_ref: none\n"
                "- reason: changed\n", encoding="utf-8")
            data = module.board(root, questions=[{"id": "Q-color-01", "ask": "Color?", "area": "color"}],
                                hooks=[{"id": "H-logo", "kind": "asset", "name": "Logo", "questions": []}],
                                sketch={"Q-color-01"})
            self.assertEqual(data["inputs"][0]["status"], "needed")
            self.assertEqual(data["assets"][0]["board_status"], "declined")
            self.assertTrue(data["assets"][0]["file_presence_not_checked"])
            statuses = {item["id"]: item["status"] for item in data["work"]["color"]}
            self.assertEqual(statuses["D-0001"], "superseded")
            self.assertEqual(statuses["D-0002"], "chosen")
            self.assertNotIn("urllib", Path(module.__file__).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
