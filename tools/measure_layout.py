#!/usr/bin/env python3
"""Measure the page layout of a set of PDFs so that a style argument can be made
from numbers rather than from taste.

What each measurement means:

  words_per_page      running words of any kind (body, captions, table cells,
                      references) divided by the page count. It is a density,
                      not a length.
  abstract_words      words between the abstract heading and whatever ends it
                      (keywords, index terms, or the first section heading).
  fig_area_frac       union area of figure graphics (raster images plus clusters
                      of vector drawing) as a fraction of total page area
                      (width * height * pages). Captions are NOT in this number.
  tab_area_frac       union area of table bodies, located from their horizontal
                      rules where a table has them and from the caption block
                      otherwise. Captions are NOT in this number.
  text_area_frac      union area of text blocks that lie outside figure and
                      table regions. Captions ARE in this number.
  margin_frac         1 - (fig + tab + text). Whitespace, gutters, margins.
  span_frac           the fraction of figures wider than 1.35 column widths,
                      i.e. drawn across the full text width of a 2-column page.
  median_fig_h_mm     median height of a figure graphic in millimetres.

Everything is measured from the rendered PDF, so it describes what a reader
sees, not what the source says.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import subprocess
import sys
from collections import Counter

import pymupdf

PT2MM = 25.4 / 72.0

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
    "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20, "XXI": 21,
    "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25, "XXVI": 26, "XXVII": 27,
    "XXVIII": 28, "XXIX": 29, "XXX": 30,
}

FIG_CAP = re.compile(
    r"^\s*(?:Fig(?:ure|\.)?|FIG(?:URE|\.)?)\s*\.?\s*(\d{1,2})\s*(?:[a-z])?\s*[.:|)]?\s",
    re.IGNORECASE,
)
TAB_CAP = re.compile(
    r"^\s*(?:Table|TABLE|Tab\.)\s*\.?\s*([IVXLC]{1,6}|\d{1,2})\s*[.:|)]?\s",
)
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")


# ---------------------------------------------------------------- geometry ---
def area(r):
    return max(0.0, r.x1 - r.x0) * max(0.0, r.y1 - r.y0)


def merge_rects(rects, pad=6.0, rounds=6):
    """Union-merge rectangles that touch or nearly touch."""
    out = [pymupdf.Rect(r) for r in rects if area(r) > 1]
    for _ in range(rounds):
        merged = []
        used = [False] * len(out)
        changed = False
        for i, a in enumerate(out):
            if used[i]:
                continue
            cur = pymupdf.Rect(a)
            for j in range(i + 1, len(out)):
                if used[j]:
                    continue
                b = out[j]
                grown = pymupdf.Rect(cur.x0 - pad, cur.y0 - pad, cur.x1 + pad, cur.y1 + pad)
                if grown.intersects(b):
                    cur |= b
                    used[j] = True
                    changed = True
            merged.append(cur)
            used[i] = True
        out = merged
        if not changed:
            break
    return out


def union_area(rects, page_rect, grid=2.0):
    """Area of the union of rects, by rasterising onto a coarse grid."""
    if not rects:
        return 0.0
    nx = int(page_rect.width / grid) + 1
    ny = int(page_rect.height / grid) + 1
    seen = set()
    for r in rects:
        x0 = max(0, int(r.x0 / grid))
        x1 = min(nx, int(r.x1 / grid) + 1)
        y0 = max(0, int(r.y0 / grid))
        y1 = min(ny, int(r.y1 / grid) + 1)
        for x in range(x0, x1):
            for y in range(y0, y1):
                seen.add((x, y))
    return len(seen) * grid * grid


def inside(small, big, tol=3.0):
    return (small.x0 >= big.x0 - tol and small.x1 <= big.x1 + tol
            and small.y0 >= big.y0 - tol and small.y1 <= big.y1 + tol)


def overlap_frac(small, big):
    """Fraction of `small` covered by `big`. Degenerate (zero-height rule)
    rectangles are inflated so that a hairline table rule is not reported as
    lying nowhere."""
    s = pymupdf.Rect(small)
    if s.height < 0.6:
        s = pymupdf.Rect(s.x0, s.y0 - 0.3, s.x1, s.y1 + 0.3)
    if s.width < 0.6:
        s = pymupdf.Rect(s.x0 - 0.3, s.y0, s.x1 + 0.3, s.y1)
    inter = s & pymupdf.Rect(big)
    a = area(s)
    return area(inter) / a if a > 0 else 0.0


# ------------------------------------------------------------ page content ---
def text_blocks(page):
    out = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, txt, _, btype = b
        if btype != 0:
            continue
        if not txt.strip():
            continue
        out.append((pymupdf.Rect(x0, y0, x1, y1), txt))
    return out


def image_rects(page):
    rects = []
    for info in page.get_image_info():
        r = pymupdf.Rect(info["bbox"])
        if area(r) > 200:
            rects.append(r)
    return rects


def drawing_items(page):
    """Split vector drawings into thin horizontal rules and everything else."""
    W = page.rect.width
    rules, other, colour_fills, grey_fills = [], [], 0, 0
    for d in page.get_drawings():
        r = pymupdf.Rect(d["rect"])
        w, h = r.width, r.height
        if w <= 0 and h <= 0:
            continue
        if w > 0.06 * W and h < 2.5:
            rules.append(r)
            continue
        if w < 2.5 and h > 4:            # vertical rule
            rules.append(r)
            continue
        if area(r) < 30:
            continue
        if r.width > 0.95 * page.rect.width and r.height > 0.95 * page.rect.height:
            continue                      # page-sized background box
        other.append(r)
        f = d.get("fill")
        if f and len(f) >= 3:
            mx, mn = max(f[:3]), min(f[:3])
            if mx - mn > 0.06 and mx > 0.15:     # saturated, not grey
                colour_fills += 1
            elif mx < 0.995:                     # grey / tint shading
                grey_fills += 1
    return rules, other, colour_fills, grey_fills


# ------------------------------------------------------------------ layout ---
def column_geometry(doc, sample_pages):
    """Return (ncols, text_x0, text_x1, colwidth) from body text blocks."""
    lefts, rights = [], []
    twocol_votes = 0
    onecol_votes = 0
    for pno in sample_pages:
        page = doc[pno]
        W = page.rect.width
        blocks = [r for r, t in text_blocks(page) if len(t) > 200]
        if len(blocks) < 2:
            continue
        widths = [r.width for r in blocks]
        med = statistics.median(widths)
        if med < 0.42 * W:
            twocol_votes += 1
        else:
            onecol_votes += 1
        for r in blocks:
            lefts.append(r.x0)
            rights.append(r.x1)
    ncols = 2 if twocol_votes > onecol_votes else 1
    if not lefts:
        return ncols, 0.0, 0.0, 0.0
    x0 = statistics.median(sorted(lefts)[: max(1, len(lefts) // 3)])
    x1 = statistics.median(sorted(rights)[-max(1, len(rights) // 3):])
    textw = x1 - x0
    colw = textw / 2 * 0.95 if ncols == 2 else textw
    return ncols, x0, x1, colw


def table_regions(page, rules, caps):
    """Locate table bodies. Rules first; caption anchoring as a fallback."""
    W = page.rect.width
    horiz = [r for r in rules if r.width > 0.10 * W and r.height < 2.5]
    regions = []
    used = [False] * len(horiz)
    for i, a in enumerate(horiz):
        if used[i]:
            continue
        cur = pymupdf.Rect(a)
        used[i] = True
        changed = True
        while changed:
            changed = False
            for j, b in enumerate(horiz):
                if used[j]:
                    continue
                xo = min(cur.x1, b.x1) - max(cur.x0, b.x0)
                if xo > 0.4 * min(cur.width, b.width):
                    gap = max(cur.y0 - b.y1, b.y0 - cur.y1)
                    if gap < 320:
                        cur |= b
                        used[j] = True
                        changed = True
        if cur.height > 4:                   # a lone rule is a header line
            regions.append(cur)
    # a table body must contain text
    keep = []
    tb = text_blocks(page)
    for r in regions:
        n = sum(1 for br, t in tb if overlap_frac(br, r) > 0.5)
        if n >= 2:
            keep.append(r)
    # captions with no rules nearby: take the block run under the caption
    for crect, _ in caps:
        if any(abs(crect.y0 - r.y0) < 420 and overlap_frac(crect, r) > 0.2 for r in keep):
            continue
        near = [br for br, t in tb
                if br is not crect
                and min(abs(br.y0 - crect.y1), abs(crect.y0 - br.y1)) < 260
                and min(br.x1, crect.x1) - max(br.x0, crect.x0) > 0.3 * crect.width]
        if near:
            r = pymupdf.Rect(crect)
            for b in near:
                r |= b
            keep.append(r)
    return keep


def figure_regions(page, imgs, other_draw, tab_regions, page_area):
    # clip to the page: an unclipped vector path can report a bbox far off-page
    src = [pymupdf.Rect(r) & page.rect for r in list(imgs) + list(other_draw)]
    src = [r for r in src if area(r) > 1]
    cands = merge_rects(src, pad=7.0)
    out = []
    for r in cands:
        if area(r) < 0.004 * page_area:
            continue
        if any(overlap_frac(r, t) > 0.6 for t in tab_regions):
            continue
        if r.width > 0.98 * page.rect.width and r.height > 0.98 * page.rect.height:
            continue
        out.append(r)
    return out


def caption_words(txt):
    return len(WORD.findall(txt))


# ------------------------------------------------------------------ driver ---
def measure(path, verbose=False):
    doc = pymupdf.open(path)
    n = doc.page_count
    page_area_total = sum(doc[p].rect.width * doc[p].rect.height for p in range(n))

    sample = list(range(min(n, 4), min(n, 4) + 12)) or list(range(n))
    sample = [p for p in sample if p < n] or [0]
    ncols, tx0, tx1, colw = column_geometry(doc, sample)

    words_total = 0
    fig_caps, tab_caps = {}, {}
    fig_rects_all = []
    first_fig_page = None
    fig_area = tab_area = txt_area = 0.0
    tables_with_rules = 0
    tables_colour = 0
    tables_grey = 0
    n_table_regions = 0
    per_page = []

    for pno in range(n):
        page = doc[pno]
        prect = page.rect
        pa = prect.width * prect.height
        txt = page.get_text("text")
        words_total += len(WORD.findall(txt))

        blocks = text_blocks(page)
        rules, other, colour_fills, grey_fills = drawing_items(page)
        imgs = image_rects(page)

        fcaps, tcaps = [], []
        for r, t in blocks:
            head = t.strip()[:80].replace("\n", " ")
            m = FIG_CAP.match(head)
            if m and len(t.strip()) > 12:
                fcaps.append((r, t))
                num = int(m.group(1))
                fig_caps.setdefault(num, []).append((pno + 1, caption_words(t)))
                if first_fig_page is None:
                    first_fig_page = pno + 1
                continue
            m = TAB_CAP.match(head)
            if m and len(t.strip()) > 12:
                tcaps.append((r, t))
                key = m.group(1)
                num = ROMAN.get(key.upper(), None) if not key.isdigit() else int(key)
                if num is None:
                    num = key
                tab_caps.setdefault(num, []).append((pno + 1, caption_words(t)))

        tregs = table_regions(page, rules, tcaps)
        n_table_regions += len(tregs)
        for t in tregs:
            nr = sum(1 for r in rules if overlap_frac(r, t) > 0.5 and r.width > 0.1 * prect.width)
            if nr >= 2:
                tables_with_rules += 1
            if colour_fills:
                tables_colour += 1
            if grey_fills:
                tables_grey += 1

        fregs = figure_regions(page, imgs, other, tregs, pa)
        # One figure is often several graphic clusters (panels). Merge nearby
        # clusters, then attach each to the caption it sits nearest to, so that
        # a reported height is the height of a float, not of one panel.
        units = merge_rects(fregs, pad=20.0)
        groups = {}
        loose = []
        for r in units:
            best, bestd = None, 1e9
            for k, (crect, _) in enumerate(fcaps):
                xo = min(r.x1, crect.x1) - max(r.x0, crect.x0)
                if xo <= 0.25 * min(r.width, max(crect.width, 1)):
                    continue
                dv = min(abs(r.y1 - crect.y0), abs(crect.y1 - r.y0))
                if dv < bestd:
                    best, bestd = k, dv
            if best is not None and bestd < 60:
                groups.setdefault(best, []).append(r)
            else:
                loose.append(r)
        for k, rs in groups.items():
            rr = pymupdf.Rect(rs[0])
            for x in rs[1:]:
                rr |= x
            fig_rects_all.append((pno + 1, rr.width, rr.height))
        for r in loose:
            fig_rects_all.append((pno + 1, r.width, r.height))
        if fregs and first_fig_page is None:
            first_fig_page = pno + 1

        fa = union_area(fregs, prect)
        ta = union_area(tregs, prect)
        floats = fregs + tregs
        prose = [r for r, t in blocks if not any(overlap_frac(r, f) > 0.55 for f in floats)]
        pa_text = union_area(prose, prect)
        fig_area += fa
        tab_area += ta
        txt_area += pa_text
        per_page.append(dict(page=pno + 1, fig=fa / pa, tab=ta / pa, txt=pa_text / pa))

    # ---- abstract. Some preprints print it with no heading at all, and some
    # arXiv editions put a contents page first, so look over the first pages.
    head = "\n".join(doc[p].get_text("text") for p in range(min(n, 4)))
    abs_words = abstract_words(head)
    abs_src = "labelled"
    if abs_words is None:
        abs_src = "lead-paragraph"
        for pno in range(min(n, 2)):
            cand = [t for r, t in text_blocks(doc[pno]) if len(WORD.findall(t)) >= 60]
            if cand:
                abs_words = len(WORD.findall(cand[0]))
                break

    # ---- sections
    secs = sections(doc)

    # ---- figure sizes
    widths = [w for _, w, h in fig_rects_all]
    heights = [h for _, w, h in fig_rects_all]
    span = sum(1 for w in widths if colw and w > 1.35 * colw)
    single = len(widths) - span

    caps_f = [w for v in fig_caps.values() for _, w in v]
    caps_t = [w for v in tab_caps.values() for _, w in v]

    body_words = words_total
    res = dict(
        file=os.path.basename(path),
        pages=n,
        columns=ncols,
        page_w_mm=round(doc[0].rect.width * PT2MM, 1),
        words=words_total,
        words_per_page=round(words_total / n, 1),
        abstract_words=abs_words,
        abstract_src=abs_src,
        n_figures=len(fig_caps),
        n_tables=len(tab_caps),
        fig_tab_ratio=(round(len(fig_caps) / len(tab_caps), 2) if tab_caps else None),
        fig_area_frac=round(fig_area / page_area_total, 4),
        tab_area_frac=round(tab_area / page_area_total, 4),
        text_area_frac=round(txt_area / page_area_total, 4),
        margin_frac=round(1 - (fig_area + tab_area + txt_area) / page_area_total, 4),
        first_fig_page=first_fig_page,
        fig1_page=(min(p for p, _ in fig_caps[1]) if 1 in fig_caps else None),
        n_fig_graphics=len(fig_rects_all),
        fig_single_col=single,
        fig_span_col=span,
        median_fig_h_mm=round(statistics.median(heights) * PT2MM, 1) if heights else None,
        max_fig_h_mm=round(max(heights) * PT2MM, 1) if heights else None,
        median_fig_w_mm=round(statistics.median(widths) * PT2MM, 1) if widths else None,
        col_width_mm=round(colw * PT2MM, 1),
        fig_caption_words_med=round(statistics.median(caps_f), 1) if caps_f else None,
        fig_caption_words_max=max(caps_f) if caps_f else None,
        tab_caption_words_med=round(statistics.median(caps_t), 1) if caps_t else None,
        tab_caption_words_max=max(caps_t) if caps_t else None,
        n_sections=secs["n1"],
        n_subsections=secs["n2"],
        n_subsubsections=secs["n3"],
        max_depth=secs["depth"],
        section_source=secs["source"],
        words_per_section=round(body_words / secs["n1"], 0) if secs["n1"] else None,
        subsec_per_sec=round(secs["n2"] / secs["n1"], 2) if secs["n1"] else None,
        table_regions=n_table_regions,
        tables_ruled=tables_with_rules,
        tables_coloured=tables_colour,
        tables_grey_shaded=tables_grey,
        section_titles=secs["titles"],
    )
    if verbose:
        res["per_page"] = per_page
        res["fig_sizes_mm"] = [
            dict(page=p, w=round(w * PT2MM, 1), h=round(h * PT2MM, 1))
            for p, w, h in fig_rects_all
        ]
        res["fig_caption_pages"] = {k: v for k, v in sorted(fig_caps.items())}
        res["tab_caption_pages"] = {str(k): v for k, v in sorted(tab_caps.items(), key=lambda kv: str(kv[0]))}
    return res


def abstract_words(text):
    t = text.replace("\r", "")
    m = re.search(r"\bA\s?B\s?S\s?T\s?R\s?A\s?C\s?T\b|\bAbstract\b", t)
    if not m:
        return None  # caller falls back to the unlabelled lead paragraph
    rest = t[m.end():]
    enders = [
        r"\n\s*(?:Index Terms|INDEX TERMS|Keywords|KEYWORDS|Key words|CCS Concepts)",
        r"\n\s*(?:1|I)[\.\s]+(?:Introduction|INTRODUCTION)",
        r"\n\s*(?:Introduction|INTRODUCTION)\s*\n",
    ]
    cut = len(rest)
    for e in enders:
        mm = re.search(e, rest)
        if mm:
            cut = min(cut, mm.start())
    return len(WORD.findall(rest[:cut]))


def sections(doc):
    """Section counts. The PDF outline when there is one; otherwise headings
    recovered from the text, preferring IEEE roman/alpha numbering and falling
    back to type size, because in several journal styles the section number and
    its title are separate text lines."""
    toc = doc.get_toc()
    if toc and len(toc) >= 4:
        lv = [l for l, _, _ in toc]
        n1 = sum(1 for l in lv if l == 1)
        n2 = sum(1 for l in lv if l == 2)
        n3 = sum(1 for l in lv if l >= 3)
        titles = [t for l, t, _ in toc if l == 1]
        return dict(n1=n1, n2=n2, n3=n3, depth=max(lv), source="pdf-outline", titles=titles)

    # ---- IEEE style: "III. SECTION TITLE" then "A. Subsection Title"
    roman = re.compile(r"^([IVXL]+)\.\s+([A-Z][A-Za-z0-9 \-,:&]{2,60})$")
    alpha = re.compile(r"^([A-Z])\.\s+([A-Z][A-Za-z0-9 \-,:&]{2,60})$")
    r1, r2 = [], []
    for pno in range(doc.page_count):
        for line in doc[pno].get_text("text").split("\n"):
            line = line.strip()
            m = roman.match(line)
            if m and m.group(2).upper() == m.group(2):
                r1.append(line[:70])
                continue
            m = alpha.match(line)
            if m:
                r2.append(line[:70])
    if len(r1) >= 3:
        seen, t1 = set(), []
        for t in r1:
            if t.lower() in seen:
                continue
            seen.add(t.lower())
            t1.append(t)
        return dict(n1=len(t1), n2=len(set(x.lower() for x in r2)), n3=0,
                    depth=2 if r2 else 1, source="ieee-regex", titles=t1)

    # ---- type-size headings, number and title possibly on separate lines
    from collections import Counter as C
    sizes = C()
    per_page = []
    for pno in range(doc.page_count):
        lines = []
        for b in doc[pno].get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                txt = "".join(sp["text"] for sp in ln["spans"]).strip()
                if not txt:
                    continue
                sz = round(max(sp["size"] for sp in ln["spans"]), 1)
                sizes[sz] += len(txt)
                lines.append((txt, sz, ln["bbox"]))
        per_page.append(lines)
    body = sizes.most_common(1)[0][0] if sizes else 10.0
    heads = []
    for lines in per_page:
        buf = None
        for txt, sz, bbox in lines:
            if sz > body + 0.9 and len(txt) < 90:
                if buf and abs(buf[1] - sz) < 0.2:
                    buf = (buf[0] + " " + txt, sz)
                else:
                    if buf:
                        heads.append(buf[0])
                    buf = (txt, sz)
            else:
                if buf:
                    heads.append(buf[0])
                buf = None
        if buf:
            heads.append(buf[0])
    pat = re.compile(r"^(\d+(?:\.\d+){0,3})\.?\s+(\S.{1,80})$")
    n1 = n2 = n3 = 0
    depth = 0
    titles = []
    seen = set()
    for h in heads:
        h = re.sub(r"\s+", " ", h).strip()
        m = pat.match(h)
        if not m:
            continue
        num = m.group(1)
        d_ = num.count(".") + 1
        key = num
        if key in seen:
            continue
        seen.add(key)
        depth = max(depth, d_)
        if d_ == 1:
            n1 += 1
            titles.append(h[:70])
        elif d_ == 2:
            n2 += 1
        else:
            n3 += 1
    return dict(n1=n1, n2=n2, n3=n3, depth=depth, source="type-size", titles=titles)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--out", default=None)
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()
    rows = []
    for p in a.pdfs:
        try:
            r = measure(p, verbose=a.verbose)
        except Exception as e:  # keep going; a miss is recorded
            r = dict(file=os.path.basename(p), error=f"{type(e).__name__}: {e}")
        rows.append(r)
        print(json.dumps({k: v for k, v in r.items()
                          if k not in ("per_page", "fig_sizes_mm", "section_titles",
                                       "fig_caption_pages", "tab_caption_pages")}))
    if a.out:
        try:
            commit = subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
        except Exception:
            commit = "unknown"
        with open(a.out, "w") as f:
            json.dump(dict(command=" ".join(sys.argv), commit=commit, rows=rows), f, indent=1)


if __name__ == "__main__":
    main()
