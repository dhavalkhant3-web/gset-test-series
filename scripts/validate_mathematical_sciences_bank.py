#!/usr/bin/env python3
"""Read-only integrity gate for the Mathematical Sciences question bank.

This script does not repair OCR, infer missing questions, or change answers.
It intentionally fails closed when the bank is missing or contains unverified
records. Run from the repository root.
"""
import json
import sys
from collections import Counter
from pathlib import Path

BANK = Path("assets/subjects/mathematical_sciences/questions.json")
VALID_ANSWERS = {"A", "B", "C", "D", "Z"}


def main() -> int:
    if not BANK.exists() or BANK.stat().st_size == 0:
        print(f"FAIL: question bank missing or empty: {BANK}")
        return 2

    try:
        records = json.loads(BANK.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: invalid JSON: {exc}")
        return 2

    if not isinstance(records, list):
        print("FAIL: bank root must be a JSON array")
        return 2

    errors = []
    ids = [r.get("id") for r in records if isinstance(r, dict)]
    duplicate_ids = [key for key, count in Counter(ids).items() if key is None or count > 1]
    if duplicate_ids:
        errors.append(f"missing/duplicate IDs: {duplicate_ids[:20]}")

    per_paper = Counter()
    unverified = []
    flagged = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record {index}: not an object")
            continue
        paper_id = record.get("paper_id")
        per_paper[paper_id or "<missing>"] += 1
        if not isinstance(record.get("question_en"), str) or not record["question_en"].strip():
            errors.append(f"{record.get('id', index)}: empty English question")
        options = record.get("options_en")
        if not isinstance(options, list) or len(options) != 4 or any(
            not isinstance(option, str) or not option.strip() for option in (options or [])
        ):
            errors.append(f"{record.get('id', index)}: expected four non-empty English options")
        answer = record.get("answer")
        if answer not in VALID_ANSWERS:
            errors.append(f"{record.get('id', index)}: invalid answer label {answer!r}")
        if record.get("source_verified") is not True:
            unverified.append(record.get("id", str(index)))
        if record.get("review_flag") is True:
            flagged.append(record.get("id", str(index)))

        # A released/verified record must include the bilingual learning fields.
        # Draft/unverified records may remain incomplete, but cannot pass release.
        if record.get("source_verified") is True:
            if record.get("review_flag") is not False:
                errors.append(
                    f"{record.get('id', index)}: source_verified record must have review_flag=false"
                )
            required_learning_fields = (
                "question_gu", "options_gu", "explanation_en",
                "explanation_gu", "tip_en", "tip_gu",
            )
            for field in required_learning_fields:
                value = record.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(
                        f"{record.get('id', index)}: verified record missing {field}"
                    )
            options_gu = record.get("options_gu")
            if not isinstance(options_gu, list) or len(options_gu) != 4 or any(
                not isinstance(option, str) or not option.strip()
                for option in (options_gu or [])
            ):
                errors.append(
                    f"{record.get('id', index)}: verified record expected four non-empty Gujarati options"
                )

    print(f"Records: {len(records)}")
    print(f"Papers: {len(per_paper)}")
    print(f"Records not source-verified: {len(unverified)}")
    print(f"Records still review-flagged: {len(flagged)}")
    print("Per-paper record counts:")
    for paper_id, count in sorted(per_paper.items()):
        print(f"  {paper_id}: {count}")

    if errors:
        print(f"STRUCTURAL ERRORS ({len(errors)}):")
        for error in errors[:100]:
            print(f"  - {error}")
    if unverified:
        print("Source verification is incomplete; no record is cleared by this script.")
    # Verification is a human/source-backed process. This integrity script only
    # checks structure and refuses to imply that structural validity means accuracy.
    return 1 if errors or unverified or flagged else 0


if __name__ == "__main__":
    sys.exit(main())
