"""Regression tests for the fail-closed Mathematical Sciences bank validator.

Run with: python -m unittest discover -s tests -p 'test_validate_mathematical_sciences_bank.py'
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_mathematical_sciences_bank.py"


def valid_record():
    return {
        "id": "test-001",
        "paper_id": "test-session",
        "question_en": "If 1 + 1 = ?",
        "options_en": ["1", "2", "3", "4"],
        "question_gu": "1 + 1 = કેટલું?",
        "options_gu": ["1", "2", "3", "4"],
        "answer": "B",
        "explanation_en": "Adding one and one gives two.",
        "explanation_gu": "એક અને એકનો સરવાળો બે થાય છે.",
        "tip_en": "Check the arithmetic.",
        "tip_gu": "ગણતરી ચકાસો.",
        "source_verified": True,
        "review_flag": False,
    }


class ValidatorTests(unittest.TestCase):
    def run_validator(self, records):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bank = root / "assets" / "subjects" / "mathematical_sciences" / "questions.json"
            bank.parent.mkdir(parents=True)
            bank.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )

    def test_accepts_structurally_complete_verified_record(self):
        result = self.run_validator([valid_record()])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Records: 1", result.stdout)

    def test_rejects_missing_gujarati_translation(self):
        record = valid_record()
        record["question_gu"] = ""
        result = self.run_validator([record])
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required learning field question_gu", result.stdout)

    def test_rejects_wrong_number_of_gujarati_options(self):
        record = valid_record()
        record["options_gu"] = ["એક", "બે", "ત્રણ"]
        result = self.run_validator([record])
        self.assertEqual(result.returncode, 1)
        self.assertIn("expected four non-empty Gujarati options", result.stdout)

    def test_rejects_verified_record_still_flagged_for_review(self):
        record = valid_record()
        record["review_flag"] = True
        result = self.run_validator([record])
        self.assertEqual(result.returncode, 1)
        self.assertIn("source_verified record must have review_flag=false", result.stdout)

    def test_rejects_unverified_record_even_if_fields_are_complete(self):
        record = valid_record()
        record["source_verified"] = False
        record["review_flag"] = True
        result = self.run_validator([record])
        self.assertEqual(result.returncode, 1)
        self.assertIn("Records not source-verified: 1", result.stdout)

    def test_rejects_duplicate_ids(self):
        first = valid_record()
        second = valid_record()
        second["paper_id"] = "other-session"
        result = self.run_validator([first, second])
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing/duplicate IDs", result.stdout)


if __name__ == "__main__":
    unittest.main()
