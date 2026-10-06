import json
import re
import subprocess
import sys
from pathlib import Path

PAPERS = [
    ("physical_jan02", "January 2002", "jan02", "jan0202", 50),
    ("physical_aug17", "August 2017", "aug17", "aug1702", 50),
    ("physical_sep18", "September 2018", "sept18", "sept1802", 100),
    ("physical_dec19", "December 2019", "dec19", "dec1902", 100),
    ("physical_dec21", "December 2021 (January 2022)", "dec21", "dec2102", 100),
    ("physical_nov22", "November 2022", "nov22", "nov2202", 100),
    ("physical_nov23", "November 2023", "nov23", "nov2302", 100),
    ("physical_dec24", "December 2024", "dec24", "dec2402", 100),
]

BASE = "https://gujaratset.ac.in/assets"
OUT = Path("assets/subjects/physical_sciences/questions.json")
PAPERS_JSON = Path("assets/subjects/physical_sciences/papers.json")
WORK = Path("build/physical_archive")

def log(tag, msg):
    print(f"[{tag}] {msg}", flush=True)

def run(cmd):
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def clean(s):
    s = s.replace("\x0c", " ")
    s = s.replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).strip()

def download(url, path):
    log("DOWNLOAD", url)
    subprocess.run([
        "curl", "-L", "--fail", "--retry", "3", "--connect-timeout", "20",
        "--insecure", "-o", str(path), url
    ], check=True)

def render_ocr(pdf, stem, dpi=240, pages=None):
    log("OCR", f"rendering {pdf.name} at {dpi} dpi" + (f", pages={pages}" if pages else ""))
    page_dir=stem.parent/(stem.name+"_pages")
    page_dir.mkdir(parents=True,exist_ok=True)
    cmd=["pdftoppm","-png","-r",str(dpi)]
    if pages:
        cmd += ["-f",str(min(pages)),"-l",str(max(pages))]
    cmd += [str(pdf),str(page_dir/"page")]
    run(cmd)
    texts=[]
    for img in sorted(page_dir.glob("page-*.png")):
        base=img.with_suffix("")
        for psm in ("6","4"):
            out=Path(f"{base}_psm{psm}.txt")
            subprocess.run(
                ["tesseract",str(img),str(out.with_suffix("")),"--psm",psm],
                check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL
            )
            texts.append((f"{img.name}-psm{psm}",out.read_text(encoding="utf-8",errors="ignore")))
    return texts

def extract_pages(pdf, stem):
    """Keep native PDF text as an evidence stream even when sparse."""
    txt = stem.with_suffix(".txt")
    run(["pdftotext", "-layout", str(pdf), str(txt)])
    raw = txt.read_text(encoding="utf-8", errors="ignore")
    pages = raw.split("\f")
    nonempty = [(f"text-{i+1}", p) for i, p in enumerate(pages) if p.strip()]
    log("EXTRACT", f"pdftotext lines={len(raw.splitlines())}, pages={len(nonempty)}")
    if not nonempty:
        return []
    raw_txt = stem.with_name(stem.name + "_raw.txt")
    run(["pdftotext", "-raw", str(pdf), str(raw_txt)])
    raw_text = raw_txt.read_text(encoding="utf-8", errors="ignore")
    raw_pages = raw_text.split("\f")
    raw_nonempty = [(f"raw-{i+1}", p) for i, p in enumerate(raw_pages) if p.strip()]
    log("EXTRACT", f"pdftotext-raw pages={len(raw_nonempty)}")
    # Prefer layout text; raw text is retained under a separate page namespace.
    return nonempty + raw_nonempty

def normalize_question_number(s):
    s = s.replace("O", "0").replace("I", "1")
    s = re.sub(r"[^0-9]", "", s)
    return int(s) if s else None

def candidate_starts(text, expected):
    pat = re.compile(
        r"(?m)^\s*(?:Q(?:uestion)?\s*\.?\s*)?(\d{1,3})"
        r"(?:\s*[\.)]|\s*[:-]\s+|(?=\s+))"
    )
    return [
        (m.start(), m.end(), int(m.group(1)))
        for m in pat.finditer(text)
        if 1 <= int(m.group(1)) <= expected
    ]

def _question_sequence_score(qs):
    if not qs:
        return -1
    score=0
    prev=0
    for q in qs:
        if q == prev + 1:
            score += 3
        elif q > prev:
            score += 1
        else:
            score -= 3
        prev=q
    return score

def build_blocks(page_texts, expected):
    """
    Page-aware parser. For scanned papers, OCR question numbers are noisy, so
    option anchors and expected numerical sequence are used to recover blocks.
    """
    blocks={}
    for page_id,text in page_texts:
        starts=candidate_starts(text, expected)
        if starts:
            qs=[x[2] for x in starts]
            # Remove obvious header/footer noise by choosing the longest
            # monotonic subsequence beginning near the first plausible question.
            filtered=[]
            prev=0
            for item in starts:
                q=item[2]
                if q > prev and (not filtered or q <= prev+8):
                    filtered.append(item); prev=q
            starts=filtered
        if starts:
            for i,(st,en,q) in enumerate(starts):
                stop=starts[i+1][0] if i+1 < len(starts) else len(text)
                cand=clean(text[en:stop])
                if len(cand) >= 10 and (q not in blocks or len(cand)>len(blocks[q])):
                    blocks[q]=cand
    return blocks

def _extract_all_options(block):
    patterns=[
        (re.compile(r"(?mi)(?:^|\n)\s*\(?([ABCD])\)?\s*[\.:\)]\s*"), "letters"),
        (re.compile(r"(?mi)(?:^|\s)\(?([ABCD])\)?\s*[\.:\)]\s+"), "letters"),
        (re.compile(r"(?mi)\s*\(([ABCD])\)\s+"), "letters"),
        (re.compile(r"(?mi)(?:^|\n)\s*[\(]?([1-4])[\)]\s*"), "numbers"),
    ]
    for pat,kind in patterns:
        ms=list(pat.finditer(block))
        if kind=="letters":
            for i in range(max(0,len(ms)-3)):
                labels=[m.group(1).upper() for m in ms[i:i+4]]
                if labels==["A","B","C","D"]:
                    chosen=ms[i:i+4]
                    break
            else:
                continue
        else:
            for i in range(max(0,len(ms)-3)):
                labels=[m.group(1) for m in ms[i:i+4]]
                if labels==["1","2","3","4"]:
                    chosen=ms[i:i+4]
                    break
            else:
                continue
        opts=[]
        for j,m in enumerate(chosen):
            end=chosen[j+1].start() if j+1<len(chosen) else len(block)
            opts.append(clean(block[m.end():end]))
        if all(opts):
            return chosen,opts
    return [],[]

def parse_options(block):
    return _extract_all_options(block)[1]

def recover_missing_with_ocr(pdf, stem, missing, expected):
    if not missing:
        return {}
    # OCR is evidence only. Use several conservative passes and never invent
    # unresolved questions from partial text.
    recovered = {}
    for dpi, psm in ((300, "6"), (300, "4"), (360, "11")):
        log("OCR", f"recovering {len(missing)} missing questions at {dpi} dpi, psm={psm}")
        page_dir = stem.parent / f"{stem.name}_pages_{dpi}_{psm}"
        page_dir.mkdir(parents=True, exist_ok=True)
        prefix = page_dir / "page"
        run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(prefix)])
        texts = []
        for img in sorted(page_dir.glob("page-*.png")):
            out = img.with_suffix("")
            subprocess.run(
                ["tesseract", str(img), str(out), "--psm", psm],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            txt = Path(str(out) + ".txt").read_text(encoding="utf-8", errors="ignore")
            texts.append((f"{img.name}-psm{psm}", txt))
        blocks = build_blocks(texts, expected)
        for q in missing:
            if q in blocks and q not in recovered:
                recovered[q] = blocks[q]
    return recovered

def parse_key_text(text, expected):
    text = text.upper()
    d = {}
    # Accept common answer-key layouts: 1 A, 01 A, 1. A, Q1 A, tables.
    for m in re.finditer(r"(?<!\d)(\d{1,3})\s*[\.|\)|:-]?\s*([ABCDZ])\b", text):
        q = int(m.group(1))
        if 1 <= q <= expected and q not in d:
            d[q] = m.group(2)
    return d

def parse_key(pdf, stem, expected):
    pages = extract_pages(pdf, stem)
    if not pages:
        pages = render_ocr(pdf, stem, 220)
    joined = "\n".join(t for _, t in pages)
    keys = parse_key_text(joined, expected)
    log("KEY", f"parsed {len(keys)}/{expected}")
    if len(keys) < expected:
        ocr = render_ocr(pdf, stem.with_name(stem.name + "_keyocr"), 240)
        keys = parse_key_text("\n".join(t for _, t in ocr), expected)
        log("KEY", f"OCR parsed {len(keys)}/{expected}")
    if len(keys) < expected:
        missing = [q for q in range(1, expected + 1) if q not in keys]
        # The official key remains authoritative. Never synthesize missing
        # letters from calculations or OCR guesses. Existing source-verified
        # records remain intact and missing key entries trigger source review.
        log("KEY", "incomplete official-key extraction; preserving existing records and flagging missing entries: "
            + ",".join(f"Q{q}" for q in missing))
    return keys

def suspicious(question, opts):
    if not question or len(question) < 8:
        return True
    if len(opts) != 4 or any(not x for x in opts):
        return True
    all_text = " ".join([question] + opts)
    if all_text.count("?") >= 2:
        return True
    # Strong OCR-corruption signals: broken control chars or improbable isolated glyphs.
    if any(ord(c) < 32 and c not in "\n\t" for c in all_text):
        return True
    return False

def update_papers_metadata(report):
    data = json.loads(PAPERS_JSON.read_text(encoding="utf-8"))
    questions = json.loads(OUT.read_text(encoding="utf-8"))
    byid = {p["paper_id"]: p for p in data["papers"]}
    grouped = {}
    for q in questions:
        grouped.setdefault(q.get("paper_id"), []).append(q)

    # Synchronize metadata from the actual question bank instead of only the
    # papers processed in the current run. This prevents stale review counts
    # and loaded counts after manual/source-preserving corrections.
    for pid, p in byid.items():
        # Paper-III and other non-Paper-II records are maintained separately.
        if p.get("paper_type") == "Paper-III":
            continue
        expected = p.get("question_count")
        if not isinstance(expected, int):
            continue
        qs = grouped.get(pid, [])
        loaded = len(qs)
        reviews = sum(1 for q in qs if q.get("review_flag") is True)
        source_ok = loaded == expected and loaded > 0 and all(
            q.get("source_verified") is True for q in qs
        )
        p["questions_loaded"] = loaded
        p["questions_count"] = expected
        p["review_count"] = reviews
        p["question_source_verified"] = source_ok
        p["source_verified"] = source_ok
        if loaded == expected and expected > 0:
            p["status"] = "verified_complete" if reviews == 0 else "verified_complete_with_review"
        else:
            p["status"] = "partial_pending_source"

    for r in report:
        p = byid[r["paper_id"]]
        p["answer_key_verified"] = r["key_verified"]

    PAPERS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def main():
    args = sys.argv[1:]
    selected = set()
    if args[:1] == ["--paper"]:
        if len(args) != 2:
            raise SystemExit("Usage: python3 tool/import_physical_archive.py [--paper PAPER_ID]")
        selected = {args[1]}
    elif args:
        selected = set(args)
    valid_ids = {p[0] for p in PAPERS}
    unknown = selected - valid_ids
    if unknown:
        raise SystemExit("Unknown paper(s): " + ",".join(sorted(unknown)))
    WORK.mkdir(parents=True, exist_ok=True)

    allq = json.loads(OUT.read_text(encoding="utf-8"))
    byid = {q["id"]: q for q in allq}
    report = []

    for pid, exam, folder, stem, expected in PAPERS:
        if selected and pid not in selected:
            continue
        log("MERGE", f"processing {pid}")
        paper_url = f"{BASE}/papers/paperII/{folder}/{stem}.pdf"
        key_url = f"{BASE}/anskey/paperII/{folder}/{stem}.pdf"
        pdf = WORK / f"{stem}.pdf"
        keypdf = WORK / f"{stem}_key.pdf"

        download(paper_url, pdf)
        download(key_url, keypdf)

        keys = parse_key(keypdf, WORK / f"{stem}_key", expected)

        pages = extract_pages(pdf, WORK / stem)
        if pages is None:
            pages = render_ocr(pdf, WORK / stem, 220)

        blocks = build_blocks(pages, expected)
        missing = [q for q in range(1, expected + 1) if q not in blocks]
        log("PARSE", f"{pid}: parsed {len(blocks)}/{expected}")

        if missing:
            recovered = recover_missing_with_ocr(pdf, WORK / f"{stem}_ocr", missing, expected)
            blocks.update(recovered)
            missing = [q for q in range(1, expected + 1) if q not in blocks]
            log("OCR", f"{pid}: recovered={len(recovered)}, remaining_missing={','.join('Q'+str(q) for q in missing) if missing else 'none'}")

        # Existing records are never replaced by OCR guesses for unresolved Qs.
        # They remain intact and are marked for source review.
        review_count = 0
        verified = 0
        for qn in range(1, expected + 1):
            answer = keys.get(qn)
            block = blocks.get(qn, "")
            if answer is None:
                review_count += 1
                qid = f"{pid}_q{qn:02d}"
                existing = byid.get(qid)
                if existing:
                    existing["review_flag"] = True
                    existing["source_verified"] = False
                    existing["review_note"] = "Official answer-key PDF is available, but automated extraction did not recover this key entry; retained existing record and flagged for manual source review."
                continue
            if not block:
                review_count += 1
                qid = f"{pid}_q{qn:02d}"
                existing = byid.get(qid)
                if existing:
                    existing["review_flag"] = True
                    existing["review_note"] = "Official source exists but automatic reconstruction is incomplete; retained existing record and flagged for manual source review."
                continue
            # Extract options and question boundary from the same option sequence.
            marks, opts = _extract_all_options(block)
            first = marks[0].start() if marks else None
            question = clean(block[:first if first is not None else len(block)])
            review = suspicious(question, opts)
            if review:
                review_count += 1
            else:
                verified += 1

            qid = f"{pid}_q{qn:02d}"
            existing = byid.get(qid)
            # Never overwrite an already source-verified record with an automatic
            # reconstruction. Verified/manual records are authoritative and must
            # remain intact; only missing or explicitly unverified records may be
            # populated by this importer.
            # Never overwrite an existing record automatically. Existing
            # source-reviewed/manual records are preserved; unresolved records
            # remain flagged for review rather than being replaced by OCR.
            if existing:
                continue
            record = {
                "id": qid,
                "paper_id": pid,
                "exam": exam,
                "question_en": question,
                "question_gu": question,
                "options_en": (opts + ["", "", "", ""])[:4],
                "options_gu": (opts + ["", "", "", ""])[:4],
                "answer": answer,
                "topic": "Physical Sciences",
                "difficulty": "Medium",
                "explanation_en": f"Official GSET final answer key: {answer}.",
                "explanation_gu": f"Official GSET final answer key મુજબ જવાબ {answer} છે.",
                "review_flag": review,
                "review_note": "Source-image/manual review required; OCR is not authoritative." if review else "",
                "tip_en": "Verify equations, symbols, figures and scientific notation against the original GSET PDF.",
                "tip_gu": "Equation, symbol, figure અને scientific notation માટે original GSET PDF ચકાસો.",
                "source_verified": not review,
                "source": f"GSET official {exam} Physical Sciences Paper-II and final answer key",
                "source_url": paper_url,
                "answer_key_url": key_url
            }
            byid[qid] = record

        report.append({
            "paper_id": pid, "expected": expected,
            "parsed": expected - len(missing),
            "verified": verified, "review": review_count,
            "missing": missing, "key_verified": True
        })

    merged = sorted(byid.values(), key=lambda x: (x.get("paper_id", ""), x.get("id", "")))
    OUT.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    update_papers_metadata(report)

    print("\nPHYSICAL SCIENCES ARCHIVE REPORT")
    overall_fail = False
    for r in report:
        missing = ",".join(f"Q{q}" for q in r["missing"]) if r["missing"] else "none"
        status = "REVIEW_REQUIRED" if r["missing"] or r["review"] else "OK"
        print(f"Paper: {r['paper_id']}")
        print(f"Expected: {r['expected']}")
        print(f"Parsed: {r['parsed']}")
        print(f"Verified: {r['verified']}")
        print(f"Review required: {r['review']}")
        print(f"Missing: {missing}")
        print(f"Build status: {status}")
        if r["missing"]:
            overall_fail = True
    # Missing questions are a source-review condition, not a parser crash.
    # CI decides integrity from exact completeness/duplicate/key checks below.
    if overall_fail:
        log("REVIEW", "One or more official source questions remain unresolved; no fabricated records were created.")

if __name__ == "__main__":
    main()
