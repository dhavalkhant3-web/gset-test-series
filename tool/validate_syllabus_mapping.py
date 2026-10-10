import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cfg = json.loads((ROOT / "assets/subjects/syllabus_units.json").read_text(encoding="utf-8"))
BANKS = {
    "mathematical_sciences": "assets/subjects/mathematical_sciences/questions.json",
    "physical_sciences": "assets/subjects/physical_sciences/questions.json",
    "chemical_sciences": "assets/subjects/chemical_sciences/questions.json",
}

def topic_unit(sid, q):
    t = str(q.get("topic") or "").lower().strip()
    if not t: return None
    if sid == "chemical_sciences":
        rules = [
          (1, ("coordination chemistry","organometallic","bioinorganic","chemical bonding","atomic structure"), ("inorganic chemistry",)),
          (2, ("quantum chemistry","thermodynamics","statistical mechanics","chemical kinetics","electrochemistry","solid state chemistry","polymer chemistry"), ("physical chemistry",)),
          (3, ("stereochemistry","medicinal chemistry","supramolecular chemistry"), ("organic chemistry",)),
          (4, ("analytical","spectroscopy","environmental","biochemistry","materials","nanoscience","nuclear chemistry","interdisciplinary","physical/environmental","physical/polymer"), ()),
        ]
        for n, contains, prefixes in rules:
            if any(x in t for x in contains) or any(t == x or t.startswith(x+" -") for x in prefixes): return n
    if sid == "physical_sciences":
        rules = [
          (1, ("mathematical physics","mathematical methods"), ()),
          (2, ("classical mechanics","charged particle motion","waves"), ("relativity",)),
          (3, ("electromagnet","electrodynamics","electrostatics","magnetism","plasma physics","radiation"), ()),
          (4, ("quantum mechanics","quantum scattering"), ()),
          (5, ("statistical physics","statistical mechanics","thermodynamics"), ()),
          (6, ("electronics","experimental physics","detector","detection"), ()),
          (7, ("atomic physics","molecular physics","optics","modern physics"), ()),
          (8, ("solid state","condensed matter","x-ray physics","diffraction"), ()),
          (9, ("nuclear physics","particle physics","nuclear/particle"), ()),
        ]
        for n, contains, equals in rules:
            if any(x in t for x in contains) or t in equals: return n
    return None

def main():
    errors=[]
    for sid, rel in BANKS.items():
        subject=cfg.get("subjects",{}).get(sid)
        if not subject:
            errors.append(f"{sid}: missing syllabus configuration")
            continue
        units=subject.get("units",[])
        ids=[str(u.get("id","")) for u in units]
        nums=[str(u.get("number","")) for u in units]
        if len(ids)!=len(set(ids)) or len(nums)!=len(set(nums)):
            errors.append(f"{sid}: duplicate syllabus unit IDs/numbers")
            continue
        path=ROOT/rel
        if not path.exists():
            print(f"{sid}: question bank absent; skipped")
            continue
        qs=json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(qs,list):
            errors.append(f"{sid}: question bank root is not a list")
            continue
        bynum={str(u.get("number")):u for u in units}
        counts=Counter(); seen=set(); dup=[]; unassigned=0; invalid=[]; review=0
        for q in qs:
            qid=str(q.get("id") or "(missing-id)")
            if qid in seen: dup.append(qid)
            seen.add(qid)
            uid=str(q.get("unit_id") or q.get("unitId") or "").strip()
            uname=str(q.get("unit") or q.get("unit_name") or q.get("unitName") or "").strip().lower()
            target=None
            if uid or uname:
                for u in units:
                    if uid in (str(u.get("id","")),str(u.get("number",""))) or (uname and uname==str(u.get("name","")).strip().lower()):
                        target=str(u.get("number")); break
                if target is None: invalid.append(qid)
            else:
                n=topic_unit(sid,q)
                if n is not None and str(n) in bynum: target=str(n)
            if target is None: unassigned+=1
            else: counts[target]+=1
            if q.get("review_flag") is True or q.get("source_verified") is False: review+=1
        if dup: errors.append(f"{sid}: duplicate question IDs: {', '.join(dup[:10])}")
        print(f"\n{sid}: total={len(qs)} mapped={sum(counts.values())} unassigned={unassigned} review_required={review}")
        for u in units: print(f"  Unit {u.get('number')} — {u.get('name')}: {counts[str(u.get('number'))]}")
        print(f"  unrecognized_explicit_unit_metadata={len(invalid)}")
        if invalid: print("  Explicit unit metadata left unassigned: "+", ".join(invalid[:25]))
        if unassigned: print("  Unassigned questions are intentionally excluded from unit tests; review/mapping pending.")
    if errors: raise SystemExit("Syllabus mapping audit failed:\n- "+"\n- ".join(errors))
    print("\nSyllabus mapping audit completed.")
if __name__=="__main__": main()
