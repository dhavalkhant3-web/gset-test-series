import argparse, hashlib, os, subprocess
import fitz

SOURCE_URL = "https://www.gujaratset.ac.in/assets/papers/paperII/sept16/sept1602.pdf"
EXPECTED_SHA256 = "bb1423a696f4aeeffe9a7e4162e1d53eecd2cfc480b63171cb31f5411664ac66"
OUT = "assets/images/physical_sep16_q29.png"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="/tmp/sept1602.pdf")
    ap.add_argument("--download", action="store_true")
    args = ap.parse_args()

    if args.download or not os.path.exists(args.source):
        os.makedirs(os.path.dirname(args.source) or ".", exist_ok=True)
        subprocess.run([
            "curl", "-L", "--fail", "--retry", "5",
            "--retry-delay", "5", "--connect-timeout", "30",
            "--max-time", "300", "--insecure",
            "-o", args.source, SOURCE_URL
        ], check=True)

    digest = hashlib.sha256(open(args.source, "rb").read()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"SHA-256 mismatch: {digest}")

    doc = fitz.open(args.source)
    if len(doc) < 12:
        raise SystemExit(f"Unexpected page count: {len(doc)}")

    page = doc[11]
    clip = fitz.Rect(35, 65, 520, 330)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip, alpha=False).save(OUT)
    print(f"Created {OUT} from original PDF page 12")

if __name__ == "__main__":
    main()
