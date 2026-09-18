"""Render paper/survey.md to paper/survey.pdf.

Markdown to HTML, then headless Chromium to PDF. The figures are inlined so the document is
self-contained, and their dark-mode rules are stripped because a printed page has one theme.
Tables are laid out fixed-width with wrapping, since several carry cells of a few hundred
characters that must not be cut.
"""
import re, subprocess, sys, shutil
from pathlib import Path
import markdown

R = Path(__file__).resolve().parents[1]
SRC = R / "paper/survey.md"
HTML = R / "paper/survey.html"
PDF = R / "paper/survey.pdf"

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
@page :first { margin-top: 30mm; }
@page landscape { size: A4 landscape; margin: 14mm 15mm 16mm 15mm; }
.landscape { page: landscape; break-before: page; break-after: page; }
:root { --ink:#15181c; --mut:#5b6672; --line:#c9d1d8; --fill:#f4f7f9; --accent:#2f6f9f; --warn:#b5462f; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Charter","Bitstream Charter","Georgia",serif; font-size: 10pt; line-height: 1.48;
       color: var(--ink); margin: 0; hyphens: auto; }
h1,h2,h3,h4 { font-family: "Helvetica Neue",Helvetica,Arial,sans-serif; line-height: 1.22;
              color: var(--ink); page-break-after: avoid; break-after: avoid; }
h1 { font-size: 17pt; margin: 0 0 6pt; padding-bottom: 4pt; border-bottom: 1.6pt solid var(--ink); }
section.title h2:first-of-type { font-size: 12.5pt; font-weight: 500; color: var(--mut); margin: 0 0 14pt; }
h1.sec { page-break-before: always; break-before: page; margin-top: 0; font-size: 15pt;
         border-bottom: 1pt solid var(--line); }
h2 { font-size: 11.5pt; margin: 16pt 0 5pt; }
h3 { font-size: 10.5pt; margin: 13pt 0 4pt; color: var(--accent); }
p { margin: 0 0 7pt; text-align: justify; }
em { color: var(--mut); }
code { font-family: "SF Mono",Menlo,Consolas,monospace; font-size: 8.4pt; background: var(--fill);
       padding: 0.4pt 2.2pt; border-radius: 2px; overflow-wrap: break-word; }
h1 code, h2 code, h3 code { font-size: 90%; background: none; padding: 0; }
a { color: var(--accent); text-decoration: none; }
ul,ol { margin: 0 0 7pt; padding-left: 16pt; }
li { margin-bottom: 2.5pt; }
blockquote { margin: 0 0 7pt; padding-left: 9pt; border-left: 2pt solid var(--line); color: var(--mut); }
hr { border: none; border-top: 1pt solid var(--line); margin: 14pt 0; }

figure { margin: 10pt 0 12pt; page-break-inside: avoid; break-inside: avoid; text-align: center; }
figure svg { max-width: 100%; height: auto; }
figure.wide { page: landscape; break-before: page; break-after: page; margin: 0; }
figure.wide svg { width: 100%; max-width: none; height: auto; }

table { border-collapse: collapse; width: 100%; table-layout: fixed; font-size: 6.6pt;
        font-family: "Helvetica Neue",Helvetica,Arial,sans-serif; line-height: 1.3; margin: 5pt 0 10pt; }
th,td { border: 0.4pt solid var(--line); padding: 2.1pt 2.8pt; vertical-align: top;
        overflow-wrap: break-word; hyphens: auto; }
th { background: var(--fill); font-weight: 600; text-align: left; }
td code, th code { font-size: 6.2pt; background: none; padding: 0; }
tbody tr:nth-child(even) { background: #fbfcfd; }
table + p em:only-child { font-size: 8pt; }

.landscape table { font-size: 6.2pt; }
.landscape td code, .landscape th code { font-size: 6pt; }
.toc { font-size: 9pt; columns: 2; column-gap: 14mm; page-break-after: always; break-after: page; }
.toc h2 { columns: 1; margin-top: 0; }
.toc ul { list-style: none; padding-left: 0; margin: 0; }
.toc li { margin: 0 0 2.6pt; }
.toc li.l2 { padding-left: 10pt; color: var(--mut); font-size: 8.4pt; }
.toc .n { color: var(--mut); }
section.title { page-break-after: always; break-after: page; }
.frontmatter { font-size: 9pt; color: var(--mut); border-left: 2.5pt solid var(--line);
               padding-left: 9pt; margin: 0 0 14pt; }
.abstract { background: var(--fill); border: 0.5pt solid var(--line); padding: 9pt 11pt;
            margin: 0 0 14pt; font-size: 9.4pt; }
.abstract h2 { margin-top: 0; font-size: 10.5pt; }
"""

def inline_figures(html: str) -> str:
    """Replace <img src="figures/x.svg"> with the SVG itself, forced to its light palette."""
    def sub(m):
        src = m.group(1)
        p = R / "paper" / src
        if not p.exists(): return m.group(0)
        svg = p.read_text()
        # a printed page has one theme: drop the dark-mode block
        svg = re.sub(r"@media\s*\(prefers-color-scheme:\s*dark\)\s*\{[^{}]*\{[^}]*\}[^}]*\}", "", svg)
        svg = re.sub(r'\s(width|height)="\d+"', "", svg, count=2)
        vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
        wide = vb and float(vb.group(1)) > 1000
        cls = "figure wide" if wide else "figure"
        return f'<figure class="{cls}">{svg}</figure>' 
    return re.sub(r'<p><img alt="[^"]*" src="([^"]+\.svg)"\s*/?></p>', sub, html)

def build_toc(html: str):
    """Number the top-level sections, mark them for a page break, and build a two-column contents."""
    items = []
    def h1(m):
        title = m.group(1)
        anchor = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", title).lower()).strip("-")
        items.append((1, re.sub(r"<[^>]+>", "", title), anchor))
        return f'<h1 class="sec" id="{anchor}">{title}</h1>'
    body = re.sub(r"<h1>(.*?)</h1>", h1, html, flags=re.S)
    def h2(m):
        title = m.group(1)
        anchor = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", title).lower()).strip("-")
        plain = re.sub(r"<[^>]+>", "", title)
        if re.match(r"^\d+\.\d+\s", plain) or plain.startswith("Table "):
            items.append((2, plain, anchor))
        return f'<h2 id="{anchor}">{title}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", h2, body, flags=re.S)
    toc = ['<nav class="toc"><h2>Contents</h2><ul>']
    for lvl, text, anchor in items:
        cls = "l2" if lvl == 2 else "l1"
        toc.append(f'<li class="{cls}"><a href="#{anchor}">{text}</a></li>')
    toc.append("</ul></nav>")
    return body, "\n".join(toc)

def main():
    md = SRC.read_text()
    # the title block and abstract are handled as front matter, not as body sections
    md = md.replace("\n---\n", "\n\n", 1)
    html = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    # the table generator soft-wraps with <br> for a narrow markdown viewer; the print layout
    # wraps on its own, so those breaks only make rows taller than they need to be
    html = re.sub(r"<br\s*/?>", " ", html)
    html = re.sub(r"  +", " ", html)
    html = inline_figures(html)
    # the leading h1 is the document title, not a section, so protect it before numbering
    first = re.search(r"<h1>.*?</h1>", html, re.S)
    title_html = first.group(0) if first else "<h1>Survey</h1>"
    html = html[first.end():] if first else html
    # wrap the provenance paragraph and the abstract
    html = re.sub(r"(<p><em>Compiled.*?</em></p>)", r'<div class="frontmatter">\1</div>', html, flags=re.S)
    html = re.sub(r"(<h2>Abstract</h2>.*?)(?=<h1)", r'<div class="abstract">\1</div>', html, count=1, flags=re.S)
    # front matter is the subtitle, the provenance block and the abstract, in that order,
    # and it belongs with the title rather than after the contents
    front = ""
    m = re.match(r"\s*(<h2>[^<]*</h2>)", html)
    if m:
        front += m.group(1); html = html[m.end():]
    m = re.search(r'<div class="frontmatter">.*?</div>', html, re.S)
    if m:
        front += m.group(0); html = html[:m.start()] + html[m.end():]
    m = re.search(r'<div class="abstract">.*?</div>', html, re.S)
    if m:
        front += m.group(0); html = html[:m.start()] + html[m.end():]
    def widen(m):
        tbl = m.group(0)
        head = re.search(r"<thead>.*?</thead>", tbl, re.S)
        ncol = len(re.findall(r"<th[ >]", head.group(0))) if head else 0
        return f'<div class="landscape">{tbl}</div>' if ncol > 5 else tbl
    html = re.sub(r"<table>.*?</table>", widen, html, flags=re.S)
    body, toc = build_toc(html)
    out = (f"<!doctype html><html><head><meta charset='utf-8'>"
           f"<title>{re.sub(r'<[^>]+>','',title_html)}</title><style>{CSS}</style></head><body>"
           f"<section class='title'>{title_html}{front}</section>{toc}{body}</body></html>")
    HTML.write_text(out)
    print(f"html: {len(out)//1024} KB, {out.count('<figure')} figures inlined, {out.count('<table>')} tables")
    chrome = shutil.which("chromium-browser") or shutil.which("chromium")
    if not chrome:
        print("no chromium found; wrote HTML only"); return 1
    cmd = [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
           "--virtual-time-budget=30000", f"--print-to-pdf={PDF}", HTML.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if not PDF.exists():
        print("chromium failed:", r.stderr[-800:]); return 1
    stamp_page_numbers()
    import pymupdf
    d = pymupdf.open(PDF)
    land = sum(1 for pg in d if pg.rect.width > pg.rect.height)
    print(f"pdf: {PDF}, {d.page_count} pages ({land} landscape), {PDF.stat().st_size//1024} KB")
    d.close()
    return 0

def stamp_page_numbers():
    """Chromium's own footer carries a URL and a date, so the numbers are stamped afterwards."""
    import pymupdf
    d = pymupdf.open(PDF)
    n = d.page_count
    for i, pg in enumerate(d):
        if i == 0: continue
        r = pg.rect
        pg.insert_text((r.width / 2 - 14, r.height - 26), f"{i + 1} / {n}",
                       fontsize=7.5, fontname="helv", color=(0.42, 0.46, 0.5))
    tmp = PDF.with_suffix(".stamped.pdf")
    d.save(tmp); d.close()
    tmp.replace(PDF)

if __name__ == "__main__": sys.exit(main())
