#!/usr/bin/env python3
"""Audit all in-scope Paper-II banks for data integrity, language policy, tips, source flags and unit mapping."""
from __future__ import annotations
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECT_ROOT = ROOT / "assets/subjects"
CONFIG_PATH = SUBJECT_ROOT / "syllabus_units.json"
REGISTRY_PATH = SUBJECT_ROOT / "subjects.json"
IN_SCOPE = {
    "02": ("physical_sciences", "questions.json"),
    "03": ("chemical_sciences", "questions.json"),
    "28": ("hindu_studies", "questions.json"),
    "29": ("indian_knowledge_system", "questions.json"),
    "30": ("music", "questions.json"),
    "31": ("performing_art_dance_drama_theatre", "questions.json"),
    "32": ("public_administration", "questions.json"),
    "33": ("visual_art", "questions.json"),
}
ENGLISH_ONLY = {"02", "03", "29", "32", "33"}
EXCLUDED_CODE = "01"
ANSWERS = {"A", "B", "C", "D", "X", "Z"}
SOURCE_FLAG_TERMS = re.compile(r"pending|review|not verified|not yet|unclear|unresolved|incomplete|not transcribed|needs|remain|audit", re.I)
GUJARATI_SCRIPT = re.compile(r"[\u0A80-\u0AFF]")
LATIN_SCRIPT = re.compile(r"[A-Za-z]")

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"FAIL: could not parse {path}: {exc}")

def meaningful_string_list(value):
    return isinstance(value, list) and all(isinstance(x, str) for x in value)

def main():
    config = load(CONFIG_PATH).get("subjects", {})
    registry = load(REGISTRY_PATH).get("subjects", [])
    by_code = {str(x.get("code")): x for x in registry}
    all_errors = []
    report = []
    for code, (sid, filename) in IN_SCOPE.items():
        bank_path = SUBJECT_ROOT / sid / filename
        if not bank_path.exists():
            all_errors.append(f"{code}/{sid}: missing bank {bank_path.relative_to(ROOT)}")
            continue
        bank = load(bank_path)
        if not isinstance(bank, list):
            all_errors.append(f"{code}/{sid}: bank root is not a list")
            continue
        units = config.get(sid, {}).get("units", [])
        valid_units = {str(u.get("number")) for u in units}
        ids, seen_questions = set(), set()
        counters = Counter()
        unresolved_examples, invalid_mappings, duplicate_ids = [], [], []
        for q in bank:
            qid = str(q.get("id") or "")
            session = str(q.get("exam_session") or q.get("paper_id") or "")
            num = q.get("question_no")
            if not qid or qid in ids:
                duplicate_ids.append(qid or "(missing ID)")
            ids.add(qid)
            if num is not None:
                k = (session, str(num))
                if k in seen_questions:
                    all_errors.append(f"{sid}/{qid}: duplicate session/question number {k}")
                seen_questions.add(k)
            en = q.get("question_en", "")
            if not isinstance(en, str) or not en.strip():
                counters["missing_question"] += 1
            if not meaningful_string_list(q.get("options_en")) or len(q.get("options_en", [])) != 4 or any(not str(x).strip() for x in q.get("options_en", [])):
                counters["invalid_english_options"] += 1
            ans = str(q.get("answer") or "")
            if ans not in ANSWERS:
                counters["invalid_answer"] += 1
            if not isinstance(q.get("tip_en"), str) or not q["tip_en"].strip():
                counters["missing_tip_en"] += 1
            if not isinstance(q.get("tip_gu"), str) or not q["tip_gu"].strip():
                counters["missing_tip_gu"] += 1
            qgu = q.get("question_gu", "")
            ogu = q.get("options_gu", [])
            if code in ENGLISH_ONLY:
                if qgu and (not isinstance(qgu, str) or qgu.strip()):
                    counters["unexpected_gu_question"] += 1
                if ogu not in ([], None):
                    counters["unexpected_gu_options"] += 1
            elif code == "28":
                # Official Hindu Studies source is English-only in Nov 2023 and Dec 2024;
                # the Nov 2025 paper is bilingual. Never fabricate Gujarati for prior sessions.
                session_l = session.lower()
                gujarati_expected = (
                    "nov25" in session_l or
                    "november 2025" in session_l or
                    ("hindu_studies" in session_l and "2025" in session_l)
                )
                valid_options_gu = (
                    isinstance(ogu, list) and len(ogu) == 4 and
                    all(isinstance(x, str) and x.strip() for x in ogu)
                )
                gujarati_stem_present = isinstance(qgu, str) and bool(GUJARATI_SCRIPT.search(qgu))
                gujarati_present = gujarati_stem_present and valid_options_gu
                if gujarati_expected and not gujarati_present:
                    counters["gujarati_source_transcription_missing"] += 1
                elif not gujarati_expected and gujarati_stem_present:
                    counters["unexpected_gujarati_for_english_source"] += 1
                if gujarati_present:
                    counters["gujarati_source_fields_populated"] += 1
                elif gujarati_expected and qgu and not gujarati_stem_present:
                    counters["gujarati_stem_missing_script"] += 1
                if gujarati_present and any(LATIN_SCRIPT.search(x) for x in ogu):
                    counters["gujarati_options_contain_latin_text"] += 1
            elif code == "30":
                valid_options_gu = (
                    isinstance(ogu, list) and len(ogu) == 4 and
                    all(isinstance(x, str) and x.strip() for x in ogu)
                )
                gujarati_stem_present = isinstance(qgu, str) and bool(GUJARATI_SCRIPT.search(qgu))
                gujarati_present = gujarati_stem_present and valid_options_gu
                if not gujarati_present:
                    counters["gujarati_source_transcription_missing"] += 1
                else:
                    counters["gujarati_source_fields_populated"] += 1
                if gujarati_stem_present and valid_options_gu and any(LATIN_SCRIPT.search(x) for x in ogu):
                    counters["gujarati_options_contain_latin_text"] += 1
                provenance = str(q.get("gujarati_source") or "").lower()
                if gujarati_present and "visually checked" in provenance:
                    counters["gujarati_source_visual_proofread"] += 1
                elif gujarati_present:
                    counters["gujarati_source_visual_review_pending"] += 1
            elif code == "31":
                gu_present = bool(isinstance(qgu, str) and qgu.strip()) or bool(isinstance(ogu, list) and any(isinstance(x, str) and x.strip() for x in ogu))
                if gu_present:
                    counters["some_gujarati_source_text_present"] += 1
                else:
                    counters["gujarati_source_transcription_missing"] += 1
                if isinstance(qgu, str) and qgu.strip() and not GUJARATI_SCRIPT.search(qgu):
                    counters["question_gu_has_no_gujarati_script"] += 1
                if isinstance(ogu, list) and any(str(x).strip() for x in ogu) and any(LATIN_SCRIPT.search(str(x)) for x in ogu):
                    counters["option_gu_has_latin_text"] += 1
            # Record unresolved source state, never upgrading any flag.
            # Keep source verification and review flags as independent dimensions.
            # A verified source page can still carry a separate content/mapping concern.
            if q.get("source_verified") is True:
                counters["source_verified_records"] += 1
            if q.get("review_flag") is True or q.get("source_verified") is False:
                counters["source_review_required"] += 1
                if len(unresolved_examples) < 20:
                    unresolved_examples.append(qid)
            # Verify every declared unit number actually exists; keep pending if not explicitly mapped.
            unit_values = [q.get(k) for k in ("syllabus_unit", "unit_number") if q.get(k) not in (None, "")]
            unit_id_values = [q.get(k) for k in ("unit_id", "unitId") if q.get(k) not in (None, "")]
            declared = []
            for value in unit_values:
                match = next((u for u in units if str(u.get("number")) == str(value) or str(u.get("id")) == str(value)), None)
                if match:
                    declared.append(str(match.get("number")))
                else:
                    try:
                        declared.append(str(int(value)))
                    except (ValueError, TypeError):
                        invalid_mappings.append((qid, f"invalid unit number/ID {value!r}"))
            for value in unit_id_values:
                match = next((u for u in units if str(u.get("id")) == str(value) or str(u.get("number")) == str(value)), None)
                if not match:
                    invalid_mappings.append((qid, f"unit ID {value!r} not in syllabus config"))
                else:
                    declared.append(str(match.get("number")))
            if declared:
                if len(set(declared)) != 1 or declared[0] not in valid_units:
                    invalid_mappings.append((qid, f"conflicting/invalid unit fields {declared}"))
                else:
                    counters["declared_unit_reference"] += 1
                    status = str(q.get("syllabus_mapping_status") or "").strip().lower()
                    unverified_status = (
                        not status or any(term in status for term in (
                            "pending", "provisional", "ambiguous", "manual_review_required", "review_required"
                        ))
                    )
                    if unverified_status:
                        counters["declared_but_unverified_unit"] += 1
                    else:
                        counters["explicitly_mapped_status"] += 1
            else:
                counters["unit_mapping_pending"] += 1
        if duplicate_ids:
            all_errors.append(f"{sid}: missing/duplicate IDs (first 10): {duplicate_ids[:10]}")
        if invalid_mappings:
            all_errors.extend([f"{sid}/{qid}: {problem}" for qid, problem in invalid_mappings[:25]])
        reg = by_code.get(code, {})
        paper_path = SUBJECT_ROOT / sid / "papers.json"
        paper_flags = []
        if paper_path.exists():
            pdata = load(paper_path)
            paper_list = pdata.get("papers", []) if isinstance(pdata, dict) else []
            for p in paper_list:
                if p.get("unit_mapping_status") != "pending_official_syllabus_unit_mapping":
                    paper_flags.append(f"{p.get('paper_id')}: mapping status differs from per-question pending state")
        report.append({
            "code": code, "subject_id": sid, "questions": len(bank), "unique_ids": len(ids),
            "source_verified_subject": reg.get("source_verified"),
            "source_verified_records": counters["source_verified_records"],
            "source_review_required": counters["source_review_required"],
            "missing_tip_en": counters["missing_tip_en"], "missing_tip_gu": counters["missing_tip_gu"],
            "missing_question": counters["missing_question"], "invalid_english_options": counters["invalid_english_options"],
            "invalid_answer": counters["invalid_answer"], "unit_mapping_pending": counters["unit_mapping_pending"],
            "declared_unit_reference": counters["declared_unit_reference"], "declared_but_unverified_unit": counters["declared_but_unverified_unit"],
            "explicitly_mapped_status": counters["explicitly_mapped_status"],
            "language_audit": {k:v for k,v in counters.items() if "gujarati" in k or "gu_" in k or "option_gu" in k or "unexpected_gu" in k},
            "unresolved_question_id_examples": unresolved_examples,
            "invalid_mappings_count": len(invalid_mappings),
            "paper_metadata_flags": paper_flags,
        })
    print(json.dumps({"audit":report,"errors":all_errors,"excluded_subject_01":"not read or changed"},ensure_ascii=False,indent=2))
    if all_errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
