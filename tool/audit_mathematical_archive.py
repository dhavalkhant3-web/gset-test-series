#!/usr/bin/env python3
"""Conservative audit for Mathematical Sciences Paper-II bank quality.

Never rewrites source content. Structural checks do not equal source verification.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "assets/subjects/mathematical_sciences"
EXPECTED = {
    "jan02": 50, "dec02": 50, "dec03": 50, "jul04": 50, "jul06": 50,
    "dec08": 50, "oct10": 50, "oct11": 50, "sep13": 50, "oct14": 50,
    "sep16": 50, "aug17": 50, "sep18": 100, "dec19": 100, "dec21": 100,
    "nov22": 100, "nov23": 100, "dec24": 100, "nov25": 100,
}
GENERIC = {
    "official gset final answer key is authoritative.",
    "official gset final answer key is authoritative",
    "official final answer key is authoritative.",
    "official final answer key authoritative છે.",
    "solution will be updated soon.",
    "explanation not available.",
    "no explanation available.",
}
OCR_SUSPECT = re.compile(r"(?:Mathematical Sciences-II|_{3,}|[|]{2,}|[“”‘’]{2,})", re.I)

def load(path):
    if not path.is_file():
        raise SystemExit("Missing required file: " + str(path))
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    questions = load(BASE / "questions.json")
    meta = load(BASE / "papers.json")
    if not isinstance(questions, list) or not isinstance(meta.get("papers"), list):
        raise SystemExit("Invalid question bank / papers metadata JSON schema.")
    errors, warnings = [], []
    ids = [q.get("id") for q in questions]
    missing_ids = [i for i, value in enumerate(ids) if not value]
    duplicate_ids = [v for v, n in Counter(ids).items() if v and n > 1]
    if missing_ids: errors.append(f"records with missing ID: {len(missing_ids)}")
    if duplicate_ids: errors.append(f"duplicate IDs: {duplicate_ids[:10]}")

    counts = Counter(str(q.get("paper_id") or q.get("paperId") or "") for q in questions)
    metadata = {p.get("paper_id"): p for p in meta["papers"]}
    question_flags = Counter()
    option_errors, bad_answers, generic, suspicious = [], [], [], []
    key_mismatches, missing_key_provenance = [], []
    for q in questions:
        qid = str(q.get("id") or "<missing-id>")
        pid = str(q.get("paper_id") or q.get("paperId") or "")
        options = q.get("options_en")
        if not isinstance(options, list) or len(options) != 4 or any(not str(x or "").strip() for x in (options or [])):
            option_errors.append(qid)
        if q.get("answer") not in {"A", "B", "C", "D", "Z", "X"}:
            bad_answers.append(qid)
        question_flags["review_flag_true" if q.get("review_flag") is True else "review_flag_not_true"] += 1
        question_flags["source_verified_true" if q.get("source_verified") is True else "source_verified_not_true"] += 1
        ex_en = str(q.get("explanation_en") or "").strip()
        ex_gu = str(q.get("explanation_gu") or "").strip()
        if ex_en.lower() in GENERIC or ex_gu.lower() in GENERIC or len(ex_en) < 35 or len(ex_gu) < 20:
            generic.append(qid)
        combined = " ".join([str(q.get("question_en") or ""), *(str(x or "") for x in (options or []))])
        if OCR_SUSPECT.search(combined):
            suspicious.append(qid)
        if not pid:
            errors.append(f"{qid}: missing paper_id")
    if option_errors: errors.append(f"missing/invalid four-option lists: {len(option_errors)}")
    if bad_answers: errors.append(f"invalid answer labels: {len(bad_answers)}")

    papers_missing_metadata = []
    incomplete, unverified_key, falsely_verified = [], [], []
    for session, expected in EXPECTED.items():
        pid = "mathematical_sciences_" + session
        found = counts.get(pid, 0)
        if pid not in metadata: papers_missing_metadata.append(pid)
        if found != expected: incomplete.append(f"{session}={found}/{expected}")
        p = metadata.get(pid, {})
        key_path = BASE / "answer_keys" / (session + "_paper2.json")
        key_record = None
        if key_path.is_file():
            try: key_record = json.loads(key_path.read_text(encoding="utf-8"))
            except Exception: pass
        answers = key_record.get("answers", {}) if key_record else {}
        has_verified_key = bool(
            key_record and key_record.get("source_verified") is True
            and len(answers) == expected
            and set(answers) == {str(n) for n in range(1, expected + 1)}
            and all(a in {"A", "B", "C", "D", "Z"} for a in answers.values())
        )
        if p.get("answer_key_verified") is True and not has_verified_key:
            unverified_key.append(session)
        if has_verified_key:
            expected_source = str(key_path.relative_to(BASE.parents[2]))
            for item in questions:
                if str(item.get("paper_id") or item.get("paperId") or "") != pid:
                    continue
                match = re.search(r"_q(\\d+)$", str(item.get("id") or ""), re.I)
                if not match:
                    continue
                number = match.group(1)
                official = answers.get(number)
                if official is None:
                    continue
                if item.get("answer") != official:
                    key_mismatches.append(f"{item.get('id')}: bank={item.get('answer')}, official={official}")
                if item.get("answer_key_verified") is not True or item.get("answer_key_source") != expected_source:
                    missing_key_provenance.append(str(item.get("id")))
        if p.get("source_verified") is True or p.get("question_source_verified") is True:
            # Metadata cannot self-certify. Question-level records need separate provenance.
            if found != expected or any(q.get("paper_id") == pid and q.get("source_verified") is not True
                                        for q in questions):
                falsely_verified.append(session)

    if papers_missing_metadata: errors.append("missing paper metadata: " + ", ".join(papers_missing_metadata))
    if falsely_verified: errors.append("sessions claim source verification without complete verified records: " + ", ".join(falsely_verified))
    if key_mismatches: errors.append("answer mismatches against verified official keys: " + "; ".join(key_mismatches[:20]))
    if missing_key_provenance: errors.append("records matched to verified official keys but missing answer-key provenance: " + ", ".join(missing_key_provenance[:20]))
    warnings.append(f"session counts incomplete: {len(incomplete)}/19 ({'; '.join(incomplete)})")
    warnings.append(f"answer-key metadata unsupported by a complete verified key JSON: {len(unverified_key)} ({', '.join(unverified_key) or 'none'})")
    warnings.append(f"generic/empty explanations: {len(generic)} question records")
    warnings.append(f"OCR/footer contamination patterns: {len(suspicious)} question records")
    warnings.append(f"review_flag true: {question_flags['review_flag_true']}/{len(questions)}")
    warnings.append(f"source_verified true: {question_flags['source_verified_true']}/{len(questions)}")
    warnings.append(f"question records cross-checked against official verified answer keys: {sum(1 for q in questions if q.get('answer_key_verified') is True)}/{len(questions)}")
    print(f"Mathematical Sciences Paper-II audit: {len(questions)} records, {len(EXPECTED)} sessions, expected total {sum(EXPECTED.values())}")
    for warning in warnings: print("WARNING: " + warning)
    if option_errors: print("OPTION ERRORS (first 20): " + ", ".join(option_errors[:20]))
    if bad_answers: print("ANSWER ERRORS (first 20): " + ", ".join(bad_answers[:20]))
    if suspicious: print("OCR SUSPECTS (first 20): " + ", ".join(suspicious[:20]))
    if generic: print("GENERIC EXPLANATIONS (first 20): " + ", ".join(generic[:20]))
    if errors:
        for error in errors: print("ERROR: " + error)
        return 1
    print("STRUCTURAL AUDIT COMPLETE. This does NOT assert question wording, notation, options, or answers are source-verified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
