"""Unit tests for Music question-level review gates."""
import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).with_name("validate_music_subject.py")
SPEC = importlib.util.spec_from_file_location("validate_music_subject", MODULE_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ReviewGateTests(unittest.TestCase):
    def test_fully_verified_question_can_clear_review_flag(self):
        question = {
            "source_verified": True,
            "answer_key_visual_verified": True,
            "syllabus_mapping_status": "manually_reviewed_official_syllabus",
        }
        self.assertTrue(VALIDATOR.question_gates_complete(question))
        self.assertFalse(VALIDATOR.expected_review_flag(question))

    def test_source_verified_but_mapping_pending_stays_flagged(self):
        question = {
            "source_verified": True,
            "answer_key_visual_verified": True,
            "syllabus_mapping_status": "manual_review_required",
        }
        self.assertFalse(VALIDATOR.question_gates_complete(question))
        self.assertTrue(VALIDATOR.expected_review_flag(question))

    def test_ocr_only_question_stays_flagged(self):
        question = {
            "source_verified": False,
            "answer_key_visual_verified": False,
            "syllabus_mapping_status": "topic_reviewed_provisional_stream_review_pending",
        }
        self.assertFalse(VALIDATOR.question_gates_complete(question))
        self.assertTrue(VALIDATOR.expected_review_flag(question))

    def test_visual_answer_key_gate_is_independent(self):
        question = {
            "source_verified": True,
            "answer_key_visual_verified": False,
            "syllabus_mapping_status": "manually_reviewed_official_syllabus",
        }
        self.assertTrue(VALIDATOR.expected_review_flag(question))


if __name__ == "__main__":
    unittest.main()
