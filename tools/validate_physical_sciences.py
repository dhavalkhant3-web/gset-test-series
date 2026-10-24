#!/usr/bin/env python3
"""Validate the September 2018 Physical Sciences Q32/Q86 source audit."""
from __future__ import annotations
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "assets/subjects/physical_sciences/questions.json"
AUDIT_PATH = ROOT / "assets/subjects/physical_sciences/sept18_source_review.json"
PAPERS_PATH = ROOT / "assets/subjects/physical_sciences/papers.json"

EXPECTED_OPTIONS_32 = [
    "IV only", "I and III", "II and IV", "All four"
]
EXPECTED_OPTIONS_86 = [
    "Cubic", "Tetragonal", "Orthogonal", "Monoclinic"
]
EXPECTED_32 = "Listed below are the Maxwell's equations of electrodynamics. If magnetic monopoles exist, which of these equations have to be modified? I. ∇×H⃗ = J⃗ + ∂D⃗/∂t II. ∇×E⃗ = −∂B⃗/∂t III. ∇·D⃗ = ρ IV. ∇·B⃗ = 0"
EXPECTED_86 = "If the primitives a ≠ b ≠ c and interfacial angles α ≠ β ≠ γ ≠ 90°, then it belongs to the following crystal system:"

def fail(message):
    print("FAIL: " + message, file=sys.stderr)
    raise SystemExit(1)

def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail("cannot parse " + str(path.relative_to(ROOT)) + ": " + str(exc))

def compact(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()

def question_number(q):
    match = re.search(r"_q0*(\d+)$", str(q.get("id", "")))
    return int(match.group(1)) if match else None

def main():
    bank = read_json(BANK_PATH)
    audit = read_json(AUDIT_PATH)
    papers = read_json(PAPERS_PATH)
    if not isinstance(bank, list) or len(bank) != 1300:
        fail("expected 1,300 base question records")
    sep18 = [q for q in bank if q.get("paper_id") == "physical_sep18"]
    if len(sep18) != 100:
        fail("September 2018 Physical Sciences Paper-II must have 100 records; got " + str(len(sep18)))
    by_number = {question_number(q): q for q in sep18}
    if set(by_number) != set(range(1, 101)):
        fail("September 2018 paper has missing or duplicate question IDs")
    q32 = by_number[32]
    q86 = by_number[86]
    if compact(q32.get("question_en")) != compact(EXPECTED_32):
        fail("Q32 equation text differs from the source-checked Maxwell-equation transcription")
    if q32.get("options_en") != EXPECTED_OPTIONS_32 or q32.get("answer") != "C":
        fail("Q32 options or official answer differs from the original paper/final key")
    if compact(q86.get("question_en")) != compact(EXPECTED_86):
        fail("Q86 crystal-system wording differs from the source booklet")
    if q86.get("options_en") != EXPECTED_OPTIONS_86 or q86.get("answer") != "Z":
        fail("Q86 options or official final-key value differs from the source")
    by_id = {x.get("id"): x for x in audit}
    if set(by_id) != {"physical_sep18_q32", "physical_sep18_q86"}:
        fail("source-review overlay must contain exactly Q32 and Q86")
    for qid, answer in (("physical_sep18_q32", "C"), ("physical_sep18_q86", "Z")):
        fix = by_id[qid]
        if fix.get("answer") != answer or fix.get("source_verified") is not True or fix.get("review_flag") is not False:
            fail(qid + ": source-review overlay has incorrect verification/key state")
        if not all(str(fix.get(field, "")).strip() for field in ("explanation_en", "explanation_gu", "tip_en", "tip_gu")):
            fail(qid + ": bilingual explanation/tip fields are missing")
    q86_fix = by_id["physical_sep18_q86"]
    if q86_fix.get("evaluation_status") != "not_evaluated_official_final_key" or q86_fix.get("not_evaluated") is not True:
        fail("Q86 must preserve official Z/non-evaluated status")
    paper = next((p for p in papers.get("papers", []) if p.get("paper_id") == "physical_sep18"), None)
    if not paper:
        fail("September 2018 Paper-II metadata is missing")
    if not str(paper.get("question_paper_url", "")).endswith("/sept18/sept1802.pdf"):
        fail("official source-paper URL is incorrect")
    if not str(paper.get("answer_key_url", "")).endswith("/sept18/sept1802.pdf"):
        fail("official final-key URL is incorrect")
    print("PASS: September 2018 Paper-II contains all 100 questions, including Q32 and Q86.")
    print("PASS: Q32's Maxwell equations/options and official answer C match the source.")
    print("PASS: Q86's crystal-system wording/options and official Z/non-evaluated status match the source.")
    print("NOTE: this focused audit does not certify unrelated OCR/figure flags in the remaining archive.")

if __name__ == "__main__":
    main()
