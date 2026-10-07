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
Fifty-four of the 113 method papers here train this way, 35 of them in Isaac Gym, and 23
distill a student from the teacher. In-hand cube reorientation is the recipe's benchmark,
inherited from `openai_dexterity_2018` and still the task a new method is expected to show.

A second branch is growing underneath it and inverts the dependency. Instead of a simulator and
a reward it takes human demonstrations through a teleoperation rig and fits a policy directly:
18 vision-language-action models, 14 diffusion policies, and 14 papers whose contribution is
the collection apparatus itself. It is the newer literature, most of it from the last two
years, and it trades the reward-design problem for a data-collection problem. Whether it
displaces the simulator pipeline or ends up feeding it is the question this corpus cannot
settle, but the growth is the most visible trend in it.

Both branches run on remarkably little hardware. Of the 33 hands with a documented
specification here, four carry almost every experiment: the Allegro at 35 method papers, a
Shadow or Adroit model at 21, the Inspire RH56 family at 19, and LEAP at 12. Eight further
hands can be bought today or built from published designs and appear in the experiments of
none. That is not a manufacturing lag, since the hardware exists and is purchasable, and
section 3 takes it up: a field whose results rest on four platforms is more fragile than its
publication volume suggests.

What this literature cannot currently do is compare its own results. Ninety-nine of the 113
methods state a success criterion, but they are not the same criterion, and only 70 say how
many trials a reported rate rests on. The criteria run from never dropping the object to
reaching a pose within a tolerance each paper picks for itself. Two success rates from two
papers on nominally the same task are usually not measuring the same event, and none of the
surveys preceding this one supplies a protocol that would make them comparable. Section 7
derives one, with the trial counts a stated confidence interval actually requires.

Every claim in this survey is traceable to a source. Two hundred and twenty-one bibliography
entries were collected, 218 of them read into a structured record under a fixed template, with
every value quoted from the source it came from and that source named. The counts printed here
are recomputed from those records when the paper is built. Where a source is silent the record
says so, which is why the coverage statistics in this paper are floors and not rates. The same
discipline extended to released code: where a method published a repository, its reward was
read from the repository as well as from the paper. Reading an implementation against its own
description is established practice outside robotics, in repeatability and reproducibility
studies `collberg_repeatability_2016` `raff_reproducibility_2019`, in audits of how
implementation detail moves reinforcement-learning results
`engstrom_implementation_matters_2020`, in reward-design review `knox_reward_misdesign_2023`,
in benchmark re-releases `metaworld_plus_2025`, and most directly in recent work on paper-code
alignment `scicoqa_2026` `biocon_2026`. We are aware of none that does it for a robotics
field's released reward functions, and section 5.6 reports what this one found.

The scope is single-hand and bimanual multi-fingered manipulation under learned control.
Parallel-jaw work enters as a comparison and not as a subject. Two limits apply to every number
here. This is a corpus of the learned era, which is a selection effect rather than a judgment
on the analytic tradition; and a value this survey failed to extract is indistinguishable in
the counts from a value its source never stated.

Figure 1 puts the field on one page. What follows works outward from the task: the task
families, what makes them hard, and the terms used throughout (section 2), the hands and their
sensing (section 3), the simulators and what they expose (section 4), how policies are trained
(section 5), what changes with two hands (section 6), and how any of it is evaluated (section
7). Section 8 states what the corpus supports and what it does not. Appendix A gives the method
and the corpus, Appendix B the hardware and engine tables, Appendix C every paper-against-code
comparison in full, Appendix D the coding of the fourteen surveys that precede this one, and
Appendix E the derivation behind every count in the protocol.