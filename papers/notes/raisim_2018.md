# raisim_2018 — Per-Contact Iteration Method for Solving Contact Dynamics (Hwangbo et al., IEEE RA-L 2018)

SOURCE THIN: the paper PDF fetch failed. `papers/md/raisim_2018.md` is a 202-byte stub containing only the title, the source-entry key, and the unresolved bitstream URL (ETH library) — no abstract, method, or results text was captured. Everything below comes from `code/md/raisim_2018.md`, which itself is a README + pruned file tree (no C++ solver source was captured; assets and most source files were pruned from the manifest).

sources: papers/md/raisim_2018.md [no manifest entry, stub only, 202 bytes] ; code/md/raisim_2018.md [74b836fb]

## One-line contribution
Unverifiable from the parsed sources: the bib entry's `subtopic`/`why` fields describe this as the bisection per-contact solver behind RaiSim, but that claim is corpus curation metadata, not text from `papers/md` or `code/md`, so it is not repeated here as a sourced fact.

## Setting
- hand(s) / robot: not stated in the parsed sources.
- simulator / physics: RaiSim, described in the README as "a physics engine for robotics and artificial intelligence research ... we specialize in running rigid-body simulations" (code/md L16). The repo README states "We no longer support Raisim. Please go to Raisim2 repo" (code/md L11).
- README "Features" list (code/md L44-49): free camera movement, screenshot/recording, contact and collision masks, a materials system "to simulate different textures," height maps for terrain, and a ray test for collision checking. None of these lines describe the contact solver's algorithm.

## Physics block
- contact model: not stated in the parsed sources (the per-contact bisection algorithm that gives the paper its title is not present in either md file; it is only echoed, unsourced, in the corpus's own annotation of the paper, which this note excludes per the note-writing rules).
- solver and iterations: not stated.
- differentiability: not stated.
- timestep: not stated.
- friction model: not stated.
- penetration handling / whether penetration depth is exposed: not stated.
- GPU or CPU: not stated (README only lists "Supported OS: MAC (including m1), Linux, Windows," code/md L66-70, which speaks to platform, not to compute backend).
- throughput: not stated. A `benchmark/` directory and a `benchmarkCommon.hpp` file appear in the pruned file tree (code/md L96-99), but no benchmark numbers were captured.

## Evaluation
Not applicable — no experiments section was parsed from either source.

## Limitations stated by the authors
Not stated in the parsed sources.

## Quotable claims (verbatim, with section)
- "RaiSim is a physics engine for robotics and artificial intelligence research that provides efficient and accurate simulations for robotic systems. We specialize in running rigid-body simulations while having an accessible, easy to use C++ library." (code/md README)
- "You should get a valid license and an activation key from the RaiSim Tech website to use RaiSim." (code/md README, License) — RaiSim is not fully open-source; a license key is required.

## Notes for the survey
- This entry cannot support any quantitative or algorithmic claim about RaiSim's per-contact bisection solver; the survey should cite `contact_models_comparison_2023` instead, which re-implements and empirically characterizes the RaiSim contact model (its relaxation of the maximum dissipation principle, its Gauss-Seidel-style per-contact iteration, and its jamming/internal-force artifacts under stiction) with a working C++ re-implementation, since RaiSim's own source is closed/license-gated.
- Flagging for re-fetch: the PDF is hosted at ETH's research collection (bitstream URL in the stub), not arXiv; a direct fetch attempt (rather than the general crawler) may succeed.
