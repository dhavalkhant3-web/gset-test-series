#!/usr/bin/env python3
"""Render source pages from the official GSET Nov 2022 Chemical Sciences Paper-II."""
from pathlib import Path
import hashlib
import time
import socket
import urllib.request
import urllib.error
import fitz

URL = "https://www.gujaratset.ac.in/assets/papers/paperII/nov22/nov2203.pdf"
OUT = Path("assets/images")
PAGES = list(range(20, 31))

def download_with_retry(url: str, target: Path, attempts: int = 5) -> None:
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
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read()
            if len(data) < 100_000:
                raise RuntimeError(f"Downloaded file is unexpectedly small: {len(data)} bytes")
            target.write_bytes(data)
            return
        except (urllib.error.URLError, TimeoutError, socket.timeout, OSError) as exc:
            last = exc
            if attempt < attempts:
                delay = attempt * 10
                print(f"Download attempt {attempt}/{attempts} failed: {exc}; retrying in {delay}s", flush=True)
                time.sleep(delay)
    raise RuntimeError(f"Official GSET PDF download failed after {attempts} attempts: {last}")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = Path("/tmp/nov2203.pdf")
    download_with_retry(URL, pdf)
    doc = fitz.open(pdf)
    assert len(doc) == 32, f"Unexpected page count: {len(doc)}"
    for page_no in PAGES:
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        pix.save(OUT / f"chemical_nov22_page{page_no}.png")
    print(f"Generated {len(PAGES)} Nov 2022 source-page images.")

if __name__ == "__main__":
    main()
