#!/usr/bin/env python3
"""Validate GSET Performing Arts (subject code 31) against official final keys.

Official key sources:
- https://www.gujaratset.ac.in/assets/anskey/paperII/nov23/nov2331.pdf
- https://www.gujaratset.ac.in/assets/anskey/paperII/dec24/dec2431.pdf
- https://www.gujaratset.ac.in/assets/anskey/paperII/nov25/nov2531.pdf

The expected key sequences below were transcribed from the official Final Answer Key
PDFs. Source-question visual review is tracked separately by review_flag.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "assets/subjects/performing_art_dance_drama_theatre/questions.json"
AUDIT_PATH = ROOT / "assets/json/performing_arts.json"
PAPERS_PATH = ROOT / "assets/subjects/performing_art_dance_drama_theatre/papers.json"
SUBJECTS_PATH = ROOT / "assets/subjects/subjects.json"

EXPECTED_KEYS = {
  "November 2023": "BBACABBBDBCBBBABBCBBACBDBCDACDCBDDCDDBACCAABBCCDBADADBDDCBCACBCCBCDCACDADCCBBDCCBBCBBDBCABAAACDBDBBC",
  "December 2024": "BCCBAACCBCDDCBDBABBBBABCDBCDACBCDCCDBACCBCCABCAAACDBDBDDDCDCABDBADDAAADDCACBBBBBBDBCDCDDBCBCBACCCCAB",
  "November 2025": "CCBDBCCDBCCCCCCBADCCDBBDDBBBABACABBDACDBACDCABBBBBBCBDDDBCCCACDDACBCCDCACABCADDBDCBCAAAABAABCBADCDDA"
}
SESSION_META = {
    "November 2023": ("NOV23", "performing_arts_nov23"),
    "December 2024": ("DEC24", "performing_arts_dec24"),
    "November 2025": ("NOV25", "performing_arts_nov25"),
}
Q57_TEXT = "‘Sangeet Natak Akademi’ has organized which ‘music, dance and drama’ festivals for the young artists in ‘Amrit Kaal’ all over India?"
Q57_OPTIONS = ["Kala Utsav", "Kala Ghoda Utsav", "Kala Sadhana Utsava", "Kalotsava"]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid JSON from {path.relative_to(ROOT)}: {exc}")


def main() -> None:
    app = load_json(APP_PATH)
    audit_doc = load_json(AUDIT_PATH)
    papers_doc = load_json(PAPERS_PATH)
    subjects_doc = load_json(SUBJECTS_PATH)
    audit = audit_doc.get("questions")
    if not isinstance(app, list) or not isinstance(audit, list):
        fail("App bank must be a JSON list and audit bank must contain a questions list")

    for label, data in (("app", app), ("audit", audit)):
        if len(data) != 300:
            fail(f"{label} bank has {len(data)} records; expected 300")

    app_by_id = {}
    audit_by_id = {}
    for label, records, output in (("app", app, app_by_id), ("audit", audit, audit_by_id)):
        for q in records:
            qid = q.get("id")
            if not qid:
                fail(f"{label} record has no id")
            if qid in output:
                fail(f"{label} bank contains duplicate id {qid}")
            output[qid] = q
    if set(app_by_id) != set(audit_by_id):
        fail("App and audit banks do not contain exactly the same IDs")

    app_by_session = Counter()
    verified_by_session = Counter()
    flagged_by_session = Counter()
    for q in app:
        session = q.get("exam_session")
        if session not in SESSION_META:
            fail(f"Unknown session on {q.get('id')}: {session!r}")
        code, paper_id = SESSION_META[session]
        n = q.get("question_no")
        if not isinstance(n, int) or n < 1 or n > 100:
            fail(f"Invalid question number on {q.get('id')}: {n!r}")
        expected_id = f"GSET_31_{code}_{n:03d}"
        if q.get("id") != expected_id:
            fail(f"Unexpected ID for {session} Q{n}: {q.get('id')}; expected {expected_id}")
        if q.get("paper_id") != paper_id or q.get("paperId") != paper_id:
            fail(f"Wrong paper id for {q.get('id')}")
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(f"Missing English question text on {q.get('id')}")
        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4 or not all(isinstance(v, str) and v.strip() for v in options):
            fail(f"Expected four readable English options on {q.get('id')}")
        official = EXPECTED_KEYS[session][n - 1]
        if q.get("answer") != official or q.get("official_answer") != official:
            fail(f"Official key mismatch {q.get('id')}: app={q.get('answer')!r}, key={official!r}")
        if q.get("review_flag"):
            flagged_by_session[session] += 1
            if q.get("source_verified") is not False:
                fail(f"Review-flagged question incorrectly has source_verified=true: {q.get('id')}")
            if not isinstance(q.get("review_note"), str) or not q["review_note"].strip():
                fail(f"Review-flagged question has no review_note: {q.get('id')}")
        else:
            if q.get("source_verified") is not True:
                fail(f"Unflagged question must remain source_verified=true or receive review_flag: {q.get('id')}")
            verified_by_session[session] += 1
        app_by_session[session] += 1

        aq = audit_by_id[q["id"]]
        if aq.get("exam_session") != session or aq.get("question_number") != n:
            fail(f"Audit session/question mismatch for {q['id']}")
        if aq.get("question_text") != q.get("question_en"):
            fail(f"Audit question text mismatch for {q['id']}")
        if aq.get("correct_answer") != official:
            fail(f"Audit official key mismatch for {q['id']}")
        expected_options = dict(zip("ABCD", options))
        if aq.get("options") != expected_options:
            fail(f"Audit options mismatch for {q['id']}")
        if aq.get("review_flag") != q.get("review_flag") or aq.get("source_verified") != q.get("source_verified"):
            fail(f"Audit verification flags mismatch for {q['id']}")

    for session in SESSION_META:
        records = [q for q in app if q.get("exam_session") == session]
        nums = [q.get("question_no") for q in records]
        if app_by_session[session] != 100 or sorted(nums) != list(range(1, 101)):
            fail(f"{session} must contain each question 1-100 exactly once")

    q57_id = "GSET_31_DEC24_057"
    q57 = [q for q in app if q.get("id") == q57_id]
    aq57 = [q for q in audit if q.get("id") == q57_id]
    if len(q57) != 1 or len(aq57) != 1:
        fail("December 2024 Q57 must appear exactly once in both banks")
    if q57[0].get("question_en") != Q57_TEXT or q57[0].get("options_en") != Q57_OPTIONS or q57[0].get("answer") != "D":
        fail("December 2024 Q57 content/options/answer differs from the approved transcription")
    if aq57[0].get("question_text") != Q57_TEXT or aq57[0].get("correct_answer") != "D":
        fail("Audit copy of December 2024 Q57 differs from the approved transcription")

    papers = papers_doc.get("papers", [])
    if len(papers) != 3:
        fail("papers.json must declare exactly three sessions")
    for p in papers:
        if p.get("exam") not in SESSION_META:
            fail(f"Unexpected paper entry in papers.json: {p.get('exam')!r}")
        if p.get("questions_loaded") != 100 or p.get("questions_count") != 100:
            fail(f"Stale count in papers.json for {p.get('exam')}")
        if p.get("source_verified") is not True or p.get("question_source_verified") is not True:
            fail(f"Paper-level source verification is incomplete for {p.get('exam')}")
        if "verified" not in str(p.get("status", "")).lower():
            fail(f"Paper status must reflect completed source review: {p.get('exam')}")
        if any(q.get("exam_session") == p.get("exam") and q.get("review_flag") for q in app):
            fail(f"Unresolved review flags remain for {p.get('exam')}")

    subject = next((s for s in subjects_doc.get("subjects", []) if s.get("code") == "31"), None)
    if not subject:
        fail("Subject code 31 missing from subjects.json")
    if subject.get("id") != "performing_art_dance_drama_theatre" or subject.get("questions_loaded") != 300 or subject.get("papers_loaded") != 3:
        fail("Subject entry id/counts are inconsistent")
    if subject.get("source_verified") is not True:
        fail("Subject-level source verification must be complete when no review flags remain")
    if subject.get("data_status") != "official_archive_verified_300_questions":
        fail("Subject-level data_status does not reflect the verified 300-question bank")

    total_flags = sum(flagged_by_session.values())
    print("PASS: Performing Arts subject 31")
    print("PASS: 300 unique records; every session has Q1-Q100 exactly once")
    print("PASS: 300/300 answers match official Final Answer Key sequences")
    print("PASS: App and audit banks have matching IDs, wording, options, answers and flags")
    print("PASS: December 2024 Q57 is present once in both banks with answer D")
    for session in SESSION_META:
        print(f"  {session}: 100 questions, {verified_by_session[session]} not flagged, {flagged_by_session[session]} flagged for source visual review")
    print(f"Review flags total: {total_flags}")


if __name__ == "__main__":
    main()
