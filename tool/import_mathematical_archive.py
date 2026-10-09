#!/usr/bin/env python3
"""Source-preserving Mathematical Sciences Paper-II archive importer.

Official GSET PDFs/keys only. OCR is evidence, not truth: uncertain blocks are
stored with review_flag/source_verified=false rather than fabricated.
"""
import json,re,subprocess
from pathlib import Path

SUBJECT="mathematical_sciences"
BASE="https://gujaratset.ac.in/assets"

ARCHIVE_FOLDERS = {
    "jan02":"jan02","dec02":"dec02","dec03":"dec03","jul04":"jy04",
    "jul06":"jy06","dec08":"dec08","oct10":"oct10","oct11":"oct11",
    "sep13":"sep13","oct14":"oct14","sep16":"sep16","aug17":"aug17",
    "sep18":"sep18","dec19":"dec19","dec21":"dec21","nov22":"nov22",
    "nov23":"nov23","dec24":"dec24","nov25":"nov25",
}
def archive_folder(session):
    return ARCHIVE_FOLDERS[session]
SESSIONS=[
("jan02","January 2002","jan0201",50),("dec02","December 2002","dec0201",50),
("dec03","December 2003","dec0301",50),("jul04","July 2004","jy0401",50),
("jul06","July 2006","jy0601",50),("dec08","December 2008","dec0801",50),
("oct10","October 2010","oct1001",50),("oct11","October 2011","oct1101",50),
("sep13","September 2013","sep1301",50),("oct14","October 2014","oct1401",50),
("sep16","September 2016","sep1601",50),("aug17","August 2017","aug1701",50),
("sep18","September 2018","sep1801",100),("dec19","December 2019","dec1901",100),
("dec21","December 2021 (January 2022)","dec2101",100),("nov22","November 2022","nov2201",100),
("nov23","November 2023","nov2301",100),("dec24","December 2024","dec2401",100),
("nov25","November 2025","nov2501",100)]
OUT=Path("assets/subjects/mathematical_sciences/questions.json")
META=Path("assets/subjects/mathematical_sciences/papers.json")
WORK=Path("build/mathematical_archive")

def run(c):
    return subprocess.run(c,check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def clean(s):
    return re.sub(r"\s+"," ",s.replace("\x0c"," ")).strip()
def download(url,p):
    p.parent.mkdir(parents=True,exist_ok=True)
    cmd=["curl","-L","--fail","--retry","6","--retry-all-errors","--retry-delay","5",
         "--connect-timeout","60","--max-time","240","--insecure","-o",str(p),url]
    try:
        run(cmd)
        return True
    except subprocess.CalledProcessError as e:
        if p.exists() and p.stat().st_size:
            p.unlink()
        print(f"[PENDING SOURCE] download failed: {url} (curl exit {e.returncode})")
        return False

def pages(pdf,stem,mode="layout"):
    txt=stem.with_name(stem.name+"_"+mode+".txt")
    run(["pdftotext","-"+mode,str(pdf),str(txt)])
    raw=txt.read_text(encoding="utf-8",errors="ignore")
    extracted=[(i+1,x) for i,x in enumerate(raw.split("\\f")) if x.strip()]
    # Legacy GSET PDFs can be image-only scans. OCR when native extraction
    # has no plausible numbered questions, rather than silently importing zero.
    if mode == "layout" and not any(starts(page,100) for _,page in extracted):
        prefix=stem.with_name(stem.name+"_ocrpage")
        run(["pdftoppm","-jpeg","-r","300","-jpegopt","quality=90",str(pdf),str(prefix)])
        images=sorted(prefix.parent.glob(prefix.name+"-*.jpg"))
        ocr=[]
        for i,img in enumerate(images,1):
            p=subprocess.run(["tesseract",str(img),"stdout","--psm","6"],
                text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            ocr.append((i,p.stdout))
        if any(text.strip() for _,text in ocr):
            print(f"[OCR FALLBACK] {pdf.name}: {len(ocr)} pages")
            return ocr
    return extracted
def starts(t,expected):
    # Anchor question numbers to line starts to avoid matching years, values
    # in equations, and option text as new questions.
    pat=re.compile(r"(?m)^\s*(?:Q(?:uestion)?\s*\.?\s*)?(\d{1,3})(?:\s*[.)]|\s*[:-]\s+|(?=\s+))")
    return [(m.start(),m.end(),int(m.group(1))) for m in pat.finditer(t) if 1<=int(m.group(1))<=expected]
def options(block):
    pats=[re.compile(r"(?mi)(?:^|\n)\s*\(?([ABCD])\)?\s*[\.:\)]\s*"),
          re.compile(r"(?mi)\(([ABCD])\)\s+")]
    for pat in pats:
        ms=list(pat.finditer(block))
        for i in range(max(0,len(ms)-3)):
            if [m.group(1).upper() for m in ms[i:i+4]]==list("ABCD"):
                m=ms[i:i+4]; out=[]
                for j,a in enumerate(m):
                    out.append(clean(block[a.end():(m[j+1].start() if j<3 else len(block))]))
                if all(out): return out
    return []
def parse_blocks(pg,expected):
    d={}
    for _,t in pg:
        st=starts(t,expected)
        # Keep only plausible question-number sequences. This avoids treating
        # years, marks and page numbers as question starts in legacy PDFs.
        if len(st) > expected * 2:
            st=[x for x in st if x[2] <= expected]
        for i,(a,b,q) in enumerate(st):
            z=st[i+1][0] if i+1<len(st) else len(t)
            block=clean(t[b:z])
            if len(block)>8 and (q not in d or len(block)>len(d[q])): d[q]=block
    return d
def keymap(pdf,stem,expected):
    pg=pages(pdf,stem); text="\n".join(x for _,x in pg).upper()
    d={}
    for m in re.finditer(r"(?<!\d)(\d{1,3})\s*[\.)\-:]?\s*([ABCDZ])\b",text):
        q=int(m.group(1))
        if 1<=q<=expected:d.setdefault(q,m.group(2))
    return d
def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--paper"); args=ap.parse_args()
    targets=[x for x in SESSIONS if not args.paper or "mathematical_sciences_"+x[0]==args.paper]
    OUT.parent.mkdir(parents=True,exist_ok=True); META.parent.mkdir(parents=True,exist_ok=True)
    existing=json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else []
    old={x["id"] for x in existing}
    meta=json.loads(META.read_text(encoding="utf-8")) if META.exists() else {"schema_version":1,"subject_id":SUBJECT,"subject_code":"01","papers":[]}
    bymeta={x["paper_id"]:x for x in meta["papers"]}
    for sess,exam,stem,expected in targets:
        pid=f"{SUBJECT}_{sess}"; w=WORK/pid; w.mkdir(parents=True,exist_ok=True)
        pdf=w/f"{stem}.pdf"; key=w/f"{stem}_key.pdf"
        folder=archive_folder(sess)
        paper_ok=download(f"{BASE}/papers/paperII/{folder}/{stem}.pdf",pdf)
        key_ok=download(f"{BASE}/anskey/paperII/{folder}/{stem}.pdf",key)
        if not paper_ok or not key_ok:
            bymeta[pid]={"paper_id":pid,"exam":exam,"subject_code":"01","question_count":expected,
              "marks":200,
              "question_paper_url":f"{BASE}/papers/paperII/{folder}/{stem}.pdf",
              "answer_key_url":f"{BASE}/anskey/paperII/{folder}/{stem}.pdf",
              "questions_loaded":sum(1 for x in existing if x.get("paper_id")==pid),
              "questions_count":sum(1 for x in existing if x.get("paper_id")==pid),
              "answer_key_verified":False,"source":"GSET official uploaded question paper + final answer key",
              "source_verified":False,"question_source_verified":False,
              "status":"pending_source"}
            print(pid, "PENDING SOURCE")
            continue
        pg_layout=pages(pdf,w/"paper","layout")
        pg_raw=pages(pdf,w/"paper","raw")
        blocks_layout=parse_blocks(pg_layout,expected)
        blocks_raw=parse_blocks(pg_raw,expected)
        # Choose the extraction layout with more complete four-option MCQs.
        score=lambda d: sum(1 for block in d.values() if len(options(block))==4)
        blocks=blocks_raw if score(blocks_raw)>score(blocks_layout) else blocks_layout
        print(pid, "extraction diagnostics:", {"layout_blocks":len(blocks_layout),"layout_mcq":score(blocks_layout),"raw_blocks":len(blocks_raw),"raw_mcq":score(blocks_raw)})
        keys=keymap(key,w/"key",expected)
        loaded=0
        for q in range(1,expected+1):
            b=blocks.get(q); opts=options(b or "")
            if not b or len(opts)!=4 or q not in keys:
                continue
            # Conservative split: retain only questions whose four options and key
            # are recoverable. Ambiguous/visual questions remain for review.
            first=re.split(r"(?m)(?:\s{2,}|\n)",b)[0].strip()
            if len(first)<8: continue
            rid=f"{pid}_q{q}"
            if rid in old: continue
            existing.append({"id":rid,"paper_id":pid,"exam":exam,
              "question_en":first,"question_gu":first,"options_en":opts,"options_gu":opts,
              "answer":keys[q],"topic":"Mathematical Sciences","difficulty":"Medium",
              "explanation_en":"Official GSET final answer key is authoritative.",
              "explanation_gu":"Official GSET final answer key is authoritative.",
              "review_flag":True,"review_note":"Imported from official PDF/key; verify mathematical notation against source page before clearing review_flag.",
              "tip_en":"Official final answer key is authoritative.","tip_gu":"Official final answer key authoritative છે.",
              "source_verified":False})
            old.add(rid); loaded+=1
        bymeta[pid]={"paper_id":pid,"exam":exam,"subject_code":"01","question_count":expected,
          "marks":200,"question_paper_url":f"{BASE}/papers/paperII/{archive_folder(sess)}/{stem}.pdf",
          "answer_key_url":f"{BASE}/anskey/paperII/{archive_folder(sess)}/{stem}.pdf",
          "questions_loaded":sum(1 for x in existing if x.get("paper_id")==pid),
          "questions_count":sum(1 for x in existing if x.get("paper_id")==pid),
          "answer_key_verified":len(keys)==expected,
          "source":"GSET official uploaded question paper + final answer key",
          "source_verified":False,"question_source_verified":False,
          "status":"verified_complete_with_review" if sum(1 for x in existing if x.get("paper_id")==pid)==expected else "partial_pending_source"}
        print(pid, "parsed",loaded,"new; total",bymeta[pid]["questions_loaded"],"/",expected)
    meta["papers"]=[bymeta[f"{SUBJECT}_{s[0]}"] for s in SESSIONS if f"{SUBJECT}_{s[0]}" in bymeta]
    json.dump(existing,OUT.open("w",encoding="utf-8"),ensure_ascii=False,indent=2)
    json.dump(meta,META.open("w",encoding="utf-8"),ensure_ascii=False,indent=2)
if __name__=="__main__": main()

# Official GSET archive mapping is resolved from the official old-paper links.
