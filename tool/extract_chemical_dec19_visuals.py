#!/usr/bin/env python3
from pathlib import Path
import hashlib, urllib.request, time, socket
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/dec19/dec1903.pdf"
EXPECTED_SHA256 = "c45c247d28a2aeef82ab05633cbc0d3bc9ed64bd7965fb2db18ed3e9077baafb"
PDF = Path("/tmp/chemical_dec19_p2.pdf")
OUT = Path("assets/images")
OUT.mkdir(parents=True, exist_ok=True)

last_error = None
for attempt in range(1, 6):
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "GSET-Test-Series-Visual-Asset-Builder/1.0"})
        with urllib.request.urlopen(req, timeout=180) as response:
            PDF.write_bytes(response.read())
        if PDF.stat().st_size > 0:
            break
    except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        last_error = exc
        if attempt == 5:
            raise SystemExit(f"Official PDF download failed after 5 attempts: {last_error}")
        delay = attempt * 10
        print(f"Download attempt {attempt}/5 failed: {exc}; retrying in {delay}s", flush=True)
        time.sleep(delay)

sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
if sha != EXPECTED_SHA256:
    raise SystemExit(f"SHA256 mismatch: {sha} != {EXPECTED_SHA256}")

pages = [8,12,13,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
# Page 20-37 are included only where a reviewed visual question occurs.
# Keep whole source pages rather than inventing/reconstructing chemical structures.
doc = fitz.open(PDF)
for page_no in pages:
    p = doc[page_no - 1]
    pix = p.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    pix.save(OUT / f"chemical_dec19_page{page_no}.png")

print(f"Generated {len(pages)} official Chemical Sciences December 2019 source-page visuals.")
