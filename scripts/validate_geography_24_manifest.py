#!/usr/bin/env python3
"""Guardrail validator for the Geography (GSET subject 24) source-audit manifest.

This validates audit bookkeeping only. It does NOT verify question transcription,
official answer keys, or declare any question source-verified.
"""
import json
import sys
from pathlib import Path

MANIFEST = Path("assets/subjects/geography_24/source_audit.json")
EXPECTED_SESSIONS = {
    "SEP-2016": 50,
    "AUG-2017": 50,
    "SEP-2018": 100,
    "DEC-2021": 100,
    "NOV-2022": 100,
    "NOV-2023": 100,
    "DEC-2024": 100,
    "NOV-2025": 100,
}

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def main() -> None:
    if not MANIFEST.is_file():
        fail(f"Missing manifest: {MANIFEST}")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("subject_code") != "24" or data.get("subject_name") != "Geography":
        fail("Manifest subject identity must be Geography (code 24).")
    if data.get("integration_status") != "not_loaded_into_app":
        fail("Do not claim app integration until the question bank is audited and loaded.")
    if data.get("question_count_loaded") != 0:
        fail("Question count must remain 0 until source-audited question JSON is integrated.")
    sessions = data.get("sessions")
    if not isinstance(sessions, list):
        fail("sessions must be a list.")
    by_name = {}
    for item in sessions:
        name = item.get("session")
        if name in by_name:
            fail(f"Duplicate session: {name}")
        by_name[name] = item
        if item.get("question_audit") != "pending" or item.get("answer_key_audit") != "pending":
            fail(f"{name}: audit status cannot be changed by this bookkeeping validator.")
        if item.get("review_flag_required") is not True:
            fail(f"{name}: review_flag_required must remain true until source review.")
        if not item.get("paper") or not item.get("key"):
            fail(f"{name}: both paper and official key filenames are required.")
    if set(by_name) != set(EXPECTED_SESSIONS):
        fail(f"Session inventory mismatch. Expected {sorted(EXPECTED_SESSIONS)}, found {sorted(by_name)}.")
    for name, expected in EXPECTED_SESSIONS.items():
        if by_name[name].get("expected_questions") != expected:
            fail(f"{name}: expected question count must be {expected}.")
        if by_name[name].get("paper_available") is not True or by_name[name].get("key_available") is not True:
            fail(f"{name}: source files must be marked available only when supplied.")
    print(f"PASS: Geography 24 audit manifest is structurally consistent ({len(sessions)} sessions).")
    print("NOTE: This does not validate any question stem, option, image, or answer key.")

if __name__ == "__main__":
    main()
