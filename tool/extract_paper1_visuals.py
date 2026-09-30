#!/usr/bin/env python3
import json
import os
import re
import subprocess
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

import fitz
from PIL import Image
import pytesseract

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "assets/questions.json"
OUT = ROOT / "assets/images"
TMP = ROOT / ".paper1_visual_tmp"
OUT.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)

# These are Paper-I items whose original question contains a table, graph,
# Venn/logic diagram, sequence, map, or other visual reference.  The source
# PDF page is shown; no visual is recreated from OCR.
VISUALS = {
    "2003_dec": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 39],
    "2008_dec": [2, 6, 8, 11, 12],
    "2010_oct": [46, 51, 53, 54],
    "2011_oct": [43, 44, 45],
    "2013_sep": [55],
    "2017_aug": [41],
}

SOURCES = {
    "2003_dec": ROOT / "assets/source_papers/dec03p1.pdf",
    "2008_dec": ROOT / "assets/source_papers/dec08p1.pdf",
    "2010_oct": ROOT / "assets/sources/oct10p1.pdf",
    "2011_oct": ROOT / "assets/source_papers/oct11p1.pdf",
    "2013_sep": ROOT / "assets/source_papers/sept13p1.pdf",
    "2017_aug": ROOT / "assets/source_papers/aug17p1.pdf",
}

OFFICIAL_URLS = {
}

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def question_no(q):
    m = re.search(r"_Q(\d+)$", str(q.get("id", "")), re.I)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(\d+)\s*[.)]", str(q.get("question_en", "")))
    return int(m.group(1)) if m else None

def download(url, dest):
    if dest.exists() and dest.stat().st_size > 10000:
        return
    cmd = [
        "curl", "-L", "--fail", "--retry", "8", "--retry-all-errors",
        "--retry-delay", "5", "--connect-timeout", "30", "--max-time", "300",
        "--insecure", "-o", str(dest), url,
    ]
    subprocess.run(cmd, check=True)

def page_texts(pdf):
    doc = fitz.open(pdf)
    texts = [p.get_text("text") for p in doc]
    # Old/scanned papers may have little/no text. OCR only those pages.
    for i, text in enumerate(texts):
        if len(norm(text)) >= 80:
            continue
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), colorspace=fitz.csRGB)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        try:
            texts[i] = pytesseract.image_to_string(img, config="--psm 6")
        except Exception:
            texts[i] = text
    return doc, texts

def find_page(q, texts):
    n = question_no(q)
    qnorm = norm(q.get("question_en", ""))
    candidates = []
    for i, text in enumerate(texts):
        t = norm(text)
        score = 0.0
        if qnorm:
            words = qnorm.split()
            # Use a distinctive prefix, avoiding generated source-note wording.
            prefix = " ".join(words[:12])
            if len(prefix) >= 25 and prefix in t:
                score += 2.0
            score += min(0.8, SequenceMatcher(None, qnorm[:140], t[:1600]).ratio())
        if n is not None:
            if re.search(rf"(?<!\d){n}\s*[.)]", text):
                score += 1.5
            if re.search(rf"(?<!\d){n}\s+", text):
                score += 0.4
        candidates.append((score, i))
    candidates.sort(reverse=True)
    return candidates[0][1] if candidates and candidates[0][0] >= 1.0 else None

def render_page(doc, page_index, dest):
    page = doc[page_index]
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    # Keep the original page visual intact; only JPEG/PNG encoding is changed.
    img.save(dest, "PNG", optimize=True)

def main():
    data = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    by_id = {str(q.get("id")): q for q in data}

    for pid, qs in VISUALS.items():
        src = Path(SOURCES[pid])
        if not src.exists() and pid in OFFICIAL_URLS:
            download(OFFICIAL_URLS[pid], src)
        if not src.exists():
            raise FileNotFoundError(f"{pid}: source PDF not found: {src}")

        doc, texts = page_texts(src)
        print(f"{pid}: {len(doc)} source pages")
        for n in qs:
            qid = f"{pid}_Q{n}"
            q = by_id.get(qid)
            if q is None:
                # Some historical IDs use lowercase q.
                q = next((x for x in data if str(x.get("paperId")) == pid and question_no(x) == n), None)
            if q is None:
                raise AssertionError(f"Missing question record: {qid}")

            page = find_page(q, texts)
            if page is None:
                raise AssertionError(f"{qid}: could not locate source page safely")

            dest = OUT / f"paper1_{pid}_q{n}.png"
            render_page(doc, page, dest)
            q["image_asset"] = f"assets/images/{dest.name}"
            q["source_page"] = page + 1
            q.setdefault("review_note", "Original source-page visual is displayed from the official GSET question paper; wording/options/official key are preserved.")

            print(f"{qid}: page {page + 1} -> {dest.name}")

    QUESTIONS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
