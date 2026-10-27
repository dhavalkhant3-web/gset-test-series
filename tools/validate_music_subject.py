#!/usr/bin/env python3
"""Structural integrity checks for the existing GSET Music (subject code 30) bank.

This script does not claim source-visual verification or decide the semantic
correctness of a syllabus-unit assignment. It checks the repository's data and
progress report for internal consistency without promoting verification flags.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MUSIC_DIR = ROOT / "assets" / "subjects" / "music"
BANK_PATH = MUSIC_DIR / "questions.json"
PAPERS_PATH = MUSIC_DIR / "papers.json"
PENDING_PATH = MUSIC_DIR / "verification_pending.json"
REGISTRY_PATH = ROOT / "assets" / "subjects" / "subjects.json"
SYLLABUS_PATH = ROOT / "assets" / "subjects" / "syllabus_units.json"
EXPECTED = {
    "music_nov23": "November 2023",
    "music_dec24": "December 2024",
    "music_nov25": "November 2025",
}
VALID_ANSWERS = {"A", "B", "C", "D", "X", "Z"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")


def nonblank(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def main() -> None:
    bank = load_json(BANK_PATH)
    papers_data = load_json(PAPERS_PATH)
    pending = load_json(PENDING_PATH)
    registry_data = load_json(REGISTRY_PATH)
    syllabus_data = load_json(SYLLABUS_PATH)

    if not isinstance(bank, list):
        fail("Music question bank root must be a JSON array")
    paper_meta_list = papers_data.get("papers", [])
    report_papers = pending.get("papers", [])
    paper_meta = {p.get("paper_id"): p for p in paper_meta_list}
    report_by_id = {p.get("paper_id"): p for p in report_papers}
    music_registry = next(
        (s for s in registry_data.get("subjects", [])
         if str(s.get("code")) == "30" and s.get("id") == "music"),
        None,
    )
    syllabus = syllabus_data.get("subjects", {}).get("music", {})
    units = syllabus.get("units", [])
    unit_by_num = {str(u.get("number")): u for u in units}
    errors: list[str] = []

    if len(bank) != 300:
        errors.append(f"expected 300 question records, found {len(bank)}")
    if set(paper_meta) != set(EXPECTED):
        errors.append(f"paper metadata keys differ from expected sessions: {sorted(paper_meta)}")
    if set(report_by_id) != set(EXPECTED):
        errors.append(f"verification report keys differ from expected sessions: {sorted(report_by_id)}")
    if len(paper_meta_list) != len(paper_meta):
        errors.append("duplicate paper_id in papers.json")
    if len(report_papers) != len(report_by_id):
        errors.append("duplicate paper_id in verification_pending.json")
    if len(units) != 10 or len(unit_by_num) != len(units):
        errors.append("Music syllabus config must contain ten uniquely numbered units")

    ids: set[str] = set()
    session_questions: set[tuple[str, int]] = set()
    counts = Counter()
    per_paper = {
        paper_id: {"total": 0, "gujarati_complete": 0, "missing_question_numbers": []}
        for paper_id in EXPECTED
    }

    for q in bank:
        qid = str(q.get("id") or "")
        paper_id = str(q.get("paper_id") or "")
        qno = q.get("question_no")

        if not qid:
            errors.append("record with missing question id")
        elif qid in ids:
            errors.append(f"duplicate question id {qid}")
        ids.add(qid)

        if paper_id not in EXPECTED:
            errors.append(f"{qid or '(missing id)'}: unexpected paper_id {paper_id!r}")
            continue
        if not isinstance(qno, int) or isinstance(qno, bool) or not 1 <= qno <= 100:
            errors.append(f"{qid}: invalid question_no {qno!r}")
            continue
        key = (paper_id, qno)
        if key in session_questions:
            errors.append(f"{paper_id}: duplicate question number {qno}")
        session_questions.add(key)
        per_paper[paper_id]["total"] += 1

        if not nonblank(q.get("question_en")):
            errors.append(f"{qid}: English stem is blank")
        options_en = q.get("options_en")
        if not isinstance(options_en, list) or len(options_en) != 4 or not all(nonblank(x) for x in options_en):
            errors.append(f"{qid}: expected four nonblank English options")

        answer = str(q.get("answer") or "").strip().upper()
        official_answer = str(q.get("official_answer") or "").strip().upper()
        if answer not in VALID_ANSWERS:
            errors.append(f"{qid}: invalid answer value {answer!r}")
        if official_answer not in VALID_ANSWERS:
            errors.append(f"{qid}: invalid official_answer value {official_answer!r}")
        if answer != official_answer:
            errors.append(f"{qid}: answer differs from stored official_answer field")

        gu_stem = nonblank(q.get("question_gu"))
        options_gu = q.get("options_gu")
        gu_options_complete = (
            isinstance(options_gu, list)
            and len(options_gu) == 4
            and all(nonblank(x) for x in options_gu)
        )
        if gu_stem and gu_options_complete:
            per_paper[paper_id]["gujarati_complete"] += 1
        else:
            per_paper[paper_id]["missing_question_numbers"].append(qno)

        if q.get("source_verified") is not False:
            errors.append(f"{qid}: must remain source_verified=false until source review is complete")
        if q.get("review_flag") is not True:
            errors.append(f"{qid}: must remain review_flag=true until all review gates are complete")
        counts["source_verified_true"] += q.get("source_verified") is True
        counts["review_flag_true"] += q.get("review_flag") is True

        unit_num = q.get("syllabus_unit")
        unit_key = str(unit_num)
        unit = unit_by_num.get(unit_key)
        if unit is None:
            errors.append(f"{qid}: syllabus_unit {unit_num!r} is not configured")
        else:
            if str(q.get("unit_number")) != unit_key:
                errors.append(f"{qid}: unit_number conflicts with syllabus_unit")
            if str(q.get("unit_id")) != str(unit.get("id")):
                errors.append(f"{qid}: unit_id conflicts with configured unit number")
        mapping_status = str(q.get("syllabus_mapping_status") or "")
        if "provisional" not in mapping_status.lower() and "pending" not in mapping_status.lower():
            errors.append(f"{qid}: mapping status must remain provisional/pending manual review")

    for paper_id, exam in EXPECTED.items():
        actual = per_paper[paper_id]
        meta = paper_meta.get(paper_id, {})
        report = report_by_id.get(paper_id, {})
        if actual["total"] != 100:
            errors.append(f"{paper_id}: expected 100 records, found {actual['total']}")
        if set(qno for pid, qno in session_questions if pid == paper_id) != set(range(1, 101)):
            errors.append(f"{paper_id}: question numbers are not exactly 1–100")
        if meta.get("exam") != exam:
            errors.append(f"{paper_id}: exam label does not match expected session")
        if meta.get("answer_key_verified") is not True:
            errors.append(f"{paper_id}: answer-key audit metadata is not marked complete")
        if meta.get("source_verified") is not False or meta.get("question_source_verified") is not False:
            errors.append(f"{paper_id}: source-verification metadata must remain false")
        if meta.get("gujarati_transcribed_count") != actual["gujarati_complete"]:
            errors.append(f"{paper_id}: papers.json Gujarati-complete count is stale")
        missing_nums = sorted(actual["missing_question_numbers"])
        if meta.get("gujarati_transcription_pending_count") != len(missing_nums):
            errors.append(f"{paper_id}: papers.json Gujarati-pending count is stale")
        if report.get("total") != actual["total"]:
            errors.append(f"{paper_id}: verification report total is stale")
        if report.get("gujarati_complete") != actual["gujarati_complete"]:
            errors.append(f"{paper_id}: verification report Gujarati-complete count is stale")
        if report.get("gujarati_missing") != len(missing_nums):
            errors.append(f"{paper_id}: verification report Gujarati-missing count is stale")
        if sorted(report.get("missing_question_numbers", [])) != missing_nums:
            errors.append(f"{paper_id}: exact missing Gujarati question list is stale")

    if pending.get("fully_verified_questions") != counts["source_verified_true"]:
        errors.append("fully_verified_questions differs from actual source_verified records")
    if pending.get("source_verified_field_count") != counts["source_verified_true"]:
        errors.append("source_verified_field_count differs from actual source_verified records")
    if pending.get("review_flags") != counts["review_flag_true"]:
        errors.append("review_flags differs from actual review_flag records")

    answer_audit = pending.get("answer_key_audit", {})
    if answer_audit.get("questions") != len(bank):
        errors.append("answer-key audit question count differs from actual bank size")

    if not music_registry:
        errors.append("Music subject code 30 is missing from subjects.json")
    else:
        if music_registry.get("papers_loaded") != 3:
            errors.append("subjects.json Music papers_loaded must be 3")
        if music_registry.get("questions_loaded") != len(bank):
            errors.append("subjects.json Music questions_loaded differs from question bank")
        if music_registry.get("source_verified") is not False:
            errors.append("subjects.json Music source_verified must remain false")

    if errors:
        fail("Music subject validation errors:\n- " + "\n- ".join(errors[:100]))

    for paper_id, exam in EXPECTED.items():
        p = per_paper[paper_id]
        print(
            f"PASS {exam}: {p['total']} records; "
            f"Gujarati stem + four options complete {p['gujarati_complete']}/100; "
            f"pending {len(p['missing_question_numbers'])}"
        )
    print(
        f"PASS structural checks: {len(bank)} unique question IDs; "
        f"answer fields match stored official_answer fields; "
        f"{counts['review_flag_true']} records remain flagged; "
        f"{counts['source_verified_true']} source-verified."
    )
    print(
        "NOTE: This script verifies repository structure and progress-report consistency only. "
        "It does not visually compare question text/figures with original PDFs, independently "
        "recalculate official answer keys, or confirm semantic syllabus-unit assignments."
    )


if __name__ == "__main__":
    main()
