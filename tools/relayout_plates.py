"""Re-render four reproduced plates from their source PDFs and re-lay out their panels.

A figure that is one long row of panels renders as a letterbox strip: across the 181 mm text
width `sim_isaacgym_inhand_envs` was 34 mm tall and nothing in it could be read. This script
rebuilds those plates from the source PDF rather than from the 200 dpi catalogue preview, cuts
the panels apart on the white gutters between them, and stacks them so the plate's aspect ratio
is one a page can carry. Panel labels stay with the panel they name.

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
    # and set two rows of three, each hand keeping the label under it.
    "hand_scale_to_human": dict(
        key="leap_hand_2023", fig=3, dpi=450,
        rows=[[(0.0000, 0.2005), (0.2005, 0.3341), (0.3341, 0.4727)],
              [(0.4727, 0.6059), (0.6059, 0.7532), (0.7532, 1.0000)]]),
    # Three simulator screenshots in one row: 5.31:1. Two on top, the third centred below.
    "sim_isaacgym_inhand_envs": dict(
        key="isaacgym_2021", fig=13, dpi=600,
        rows=[[(0.0000, 0.3334), (0.3334, 0.6670)],
              [(0.6670, 1.0000)]]),
    # Five panels in one row: 3.33:1. Panels (a)-(d) are the capture-to-contact chain the plate
    # is placed for and already sit two-up; the (e) object-articulation column, which the caption
    # does not discuss, is dropped so the remaining four can be read.
    "data_arctic_bimanual": dict(
        key="arctic_2022", fig=1, dpi=600,
        rows=[[(0.0000, 0.7643)]]),
    # Not a re-layout: the first four gesture rows over the column-label strip, as before, but
    # rendered to the full width of the region. The previous crop cut the final letter of the
    # "Allegro" column label.
    "teleop_retarget_embodiments": dict(
        key="anyteleop_2023", fig=10, dpi=400,
        rows=[[(0.0, 1.0, 0.0, 0.468)],
              [(0.0, 1.0, 0.938, 1.0)]],
        gutter=0.0, vgap=0.0),
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
