#!/usr/bin/env python3
"""Convert the supplied GSET Public Administration staging bank to the app schema.

Usage:
  python tools/import_public_administration.py path/to/gset_paper2_public_administration_staging.json
Writes assets/subjects/public_administration/questions.json.

The source staging file must be supplied separately. This script never guesses
questions, options, or answers; it preserves source wording and marks uncertain
records for review.
"""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/subjects/public_administration/questions.json"
SESSIONS = {"November 2025": "public_administration_nov25",
            "December 2024": "public_administration_dec24",
            "November 2023": "public_administration_nov23"}
LETTERS = ("A", "B", "C", "D")

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/import_public_administration.py <staging.json>", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    raw = json.loads(source.read_text(encoding="utf-8"))
    questions = raw.get("questions")
    if not isinstance(questions, list):
        raise SystemExit("Invalid staging file: 'questions' must be a list.")
    if len(questions) != 300:
        raise SystemExit(f"Refusing import: expected 300 records, found {len(questions)}.")
    counts = Counter(q.get("session") for q in questions)
    if counts != Counter({s: 100 for s in SESSIONS}):
        raise SystemExit(f"Refusing import: expected 100 questions per session, found {dict(counts)}.")
    out = []
    seen = set()
    for q in questions:
        session = q.get("session")
        number = q.get("question_number")
        if session not in SESSIONS or not isinstance(number, int):
            raise SystemExit(f"Invalid session/question number in record {q.get('id')!r}.")
        key = (session, number)
        if key in seen:
            raise SystemExit(f"Duplicate question: {session} Q{number}.")
        seen.add(key)
        opts = q.get("options") or {}
        answer = q.get("official_answer")
        if set(opts) != set(LETTERS):
            raise SystemExit(f"Q{number} ({session}) does not have exactly A-D options.")
        flagged = bool(q.get("review_flag")) or q.get("verification_status") != "verified"
        out.append({
            "id": f"{SESSIONS[session]}_q{number}",
            "paper_id": SESSIONS[session],
            "paperId": SESSIONS[session],
            "question_no": number,
            "question_en": q.get("question", ""),
            "question_gu": q.get("question", ""),
            "options_en": [opts[k] for k in LETTERS],
            "options_gu": [opts[k] for k in LETTERS],
            "answer": answer if answer in LETTERS else "",
            "topic": "Public Administration",
            "difficulty": "medium",
            "source_verified": not flagged and answer in LETTERS,
            "image_asset": "",
            "passage_en": "",
            "passage_gu": "",
            "explanation_en": "",
            "explanation_gu": "",
            "review_flag": flagged or answer not in LETTERS,
            "review_note": q.get("review_note", "") or ("" if answer in LETTERS else "Official answer is not A-D; manual schema review required."),
            "tip_en": "",
            "tip_gu": "",
            "official_answer": answer,
            "answer_source": q.get("answer_source", ""),
            "exam_session": session,
            "exam_date": q.get("exam_date", ""),
            "source_booklet_sl_no": q.get("source_booklet_sl_no", ""),
            "syllabus_unit": q.get("syllabus_unit"),
            "syllabus_mapping_status": q.get("syllabus_mapping_status", ""),
            "language": q.get("language", "en"),
            "verification_status": q.get("verification_status", "review_required"),
        })
    out.sort(key=lambda q: (q["exam_date"], q["question_no"]))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(out)} questions to {OUT}")
    print("Review flags:", sum(q["review_flag"] for q in out))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
