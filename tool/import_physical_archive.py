import json, re, subprocess, urllib.request
from pathlib import Path

PAPERS = [
    ("physical_aug17", "August 2017", "aug17", "aug1702", 50),
    ("physical_sep18", "September 2018", "sept18", "sept1802", 100),
    ("physical_dec19", "December 2019", "dec19", "dec1902", 100),
    ("physical_dec21", "December 2021 (January 2022)", "dec21", "dec2102", 100),
    ("physical_nov22", "November 2022", "nov22", "nov2202", 100),
    ("physical_nov23", "November 2023", "nov23", "nov2302", 100),
]
BASE="https://gujaratset.ac.in/assets"
OUT=Path("assets/subjects/physical_sciences/questions.json")
WORK=Path("build/physical_archive")

def run(cmd):
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def clean(s):
    return re.sub(r"\s+", " ", s.replace("\x0c", " ")).strip()

def download(url, path):
    urllib.request.urlretrieve(url, path)

def extract_text(pdf, stem):
    txt=Path(stem+".txt")
    run(["pdftotext","-layout",str(pdf),str(txt)])
    t=txt.read_text(errors="ignore")
    if len(re.findall(r"(?m)^\s*\d{1,3}[\.\)]\s+",t)) >= 20:
        return t
    imgstem=Path(stem)
    run(["pdftoppm","-f","1","-l","-1","-png","-r","180",str(pdf),str(imgstem)])
    chunks=[]
    for img in sorted(imgstem.parent.glob(imgstem.name+"-*.png")):
        out=img.with_suffix("")
        subprocess.run(["tesseract",str(img),str(out),"--psm","6"],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        chunks.append(Path(str(out)+".txt").read_text(errors="ignore"))
    return "\n".join(chunks)

def parse_key(text, expected):
    pairs=re.findall(r"(?<!\d)(\d{1,3})\s*(?:\|\|)?\s*([ABCDZ])\b",text.upper())
    d={}
    for n,a in pairs:
        n=int(n)
        if 1<=n<=expected and n not in d: d[n]=a
    return d

def question_blocks(text, expected):
    matches=list(re.finditer(r"(?m)^\s*(\d{1,3})[\.\)]\s+",text))
    chosen=[]; wanted=1
    for m in matches:
        q=int(m.group(1))
        if q==wanted:
            chosen.append(m); wanted+=1
            if wanted>expected: break
    if len(chosen)<expected:
        by={}
        for m in matches:
            q=int(m.group(1))
            if 1<=q<=expected: by[q]=m
        chosen=[by[q] for q in range(1,expected+1) if q in by]
    blocks={}
    for i,m in enumerate(chosen):
        q=int(m.group(1)); end=chosen[i+1].start() if i+1<len(chosen) else len(text)
        blocks[q]=text[m.end():end]
    return blocks

def parse_options(block):
    ms=list(re.finditer(r"(?m)(?:^|\s)\(?([ABCD])\)?[\.\:\)]\s+",block))
    if len(ms)<4:
        ms=list(re.finditer(r"(?m)^\s*\(?([ABCD])\)?\s+",block))
    return [clean(block[m.end():(ms[i+1].start() if i+1<len(ms) else len(block))]) for i,m in enumerate(ms[:4])]

def main():
    WORK.mkdir(parents=True,exist_ok=True)
    allq=json.loads(OUT.read_text(encoding="utf-8"))
    byid={q["id"]:q for q in allq}
    report=[]
    for pid,exam,folder,stem,expected in PAPERS:
        paper_url=f"{BASE}/papers/paperII/{folder}/{stem}.pdf"
        key_url=f"{BASE}/anskey/paperII/{folder}/{stem}.pdf"
        pdf=WORK/(stem+".pdf"); keypdf=WORK/(stem+"_key.pdf")
        download(paper_url,pdf); download(key_url,keypdf)
        keys=parse_key(extract_text(keypdf,str(WORK/(stem+"_key"))),expected)
        if len(keys)<expected: raise SystemExit(f"{pid}: only {len(keys)}/{expected} answer keys parsed")
        blocks=question_blocks(extract_text(pdf,str(WORK/stem)),expected)
        if len(blocks)<expected: raise SystemExit(f"{pid}: only {len(blocks)}/{expected} question blocks parsed")
        bad=0
        for qn in range(1,expected+1):
            block=blocks[qn]
            om=list(re.finditer(r"(?m)(?:^|\s)\(?([ABCD])\)?[\.\:\)]\s+",block))
            first=om[0].start() if om else len(block)
            question=clean(block[:first])
            opts=(parse_options(block)+["","","",""])[:4]
            answer=keys[qn]
            review=(any(not x for x in opts) or not question or "?" in question or any("?" in x for x in opts))
            bad += int(review)
            byid[f"{pid}_q{qn:02d}"]={
              "id":f"{pid}_q{qn:02d}","paper_id":pid,"exam":exam,
              "question_en":question,"question_gu":question,
              "options_en":opts,"options_gu":opts,"answer":answer,
              "topic":"Physical Sciences","difficulty":"Medium",
              "explanation_en":f"Official GSET final answer key: {answer}. Transcribed from the official paper; verify original notation/figures where OCR is uncertain.",
              "explanation_gu":f"Official GSET final answer key મુજબ જવાબ {answer} છે. OCR notation/figure માટે original PDF ચકાસો.",
              "review_flag":review,
              "review_note":"OCR/notation/options require source-image review." if review else "",
              "tip_en":"Verify equations, symbols and figures against the original GSET paper.",
              "tip_gu":"Equation, symbol અને figure માટે original GSET paper સાથે ચકાસણી કરો.",
              "source_verified":not review,
              "source":f"GSET official {exam} Physical Sciences Paper-II and final answer key",
              "source_url":paper_url,"answer_key_url":key_url
            }
        report.append((pid,expected,bad))
    merged=sorted(byid.values(),key=lambda x:(x.get("paper_id",""),x.get("id","")))
    OUT.write_text(json.dumps(merged,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Imported:",report)
    print("Total Physical Sciences questions:",len(merged))

if __name__=="__main__": main()
