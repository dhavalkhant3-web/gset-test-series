#!/usr/bin/env python3
"""Audit the Mathematical Sciences Paper-II archive without auto-verifying OCR.

This tool is intentionally conservative: it reports missing, suspicious, or
unmapped records and only fails completeness when --require-complete is passed.
Official PDFs/final keys remain authoritative. It never edits question data.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_PATH = ROOT / "assets/subjects/mathematical_sciences/questions.json"
PAPER_PATH = ROOT / "assets/subjects/mathematical_sciences/papers.json"
ANSWER_VALUES = {"A", "B", "C", "D", "Z"}
QUESTION_NUMBER = re.compile(r"_q(\d+)$", re.IGNORECASE)
OCR_RISK = (
    "mathematical sciences-ii",
    "rough work",
    "instructions for the candidates",
    "p.t.o.",
    "omr answer sheet",
    "signature of the invigilator",
)

def question_number(record):
    match = QUESTION_NUMBER.search(str(record.get("id", "")))
    return int(match.group(1)) if match else None

def looks_like_cover_or_instruction(record):
    """Flag obvious booklet text that OCR may have misread as a numbered MCQ."""
    text = " ".join(
        [str(record.get("question_en") or "")]
        + [str(x) for x in (record.get("options_en") or [])]
    )
    text = re.sub(r"\s+", " ", text).strip().lower()
    markers = (
        "at the commencement of examination",
        "instructions for the candidates",
        "write your roll number in the space provided",
        "this paper consists of one hundred questions",
        "omr answer sheet",
        "signature of the invigilator",
        "tear off the paper seal",
        "do not accept a booklet",
        "rough work",
    )
    return any(marker in text for marker in markers)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", help="Limit the report to one exact paper_id")
    parser.add_argument(
        "--require-complete", action="store_true",
        help="Fail when a selected paper lacks any question number in 1..question_count",
    )
    args = parser.parse_args()

    questions = json.loads(QUESTION_PATH.read_text(encoding="utf-8"))
    index = json.loads(PAPER_PATH.read_text(encoding="utf-8"))
    if not isinstance(questions, list):
        raise SystemExit("questions.json root must be a list")
    papers = index.get("papers", [])
    by_paper = {str(item.get("paper_id", "")): item for item in papers}
    if args.paper and args.paper not in by_paper:
        raise SystemExit(f"Unknown Mathematical Sciences paper_id: {args.paper}")

    errors = []
    records_by_paper = defaultdict(list)
    seen_ids = set()
    seen_question_numbers = defaultdict(set)
    duplicates = defaultdict(list)
    high_risk = defaultdict(list)
    topic_counts = Counter()
    answer_counts = Counter()
    unverified = 0
    missing_source_reference = 0
    cover_instruction_suspects = defaultdict(list)

    selected = {args.paper} if args.paper else set(by_paper)
    for q in questions:
        qid = str(q.get("id") or "(missing-id)")
        pid = str(q.get("paper_id") or "")
        if qid in seen_ids:
            errors.append(f"duplicate question id: {qid}")
        seen_ids.add(qid)
        if pid not in by_paper:
            errors.append(f"{qid}: paper_id {pid!r} is absent from papers.json")
        records_by_paper[pid].append(q)
        if pid not in selected:
            continue

        number = question_number(q)
        if number is not None:
            if number in seen_question_numbers[pid]:
                duplicates[pid].append(number)
            seen_question_numbers[pid].add(number)

        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"{qid}: options_en must contain exactly four options")
        elif any(not str(option).strip() for option in options):
            high_risk[pid].append(qid + " (empty option)")
        answer = str(q.get("answer", "")).strip().upper()
        if answer not in ANSWER_VALUES:
            errors.append(f"{qid}: invalid answer value {answer!r}")
        answer_counts[answer] += 1

        source_verified = q.get("source_verified") is True
        if q.get("review_flag") is True or not source_verified:
            unverified += 1
        if q.get("source_verified") is False and q.get("review_flag") is not True:
            errors.append(f"{qid}: unverified source must remain review_flag=true")
        expected_paper_url = str(by_paper.get(pid, {}).get("question_paper_url") or "")
        expected_key_url = str(by_paper.get(pid, {}).get("answer_key_url") or "")
        if q.get("source_question_paper_url") != expected_paper_url:
            errors.append(f"{qid}: source_question_paper_url does not match papers.json")
        if q.get("source_answer_key_url") != expected_key_url:
            errors.append(f"{qid}: source_answer_key_url does not match papers.json")
        if not q.get("source_question_paper_url") or q.get("source_page") is None:
            missing_source_reference += 1

        topic = str(q.get("topic") or "").strip()
        topic_counts[topic or "(empty topic)"] += 1
        text = str(q.get("question_en") or "")
        lowered = text.lower()
        if looks_like_cover_or_instruction(q):
            cover_instruction_suspects[pid].append(qid)
        if (len(text.strip()) < 20
                or any(marker in lowered for marker in OCR_RISK)
                or "\ufffd" in text
                or len(re.findall(r"[^\w\s.,;:!?()\[\]{}+*/=<>|^%$\\-]", text)) > max(20, len(text) // 3)):
            high_risk[pid].append(qid)

    for pid, numbers in duplicates.items():
        if numbers:
            errors.append(
                f"{pid}: duplicate question numbers: " +
                ", ".join(map(str, sorted(set(numbers))[:30]))
            )

    for pid in sorted(selected):
        meta = by_paper[pid]
        actual = records_by_paper.get(pid, [])
        actual_count = len(actual)
        declared_loaded = meta.get("questions_loaded")
        declared_count = meta.get("questions_count")
        if declared_loaded is not None and int(declared_loaded) != actual_count:
            errors.append(f"{pid}: questions_loaded={declared_loaded}, actual={actual_count}")
        if declared_count is not None and int(declared_count) != actual_count:
            errors.append(f"{pid}: questions_count={declared_count}, actual={actual_count}")

        target = int(meta.get("question_count", 0) or 0)
        missing = sorted(set(range(1, target + 1)) - seen_question_numbers.get(pid, set()))
        beyond_target = sorted(n for n in seen_question_numbers.get(pid, set()) if target and n > target)
        status = "COMPLETE" if target and actual_count >= target and not missing else "INCOMPLETE"
        print(
            f"{pid}: {status}; records={actual_count}/{target}; "
            f"missing_numbers={len(missing)}; source_verified={sum(1 for x in actual if x.get('source_verified') is True)}; "
            f"review_required={sum(1 for x in actual if x.get('review_flag') is True or x.get('source_verified') is not True)}"
        )
        if missing:
            print("  Missing question numbers: " + ", ".join(map(str, missing)))
        if beyond_target:
            print("  Question IDs beyond declared target (check official cover page): " + ", ".join(map(str, beyond_target)))
        if args.require_complete and (status != "COMPLETE" or beyond_target):
            errors.append(f"{pid}: archive completeness gate failed")
        page_referenced = sum(1 for x in actual if x.get("source_page") is not None)
        generic_topics = sum(1 for x in actual if str(x.get("topic") or "").strip().lower() in ("", "mathematical sciences"))
        print(f"  Source-page coverage: {page_referenced}/{actual_count}; generic/unmapped topic labels: {generic_topics}/{actual_count}")
        if generic_topics:
            print("  WARNING: topic labels are generic; do not include these records in syllabus-unit tests until individually mapped.")
        if meta.get("source_verified") is True and meta.get("question_source_verified") is not True:
            print("  WARNING: paper-level source_verified=true but question_source_verified is not true")
        if meta.get("answer_key_verified") is not True:
            print("  Note: answer key has not been marked manually verified.")

    print("\nMathematical Sciences archive audit:")
    print(f"  Total records: {len(questions)}; unique IDs: {len(seen_ids)}")
    print(f"  Selected unverified/review-required records: {unverified}")
    print(f"  Selected records missing a source-page reference: {missing_source_reference}")
    suspect_total = sum(len(v) for k, v in cover_instruction_suspects.items() if k in selected)
    print(f"  Selected cover/instruction OCR suspects: {suspect_total}")
    for pid in sorted(selected):
        suspects = cover_instruction_suspects.get(pid, [])
        if suspects:
            print(f"  {pid} suspected non-question records: " + ", ".join(suspects[:30]))
    print(f"  Selected high-risk OCR records: {sum(len(v) for k,v in high_risk.items() if k in selected)}")
    print(f"  Most common topics: {topic_counts.most_common(6)}")
    print(f"  Selected answer counts: {dict(answer_counts)}")
    if errors:
        raise SystemExit("Mathematical Sciences audit failed:\n- " + "\n- ".join(errors))
    print("Audit structural checks passed. Source review and unit mapping remain separate tasks.")

if __name__ == "__main__":
    main()
