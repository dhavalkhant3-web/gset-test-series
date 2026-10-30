#!/usr/bin/env python3
"""Validate unit mapping only when explicit and syllabus-backed."""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "assets/subjects/syllabus_units.json"
SUBJECTS_ROOT = ROOT / "assets/subjects"
QUESTION_FILES = {
    "02": "physical_sciences/questions.json",
    "03": "chemical_sciences/questions.json",
    "28": "hindu_studies/questions.json",
    "29": "indian_knowledge_system/questions.json",
    "30": "music/questions.json",
    "31": "performing_art_dance_drama_theatre/questions.json",
    "32": "public_administration/questions.json",
    "33": "visual_art/questions.json",
}
UNIT_FIELDS = ("syllabus_unit", "unit_number", "unit")
UNIT_ID_FIELDS = ("unit_id", "unitId")
UNVERIFIED_STATUS_TERMS = ("pending", "provisional", "ambiguous", "manual_review_required", "review_required")

def fail(message: str) -> None:
    print("FAIL: " + message, file=sys.stderr)
    raise SystemExit(1)

def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")

def resolve_unit(q, units):
    values = []
    for field in UNIT_FIELDS + UNIT_ID_FIELDS:
        value = q.get(field)
        if value is not None and str(value).strip():
            values.append((field, str(value).strip()))
    if not values:
        return None, None
    number_matches = []
    for field, value in values:
        match = next((u for u in units if value in {
            str(u.get("number", "")), str(u.get("id", ""))
        }), None)
        if match is None:
            return None, f"{field}={value!r} does not reference a configured unit"
        number_matches.append(str(match.get("number")))
    if len(set(number_matches)) > 1:
        return None, "conflicting unit fields"
    return next(u for u in units if str(u.get("number")) == number_matches[0]), None

def main():
    cfg = load(CONFIG)
    subject_cfg = cfg.get("subjects", {})
    errors = []
    for code, rel in QUESTION_FILES.items():
        sid = Path(rel).parts[0]
        subject = subject_cfg.get(sid)
        if not subject:
            errors.append(f"{sid}: missing official syllabus configuration")
            continue
        units = subject.get("units", [])
        numbers = [str(u.get("number")) for u in units]
        ids = [str(u.get("id")) for u in units]
        if not units or len(numbers) != len(set(numbers)) or len(ids) != len(set(ids)):
            errors.append(f"{sid}: missing or duplicate configured unit numbers/IDs")
            continue
        if not str(subject.get("official_pdf", "")).startswith(("https://www.gujaratset.ac.in/assets/syllabus/", "https://gujaratset.ac.in/assets/syllabus/")):
            errors.append(f"{sid}: official syllabus URL missing or non-GSET")
            continue
        bank_path = SUBJECTS_ROOT / rel
        if not bank_path.exists():
            print(f"{sid}: bank absent; skipped")
            continue
        bank = load(bank_path)
        if not isinstance(bank, list):
            errors.append(f"{sid}: question bank root must be a list")
            continue
        seen, mapped, pending = set(), Counter(), 0
        for q in bank:
            qid = str(q.get("id") or "(missing-id)")
            if qid in seen:
                errors.append(f"{sid}: duplicate question ID {qid}")
            seen.add(qid)
            unit, problem = resolve_unit(q, units)
            if problem:
                errors.append(f"{sid}/{qid}: invalid mapping: {problem}")
                continue
            if unit is None:
                pending += 1
                continue
            mapped[str(unit.get("number"))] += 1
            status = str(q.get("syllabus_mapping_status", "")).strip().lower()
            if not status or any(term in status for term in UNVERIFIED_STATUS_TERMS):
                pending += 1
        print(f"{sid} (code {code}): total={len(bank)}, explicitly_mapped={sum(mapped.values())}, pending_or_unverified={pending}")
        for unit in units:
            print(f"  Unit {unit.get('number')}: {mapped[str(unit.get('number'))]}")
    if errors:
        fail("unit-mapping validation errors:\n- " + "\n- ".join(errors))
    print("PASS: configured syllabus references and explicit unit references are structurally valid.")
    print("NOTE: this validator does not infer mappings; unassigned questions remain pending.")
if __name__ == "__main__":
    main()
