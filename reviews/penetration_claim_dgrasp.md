# The interpenetration claim against D-Grasp

Date: 2026-10-06. Trigger: `~/projects/_ops/briefs/survey.md` item 1.

## What the survey claimed

Headline finding 2, in the abstract, section 1, section 7.2 and the conclusion:
no closed-loop policy in the corpus reports interpenetration for the rollouts of
its own trained policy, and all eleven rows that handle penetration at all sit on
the reference side of the reference-versus-rollout split.

## What D-Grasp reports

D-Grasp (Christen, Kocabas, Aksan, Song, Hilliges; CVPR 2022; arXiv 2112.03028)
trains a PPO grasping policy in a physics simulation and reports, in Table 1, a
metric headed `Interpenetration [cm3]`. For the three DexYCB rows the values are
GT+PD 4.41, GT+IK 9.08, Ours 1.74 cm^3, beside `SimDist [mm/s]` of 13.7, 11.7 and
9.0 and success rates 0.30, 0.38, 0.56.

Three verbatim statements fix what the number is:

- "We evaluate physical plausibility of a grasp in terms of stability and
  interpenetration on a set of unseen grasp labels and unseen objects."
- "Interpenetration: We calculate the amount of hand volume that penetrates the
  object. To do so, we use the original MANO mesh and the high-resolution object
  mesh. Hence, there is no physical simulation involved when measuring
  interpenetration." (appendix)
- "We note that our method achieves 0 interpenetration loss when evaluated in the
  physics simulation. In Tab. 1, however, we report interpenetration on the
  original MANO hand model and detailed object meshes. For computational
  efficiency during training, the hand model and the object meshes are simplified
  in the physics simulation, limiting the performance of our model when evaluated
  in the original setting."

## Verdict

The claim as written does not survive. D-Grasp is a closed-loop reinforcement
learning policy and it reports a penetration volume computed on poses its own
policy produced, not on an input reference. The survey's sentence is literally
true only because it is scoped to "in the corpus" and D-Grasp has no corpus row,
while the corpus's own ArtiGrasp note cites D-Grasp as a baseline and quotes
ArtiGrasp declining the same metric: "We omit the interpenetration metric since
all of our baselines include a physics simulation which exhibits no
interpenetration" (`papers/notes/artigrasp_2023.md`, line 25). A reader who
follows that note reaches D-Grasp in one step. Keeping the claim behind a corpus
boundary that excludes the counterexample is not defensible.

## What is true instead, and is a sharper finding

D-Grasp measures the quantity twice and the two numbers disagree by construction:
zero inside the physics simulation, because the simulated meshes are simplified
for speed, and 1.74 cm^3 when the policy's output pose is re-measured against the
original MANO and full-resolution object meshes with no physics involved. So the
number a reader would want, how far the hand sinks into the object in the physics
that trained the policy, is zero by construction, and the number actually
reported is a geometric re-measurement on different geometry than the policy ever
saw. That is a statement about what the measurement can mean, and it survives the
counterexample instead of being refuted by it.

## Consequence for the paper

Restate the claim along those lines, or drop it. Add a D-Grasp row to the corpus.
Search the corpus for other closed-loop policies reporting a rollout penetration
number before restating, since one counterexample found this way implies the
search was never done.

## The systematic search the brief asked for

Run 2026-10-06 over all 96 method notes mentioning a penetration quantity
(`papers/notes/*.md`), looking for a reported number rather than a reward term or
a passing mention. Result: every corpus paper that reports penetration as a
metric measures it on a reference, not on a policy's rollouts.

| row | field | what it reports |
|---|---|---|
| `toporetarget_2026` | constrained | max depth in mm and share of frames over 2 mm, on retargeted references |
| `dextrack_2025` | measured | max depth over frames, on the input kinematic reference |
| `bidexgrasp_2026` | measured | Penetration Depth and Self-Penetration Depth, grasp synthesis |
| `unidexgrasp_2023` | penalised | object penetration depth in Table 1 and Table 2, a proposal-quality metric, "not a reward term for the execution policy" |
| `teledexter_2026` | penalised | L_pen on hand-object mesh interpenetration, inside the retargeting pipeline |
| `bimangrasp_2024` | penalised | a 1.5 mm hard gate, no number reported |
| `omnigrasp_2024` | not addressed | declines the metric explicitly, with a stated rationale |
| `graspxl_2024` | not addressed | 35 human raters score realism, one dimension of which is interpenetration |

`unidexgrasp_2023` was the one worth checking closely, because it is an RL plus
distillation row whose note says penetration depth is reported in Table 1 and
Table 2. It is not a counterexample: Table 1 is proposal generation and the note
records that the metric "is not a reward term for the execution policy". The
corpus classification was right.

So the corpus claim held and the headline was still wrong, because the headline
generalised past the corpus and the one counterexample sits just outside it,
reachable in one step from the corpus's own ArtiGrasp note. The fix was to stop
claiming a null and report what the measurement actually is.
