"""Build a catalogue of figures from the source PDFs by rendering the region above each caption.

Academic figures are usually a composite of raster panels and vector labels, so pulling embedded
images gives fragments. Instead this finds every caption block beginning "Figure N" or "Fig. N",
takes the rectangle above it that is free of body text, and renders that region. Each entry
records the source key, page, caption, the rendered size and the source PDF's sha256, so a
reproduced figure can be attributed and its permission tracked.
"""
import json, re, sys
from pathlib import Path
import pymupdf

R = Path(__file__).resolve().parents[1]
OUT = R / "tex/figs/extracted"; OUT.mkdir(parents=True, exist_ok=True)
CAT = R / "corpus/figure_catalogue.json"
CAP = re.compile(r"^\s*(?:Figure|Fig\.?|FIGURE|Fig)\s*(\d+)[.:\s]", re.M)
DPI = 200

ARXIV = re.compile(r"arXiv:\s*\d{4}\.\d{4,5}", re.I)

def figures_on_page(page):
    blocks = sorted(page.get_text("blocks"), key=lambda b: b[1])
    # the arXiv stamp is a rotated block down the left edge; keep the clip clear of it
    page_left = page.rect.x0 + 2
    for b in blocks:
        if ARXIV.search(b[4] or "") and b[2] - b[0] < 60:
            page_left = max(page_left, b[2] + 3)
    out = []
    for i, b in enumerate(blocks):
        x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4]
        m = CAP.match(txt)
        if not m: continue
        # the figure is above the caption, bounded by the nearest text block above it
        top = page.rect.y0 + 2
        for c in blocks:
            t = c[4].strip()
            if c[3] <= y0 - 2 and c[3] > top and len(t) > 12 and not CAP.match(t) and not ARXIV.search(t):
                top = c[3]
        # and horizontally by the caption's own column
        left, right = min(x0, page_left), max(x1, page.rect.x1 - 2)
        for c in blocks:
            if c[1] >= top and c[3] <= y0 and c is not b and not ARXIV.search(c[4] or ""):
                left, right = min(left, c[0]), max(right, c[2])
        h = y0 - top
        if h < 60: continue
        rect = pymupdf.Rect(max(left - 4, page_left), max(top + 2, page.rect.y0),
                            min(right + 4, page.rect.x1), y0 - 1)
        if rect.width < 100 or rect.height < 60: continue
        # a region that is mostly blank is not a figure
        drawings = sum(1 for d in page.get_drawings() if rect.intersects(d["rect"]))
        images = sum(1 for r in [page.get_image_rects(i[0]) for i in page.get_images(full=True)]
                     for rr in r if rect.intersects(rr))
        if drawings < 3 and images == 0: continue
        out.append((int(m.group(1)), rect, " ".join(txt.split())[:400], drawings, images))
    return out

def trim_white(png, thresh=246, pad=6):
    """Crop uniform near-white margins so the figure fills its box."""
    try:
        import numpy as np, io
        from PIL import Image
    except Exception:
        return png
    im = Image.open(io.BytesIO(png)).convert("RGB")
    a = np.asarray(im)
    mask = (a < thresh).any(axis=2)
    if not mask.any(): return png
    ys, xs = np.where(mask)
    box = (max(int(xs.min()) - pad, 0), max(int(ys.min()) - pad, 0),
           min(int(xs.max()) + pad, im.width), min(int(ys.max()) + pad, im.height))
    out = io.BytesIO(); im.crop(box).save(out, "PNG")
    return out.getvalue()

def main(keys=None, limit_pages=24):
    cat = json.loads(CAT.read_text()) if CAT.exists() else {}
    manifest = json.loads((R / "corpus/manifest.json").read_text())
    for pdf in sorted((R / "papers/pdf").glob("*.pdf")):
        key = pdf.stem
        if keys and key not in keys: continue
        if key in cat: continue
        try: doc = pymupdf.open(pdf)
        except Exception as e: print(f"[skip] {key}: {e}"); continue
        items, seen = [], set()
        for pno in range(min(doc.page_count, limit_pages)):
            page = doc[pno]
            for num, rect, cap, nd, ni in figures_on_page(page):
                if num in seen: continue
                seen.add(num)
                try:
                    pix = page.get_pixmap(clip=rect, dpi=DPI)
                except Exception: continue
                if pix.width < 200 or pix.height < 120: continue
                name = f"{key}__fig{num:02d}.png"
                (OUT / name).write_bytes(trim_white(pix.tobytes("png")))
                items.append(dict(file=name, fig=num, page=pno + 1, w=pix.width, h=pix.height,
                                  caption=cap, vectors=nd, rasters=ni))
        doc.close()
        if items:
            cat[key] = dict(source_sha256=(manifest.get(key) or {}).get("sha256"),
                            images=sorted(items, key=lambda x: x["fig"]))
            CAT.write_text(json.dumps(cat, indent=1))
            print(f"[ok] {key}: {len(items)} figures", flush=True)
    tot = sum(len(v["images"]) for v in cat.values())
    print(f"\ncatalogue: {len(cat)} papers, {tot} figures")

if __name__ == "__main__": main(set(sys.argv[1:]) or None)
