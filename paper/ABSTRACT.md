## Abstract

A dexterous hand can change an object's pose without setting it down. This survey covers 112
learning-based methods that attempt it, the hands they run on, the simulators they train in,
and how they report results. The field has largely converged on one recipe: reinforcement
learning on privileged state in a GPU simulator, distilled into a vision-only student for
transfer to hardware. Fifty-three of the 112 methods train with reinforcement learning, 35 of
those in Isaac Gym against 7 on its successors, and 23 distill. A second and faster-growing
branch learns from teleoperated demonstration instead: 18 vision-language-action models, 14
diffusion policies, and 14 whose contribution is the collection rig. Work tripled between 2022
and 2024. Tasks concentrate on grasping, 57 of the 112, and in-hand reorientation, 31, with
bimanual coordination at 43 rising fastest, and almost every experiment runs on one of four
hands. What the survey adds comes from reading released code and vendor specifications beside
the papers. Eight hands that can be bought or built from published designs appear in no method
paper here. No closed-loop policy in the corpus reports how far its hand passes into the object
it holds, which a position-only success criterion cannot see. Section VII proposes a protocol
for the unreported quantities.
