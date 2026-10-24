#!/usr/bin/env python3
"""Validate GSET Indian Knowledge System (subject 29) counts, official keys, tips and audit parity."""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "assets/subjects/indian_knowledge_system/questions.json"
AUDIT_PATH = ROOT / "assets/json/indian_knowledge_system.json"
PAPERS_PATH = ROOT / "assets/subjects/indian_knowledge_system/papers.json"
SUBJECTS_PATH = ROOT / "assets/subjects/subjects.json"

# Transcribed from the supplied official GSET Final Answer Key PDFs.
EXPECTED_KEYS = {
    "November 2023": "DCAABDDCACBBDDACCADBADACAABCADBCDCDABDADDBABACCDDCBDCDDBACCDADABBACDABADCAABCAABBACDACDACCBDBADAADAD",
    "December 2024": "BAAAACDADAADDDBCBBDABCBDCDDCBBCDCABBACDBCDCADBABCBCADACBDAABADCBCACDABCABABACDCDBACDACBACCADCCBCBDAD",
    "November 2025": "BBBBBDABBACDBACDABCBCABDACDACBBABABCCABDACAABDCADCBAAABBBADBBABAADCADCCBADDACACAABACBAACADBAACABABBA",
}
SESSION_META = {
    "November 2023": ("NOV23", "indian_knowledge_system_nov23"),
    "December 2024": ("DEC24", "indian_knowledge_system_dec24"),
    "November 2025": ("NOV25", "indian_knowledge_system_nov25"),
}

def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)

def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid JSON from {path.relative_to(ROOT)}: {exc}")

def index(records, label):
    result = {}
    for q in records:
        qid = q.get("id")
        if not qid:
            fail(f"{label} record has no id")
        if qid in result:
            fail(f"{label} bank has duplicate ID {qid}")
        result[qid] = q
    return result

def main() -> None:
    app = load(APP_PATH)
    audit_doc = load(AUDIT_PATH)
    papers_doc = load(PAPERS_PATH)
    subjects_doc = load(SUBJECTS_PATH)
    audit = audit_doc.get("questions")

    if not isinstance(app, list) or not isinstance(audit, list):
        fail("App bank must be a list and audit bank must contain a questions list")
    if len(app) != 300 or len(audit) != 300:
        fail(f"Expected 300 app/audit records, found {len(app)}/{len(audit)}")

    app_by_id = index(app, "App")
    audit_by_id = index(audit, "Audit")
    if set(app_by_id) != set(audit_by_id):
        fail("App/audit ID sets differ")

    counts = Counter()
    flags = Counter()
    for q in app:
        session = q.get("exam_session")
        number = q.get("question_no")
        if session not in SESSION_META:
            fail(f"Unknown session on {q.get('id')}: {session!r}")
        code, paper_id = SESSION_META[session]
        if not isinstance(number, int) or not 1 <= number <= 100:
            fail(f"Invalid question number on {q.get('id')}")
        if q.get("id") != f"GSET_29_{code}_{number:03d}":
            fail(f"Unexpected ID on {q.get('id')}")
        if q.get("paper_id") != paper_id or q.get("paperId") != paper_id:
            fail(f"Wrong paper ID on {q.get('id')}")
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(f"Missing question text on {q.get('id')}")
        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4 or not all(isinstance(v, str) and v.strip() for v in options):
            fail(f"Need exactly four non-empty English options on {q.get('id')}")
        options_gu = q.get("options_gu")
        if not isinstance(options_gu, list) or len(options_gu) != 4 or not all(isinstance(v, str) and v.strip() for v in options_gu):
            fail(f"Need exactly four non-empty Gujarati/display options on {q.get('id')}")
        official = EXPECTED_KEYS[session][number - 1]
        if q.get("answer") != official or q.get("official_answer") != official:
            fail(f"Official key mismatch on {q.get('id')}: expected {official}")
        for field in ("tip_en", "tip_gu"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                fail(f"Missing {field} on {q.get('id')}")
            if len(q[field].strip()) < 80:
                fail(f"Tip is too short to be useful ({field}) on {q.get('id')}")

        if q.get("review_flag") is True:
            flags[session] += 1
            if q.get("source_verified") is not False:
                fail(f"Flagged item incorrectly has source_verified=true: {q.get('id')}")
            if not isinstance(q.get("review_note"), str) or not q["review_note"].strip():
                fail(f"Flagged item has no review note: {q.get('id')}")
        elif q.get("source_verified") is not True:
            fail(f"Unflagged item must be source verified: {q.get('id')}")

        aq = audit_by_id[q["id"]]
        if aq.get("exam_session") != session or aq.get("question_number") != number:
            fail(f"Audit session/number mismatch for {q['id']}")
        if aq.get("question_text") != q.get("question_en"):
            fail(f"Audit question text mismatch for {q['id']}")
        if aq.get("options") != dict(zip("ABCD", options)):
            fail(f"Audit options mismatch for {q['id']}")
        if aq.get("correct_answer") != official:
            fail(f"Audit official answer mismatch for {q['id']}")
        if aq.get("review_flag") != q.get("review_flag") or aq.get("source_verified") != q.get("source_verified"):
            fail(f"Audit review state mismatch for {q['id']}")
        if aq.get("tip_en") != q.get("tip_en") or aq.get("tip_gu") != q.get("tip_gu"):
            fail(f"Audit exam tip mismatch for {q['id']}")
        if aq.get("review_note") != (q.get("review_note") or None):
            fail(f"Audit review note mismatch for {q['id']}")
        counts[session] += 1

    for session, key in EXPECTED_KEYS.items():
        if len(key) != 100:
            fail(f"Embedded official key string for {session} must contain exactly 100 answers")
    for session in SESSION_META:
        numbers = sorted(q["question_no"] for q in app if q.get("exam_session") == session)
        if counts[session] != 100 or numbers != list(range(1, 101)):
            fail(f"{session} must contain Q1-Q100 exactly once")

    papers = papers_doc.get("papers", [])
    if len(papers) != 3 or {p.get("exam") for p in papers} != set(SESSION_META):
        fail("papers.json must contain exactly one record for each of the three sessions")
    for p in papers:
        session = p.get("exam")
        if session not in SESSION_META or p.get("questions_loaded") != 100 or p.get("questions_count") != 100:
            fail(f"Paper metadata/count mismatch: {session}")
        if flags[session] == 0:
            if p.get("source_verified") is not True:
                fail(f"Fully reviewed paper should be verified: {session}")
        elif p.get("source_verified") is not False or "review" not in str(p.get("status", "")).lower():
            fail(f"Paper review metadata mismatch: {session}")

    subject = next((x for x in subjects_doc.get("subjects", []) if x.get("code") == "29"), None)
    if not subject:
        fail("Subject 29 missing from subjects.json")
    if subject.get("id") != "indian_knowledge_system" or subject.get("questions_loaded") != 300 or subject.get("papers_loaded") != 3:
        fail("Subject 29 metadata/count mismatch")
    if sum(flags.values()) == 0 and subject.get("source_verified") is not True:
        fail("A fully source-verified subject should be marked verified")
    if sum(flags.values()) > 0 and subject.get("source_verified") is not False:
        fail("Subject with remaining review flags must remain unverified")

    remaining = audit_doc.get("review_flags_remaining")
    expected_remaining = [
        {"id": q["id"], "review_note": q["review_note"]}
        for q in app if q.get("review_flag") is True
    ]
    if not isinstance(remaining, list) or remaining != expected_remaining:
        fail("Audit review_flags_remaining list is stale or differs from app review metadata")

    print("PASS: Indian Knowledge System subject 29 — 300 app/audit questions")
    print("PASS: every session has Q1-Q100 exactly once; no duplicate IDs")
    print("PASS: 300/300 answers match official Final Answer Keys")
    print("PASS: app/audit wording, options, answers, tips and review states match")
    if len({q["tip_en"] for q in app}) < 250 or len({q["tip_gu"] for q in app}) < 250:
        fail("Tip strings are too repetitive; add question-specific revision guidance")
    print("PASS: English and Gujarati exam tips exist on all 300 questions")
    print(f"PASS: distinct tips — English {len({q['tip_en'] for q in app})}, Gujarati {len({q['tip_gu'] for q in app})}")
    print(f"Source review flags remaining: {sum(flags.values())}")
    for session in SESSION_META:
        print(f"  {session}: {counts[session]} questions; {counts[session] - flags[session]} source verified; {flags[session]} flagged")

if __name__ == "__main__":
    main()
