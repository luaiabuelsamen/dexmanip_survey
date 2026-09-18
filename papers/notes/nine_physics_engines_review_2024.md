# nine_physics_engines_review_2024 — A Review of Nine Physics Engines for Reinforcement Learning Research (Kaup, Wolff, Hwang, Mayer, Bruni; Osnabrück University, arXiv 2024)

sources: papers/md/nine_physics_engines_review_2024.md [26050d03] ; code/md: no code (not on GitHub as a fetchable repository — bib `github: null`)

## One-line contribution
A qualitative popularity/feature/usability review of nine engines (Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity, Webots) for RL research, scored on documentation, MARL-readiness, URDF/MJCF support, and other usability axes, concluding MuJoCo is currently dominant on performance/flexibility despite poor usability (Abstract).

## Setting
- hand(s) / robot: none specifically — the review is engine-level, using ant/humanoid/half-cheetah-style RL benchmark bodies as running examples (Fig. 1), not dexterous hands.
- simulator / physics: the nine engines under review are the subject, not a single testbed. No new simulation is run by the authors; this is a literature + documentation review (Sec. II, "Methodology": popularity analysis by citation count, feature analysis from documentation and prior reviews).

## Physics block
This is a review paper: rather than one engine's contact model, it reports each engine's compute backend and rigid-body feature completeness (Table II, "Feature and Usability Comparison," legend: ++ fully available/functional, + available but lacking, − available but lacking or workaround-only, −− not available/difficult):

| Feature | Brax | Chrono | Gazebo | MuJoCo | ODE | PhysX | PyBullet | Unity | Webots |
|---|---|---|---|---|---|---|---|---|---|
| Open Source | ++ | ++ | ++ | ++ | ++ | + | ++ | − | ++ |
| Documentation | −− | − | − | + | − | ++ | − | ++ | ++ |
| Community resources | −− | − | + | + | − | − | − | ++ | + |
| Model library | + | ++ | ++ | ++ | −− | + | ++ | ++ | + |
| Model creation | − | − | − | − | −− | − | − | ++ | + |
| Environment library | −− | −− | + | −− | −− | − | −− | ++ | + |
| Environment creation | −− | −− | −− | −− | −− | −− | −− | ++ | − |
| Visualization | ++ | ++ | ++ | + | −− | ++ | + | ++ | ++ |
| Rigid body dynamics | ++ | ++ | ++ | ++ | ++ | ++ | ++ | ++ | ++ |
| Multi-joint dynamics | ++ | ++ | + | ++ | ++ | ++ | ++ | − | + |
| Sensors | − | ++ | ++ | ++ | −− | ++ | − | ++ | ++ |
| URDF support | ++ | − | ++ | ++ | −− | ++ | ++ | −− | + |
| MJCF support | ++ | − | ++ | ++ | −− | ++ | ++ | + | − |

- GPU or CPU (per engine, from the feature narrative): **Brax** — GPU/TPU, JAX-based, "brings both together on a single GPU or TPU chip in order to reduce latency" (Sec. III-B.8). **PhysX/IsaacGym** — GPU-accelerated, "leverages GPU acceleration to increase simulation speed compared to other engines' CPU-based physics simulation," connecting simulation tensors directly to PyTorch to avoid CPU bottlenecks (Sec. III-B.5). **MuJoCo** — "natively runs on a single thread, but multi-threading can also be implemented"; libraries like Envpool can vectorize sampling but are optimized mainly for single-agent Gym tasks (Sec. III-B.1). PyBullet, Unity, Gazebo, ODE, Webots, Chrono are described as CPU-based (no GPU acceleration claims made for any of them in the text).
- solver/contact detail per engine: not derived independently by this paper — it summarizes documentation and cites external benchmark papers rather than deriving new solver characterizations, so no LCP/CCP/NCP-level detail is given for any engine here (contrast `contact_models_comparison_2023`, which does derive this).
- differentiability: only Brax is described as differentiable in this paper's narrative ("a differentiable physics engine for large scale rigid body simulation," Sec. III-B.8, quoting Brax's own tagline); no other engine's differentiability is discussed.
- timestep / friction model / penetration exposure: not discussed at the level of individual engines in this paper.
- throughput: no independent benchmarking was run by the authors (Sec. V, Limitations: "To rigorously assess and compare the quantitative performance of the presented frameworks, one would have to implement the same scenarios ... This goes beyond the scope of this paper"). Throughput claims are second-hand, cited from other papers (Sec. IV, "Performance"): MuJoCo's own developers found MuJoCo to have "the best performance out of all engines" vs. Bullet, ODE, PhysX, especially with many joints/links, by comparing time-to-simulation-error (cited work [20]); a separate cited study ([33]) compared real-time factor (RTF) for Gazebo, MuJoCo, PyBullet, Webots and found "MuJoCo was reported to have a high RTF across scenarios, at the cost of some accuracy," PyBullet "achieved a lower RTF but was highlighted for its superior usability," Webots showed "high stability and RTF even in the most complex scenarios but is criticized for its lack of native parallelization support," and Gazebo was "found to be unwieldy." No absolute FPS/step-rate numbers are quoted from any of the cited sources.

## Evaluation
- metrics: citation-count popularity (overall and ML-related), and feature/usability ratings (Table II) derived by the authors from documentation and prior work — not a runtime benchmark.
- full comparison conclusions (Sec. VI, Conclusion):
  - **MuJoCo**: "currently the dominant framework for RL research due to its good performance and flexibility," best MARL foundation "due to its high simulation fidelity and high training efficiency," but "documentation is sometimes lacking" and "creation of complex training environments ... can be comparatively strenuous."
  - **PyBullet**: "offers similar features and usability as MuJoCo, but consistently rates worse in performance reviews" (citing [20],[33],[38]); compensates with "a wide range of dedicated functions for loading and defining objects and models."
  - **Unity**: easiest environment design of all frameworks reviewed, but "not optimized for parallel computing and large-scale training"; strong for video-game-style single/simple multi-agent scenarios, weak for scaling complexity/fidelity.
  - **Brax**: "fails to impress, due to its limited available resources and documentation and poor multi-agent performance" — scaling agent count "reaches a standstill" after a low threshold (citing [10]); its main selling point (GPU/TPU) is "also offered by PhysX/IsaacGym with a better feature range and usability."
  - **PhysX/IsaacGym**: "excels in terms of usability and provides a unified framework for scenario creation, simulation, and RL," but GPU-driven simulation "can be disadvantageous for large-scale RL research" when the GPU must be dedicated to the learning algorithm.
  - **ODE**: "outdated both in terms of feature range and usability and accordingly has limited impact on current RL research."
  - **Chrono**: "lacks important features such as URDF and MJCF support."
  - **Gazebo and Webots**: "represent powerful tools for high-fidelity simulation robotics with decent usability. However, both are not geared towards MARL applications."
  - **Cross-engine transfer** (cited work [38]): "MuJoCo is better than PyBullet and ODE at generalizing learning to other engines ... Agents trained via PyBullet did not transfer their learning at all."
  - **Overall symptom named by the authors**: "the most performant engine (MuJoCo) has poor usability and the most user-friendly engine (Unity) suffers from poor performance. For significant progress in the field, a better combination of the best of the two worlds has to be achieved." (Sec. VI)
- baselines beaten: not applicable (no runtime experiment; qualitative ranking only, per engine and per usability axis in Table II).
- real robot? none.

## Limitations stated by the authors
- No original quantitative benchmark was run across engines: "the performance evaluation is neither exhaustive nor compares all frameworks on equal footing ... the evaluation might be skewed by the availability of data on the engines" (Sec. V).
- "A general and systematic review of the underlying engines, particularly one that also considers capabilities for multi-agent reinforcement learning (MARL) research, is missing" is the gap the paper claims to fill, implying prior reviews (including their own citations) had similar scope limits (Sec. I).
- No technical training-performance comparison exists in the literature for MARL in complex 3D environments across engines, "a research gap" the authors flag rather than close (Sec. VI).

## Quotable claims (verbatim, with section)
- "MuJoCo is currently the dominant framework for RL research due to its good performance and flexibility, even though its documentation is sometimes lacking." (Abstract)
- "Symptomatic for the field, the most performant engine (MuJoCo) has poor usability and the most user-friendly engine (Unity) suffers from poor performance." (Sec. VI)
- "PhysX might be more of a specialized tool for robotics RL and less suitable to basic RL research." (Sec. III-B.5)
- "There is no reason to handle the usability inconveniences of MuJoCo if it is sufficient to have a MARL setup in 2D." (Sec. VI)

## Notes for the survey
- This paper is a documentation/usability survey, not a physics-fidelity benchmark; every throughput or accuracy claim it makes is second-hand (cited from other papers, none of which are independently parsed in this corpus at the numeric level) — the survey should not quote its "MuJoCo is fastest" line as an independent measurement, only as a review-of-reviews consensus.
- Table II (feature/usability matrix) is the most citable artifact here: it is useful for a "which engine has X" appendix table but says nothing about contact-model correctness, which `contact_models_comparison_2023` covers instead.
- No dexterous-hand or tactile content anywhere in this paper; it is included in the corpus purely for the general physics-engine landscape section of the survey.
- No code manifest exists for this entry (`github: null` in the bib record) — the note above is paper-only.
