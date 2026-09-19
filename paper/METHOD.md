# How this survey was built

The survey is written from a corpus that lives on disk. No claim about a paper is made from
memory. Each claim traces to a note, each note to a parsed markdown file, and each markdown file
to a PDF or repository with a recorded hash or commit.

## Selection
Six topic-specific bibliographies were assembled in parallel (simulators and physics, hands and
vendors, reinforcement learning, imitation and human data, bimanual, benchmarks and evaluation),
seeded with the canonical works in each area and extended by search up to 2026-09-17. Every
arXiv identifier was checked by fetching the abstract page and matching the title, and entries
that could not be checked that way are marked. The six lists were merged with deduplication on arXiv
identifier and normalised title, giving 221 entries.

Seven further bibliography entries are not part of that corpus and are not counted anywhere in this
survey. They are the prior audits and case studies section 1 positions this survey against, they
carry the topic `related` in `corpus/bib_related.json`, and none of them carries a structured row.
No source for them was parsed either, so each is quoted only from its abstract and its stated
method.

## Acquisition
PDFs were downloaded from arXiv or, for work without a preprint, from the publisher or vendor
page recorded in the bibliography. Vendor pages for hands without any paper were fetched as HTML
and converted to markdown, so that a specification quoted in this survey is quoted from a stored
copy of the page and dated. Repositories were shallow-cloned and parsed, then deleted. What
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
"not stated", and nothing was inferred from the reviewer's prior knowledge of the work. For method
papers the reward or loss was quoted from the paper and, separately, from the released code, so
that disagreements between the two are visible rather than smoothed over. Those disagreements
turned out to be common enough to become a finding in their own right.

## Sources that could not be obtained
Six works are cited by metadata only and no claim in this survey rests on their contents. Five
are behind publisher paywalls with no author-hosted copy found on 2026-09-18: Okamura et al.
2000, Bicchi 2000 (IEEE T-RO), Piazza et al. 2019, Roa and Suarez 2015, and Butterfass et al.
2001 on DLR-Hand II. The sixth is Hwangbo et al. 2018 on RaiSim, whose hosted PDF returned no
body. The freely circulating PDF often taken for Bicchi 2000 is a different work, a book chapter,
and is listed separately.

Ma and Dollar 2011 is a seventh case with a different cause. The fetch that failed when its note
was written succeeded on 2026-09-18, so a seven-page PDF and its hash are in the manifest, but no
note has been read from it. It is cited by metadata only for that reason and not because the
source is unavailable.

Three of the 221 bibliography entries carry no structured row. Two are the paywalled
Bicchi 2000 and DLR-Hand II entries. The third is `bicchi_grasping_chapter_2001`, which was read
into a note and quoted throughout but is a book chapter rather than a work with an embodiment, a
method or a result to record in a row.

The reference list of the typeset edition is shorter than the corpus, and the two numbers are
different quantities. It prints 205 entries: the 198 corpus entries that some sentence, table or
figure of this paper cites, plus the 7 prior-work entries from outside the corpus. The other 23
corpus entries carry a row and a note and are counted in every statistic here, but no passage in
the paper names them, so they have nothing to be cited from and do not appear in the list. This
edition cites by key rather than by number and prints no list, so the place to count all 221 is
`corpus/bib.json`. A reader counting the typeset reference list should get 205, and a reader
counting the corpus should get 221.

## What this method cannot do
Mention counts over the corpus are counts of mentions, not of use: a related-work sentence
counts the same as an experiment. Vendor specifications are manufacturer claims and are labelled
as such throughout, and where a page has since gone offline the note says so. The corpus is
large but not exhaustive, and selection by search favours work that is indexed, in English, and
posted as a preprint. It also favours recent work. Of the 221 bibliography entries, 138 are dated
2024 or later and 16 predate 2018, so this is a corpus of the learned era and any claim here
about a trend over time is a claim about 2022 onward.

Every coverage statistic in this survey measures what this survey's extraction captured, not what
the literature reported. A structured row holds a scalar. A paper that reports a per-task count,
a rubric, or a total spread across several tables produces a null, and a null is then counted as
silence. The bias runs one way. Every miss converts a reporting paper into a silent one, so the
field is made to look worse at reporting than it is. The size of the effect was measured on the
statistic the survey leads with. Of the 34 method rows that had a real robot and no recorded
trial count, 15 carried a count in plain text in their own note, dropped because the paper
reports it per task and the field takes a single integer. Those 15 have since been re-extracted,
which moved the stated-trial-count row from 55 to 70. The success criterion and the unseen-object
count were audited the same way, rising from 79 to 98 and from 32 to 39. What those 19 recovered criteria say is mostly
not a threshold: eleven score by rubric or staged partial credit, five judge binary completion
against a task description by eye, two defer to a benchmark's own definition, and exactly one,
`pistar06_2025`, states a verbatim numeric threshold. The audit counted only cases where the note
itself carried the number, so a count the note also missed is still uncounted, and 19 trial counts,
8 unseen-object evaluations whose object count the note never gives, and 4 criteria remain
genuinely unsettled. Fifteen of the recovered trial counts are named in the rows: `pi0_2024` at ten
trials per task, `rdt1b_2024` at 139 across seven tasks, `umi_2024` at 260, `pistar06_2025` at 750,
`gemini_robotics_2025` at twenty per task, and ten more, which is 44 percent of the audited nulls
and moved the "never says" figure from 34 of 89 down to 19. Read every coverage statistic in this
survey as a floor rather than as a rate, and read the bars in Figure 6 the same way.

**The penetration field, audited the same way.** The same mechanism reaches the penetration,
code-release and failure-mode fields. The penetration field has since been audited by hand, because
this survey's second finding is a null over it and a null is worth what the search behind it is
worth. The population is the 85 method rows whose contact-handling field records that the work does
not address penetration. It excludes the 16 nulls, which are already counted as unsettled rather
than as silence, so recovering one would not move the finding. Twenty-five of the 85, 29 percent,
were drawn with `random.Random(20260919).sample` over the sorted population, so the draw is fixed
and can be redrawn. Each sampled row was read again in `papers/md/`, in its OCR recovery where one
exists, and in `code/md/` where a repository was parsed, but not in `papers/notes/`, because the
note is the artefact under suspicion: a field is wrong exactly when the source says something the
note did not carry. A regular expression over the whole source collected every occurrence of
penetration, interpenetration, intersection, intersection volume, solid intersection, simulation
displacement, contact consistency, physical plausibility, signed distance and contact depth, and of
the words that are mistaken for them, and every hit was read in its context. A row counted as a
recovery if its own source reported a measurement of any of those quantities on that method's own
rollouts. A statement that penetration occurs, a citation whose title says physically plausible, a
collision-avoidance constraint on a reference trajectory and a solver setting did not count, and the
three recurring near misses of that kind are listed in section 7.2. Recoveries: none of the 25,
against the 20 to 45 percent the three earlier audits recovered on the fields above. The one-sided
95 percent bound, computed hypergeometrically over the finite population, is therefore 8 of the 85,
and section 7.2 states it beside the claim and names the one borderline case that a reader might
count differently. Why this field held where the others did not is visible in the verdicts: the
recovered trial counts and criteria were numbers present in the source and dropped by a field shaped
to hold a scalar, whereas a penetration number is absent from the source altogether. The earlier
audits measured a defect in this schema; this one looked for an absence in the literature.
`reviews/penetration_audit.md` holds the seed, the sample and a verdict per row beside the sentence
it rests on, and `tools/audit_penetration.py` redraws the sample and re-runs the sweep. The
code-release and failure-mode fields have still not been audited this way, and their counts stay
floors.
