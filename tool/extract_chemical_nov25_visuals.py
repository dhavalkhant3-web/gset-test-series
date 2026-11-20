#!/usr/bin/env python3
"""Generate source-page images for GSET Chemical Sciences Nov 2025 Paper-II."""
from pathlib import Path
import time
import urllib.request
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/nov25/nov2503.pdf"
OUT = Path("assets/images")
PAGES = [12, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def download_with_retry(url: str, target: Path, attempts: int = 4) -> None:
    last = None
    for attempt in range(1, attempts + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (GSET source verification)",
                    "Accept": "application/pdf,*/*",
                    "Connection": "close",
                },
            )
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if len(data) < 100_000:
                raise RuntimeError(f"Downloaded file is unexpectedly small: {len(data)} bytes")
            target.write_bytes(data)
            return
        except Exception as exc:
            last = exc
            if attempt < attempts:
                time.sleep(attempt * 5)
    raise RuntimeError(f"Official GSET PDF download failed after {attempts} attempts: {last}")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = Path("/tmp/nov2503.pdf")
    download_with_retry(URL, pdf)
    doc = fitz.open(pdf)
    assert len(doc) == 32, f"Unexpected page count: {len(doc)}"
    for page_no in PAGES:
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        pix.save(OUT / f"chemical_nov25_page{page_no}.png")
    print(f"Generated {len(PAGES)} source-page images.")

if __name__ == "__main__":
    main()
