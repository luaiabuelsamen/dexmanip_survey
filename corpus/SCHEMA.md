Each bib_<topic>.json is a JSON list. Entry fields:
key (str, unique, snake_case e.g. dextrack_2025), title, authors (short: "Liu et al."), year (int),
venue (str), arxiv (str id like 2502.09614 or null), pdf_url (only when not on arXiv, else null),
github (str url or null), topic (one of: sim, hand, rl, il, bimanual, bench, data, related), 
subtopic (free str), why (one sentence: what this paper contributes to the survey), 
verified (true only if the arXiv abs page or landing page was fetched and title matched).

topic `related` is not a corpus topic. It marks a work outside dexterous manipulation that the
survey cites as prior work, in `corpus/bib_related.json`: an audit or case study Section 1 positions
this survey against. Such an entry carries no file in `corpus/rows/`, is excluded from every count
over the corpus, and is quoted only from its abstract and its stated method, because no source for
it was parsed into `papers/md/`.
