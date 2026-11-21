#!/usr/bin/env python3
"""Strict canonical-data validation for GSET Gujarati Paper-II (Code 06)."""
import json, re, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUB=ROOT/"assets/subjects/gujarati"
VALID={"A","B","C","D"}
ID_RE=re.compile(r"^GSET-GUJ06-[A-Z0-9]+-Q\d{3}$")
def fail(message):
 print("FAIL: "+message,file=sys.stderr); raise SystemExit(1)
def load(path):
 try: return json.loads(path.read_text(encoding="utf-8"))
 except Exception as exc: fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")
def main():
 active=load(SUB/"questions.json"); review=load(SUB/"questions_review_pending.json")
 doc=load(SUB/"papers.json"); audit=load(SUB/"source_audit.json")
 cfg=load(ROOT/"assets/subjects/syllabus_units.json")
 if not isinstance(active,list) or not isinstance(review,list): fail("question bank roots must be JSON lists")
 papers=doc.get("papers")
 if not isinstance(papers,list) or not papers: fail("papers.json has no papers list")
 scfg=cfg.get("subjects",{}).get("gujarati",{})
 if not scfg.get("official_pdf","").startswith(("https://gujaratset.ac.in/assets/syllabus/","https://www.gujaratset.ac.in/assets/syllabus/")): fail("official Gujarati syllabus URL missing")
 units={str(u.get("number")):u for u in scfg.get("units",[])}
 if not units: fail("Gujarati syllabus units missing")
 paper_ids={p.get("paper_id") for p in papers}; seen={}; counts=Counter(); errors=[]
 for kind,bank in (("active",active),("review",review)):
  for q in bank:
   qid=str(q.get("id","")); pid=q.get("paper_id")
   if not ID_RE.fullmatch(qid): errors.append(f"{kind}: invalid ID {qid!r}")
   if qid in seen: errors.append(f"duplicate ID {qid} in {seen[qid]} and {kind}")
   seen[qid]=kind; counts[(pid,kind)]+=1
   if pid not in paper_ids: errors.append(f"{qid}: unknown paper_id {pid!r}")
   if q.get("paperId")!=pid: errors.append(f"{qid}: paperId mismatch")
   if not isinstance(q.get("question_no"),int) or not 1<=q["question_no"]<=100: errors.append(f"{qid}: invalid question_no")
   opts=q.get("options_gu")
   if not isinstance(opts,list) or len(opts)!=4 or any(not isinstance(v,str) or not v.strip() for v in opts): errors.append(f"{qid}: needs four non-empty Gujarati options")
   if not isinstance(q.get("question_gu"),str) or not q["question_gu"].strip(): errors.append(f"{qid}: missing Gujarati question")
   if not q.get("source_question_paper") or not q.get("answer_source"): errors.append(f"{qid}: missing source reference")
   n=str(q.get("unit_number","")); unit=units.get(n)
   if not unit or q.get("unit_id")!=unit.get("id") or q.get("syllabus_unit")!=f"Unit {n}": errors.append(f"{qid}: syllabus unit fields invalid")
   if not q.get("syllabus_mapping_note") or not q.get("syllabus_mapping_status"): errors.append(f"{qid}: syllabus mapping evidence/status missing")
   if kind=="active":
    if q.get("review_flag") is not False: errors.append(f"{qid}: active record must not be review-flagged")
    if q.get("source_verified") is not True: errors.append(f"{qid}: active record not source-verified")
    if q.get("answer_key_verified") is not True: errors.append(f"{qid}: active record lacks final-key verification")
    if q.get("answer") not in VALID: errors.append(f"{qid}: active answer is not A/B/C/D")
    if q.get("official_answer")!=q.get("answer"): errors.append(f"{qid}: active answer differs from official answer")
   elif q.get("review_flag") is not True: errors.append(f"{qid}: review-only record must be flagged")
 if errors: fail("\n- "+"\n- ".join(errors))
 if len(seen)!=len(active)+len(review): fail("active/review IDs overlap or duplicate")
 if len(paper_ids)!=len(papers): fail("duplicate paper_id in papers.json")
 for p in papers:
  pid=p["paper_id"]; ac=counts[(pid,"active")]; rc=counts[(pid,"review")]
  if p.get("question_count")!=ac+rc: fail(f"{pid}: question_count mismatch")
  if p.get("questions_loaded")!=ac: fail(f"{pid}: questions_loaded mismatch")
  if p.get("review_flags_remaining_count")!=rc: fail(f"{pid}: review count mismatch")
 cp=audit.get("live_review_queue_checkpoint",{})
 expected={"active_questions":len(active),"pending_review":len(review),"unique_pending_ids":len(review),
 "source_verified_total":sum(q.get("source_verified") is True for q in active+review),
 "answer_key_verified_total":sum(q.get("answer_key_verified") is True for q in active+review)}
 for k,v in expected.items():
  if cp.get(k)!=v: fail(f"audit checkpoint {k}={cp.get(k)!r}; expected {v}")
 print(f"PASS: Gujarati Code 06 — {len(active)} active, {len(review)} review-only, {len(seen)} unique.")
 print("PASS: schema, source/final-key gate, paper metadata, syllabus references and audit counters.")
 print("NOTE: review-only records are not promoted by this validator.")
if __name__=="__main__": main()
