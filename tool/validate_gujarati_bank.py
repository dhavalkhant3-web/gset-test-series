#!/usr/bin/env python3
"""Strict integrity validator for Gujarati (GSET Paper-II Code 06)."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ROOT / "assets/subjects"
ACTIVE_FILE = SUBJECTS / "gujarati/questions.json"
REVIEW_FILE = SUBJECTS / "gujarati/questions_review_pending.json"
PAPERS_FILE = SUBJECTS / "gujarati/papers.json"
AUDIT_FILE = SUBJECTS / "gujarati/source_audit.json"
REGISTRY_FILE = SUBJECTS / "subjects.json"
SYLLABUS_FILE = SUBJECTS / "syllabus_units.json"
ERRORS: list[str] = []


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")


def fail(message: str) -> None:
    ERRORS.append(message)


def unit_number(value: object, units: list[dict]) -> str | None:
    text = str(value).strip()
    if text.lower().startswith("unit "):
        text = text[5:].strip()
    for unit in units:
        if text in {str(unit.get("number")), str(unit.get("id"))}:
            return str(unit.get("number"))
    return None


def main() -> int:
    active = load(ACTIVE_FILE)
    review = load(REVIEW_FILE)
    papers_doc = load(PAPERS_FILE)
    audit = load(AUDIT_FILE)
    registry = load(REGISTRY_FILE)
    syllabus = load(SYLLABUS_FILE)

    if not all(isinstance(x, list) for x in (active, review)):
        fail("active and review banks must both be JSON arrays")
        return report()

    config = syllabus.get("subjects", {}).get("gujarati", {})
    units = config.get("units", [])
    if not config.get("official_pdf", "").startswith("https://gujaratset.ac.in/assets/syllabus/06.pdf"):
        fail("Gujarati official Code 06 syllabus URL missing or incorrect")
    if len(units) != 10:
        fail(f"expected 10 configured Gujarati syllabus units, found {len(units)}")
    valid_numbers = {str(u.get("number")) for u in units}

    all_questions = active + review
    ids: set[str] = set()
    by_paper: dict[str, list[dict]] = {}
    for bank_name, bank, is_active in (
        ("active", active, True),
        ("review-only", review, False),
    ):
        for index, q in enumerate(bank, 1):
            qid = str(q.get("id") or "")
            if not qid:
                fail(f"{bank_name}[{index}] missing question ID")
            elif qid in ids:
                fail(f"duplicate question ID: {qid}")
            ids.add(qid)

            paper_id = str(q.get("paper_id") or q.get("paperId") or "")
            if not paper_id:
                fail(f"{qid or bank_name}: missing paper_id")
            by_paper.setdefault(paper_id, []).append(q)

            if not isinstance(q.get("question_gu"), str) or not q["question_gu"].strip():
                fail(f"{qid}: Gujarati question stem is empty")
            options = q.get("options_gu")
            if not isinstance(options, list) or len(options) != 4 or any(
                not isinstance(option, str) or not option.strip() for option in (options or [])
            ):
                fail(f"{qid}: options_gu must contain exactly four non-empty strings")

            answer = str(q.get("answer") or "")
            if answer not in {"A", "B", "C", "D", "Z"}:
                fail(f"{qid}: invalid answer {answer!r}")
            if is_active:
                if answer not in {"A", "B", "C", "D"}:
                    fail(f"{qid}: non-scoring answer cannot be active")
                if q.get("source_verified") is not True:
                    fail(f"{qid}: active record is not source-verified")
                if q.get("answer_key_verified") is not True:
                    fail(f"{qid}: active record lacks official final-key verification")
                if q.get("review_flag") is not False:
                    fail(f"{qid}: active record must have review_flag=false")
            else:
                if q.get("review_flag") is not True:
                    fail(f"{qid}: review-only record must have review_flag=true")

            if q.get("syllabus_mapping_status") != "verified":
                fail(f"{qid}: syllabus mapping status is not verified")
            values = []
            for field in ("syllabus_unit", "unit_number", "unit_id"):
                value = q.get(field)
                if value in (None, ""):
                    fail(f"{qid}: missing {field}")
                    continue
                resolved = unit_number(value, units)
                if resolved is None:
                    fail(f"{qid}: {field}={value!r} is not a configured official unit")
                else:
                    values.append(resolved)
            if len(values) == 3 and len(set(values)) != 1:
                fail(f"{qid}: conflicting syllabus unit fields {values}")
            if not str(q.get("syllabus_mapping_note") or "").strip():
                fail(f"{qid}: syllabus_mapping_note missing")

    if len(all_questions) != len(ids):
        fail("question ID uniqueness check failed")
    if len(all_questions) != 400:
        fail(f"expected 400 Gujarati questions across six sessions, found {len(all_questions)}")

    papers = papers_doc.get("papers", [])
    if not isinstance(papers, list):
        fail("papers.json must contain a papers array")
        papers = []
    paper_meta = {str(p.get("paper_id")): p for p in papers}
    if set(paper_meta) != set(by_paper):
        fail("papers.json paper IDs do not exactly match canonical question paper IDs")

    for paper_id, questions in by_paper.items():
        meta = paper_meta.get(paper_id)
        if not meta:
            continue
        active_count = sum(q in active for q in questions)
        review_count = len(questions) - active_count
        source_count = sum(q.get("source_verified") is True for q in questions)
        final_count = sum(q.get("answer_key_verified") is True for q in questions)
        mapping_count = sum(q.get("syllabus_mapping_status") == "verified" for q in questions)
        expected = {
            "question_count": len(questions),
            "questions_transcribed": len(questions),
            "questions_loaded": active_count,
            "questions_count": active_count,
            "review_flags_remaining_count": review_count,
            "question_source_verified": source_count,
            "final_key_verified_count": final_count,
            "answer_key_reconciled_count": final_count,
            "syllabus_mapping_verified": mapping_count,
        }
        for field, value in expected.items():
            if meta.get(field) != value:
                fail(f"{paper_id}: {field}={meta.get(field)!r}, expected {value}")
        if meta.get("answer_key_verified") is not all(
            q.get("answer_key_verified") is True for q in questions
        ):
            fail(f"{paper_id}: answer_key_verified aggregate is inconsistent")

    registry_entries = registry.get("subjects", [])
    gujarati = next((x for x in registry_entries if str(x.get("code")) == "06"), None)
    if not gujarati:
        fail("subjects.json has no Gujarati Code 06 entry")
    else:
        expected_registry = {
            "papers_loaded": len(by_paper),
            "questions_loaded": len(active),
            "questions_pending_review": len(review),
        }
        for field, value in expected_registry.items():
            if gujarati.get(field) != value:
                fail(f"subjects.json Gujarati {field}={gujarati.get(field)!r}, expected {value}")
        if gujarati.get("source_verified") is True and any(
            q.get("source_verified") is not True for q in all_questions
        ):
            fail("subject-level source_verified cannot be true while any question source is unverified")

    source_total = sum(q.get("source_verified") is True for q in all_questions)
    final_total = sum(q.get("answer_key_verified") is True for q in all_questions)
    mapping_total = sum(q.get("syllabus_mapping_status") == "verified" for q in all_questions)
    expected_audit = {
        "transcribed_questions": len(all_questions),
        "active_questions": len(active),
        "pending_review": len(review),
        "visual_checked": source_total,
    }
    for field, value in expected_audit.items():
        if audit.get(field) != value:
            fail(f"source_audit.json {field}={audit.get(field)!r}, expected {value}")
    checkpoint = audit.get("live_review_queue_checkpoint", {})
    checkpoint_expected = {
        "active_questions": len(active),
        "pending_review": len(review),
        "unique_pending_ids": len(review),
        "source_verified_total": source_total,
        "answer_key_verified_total": final_total,
    }
    for field, value in checkpoint_expected.items():
        if checkpoint.get(field) != value:
            fail(f"source_audit live checkpoint {field}={checkpoint.get(field)!r}, expected {value}")
    if mapping_total != len(all_questions):
        fail(f"only {mapping_total}/{len(all_questions)} records have verified syllabus mapping status")

    return report()


def report() -> int:
    if ERRORS:
        print("FAIL: Gujarati Code 06 validation found:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("PASS: Gujarati Code 06 canonical data, active/review separation, official key flags,")
    print("      syllabus references, papers metadata, registry counters and audit counters agree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
