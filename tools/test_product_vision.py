#!/usr/bin/env python3
"""Lock the repository facts named in docs/PRODUCT-VISION.md. No network."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class VisionGrounding(unittest.TestCase):
    def test_the_vision_matches_files_that_exist(self):
        self.assertTrue((ROOT / "skills/opendesigner/scripts/engine.py").is_file())
        templates = list((ROOT / "skills/opendesigner/assets/templates").glob("*.html"))
        self.assertGreaterEqual(len(templates), 8)
        journey = (ROOT / "skills/opendesigner/scripts/journey.py").read_text(encoding="utf-8")
        self.assertIn("def analyze(", journey)
        engine = (ROOT / "skills/opendesigner/scripts/engine.py").read_text(encoding="utf-8")
        self.assertNotIn("suggest_flow", engine)
        instructions = (ROOT / "chatgpt-project/instructions.md").read_text(encoding="utf-8")
        self.assertIn("no journey log", instructions)
        vision = (ROOT / "docs/PRODUCT-VISION.md").read_text(encoding="utf-8")
        self.assertIn("Front-end engineers", vision)
        self.assertIn("does not assert demand", vision)
        self.assertIn("tools/test_product_vision.py", vision)


if __name__ == "__main__":
    unittest.main()
