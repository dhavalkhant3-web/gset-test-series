#!/usr/bin/env python3
"""Non-destructive integrity checks for Subject 02/03 MCQ recovery.

Checks counts, unique IDs, overlays, metadata and loader exclusions. It does not
claim full question-text/options verification against official scanned papers.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "physical": ROOT / "assets/subjects/physical_sciences/questions.json",
    "physical_sep16": ROOT / "assets/subjects/physical_sciences/questions_sep16_p2.json",
    "physical_p3": ROOT / "assets/subjects/physical_sciences/questions_sep16_p3.json",
    "chemical": ROOT / "assets/subjects/chemical_sciences/questions.json",
    "chemical_sep16": ROOT / "assets/subjects/chemical_sciences/questions_sep16_p2.json",
    "chemical_p3": ROOT / "assets/subjects/chemical_sciences/questions_sep16_p3.json",
    "subjects": ROOT / "assets/subjects/subjects.json",
    "physical_papers": ROOT / "assets/subjects/physical_sciences/papers.json",
    "chemical_papers": ROOT / "assets/subjects/chemical_sciences/papers.json",
    "dart": ROOT / "lib/main.dart",
}

def fail(message: str) -> None:
    print("FAIL: " + message, file=sys.stderr)
    raise SystemExit(1)

def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")

def bank(path: Path, expected: int, label: str):
    data = read_json(path)
    if not isinstance(data, list) or len(data) != expected:
        fail(f"{label}: expected {expected} records")
    ids = [q.get("id") for q in data]
    if any(not isinstance(qid, str) or not qid for qid in ids):
        fail(f"{label}: blank/missing record ID")
    if len(set(ids)) != len(ids):
        fail(f"{label}: duplicate IDs")
    for q in data:
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(f"{label}: blank question text on {q.get('id')}")
        options = q.get("options_en")
        # Do not reject existing OCR/source-review records merely because their
        # options need manual reconstruction; require a documented review flag.
        if not isinstance(options, list) or (len(options) != 4 and q.get("review_flag") is not True):
            fail(f"{label}: {q.get('id')} needs four options unless explicitly review-flagged")
        if q.get("review_flag") is True and not (isinstance(q.get("review_note"), str) and q["review_note"].strip()):
            fail(f"{label}: {q.get('id')} is review-flagged without a note")
    return data

def main():
    physical = bank(FILES["physical"], 1300, "Physical Sciences main bank")
    physical16 = bank(FILES["physical_sep16"], 50, "Physical Sciences Sep 2016 overlay")
    physical_p3 = bank(FILES["physical_p3"], 75, "Physical Sciences Paper-III archive")
    chemical = bank(FILES["chemical"], 1250, "Chemical Sciences main bank")
    chemical16 = bank(FILES["chemical_sep16"], 50, "Chemical Sciences Sep 2016 overlay")
    chemical_p3 = bank(FILES["chemical_p3"], 75, "Chemical Sciences Paper-III archive")

    phys_ids = {q["id"] for q in physical}
    phys16_ids = {q["id"] for q in physical16}
    expected_phys16 = {f"physical_sep16_q{n:02d}" for n in range(1, 51)}
    if phys16_ids != expected_phys16 or not expected_phys16.issubset(phys_ids):
        fail("Physical Sciences Sep 2016 Q01-Q50 must already be present in the main bank")
    if phys_ids & {q["id"] for q in physical_p3}:
        fail("Physical Sciences Paper-III IDs overlap the Paper-II bank")

    chem_ids = {q["id"] for q in chemical}
    chem16_ids = {q["id"] for q in chemical16}
    expected_chem16 = {f"chemical_sep16_q{n}" for n in range(1, 51)}
    if chem16_ids != expected_chem16:
        fail("Chemical Sciences Sep 2016 supplement must contain Q1-Q50")
    if chem_ids & chem16_ids:
        fail("Chemical Sciences Sep 2016 Paper-II overlay duplicates main-bank IDs")
    if (chem_ids | chem16_ids) & {q["id"] for q in chemical_p3}:
        fail("Chemical Sciences Paper-III IDs must stay outside the Paper-II bank")

    dart = FILES["dart"].read_text(encoding="utf-8")
    if "assets/subjects/physical_sciences/questions_sep16_p2.json" in dart:
        fail("Physical Sciences loader still references duplicate Sep 2016 overlay")
    if "assets/subjects/physical_sciences/questions_sep16_p3.json" in dart:
        fail("Physical Sciences Paper-III is incorrectly referenced by the Paper-II loader")
    if "assets/subjects/chemical_sciences/questions_sep16_p2.json" not in dart:
        fail("Chemical Sciences loader must append its unique Sep 2016 Paper-II supplement")
    if "assets/subjects/chemical_sciences/questions_sep16_p3.json" in dart:
        fail("Chemical Sciences Paper-III is incorrectly referenced by the Paper-II loader")

    registry = read_json(FILES["subjects"])
    subjects = {str(s.get("code")): s for s in registry.get("subjects", [])}
    if subjects.get("02", {}).get("questions_loaded") != 1300:
        fail("Subject 02 metadata count must be 1,300")
    if subjects.get("03", {}).get("questions_loaded") != 1300:
        fail("Subject 03 metadata count must be 1,300")
    print("PASS: Physical Sciences has 1,300 unique main-bank records; Sep 2016 overlay is duplicate and excluded.")
    print("PASS: Chemical Sciences has 1,250 + 50 unique Sep 2016 Paper-II records.")
    print("PASS: Paper-III remains separate; subject metadata counts match Paper-II totals.")
    print("NOTE: this integrity validator does not certify every question stem/option against official scans.")

if __name__ == "__main__":
    main()
