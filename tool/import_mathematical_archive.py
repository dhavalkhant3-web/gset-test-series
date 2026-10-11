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
    "sep13":"sept13","oct14":"oct14","sep16":"sept16","aug17":"aug17",
    "sep18":"sept18","dec19":"dec19","dec21":"dec21","nov22":"nov22",
    "nov23":"nov23","dec24":"dec24","nov25":"nov25",
}
def archive_folder(session):
    return ARCHIVE_FOLDERS[session]
SESSIONS=[
("jan02","January 2002","jan0201",50),("dec02","December 2002","dec0201",50),
("dec03","December 2003","dec0301",50),("jul04","July 2004","jy0401",50),
("jul06","July 2006","jy0601",50),("dec08","December 2008","dec0801",50),
("oct10","October 2010","oct1001",50),("oct11","October 2011","oct1101",50),
("sep13","September 2013","sept1301",50),("oct14","October 2014","oct1401",50),
("sep16","September 2016","sept1601",50),("aug17","August 2017","aug1701",50),
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
    """Collapse whitespace for display-only fields."""
    return re.sub(r"\s+"," ",s.replace("\x0c"," ")).strip()

def preserve_lines(s):
    """Normalize each source line without joining adjacent MCQ/options lines."""
    lines=[]
    for line in s.replace("\x0c","\n").splitlines():
        line=re.sub(r"[ \t]+"," ",line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)

def question_stem(block):
    """Return the prompt before option A, preserving equations and line breaks."""
    m=re.search(r"(?im)^\s*(?:\(?A\)?[.) :]\s+|\(A\)\s+)",block)
    if not m:
        m=re.search(r"(?i)\s+\(A\)\s+",block)
    return clean(block[:m.start()]) if m else clean(block)
def download(url,p):
    p.parent.mkdir(parents=True,exist_ok=True)
    # Official GSET archive has used both short and "sept" folder spellings
    # for September sessions. Try known official URL variants, never guessed content.
    candidates=[url]
    if "/sep16/" in url: candidates.append(url.replace("/sep16/","/sept16/"))
    if "/sept16/" in url: candidates.append(url.replace("/sept16/","/sep16/"))
    if "/sep18/" in url: candidates.append(url.replace("/sep18/","/sept18/"))
    if "/sept18/" in url: candidates.append(url.replace("/sept18/","/sep18/"))
    if "/sept18/sep1801.pdf" in url: candidates.append(url.replace("/sep1801.pdf","/sept1801.pdf"))
    if "/sep18/sept1801.pdf" in url: candidates.append(url.replace("/sept1801.pdf","/sep1801.pdf"))
    for candidate in dict.fromkeys(candidates):
        cmd=["curl","-L","--fail","--retry","2","--retry-all-errors","--retry-delay","2",
             "--connect-timeout","30","--max-time","180","--insecure","-o",str(p),candidate]
        try:
            run(cmd)
            if p.exists() and p.stat().st_size>5000:
                print(f"[SOURCE OK] {candidate}")
                return True
        except subprocess.CalledProcessError as e:
            if p.exists(): p.unlink()
            print(f"[SOURCE RETRY] {candidate} (curl exit {e.returncode})")
    print(f"[PENDING SOURCE] all official URL variants failed for {url}")
    return False

def pages(pdf,stem,mode="layout",expected=None):
    txt=stem.with_name(stem.name+"_"+mode+".txt")
    run(["pdftotext","-"+mode,str(pdf),str(txt)])
    raw=txt.read_text(encoding="utf-8",errors="ignore")
    extracted=[(i+1,x) for i,x in enumerate(raw.split("\f")) if x.strip()]
    # Legacy GSET PDFs can be image-only scans. OCR when native extraction
    # has no plausible numbered questions, rather than silently importing zero.
    native_count=len({q for _,page in extracted for _,_,q in starts(page, expected or 100)})
    # Question-number detection alone is misleading in math PDFs: page numbers,
    # equations and selectable fragments can make a broken extraction look complete.
    # Trigger OCR based on recoverable MCQs (prompt + all four options), not just
    # the count of numbered fragments.
    native_mcq=0
    if mode == "layout":
        try:
            native_mcq=sum(1 for block in parse_blocks(extracted, expected or 100).values()
                           if len(options(block))==4)
        except NameError:
            native_mcq=0
    if mode == "layout" and native_mcq < int((expected or 100)*0.75):
        print(f"[OCR TRIGGER] {pdf.name}: numbered={native_count}, four_option_mcq={native_mcq}/{expected or 100}")
        prefix=stem.with_name(stem.name+"_ocrpage")
        run(["pdftoppm","-jpeg","-r","300","-jpegopt","quality=90",str(pdf),str(prefix)])
        images=sorted(prefix.parent.glob(prefix.name+"-*.jpg"))
        ocr=[]
        for i,img in enumerate(images,1):
            # Old math papers contain dense equations and multi-column choices.
            # Keep independent OCR candidates; parse_blocks will prefer a candidate
            # with all four choices, then the fuller source text.
            for psm in ("6","4","11"):
                p=subprocess.run(["tesseract",str(img),"stdout","--psm",psm],
                    text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                if p.stdout.strip():
                    ocr.append((i,p.stdout))
        if any(text.strip() for _,text in ocr):
            first_mcq=sum(1 for block in parse_blocks(ocr, expected or 100).values()
                          if len(options(block))==4)
            print(f"[OCR FALLBACK] {pdf.name}: {len(images)} pages x 3 modes, {len(ocr)} candidates; recoverable_mcq={first_mcq}/{expected or 100}")
            # Old scans and math-heavy layouts can lose superscripts, option labels,
            # or question numbers at 300 DPI. Run a higher-resolution recovery pass
            # only when the first pass still leaves a substantial gap. These remain
            # OCR candidates, never auto-verified; every imported item keeps review_flag.
            if first_mcq < int((expected or 100)*0.85):
                prefix_hi=stem.with_name(stem.name+"_ocr450page")
                run(["pdftoppm","-jpeg","-r","450","-jpegopt","quality=95",str(pdf),str(prefix_hi)])
                images_hi=sorted(prefix_hi.parent.glob(prefix_hi.name+"-*.jpg"))
                extra=[]
                for i,img in enumerate(images_hi,1):
                    for psm in ("6","4","11","12","13"):
                        p=subprocess.run(["tesseract",str(img),"stdout","--psm",psm],
                            text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        if p.stdout.strip():
                            extra.append((i,p.stdout))
                if extra:
                    ocr.extend(extra)
                    recovered=sum(1 for block in parse_blocks(ocr, expected or 100).values()
                                  if len(options(block))==4)
                    print(f"[OCR 450 DPI RECOVERY] {pdf.name}: {len(images_hi)} pages x 5 modes; recoverable_mcq={recovered}/{expected or 100}")
            return ocr
    return extracted
def starts(t,expected):
    # Anchor question numbers to line starts to avoid matching years, values
    # in equations, and option text as new questions.
    pat=re.compile(r"(?m)^\s*(?:Q(?:uestion)?\s*\.?\s*)?(\d{1,3})(?:\s*[.)]|\s*[:-]\s+|(?=\s+))")
    return [(m.start(),m.end(),int(m.group(1))) for m in pat.finditer(t) if 1<=int(m.group(1))<=expected]
def options(block):
    # Labels can be on separate lines or inline in older scanned papers.
    pats=[re.compile(r"(?mi)^[ \t]*\(?([ABCD])\)?[ \t]*[.:)][ \t]*"),
          re.compile(r"(?i)(?<!\w)\(([ABCD])\)[ \t]*"),
          re.compile(r"(?i)(?<!\w)([ABCD])[.)][ \t]+")]
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
            # Preserve source line boundaries: flattening here made the option
            # parser miss OCR choices and corrupted the question prompt.
            block=preserve_lines(t[b:z])
            # Prefer a candidate that retains all four options before comparing
            # text length; this matters when combining PSM 6/4/11 OCR results.
            score=(1 if len(options(block))==4 else 0,len(block))
            previous=d.get(q,"")
            previous_score=(1 if len(options(previous))==4 else 0,len(previous))
            if len(block)>8 and (q not in d or score>previous_score): d[q]=block
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
        pg_layout=pages(pdf,w/"paper","layout",expected=expected)
        pg_raw=pages(pdf,w/"paper","raw")
        blocks_layout=parse_blocks(pg_layout,expected)
        blocks_raw=parse_blocks(pg_raw,expected)
        # Merge per-question across layout, raw, and OCR extraction. Selecting
        # one whole document loses valid questions when different pages extract
        # better under different modes. Prefer four-option blocks, then fuller text.
        score=lambda block: (1 if len(options(block))==4 else 0, len(block))
        blocks={}
        for candidate in (blocks_layout, blocks_raw):
            for q,block in candidate.items():
                if q not in blocks or score(block)>score(blocks[q]):
                    blocks[q]=block
        print(pid, "extraction diagnostics:", {"layout_blocks":len(blocks_layout),"layout_mcq":sum(1 for b in blocks_layout.values() if len(options(b))==4),"raw_blocks":len(blocks_raw),"raw_mcq":sum(1 for b in blocks_raw.values() if len(options(b))==4),"merged_blocks":len(blocks),"merged_mcq":sum(1 for b in blocks.values() if len(options(b))==4)})
        keys=keymap(key,w/"key",expected)
        loaded=0
        for q in range(1,expected+1):
            b=blocks.get(q); opts=options(b or "")
            if not b or len(opts)!=4 or q not in keys:
                continue
            # Conservative split: retain only questions whose four options and key
            # are recoverable. Ambiguous/visual questions remain for review.
            first=question_stem(b)
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
