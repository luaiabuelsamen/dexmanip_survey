# 1. Introduction

{{figure:fig1_field}}

A hand is dexterous when it can change an object's pose without putting the object down. That
property, and not the finger count, is what separates a hand from a gripper.
`bicchi_grasping_chapter_2001` draws the same line in Sec. 1.1 between restraining an object
and manipulating it with the fingers: restraint is a static question about whether the contacts
prevent motion, while in-hand manipulation is a dynamic one about whether contacts can be
broken and remade while the object stays held. A parallel-jaw gripper can hold almost anything
and reorient almost nothing.

The classical theory of grasping is about holding, and it is good at it. Given a set of contact
points and an assumption about friction, it can decide whether an object is immobilized, and
what force each finger has to apply to keep it that way. What it cannot do is say what the
fingers should do next. Contact is what makes that hard: a finger is either touching or it is
not, and it can push but not pull, so the equations of motion change form every time a contact
is made or broken. The standard treatment says as much about its own results, that immobilizing
an object "does not guarantee stability", and that "the nonsmooth nature of grasp dynamics,
because of the unilateral constraints on displacements and forces, has made a thorough analysis
very difficult" (`bicchi_grasping_chapter_2001`, Sec. 1.5 and 1.8). The tradition produced
tests. You can check a candidate grasp against them; you cannot run them on a robot.

Learning changed what a practitioner has to produce. The old deliverable was a proof that a
configuration holds. The new one is a policy that scores well over many simulated attempts,
which means the simulator now stands in for the analysis and the score stands in for the proof.
That is why the field moved, and it is also why this survey is organized as it is. It shifts
two burdens onto the author. The simulator has to be faithful where fidelity matters. The
measurement has to mean something. Much of what follows asks how well this literature carries
those two.

One recipe now carries most of the field. Train a policy with reinforcement learning on
privileged state, the object pose, velocities and physical parameters the robot cannot sense,
in a GPU simulator running thousands of environments in parallel; distill that teacher into a
student that sees only what a camera and joint encoders provide; transfer the student.
Fifty-four of the 113 method papers here train this way, most of them in one simulator, and
about half of those add the distillation stage. In-hand cube reorientation is the recipe's
benchmark, inherited from `openai_dexterity_2018` and still the task a new method is expected to
show.

A second branch is growing underneath it and inverts the dependency. Instead of a simulator and
a reward it takes human demonstrations through a teleoperation rig and fits a policy directly,
as a vision-language-action model, a diffusion policy, or a data-collection rig whose design is
itself the contribution. Section 5 counts them; Figure 1 shows how fast they have arrived. It is
the newer literature, most of it from the last two years, and it trades the reward-design problem
for a data-collection problem. Which of the two branches ends up feeding the other is not settled
here, but the growth is the clearest trend in the corpus.

Both branches run on remarkably little hardware. Four hands carry almost every experiment in
this corpus, led by the Allegro at 35 of the 113 papers; Figure 2 gives the rest of the
distribution. Eight further hands can be bought today or built from published designs and appear
in the experiments of none of them. The hardware exists and is purchasable, so this is not a
manufacturing lag, and section 3 takes it up: a field whose results rest on four platforms is
more fragile than its publication volume suggests.

What this literature cannot currently do is compare its own results. Nearly every paper states
a success criterion, but they are not the same criterion, and only 70 of the 113 say how many
trials a reported rate rests on. The criteria run from never dropping the object to
reaching a pose within a tolerance each paper picks for itself. Two success rates from two
papers on nominally the same task are usually not measuring the same event, and none of the
surveys preceding this one supplies a protocol that would make them comparable. Section 7
derives one, with the trial counts a stated confidence interval actually requires.

Every number in this survey is traceable to a source, and every count in it is recomputed from
those sources rather than typed in. Appendix A says how the corpus was built, what the method
cannot do, and why each coverage figure here should be read as a floor rather than a rate.

One part of that method is unusual enough to flag now. Where a paper published a repository, its
reward was read from the repository as well as from the paper, so the two can be compared.
Reading an implementation against its own description is established practice outside robotics,
in repeatability and reproducibility studies `collberg_repeatability_2016`
`raff_reproducibility_2019`, in audits of how implementation detail moves reinforcement-learning
results `engstrom_implementation_matters_2020`, in reward-design review
`knox_reward_misdesign_2023`, in benchmark re-releases `metaworld_plus_2025`, and most directly
in recent work on paper-code alignment `scicoqa_2026` `biocon_2026`. We are aware of none that
does it for a robotics field's released reward functions. Section 5.6 reports what this one
found.

The scope is single-hand and bimanual multi-fingered manipulation under learned control.
Parallel-jaw work enters as a comparison and not as a subject. Two limits apply to every number
here. The corpus is of the learned era, which is a selection and not a verdict on the analytic
tradition; and where this survey failed to extract a value, the counts look the same as if the
source had never stated one.

## 1.1 How to read this survey

Figure 1 puts the field on one page, and the sections work outward from the task. Section 2 sets
out the task families, what makes each one hard, and the handful of terms this survey uses
precisely. Section 3 covers the hands and their sensing, section 4 the simulators and what they
expose about contact, section 5 how policies are actually trained, section 6 what changes when
there are two hands, and section 7 how any of it is evaluated. Section 8 says what the corpus
supports and what it does not. The appendices hold the method and the full tabulation: A the
method and its limits, B the hardware and engine tables, C every paper-against-code comparison,
D the surveys that precede this one, E the derivation behind the protocol.

If you are new to the field, read section 2 for the vocabulary, then the first half of section 5
for the two ways a dexterous policy gets trained, then section 3 to see what hardware any of it
runs on. Those three give the shape of the field in about half an hour. Section 7 is the one to
read before designing an experiment, because it is about what the field's numbers do and do not
mean.

If you already work here, the sections that are likely to tell you something you did not know
are 4.2 on what simulators expose about contact, 5.6 on papers against their own released code,
6 on bimanual work as its own problem rather than two single hands, and 7.3 on what a success
rate at twenty trials can support.

If you want the data rather than the prose, every table is generated from the corpus and every
number in the text is recomputed from it at build time. Table 7 is the paper-by-paper
tabulation, Tables 2 and 3 the hands, Table 4 the simulators, and the appendices hold the rest.

Three things to carry while reading. The corpus is of the learned era, which is a selection and
not a verdict on the analytic tradition that preceded it. Every coverage figure is a floor: when
a paper is silent and when this survey failed to extract a value, the counts look the same, and
Appendix A says which direction that bias runs. And a success rate in this literature is rarely
comparable across two papers, for reasons section 7 sets out, so prefer the sections that explain
mechanisms to any ranking you could assemble from the numbers.