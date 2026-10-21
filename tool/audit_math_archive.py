#!/usr/bin/env python3
"""Quality audit for Mathematical Sciences Paper-II imports.

This tool deliberately does not correct or verify OCR text. It detects records
that need comparison with the original GSET paper and writes a CSV/JSON report.
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path("assets/subjects/mathematical_sciences")
QUESTIONS = ROOT / "questions.json"
PAPERS = ROOT / "papers.json"
OUT = Path("build/math-source-audit")
INSTRUCTION = re.compile(
    r"commencement of examination|question booklet|answer sheet|"
    r"roll number|roll no\.?|invigilator|no negative marking|"
    r"this paper consists|each item has (?:upto |up to )?four alternative",
    re.I,
)
FOOTER = re.compile(r"mathematical sciences\s*[-–]?\s*(?:i|ii|iii)?\s*\d*|page\s*\d+|www\.gujaratset\.ac\.in", re.I)
QUESTION_START = re.compile(r"(?<!^)(?:^|\s)\d{1,3}[.)]\s+[A-Z]", re.M)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if not QUESTIONS.exists() or QUESTIONS.stat().st_size == 0:
        raise SystemExit(f"BLOCKER: {QUESTIONS} is missing or empty; restore/import source records before auditing.")
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    meta = json.loads(PAPERS.read_text(encoding="utf-8"))
    if not isinstance(questions, list):
        raise SystemExit("BLOCKER: questions.json must be a JSON list")
    expected = {p["paper_id"]: int(p["question_count"]) for p in meta.get("papers", [])}
    grouped = {}
    for q in questions:
        grouped.setdefault(q.get("paper_id", "MISSING_PAPER_ID"), []).append(q)
    rows = []
    for paper_id, total in expected.items():
        records = grouped.get(paper_id, [])
        ids = [q.get("id", "") for q in records]
        numbers = []
        for rid in ids:
            m = re.search(r"_q(\d+)$", rid)
            if m:
                numbers.append(int(m.group(1)))
        dup_ids = len(ids) - len(set(ids))
        dup_nums = len(numbers) - len(set(numbers))
        missing = sorted(set(range(1, total + 1)) - set(numbers))
        bad = 0
        for q in records:
            stem = str(q.get("question_en", ""))
            options = q.get("options_en", [])
            reasons = []
            if len(stem.strip()) < 12: reasons.append("short_or_empty_stem")
            if INSTRUCTION.search(stem): reasons.append("exam_instruction_in_stem")
            if FOOTER.search(stem): reasons.append("footer_in_stem")
            if QUESTION_START.search(stem): reasons.append("possible_merged_question")
            if not isinstance(options, list) or len(options) != 4: reasons.append("not_four_options")
            elif any(INSTRUCTION.search(str(o)) or FOOTER.search(str(o)) or QUESTION_START.search(str(o)) for o in options):
                reasons.append("instruction_footer_or_next_question_in_option")
            if q.get("source_verified") is not True or q.get("review_flag") is True:
                reasons.append("not_source_verified")
            if reasons:
                bad += 1
            rows.append({
                "paper_id": paper_id, "exam": records[0].get("exam", "") if records else "",
                "question_id": q.get("id", ""), "source_verified": q.get("source_verified", False),
                "review_flag": q.get("review_flag", False), "reasons": ";".join(reasons),
                "question_en": stem[:500], "options_en": json.dumps(options, ensure_ascii=False)[:800],
            })
        print(f"{paper_id}: {len(records)}/{total} records; missing question numbers={len(missing)}; "
              f"flagged={bad}; duplicate_ids={dup_ids}; duplicate_numbers={dup_nums}")
        (OUT / f"{paper_id}_missing_numbers.json").write_text(
            json.dumps(missing, indent=2), encoding="utf-8")
    with (OUT / "question_review.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["paper_id","exam","question_id","source_verified","review_flag","reasons","question_en","options_en"])
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "paper_count": len(expected), "question_records": len(questions),
        "unmapped_paper_ids": sorted(set(grouped) - set(expected)),
        "records_not_source_verified": sum(q.get("source_verified") is not True for q in questions),
        "records_review_flagged": sum(q.get("review_flag") is True for q in questions),
        "paper_counts": {p: {"expected": n, "loaded": len(grouped.get(p, []))} for p, n in expected.items()},
        "note": "This is a triage report, not a source verification. Never clear review flags from heuristics."
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Audit report: {OUT}")

if __name__ == "__main__":
    main()
