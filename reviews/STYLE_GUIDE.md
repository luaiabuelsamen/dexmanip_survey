# Style guide, measured against eleven competitors and five exemplars

Written 18 September 2026. This is a specification, not an edit. It says where
`tex/main.pdf` sits outside the range that well-made surveys occupy, states the
rules that would bring it inside, and lists the changes in the order worth doing
them. Nothing here is an opinion about taste that is not first a number or a
rendered page that was looked at.

## 1. How this was measured

Every number below comes from `tools/measure_layout.py`, run over seventeen
PDFs:

```
. .venv/bin/activate
python tools/measure_layout.py --verbose --out reviews/style_measurements.json \
  tex/main.pdf papers/pdf/{eleven corpus surveys}.pdf papers/pdf/exemplars/*.pdf
```

The full output, per paper and per page, is `reviews/style_measurements.json`.
The exemplars live in `papers/pdf/exemplars/`, deliberately outside
`papers/pdf/`, so they enter no corpus row, no bibliography and no count.

What the measurements mean, and what they cannot do:

- **figure area** is the union of raster images and clustered vector drawing,
  clipped to the page, as a fraction of total page area (width x height x
  pages). Captions are *not* in it.
- **table area** is the table body, found from its horizontal rules where it has
  them, from its vertical rules where it has only those, and by growing out from
  the caption where it has none. Captions are *not* in it.
- **prose area** is the union of text blocks outside those regions. Captions
  *are* in it. Whatever is left over is margin, gutter and leading.
- **figure heights** are per float, not per panel: nearby graphic clusters are
  merged and attached to the caption they sit nearest, so a six-panel plate is
  measured once.
- **captions** are counted only where the label is closed by punctuation or a
  line break, so that `Fig. 3: A low-cost hand` counts and `Fig. 3 puts the
  field on one page` and `Fig. 5 of Kim et al., CC BY 4.0` do not. Before that
  filter our own credit lines were being counted as figures.
- **sections** come from the PDF outline where there is one; from IEEE
  roman/alpha heading regexes or from type size where there is not. Four papers
  took the fallback, and the fallback undercounts third-level headings.
- **abstracts** are cut at the keywords, index terms or first section heading.
  Where a paper puts something else in between, the count is a ceiling: An et
  al.'s 580 words include its "Note to Practitioners".
- **visual styles** and **table treatment** were judged by rendering pages and
  looking at them: 39 pages across six corpus surveys, 27 across five more, and
  every figure page of ours and sampled pages of each exemplar.

Two honest caveats. Three of the five exemplars were obtained as preprints
(Ibarz, Kober, Brunke), so their margins and column setting are the authors'
LaTeX rather than the journal's; page-budget numbers for those three are
indicative, and their figure, caption and section counts are not affected.
Billard and Kragic (*Science*, 2019) was wanted as a sixth exemplar and is not
here: OpenAlex records no open-access copy and none was found, so it was not
taken.

## 2. The measurement table

`ours` is `tex/main.pdf`. `exemplar` is the five downloaded surveys. `corpus` is
the eleven competitors already in `papers/pdf/`.

### 2a. Page budget

| paper | kind | pp | col | words/pp | abstract | figs | tabs | fig:tab | fig % | tab % | prose % | margin % |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **this survey** | ours | 43 | 2 | 877 | 193 | 27 | 6 | 4.50 | 7.0 | 5.1 | 56.1 | 31.8 |
| Kroemer et al., JMLR 2021 | exemplar | 82 | 1 | 447 | 154 | 3 | 0 | -- | 1.2 | 0.0 | 46.5 | 52.4 |
| Ibarz et al., IJRR 2021 | exemplar | 22 | 2 | 946 | 232 | 7 | 0 | -- | 3.0 | 0.0 | 64.9 | 32.1 |
| Brunke et al., ARCRAS 2022 | exemplar | 36 | 1 | 546 | 190 | 8 | 1 | 8.00 | 5.0 | 2.1 | 34.2 | 58.7 |
| Kober et al., IJRR 2013 | exemplar | 38 | 2 | 818 | 185 | 8 | 5 | 1.60 | 1.4 | 3.7 | 59.3 | 35.5 |
| Bohg et al., T-RO 2014 | exemplar | 21 | 2 | 883 | 156 | 17 | 3 | 5.67 | 6.9 | 4.1 | 53.9 | 35.1 |
| An et al., DexIL survey 2025 | corpus | 32 | 2 | 883 | 580 | 6 | 9 | 0.67 | 3.1 | 5.3 | 61.6 | 30.0 |
| Bai et al., unified manip. 2025 | corpus | 212 | 1 | 431 | 367 | 24 | 9 | 2.67 | 2.6 | 1.6 | 48.4 | 47.4 |
| Zhao et al., dex. hand 2026 | corpus | 22 | 2 | 882 | 208 | 9 | 2 | 4.50 | 9.0 | 2.0 | 59.6 | 29.3 |
| Welte et al., IIL survey 2025 | corpus | 27 | 1 | 551 | 199 | 4 | 3 | 1.33 | 4.0 | 3.4 | 45.6 | 47.1 |
| Firoozi et al., found. models 2023 | corpus | 33 | 2 | 906 | 203 | 1 | 2 | 0.50 | 1.0 | 1.9 | 64.1 | 32.9 |
| Zhao et al., sim2real 2020 | corpus | 8 | 2 | 839 | 213 | 3 | 1 | 3.00 | 4.0 | 8.0 | 52.5 | 35.5 |
| contact models comparison 2023 | corpus | 17 | 2 | 815 | 222 | 19 | 3 | 6.33 | 10.5 | 11.0 | 46.9 | 31.6 |
| nine physics engines 2024 | corpus | 11 | 2 | 832 | 161 | 2 | 2 | 1.00 | 0.9 | 8.4 | 52.7 | 38.0 |
| physics engine comparison 2015 | corpus | 8 | 2 | 798 | 153 | 5 | 0 | -- | 12.6 | 0.0 | 50.7 | 36.6 |
| Ma and Dollar, dexterity 2011 | corpus | 7 | 2 | 733 | 162 | 9 | 1 | 9.00 | 10.6 | 5.0 | 48.3 | 36.1 |
| Isaac Sim 2026 | corpus | 9 | 2 | 688 | 138 | 2 | 1 | 2.00 | 4.0 | 1.9 | 54.3 | 39.8 |

### 2b. Figures and captions

`span %` is the share of figures wider than 1.35 column widths, i.e. drawn
across the page in a two-column layout. Caption columns are median / maximum
words.

| paper | 1st fig pp | fig 1 pp | 1-col | 2-col | span % | med fig h (mm) | max fig h (mm) | fig caption | tab caption |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **this survey** | 1 | 1 | 14 | 12 | **46** | 51 | 134 | 39 / **142** | **44** / **70** |
| Kroemer et al., JMLR 2021 | 2 | 2 | 2 | 1 | 33 | 86 | 162 | 10 / 12 | -- |
| Ibarz et al., IJRR 2021 | 2 | 2 | 6 | 1 | 14 | 49 | 119 | 39 / 60 | -- |
| Brunke et al., ARCRAS 2022 | 1 | 3 | 12 | 1 | 8 | 55 | 121 | 41 / 70 | 12 / 12 |
| Kober et al., IJRR 2013 | 2 | 2 | 8 | 4 | 33 | 25 | 64 | 20 / 128 | 18 / 25 |
| Bohg et al., T-RO 2014 | 3 | 3 | 31 | 2 | 6 | 29 | 114 | 29 / 120 | 8 / 8 |
| An et al., DexIL survey 2025 | 2 | 2 | 16 | 2 | 11 | 32 | 109 | 18 / 52 | 9 / 13 |
| Bai et al., unified manip. 2025 | 1 | 1 | 22 | 0 | 0 | 103 | 204 | 21 / 89 | 9 / 22 |
| Zhao et al., dex. hand 2026 | 3 | 3 | 5 | 4 | 44 | 89 | 152 | 6 / 35 | 8 / 8 |
| Welte et al., IIL survey 2025 | 2 | 2 | 4 | 0 | 0 | 93 | 113 | 14 / 21 | 12 / 12 |
| Firoozi et al., found. models 2023 | 5 | 5 | 0 | 1 | 100 | 115 | 115 | 8 / 8 | 6 / 6 |
| Zhao et al., sim2real 2020 | 1 | 1 | 2 | 1 | 33 | 46 | 76 | 33 / 36 | 13 / 13 |
| contact models comparison 2023 | 1 | 1 | 12 | 4 | 25 | 46 | 197 | 45 / 160 | 7 / 10 |
| nine physics engines 2024 | 2 | 2 | 0 | 1 | 100 | 46 | 46 | 8 / 9 | 36 / 53 |
| physics engine comparison 2015 | 3 | 3 | 5 | 2 | 29 | 83 | 234 | 44 / 81 | -- |
| Ma and Dollar, dexterity 2011 | 1 | 1 | 2 | 2 | 50 | 92 | 114 | 7 / 16 | 7 / 7 |
| Isaac Sim 2026 | 2 | 2 | 0 | 2 | 100 | 61 | 74 | 30 / 46 | 48 / 48 |

The 100 % span figures are papers with one or two figures in total; ignore them.

### 2c. Structure

| paper | sec | subsec | subsubsec | depth | headings/pp | words/section | subsec/sec | figs/10pp | floats/pp | fig+tab % |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **this survey** | **14** | **52** | 8 | 3 | **1.72** | 2694 | 3.71 | 6.3 | 0.77 | **12.1** |
| Kroemer et al., JMLR 2021 | 9 | 28 | 5 | 3 | 0.51 | 4072 | 3.11 | 0.4 | 0.04 | 1.2 |
| Ibarz et al., IJRR 2021 | 5 | 15 | 0 | 2 | 0.91 | 4164 | 3.00 | 3.2 | 0.32 | 3.0 |
| Brunke et al., ARCRAS 2022 | 7 | 7 | 0 | 2 | 0.39 | 2808 | 1.00 | 2.2 | 0.25 | 7.2 |
| Kober et al., IJRR 2013 | 8 | 29 | 0 | 2 | 0.97 | 3883 | 3.62 | 2.1 | 0.34 | 5.2 |
| Bohg et al., T-RO 2014 | 7 | 19 | 8 | 3 | 1.62 | 2650 | 2.71 | 8.1 | 0.95 | 11.1 |
| An et al., DexIL survey 2025 | 9 | 39 | 48 | 3 | 3.00 | 3140 | 4.33 | 1.9 | 0.47 | 8.4 |
| Bai et al., unified manip. 2025 | 11 | 47 | 26 | 3 | 0.40 | 8308 | 4.27 | 1.1 | 0.16 | 4.2 |
| Zhao et al., dex. hand 2026 | 6 | 13 | 0 | 2 | 0.86 | 3236 | 2.17 | 4.1 | 0.50 | 11.1 |
| Welte et al., IIL survey 2025 | 5 | 3 | 6 | 3 | 0.52 | 2974 | 0.60 | 1.5 | 0.26 | 7.3 |
| Firoozi et al., found. models 2023 | 8 | 27 | 24 | 3 | 1.79 | 3736 | 3.38 | 0.3 | 0.09 | 3.0 |
| Zhao et al., sim2real 2020 | 7 | 15 | 0 | 2 | 2.75 | 959 | 2.14 | 3.8 | 0.50 | 12.0 |
| contact models comparison 2023 | 6 | 9 | 0 | 2 | 0.88 | 2310 | 1.50 | 11.2 | 1.29 | 21.5 |
| nine physics engines 2024 | 9 | 8 | 10 | 3 | 2.45 | 1017 | 0.89 | 1.8 | 0.36 | 9.3 |
| physics engine comparison 2015 | 7 | 6 | 4 | 3 | 2.12 | 912 | 0.86 | 6.2 | 0.62 | 12.6 |
| Ma and Dollar, dexterity 2011 | 4 | 5 | 0 | 2 | 1.29 | 1282 | 1.25 | 12.9 | 1.43 | 15.6 |
| Isaac Sim 2026 | 6 | 12 | 0 | 2 | 2.00 | 1032 | 2.00 | 2.2 | 0.33 | 5.9 |

Our 14 first-level entries are 9 body sections, 4 appendices and the references.
Counting body sections only, 9 is inside the 4-to-11 range. The 52 second-level
headings are not.

### 2d. Figure styles and table treatment, judged by looking

| paper | distinct figure styles | one colour code across figures? | table treatment |
|---|--:|---|---|
| **this survey** | **11** (one TikZ house style over 9 generated figures; 18 reproduced plates in the styles of 10 source papers) | no; the TikZ figures share a grey/amber palette, the 18 plates each keep their source's palette | horizontal rules, near-white blue-grey zebra tint, plus a 6 pt footnote paragraph under most tables |
| Kroemer et al., JMLR 2021 | 2 (flat pastel block diagram; one photo collage of the authors' own work) | n/a, 3 figures | no tables at all |
| Ibarz et al., IJRR 2021 | 1 (the authors' own robot photographs) | n/a | no tables |
| Brunke et al., ARCRAS 2022 | 2 (block schematics; taxonomy/summary graphics) | yes: blue = cross-reference, orange = run-in heading, consistent fills | horizontal rules only, no tint |
| Kober et al., IJRR 2013 | 2 (own photographs; line schematics) | yes, restrained | horizontal rules only |
| Bohg et al., T-RO 2014 | 3 (radial taxonomy; a repeated flow-chart grammar; result grids) | **yes, strictly**: one colour per taxonomy branch, reused in every figure and in the edge labels | horizontal rules only |
| An et al., DexIL survey 2025 | 4 | close to one pastel family, reused in the priority matrix | full grids, no tint |
| Bai et al., unified manip. 2025 | 3 | yes, one blue accent plus fixed category tints | booktabs, rules only |
| Zhao et al., dex. hand 2026 | 4 | yes for the four timelines (fixed method-family legend), dropped elsewhere | rules only, 13 columns, very small type |
| Welte et al., IIL survey 2025 | 4 | loose; Excel defaults sit outside the house blue | rules only |
| Firoozi et al., found. models 2023 | 1 | single salmon fill, meaning nothing | rules plus **zebra**; the most legible wide table in the corpus |
| Zhao et al., sim2real 2020 | 3 | no | rules only; one table rotated onto a whole landscape page |
| contact models comparison 2023 | 5 | two codes that conflict (red = force in schematics, red = a solver in plots) | rules + one vertical + blue-grey zebra + bold spanning group rows |
| nine physics engines 2024 | 3 | no | full grids, 14 x 9 of `++/+/-/--` at about 6 pt |
| physics engine comparison 2015 | 4 | **yes, strictly**: one colour per engine in every chart | no tables at all |
| Ma and Dollar, dexterity 2011 | **1** | yes, plus a motif vocabulary (dashed = alternative pose, solid = current) | one full-grid table with a tinted header |
| Isaac Sim 2026 | 3 | no; the taxonomy's five category colours are never reused | rules only, three-level tick/circle/cross; the best-looking matrix in the corpus |

## 3. Where we sit outside the range

Outside the exemplar range, worst first:

1. **Borrowed figures.** 18 of our 27 figures are photographs or screenshots
   reproduced from 10 other papers, 8 of them carrying a CC BY attribution line.
   All five exemplars reproduce **nothing**: every figure is the authors' own
   diagram, plot or photograph. This is the root of the ugliness. It forces 11
   visual styles where the exemplars hold 1 to 3, it forces a third typographic
   element under the caption (the grey `\src` credit line), and it creates the
   permissions register in `tex/PERMISSIONS.md`.
2. **Second-level headings: 52**, against 7 to 29 for the exemplars, and
   **1.72 numbered headings per page** against 0.39 to 1.62. Only An et al.
   (3.00) and the two 8-page benchmark papers are denser, and none of those is a
   model. The headings are also sentences rather than labels ("No closed-loop
   policy records interpenetration for its own rollouts"), so the table of
   contents reads as an argument instead of a map.
3. **Full-width figures: 46 %** of our figures break the column grid, against
   6 % (Bohg), 14 % (Ibarz) and 33 % (Kober) in the two-column exemplars. Twelve
   `figure*` floats in 43 pages is what makes the page feel out of control, and
   one of them (Fig. 3) is a full-width float carrying a 0.66-textwidth image,
   so it reserves the strip and then leaves a third of it white.
4. **Table captions: 44 words median, 70 maximum**, against 8 to 18 median and
   8 to 25 maximum in the exemplars. Every one of our tables also carries a
   second explanatory paragraph beneath it at 6 pt. Three text elements per
   float, where the exemplars have one.
5. **Figure caption maximum: 142 words**, above every exemplar (12, 60, 70, 120,
   128). Our median, 39, is fine and matches Ibarz and Brunke exactly.
6. **Float ink: 12.1 %** of total page area is figure or table, just above the
   exemplar ceiling of 11.1 % (Bohg) and far above the 1.2 % to 7.2 % of the
   three long exemplars.
7. **Abstract shape.** 193 words is inside the range. **Four paragraphs** is not:
   every exemplar abstract, read off the rendered page, is a single paragraph.

Inside the range, and worth not breaking: 43 pages (21-82); 877 words per page
(447-946); 6.3 figures per ten pages (0.4-8.1); 51 mm median figure height
(25-86); 2694 words per section (2650-4164); 39-word median figure caption
(10-41); and a figure on page 1, which only Bai, Brunke and two corpus papers
manage.

## 4. The author's five complaints, checked against the data

**"Figure 1 is ugly." Supported, but not for the reason it looks like.** Fig. 1
is 82 x 34 mm, the *smallest* float in the paper, so no size cut will help. It is
ugly because it puts three unrelated encodings into 28 cm-squared: three grey
funnel bars carrying 112 / 62 / 38, a strip of 38 blue unit marks whose unit is
explained only by a line of amber text inside the figure, and two lines of
blue micro-copy that repeat the caption. Grey, blue and amber appear in this
combination nowhere else in the paper. And it spends the page-1 slot, which
Kroemer, Brunke, Bohg and Bai all spend on a map of the paper, on a single
statistic.

**"Figure 2 does not transmit its idea." Supported.** Fig. 2 is 181 x 33 mm and
holds five stages, 22 labelled nodes and 92 edges: 0.68 nodes per millimetre of
height. Kroemer's Figure 1, the comparable "structure of the review" diagram, is
114 x 81 mm for about a dozen boxes, roughly 0.15 per millimetre, four to five
times less dense. The routing that is the whole point of our figure is drawn at
0.13 pt in 14 % grey; at print scale it is invisible, so the caption's claim
that "the routes converge" cannot be checked by looking at the figure. It is
also on page 4, two pages after the text that introduces it.

**"Figures 3 to 5 are too big." Not supported as stated.** They measure 49, 39
and 33 mm tall: the three smallest body floats, all below our own 51 mm median
and below every exemplar median but Kober's and Bohg's. What is true is that
Fig. 3 is a full-width float around a 0.66-width image, and that all three are
multi-panel photo collages whose panels land at roughly 15 mm across with
sub-8 pt labels, so they cost a page-top float and deliver nothing readable. The
figures that *are* too big are the reproduced plates later on: Fig. 12 at 103 mm,
Fig. 19 at 104 mm, Fig. 23 at 91 mm, and page 23, which gives 67 % of its text
height to two borrowed plates in two unrelated visual styles.

**"The abstract is too long." Not supported on length.** 193 words, against
154-232 for the exemplars, 138-580 for the corpus, and a median of 194.5 across
the sixteen comparison papers. (The 580 is An et al., where the extractor could
not separate the abstract from the IEEE "Note to Practitioners" that follows it;
the abstract proper is shorter.) It *is* out of range on shape: four paragraphs,
where all five exemplars, checked by looking at the rendered page, use one, and
eight separate numeric claims. And it never states the partition. Bohg's abstract says "we divide the
approaches into three groups based on whether they synthesise grasps for known,
familiar or unknown objects", and those three groups are then Sections IV, V and
VI. Brunke's does the same in one sentence. Ours announces findings and leaves
the reader with no map.

**"The paper is disorganised." Supported.** Three measurements carry it.
(i) 74 numbered headings in 43 pages, a new one every 0.6 pages, above every
exemplar. (ii) 52 second-level headings, against 7 in Brunke and 19 in Bohg.
(iii) Each headline finding is stated four times. "Penetration" appears twice in
the abstract, 11 times in the introduction, 31 times in Section VII, 8 times in
Section VIII (Gaps) and 6 times in the conclusion; six of the seven subsections
of Gaps restate a result that already has its own subsection earlier. Gaps is
1665 words that mostly repeat Sections III to VII.

## 5. Six rules

**R1. Page 1 or 2 carries one figure that is a map of the paper, and every box
in it names the section that covers it.** Kroemer's Figure 1 is captioned
"Overview of the structure of the review" and each block reads `State space
(Sec. 4)`, `Policy (Sec. 6)`, `Pre- and post-conditions (Sec. 7)`. Brunke's
Figure 2 labels its blocks `Sec. 3.1 and Sec. 3.2` and `Sec. 3.3`. Bohg's
Figure 1 is a radial taxonomy whose caption cross-references Section II-D. Bai's
Figure 1 tags every block with a section number and is on page 1. The device is
not "have a teaser"; it is "the teaser is the table of contents, drawn". Of the
eleven corpus papers only Bai and Zhao 2020 put it where the reader meets it;
An, Zhao 2026 and Firoozi bury theirs on pages 3, 3 and 5.

**R2. Draw everything yourself, in one house style, with one colour code.** Zero
reproduced figures in all five exemplars. Ma and Dollar hold nine figures in a
single flat vector style with a motif vocabulary (dashed outline = alternative
configuration, solid = current, filled disc = the manipulated object). Bohg uses
one flow-chart grammar twice on facing columns so the reader can diff offline
learning against online learning, and one colour per taxonomy branch everywhere,
down to the edge labels. Todorov's five engine colours are the same five colours
in every chart in the paper. The ceiling is two styles: one diagram style and
one plot style. The colour must mean the same thing in every figure, and no
second code may borrow the same hues.

**R3. A figure is single-column until it has earned the page width, and a
full-width float fills its width.** Two-column exemplars span 6 %, 14 % and 33 %
of their figures; we span 46 %. Bohg gets 17 figures into 21 pages with 31
single-column graphics and 2 spanning ones. A `figure*` is for the map, the
taxonomy and the one matrix that needs it, and nothing else.

**R4. One float, one caption, one sentence of label; the argument goes in the
body.** Exemplar table captions run 8 to 18 words, ours 44. Exemplar figure
captions top out at 128 words and are usually far shorter. Cap figure captions
at 40 words and table captions at 20, delete the 6 pt explanatory paragraph
under each table by moving it into the body, and fold the `\src` credit into the
caption sentence rather than setting it as a separate grey line.

**R5. Two numbered heading levels, noun-phrase titles, and run-in bold leads for
everything below.** Brunke carries 36 dense pages on 7 sections and 7
subsections; below that the structure is run-in coloured heads (`3.1.1. Safe
Model-Based RL with A Priori Dynamics.`) and bold-italic paragraph leads
(`Cautious Adaptation with Probabilistic Model Learning.`). Kober does the same
with plain bold (`Neural Networks`, `Locally Linear Controllers.`,
`Non-parametric Policies.`). Ibarz runs the number into the line
(`4.2.1 Off-Policy Algorithms On-policy algorithms such as...`). All three get
four levels of texture out of two levels of numbering. Target: at most 25
numbered subsections and under 1.2 numbered headings per page.

**R6. Say each finding once, in the section that owns it, and front-load the
contribution in a table on page 1 to 3.** Kroemer states the structure once, on
page 2, tied to Figure 1, and never restates it. Against that, our Gaps section
restates six of seven findings that already have subsections. Separately: *none*
of the sixteen comparison papers has a comparison-to-prior-surveys table. Bai,
Zhao 2026, An and Isaac Sim all do the comparison in prose, and Bai buries it in
section 1.2 of a 212-page document. We already have that comparison, over 14
surveys on one set of columns, and it is prose in Appendix D on page 39, with
the table generator (`tex/tables/surveys.tex`) emitting nothing at all. Putting
it back as a table on page 2 is the single cheapest thing that would distinguish
this survey from every competitor measured.

## 6. Changes, in priority order

1. **Rebuild Figure 1 as the map of the paper.** Take Fig. 2's content (data
   source, embodiment, simulator, training, evaluation), give it the page-1 slot,
   set it at roughly 180 x 90 mm rather than 180 x 33 mm, put the section number
   in every column head, draw the routes at a weight that survives print
   (0.4 pt minimum, 40 % grey minimum), and let the node counts label the boxes
   rather than being the figure. The funnel now on page 1 becomes one sentence
   with three numbers in the introduction, or a 40 mm inline bar beside the
   Section I text. This fixes complaints one and two, and gives the reader an
   orientation device at the same time.
2. **Cut the 18 reproduced plates to at most six, all single column, one panel
   each.** Keep the ones that carry an argument no drawing can (the retargeting
   failure modes, the penetration close-up, one hand photograph for scale) and
   redraw the rest as diagrams in the TikZ house style. This removes roughly ten
   visual styles, eight CC BY attribution lines, most of the 12 full-width
   floats, and about half of the 12.1 % float ink; it brings span % from 46
   towards 15 and gives back 3 to 4 pages.
3. **Collapse Gaps and cap the heading tree.** Move each gap into the section
   that owns it as the closing run-in paragraph, and reduce Section VIII to a
   one-page numbered list of seven claims, each one sentence with a pointer to
   its section. Rename the 52 subsections to noun phrases and merge them to 25 or
   fewer, demoting the rest to bold run-in leads. Target 1.2 headings per page.
4. **Restore the prior-surveys comparison as a table on page 2**, 14 rows by the
   columns already in the repository, with the three-level tick/circle/cross
   encoding that Isaac Sim's Table 1 uses (it decoded at a glance where the
   nine-engines `++/+/-/--` grid did not). Appendix D keeps the prose.
5. **One-paragraph abstract**, still about 190 words, whose second sentence
   states the partition the survey is built on, so that the abstract and the
   section list are the same object. Keep at most three numbers.
6. **Caption discipline.** Figure captions to 40 words, table captions to 20,
   the under-table 6 pt paragraphs moved into the body, the `\src` line folded
   into the caption sentence. Our 142-word figure caption and 70-word table
   caption both come inside the exemplar range.
7. **Table treatment**, in the order the corpus shows works: horizontal rules
   only; bold spanning group rows where the groups are the taxonomy (the contact
   models paper does this well); zebra tint only on tables wider than six
   columns (Firoozi's is the most legible wide table in the corpus and is the
   only zebra in it); never a full grid, and never 6 pt.

## 7. What the exemplars do that we should not copy

- **Kroemer's figure budget.** Three figures and no tables in 82 pages, 1.2 % of
  the page area. It works because the paper is a formalism and the reader is
  expected to read it linearly, and because it was JMLR in 2021. A 2026 survey
  whose contribution is a tabulation cannot be that austere, and a reviewer would
  say so. Take Kroemer's Figure 1 and the run-in bold leads; leave the density.
- **Brunke's margin notes.** The `M12. Lipschitz Continuity:` definition boxes in
  the outer margin are excellent, and they cost 59 % of the page to white space
  in a single-column Annual Review layout. IEEEtran two-column has no margin to
  put them in. Do not fake it with framed boxes in the text column.
- **Bohg's float density.** 0.95 floats per page and 11.1 % ink is the top of the
  range, and pages 12 to 15 of the contact-models paper show where that road
  ends: grids of thumbnail plots with no text. Bohg gets away with it because
  every figure is in one of three styles. We would not.
- **Building to the contribution.** Kober, Ma and Dollar and Todorov all build to
  it, and in 7 to 38 pages of argument that reads well. In a 40-page reference
  document the reader enters in the middle, and the scope and the delta belong on
  pages 1 to 3.
- **Ibarz's running example as the organising principle.** Three case studies
  from the authors' own prior work carry the whole paper. We have no own work to
  carry, and substituting someone else's is what produced the 18 borrowed plates
  in the first place. Our equivalent running thread is the corpus row: the same
  structured record read out under every heading. Make that explicit instead.
- **The bracket-taxonomy-with-citation-leaves figure**, which Bai and Firoozi
  both use and which both let collapse into unreadable lists of bracketed
  numbers past about 40 citations. If it is a list of citations, set it as a
  table.

## 8. The exemplars, and what could not be obtained

In `papers/pdf/exemplars/`, outside the corpus:

| file | source |
|---|---|
| `kroemer_jmlr_manip_review_2021.pdf` | JMLR 22(30), final typeset version |
| `ibarz_how_to_train_2021.pdf` | arXiv:2102.02915, IJRR `sagej` class |
| `brunke_safe_learning_arcras_2022.pdf` | arXiv:2108.06266, the authors' Annual Review edition |
| `kober_rl_robotics_ijrr_2013.pdf` | authors' preprint of IJRR 32(11) |
| `bohg_grasp_synthesis_tro_2014.pdf` | arXiv:1309.2660, IEEE T-RO accepted version |

Not obtained: Billard and Kragic, "Trends and challenges in robot manipulation",
*Science* 364 (2019). OpenAlex reports no open-access location and none was
found; it is paywalled and was therefore not taken. No claim above rests on it.
