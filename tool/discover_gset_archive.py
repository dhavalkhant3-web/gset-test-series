#!/usr/bin/env python3
"""Discover official GSET Paper-II source inventory for all subjects/sessions."""
from __future__ import annotations
import json, re, ssl, urllib.request
from pathlib import Path

BASE = "https://www.gujaratset.ac.in/assets"
OLD_PAPERS = "https://www.gujaratset.ac.in/oldpap"
ANSWER_KEYS = "https://www.gujaratset.ac.in/anskey"
SUBJECTS_FILE = Path("assets/subjects/subjects.json")
OUT_FILE = Path("assets/subjects/archive_manifest.json")

SESSIONS = [
    ("jan02","January 2002","jan02",50),("dec02","December 2002","dec02",50),
    ("dec03","December 2003","dec03",50),("jul04","July 2004","jy04",50),
    ("jul06","July 2006","jul06",50),("dec08","December 2008","dec08",50),
    ("oct10","October 2010","oct10",50),("oct11","October 2011","oct11",50),
    ("sep13","September 2013","sep13",50),("oct14","October 2014","oct14",50),
    ("sep16","September 2016","sep16",50),("aug17","August 2017","aug17",50),
    ("sep18","September 2018","sep18",100),("dec19","December 2019","dec19",100),
    ("dec21","December 2021 (January 2022)","dec21",100),("nov22","November 2022","nov22",100),
    ("nov23","November 2023","nov23",100),("dec24","December 2024","dec24",100),
    ("nov25","November 2025","nov25",100),
]
STEMS = {
    "jan02":"jan02","dec02":"dec02","dec03":"dec03","jul04":"jul04",
    "jul06":"jul06","dec08":"dec08","oct10":"oct10","oct11":"oct11",
    "sep13":"sep13","oct14":"oct14","sep16":"sep16","aug17":"aug17",
    "sep18":"sept18","dec19":"dec19","dec21":"dec21","nov22":"nov22",
    "nov23":"nov23","dec24":"dec24","nov25":"nov25",
}

def fetch(url):
    ctx=ssl._create_unverified_context()
    req=urllib.request.Request(url,headers={"User-Agent":"gset-test-series-archive-discovery/1.0"})
    with urllib.request.urlopen(req,timeout=90,context=ctx) as r:
        return r.read().decode("utf-8","ignore")

def main():
    subjects=json.loads(SUBJECTS_FILE.read_text(encoding="utf-8"))["subjects"]
    papers_html=fetch(OLD_PAPERS)
    keys_html=fetch(ANSWER_KEYS)
    paper_links=set(re.findall(r'https?://[^"\']+/assets/papers/paperII/[^"\']+\.pdf',papers_html))
    key_links=set(re.findall(r'https?://[^"\']+/assets/anskey/paperII/[^"\']+\.pdf',keys_html))
    entries=[]
    for subject in subjects:
        code=str(subject["code"]).zfill(2)
        for sid,exam,folder,expected in SESSIONS:
            filename=f"{STEMS[sid]}{code}.pdf"
            paper_url=f"{BASE}/papers/paperII/{folder}/{filename}"
            key_url=f"{BASE}/anskey/paperII/{folder}/{filename}"
            entries.append({
                "paper_id":f"{subject['id']}_{sid}","subject_id":subject["id"],
                "subject_code":code,"subject_name":subject["name_en"],"exam":exam,
                "session":sid,"paper_type":"Paper-II","expected_questions":expected,
                "question_paper_url":paper_url,"answer_key_url":key_url,
                "official_question_paper_listed":paper_url in paper_links,
                "official_answer_key_listed":key_url in key_links,
                "ready_for_batch_import":paper_url in paper_links and key_url in key_links,
            })
    ready=sum(x["ready_for_batch_import"] for x in entries)
    out={"schema_version":1,"generated_by":"tool/discover_gset_archive.py",
         "official_archive":OLD_PAPERS,"official_answer_keys":ANSWER_KEYS,
         "subject_count":len(subjects),"session_count":len(SESSIONS),
         "paper_count":len(entries),"ready_count":ready,"entries":entries}
    OUT_FILE.parent.mkdir(parents=True,exist_ok=True)
    OUT_FILE.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"GSET archive inventory: {len(subjects)} subjects x {len(SESSIONS)} sessions = {len(entries)} Paper-II entries")
    print(f"Ready for batch import: {ready}/{len(entries)}")

if __name__=="__main__":
    main()
