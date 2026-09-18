## Appendix D. The existing surveys, and what each covers

Fourteen corpus entries are themselves surveys or engine-comparison studies. Table 10 sets them on
one set of columns. The columns record what each work covers, not how well. Section 1 states what
this survey adds over them and does not repeat the comparison here.

`an_dexil_survey_2025` is the closest in subject, covering imitation learning for multi-fingered
hands by learning family, end-effector class and demonstration source. It gives reinforcement
learning no taxonomy, treats bimanual work as a single "multi-agent" subsection, compares no
simulator, and defines no evaluation metric. `welte_iil_survey_2025` finds only seven dexterous
works that use interactive imitation learning and carries a fifteen-hand commercial table, with no
bimanual section, no benchmark table and no contact modelling. `zhao_sim2real_survey_2020`
supplies the standard sim-to-real split and predates GPU-parallel simulation.
`firoozi_foundation_models_2023` has zero occurrences of bimanual, tactile or in-hand.

`bai_unified_manip_survey_2025` spans all of manipulation across 212 pages. Its Sec. 4.3 on
dexterous manipulation runs about 720 words, the third longest of its ten task subsections behind
grasping and quadrupedal manipulation, which is a real treatment and not a passing mention. The
difference is elsewhere. Its Sec. 1.2 lists dexterous manipulation among the topics that "existing
surveys" cover from "narrower perspectives" and defers it to two of them.

`zhao_dexhand_survey_2026` is the most recent hand-centred survey, with a 29-hand anatomy table
and a task-by-paradigm taxonomy. Its Sec. IV-C names the reference-versus-rollout split that
Section 1 credits it with, and its Sec. III-F is the one bimanual subsection, 16 cited works with
no coordination analysis.

`nine_physics_engines_review_2024` is the predecessor closest to the engine comparison, and it
reviews Brax, Chrono, Gazebo, MuJoCo, ODE, PhysX, PyBullet, Unity and Webots for reinforcement
learning research. It scores each on documentation, model and environment creation, URDF and MJCF
support, and readiness for multi-agent work. It runs no benchmark of its own and says so in its
Sec. V, that implementing the same scenarios across nine engines "goes beyond the scope of this
paper". Its running bodies are ant-and-humanoid RL benchmarks rather than hands, and it discusses
no timestep, no friction model, no contact formulation and no penetration.

{{table:table10_surveys}}

Table 10's last rows carry the cost of the corpus. `okamura_overview_2000`, `piazza_century_2019`
and `roa_suarez_grasp_quality_2015` are behind publisher paywalls with no author-hosted copy found
on 2026-09-18, and `bicchi_hands_2000` is in the same position with no row at all.
`ma_dollar_dexterity_2011` is a different case. The fetch that failed when its note was written
succeeded afterwards, so a seven-page PDF is on disk with a recorded hash, and no note has been
read from it. All five are cited by metadata only and nothing in this survey describes their
contents. The open chapter `bicchi_grasping_chapter_2001` overlaps the paywalled Bicchi paper
without being identical to it, so it is quoted in its own right.
