### Table 9. The matrix, for someone else to fill

| method | task success (rate &plusmn; Wilson 95, n) | robustness (per-axis rate &plusmn; Wilson 95, n; ratio to anchor) | unseen objects (mean per-object rate, bootstrap 95, k objects) | plausibility (max / mean mm, frac frames > 2 mm) | cost (env steps, GPU-h, 3-seed range) | transfer (&rho; [lo, hi], rectifier var / real var) | reproducibility (file:line of each disagreement, or none) |
|---|---|---|---|---|---|---|---|
| *worked example &mdash; every number fabricated* | 0.72 &plusmn; 0.09 (100) | lighting 0.41 &plusmn; 0.15 (40), ratio 0.57; anchor 0.72 &plusmn; 0.09 (100) | 0.55, [0.41, 0.68], 20 objects | 3.1 / 0.8 mm, 0.12 | 1.2e9 steps, 46 GPU-h, 0.68&ndash;0.74 | 0.61 [0.47, 0.72], 0.43 | `cfg/train.yaml:88` orient weight 0.0 vs paper 0.5 |
| `openai_dexterity_2018`&#10035; | | | | | | | |
| `dexmv_2021` | | | | | | | |
| `dapg_2017`&#10035; | | | | | | | |
| `dextreme_2022` | | | | | | | |
| `dexcap_2024` | | | | | | | |
| `hora_2022`&#10035; | | | | | | | |
| `visual_dexterity_2022`&#10035; | | | | | | | |
| `rotating_without_seeing_2023`&#10035; | | | | | | | |
| `unidexgrasp_2023` | | | | | | | |
| `pddm_2019`&#10035; | | | | | | | |
| `hato_visuotactile_2024`&#10035; | | | | | | | |
| `dexpoint_2022` | | | | | | | |

*12 rows, 84 cells, all 84 empty; the first row is a worked example and every number in it is fabricated. Rows are the 12 most-mentioned dexterous-hand policy methods in the corpus, by the rule in §7.4, scored on whole-word matches over `papers/md`: `openai_dexterity_2018` 64; `dexmv_2021` 50; `dapg_2017` 49; `dextreme_2022` 44; `dexcap_2024` 40; `hora_2022` 34; `visual_dexterity_2022` 32; `rotating_without_seeing_2023` 27; `unidexgrasp_2023` 27; `pddm_2019` 25; `hato_visuotactile_2024` 23; `dexpoint_2022` 22. Mention counts are counts of mentions, not of use. &#10035; marks a work matched on its title rather than a short name; a title is matched mostly inside reference lists and a short name in running text, so the two kinds of count are not comparable with each other.*
