#!/usr/bin/env python3
"""Generate verified original-image crops for GSET September 2016 Chemical Sciences Paper-III.

The source PDF is downloaded from the official GSET URL and its SHA-256 is checked
against the exact user-uploaded original before any crop is generated.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import urllib.request
import time
import socket

import fitz


SOURCE_URL = "https://www.gujaratset.ac.in/assets/papers/paperIII/sept16/sept16p303.pdf"
EXPECTED_SHA256 = "727eebe36e25cc51b80dade0ceffa1495daec681b3f79932ab6c524a2a81a20e"

# (question_no, zero_based_pdf_page_index, top_fraction, bottom_fraction)
CROPS = {
    17: (8, 0.03, 0.42),
    46: (16, 0.02, 0.995),
    48: (17, 0.28, 0.70),
    49: (17, 0.59, 0.995),
    50: (18, 0.02, 0.995),
    51: (19, 0.02, 0.72),
    52: (19, 0.42, 0.995),
    54: (20, 0.02, 0.55),
    55: (20, 0.43, 0.995),
    56: (21, 0.02, 0.995),
    58: (22, 0.02, 0.995),
    59: (23, 0.02, 0.58),
    60: (23, 0.46, 0.995),
    62: (24, 0.02, 0.995),
    63: (25, 0.02, 0.57),
    66: (26, 0.02, 0.75),
    68: (27, 0.02, 0.64),
}


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def download_source(destination: pathlib.Path) -> None:
    req = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "GSET-Test-Series-Visual-Asset-Builder/1.0"},
    )
    last_error = None
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                destination.write_bytes(response.read())
            if destination.stat().st_size > 0:
                return
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last_error = exc
            if attempt == 5:
                break
            delay = attempt * 10
            print(f"Download attempt {attempt}/5 failed: {exc}; retrying in {delay}s", flush=True)
            time.sleep(delay)
    raise RuntimeError(f"Unable to download official source after 5 attempts: {last_error}")


def build_crops(source_pdf: pathlib.Path, output_dir: pathlib.Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with fitz.open(source_pdf) as doc:
        if len(doc) != 32:
            raise RuntimeError(f"Unexpected PDF page count: {len(doc)}; expected 32.")

        for qno, (page_index, top, bottom) in CROPS.items():
            page = doc[page_index]
            rect = page.rect
            clip = fitz.Rect(
                8,
                rect.height * top,
                rect.width - 8,
                rect.height * bottom,
            )
            pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip, alpha=False)
            target = output_dir / f"chemical_sep16_q{qno}.png"
            pix.save(target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=pathlib.Path, default=pathlib.Path("/tmp/sept16p303.pdf"))
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("assets/images"))
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()

    if args.download or not args.source.exists():
        download_source(args.source)

    actual = sha256(args.source)
    if actual != EXPECTED_SHA256:
        raise RuntimeError(
            "SOURCE HASH MISMATCH. Refusing to generate assets.\n"
            f"Expected: {EXPECTED_SHA256}\nActual:   {actual}"
        )

    build_crops(args.source, args.out)
    print(f"Generated {len(CROPS)} verified visual assets.")


if __name__ == "__main__":
    main()
