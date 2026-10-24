#!/usr/bin/env python3
"""Validate Chemical Sciences Paper-II integration and the September 2016 missing-session overlay."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "assets/subjects/chemical_sciences/questions.json"
SEP16_PATH = ROOT / "assets/subjects/chemical_sciences/questions_sep16_p2.json"
SEP16_P3_PATH = ROOT / "assets/subjects/chemical_sciences/questions_sep16_p3.json"
PAPERS_PATH = ROOT / "assets/subjects/chemical_sciences/papers.json"
SUBJECTS_PATH = ROOT / "assets/subjects/subjects.json"
SEP16_KEY = "AADBCBCAAACBBBABCCCDABBCBBCDCDABCCACCCCABDACBACADB"

def fail(message):
    print("FAIL: " + message, file=sys.stderr)
    raise SystemExit(1)

def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail("cannot parse " + str(path.relative_to(ROOT)) + ": " + str(exc))

def main():
    base = read_json(BANK_PATH)
    p2 = read_json(SEP16_PATH)
    p3 = read_json(SEP16_P3_PATH)
    papers_data = read_json(PAPERS_PATH)
    registry = read_json(SUBJECTS_PATH)
    if not isinstance(base, list) or len(base) != 1250:
        fail("expected 1,250 base Paper-II questions, got " + str(len(base) if isinstance(base, list) else type(base).__name__))
    if not isinstance(p2, list) or len(p2) != 50:
        fail("expected 50 September 2016 Paper-II overlay records")
    if not isinstance(p3, list) or len(p3) != 75:
        fail("September 2016 Paper-III archive must remain a separate 75-question file")
    base_ids = [q.get("id") for q in base]
    p2_ids = [q.get("id") for q in p2]
    if len(set(base_ids)) != len(base_ids) or len(set(p2_ids)) != 50:
        fail("duplicate or missing IDs in base/September 2016 bank")
    if set(base_ids).intersection(p2_ids):
        fail("September 2016 Paper-II overlay duplicates IDs already in base bank")
    p2_numbers = sorted(q.get("question_no") for q in p2)
    if p2_numbers != list(range(1, 51)):
        fail("September 2016 Paper-II overlay must contain Q1–Q50 exactly once")
    if len(SEP16_KEY) != 50:
        fail("embedded official final key must contain 50 letters")
    for q in p2:
        n = q.get("question_no")
        qid = q.get("id")
        if qid != "chemical_sep16_q" + str(n):
            fail(str(qid) + ": question ID/number mismatch")
        if q.get("paper_id") != "chemical_sep16":
            fail(str(qid) + ": wrong paper_id")
        answer = q.get("official_answer", q.get("answer"))
        expected = SEP16_KEY[n - 1]
        if answer != expected or q.get("answer") != expected:
            fail(str(qid) + ": stored answer does not match official final answer key " + expected)
        if not isinstance(q.get("question_en"), str) or not q["question_en"].strip():
            fail(str(qid) + ": missing question text")
        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4:
            fail(str(qid) + ": expected four options")
        if q.get("review_flag") and not q.get("review_note"):
            fail(str(qid) + ": unresolved review flag has no review note")
    all_paper_ii = base + p2
    all_ids = [q.get("id") for q in all_paper_ii]
    if len(all_paper_ii) != 1300 or len(set(all_ids)) != 1300:
        fail("combined Paper-II bank must contain 1,300 unique records")
    if any(q.get("paper_id") == "chemical_sep16_p3" for q in all_paper_ii):
        fail("Paper-III questions must not be appended to the Paper-II bank")
    paper = next((p for p in papers_data.get("papers", []) if p.get("paper_id") == "chemical_sep16"), None)
    if not paper:
        fail("September 2016 Paper-II metadata missing")
    if paper.get("question_count") != 50:
        fail("September 2016 Paper-II metadata question_count must remain 50")
    if not str(paper.get("question_paper_url", "")).endswith("/sept16/sept1603.pdf"):
        fail("September 2016 question-paper URL does not point to official Paper-II source")
    if not str(paper.get("answer_key_url", "")).endswith("/sept16/sept1603.pdf"):
        fail("September 2016 answer-key URL does not point to official final key")
    subject = next((s for s in registry.get("subjects", []) if s.get("id") == "chemical_sciences"), None)
    if not subject or subject.get("questions_loaded") != 1300 or subject.get("source_verified") is not False:
        fail("subject registry must report 1,300 Paper-II questions while retaining incomplete source-review status")
    print("PASS: 1,250 base questions + 50 September 2016 Paper-II records = 1,300.")
    print("PASS: September 2016 Q1-Q50 all match the official FINAL answer key.")
    print("PASS: 75 Paper-III questions remain separate; source-review status is not overstated.")

if __name__ == "__main__":
    main()
