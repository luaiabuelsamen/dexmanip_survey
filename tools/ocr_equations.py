"""Re-parse PDFs with OCR to recover equations that the layout parse dropped as images.

Writes papers/md/<key>.ocr.md. OCR text is noisier than the layout parse, so it is kept in a
separate file: notes quote the layout parse for prose and the OCR file for an equation, and say
which. Pages are selected as those whose native text is sparse relative to their image area,
plus any page whose native text names an equation the note needs.
"""
import os, sys, time
from pathlib import Path
import pymupdf
R = Path(__file__).resolve().parents[1]

# Tesseract looks for its language data under TESSDATA_PREFIX and fails every page without
# saying which variable is missing until you read the stderr of each one. The data ships in a
# user directory on this machine, so point at it when the environment has not.
if "TESSDATA_PREFIX" not in os.environ:
    for _c in (Path.home() / ".local/share/tessdata", Path("/usr/share/tesseract-ocr/5/tessdata"),
               Path("/usr/share/tessdata")):
        if (_c / "eng.traineddata").exists():
            os.environ["TESSDATA_PREFIX"] = str(_c); break

def ocr_key(key, dpi=200, max_pages=40):
    pdf = R / f"papers/pdf/{key}.pdf"
    if not pdf.exists(): return f"[skip] {key}: no pdf"
    out = R / f"papers/md/{key}.ocr.md"
    if out.exists() and out.stat().st_size > 5000: return f"[have] {key}"
    d = pymupdf.open(pdf)
    parts, t0 = [], time.time()
    for i, p in enumerate(d):
        if i >= max_pages: break
        try:
            tp = p.get_textpage_ocr(flags=0, dpi=dpi, full=False)
            parts.append(f"<!-- page {i+1} (ocr) -->\n" + p.get_text(textpage=tp))
        except Exception as e:
            parts.append(f"<!-- page {i+1} ocr failed: {e} -->")
    txt = "\n\n".join(parts); out.write_text(txt); d.close()
    return f"[ok] {key}: {len(parts)} pages, {len(txt)} chars, {time.time()-t0:.0f}s"

if __name__ == "__main__":
    for k in sys.argv[1:]: print(ocr_key(k), flush=True)
