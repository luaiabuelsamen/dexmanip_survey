### Table 5. Reward terms across in-hand reorientation methods

| method | yr | goal or rotation tracking | object velocity | finger-object distance | hand-pose deviation | action rate or magnitude | torque, work or joint velocity | drop or failure | contact or force | success bonus | terms | code | paper/code mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `openai_dexterity_2018` | 2018 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `openai_rubiks_cube_2019` | 2019 | paper |   |   |   |   |   | paper |   | paper | 3 | no |   |
| `dextreme_2022` | 2022 | both |   |   |   | both | both | code (0) |   | both | 6 | yes | yes |
| `hora_2022` | 2022 | both | both |   | both |   | both |   |   |   | 5 | yes | yes |
| `visual_dexterity_2022` | 2022 | both |   | both | paper |   | both | both | paper | both | 7 | yes | yes |
| `dexpbt_2023` | 2023 | both |   | both |   | code | paper | code (0) |   | both | 4 | yes | yes |
| `eureka_2023` | 2023 | paper | paper | paper |   |   |   |   |   |   |   | yes | yes |
| `robot_synesthesia_2023` | 2023 | paper | paper | paper |   | paper | paper | paper |   |   | 6 | no |   |
| `rotateit_2023` | 2023 | paper | paper |   | paper |   | paper |   |   |   | 6 |   |   |
| `rotating_without_seeing_2023` | 2023 | paper | paper | paper |   |   | paper | paper |   |   | 6 |   |   |
| `anyrotate_2024` | 2024 | paper | paper |   | paper |   | paper | paper | paper | paper | 10 | no |   |
| `demostart_2024` | 2024 |   |   |   |   |   |   |   |   | paper | 1 | no |   |
| `dreureka_2024` | 2024 | paper | paper |   | paper |   |   | paper |   |   | 4 | yes | yes |
| `penspin_2024` | 2024 | both | both |   | both | code (0) | both |   |   |   | 7 | yes | yes |
| `dexndm_2025` | 2025 | paper | paper |   | paper |   | paper |   |   | paper | 7 | no |   |
| `dexremoe_2025` | 2025 | paper | paper |   |   | paper |   |   |   | paper | 5 | no |   |
| `dexteritygen_2025` | 2025 |   |   |   |   |   |   |   |   |   |   | no |   |
| `force_grasp_sim2real_2026` | 2026 | paper |   |   | paper | paper | paper | paper | paper | paper | 7 | no |   |
| `poise_2026` | 2026 | paper |   |   |   |   | paper | paper | paper | paper | 4 | no |   |
| `teledexter_2026` | 2026 | paper |   |   |   |   |   |   |   | paper |   | no |   |
| `viserdex_2026` | 2026 | paper | paper |   |   | paper | paper | paper |   | paper | 10 | no |   |

*21 rows; 97 of 189 term cells (51%) are families the method does not use. `paper` means the term is in the paper and either no code was released or it is absent from the released reward code; `code` means it is in the released code and not in the paper's stated reward; `both` means it is in both. Marks are read from papers/notes/, term by term; the per-method source section is in corpus/reward_matrix.json.*