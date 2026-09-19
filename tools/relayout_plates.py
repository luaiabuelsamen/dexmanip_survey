"""Re-render the three surviving reproduced plates from their source PDFs and cut them down.

Every plate in this survey is single column and, where the argument allows it, a single panel.
A borrowed multi-panel plate set at one column lands its panels at about 15 mm across with
labels under 8 pt, which is not a figure but the memory of one. So each plate here is either
re-laid out so that no panel shrinks (`hand_scale_to_human`, six hands cut off one long row and
stacked two deep) or cut down to the panels that carry the argument (`teleop_retarget_artifacts`,
one of sixteen cells; `bimanual_grasp_penetration`, two of four). What is dropped is dropped
because a diagram in the paper's own style now makes the point, or because the prose already did.

`pre` crops the trimmed source region before the panel boxes are read, for a region the figure
finder swept a neighbouring figure or a body-text column into.

Each entry records the source key, the figure number, the render dpi, and the panel boxes as
fractions of the trimmed figure region, so every crop here is reproducible; the same fractions
are written into tex/figs/SELECTED.md. Run from anywhere:

    python tools/relayout_plates.py [name ...]
"""
import sys
from pathlib import Path

import pymupdf
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract_figures as E  # noqa: E402  (shares the region finder and the white trim)

R = Path(__file__).resolve().parents[1]
OUT = R / "tex/figs/selected"

# name -> (source key, figure number, dpi, layout)
# A layout is a list of rows; a row is a list of (x0, x1, y0, y1) boxes in fractions of the
# trimmed region. Rows are concatenated left to right at the source scale, then centred and
# stacked, so no panel is resampled relative to any other.
PLATES = {
    # Six hands photographed to scale in one row: 3.68:1. Cut on the gutters between the hands
    # and set two rows of three, each hand keeping the label under it. Nothing is dropped: the
    # spread of sizes against the ruler is the whole content, so every hand stays.
    "hand_scale_to_human": dict(
        key="leap_hand_2023", fig=3, dpi=450,
        rows=[[(0.0000, 0.2005), (0.2005, 0.3341), (0.3341, 0.4727)],
              [(0.4727, 0.6059), (0.6059, 0.7532), (0.7532, 1.0000)]]),
    # Four failure panels over four zoomed insets, of which (A) hand-object penetration and
    # (C) inter-hand penetration are the two the section argues. (B) self-penetration and
    # (D) no-contact are dropped: at one column four panels put each inset at 20 mm, and the two
    # kept are the two the prose names. `pre` removes Fig. 6, which the finder swept into the
    # same region.
    "bimanual_grasp_penetration": dict(
        key="bimangrasp_2024", fig=9, dpi=450, pre=(0.500, 1.000, 0.000, 1.000),
        rows=[[(0.0039, 0.2360), (0.4855, 0.7215)]]),
    # A 4x4 grid of retargeting verdicts, 16 cells: at one column each cell is 22 mm and its
    # verdict label 3 pt. One cell is kept -- the hand-object case where DexPilot drives the
    # fingertip through the spectacle temple -- because one magnified contact set makes the
    # argument and sixteen illegible ones do not. The source's own label strip is cropped away
    # with it; the caption carries the verdict in the document font.
    "teleop_retarget_artifacts": dict(
        key="toporetarget_2026", fig=3, dpi=400,
        rows=[[(0.4970, 0.7190, 0.2800, 0.4550)]]),
}


def region(key, fig, dpi):
    """Render the catalogued figure region from the source PDF and trim its white margin."""
    doc = pymupdf.open(R / "papers/pdf" / f"{key}.pdf")
    for pno in range(min(len(doc), 24)):
        page = doc[pno]
        for n, rect, _cap, _d, _i in E.figures_on_page(page):
            if n != fig:
                continue
            png = page.get_pixmap(clip=rect, dpi=dpi).tobytes("png")
            import io
            return Image.open(io.BytesIO(E.trim_white(png))).convert("RGB")
    raise SystemExit(f"figure {fig} not found in {key}")


def build(name, spec):
    im = region(spec["key"], spec["fig"], spec["dpi"])
    if spec.get("pre"):
        x0, x1, y0, y1 = spec["pre"]
        W0, H0 = im.size
        im = im.crop((int(round(x0 * W0)), int(round(y0 * H0)),
                      int(round(x1 * W0)), int(round(y1 * H0))))
    W, H = im.size
    gutter = int(round(spec.get("gutter", 0.012) * W))
    vgap = int(round(spec.get("vgap", 0.030) * H))
    rows = []
    for row in spec["rows"]:
        cells = []
        for box in row:
            x0, x1 = box[0], box[1]
            y0, y1 = (box[2], box[3]) if len(box) == 4 else (0.0, 1.0)
            cells.append(im.crop((int(round(x0 * W)), int(round(y0 * H)),
                                  int(round(x1 * W)), int(round(y1 * H)))))
        w = sum(c.width for c in cells) + gutter * (len(cells) - 1)
        h = max(c.height for c in cells)
        strip = Image.new("RGB", (w, h), (255, 255, 255))
        x = 0
        for c in cells:
            strip.paste(c, (x, h - c.height))   # panels sit on a common baseline
            x += c.width + gutter
        rows.append(strip)
    w = max(r.width for r in rows)
    h = sum(r.height for r in rows) + vgap * (len(rows) - 1)
    out = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for r in rows:
        out.paste(r, ((w - r.width) // 2, y))
        y += r.height + vgap
    path = OUT / f"{name}.png"
    out.save(path)
    print(f"{name}: source region {W}x{H} ({W/H:.2f}:1) -> {w}x{h} ({w/h:.2f}:1)  {path}")


if __name__ == "__main__":
    wanted = sys.argv[1:] or list(PLATES)
    for name in wanted:
        build(name, PLATES[name])
