#!/usr/bin/env python3
"""Validate the structure and provenance fields of the Public Administration bank.

This validates data integrity only. It does NOT independently verify the question
wording or official answers against GSET source PDFs.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "assets/subjects/public_administration/questions.json"
PAPERS = ROOT / "assets/subjects/public_administration/papers.json"
REGISTRY = ROOT / "assets/subjects/subjects.json"
EXPECTED_SESSIONS = {
    "November 2023": ("public_administration_nov23", 100),
    "December 2024": ("public_administration_dec24", 100),
    "November 2025": ("public_administration_nov25", 100),
}
VALID_ANSWERS = {"A", "B", "C", "D"}
EXPECTED_OFFICIAL_KEYS = {
    "November 2023": "BCDACADDACBCCBDCACDBCDADAACDADABDABCAADBDDCBCDDCDBBCCADCDBCCBCBCDBAADBACDBCDCCAABDCDABBCCBCCDBDCADBA",
    "December 2024": "CDCBCCDBADCDBAAACBDBBDBDAADCACDAABCCCACDBACCBAACCDDBDBADBDCADBBCDAABCBCDBCCACABABAACBCABBACBDABAABAD",
    "November 2025": "DDBDABCCAADCAABBDAACCABDCBADBBBDCDACBDDAACBBCBCCBDCDCBACCBDACAAAAABADCDDBADAACAABACDDDBACCDCADCCDBDA"
}

def fail(message):
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")

def main():
    bank = load(BANK)
    papers = load(PAPERS)
    registry = load(REGISTRY)
    if not isinstance(bank, list) or len(bank) != 300:
        fail(f"expected 300 questions, found {len(bank) if isinstance(bank, list) else type(bank).__name__}")
    if not isinstance(papers.get("papers"), list):
        fail("papers.json must contain a papers list")
    paper_by_id = {p.get("paper_id"): p for p in papers["papers"]}
    if len(paper_by_id) != 3:
        fail(f"expected 3 unique session papers, found {len(paper_by_id)}")
    counts = Counter(q.get("exam_session") for q in bank)
    if counts != Counter({s: n for s, (_, n) in EXPECTED_SESSIONS.items()}):
        fail(f"session distribution mismatch: {dict(counts)}")
    seen_ids, seen_questions = set(), set()
    flags = 0
    for q in bank:
        qid = q.get("id")
        if not qid or qid in seen_ids:
            fail(f"missing/duplicate question id: {qid!r}")
        seen_ids.add(qid)
        session = q.get("exam_session")
        if session not in EXPECTED_SESSIONS:
            fail(f"{qid}: unexpected session {session!r}")
        expected_paper_id, _ = EXPECTED_SESSIONS[session]
        if q.get("paper_id") != expected_paper_id or q.get("paperId") != expected_paper_id:
            fail(f"{qid}: paper id mismatch")
        if expected_paper_id not in paper_by_id:
            fail(f"{qid}: no matching paper metadata")
        number = q.get("question_no")
        if not isinstance(number, int) or not 1 <= number <= 100:
            fail(f"{qid}: invalid question number {number!r}")
        key = (session, number)
        if key in seen_questions:
            fail(f"duplicate question number: {session} Q{number}")
        seen_questions.add(key)
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(f"{qid}: missing question text")
        for field in ("options_en", "options_gu"):
            options = q.get(field)
            if not isinstance(options, list) or len(options) != 4 or any(not isinstance(x, str) for x in options):
                fail(f"{qid}: {field} must contain exactly four strings")
        answer = q.get("official_answer", q.get("answer", ""))
        if answer not in VALID_ANSWERS and not q.get("review_flag"):
            fail(f"{qid}: non-standard official answer must be review flagged")
        expected_key = EXPECTED_OFFICIAL_KEYS[session]
        expected_answer = expected_key[number - 1]
        if answer != expected_answer:
            fail(f"{qid}: stored official answer {answer!r} differs from official final key {expected_answer!r}")
        if q.get("answer") != answer and answer in VALID_ANSWERS:
            fail(f"{qid}: app answer differs from official_answer field")
        if q.get("review_flag"):
            flags += 1
            if not q.get("review_note"):
                fail(f"{qid}: review flag has no review note")
        if not q.get("answer_source"):
            fail(f"{qid}: missing answer source")
    subject = next((s for s in registry.get("subjects", []) if s.get("id") == "public_administration"), None)
    if not subject:
        fail("Public Administration missing from subjects registry")
    if subject.get("questions_loaded") != len(bank) or subject.get("papers_loaded") != len(papers["papers"]):
        fail("subject registry counts do not match the question/paper files")
    if subject.get("source_verified") is not False:
        fail("source_verified must remain false until official source audit is complete")
    for p in papers["papers"]:
        if p.get("answer_key_verified") is not True:
            fail(f"{p.get('paper_id')}: official final answer key comparison must be recorded as verified")
        if p.get("source_verified") is not False or p.get("question_source_verified") is not False:
            fail(f"{p.get('paper_id')}: question wording/options must remain unverified until source audit is complete")
        if not str(p.get("question_paper_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{p.get('paper_id')}: question paper URL is not official GSET domain")
        if not str(p.get("answer_key_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{p.get('paper_id')}: answer key URL is not official GSET domain")
    print(f"PASS: {len(bank)} questions; {len(papers['papers'])} sessions; {flags} review-flagged records; 300 official final-key comparisons.")
    print("NOTE: official answer keys reconciled. Question wording/options verification remains separate; unresolved records stay flagged.")

if __name__ == "__main__":
    main()
