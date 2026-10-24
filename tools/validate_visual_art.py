#!/usr/bin/env python3
"""Validate GSET Visual Art Paper-II counts, final keys, figure mappings and review state."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "assets/subjects/visual_art/questions.json"
PAPERS_PATH = ROOT / "assets/subjects/visual_art/papers.json"
SUBJECTS_PATH = ROOT / "assets/subjects/subjects.json"
EXPECTED_SESSIONS = {
    "November 2023": "visual_art_nov23",
    "December 2024": "visual_art_dec24",
    "November 2025": "visual_art_nov25",
}
EXPECTED_KEYS = {
    "November 2023": "CADBDBDBCBCACBCBCACBDCABCBBDABBCACACAADACDBADCBAABBCDCCABBDCACCAAADDAADDBADDBDBBDDBABBCCDCBDDBCBBBCB",
    "December 2024": "BACBBAACBACBCABDCADADABCBCABCDBCACDCCCBBBAAADBBBCABCDDBDBACBDCCBBCCDDACBCCAAACBAABBABCBADABAABCDCDDB",
    "November 2025": "BAABAABBAABCCABCCBBBBBDBBACAABCACBABBAABBAAABCABBBBBBCBCACBABBBABCCAAAACADCDDACACDBCABDABDBBAACCAABA"
}
EXPECTED_REVIEW_FLAGS = [
    "visual_art_nov23_q17",
    "visual_art_nov23_q62",
    "visual_art_nov23_q63",
    "visual_art_nov23_q68",
    "visual_art_nov23_q70",
    "visual_art_nov23_q71",
    "visual_art_nov23_q72",
    "visual_art_dec24_q30",
    "visual_art_dec24_q32",
    "visual_art_dec24_q36",
    "visual_art_dec24_q46",
    "visual_art_dec24_q64",
    "visual_art_nov25_q8",
    "visual_art_nov25_q37"
]
EXPECTED_FIGURES = {
    "November 2023": {
        "first": "assets/subjects/visual_art/figures/visual_art_nov23_q91_95.jpg",
        "second": "assets/subjects/visual_art/figures/visual_art_nov23_q96_100.jpg",
    },
    "December 2024": {
        "first": "assets/subjects/visual_art/figures/visual_art_dec24_q91_95.jpg",
        "second": "assets/subjects/visual_art/figures/visual_art_dec24_q96_100.jpg",
    },
    "November 2025": {
        "first": "assets/subjects/visual_art/figures/visual_art_nov25_q91_95.jpg",
        "second": "assets/subjects/visual_art/figures/visual_art_nov25_q96_100.jpg",
    },
}

def fail(message):
    print("FAIL: " + message, file=sys.stderr)
    raise SystemExit(1)

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail("cannot parse " + str(path.relative_to(ROOT)) + ": " + str(exc))

def main():
    bank = load(BANK_PATH)
    data = load(PAPERS_PATH)
    registry = load(SUBJECTS_PATH)
    if not isinstance(bank, list) or len(bank) != 300:
        fail("expected exactly 300 question records")
    papers_list = data.get("papers")
    if not isinstance(papers_list, list) or len(papers_list) != 3:
        fail("papers.json must contain exactly three session records")
    papers = {p.get("paper_id"): p for p in papers_list}
    if set(papers) != set(EXPECTED_SESSIONS.values()):
        fail("paper IDs do not match the three expected sessions")
    for session, key in EXPECTED_KEYS.items():
        if len(key) != 100 or set(key) - set("ABCDZ"):
            fail("invalid embedded official final key for " + session)
    counts = Counter(q.get("exam_session") for q in bank)
    if counts != Counter({session: 100 for session in EXPECTED_SESSIONS}):
        fail("expected exactly 100 questions per session; got " + str(dict(counts)))
    seen_ids, seen_numbers, flags = set(), set(), []
    verified_figure_count = 0
    for q in bank:
        qid = q.get("id")
        session = q.get("exam_session")
        number = q.get("question_no")
        if not qid or qid in seen_ids:
            fail("missing/duplicate ID: " + str(qid))
        seen_ids.add(qid)
        if session not in EXPECTED_SESSIONS or not isinstance(number, int) or not 1 <= number <= 100:
            fail(str(qid) + ": invalid session or question number")
        if (session, number) in seen_numbers:
            fail("duplicate question number " + session + " Q" + str(number))
        seen_numbers.add((session, number))
        paper_id = EXPECTED_SESSIONS[session]
        if q.get("paper_id") != paper_id or q.get("paperId") != paper_id:
            fail(str(qid) + ": paper ID mismatch")
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(str(qid) + ": missing English question text")
        for field in ("options_en", "options_gu"):
            options = q.get(field)
            if not isinstance(options, list) or len(options) != 4 or any(not isinstance(v, str) or not v.strip() for v in options):
                fail(str(qid) + ": " + field + " must contain four non-empty strings")
        answer = q.get("official_answer", q.get("answer", ""))
        expected = EXPECTED_KEYS[session][number - 1]
        if answer != expected or q.get("answer") != expected:
            fail(str(qid) + ": answer letter does not match official final key " + expected)
        for field in ("explanation_en", "explanation_gu", "tip_en", "tip_gu"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                fail(str(qid) + ": missing bilingual explanation/tip field " + field)
        if q.get("review_flag"):
            flags.append(qid)
            if not q.get("review_note"):
                fail(str(qid) + ": review_flag has no review_note")
        if number >= 91:
            group = "first" if number <= 95 else "second"
            expected_asset = EXPECTED_FIGURES[session][group]
            if q.get("review_flag") is not False or q.get("source_verified") is not True:
                fail(str(qid) + ": grouped figure item is not marked source-checked")
            if q.get("image_asset") != expected_asset or not (ROOT / expected_asset).is_file():
                fail(str(qid) + ": image_asset does not resolve to the expected original crop")
            if not q.get("has_figure") or not q.get("passage_en") or not q.get("passage_gu"):
                fail(str(qid) + ": missing figure/passage metadata")
            verified_figure_count += 1
        if q.get("review_flag") and q.get("source_verified") is True:
            fail(str(qid) + ": unresolved item cannot be marked source_verified")
    if sorted(flags) != sorted(EXPECTED_REVIEW_FLAGS):
        fail("unresolved review flags differ from expected list: " + str(sorted(flags)))
    if verified_figure_count != 30:
        fail("expected 30 visually reviewed image questions, got " + str(verified_figure_count))
    subject = next((s for s in registry.get("subjects", []) if s.get("id") == "visual_art"), None)
    if not subject:
        fail("Visual Art is missing from subject registry")
    if subject.get("source_verified") is not False:
        fail("subject source_verified must remain false while source review is incomplete")
    if subject.get("questions_loaded") != 300 or subject.get("papers_loaded") != 3:
        fail("subject registry counts do not match questions/papers")
    for session, paper_id in EXPECTED_SESSIONS.items():
        p = papers[paper_id]
        if p.get("exam") != session or p.get("question_count") != 100:
            fail(paper_id + ": session/question count mismatch")
        if p.get("answer_key_verified") is not True:
            fail(paper_id + ": official final answer key not recorded as verified")
        if p.get("source_verified") is not False or p.get("question_source_verified") is not False:
            fail(paper_id + ": do not claim full question-source verification before audit completion")
        if sorted(p.get("review_flags_remaining", [])) != sorted([qid for qid in EXPECTED_REVIEW_FLAGS if qid.startswith(paper_id)]):
            fail(paper_id + ": paper review flag metadata is inconsistent")
        for field in ("question_paper_url", "answer_key_url"):
            if not str(p.get(field, "")).startswith("https://www.gujaratset.ac.in/"):
                fail(paper_id + ": " + field + " must use official GSET URL")
    print("PASS: 300 questions; 300 official final-key matches; 300 bilingual explanation/tip pairs.")
    print("PASS: all 30 grouped figure questions have source image mappings; 14 content concerns remain flagged.")
    print("NOTE: subject-level question source verification remains false while source review is incomplete.")

if __name__ == "__main__":
    main()
