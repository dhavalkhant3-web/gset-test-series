#!/usr/bin/env python3
"""Geography Code 24 canonical bank schema, source-state and official-key validator."""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECT = ROOT / "assets/subjects/geography"
BANK = SUBJECT / "questions.json"
PENDING = SUBJECT / "questions_review_pending.json"
KEYS = SUBJECT / "official_final_keys.json"
PAPERS = SUBJECT / "papers.json"
REGISTRY = ROOT / "assets/subjects/subjects.json"

REQUIRED = {
    "id", "paper_id", "paperId", "question_no", "question_en", "question_gu",
    "options_en", "options_gu", "answer", "official_answer", "answer_key_verified",
    "source_verified", "review_flag", "review_note", "topic", "syllabus_mapping_status",
    "difficulty", "exam_session", "exam_date", "source_booklet_sl_no",
    "source_question_id", "source_question_paper", "answer_source", "passage_en",
    "passage_gu", "explanation_en", "explanation_gu", "tip_en", "tip_gu",
    "has_figure", "image_asset", "verification_status", "evaluation_status",
    "source_question_paper_url", "source_verification_note", "syllabus_unit",
}
PAPER_KEYS = {
    "geography_sep2016": "SEP2016", "geography_aug2017": "AUG2017",
    "geography_sep2018": "SEP2018", "geography_dec2021": "DEC2021",
    "geography_nov2022": "NOV2022", "geography_nov2023": "NOV2023",
    "geography_dec2024": "DEC2024", "geography_nov2025": "NOV2025",
}
NEW_PAPERS = {"geography_dec2021", "geography_nov2023", "geography_dec2024"}

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"FAIL: cannot parse {path.relative_to(ROOT)}: {exc}")

def fail(errors):
    if errors:
        print("FAIL: Geography Code 24 validation")
        for e in errors[:100]:
            print(" - " + e)
        raise SystemExit(1)

def main():
    bank, pending, keydoc, paperdoc, registrydoc = map(load, (BANK, PENDING, KEYS, PAPERS, REGISTRY))
    errors = []
    if not isinstance(bank, list) or not isinstance(pending, list):
        raise SystemExit("FAIL: question bank and review queue must be JSON arrays")
    keys = keydoc.get("sessions", {})
    papers = paperdoc.get("papers", [])
    by_paper = {}
    ids = set()
    pairs = set()
    review_ids = set()
    for q in bank:
        qid = str(q.get("id", ""))
        if not qid or qid in ids:
            errors.append(f"missing/duplicate ID: {qid or '(blank)'}")
        ids.add(qid)
        missing = REQUIRED - set(q)
        if missing:
            errors.append(f"{qid}: missing schema fields {sorted(missing)}")
        pid = q.get("paper_id")
        if q.get("paperId") != pid:
            errors.append(f"{qid}: paperId does not match paper_id")
        n = q.get("question_no")
        if not isinstance(n, int) or not 1 <= n <= 100:
            errors.append(f"{qid}: invalid question_no {n!r}")
        else:
            pair = (pid, n)
            if pair in pairs:
                errors.append(f"{qid}: duplicate paper/question number {pair}")
            pairs.add(pair)
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            errors.append(f"{qid}: empty/non-string question_en")
        opts = q.get("options_en")
        if not isinstance(opts, list) or len(opts) != 4 or any(not isinstance(v, str) or not v.strip() for v in opts):
            errors.append(f"{qid}: options_en must contain exactly four non-empty strings")
        if q.get("answer") not in {"A", "B", "C", "D", "Z"}:
            errors.append(f"{qid}: invalid answer {q.get('answer')!r}")
        if q.get("answer") != q.get("official_answer"):
            errors.append(f"{qid}: answer differs from official_answer")
        key_session = PAPER_KEYS.get(pid)
        if not key_session or key_session not in keys:
            errors.append(f"{qid}: no official final-key session configured for {pid}")
        else:
            official = keys[key_session].get("key", {}).get(str(n))
            if official is None or official != q.get("answer"):
                errors.append(f"{qid}: final-key mismatch bank={q.get('answer')} official={official}")
        if q.get("answer_key_verified") is not True:
            errors.append(f"{qid}: answer_key_verified is not true")
        if q.get("review_flag") is True:
            review_ids.add(qid)
            if not isinstance(q.get("review_note"), str) or not q["review_note"].strip():
                errors.append(f"{qid}: review_flag lacks review_note")
        if q.get("syllabus_mapping_status") == "pending" and q.get("review_flag") is not True:
            errors.append(f"{qid}: pending syllabus mapping must remain review-only")
        by_paper.setdefault(pid, []).append(q)

    pending_ids = [str(q.get("id", "")) for q in pending]
    if len(pending_ids) != len(set(pending_ids)):
        errors.append("review queue contains duplicate IDs")
    if set(pending_ids) != review_ids:
        errors.append(f"review queue IDs differ from canonical review_flag IDs (queue={len(set(pending_ids))}, canonical={len(review_ids)})")

    for pid in NEW_PAPERS:
        records = by_paper.get(pid, [])
        nums = sorted(q.get("question_no") for q in records)
        if len(records) != 100 or nums != list(range(1, 101)):
            errors.append(f"{pid}: expected exactly Q1-Q100; found {len(records)} records")
        for q in records:
            if q.get("source_verified") is not True or q.get("review_flag") is not True:
                errors.append(f"{q.get('id')}: new source-verified paper must stay review-only for syllabus mapping")
            if q.get("syllabus_mapping_status") != "pending":
                errors.append(f"{q.get('id')}: new mapping status must remain pending")

    manifest_by_id = {p.get("paper_id"): p for p in papers}
    for pid, records in by_paper.items():
        p = manifest_by_id.get(pid)
        if not p:
            errors.append(f"{pid}: missing papers.json manifest entry")
            continue
        if p.get("questions_loaded") != len(records) or p.get("questions_transcribed") != len(records):
            errors.append(f"{pid}: papers.json count does not match canonical bank ({len(records)})")
    for pid in NEW_PAPERS:
        p = manifest_by_id.get(pid, {})
        if p.get("question_source_verified") != 100 or p.get("answer_key_question_parity_verified") is not True:
            errors.append(f"{pid}: manifest source/key parity counters are incomplete")

    subject = next((s for s in registrydoc.get("subjects", []) if str(s.get("code")) == "24"), None)
    if not subject:
        errors.append("subjects.json has no Code 24 registry entry")
    else:
        if subject.get("questions_loaded") != len(bank):
            errors.append("subjects.json questions_loaded does not match canonical bank")
        if subject.get("questions_pending_review") != len(review_ids):
            errors.append("subjects.json questions_pending_review does not match review flags")
        if subject.get("source_verified") is not False:
            errors.append("subject-level source_verified must remain false while mapping/archive work is pending")

    fail(errors)
    print("PASS: Geography Code 24 canonical schema and required fields")
    print(f"PASS: {len(bank)} unique records; {len(ids)} unique IDs; no duplicate paper/question numbers")
    print("PASS: four non-empty English options and valid answer fields on every record")
    print("PASS: official final answer-key parity for every loaded question")
    print(f"PASS: {len(review_ids)} review-only records match questions_review_pending.json")
    print("PASS: 2021, 2023 and 2024 each contain 100 visually verified, key-matched records")
    print("PASS: papers.json and subjects.json counts match canonical records")
    print("NOTE: syllabus mapping is intentionally pending for the 300 new records; they remain excluded from active quiz use.")

if __name__ == "__main__":
    main()
