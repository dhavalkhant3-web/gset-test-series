#!/usr/bin/env python3
"""Validate GSET Visual Art (33) Paper-II question records against official FINAL keys.

This checks structural integrity, session coverage, key parity, and figure-asset
references. It intentionally does not mark question wording as source-verified;
that requires a separate visual proofread against the official question PDFs.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "assets/subjects/visual_art/questions.json"
PAPERS_PATH = ROOT / "assets/subjects/visual_art/papers.json"
REGISTRY_PATH = ROOT / "assets/subjects/subjects.json"

# Transcribed from the official GSET FINAL answer-key PDFs for Paper-II Visual Art (33).
# Each string is in question-number order, Q1 through Q100.
OFFICIAL_FINAL_KEYS = {
    "November 2023": "CADBDBDBCBCACBCBCACBDCABCBBDABBCACACAADACDBADCBAABBCDCCABBDCACCAAADDAADDBADDBDBBDDBABBCCDCBDDBCBBBCB",
    "December 2024": "BACBBAACBACBCABDCADADABCBCABCDBCACDCCCBBBAAADBBBCABCDDBDBACBDCCBBCCDDACBCCAAACBAABBABCBADABAABCDCDDB",
    "November 2025": "BAABAABBAABCCABCCBBBBBDBBACAABCACBABBAABBAAABCABBBBBBCBCACBABBBABCCAAAACADCDDACACDBCABDABDBBAACCAABA",
}
EXPECTED_SESSIONS = {"November 2023", "December 2024", "November 2025"}
VALID_ANSWERS = set("ABCD")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"could not read {path.relative_to(ROOT)}: {exc}")


def main() -> None:
    bank = read_json(BANK_PATH)
    papers_doc = read_json(PAPERS_PATH)
    registry = read_json(REGISTRY_PATH)

    if not isinstance(bank, list) or len(bank) != 300:
        fail(f"expected 300 questions, found {len(bank) if isinstance(bank, list) else type(bank).__name__}")
    if papers_doc.get("subject_code") != "33" or papers_doc.get("subject_id") != "visual_art":
        fail("papers.json does not identify Visual Art subject code 33")
    paper_by_id = {p.get("paper_id"): p for p in papers_doc.get("papers", [])}
    if len(paper_by_id) != 3:
        fail(f"expected 3 paper metadata entries, found {len(paper_by_id)}")
    if set(p.get("exam") for p in papers_doc["papers"]) != EXPECTED_SESSIONS:
        fail("paper metadata sessions do not match the three required sessions")

    session_counts = Counter(q.get("exam_session") for q in bank)
    if session_counts != Counter({s: 100 for s in EXPECTED_SESSIONS}):
        fail(f"session count mismatch: {dict(session_counts)}")

    subject = next((s for s in registry.get("subjects", []) if s.get("id") == "visual_art"), None)
    if subject is None:
        fail("Visual Art is missing from assets/subjects/subjects.json")
    if subject.get("code") != "33" or subject.get("questions_loaded") != 300 or subject.get("papers_loaded") != 3:
        fail("subject registry code/counts do not match the bank and metadata")
    if subject.get("source_verified") is not False:
        fail("subject source_verified must stay false while wording/option proofread is pending")

    seen_ids, seen_pairs = set(), set()
    mismatches, flags, figure_count = [], 0, 0
    for q in bank:
        qid = q.get("id")
        if not qid or qid in seen_ids:
            fail(f"missing or duplicate id: {qid!r}")
        seen_ids.add(qid)
        session = q.get("exam_session")
        number = q.get("question_no")
        if session not in EXPECTED_SESSIONS or not isinstance(number, int) or not 1 <= number <= 100:
            fail(f"{qid}: invalid session/question number")
        pair = (session, number)
        if pair in seen_pairs:
            fail(f"duplicate question number: {session} Q{number}")
        seen_pairs.add(pair)
        if q.get("paper_id") != {"November 2023": "visual_art_nov23", "December 2024": "visual_art_dec24", "November 2025": "visual_art_nov25"}[session]:
            fail(f"{qid}: paper_id mismatch")
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(f"{qid}: missing English question stem")
        for field in ("explanation_en", "explanation_gu", "tip_en", "tip_gu"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                fail(f"{qid}: missing bilingual explanation/exam-tip field {field}")
        if q.get("source_verified") is True:
            if not (q.get("has_figure") and 91 <= number <= 100 and q.get("verification_status") == "visually_checked_against_official_scan"):
                fail(f"{qid}: source_verified=true is reserved for the visually checked figure block in this partial audit")
        if q.get("has_figure") and 91 <= number <= 100:
            if q.get("source_verified") is not True or q.get("review_flag") is True:
                fail(f"{qid}: figure question must retain its visual source verification status")
            if not q.get("source_page"):
                fail(f"{qid}: visually checked figure question is missing its printed source page")
        for field in ("options_en", "options_gu"):
            options = q.get(field)
            if not isinstance(options, list) or len(options) != 4 or any(not isinstance(v, str) for v in options):
                fail(f"{qid}: {field} must contain four strings")
        answer = q.get("official_answer", q.get("answer"))
        if answer not in VALID_ANSWERS:
            fail(f"{qid}: invalid official answer {answer!r}")
        if q.get("answer") != answer:
            fail(f"{qid}: app answer and official_answer differ")
        expected = OFFICIAL_FINAL_KEYS[session][number - 1]
        if answer != expected:
            mismatches.append(f"{session} Q{number}: stored={answer}, official={expected}")
        paper = paper_by_id.get(q.get("paper_id"))
        if not paper:
            fail(f"{qid}: missing paper metadata")
        if paper.get("answer_key_verified") is not True:
            fail(f"{q['paper_id']}: official final-key verification must be recorded")
        if paper.get("question_source_verified") is not False or paper.get("source_verified") is not False:
            fail(f"{q['paper_id']}: do not mark unproofread question wording as source-verified")
        if not str(paper.get("question_paper_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{q['paper_id']}: non-official question-paper URL")
        if not str(paper.get("answer_key_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{q['paper_id']}: non-official final-key URL")
        if q.get("review_flag"):
            flags += 1
            if not q.get("review_note"):
                fail(f"{qid}: review_flag requires a review_note")
        if q.get("has_figure"):
            figure_count += 1
            asset = q.get("image_asset")
            if not asset:
                fail(f"{qid}: figure question has no image_asset")
            if not (ROOT / asset).is_file():
                fail(f"{qid}: missing referenced figure asset {asset}")

    expected_review_counts = {"November 2023": 7, "December 2024": 5, "November 2025": 2}
    observed_review_counts = {
        session: sum(1 for q in bank if q.get("exam_session") == session and q.get("review_flag"))
        for session in EXPECTED_SESSIONS
    }
    if observed_review_counts != expected_review_counts:
        fail(f"review-flag counts do not match the recorded source audit: {observed_review_counts}")
    for paper in papers_doc["papers"]:
        if paper.get("review_count") != expected_review_counts.get(paper.get("exam")):
            fail(f"{paper.get('paper_id')}: review_count does not match question-level flags")

    if mismatches:
        fail("official final-key mismatches: " + "; ".join(mismatches[:20]))
    if len(seen_pairs) != 300:
        fail(f"expected 300 unique session/question pairs, found {len(seen_pairs)}")

    for paper in papers_doc["papers"]:
        if paper.get("answer_key_verified") is not True:
            fail(f"{paper.get('paper_id')}: answer_key_verified must be true")
        if paper.get("source_verified") is not False or paper.get("question_source_verified") is not False:
            fail(f"{paper.get('paper_id')}: question source verification must remain pending")
        if not str(paper.get("question_paper_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{paper.get('paper_id')}: invalid question-paper source URL")
        if not str(paper.get("answer_key_url", "")).startswith("https://www.gujaratset.ac.in/"):
            fail(f"{paper.get('paper_id')}: invalid final-answer-key source URL")

    print(
        f"PASS: {len(bank)} questions; 3 sessions × 100 questions; "
        "300/300 official FINAL-key comparisons; "
        f"{flags} review-flagged records; {figure_count} figure questions validated."
    )
    print(
        "NOTE: official answer keys are verified; question wording/options remain unverified "
        "until all flagged and pending records are proofread against the official paper scans."
    )


if __name__ == "__main__":
    main()
