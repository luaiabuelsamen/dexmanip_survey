# How this survey was built

The survey is written from a corpus that lives on disk. No claim about a paper is made from
memory; each traces to a note, each note to a parsed markdown file, and each markdown file to a
PDF or repository with a recorded hash or commit.

## Selection
Six topic-specific bibliographies were assembled in parallel (simulators and physics, hands and
vendors, reinforcement learning, imitation and human data, bimanual, benchmarks and evaluation),
seeded with the canonical works in each area and extended by search up to 2026-09-17. Every
arXiv identifier was checked by fetching the abstract page and matching the title; entries that
could not be checked that way are marked. The six lists were merged with deduplication on arXiv
identifier and normalised title, giving 221 entries.

## Acquisition
PDFs were downloaded from arXiv or, for work without a preprint, from the publisher or vendor
page recorded in the bibliography. Vendor pages for hands without any paper were fetched as HTML
and converted to markdown, so that a specification quoted in this survey is quoted from a stored
copy of the page and dated. Repositories were shallow-cloned and parsed, then deleted; what
remains is one markdown per repository holding the README, a pruned file tree, the task and
reward configuration files, and the bodies of reward and observation functions.

## Parsing
PDFs were converted with pymupdf4llm, falling back to raw text extraction when the layout parse
returned too little. The corpus manifest records, per entry, the source URL, page count, sha256
of the PDF and the converter used. Two consequences matter for reading this survey. Equations
rendered as images do not survive conversion, so where a reward weight exists only inside a
figure it is recorded as unreadable rather than guessed. Tables are flattened, so a number taken
from a table is quoted with the table it came from and, where the flattening is ambiguous, the
ambiguity is stated.

## Notes
Each entry was read into a structured note under a fixed template: embodiment, learning method,
objective, contact handling, evaluation, reproducibility, stated limitations, and quotable
claims. Notes were written only from the parsed files. Where the source is silent the note says
"not stated"; nothing was inferred from the reviewer's prior knowledge of the work. For method
papers the reward or loss was quoted from the paper and, separately, from the released code, so
that disagreements between the two are visible rather than smoothed over. Those disagreements
turned out to be common enough to become a finding in their own right.

## Sources that could not be obtained
Five works are behind publisher paywalls with no author-hosted copy found: Okamura et al. 2000,
Bicchi 2000 (IEEE T-RO), Piazza et al. 2019, Butterfass et al. 2001 (DLR-Hand II), and Hwangbo
et al. 2018 (RaiSim). They are cited by metadata and no claim in this survey rests on their
contents. The freely circulating PDF often taken for Bicchi 2000 is a different work, a book
chapter, and is listed separately.

## What this method cannot do
Mention counts over the corpus are counts of mentions, not of use: a related-work sentence
counts the same as an experiment. Vendor specifications are manufacturer claims and are labelled
as such throughout; where a page has since gone offline the note says so. The corpus is large
but not exhaustive, and selection by search favours work that is indexed, in English, and
posted as a preprint.
