#!/usr/bin/env python3
"""Evidence-sensitive structural checks for GSET Music subject code 30.

This validator checks record integrity and that stored progress metadata agrees
with question-level evidence. It never promotes a record to verified status.
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
MAPPING_DONE = "manually_reviewed_official_syllabus"


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


def mapping_is_reviewed(question: dict) -> bool:
    return question.get("syllabus_mapping_status") == MAPPING_DONE


def question_gates_complete(question: dict) -> bool:
    """All represented gates must be evidenced before a question can be unflagged."""
    return (
        question.get("source_verified") is True
        and question.get("answer_key_visual_verified") is True
        and mapping_is_reviewed(question)
    )


def expected_review_flag(question: dict) -> bool:
    return not question_gates_complete(question)


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
    units = syllabus_data.get("subjects", {}).get("music", {}).get("units", [])
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
        paper_id: {
            "total": 0, "gujarati_complete": 0, "missing_question_numbers": [],
            "source_verified": 0, "review_flags": 0, "visual_proofread": 0,
            "mapping_reviewed": 0, "mapping_ambiguous": 0,
            "answer_key_visual_checked": 0, "fully_verified": 0,
        }
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
        p = per_paper[paper_id]
        p["total"] += 1

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
        gu_complete = isinstance(options_gu, list) and len(options_gu) == 4 and all(nonblank(x) for x in options_gu)
        if gu_stem and gu_complete:
            p["gujarati_complete"] += 1
        else:
            p["missing_question_numbers"].append(qno)

        source_verified = q.get("source_verified") is True
        if source_verified:
            status = str(q.get("verification_status") or "")
            note = str(q.get("review_note") or "")
            if "question_text_options_visually_proofread" not in status:
                errors.append(f"{qid}: source_verified=true without visual-proofreading status evidence")
            if "original official GSET" not in note:
                errors.append(f"{qid}: source_verified=true without an original official GSET source note")
        if q.get("source_verified") not in (True, False):
            errors.append(f"{qid}: source_verified must be boolean")
        if q.get("review_flag") is not expected_review_flag(q):
            errors.append(
                f"{qid}: review_flag must be {expected_review_flag(q)} based on source, answer-key, and mapping gates"
            )

        p["source_verified"] += int(source_verified)
        p["review_flags"] += int(q.get("review_flag") is True)
        p["visual_proofread"] += int(source_verified)
        p["mapping_reviewed"] += int(mapping_is_reviewed(q))
        p["mapping_ambiguous"] += int(q.get("syllabus_mapping_status") == "manual_review_required")
        p["answer_key_visual_checked"] += int(q.get("answer_key_visual_verified") is True)
        p["fully_verified"] += int(question_gates_complete(q))
        counts["source_verified_true"] += int(source_verified)
        counts["review_flag_true"] += int(q.get("review_flag") is True)
        counts["fully_verified"] += int(question_gates_complete(q))
        counts["mapping_reviewed"] += int(mapping_is_reviewed(q))
        counts["answer_key_visual_checked"] += int(q.get("answer_key_visual_verified") is True)

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
        if not nonblank(q.get("syllabus_mapping_status")):
            errors.append(f"{qid}: missing syllabus_mapping_status")

    for paper_id, exam in EXPECTED.items():
        p = per_paper[paper_id]
        meta = paper_meta.get(paper_id, {})
        report = report_by_id.get(paper_id, {})
        if p["total"] != 100:
            errors.append(f"{paper_id}: expected 100 records, found {p['total']}")
        if set(qno for pid, qno in session_questions if pid == paper_id) != set(range(1, 101)):
            errors.append(f"{paper_id}: question numbers are not exactly 1–100")
        if meta.get("exam") != exam:
            errors.append(f"{paper_id}: exam label does not match expected session")
        if meta.get("answer_key_verified") is not True:
            errors.append(f"{paper_id}: parsed answer-key reconciliation metadata is not marked complete")
        for field, expected in (
            ("source_verified", p["source_verified"] == p["total"]),
            ("question_source_verified", p["source_verified"] == p["total"]),
            ("gujarati_transcribed_count", p["gujarati_complete"]),
            ("gujarati_transcription_pending_count", len(p["missing_question_numbers"])),
            ("visual_questions_checked_count", p["visual_proofread"]),
            ("syllabus_mapping_manual_reviewed_count", p["mapping_reviewed"]),
            ("syllabus_mapping_ambiguous_count", p["mapping_ambiguous"]),
            ("answer_key_visual_checked_count", p["answer_key_visual_checked"]),
        ):
            if meta.get(field) != expected:
                errors.append(f"{paper_id}: papers.json {field} is stale (expected {expected!r})")
        if report.get("total") != p["total"]:
            errors.append(f"{paper_id}: verification report total is stale")
        if report.get("gujarati_complete") != p["gujarati_complete"]:
            errors.append(f"{paper_id}: verification report Gujarati-complete count is stale")
        if report.get("gujarati_missing") != len(p["missing_question_numbers"]):
            errors.append(f"{paper_id}: verification report Gujarati-missing count is stale")
        if sorted(report.get("missing_question_numbers", [])) != sorted(p["missing_question_numbers"]):
            errors.append(f"{paper_id}: exact missing Gujarati question list is stale")
        for field, expected in (
            ("visual_questions_checked_count", p["visual_proofread"]),
            ("syllabus_mapping_manual_reviewed_count", p["mapping_reviewed"]),
            ("syllabus_mapping_ambiguous_count", p["mapping_ambiguous"]),
            ("answer_key_visual_checked_count", p["answer_key_visual_checked"]),
            ("source_verified", p["source_verified"] == p["total"]),
            ("question_source_verified", p["source_verified"] == p["total"]),
        ):
            if report.get(field) != expected:
                errors.append(f"{paper_id}: verification report {field} is stale (expected {expected!r})")

    for field, expected in (
        ("fully_verified_questions", counts["fully_verified"]),
        ("source_verified_field_count", counts["source_verified_true"]),
        ("review_flags", counts["review_flag_true"]),
    ):
        if pending.get(field) != expected:
            errors.append(f"{field} differs from question-level gates (expected {expected})")

    answer_audit = pending.get("answer_key_audit", {})
    if answer_audit.get("questions") != len(bank):
        errors.append("answer-key audit question count differs from actual bank size")
    if answer_audit.get("visually_checked_questions") != counts["answer_key_visual_checked"]:
        errors.append("answer-key audit visually_checked_questions differs from question-level evidence")
    if answer_audit.get("direct_visual_check_remaining") != len(bank) - counts["answer_key_visual_checked"]:
        errors.append("answer-key audit direct_visual_check_remaining is stale")

    progress = pending.get("visual_audit_progress", {})
    for field, expected in (
        ("total_questions", len(bank)),
        ("visually_proofread_questions", counts["source_verified_true"]),
        ("remaining_questions", len(bank) - counts["source_verified_true"]),
        ("english_stem_and_options_checked", counts["source_verified_true"]),
        ("gujarati_stem_and_options_checked", counts["source_verified_true"]),
        ("unit_mapping_manual_reviewed", counts["mapping_reviewed"]),
        ("answer_key_visual_checked", counts["answer_key_visual_checked"]),
        ("answer_key_visual_remaining", len(bank) - counts["answer_key_visual_checked"]),
    ):
        if progress.get(field) != expected:
            errors.append(f"visual_audit_progress.{field} is stale (expected {expected})")

    if not music_registry:
        errors.append("Music subject code 30 is missing from subjects.json")
    else:
        if music_registry.get("papers_loaded") != 3:
            errors.append("subjects.json Music papers_loaded must be 3")
        if music_registry.get("questions_loaded") != len(bank):
            errors.append("subjects.json Music questions_loaded differs from question bank")
        if music_registry.get("source_verified") is not (counts["source_verified_true"] == len(bank)):
            errors.append("subjects.json Music source_verified must reflect all question records")
        expected_review_text = f"{counts['review_flag_true']} of {len(bank)} questions remain review-flagged"
        if expected_review_text not in str(music_registry.get("data_status", "")):
            errors.append("subjects.json Music data_status does not include the current review-flag count")

    if errors:
        fail("Music subject validation errors:\n- " + "\n- ".join(errors[:100]))

    for paper_id, exam in EXPECTED.items():
        p = per_paper[paper_id]
        print(
            f"PASS {exam}: {p['total']} records; Gujarati complete "
            f"{p['gujarati_complete']}/100; source-proofread {p['source_verified']}/100; "
            f"mapping reviewed {p['mapping_reviewed']}/100; key visually checked "
            f"{p['answer_key_visual_checked']}/100; flagged {p['review_flags']}/100"
        )
    print(
        f"PASS structural checks: {len(bank)} unique IDs; {counts['fully_verified']} questions "
        f"passed all represented gates; {counts['review_flag_true']} remain flagged; "
        f"{counts['source_verified_true']} source-proofread; "
        f"{counts['answer_key_visual_checked']} direct visual answer-key checks."
    )
    print("NOTE: Parsed answer-key agreement is not the same as direct visual answer-key verification.")


if __name__ == "__main__":
    main()
