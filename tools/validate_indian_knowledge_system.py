#!/usr/bin/env python3
"""Validate GSET Indian Knowledge System (subject 29) counts, official keys and audit parity.

The answer strings are transcribed from the supplied official GSET Final Answer Key PDFs.
Question wording and options were OCR-imported from supplied official scanned papers and remain flagged
until a human checks them against the original page images.
"""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
APP_PATH=ROOT/"assets/subjects/indian_knowledge_system/questions.json"
AUDIT_PATH=ROOT/"assets/json/indian_knowledge_system.json"
PAPERS_PATH=ROOT/"assets/subjects/indian_knowledge_system/papers.json"
SUBJECTS_PATH=ROOT/"assets/subjects/subjects.json"
EXPECTED_KEYS = {
    'November 2023': 'DCAABDDCACBBDDACCADBADACAABCADBCDCDABDADDBABACCDDCBDCDDBACCDADABBACDABADCAABCAABBACDACDACCBDBADAADAD',
    'December 2024': 'BAAAACDADAADDDBCBBDABCBDCDDCBBCDCABBACDBCDCADBABCBCADACBDAABADCBCACDABCABABACDCDBACDACBACCADCCBCBDAD',
    'November 2025': 'BBBBBDABBACDBACDABCBCABDACDACBBABABCCABDACAABDCADCBAAABBBADBBABAADCADCCBADDACACAABACBAACADBAACABABBA',
}
SESSION_META={"November 2023":("NOV23","indian_knowledge_system_nov23"),"December 2024":("DEC24","indian_knowledge_system_dec24"),"November 2025":("NOV25","indian_knowledge_system_nov25")}
def fail(msg):
 print(f"FAIL: {msg}",file=sys.stderr); raise SystemExit(1)
def load(path):
 try:return json.loads(path.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as e: fail(f"Cannot read {path.relative_to(ROOT)}: {e}")
def main():
 app=load(APP_PATH); auddoc=load(AUDIT_PATH); papersdoc=load(PAPERS_PATH); subjectsdoc=load(SUBJECTS_PATH); audit=auddoc.get("questions")
 if not isinstance(app,list) or not isinstance(audit,list):fail("App bank must be a list and audit must contain a questions list")
 if len(app)!=300 or len(audit)!=300:fail(f"Expected 300 app/audit records, found {len(app)}/{len(audit)}")
 def index(records,label):
  d={}
  for x in records:
   xid=x.get("id")
   if not xid:fail(f"{label} record missing id")
   if xid in d:fail(f"{label} duplicate id {xid}")
   d[xid]=x
  return d
 amap=index(app,"app"); bmap=index(audit,"audit")
 if set(amap)!=set(bmap):fail("App/audit ID sets differ")
 counts=Counter(); flags=Counter()
 for x in app:
  s=x.get("exam_session"); n=x.get("question_no")
  if s not in SESSION_META:fail(f"Unknown session {s!r} on {x.get('id')}")
  code,pid=SESSION_META[s]
  if not isinstance(n,int) or not 1<=n<=100:fail(f"Invalid question_no on {x.get('id')}")
  if x.get("id")!=f"GSET_29_{code}_{n:03d}":fail(f"Unexpected ID {x.get('id')}")
  if x.get("paper_id")!=pid or x.get("paperId")!=pid:fail(f"Wrong paper id on {x.get('id')}")
  if not isinstance(x.get("question_en"),str) or not x["question_en"].strip():fail(f"Missing question text on {x.get('id')}")
  opts=x.get("options_en")
  if not isinstance(opts,list) or len(opts)!=4 or not all(isinstance(z,str) and z.strip() for z in opts):fail(f"Need four nonempty options on {x.get('id')}")
  official=EXPECTED_KEYS[s][n-1]
  if x.get("answer")!=official or x.get("official_answer")!=official:fail(f"Key mismatch on {x.get('id')}: expected {official}")
  # Until individual OCR transcription is visually verified, the review flag and source status must remain conservative.
  if x.get("review_flag") is not True or x.get("source_verified") is not False:fail(f"OCR item not marked for visual review: {x.get('id')}")
  if not isinstance(x.get("review_note"),str) or not x["review_note"].strip():fail(f"Missing review note on {x.get('id')}")
  a=bmap[x["id"]]
  if a.get("exam_session")!=s or a.get("question_number")!=n:fail(f"Audit session/number mismatch on {x['id']}")
  if a.get("question_text")!=x["question_en"]:fail(f"Audit question text mismatch on {x['id']}")
  if a.get("options")!=dict(zip("ABCD",opts)):fail(f"Audit options mismatch on {x['id']}")
  if a.get("correct_answer")!=official:fail(f"Audit answer key mismatch on {x['id']}")
  if a.get("review_flag") is not True or a.get("source_verified") is not False:fail(f"Audit source-review status mismatch on {x['id']}")
  counts[s]+=1; flags[s]+=1
 for s in SESSION_META:
  nums=sorted(x["question_no"] for x in app if x["exam_session"]==s)
  if counts[s]!=100 or nums!=list(range(1,101)):fail(f"{s} must contain Q1-Q100 exactly once")
 papers=papersdoc.get("papers",[])
 if len(papers)!=3:fail("papers.json must include exactly three sessions")
 for p in papers:
  if p.get("exam") not in SESSION_META or p.get("questions_loaded")!=100 or p.get("questions_count")!=100:fail(f"Paper metadata count error: {p.get('exam')}")
  if p.get("source_verified") is not False or "review" not in p.get("status","").lower():fail(f"Paper must stay unverified until OCR review: {p.get('exam')}")
 subject=next((x for x in subjectsdoc.get("subjects",[]) if x.get("code")=="29"),None)
 if not subject:fail("Subject 29 missing from subjects.json")
 if subject.get("id")!="indian_knowledge_system" or subject.get("questions_loaded")!=300 or subject.get("papers_loaded")!=3:fail("Subject 29 metadata count mismatch")
 if subject.get("source_verified") is not False:fail("Subject 29 must remain source_verified=false until manual review")
 print("PASS: Indian Knowledge System (subject 29): 300 questions in app and audit banks")
 print("PASS: every session has Q1-Q100 exactly once")
 print("PASS: 300/300 stored answers match the supplied official Final Answer Key sequences")
 print("PASS: app/audit wording and option parity; no duplicate IDs")
 print("REVIEW REQUIRED: all 300 OCR-derived question records remain flagged for visual source verification")
if __name__=="__main__":main()