#!/usr/bin/env python3
"""Generate verified original-image crops for GSET September 2016 Chemical Sciences Paper-II."""
from __future__ import annotations
import argparse, hashlib, pathlib, subprocess
import fitz

SOURCE_URL = "https://www.gujaratset.ac.in/assets/papers/paperII/sept16/sept1603.pdf"
EXPECTED_SHA256 = "abc5987bbad88e748dea7bc127ff03f0f7111714cb8dbbffec9c8c5a3bf55738"

# (question_no, zero_based_pdf_page_index, top_fraction, bottom_fraction)
CROPS = {
    19: (8, 0.57, 0.995),
    31: (11, 0.47, 0.995),
    32: (12, 0.02, 0.57),
    34: (12, 0.48, 0.995),
    36: (13, 0.34, 0.73),
    37: (13, 0.68, 0.995),
    38: (14, 0.02, 0.58),
    40: (14, 0.50, 0.995),
    43: (15, 0.32, 0.995),
    45: (16, 0.25, 0.995),
}

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def download_source(destination: pathlib.Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp = destination.with_suffix(destination.suffix + ".part")
    if tmp.exists():
        tmp.unlink()
    # The official host occasionally stalls during TLS negotiation. curl provides
    # retries for transient network/SSL failures without weakening certificate checks.
    cmd = [
        "curl", "--fail", "--location", "--silent", "--show-error",
        "--retry", "6", "--retry-delay", "5", "--retry-max-time", "300",
        "--connect-timeout", "30", "--max-time", "180",
        "-A", "GSET-Test-Series-Visual-Asset-Builder/1.0",
        "-o", str(tmp), SOURCE_URL,
    ]
    try:
        subprocess.run(cmd, check=True)
        tmp.replace(destination)
    except Exception:
        if tmp.exists():
            tmp.unlink()
        raise

def build_crops(source_pdf: pathlib.Path, output_dir: pathlib.Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with fitz.open(source_pdf) as doc:
        if len(doc) != 20:
            raise RuntimeError(f"Unexpected PDF page count: {len(doc)}; expected 20.")
        for qno, (page_index, top, bottom) in CROPS.items():
            page = doc[page_index]
            rect = page.rect
            clip = fitz.Rect(8, rect.height * top, rect.width - 8, rect.height * bottom)
            pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=clip, alpha=False)
            pix.save(output_dir / f"chemical_sep16_q{qno}.png")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=pathlib.Path, default=pathlib.Path("/tmp/sept1603.pdf"))
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("assets/images"))
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    if args.download or not args.source.exists():
        download_source(args.source)
    actual = sha256(args.source)
    if actual != EXPECTED_SHA256:
        raise RuntimeError(f"SOURCE HASH MISMATCH. Expected: {EXPECTED_SHA256}; Actual: {actual}")
    build_crops(args.source, args.out)
    print(f"Generated {len(CROPS)} verified visual assets.")

if __name__ == "__main__":
    main()
