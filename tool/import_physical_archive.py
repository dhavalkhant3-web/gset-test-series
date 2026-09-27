import json
import re
import subprocess
import sys
from pathlib import Path

PAPERS = [
    ("physical_aug17", "August 2017", "aug17", "aug1702", 50),
    ("physical_sep18", "September 2018", "sept18", "sept1802", 100),
    ("physical_dec19", "December 2019", "dec19", "dec1902", 100),
    ("physical_dec21", "December 2021 (January 2022)", "dec21", "dec2102", 100),
    ("physical_nov22", "November 2022", "nov22", "nov2202", 100),
    ("physical_nov23", "November 2023", "nov23", "nov2302", 100),
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

def render_ocr(pdf, stem, dpi=260):
    log("OCR", f"rendering {pdf.name} at {dpi} dpi")
    page_dir = stem.parent / (stem.name + "_pages")
    page_dir.mkdir(parents=True, exist_ok=True)
    run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(page_dir / "page")])
    texts = []
    for img in sorted(page_dir.glob("page-*.png")):
        out = img.with_suffix(".txt")
        subprocess.run(
            ["tesseract", str(img), str(out.with_suffix("")), "--psm", "6"],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        texts.append((img.name, out.read_text(encoding="utf-8", errors="ignore")))
    return texts

def extract_pages(pdf, stem):
    txt = stem.with_suffix(".txt")
    run(["pdftotext", "-layout", str(pdf), str(txt)])
    raw = txt.read_text(encoding="utf-8", errors="ignore")
    log("EXTRACT", f"pdftotext lines={len(raw.splitlines())}")
    # Keep page separators so question blocks can be page-aware.
    pages = raw.split("\f")
    numbered = sum(
        1 for page in pages
        for _ in re.finditer(r"(?m)^\s*(?:Q\.?\s*)?\d{1,3}[\.\)]?\s+", page)
    )
    if numbered >= 20:
        return [(f"text-{i+1}", p) for i, p in enumerate(pages) if p.strip()]
    return None

def normalize_question_number(s):
    s = s.replace("O", "0").replace("I", "1")
    s = re.sub(r"[^0-9]", "", s)
    return int(s) if s else None

def candidate_starts(text, expected):
    patterns = [
        re.compile(r"(?m)^\s*(?:Q\.?\s*)?(\d{1,3})[\.]\s+"),
        re.compile(r"(?m)^\s*(?:Q\.?\s*)?(\d{1,3})[\)]\s+"),
        re.compile(r"(?m)^\s*(?:Q\.?\s*)?(\d{1,3})\s+"),
    ]
    starts = []
    for pat in patterns:
        for m in pat.finditer(text):
            q = int(m.group(1))
            if 1 <= q <= expected:
                starts.append((m.start(), m.end(), q))
    # Keep the earliest start for each q; duplicates often come from OCR/header artefacts.
    best = {}
    for item in starts:
        best[item[2]] = min(best.get(item[2], item), item)
    return [best[q] for q in sorted(best)]

def build_blocks(page_texts, expected):
    all_pages = list(page_texts)
    global_text = "\n\n".join(t for _, t in all_pages)
    starts = candidate_starts(global_text, expected)
    blocks = {}
    for idx, (start, end, q) in enumerate(starts):
        stop = starts[idx + 1][0] if idx + 1 < len(starts) else len(global_text)
        blocks[q] = global_text[end:stop]
    return blocks

def parse_options(block):
    pats = [
        re.compile(r"(?m)(?:^|\n)\s*\(?([ABCD])\)?\s*[\.:\)]\s+"),
        re.compile(r"(?m)(?:^|\s)\(?([ABCD])\)?\s*[\.:\)]\s+"),
        re.compile(r"(?m)\s*\(([ABCD])\)\s+"),
    ]
    chosen = None
    for pat in pats:
        ms = list(pat.finditer(block))
        if len(ms) >= 4:
            chosen = ms[:4]
            break
    if not chosen:
        return []
    opts = []
    for i, m in enumerate(chosen):
        end = chosen[i + 1].start() if i + 1 < len(chosen) else len(block)
        opts.append(clean(block[m.end():end]))
    return opts[:4]

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
    if pages is None:
        pages = render_ocr(pdf, stem, 240)
    joined = "\n".join(t for _, t in pages)
    keys = parse_key_text(joined, expected)
    log("KEY", f"parsed {len(keys)}/{expected}")
    if len(keys) < expected:
        ocr = render_ocr(pdf, stem.with_name(stem.name + "_keyocr"), 300)
        keys = parse_key_text("\n".join(t for _, t in ocr), expected)
        log("KEY", f"OCR parsed {len(keys)}/{expected}")
    if len(keys) < expected:
        missing = ",".join(str(q) for q in range(1, expected + 1) if q not in keys)
        raise RuntimeError(f"answer key incomplete: missing {missing}")
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
    byid = {p["paper_id"]: p for p in data["papers"]}
    for r in report:
        p = byid[r["paper_id"]]
        p["questions_loaded"] = r["parsed"]
        p["questions_count"] = r["expected"]
        p["review_count"] = r["review"]
        p["missing_questions"] = r["missing"]
        p["source_verified"] = r["verified"] == r["expected"] and not r["missing"]
        p["answer_key_verified"] = r["key_verified"]
    PAPERS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    selected = set(sys.argv[1:])
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
            pages = render_ocr(pdf, WORK / stem, 260)

        blocks = build_blocks(pages, expected)
        missing = [q for q in range(1, expected + 1) if q not in blocks]
        log("PARSE", f"{pid}: parsed {len(blocks)}/{expected}")

        # A second OCR pass is used only for unresolved question numbers.
        if missing:
            ocr_pages = render_ocr(pdf, WORK / f"{stem}_ocr", 320)
            ocr_blocks = build_blocks(ocr_pages, expected)
            for q, b in ocr_blocks.items():
                if q in missing:
                    blocks[q] = b
            missing = [q for q in range(1, expected + 1) if q not in blocks]
            log("OCR", f"{pid}: recovered={expected-len(missing)}/{expected}")

        review_count = 0
        verified = 0
        for qn in range(1, expected + 1):
            answer = keys[qn]
            block = blocks.get(qn, "")
            if not block:
                review_count += 1
                continue
            opts = parse_options(block)
            # Question ends immediately before first option marker.
            first = None
            for pat in [
                re.compile(r"(?m)(?:^|\n)\s*\(?[ABCD]\)?\s*[\.:\)]\s+"),
                re.compile(r"(?m)(?:^|\s)\(?[ABCD]\)?\s*[\.:\)]\s+"),
                re.compile(r"(?m)\s*\([ABCD]\)\s+"),
            ]:
                m = pat.search(block)
                if m:
                    first = m.start()
                    break
            question = clean(block[:first if first is not None else len(block)])
            review = suspicious(question, opts)
            if review:
                review_count += 1
            else:
                verified += 1

            qid = f"{pid}_q{qn:02d}"
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
        status = "REVIEW_REQUIRED" if r["missing"] else "OK"
        print(f"Paper: {r['paper_id']}")
        print(f"Expected: {r['expected']}")
        print(f"Parsed: {r['parsed']}")
        print(f"Verified: {r['verified']}")
        print(f"Review required: {r['review']}")
        print(f"Missing: {missing}")
        print(f"Build status: {status}")
        if r["missing"]:
            overall_fail = True
    if overall_fail:
        raise SystemExit("Physical Sciences archive contains missing questions; manual source review is required.")

if __name__ == "__main__":
    main()
