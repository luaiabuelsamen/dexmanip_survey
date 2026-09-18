<!-- page 1 (ocr) -->
DexPBT: Scaling up Dexterous Manipulation for
Hand-Arm Systems with Population Based Training
Aleksei Petrenko, Arthur Allshire, Gavriel State, Ankur Handa, Viktor Makoviychuk
Fig. 1: Tasks trained with DexPBT. Left-to-right: regrasping, throwing, single-handed reorientation, two-handed reorientation.
Abstract—In this work, we propose algorithms and methods
that enable learning dexterous object manipulation using sim-
ulated one- or two-armed robots equipped with multi-fingered
hand end-effectors. Using a parallel GPU-accelerated physics
simulator (Isaac Gym), we implement challenging tasks for these
robots, including regrasping, grasp-and-throw, and object reori-
entation. To solve these problems we introduce a decentralized
Population-Based Training (PBT) algorithm that allows us to
massively amplify the exploration capabilities of deep reinforce-
ment learning. We find that this method significantly outperforms
regular end-to-end learning and is able to discover robust control
policies in challenging tasks. Video demonstrations of learned
behaviors and the code can be found at the supplementary
website.
I. INTRODUCTION
In recent years researchers have started to apply deep
reinforcement learning methods in an increasing number of chal-
lenging continuous control domains. Some applications include
impressive demonstrations of skill in virtual environments, such
as playing football by directly controlling humanoid characters
using joint torques [22]. In other domains such as agile drone
flight [37, 28, 4] and quadruped locomotion [17, 27], control
policies trained in simulation are deployed directly on the real
hardware.
Learning-based approaches appear to be particularly promis-
ing in the domain of robotic manipulation. Traditional methods
such as direct trajectory optimization, may struggle to model
complex contact dynamics. Due to these difficulties, researchers
working on manipulation problems typically focus their efforts
on robotic arms with end-effectors that simplify contact
handling, such as parallel jaw grippers [5, 29, 26]. Even though
more capable human-like robotic hands have the potential to
endow robots with far more advanced manipulation capabilities,
this type of end-effector remains relatively unpopular due to the
difficulty of controlling high degree-of-freedom (DoF) systems
in contact-rich environments.
With the advent of modern deep RL methods that use a large
amount of data and computation, it has become possible to learn
control policies for multi-fingered robotic hands. Systems like
"Dactyl" [2, 31] and "DeXtreme" [10] have demonstrated how
large-scale reinforcement learning in simulation can be used to
obtain robust policies for complex in-hand object manipulation.
In this work, we extend this approach and apply it to a
fully actuated hand-arm system: a four finger 16-DoF Allegro
Hand mounted on a 7-DoF Kuka arm. We target a variety of
manipulation tasks in simulated environment Isaac Gym [24],
such as regrasping, throwing, and reorientation. We then scale
our learning method to train agents that control a pair of arms
and hands with combined 46 degrees of freedom using a single
neural network policy.
We observe that despite the relative success of straight-
forward end-to-end learning, our RL experiments are char-
acterized by a high variance of results and dependency on
initial conditions, especially in tasks that require exploration
in the vast space of possible behaviors. To that end, we
develop a Population-Based Training (PBT) algorithm [13],
an outer optimization loop that can significantly amplify the
exploration capabilities of end-to-end RL. In order to facilitate
asynchronous learning in a volatile compute environment we
implement a decentralized version of the PBT algorithm that
we can run without a central orchestrator instance and is robust
to the disconnect of one or a few learners. We find that the PBT
approach demonstrates improved performance in all scenarios
over standard end-to-end learning and becomes the enabling
factor for the successful training of ambidextrous agents that
control two hand-arm systems simultaneously.
Our contributions can be summarized as follows:
• We develop a framework that combines on-policy RL and
decentralized Population Based Training with realistic
GPU-accelerated robotic simulation and use this frame-
work to train policies for dexterous object manipulation
arXiv:2305.12127v1  [cs.RO]  20 May 2023
se
—
T= my —
p- — = _—
amy =
:
2
>
"4
x fi
A
| N-


<!-- page 2 (ocr) -->
<latexit sha1_base64="wWYRX+WPXbCv/x4O
SEvSL38VDqQ=">AC0XichVFLS8NAEJ7GV+uz6tFLsBQ8laSCeiz4wItQsS9oi2zSbQzNi2RbqE
UQr9686h/T3+LBb9dU0CLdsJnZb75dmbHijw3EYbxntEWFpeWV7K51bX1jc2t/PZOIwmHsc3rd
uiFctiCfcgNeFKzeimLOfMvjTWtwKuPNEY8TNwxqYhzxrs+cwO27NhOAWrUw0g+NTvE2XzBKh
lr6rGOmToHSVQ3zH9ShHoVk05B84hSQgO8RowRfm0wyKALWpQmwGJ6r4pweaBW5Q7A4GAzoAH8H
p3aKBjhLzURl27jFw46RqVMR+0IpWmDLWzn8BPYT+15hzr83TJSyrHAMa0ExpxSvgAu6A2Nep8y
p7XMz5RdCerTierGRX2RQmSf9o/OGSIxsIGK6HSumA40LHUe4QUC2DoqkK8VdBVxz1YpixXKkG
qyKAXw8rXRz0Ys/l3qLNOo1wyj0rl63KhYqQDz9Ie7dMBpnpMFbqkKuqQ03yhV3rTbrSx9qg9fVO
1TJqzS7+W9vwFSyeRAQ=</latexit>Top 30%
<latexit sha1_base64="wWYRX+WPXbCv/x4O
SEvSL38VDqQ=">AC0XichVFLS8NAEJ7GV+uz6tFLsBQ8laSCeiz4wItQsS9oi2zSbQzNi2RbqE
UQr9686h/T3+LBb9dU0CLdsJnZb75dmbHijw3EYbxntEWFpeWV7K51bX1jc2t/PZOIwmHsc3rd
uiFctiCfcgNeFKzeimLOfMvjTWtwKuPNEY8TNwxqYhzxrs+cwO27NhOAWrUw0g+NTvE2XzBKh
lr6rGOmToHSVQ3zH9ShHoVk05B84hSQgO8RowRfm0wyKALWpQmwGJ6r4pweaBW5Q7A4GAzoAH8H
p3aKBjhLzURl27jFw46RqVMR+0IpWmDLWzn8BPYT+15hzr83TJSyrHAMa0ExpxSvgAu6A2Nep8y
p7XMz5RdCerTierGRX2RQmSf9o/OGSIxsIGK6HSumA40LHUe4QUC2DoqkK8VdBVxz1YpixXKkG
qyKAXw8rXRz0Ys/l3qLNOo1wyj0rl63KhYqQDz9Ie7dMBpnpMFbqkKuqQ03yhV3rTbrSx9qg9fVO
1TJqzS7+W9vwFSyeRAQ=</latexit>Top 30%
<latexit sha1_base64="aLlmioF4cz2yBMnM
mdeQaJ/pNiw=">AC0XichVFLS8NAEJ7GV+uz6tFLsBQ8laSIeiz4wEuhon1AWyRJt3FpXmzSQi
2CePXmVf+Y/hYPfrumghbphs3MfvPNtzM7duTxODGM94y2sLi0vJLNra6tb2xu5bd3GnE4FA6rO
6EXipZtxczjAasnPFYKxLM8m2PNe3BqYw3R0zEPAxuknHEur7lBrzPHSsB1Kryn5odIq3+YJRM
tTSZx0zdQqUrlqY/6AO9Sgkh4bkE6OAEvgeWRTja5NJBkXAujQBJuBxFWf0QKvIHYLFwLCADvB3
cWqnaICz1IxVtoNbPGyBTJ2K2BdK0QZb3srgx7Cf2PcKc/+9YaKUZYVjWBuKOaVYBZ7QHRjzMv2U
Oa1lfqbsKqE+nahuOqLFCL7dH50zhARwAYqotO5YrQsNV5hBcIYOuoQL7yVEFXHfdgLWZUgl
SRQt6Ala+PurBmM2/Q51GuWSeVQqX5ULFSMdeJb2aJ8OMNVjqtAl1VCHnOYLvdKbdq2NtUft6Zu
qZdKcXfq1tOcvEQmQ6Q=</latexit>Mid 40%
<latexit sha1_base64="aLlmioF4cz2yBMnM
mdeQaJ/pNiw=">AC0XichVFLS8NAEJ7GV+uz6tFLsBQ8laSIeiz4wEuhon1AWyRJt3FpXmzSQi
2CePXmVf+Y/hYPfrumghbphs3MfvPNtzM7duTxODGM94y2sLi0vJLNra6tb2xu5bd3GnE4FA6rO
6EXipZtxczjAasnPFYKxLM8m2PNe3BqYw3R0zEPAxuknHEur7lBrzPHSsB1Kryn5odIq3+YJRM
tTSZx0zdQqUrlqY/6AO9Sgkh4bkE6OAEvgeWRTja5NJBkXAujQBJuBxFWf0QKvIHYLFwLCADvB3
cWqnaICz1IxVtoNbPGyBTJ2K2BdK0QZb3srgx7Cf2PcKc/+9YaKUZYVjWBuKOaVYBZ7QHRjzMv2U
Oa1lfqbsKqE+nahuOqLFCL7dH50zhARwAYqotO5YrQsNV5hBcIYOuoQL7yVEFXHfdgLWZUgl
SRQt6Ala+PurBmM2/Q51GuWSeVQqX5ULFSMdeJb2aJ8OMNVjqtAl1VCHnOYLvdKbdq2NtUft6Zu
qZdKcXfq1tOcvEQmQ6Q=</latexit>Mid 40%
<latexit sha1_base64="2nyu5pspGNeBtz7D
RHCdRt3j2/c=">AC1HichVFLS8NAEJ7GV1tfVY9egqXgqSQV1GPxhRehgn1AWyRJ1xiaF5toV
ZP4tWbV/1d+ls8+O2aClqkGzYz+80387s2LHvJcIw3jPa3PzC4lI2l19eWV1bL2xsNpJowB1Wd
yI/4i3bSpjvhawuPOGzVsyZFdg+a9r9YxlvDhlPvCi8EqOYdQPLDb0bz7EoPZRJEQU6HtGp3RdK
BplQy192jFTp0jpqkWFD+pQjyJyaEABMQpJwPfJogRfm0wyKAbWpTEwDs9TcUYPlEfuACwGhgW0
j7+LUztFQ5ylZqKyHdziY3Nk6lTCPlOKNtjyVgY/gf3EvlOY+8NY6UsKxzB2lDMKcUL4IJuwZiV
GaTMS2zM2VXgm7oUHXjob5YIbJP50fnBEOrK8iOp0qpgsNW52HeIEQto4K5CtPFHTVcQ/WUpY
plTBVtKDHYeXrox6M2fw71GmnUSmb+XKZaVYNdKBZ2mbdmgXUz2gKp1TDXIubzQK71pDe1e9S
evqlaJs3Zol9Le/4CzA6SYQ=</latexit>Bottom 30%
<latexit sha1_base64="2nyu5pspGNeBtz7D
RHCdRt3j2/c=">AC1HichVFLS8NAEJ7GV1tfVY9egqXgqSQV1GPxhRehgn1AWyRJ1xiaF5toV
ZP4tWbV/1d+ls8+O2aClqkGzYz+80387s2LHvJcIw3jPa3PzC4lI2l19eWV1bL2xsNpJowB1Wd
yI/4i3bSpjvhawuPOGzVsyZFdg+a9r9YxlvDhlPvCi8EqOYdQPLDb0bz7EoPZRJEQU6HtGp3RdK
BplQy192jFTp0jpqkWFD+pQjyJyaEABMQpJwPfJogRfm0wyKAbWpTEwDs9TcUYPlEfuACwGhgW0
j7+LUztFQ5ylZqKyHdziY3Nk6lTCPlOKNtjyVgY/gf3EvlOY+8NY6UsKxzB2lDMKcUL4IJuwZiV
GaTMS2zM2VXgm7oUHXjob5YIbJP50fnBEOrK8iOp0qpgsNW52HeIEQto4K5CtPFHTVcQ/WUpY
plTBVtKDHYeXrox6M2fw71GmnUSmb+XKZaVYNdKBZ2mbdmgXUz2gKp1TDXIubzQK71pDe1e9S
evqlaJs3Zol9Le/4CzA6SYQ=</latexit>Bottom 30%
<latexit sha1_base64="ro4QyBpsEpTKzao7
j3q3aDglcpU=">AC0XichVFLS8NAEJ7GV1tfVY9egkXwVJIe1GPxhRehYl9Qi2zStS7Ni01aqE
UQr9686h/T3+LBb9dU0CLdsJnZb75dmbHiTwRJ5b1njHm5hcWl7K5/PLK6tp6YWOzEYcD6fK6G
3qhbDks5p4IeD0RicdbkeTMdzedPrHKt4chmLMKglo4h3fNYLxK1wWQKoVT2qmXzIvJtC0SpZe
pnTjp06RUpXNSx80DV1KSXBuQTp4AS+B4xivG1ySaLImAdGgOT8ISOc3qgPHIHYHEwGNA+/j2c
2ika4Kw0Y53t4hYPWyLTpF3sM63ogK1u5fBj2E/se431/r1hrJVhSNYB4o5rXgBPKE7MGZl+ilz
UsvsTNVQrd0qLsRqC/SiOrT/dE5QUQC6+uISaea2YOGo89DvEAW0cF6pUnCqbuAvLtOVaJUg
VGfQkrHp91IMx23+HOu0yiV7v1S+LBcrVjrwLG3TDu1hqgdUoXOqog41zRd6pTfjyhgZj8bTN9X
IpDlb9GsZz19oEZF4</latexit>PBT eval
<latexit sha1_base64="ro4QyBpsEpTKzao7
j3q3aDglcpU=">AC0XichVFLS8NAEJ7GV1tfVY9egkXwVJIe1GPxhRehYl9Qi2zStS7Ni01aqE
UQr9686h/T3+LBb9dU0CLdsJnZb75dmbHiTwRJ5b1njHm5hcWl7K5/PLK6tp6YWOzEYcD6fK6G
3qhbDks5p4IeD0RicdbkeTMdzedPrHKt4chmLMKglo4h3fNYLxK1wWQKoVT2qmXzIvJtC0SpZe
pnTjp06RUpXNSx80DV1KSXBuQTp4AS+B4xivG1ySaLImAdGgOT8ISOc3qgPHIHYHEwGNA+/j2c
2ika4Kw0Y53t4hYPWyLTpF3sM63ogK1u5fBj2E/se431/r1hrJVhSNYB4o5rXgBPKE7MGZl+ilz
UsvsTNVQrd0qLsRqC/SiOrT/dE5QUQC6+uISaea2YOGo89DvEAW0cF6pUnCqbuAvLtOVaJUg
VGfQkrHp91IMx23+HOu0yiV7v1S+LBcrVjrwLG3TDu1hqgdUoXOqog41zRd6pTfjyhgZj8bTN9X
IpDlb9GsZz19oEZF4</latexit>PBT eval
<latexit sha1_base64="GRFKNV4w76Vu7J0J
caefUj7ML/0=">AC03ichVFLT8JAEB7qC/CFevTSCacSMtBPZL4iBcSTCwQkZhtWpDX2m3JE
i8GK/evOr/0t/iwa9rMVFi3GY7s9/MfPMyQ9eJha95ZSFxaXlXyhuLq2vrFZ2tpux0ESWdywA
jeIuiaLuev43BCOcHk3jDjzTJd3zNFxau+MeRQ7gX8pJiHve8z2naFjMQHoqpkIJrhaCSs3pbJW0
+R5xU9U8qUnVZQeqdrGlBAFiXkESefBHSXGMX4eqSTRiGwPk2BRdAcaed0T0XEJvDi8GBAR/jb
ePUy1Mc75YxltIUsLm6ESJX2c8kownvNCuHkN+4N5JzP4zw1QypxVOIE0wFiRjE7igW3j8F+l
nrNa/o9MuxI0pCPZjYP6QomkfVrfPCewRMBG0qLSqfS0wWHK9xgT8CENVJBOecagyo4HkExKLln
8jJGBL4JMp496sGb91LnlXa9ph/U6hf1cqOaLTxPu7RHVWz1kBp0Ti3UYSHLM73Qq2IoU+VBefx
yVXJZzA79OMrTJyswkh4=</latexit>Mutate p
<latexit sha1_base64="GRFKNV4w76Vu7J0J
caefUj7ML/0=">AC03ichVFLT8JAEB7qC/CFevTSCacSMtBPZL4iBcSTCwQkZhtWpDX2m3JE
i8GK/evOr/0t/iwa9rMVFi3GY7s9/MfPMyQ9eJha95ZSFxaXlXyhuLq2vrFZ2tpux0ESWdywA
jeIuiaLuev43BCOcHk3jDjzTJd3zNFxau+MeRQ7gX8pJiHve8z2naFjMQHoqpkIJrhaCSs3pbJW0
+R5xU9U8qUnVZQeqdrGlBAFiXkESefBHSXGMX4eqSTRiGwPk2BRdAcaed0T0XEJvDi8GBAR/jb
ePUy1Mc75YxltIUsLm6ESJX2c8kownvNCuHkN+4N5JzP4zw1QypxVOIE0wFiRjE7igW3j8F+l
nrNa/o9MuxI0pCPZjYP6QomkfVrfPCewRMBG0qLSqfS0wWHK9xgT8CENVJBOecagyo4HkExKLln
8jJGBL4JMp496sGb91LnlXa9ph/U6hf1cqOaLTxPu7RHVWz1kBp0Ti3UYSHLM73Qq2IoU+VBefx
yVXJZzA79OMrTJyswkh4=</latexit>Mutate p
<latexit sha1_base64="ef+ZTfWjz05j6iz
Rbe9SXtxMdA=">AC23ichVFLT8JAEB7qC/BV9eilEUw4kcJBPZL4iBcTNPJIgJBtWUpDX2kXEi
SevBmv3rzqf9Lf4sGvazFRYthmO7PfPtzI4ROHYkdP09pSwtr6yupTPZ9Y3NrW1Z7ce+aPQ5
DXTd/ywabCIO7bHa8IWDm8GIWeu4fCGMTyN40xDyPb927FJOAdl1me3bdNJgB1VfWGBw4zuZvi
wEXLN9Vc3pRl0ubd0qJk6NkVX31g9rUI59MGpFLnDwS8B1iFOFrUYl0CoB1aAoshGfLOKd7yiJ3
BYHgwEd4m/h1EpQD+dYM5LZJm5xsENkanSIfSEVDbDjWzn8CPYT+05i1r83TKVyXOE1oBiRipe
ARc0AGNRpswZ7Uszoy7EtSnE9mNjfoCicR9mj86Z4iEwIYyotG5ZFrQMOR5jBfwYGuoIH7lmYI
mO+7BMm5VPESRQa9EDZ+fdSDMZf+DnXeqZeLpaNi+bqcqxSgadpnw6ogKkeU4UuqYo6TNT0Qq/
0pnSUB+VRefqmKqkZ49+LeX5C0N4lNk=</latexit>Replace ✓
<latexit sha1_base64="ef+ZTfWjz05j6iz
Rbe9SXtxMdA=">AC23ichVFLT8JAEB7qC/BV9eilEUw4kcJBPZL4iBcTNPJIgJBtWUpDX2kXEi
SevBmv3rzqf9Lf4sGvazFRYthmO7PfPtzI4ROHYkdP09pSwtr6yupTPZ9Y3NrW1Z7ce+aPQ5
DXTd/ywabCIO7bHa8IWDm8GIWeu4fCGMTyN40xDyPb927FJOAdl1me3bdNJgB1VfWGBw4zuZvi
wEXLN9Vc3pRl0ubd0qJk6NkVX31g9rUI59MGpFLnDwS8B1iFOFrUYl0CoB1aAoshGfLOKd7yiJ3
BYHgwEd4m/h1EpQD+dYM5LZJm5xsENkanSIfSEVDbDjWzn8CPYT+05i1r83TKVyXOE1oBiRipe
ARc0AGNRpswZ7Uszoy7EtSnE9mNjfoCicR9mj86Z4iEwIYyotG5ZFrQMOR5jBfwYGuoIH7lmYI
mO+7BMm5VPESRQa9EDZ+fdSDMZf+DnXeqZeLpaNi+bqcqxSgadpnw6ogKkeU4UuqYo6TNT0Qq/
0pnSUB+VRefqmKqkZ49+LeX5C0N4lNk=</latexit>Replace ✓
<latexit sha1_base64="GRFKNV4w76Vu7J0J
caefUj7ML/0=">AC03ichVFLT8JAEB7qC/CFevTSCacSMtBPZL4iBcSTCwQkZhtWpDX2m3JE
i8GK/evOr/0t/iwa9rMVFi3GY7s9/MfPMyQ9eJha95ZSFxaXlXyhuLq2vrFZ2tpux0ESWdywA
jeIuiaLuev43BCOcHk3jDjzTJd3zNFxau+MeRQ7gX8pJiHve8z2naFjMQHoqpkIJrhaCSs3pbJW0
+R5xU9U8qUnVZQeqdrGlBAFiXkESefBHSXGMX4eqSTRiGwPk2BRdAcaed0T0XEJvDi8GBAR/jb
ePUy1Mc75YxltIUsLm6ESJX2c8kownvNCuHkN+4N5JzP4zw1QypxVOIE0wFiRjE7igW3j8F+l
nrNa/o9MuxI0pCPZjYP6QomkfVrfPCewRMBG0qLSqfS0wWHK9xgT8CENVJBOecagyo4HkExKLln
8jJGBL4JMp496sGb91LnlXa9ph/U6hf1cqOaLTxPu7RHVWz1kBp0Ti3UYSHLM73Qq2IoU+VBefx
yVXJZzA79OMrTJyswkh4=</latexit>Mutate p
<latexit sha1_base64="GRFKNV4w76Vu7J0J
caefUj7ML/0=">AC03ichVFLT8JAEB7qC/CFevTSCacSMtBPZL4iBcSTCwQkZhtWpDX2m3JE
i8GK/evOr/0t/iwa9rMVFi3GY7s9/MfPMyQ9eJha95ZSFxaXlXyhuLq2vrFZ2tpux0ESWdywA
jeIuiaLuev43BCOcHk3jDjzTJd3zNFxau+MeRQ7gX8pJiHve8z2naFjMQHoqpkIJrhaCSs3pbJW0
+R5xU9U8qUnVZQeqdrGlBAFiXkESefBHSXGMX4eqSTRiGwPk2BRdAcaed0T0XEJvDi8GBAR/jb
ePUy1Mc75YxltIUsLm6ESJX2c8kownvNCuHkN+4N5JzP4zw1QypxVOIE0wFiRjE7igW3j8F+l
nrNa/o9MuxI0pCPZjYP6QomkfVrfPCewRMBG0qLSqfS0wWHK9xgT8CENVJBOecagyo4HkExKLln
8jJGBL4JMp496sGb91LnlXa9ph/U6hf1cqOaLTxPu7RHVWz1kBp0Ti3UYSHLM73Qq2IoU+VBefx
yVXJZzA79OMrTJyswkh4=</latexit>Mutate p
<latexit sha1_base6
4="B/DtDUFCzWcfbXNCnQa45LPivPQ=">AC5
nichVHBTtAEH0xpQVKW0OPuViNKnGKnBxKj0i
FqpdKoBJAgit15tkFce21ptIeLAD/RW9dpbr
+3nlG/pgefFIEGEstZ6Zt+8eTuzE+WJLmwY/q
t5S8+Wn79YWV17uf7q9Rt/Y/OoyMZGqo7Mksyc
RKJQiU5Vx2qbqJPcKDGKEnUcDT+V8eOJMoXO0k
M7zV3JPqp7mkpLKFzv/5tIyKAzlQcphnOrVB
rI2SNjPTc78RNkO3gnmnVTkNVGs/869xhgZJ
MYQSGFpZ9AoOB3ihZC5MS6mBEz9LSLK1xijbl
jshQZguiQ/z5PpxWa8lxqFi5b8paE2zAzwHvuz
04xIru8VdEvaP9zXzis/+QNM6dcVjiljai46hS
/ErcYkLEoc1Qx72pZnFl2ZdHDR9eNZn25Q8o+
5b3OLiOG2NBFAuw5Zp8akTtP+AIpbYcVlK98px
C4jmNa4axyKmlKhnaMvXZz0c+vxUOedo3az
9aHZPmg3draqga+gjnfY4lS3sYMv2GcdElf4jT
/46w28794P7+ct1atVOW/xYHm/bgA58ZpF</l
atexit>Shared checkpoint directory
<latexit sha1_base6
4="B/DtDUFCzWcfbXNCnQa45LPivPQ=">AC5
nichVHBTtAEH0xpQVKW0OPuViNKnGKnBxKj0i
FqpdKoBJAgit15tkFce21ptIeLAD/RW9dpbr
+3nlG/pgefFIEGEstZ6Zt+8eTuzE+WJLmwY/q
t5S8+Wn79YWV17uf7q9Rt/Y/OoyMZGqo7Mksyc
RKJQiU5Vx2qbqJPcKDGKEnUcDT+V8eOJMoXO0k
M7zV3JPqp7mkpLKFzv/5tIyKAzlQcphnOrVB
rI2SNjPTc78RNkO3gnmnVTkNVGs/869xhgZJ
MYQSGFpZ9AoOB3ihZC5MS6mBEz9LSLK1xijbl
jshQZguiQ/z5PpxWa8lxqFi5b8paE2zAzwHvuz
04xIru8VdEvaP9zXzis/+QNM6dcVjiljai46hS
/ErcYkLEoc1Qx72pZnFl2ZdHDR9eNZn25Q8o+
5b3OLiOG2NBFAuw5Zp8akTtP+AIpbYcVlK98px
C4jmNa4axyKmlKhnaMvXZz0c+vxUOedo3az
9aHZPmg3draqga+gjnfY4lS3sYMv2GcdElf4jT
/46w28794P7+ct1atVOW/xYHm/bgA58ZpF</l
atexit>Shared checkpoint directory
<latexit sha1_base6
4="7DCHAiauHD87fCzY9nL/wWiGBE=">AC2
3ichVFLS8NAEB7jq/UZ9egl2ArioaQ9qMeCD7w
oFVpbqKVs4jYuzYvNtqDFkzfx6s2r/if9LR78s
kZBi7hM7PfPtzI4T+yJRtv06YUxOTc/M5v
Jz8wuLS8vmyup5Eg2kyxtu5Eey5bCE+yLkDSWU
z1ux5CxwfN50+vtpvDnkMhFRWFfXMe8EzAtFT7
hMAeqaZl0yEVrF0+5IKC5vi12zYJdsvaxp5w5
BcpWLTLf6IuKSKXBhQp5AUfJ8YJfjaVCabY
mAdGgGT8ISOc7qlOeQOwOJgMKB9/D2c2hka4px
qJjrbxS0+tkSmRZvYR1rRATu9lcNPYN+xbzTm/
XnDSCunFV7DOlDMa8UT4IquwPgvM8iYX7X8n5l
2pahHe7obgfpijaR9ut86B4hIYH0dsehQMz1o
OPo8xAuEsA1UkL7yl4KlO76EZdpyrRJmigx6Ej
Z9fdSDMZd/D3XcOa+UyjulylmlUN3OBp6jdqg
LUx1l6p0TDXU4aKmJ3qmF6Nj3Bn3xsMn1ZjIct
boxzIePwCl1ZUE</latexit>Train Niter
<latexit sha1_base6
4="7DCHAiauHD87fCzY9nL/wWiGBE=">AC2
3ichVFLS8NAEB7jq/UZ9egl2ArioaQ9qMeCD7w
oFVpbqKVs4jYuzYvNtqDFkzfx6s2r/if9LR78s
kZBi7hM7PfPtzI4T+yJRtv06YUxOTc/M5v
Jz8wuLS8vmyup5Eg2kyxtu5Eey5bCE+yLkDSWU
z1ux5CxwfN50+vtpvDnkMhFRWFfXMe8EzAtFT7
hMAeqaZl0yEVrF0+5IKC5vi12zYJdsvaxp5w5
BcpWLTLf6IuKSKXBhQp5AUfJ8YJfjaVCabY
mAdGgGT8ISOc7qlOeQOwOJgMKB9/D2c2hka4px
qJjrbxS0+tkSmRZvYR1rRATu9lcNPYN+xbzTm/
XnDSCunFV7DOlDMa8UT4IquwPgvM8iYX7X8n5l
2pahHe7obgfpijaR9ut86B4hIYH0dsehQMz1o
OPo8xAuEsA1UkL7yl4KlO76EZdpyrRJmigx6Ej
Z9fdSDMZd/D3XcOa+UyjulylmlUN3OBp6jdqg
LUx1l6p0TDXU4aKmJ3qmF6Nj3Bn3xsMn1ZjIct
boxzIePwCl1ZUE</latexit>Train Niter
<latexit sha1_base6
4="yzkwAIMTns3QVcbgnZznwTym6s=">AC9
HichVFNTxRBEH2MX4Bfqx65dFhM9LKZ3QN6JEG
JF5MlYECOlpmtnO9vRMeno3AeJv8A94M165c
dXfIb/Fg2+awUSJoSc9Vf3q1euqrqypg5p+n
MuXP3v0H8wuLDx89fvK08+z5dl1OvdIjVdrS
72ay1tY4PQomWL1beS2LzOqdbLexHdm2temdF
vhpNIHhcydOTZKBkKHndcbpRdaqrGQuXZBGCeq
spraGBYr+4UMYyWtGK4cdrpL41L3HT6rdNFu
4Zl5xL7OEIJhSkKaDgE+hYSNb89JGiInaAM2K
enolxjU9YZO6ULE2GJDrhP+dpr0Udz41mHbMVb
7HcnpkCL7k3omJGdnOrpl/T/uI+jVj+3xvOonJ
T4QltRsWFqPiReMCYjNsyi5Z5XcvtmU1XAcd4
G7sxrK+KSNOn+qPzjhFPbBIjAu8jM6dGFs8zvo
CjHbGC5pWvFUTs+IhWRqujimsVJfU8bfP6rIdj
7v871JvO9qDX+0NgfdtbQd+DyWsIxXnOobrO
EDhqxD4TMu8B0/klnyJfmafLuiJnNtzgv8tZL
z30XMnrw=</latexit>For each agent in population P
<latexit sha1_base6
4="yzkwAIMTns3QVcbgnZznwTym6s=">AC9
HichVFNTxRBEH2MX4Bfqx65dFhM9LKZ3QN6JEG
JF5MlYECOlpmtnO9vRMeno3AeJv8A94M165c
dXfIb/Fg2+awUSJoSc9Vf3q1euqrqypg5p+n
MuXP3v0H8wuLDx89fvK08+z5dl1OvdIjVdrS
72ay1tY4PQomWL1beS2LzOqdbLexHdm2temdF
vhpNIHhcydOTZKBkKHndcbpRdaqrGQuXZBGCeq
spraGBYr+4UMYyWtGK4cdrpL41L3HT6rdNFu
4Zl5xL7OEIJhSkKaDgE+hYSNb89JGiInaAM2K
enolxjU9YZO6ULE2GJDrhP+dpr0Udz41mHbMVb
7HcnpkCL7k3omJGdnOrpl/T/uI+jVj+3xvOonJ
T4QltRsWFqPiReMCYjNsyi5Z5XcvtmU1XAcd4
G7sxrK+KSNOn+qPzjhFPbBIjAu8jM6dGFs8zvo
CjHbGC5pWvFUTs+IhWRqujimsVJfU8bfP6rIdj
7v871JvO9qDX+0NgfdtbQd+DyWsIxXnOobrO
EDhqxD4TMu8B0/klnyJfmafLuiJnNtzgv8tZL
z30XMnrw=</latexit>For each agent in population P
<latexit s
ha1_base64="cpSpYP5
e0GQd0Rkjdt1IP+a5rY
U=">ACzHichVFLT8J
AEB7qC/CFevTSEw4k
ZaDeiTxES8ajIkSMi2
LNjQV7YLCRKu3rzqb9P
f4sFv12KixLDNdma/+e
bmR0n9r1EWtZ7xlhaX
ldy+by6xubW9uFnd1G
Eg2Fy+tu5Eei6bCE+17
I69KTPm/GgrPA8fm9Mz
hV8fsRF4kXhXdyHPN2
wPqh1/NcJgHdso7sFIp
W2dLnHfs1ClSumpR4Y
MeqEsRuTSkgDiFJOH7x
CjB1yKbLIqBtWkCTMDz
dJzTlPLIHYLFwWBAB/j
3cWqlaIiz0kx0totbfG
yBTJMOsS+0ogO2upXDT
2A/sZ801v/3holWVhW
OYR0o5rTiFXBJj2Asyg
xS5qyWxZmqK0k9OtHde
Kgv1ojq0/3ROUNEABvo
iEnmtmHhqPI7xACFt
HBeqVZwqm7rgLy7TlWi
VMFRn0BKx6fdSDMdt/h
zrvNCpl+6hcuakUq6V0
4FnapwMqYarHVKVLq
EOF9W90Cu9GdeGNCbG9
JtqZNKcPfq1jOcvFpCP
xA=</latexit>at
<latexit s
ha1_base64="cpSpYP5
e0GQd0Rkjdt1IP+a5rY
U=">ACzHichVFLT8J
AEB7qC/CFevTSEw4k
ZaDeiTxES8ajIkSMi2
LNjQV7YLCRKu3rzqb9P
f4sFv12KixLDNdma/+e
bmR0n9r1EWtZ7xlhaX
ldy+by6xubW9uFnd1G
Eg2Fy+tu5Eei6bCE+17
I69KTPm/GgrPA8fm9Mz
hV8fsRF4kXhXdyHPN2
wPqh1/NcJgHdso7sFIp
W2dLnHfs1ClSumpR4Y
MeqEsRuTSkgDiFJOH7x
CjB1yKbLIqBtWkCTMDz
dJzTlPLIHYLFwWBAB/j
3cWqlaIiz0kx0totbfG
yBTJMOsS+0ogO2upXDT
2A/sZ801v/3holWVhW
OYR0o5rTiFXBJj2Asyg
xS5qyWxZmqK0k9OtHde
Kgv1ojq0/3ROUNEABvo
iEnmtmHhqPI7xACFt
HBeqVZwqm7rgLy7TlWi
VMFRn0BKx6fdSDMdt/h
zrvNCpl+6hcuakUq6V0
4FnapwMqYarHVKVLq
EOF9W90Cu9GdeGNCbG9
JtqZNKcPfq1jOcvFpCP
xA=</latexit>at
<latexit s
ha1_base64="vDz17im
uHaNAYWMt2JBztfmCMN
I=">AC03ichVFLS8N
AEJ7GV1tfVY9egkXxV
JIe1GPB16EiqYt1iKb
dK1L82KTFGrxIl69edX
/pb/Fg1/WVNAi3bCZ2W
9mvnZoSui2Dec9rM7
Nz8Qr5QXFxaXlktra03
oiCRDrecwA1ky2YRd4X
PrVjELm+FkjPdnT7h
+m9uaAy0gE/mU8DHnH
Yz1f3AqHxYCuLoSXuEq
9KZWNiqGOPqmYmVKm7N
SD0gdU5cCcighjzj5F
EN3iVGEr0mGRQC69AI
mIQmlJ3TAxURm8CLw4M
B7ePfw6udoT7eKWekoh
1kcXElInXaxj1RjDa80
6wcegT5iXuvsN6/GUa
KOa1wCGmDsaAYz4DHdA
ePaZFe5jmuZXpk2lVMt
3SguhGoL1RI2qfzw3ME
iwTWVxadjpVnDxy2eg8
wAR/SQgXplMcMuq4C8
mU5IrFzxgZ+CRkOn3Ug
zWbf5c6qTSqFXOvUj2v
lms72cLztElbtIut7l
ONTqmOhxkeaFXetMsb
aQ9ak/frloui9mgX0d7
/gI+LJL5</latexit>Simulation
<latexit s
ha1_base64="vDz17im
uHaNAYWMt2JBztfmCMN
I=">AC03ichVFLS8N
AEJ7GV1tfVY9egkXxV
JIe1GPB16EiqYt1iKb
dK1L82KTFGrxIl69edX
/pb/Fg1/WVNAi3bCZ2W
9mvnZoSui2Dec9rM7
Nz8Qr5QXFxaXlktra03
oiCRDrecwA1ky2YRd4X
PrVjELm+FkjPdnT7h
+m9uaAy0gE/mU8DHnH
Yz1f3AqHxYCuLoSXuEq
9KZWNiqGOPqmYmVKm7N
SD0gdU5cCcighjzj5F
EN3iVGEr0mGRQC69AI
mIQmlJ3TAxURm8CLw4M
B7ePfw6udoT7eKWekoh
1kcXElInXaxj1RjDa80
6wcegT5iXuvsN6/GUa
KOa1wCGmDsaAYz4DHdA
ePaZFe5jmuZXpk2lVMt
3SguhGoL1RI2qfzw3ME
iwTWVxadjpVnDxy2eg8
wAR/SQgXplMcMuq4C8
mU5IrFzxgZ+CRkOn3Ug
zWbf5c6qTSqFXOvUj2v
lms72cLztElbtIut7l
ONTqmOhxkeaFXetMsb
aQ9ak/frloui9mgX0d7
/gI+LJL5</latexit>Simulation
<latexit sha1_base6
4="Da02sr8Ey/BnfNxrHSc1jHP+nKU=">ACz
HichVFLT8JAEB7qC/CFevTSEw4kZaDeiTxES8
ajIkSMi2LNjQV7YLCRKu3rzqb9Pf4sFv12Kix
LDNdma/+ebmR0n9r1EWtZ7xlhaXldy+by6x
ubW9uFnd1GEg2Fy+tu5Eei6bCE+17I69KTPm/G
grPA8fm9MzhV8fsRF4kXhXdyHPN2wPqh1/NcJg
Hdio7sFIpW2dLnHfs1ClSumpR4YMeqEsRuTSk
gDiFJOH7xCjB1yKbLIqBtWkCTMDzdJzTlPLIH
YLFwWBAB/j3cWqlaIiz0kx0totbfGyBTJMOsS+
0ogO2upXDT2A/sZ801v/3holWVhWOYR0o5rTiF
XBJj2AsygxS5qyWxZmqK0k9OtHdeKgv1ojq0/3
ROUNEABvoiEnmtmHhqPI7xACFtHBeqVZwqm
7rgLy7TlWiVMFRn0BKx6fdSDMdt/hzrvNCpl+6
hcuakUq6V04FnapwMqYarHVKVLqEOF9W90Cu9
GdeGNCbG9JtqZNKcPfq1jOcvP3iP1Q=</late
xit>rt
<latexit sha1_base6
4="Da02sr8Ey/BnfNxrHSc1jHP+nKU=">ACz
HichVFLT8JAEB7qC/CFevTSEw4kZaDeiTxES8
ajIkSMi2LNjQV7YLCRKu3rzqb9Pf4sFv12Kix
LDNdma/+ebmR0n9r1EWtZ7xlhaXldy+by6x
ubW9uFnd1GEg2Fy+tu5Eei6bCE+17I69KTPm/G
grPA8fm9MzhV8fsRF4kXhXdyHPN2wPqh1/NcJg
Hdio7sFIpW2dLnHfs1ClSumpR4YMeqEsRuTSk
gDiFJOH7xCjB1yKbLIqBtWkCTMDzdJzTlPLIH
YLFwWBAB/j3cWqlaIiz0kx0totbfGyBTJMOsS+
0ogO2upXDT2A/sZ801v/3holWVhWOYR0o5rTiF
XBJj2AsygxS5qyWxZmqK0k9OtHdeKgv1ojq0/3
ROUNEABvoiEnmtmHhqPI7xACFtHBeqVZwqm
7rgLy7TlWiVMFRn0BKx6fdSDMdt/hzrvNCpl+6
hcuakUq6V04FnapwMqYarHVKVLqEOF9W90Cu9
GdeGNCbG9JtqZNKcPfq1jOcvP3iP1Q=</late
xit>rt
<latexit sha1_base6
4="pMTn5WVXNb4WRfEMBNxBVLZiIGk=">ACz
XichVFLS8NAEJ7GV1tfVY9egkXoQUrag3os+MC
LWME+oJaySbcxNC+STaFWvXrzqn9Nf4sHv1TQ
Yt0w2Zmv/nm25kdM3SdWBjGe0ZbWFxaXsnm8q
tr6xubha3tZhwkcUbVuAGUdtkMXcdnzeEI1ze
DiPOPNPlLXN4IuOtEY9iJ/BvxDjkXY/ZvjNwLC
YkFPfEQa9QNMqGWvqsU0mdIqWrHhQ+6Jb6FJBF
CXnEyScB3yVGMb4OVcigEFiXJsAieI6Kc3qkP
HITsDgYDOgQfxunTor6OEvNWGVbuMXFjpCp0z7
2uVI0wZa3cvgx7Cf2vcLsf2+YKGVZ4RjWhGJOK
V4CF3QHxrxML2VOa5mfKbsSNKBj1Y2D+kKFyD6
tH51TRCJgQxXR6UwxbWiY6jzC/iwDVQgX3mq
oKuO+7BMWa5U/FSRQS+Cla+PejDmyt+hzjrNar
lyWK5eV4u1UjrwLO3SHpUw1SOq0QXVUYeFrl/o
ld60Ky3RHrSnb6qWSXN26NfSnr8A0niQDA=</
latexit>st,
<latexit sha1_base6
4="pMTn5WVXNb4WRfEMBNxBVLZiIGk=">ACz
XichVFLS8NAEJ7GV1tfVY9egkXoQUrag3os+MC
LWME+oJaySbcxNC+STaFWvXrzqn9Nf4sHv1TQ
Yt0w2Zmv/nm25kdM3SdWBjGe0ZbWFxaXsnm8q
tr6xubha3tZhwkcUbVuAGUdtkMXcdnzeEI1ze
DiPOPNPlLXN4IuOtEY9iJ/BvxDjkXY/ZvjNwLC
YkFPfEQa9QNMqGWvqsU0mdIqWrHhQ+6Jb6FJBF
CXnEyScB3yVGMb4OVcigEFiXJsAieI6Kc3qkP
HITsDgYDOgQfxunTor6OEvNWGVbuMXFjpCp0z7
2uVI0wZa3cvgx7Cf2vcLsf2+YKGVZ4RjWhGJOK
V4CF3QHxrxML2VOa5mfKbsSNKBj1Y2D+kKFyD6
tH51TRCJgQxXR6UwxbWiY6jzC/iwDVQgX3mq
oKuO+7BMWa5U/FSRQS+Cla+PejDmyt+hzjrNar
lyWK5eV4u1UjrwLO3SHpUw1SOq0QXVUYeFrl/o
ld60Ky3RHrSnb6qWSXN26NfSnr8A0niQDA=</
latexit>st,
<latexit s
ha1_base64="XMYE8cw
ucWbhyjubmGyMGUqcz
8=">AC1HichVFNT8J
AEB3qF+AX6tFLIzHxR
AoH9UjiRzxogaQBI3Z
1rVuKNtmW0gQPRmv3rz
q79Lf4sG3azFRYthmO7
Nv3ryd2XGjQMSJ47xnr
Knpmdm5bC4/v7C4tFxY
W3GYU95vOGFQahaLot
5ICRvJCIJeCtSnHXdgJ
+7nT0dP+9zFYtQ1pNB
xC+7zJfiRngsAdQ+O7b
rigkpH9VKDolxyx73C
mnTpHSVQsLH3RB1xSR
z3qEidJCfyAGMX42lQm
hyJglzQEpuAJE+f0QHn
k9sDiYDCgHfx9nNopKn
HWmrHJ9nBLgK2QadMm9
qFRdMHWt3L4Mewn9p3
B/H9vGBplXeEA1oVizi
ieAE/oFoxJmd2UOaplc
qbuKqEb2jXdCNQXGUT3
6f3o7COigHVMxKYDw/S
h4ZpzHy8gYRuoQL/ySM
E2HV/DMmO5UZGpIoOeg
tWvj3ow5vLfoY47zUqp
vF2qnFaKVScdeJbWaY
O2MNUdqtIR1VCHnsLv
dKb1bTurUfr6ZtqZdKc
Nfq1rOcv/5eS4g=</l
atexit>RL Training
<latexit s
ha1_base64="XMYE8cw
ucWbhyjubmGyMGUqcz
8=">AC1HichVFNT8J
AEB3qF+AX6tFLIzHxR
AoH9UjiRzxogaQBI3Z
1rVuKNtmW0gQPRmv3rz
q79Lf4sG3azFRYthmO7
Nv3ryd2XGjQMSJ47xnr
Knpmdm5bC4/v7C4tFxY
W3GYU95vOGFQahaLot
5ICRvJCIJeCtSnHXdgJ
+7nT0dP+9zFYtQ1pNB
xC+7zJfiRngsAdQ+O7b
rigkpH9VKDolxyx73C
mnTpHSVQsLH3RB1xSR
z3qEidJCfyAGMX42lQm
hyJglzQEpuAJE+f0QHn
k9sDiYDCgHfx9nNopKn
HWmrHJ9nBLgK2QadMm9
qFRdMHWt3L4Mewn9p3
B/H9vGBplXeEA1oVizi
ieAE/oFoxJmd2UOaplc
qbuKqEb2jXdCNQXGUT3
6f3o7COigHVMxKYDw/S
h4ZpzHy8gYRuoQL/ySM
E2HV/DMmO5UZGpIoOeg
tWvj3ow5vLfoY47zUqp
vF2qnFaKVScdeJbWaY
O2MNUdqtIR1VCHnsLv
dKb1bTurUfr6ZtqZdKc
Nfq1rOcv/5eS4g=</l
atexit>RL Training
<latexit s
ha1_base64="XFOgbW9
akfqeXCXt73mkVCqoM
I=">ACzXichVFLT8J
AEB7qC/CFevTSEw4k
ZaDeiTxEQ8SMfJKkJi2
LWhr2xbEkS9evOqf01
/iwe/XYuJEsM25n95p
tvZ3bM0HWiWNPeM8rC4
tLySjaX1b39gsbG23
oiDhFmtagRvwjmlEzHV
81oyd2GWdkDPDM13WNo
fHIt4eMR45gd+IxyHr
eYbtOwPHMmIBXVw3are
FolbW5FJnHT1ipSuel
D4oBvqU0AWJeQRI59i+
C4ZFOHrk4ahcB6NAHG
4TkyzuiR8shNwGJgGEC
H+Ns4dVPUx1loRjLbwi
0uNkemSvYZ1LRBFvcy
uBHsJ/Y9xKz/71hIpV
FhWNYE4o5qVgDHtMdGP
MyvZQ5rWV+pugqpgEdy
W4c1BdKRPRp/eicIMKB
DWVEpVPJtKFhyvMIL+D
DNlGBeOWpgio7sMa0j
Kp4qeKBvQ4rHh91IMx6
3+HOu0KmX9oFy5qhSr
pXTgWdqlPSphqodUpX
Oqow4LXb/QK70pl0qiP
ChP31Qlk+bs0K+lPH8B
Wd+P2g=</latexit>LSTM
<latexit s
ha1_base64="XFOgbW9
akfqeXCXt73mkVCqoM
I=">ACzXichVFLT8J
AEB7qC/CFevTSEw4k
ZaDeiTxEQ8SMfJKkJi2
LWhr2xbEkS9evOqf01
/iwe/XYuJEsM25n95p
tvZ3bM0HWiWNPeM8rC4
tLySjaX1b39gsbG23
oiDhFmtagRvwjmlEzHV
81oyd2GWdkDPDM13WNo
fHIt4eMR45gd+IxyHr
eYbtOwPHMmIBXVw3are
FolbW5FJnHT1ipSuel
D4oBvqU0AWJeQRI59i+
C4ZFOHrk4ahcB6NAHG
4TkyzuiR8shNwGJgGEC
H+Ns4dVPUx1loRjLbwi
0uNkemSvYZ1LRBFvcy
uBHsJ/Y9xKz/71hIpV
FhWNYE4o5qVgDHtMdGP
MyvZQ5rWV+pugqpgEdy
W4c1BdKRPRp/eicIMKB
DWVEpVPJtKFhyvMIL+D
DNlGBeOWpgio7sMa0j
Kp4qeKBvQ4rHh91IMx6
3+HOu0KmX9oFy5qhSr
pXTgWdqlPSphqodUpX
Oqow4LXb/QK70pl0qiP
ChP31Qlk+bs0K+lPH8B
Wd+P2g=</latexit>LSTM
<latexit s
ha1_base64="e/iGA7t
l/fEarqB9ZxBNeSyRtV
I=">AC1XichVFNT8J
AEB3qF+AX6tELkZhwk
RQO6hGDGi8mMhHAsS0
y1I3lLbZLiRIuBmv3rz
q39Lf4sHXtZgoMWyznd
k3b97O7NiBK0Jlmu8JY
2l5ZXUtmUqvb2xubWd2
duhP5SM15jv+rJpWyF
3hcdrSiXNwPJrYHt8o
bdr0TxojLUPjerRoH
vDOwHE/0BLMUoPYZU74
8qkihBLvL5MyCqVd23i
nGTo7iVfUzH9SmLvnEa
EgD4uSRgu+SRSG+FhXJ
pABYhybAJDyh45ymlEb
uECwOhgW0j7+DUytGPZ
wjzVBnM9ziYktkZukQ+
1Ir2mBHt3L4Iewn9oP
GnH9vmGjlqMIxrA3FlF
a8Bq7oHoxFmYOYOatlc
WbUlaIenepuBOoLNBL1
yX50zhGRwPo6kqULzXS
gYevzC/gwdZQfTKM4
Ws7rgLa2nLtYoXK1rQk
7DR6MejLn4d6jzTr1U
KB4XSjelXDkfDzxJ+3
RAeUz1hMp0RVXUwdDHC
73Sm9Ewpsaj8fRNRJx
zh79WsbzF3Q8k24=</l
atexit>Actor-Critic
<latexit s
ha1_base64="e/iGA7t
l/fEarqB9ZxBNeSyRtV
I=">AC1XichVFNT8J
AEB3qF+AX6tELkZhwk
RQO6hGDGi8mMhHAsS0
y1I3lLbZLiRIuBmv3rz
q39Lf4sHXtZgoMWyznd
k3b97O7NiBK0Jlmu8JY
2l5ZXUtmUqvb2xubWd2
duhP5SM15jv+rJpWyF
3hcdrSiXNwPJrYHt8o
bdr0TxojLUPjerRoH
vDOwHE/0BLMUoPYZU74
8qkihBLvL5MyCqVd23i
nGTo7iVfUzH9SmLvnEa
EgD4uSRgu+SRSG+FhXJ
pABYhybAJDyh45ymlEb
uECwOhgW0j7+DUytGPZ
wjzVBnM9ziYktkZukQ+
1Ir2mBHt3L4Iewn9oP
GnH9vmGjlqMIxrA3FlF
a8Bq7oHoxFmYOYOatlc
WbUlaIenepuBOoLNBL1
yX50zhGRwPo6kqULzXS
gYevzC/gwdZQfTKM4
Ws7rgLa2nLtYoXK1rQk
7DR6MejLn4d6jzTr1U
KB4XSjelXDkfDzxJ+3
RAeUz1hMp0RVXUwdDHC
73Sm9Ewpsaj8fRNRJx
zh79WsbzF3Q8k24=</l
atexit>Actor-Critic
<latexit sha1_base64="Zz0kmSKYEw+UP2WS
9MKjV+tydF4=">AC3HichVFNS8QwEH3W7+9Vj16Ki+Bp6e5BPQp+4EVQcFXwi7TGrabljSrqH
jzJl69edXfpL/Fg6+xCipiSjqTN29eZjJhlqjcBsFLl9fd09vXPzA4NDwyOjZemZjcydOiWQzS
pPU7IUil4nSsmVTeReZqRoh4ncDVvLRXz3XJpcpXrbXmbysC1irU5VJCyh48rEcqt0h3pWyOUV
jo+rlSDWuCW/9upl04V5dpMK684wAlSROigDQkNSz+BQM5vH3UEyIgd4pqYoadcXOIGQ8ztkCXJ
ERb/Mc87Zeo5rnQzF12xFsSbsNMH7Pca04xJLu4VdLPad+4rxwW/3nDtVMuKrykDak46BQ3iFuc
kfFfZrtkftbyf2bRlcUpFl03ivVlDin6jL50VhgxFou4mPVMWNqhO58zhfQtE1WULzyp4LvOj6
hFc5Kp6JLRUE9Q1u8PuvhmOs/h/rb2WnU6vO1xlajuhSUAx/ANGYwx6kuYAnr2GQdES7wiCc8e0f
erXfn3X9Qva4yZwrflvfwDkNRlhY=</latexit>Continue training
<latexit sha1_base64="Zz0kmSKYEw+UP2WS
9MKjV+tydF4=">AC3HichVFNS8QwEH3W7+9Vj16Ki+Bp6e5BPQp+4EVQcFXwi7TGrabljSrqH
jzJl69edXfpL/Fg6+xCipiSjqTN29eZjJhlqjcBsFLl9fd09vXPzA4NDwyOjZemZjcydOiWQzS
pPU7IUil4nSsmVTeReZqRoh4ncDVvLRXz3XJpcpXrbXmbysC1irU5VJCyh48rEcqt0h3pWyOUV
jo+rlSDWuCW/9upl04V5dpMK684wAlSROigDQkNSz+BQM5vH3UEyIgd4pqYoadcXOIGQ8ztkCXJ
ERb/Mc87Zeo5rnQzF12xFsSbsNMH7Pca04xJLu4VdLPad+4rxwW/3nDtVMuKrykDak46BQ3iFuc
kfFfZrtkftbyf2bRlcUpFl03ivVlDin6jL50VhgxFou4mPVMWNqhO58zhfQtE1WULzyp4LvOj6
hFc5Kp6JLRUE9Q1u8PuvhmOs/h/rb2WnU6vO1xlajuhSUAx/ANGYwx6kuYAnr2GQdES7wiCc8e0f
erXfn3X9Qva4yZwrflvfwDkNRlhY=</latexit>Continue training
<latexit sha1_base64="Fr65aWl5qvGLDJmj
CLi2+J3UBP0=">ADFnichVLSsNAFD3G97vq0k2wC4kpEXbuhN84EJBwapQRSbpGEPTJCSpoO
J/CG71N9yJW7f+iQsXnhlT0UVxws29c+beM+fOjBMHfprZ9nuf0T8wODQ8Mjo2PjE5NV2YmT1Ko
07iyrobBVFy4ohUBn4o65mfBfIkTqRoO4E8dlobav34SiapH4WH2XUsz9rC/0L3xUZofPC9G4km
mYcxZ0gR4q2tVqz12or5ndQqeZBtWKWLFuPIvKxHxU+cIomIrjoA2JEBnjAIpvwZKsBETO8Mt
sYSRr9cl7jDG2g6zJDME0Rb/HmeNHA05V5yprna5S0BLWHn6a9ageXB0jg0Lq6hx1+Ue8R1MLNK2
tRqHOynFknFK/0m70ZjXU92tVqW6u6Z3yDiqGfeIZ7hkxn+V7Tyzq+X/SnUiGS7YgerSp75YI+q
M3B+eTa4kxFp6xcSWzvTI4ej5Fc8rpK9TgbqhLoOpO27SC+2lZglzRkG+hF7dHPXwiXTfgdk7OCp
bpYpVPigX15fyxzKCeSxgiXdQxTp2sE8d6tU84BFPxr3xbLwYr9+pRl9eM4c/w3j7Ap1dn4g=</
latexit>Load population
<latexit sha1_base64="Fr65aWl5qvGLDJmj
CLi2+J3UBP0=">ADFnichVLSsNAFD3G97vq0k2wC4kpEXbuhN84EJBwapQRSbpGEPTJCSpoO
J/CG71N9yJW7f+iQsXnhlT0UVxws29c+beM+fOjBMHfprZ9nuf0T8wODQ8Mjo2PjE5NV2YmT1Ko
07iyrobBVFy4ohUBn4o65mfBfIkTqRoO4E8dlobav34SiapH4WH2XUsz9rC/0L3xUZofPC9G4km
mYcxZ0gR4q2tVqz12or5ndQqeZBtWKWLFuPIvKxHxU+cIomIrjoA2JEBnjAIpvwZKsBETO8Mt
sYSRr9cl7jDG2g6zJDME0Rb/HmeNHA05V5yprna5S0BLWHn6a9ageXB0jg0Lq6hx1+Ue8R1MLNK2
tRqHOynFknFK/0m70ZjXU92tVqW6u6Z3yDiqGfeIZ7hkxn+V7Tyzq+X/SnUiGS7YgerSp75YI+q
M3B+eTa4kxFp6xcSWzvTI4ej5Fc8rpK9TgbqhLoOpO27SC+2lZglzRkG+hF7dHPXwiXTfgdk7OCp
bpYpVPigX15fyxzKCeSxgiXdQxTp2sE8d6tU84BFPxr3xbLwYr9+pRl9eM4c/w3j7Ap1dn4g=</
latexit>Load population
<latexit sha1_base6
4="czGwoX8A6g2UO0SVTqUTfBG6jBc=">ADC
XichVLSsNAFD3G97vq0k2wC4kpEXbuhN84EZ
QtCpUkUkcY2iahCQtqPgFglv9DXfi1q/wT1y48
MyYi6KEyb3zrn3njl3Zpw48NPMt/7jP6Bwa
HhkdGx8YnJqenCzOxRGrUTV9bdKIiSE0ekMvBD
Wc/8LJAncSJFywnksdPcUPHjkxSPwoPs+tYnr
WEF/qXvisyBR2IjwvFG1rtWav1VbMb6dSzZ1q
xSxZth5F5GMvKnzgFBeI4KNFiRCZPQDCKT8G
ijBRkzsDLfEnq+jkvcYy1bWZJZgiTf49rho
5GnKtOFNd7XKXgDNh5emvVYPTg6NzbFhYRY27L
vfw72BikXNbq3G4k1Is6ae0n5w3GvN6qrvVqlR
317QOGUc14y7xDFfM+K+ylWd2tfxfqU4kwyU7
UF361BdrRJ2R+8OzyUhCrKkjJrZ0pkcOR687PK
+Qtk4F6oa6DKbu+IJWaCs1S5gzCvIltOrmqIdP
pPsOzN7OUdkqVazyfrm4vpQ/lhHMYwFLvIMq1r
GDPepw2fUDHvFk3BvPxovx+p1q9OU1c/gzjLc
vwBGajQ=</latexit>Save
<latexit sha1_base6
4="czGwoX8A6g2UO0SVTqUTfBG6jBc=">ADC
XichVLSsNAFD3G97vq0k2wC4kpEXbuhN84EZ
QtCpUkUkcY2iahCQtqPgFglv9DXfi1q/wT1y48
MyYi6KEyb3zrn3njl3Zpw48NPMt/7jP6Bwa
HhkdGx8YnJqenCzOxRGrUTV9bdKIiSE0ekMvBD
Wc/8LJAncSJFywnksdPcUPHjkxSPwoPs+tYnr
WEF/qXvisyBR2IjwvFG1rtWav1VbMb6dSzZ1q
xSxZth5F5GMvKnzgFBeI4KNFiRCZPQDCKT8G
ijBRkzsDLfEnq+jkvcYy1bWZJZgiTf49rho
5GnKtOFNd7XKXgDNh5emvVYPTg6NzbFhYRY27L
vfw72BikXNbq3G4k1Is6ae0n5w3GvN6qrvVqlR
317QOGUc14y7xDFfM+K+ylWd2tfxfqU4kwyU7
UF361BdrRJ2R+8OzyUhCrKkjJrZ0pkcOR687PK
+Qtk4F6oa6DKbu+IJWaCs1S5gzCvIltOrmqIdP
pPsOzN7OUdkqVazyfrm4vpQ/lhHMYwFLvIMq1r
GDPepw2fUDHvFk3BvPxovx+p1q9OU1c/gzjLc
vwBGajQ=</latexit>Save
Fig. 2: An illustration of the system used to solve our complex manipulation tasks using a combination of RL, highly parallelized robotic
simulation, and Population Based Training (PBT).
with high-DoF single and dual hand-arm systems.
• We introduce a staged reward function formulation and
a PBT meta-objective to simplify and automate reward
tuning and hyperparameter search.
• We release our environments, RL, and PBT code to facil-
itate further research in dexterous robotic manipulation
(see the supplementary website).
II. RELATED WORK
Producing control policies to perform complex, contact-rich
tasks has been a long-standing challenge in robotics. Classical
methods for this have focused on directly leveraging robot
kinematics [34, 25, 20]. While useful in free-space or pick-
and-place style tasks, these methods struggle as the number of
contacts grows.
Recently, various systems have leveraged learning-based
methods to perform contact-rich robotic manipulation, achiev-
ing impressive results both in simulation and reality [18, 15].
In particular, RL-based methods in simulation have shown the
ability to learn complex and robust behaviors in realistic scenar-
ios which transfer to the real world [17, 2, 10]. The advent of
high-throughput simulation on GPUs has improved the speed
at which such tasks can be learned using RL [24, 33, 1, 12, 8].
Multiple prior projects have explored the problem of dexter-
ous object manipulation. Kumar et al. [16] achieved in-hand
object rotation with a Shadow Hand-like robotic hand using
a model-based approach. Andrychowicz et al. [2] and Handa
et al. [10] showed that it was possible to train the policy to
do in-hand cube manipulation and even Rubik’s cube [31]
solving entirely in simulation and deploy the learned policy
on the real robot. Other work has shown multiple tasks with
free-floating hands [6] or with object grasping [41]. Matl et al.
[26] demonstrated methods for learning grasping policies with
two robotic arms and different types of end-effectors such as
suction cups and parallel jaw grippers. Gupta et al. [9] were
able to learn object manipulation skills on a hand-arm system
using off-policy reset-free reinforcement learning directly in
the real world. Our approach is most similar to Handa et al.
[10]: we also take advantage of the massively parallel GPU-
accelerated physics engine, and we add a Population-Based
Training outer loop for improved exploration, automated reward
function tuning, and hyperparameter optimization.
Jaderberg et al. [13] popularized Population-Based Training
in a variety of domains such as RL, adversarial learning, and
machine translation, however PBT methods turned out to be
particularly promising in deep RL where exploration is often
the bottleneck. PBT provides a way to combine the exploration
power of multiple learners and directs resources toward more
promising behaviors. Since then, PBT algorithms have been
exceptionally successful in RL for video game applications
and helped to produce state-of-the-art agents for games such
as Quake [14], Doom [32], and Starcraft II [38].
Recently Wan et al. [39] augmented PBT-style methods
with trust-region based Bayesian Optimization and were able
to optimize both hyperparameters and model architectures
simultaneously. Flajolet et al. [7] proposed highly efficient
JAX implementation of PBT that enables evaluation of multiple
agents on one accelerator. Both Wan et al. [39] and Flajolet et al.
[7] demonstrated great results on standard continuous control
benchmarks such as Half-Cheetah and Humanoid, in contrast,
we apply our method in complex dexterous manipulation
domains more similar to real robot settings. Additionally, our
decentralized PBT implementation (Section III-D) makes it
easy to use the algorithm in distributed compute environments
such as Slurm clusters.
III. METHOD
A. Problem Statement
A lot of problems in practical robotics require the robot
to perform some notion of rearrangement [3], i.e. bringing a
given environment into a specified state. In household, factory,
or warehouse environments many interesting tasks will involve
20 4 |
—
| &


<!-- page 3 (ocr) -->
a type of rearrangement that requires dexterous object handling
and manipulation [30]. In this work, we target a high-DoF
anthropomorphic hand+arm system in the attempt to build
towards the desired level of dexterity.
We focus on a problem that can be seen as a special case
of rearrangement: single-object reposing. This task requires
changing the state of a single rigid body such that it matches
the target position x
∈
R3 and, optionally, orientation
R ∈SO(3). Dexterous single-object manipulation can be
seen as an essential primitive required to perform general-
purpose rearrangement. This task requires mastery of contact-
rich grasping and in-hand manipulation and presents an exciting
challenge for robotics research.
We approach dexterous manipulation as a discrete-time
sequential decision-making process. At each step the controller
observes environment state st ∈RNobs (which includes the
target object pose) and yields an action at ∈RNdof specifying
the desired angles of arm and finger joints. Whenever the object
state matches the target within a specified tolerance, the attempt
is considered successful, and the target state is reset. If the
object is dropped during the attempt, or if the target state is not
achieved within a time period τ we consider this attempt failed.
The simulation proceeds until Nmax consecutive successes are
reached or until the first failure. The performance on the task
can thus be measured as a number of consecutive successes
within the episode Nsucc ≤Nmax, as done in prior work [2].
Similar to Allshire et al. [1] we use Nkp keypoints to
represent the observed object pose xkp ∈R3Nkp. In tasks
that require orientation matching, keypoints are also used to
represent the desired object pose xtarg ∈R3Nkp (Figure 3).
We consider such task successfully executed when all of
Nkp keypoints are within the tolerance threshold of their
corresponding target locations
max
i∈1..Nkp||x(i)
targ −x(i)
kp|| ≤ε∗.
For tasks that require only position matching we just require
Fig. 3: We use object keypoints (yellow) to represent both observed
object position xkp ∈R3Nkp and object shape. In reorientation tasks
keypoints are also used to represent the desired object pose xtarg ∈
R3Nkp (green). Observed fingertip locations are additionally rendered
in blue.
the object’s center to be within ε∗of the desired location.
The keypoint representation provides multiple benefits. It
eliminates the need to tune tolerance thresholds and RL reward
weights separately for rotation and translation. In addition to
that, keypoints placed in a predefined pattern on the convex
hull of the object allow the policy to observe the shape of
the rigid body. In this work we use parallelepipeds with
dimensions ranging from 3 cm to 30 cm as our manipulation
targets, therefore a representation with Nkp = 4 keypoints is
sufficient to convey the shape information.
B. Scenarios
We developed three variants of our object manipulation task
that highlight different challenges in dexterous manipulation.
These scenarios are regrasping, grasp-and-throw, and reorien-
tation (Figure 1). At the beginning of each episode, the object
appears in a random position on the table and the hand-arm
system is reset to a random state srobot ∈R2Ndof consisting
of random joint angular velocities and initial angles within the
DoF limits. The episode then proceeds according to one of the
following scenarios.
The regrasping task demands that the agent grasp the object,
pick it up from the table, and hold it in a specified location for
a duration of time, after which both object and target positions
are reset. To succeed in this scenario the control policy must
develop stable grasps that minimize the probability of dropping
the object during the attempt.
In grasp-and-throw the task is to pick up the object and
displace it into a container that can be outside of manipulator’s
reach. This scenario requires aiming for the container and
throwing the object a significant distance. Here we test the
ability of the control policy to understand the dynamic aspects
of object manipulation: successful execution of this task
requires releasing the grip at the right point of the trajectory,
giving the object just the right amount of momentum to direct
it towards the goal. After each attempt we reset the positions
of the object and the container to make sure that the policy is
able to complete the task repeatedly for a diverse set of initial
conditions.
The reorientation task provides perhaps the most difficult
object manipulation challenge among the chosen scenarios.
The goal is to grasp the object and consecutively move it to
different target positions and orientations. This scenario requires
maintaining a stable grip for minutes of simulated time, fine
control of the joints of the robotic arm, and occasional in-hand
rotation when the reorientation cannot be performed by merely
using the affordances of the Kuka arm (video demonstration).
Thus formulated, the reorientation task includes elements seen
in previous work such as dexterous in-hand manipulation
[31, 10], but extends the capability of the manipulator to
perform reposing in much larger volume. While regrasping and
grasp-and-throw tasks only require matching the target position,
reorientation scenario additionally demands that object rotation
matches the target.
In both regrasping and reorientation the final required
tolerance is ε∗= 1 cm, thus demanding very precise control.
~
\
e
L
1
>
=
|
[NE
3


<!-- page 4 (ocr) -->
TABLE I: Actor/critic observations and their dimensionality. Here
Narm = 1 for single-arm and Narm = 2 for dual-arm tasks, and
Nkp = 4.
INPUT
DIMENSIONALITY
JOINT ANGLES
23D ∗Narm
JOINT VELOCITIES
23D ∗Narm
HAND POSITION
3D ∗Narm
HAND ROTATION
3D ∗Narm
HAND VELOCITY
3D ∗Narm
HAND ANGULAR VELOCITY
3D ∗Narm
FINGERTIP POSITIONS
12D ∗Narm
OBJECT KEYPOINTS REL. TO HAND
3D ∗Nkp ∗Narm
OBJECT KEYPOINTS REL. TO GOAL
3D ∗Nkp
OBJECT ROTATION
4D (QUATERNION)
OBJECT VELOCITY
3D
OBJECT ANGULAR VELOCITY
3D
OBJECT DIMENSIONS
3D
1picked
1D
dclosest
1D
ˆdclosest
1D
TOTAL, ONE ARM TASKS
110D
TOTAL, DUAL-ARM TASKS
192D
For grasp-and-throw we use ε∗= 7.5 cm since the main focus
is on landing the object into the container, not the precise
positioning within it.
Dual-Arm Scenarios. In the attempt to find the limits of end-
to-end learning for continuous control, we introduce versions
of regrasping and reorientation scenarios for two hand-arm
systems. It is likely not a coincidence that humans, sculpted
into a form optimised for object manipulation by evolution,
wield not one but a pair of arms and hands. Thus solving
object reposing with two high-DoF manipulators in simulation
can be seen as a milestone on the path towards future robotic
systems that can match or exceed human dexterity.
To produce dual-arm scenarios we double the number of
simulated robots per task for the total of 46 degrees of
freedom (Figure 1, on the right). We change the sampling
of initial and target object positions in a way that guarantees
that the task cannot be solved by any one robot. Thus,
a complete solution requires grasping the object, passing
the object from one hand to another, as well as in-hand
manipulation, combining the most challenging elements from
all scenarios. We extend both observation (Table I) and action
space (at ∈RNdof ∗Narm, Narm = 2) to allow a single policy
to control both manipulators.
C. Reinforcement Learning
We formalize the problem as a Markov Decision Process
(MDP) where the agent interacts with the environment to
maximize the expected episodic discounted sum of rewards
E[
T
t=0 γtr(st, at)]. We use Proximal Policy Optimization
algorithm [36] to simultaneously learn the policy πθ and the
value function V π
θ (s), both parameterized by a single parameter
vector θ. The model architecture is an LSTM [11] followed by
a 3-layer MLP. Even though agents can observe all relevant
parts of the environment state, we decided to follow prior
work [2, 31] and train recurrent models because any future real-
world deployment will necessarily involve partial observability
and require memory for test-time system identification.
The policy is trained using experience simulated in Isaac
Gym [24], a highly parallelized GPU-accelerated physics
engine. To process high volume of data generated by this
simulator we use an efficient PPO implementation [23] which
keeps the computation graph entirely on the GPU. Combined
with the minibatch size of 215 transitions, this allows us to
maximize the hardware utilization and learning throughput.
We utilize normalization of observations, advantages, and
TD-returns [35] to make the algorithm invariant to absolute
scale of observations and rewards. We also use an adaptive
learning rate algorithm that maintains a constant KL-divergence
DKL(π|πold) between the current policy πθ and the behavior
policy πθold that collected the rollouts. The learning rate is
reduced by a factor of 1.5 whenever DKL exceeds the threshold
by the end of the training iteration, and is multiplied by 1.5
when DKL falls below the threshold.
Both regrasping and reorientation demand very precise
control (ε∗= 1 cm). Because of that, agents almost never
encounter successul task execution early in the training. In
order to create a smooth learning curriculum we adaptively
anneal the tolerance from a larger initial value ε0 = 7.5 cm.
We periodically check if the policy crossed the performance
threshold Nsucc > 3, and in this case we decrease the
current success tolerance until it reaches the final value ε∗:
ε ←max(0.9ε, ε∗).
Reward function. For the successful application of any
reinforcement learning method, the reward should be dense
enough to facilitate exploration yet should not distract the
agent from the sparse final objective (which in our case is to
maximize the number of consecutive successful manipulations).
We propose a reward function that naturally guides the agent
through a sequence of motions required to complete the task,
from reaching for the object to picking it up and moving it to
the final location:
r(s, a) = rreach(s) + rpick(s) + rtarg(s) −rvel(a).
(1)
Here rreach rewards the agent for moving the hand closer
to the object at the start of the attempt:
rreach = αreach ∗max(dclosest −d, 0),
(2)
where both d and dclosest are distances between the end-effector
and the object, d is the current distance, and dclosest is the
closest distance achieved during the attempt so far. In dual-arm
scenarios we calculate distance d for the end-effector that’s
closer to the object.
Component rpick rewards the agent for picking up the object
and lifting it off the table:
rpick = (1 −1picked) ∗αpick ∗ht + rpicked.
(3)
In this equation 1picked is an indicator function which becomes
1 once the height of the object relative to the table ht exceeds
a predefined threshold of 15 cm. At this moment the agent
)3


<!-- page 5 (ocr) -->
receives an additional sparse reward rpicked. Once the object
is picked up, rtarg rewards the agent for moving the object
closer to the target state:
rtarg = 1picked ∗αtarg ∗max( ˆdclosest −ˆd, 0) + rsuccess. (4)
In the reorientation task ˆd =
max
i∈1..Nkp||x(i)
targ −x(i)
kp|| is the
maximum distance between corresponding pairs of object and
target keypoints, while in tasks that do not require orientation
matching ˆd is simply the distance between the object center
and the target location; in both cases ˆdclosest is the smallest
ˆd achieved during the attempt so far. A large sparse reward
rsuccess is added when the desired position and/or orientation
is reached, ˆd = ˆdclosest ≤ε∗.
Finally, rvel in Eq. (1) is a simple joint velocity penalty
that can be tuned to promote smoother movement, and in
Equations (2) to (4) αreach, αpick, αtarg are relative reward
weights. Note that we apply virtually the same reward function
in all scenarios, sans the minor differences in ˆd calculation.
Overall, our reward formulation follows a sequential pattern:
the reward components rreach, rpick and rtarg are mutually
exclusive and do not interfere with each other. For example: by
the time the hand approaches the object, the component rreach
is exhausted since d = dclosest = 0, therefore rreach does not
contribute to the reward for the remainder of the trajectory.
Likewise, rpick̸ = 0 if and only if rtarg = 0 and vice versa
due to the indicator function 1picked. The fact that only one
major reward component guides the motion at each stage of
the trajectory makes it easier to tune the rewards and avoid
interference between reward components. This allows us to
avoid many possible local minima: for example, if rpick and
rtarg are applied together, depending on the relative reward
magnitudes the agent might choose to slide the object to the
edge of the table closer to the target location to maximize
rtarg and cease further attempts to pick it up and solve the
problem for the fear of dropping the object.
In addition to that, rewards in Equations (2) and (4) have
a predefined maximum total value depending on the initial
distance between the hand and the object, and the object and
the target respectively. This eliminates an entire class of reward
hacking behaviors where the agent would remain close but not
quite at the goal to keep collecting the proximity reward. In
our formulation, only movement towards the goal is rewarded
while mere proximity to the goal is not.
Observations and actions. In our experiments both actor πθ
and critic V π
θ (s) observe environment state directly, including
joint angles and velocities, positions of fingertips, object
rotation, velocity, and angular velocity. Additionally, keypoint
positions and object dimensions provide information about the
object shape. Table I lists all observations available to the agent
and their corresponding dimensionalities.
The policy πθ outputs two vectors µ, σ ∈RNdof ∗Narm
which are used as parameters of Ndof ∗Narm independent
Gaussian probability distributions. Actions are sampled from
these distributions a ∼N(µ, σ), clipped to corresponding
joint limits and interpreted as target joint angles. Then a PD
TABLE II: RL hyperparameters and reward function coefficients.
Rightmost column provides an example of the highest scoring
agent’s final parameter values for a single dual-arm reorientation
PBT experiment (parameters not optimized by PBT are omitted).
PARAMETER
INITIAL VALUE
PBT-OPTIMIZED
VALUE
LSTM SIZE
768
-
MLP LAYERS
[768,512,256]
-
NONLINEARITY
ELU
-
DISCOUNT FACTOR γ
0.99
0.9888
GAE DISCOUNT λ [35]
0.95
-
LEARNING RATE
ADAPTIVE (SEC III-C)
-
ADAPT. LR DKL(π|πold)
0.016
0.01432
GRADIENT NORM
1.0
1.028
PPO-CLIP ϵ
0.1
0.2564
CRITIC LOSS COEFF.
4.0
5.188
ENTROPY COEFF.
0
-
NUM. AGENTS
8192
-
MINIBATCH SIZE
32768
-
ROLLOUT LENGTH
16
-
NUM. PPO EPOCHS
2
1
αreach
50
74.8
αpick
20
22.1
rpicked
300
414.4
αtarg
200
263.5
rsuccess
1000
1322.7
controller yields joint torques in order to get joints to the target
angles specified by the policy.
It is unrealistic to expect that all of the mentioned observa-
tions are available on the real robot. In this case, we propose
using all aforementioned observations for the critic during
training, while the policy only receives a subset of observations
that can be obtained from i.e. a vision system, also known as
asymmetric actor-critic approach (see [10, 31]).
D. Population-Based Training
A contact-rich continuous control problem with up to
192 observation dimensions (Table I) and up to 46 action
dimensions can be exceptionally challenging even for modern
RL algorithms [23]. The main challenge is exploration: from the
large number of possible behaviors that maximize rewards early
in the training only relatively few lead to high-performance
solutions at convergence.
Another dimension of complexity when using learning
methods is hyperparameter tuning. Any reward shaping scheme
contains a number of coefficients that need to be carefully
balanced in order to maximize the objective. In addition to
that, modern RL algorithms have a substantial number of
settings, such as learning rate, number of training epochs on
each set of collected trajectories, relative magnitudes of actor
and critic losses, and so on. Choosing these parameters can
be quite challenging and heavily relies on the expertise of
engineers and researchers.
In order to mitigate these problems we employ a Population-
Based Training approach [13]. The core idea is akin to
an evolutionary algorithm: we train a population of agents
P, perform mutation to generate promising hyperparameter
combinations, and use selection to prioritize agents with


<!-- page 6 (ocr) -->
TABLE III: Parameters of the PBT algorithm.
PARAMETER
VALUE
POPULATION SIZE |P|
8, 16, OR 32 AGENTS
POPULATION SPLIT |Ptop|, |Pmid|, |Pbottom|
30%, 40%, 30% OF |P|
INITIAL DELAY Nstart
200,000,000 ENV. STEPS
BURN-IN AFTER MUTATION Nadapt
50,000,000 ENV. STEPS
NORMAL PBT PERIODICITY Niter
20,000,000 ENV. STEPS
MUTATION PROBABILITY βmut
0.2
MIN. PERTURBATION µmin
1.1
MAX. PERTURBATION µmin
1.5
superior performance. Each agent (θi, pi) ∈P is characterized
by a parameter vector θi and a set of hyperparameters pi,
which includes settings of the RL algorithm as well as reward
coefficients αreach, αpick, αtarg, rpicked, rsuccess (see Table II).
Periodically (after training on Niter environment transitions),
each agent is evaluated to obtain the target performance metric
rmeta and the population is sorted according to this metric into
three subsets Ptop, Pmid, Pbottom ⊂P with cardinality equal
to 30%, 40%, and 30% of P respectively (see Figure 2 and
Algorithm 1). Note that for performance reasons we use rmeta
measured at the end of the training iteration to approximate a
separate evaluation procedure EVAL(θ).
Agents that belong to the highest-performing subset Ptop ⊂
P continue training without interruption. Agents in the
middle 40% of the population Pmid undergo hyperapame-
ter mutation and continue training. Underperforming agents
(θ, p) ∈Pbottom are discarded and get replaced with a
randomly sampled high-performing agent (θ∗, p∗) ∼Ptop with
mutated copy of hyperparameters p∗. This algorithm directs
computational resources towards more promising agents in
Ptop and explores numerous hyperparameter combinations,
maximizing exploration (as 70% of the population constantly
undergoes mutation).
The hyperparameter mutation scheme is kept simple: at
each iteration of mutation each regular floating-point hyper-
parameter has a βmut probability to be multiplied or divided
by random number sampled from the uniform distribution
µ ∼U(µmin, µmax) (see Algorithm 2 and Table III for details).
Note that discrete hyperparameters (such as the number of PPO
epochs) and parameters with limited scope (such as discount
factor 0 < γ < 1) require slightly different mutation rules.
Some hyperparameter mutations may temporarily lead to
decreased performance, e.g. even relatively small discount
factor mutations lead to significant changes in the distribution
of TD-returns, thus decreasing the accuracy of the critic. Yet
despite this temporary disadvantage these changes may lead to
long-term benefits. To give agents a chance to adapt to altered
parameters we temporarily pause PBT updates for this agent
for Nadapt = 5 × 107 steps. Similar to Jaderberg et al. [14]
and Petrenko et al. [32] we also enable PBT only Nstart =
2×108 steps after the beginning of training in order to promote
population diversity. This helps us prevent the situation where
the entire population is filled by copies of one particularly
lucky seed.
Meta-objective. One advantage of PBT is that it introduces an
Algorithm 1 Population-Based Training
Require: P (initial population, θ, p sampled randomly)
1: for (θ, p) ∈P do (async. and decentralized)
2:
while not end of training do
3:
θ ←TRAIN(θ, p)
▷Do RL for Niter steps
4:
rmeta ←EVAL(θ)
5:
Ptop, Pmid, Pbottom ⊂P
▷Sort P according to rmeta
6:
(θ∗, p∗) ∼Ptop
▷Get agent from top 30%
7:
if (θ, p) ∈Pbottom then
8:
p ←MUTATE(p∗)
9:
θ ←θ∗
▷Replace weights
10:
else if (θ, p) ∈Pmid then
11:
p ←MUTATE(p)
12:
end if
13:
end while
14: end for
15: return θbest ∈P
▷Agent with the highest rmeta
outer optimization loop that can meta-optimize for a final sparse
scalar objective as opposed to inner RL loop which balances
various dense reward components. Although meta-optimizing
for Nsucc is an obvious choice, the adaptive tolerance annealing
described in Section III-C creates a complication: different
agents in the population can have different current values of
success tolerance ε and therefore cannot be compared directly
as it is much easier to achieve high Nsucc at looser tolerance.
To address this issue, we define our meta-optimization
objective that takes both Nsucc and ε into account:
rmeta =
ε0−ε
ε0−ε∗+ 0.01 ∗Nsucc
if ε > ε∗
rmeta = 1 + Nsucc
if ε = ε∗
(5)
Until the target tolerance ε∗is reached, this objective is
dominated by the term 0 ≤
ε0−ε
ε0−ε∗≤1 which is maximized
when ε approaches ε∗. After the desired tolerance is reached
the maximization of Nsucc is prioritized.
Decentralized PBT. A trait that characterizes our implemen-
tation is a complete lack of any central orchestrator, typically
found in other algorithms [32, 21]. Instead, we propose a
completely decentralized PBT architecture (see Figure 2). In
such architecture, each agent is responsible for execution of
its own part of Algorithm 1, including finding its ranking in
Algorithm 2 Hyperparameter mutation subroutine.
1: function MUTATE(p)
▷Hyperparameter vector p
2:
for j ←1 to len(p) do
3:
z′ ∼U(0, 1)
4:
if zmut < βmut then
▷Mutation probability
5:
µ ∼U(µmin, µmax)
▷Mutation amount
6:
zdir ∼U(0, 1)
▷Mutation direction
7:
if zdir < 0.5 then
8:
pj ←pj ∗µ
9:
else
10:
pj ←pj/µ
11:
end if
12:
end if
13:
end for
14:
return p
15: end function
(


<!-- page 7 (ocr) -->
0
1
2
3
4
5
Env. steps
×109
0
10
20
30
40
Num. successes
Regrasping
0
1
2
3
4
5
Env. steps
×109
0
10
20
30
40
Grasp-And-Throw
0
1
2
3
4
5
Env. steps
×109
0
10
20
30
40
Reorientation
PBT (best)
PBT (mean)
No PBT (best)
No PBT (mean)
0
1
2
3
4
5
Env. steps
×109
0
2
4
6
8
Success tolerance, cm
Reorientation (success tolerance)
Fig. 4: Training curves with and without PBT for single-arm + hand tasks. Shaded area is between the best and the worst policy among 8
agents in P or 8 seeds in non-PBT experiments.
P, mutating its own hyperparameters p, or replacing self with
a copy of another agent.
In our implementation, agents in P interact exclusively
through low-bandwidth access to a shared network directory
containing histories of agent checkpoints and performance
metrics for each agent. This eliminates the need for any
other form of network communication or message passing
between instances and makes it exceptionally easy to deploy
the system, as most popular clusters provide some kind of
shared filesystem. Our approach allows us to run exactly the
same code with NFSv4 on Slurm, sshfs on NGC, S3 on AWS, or
local filesystem on a multi-GPU server, provided that a shared
workspace folder is mounted and accessible via a predefined
path.
The lack of any central controller not only removes a
point of failure, but also allows training in a volatile compute
environment such as a contested cluster where some jobs can
remain in queue for a long time. In this case, agents that start
training later will be at a disadvantage when compared to other
members of P that started earlier. To allow such agents to
contribute to the population, we compare their performance
only to historical checkpoints (of more advanced agents) that
correspond to the same amount of collected experience.
It is almost inevitable that some learners may be lost during
training, e.g. due to random hardware issues. We require
no special treatment for such agents and simply use the
evaluation result from the latest available checkpoint. Although
reduced number of active agents will almost certainly hinder
the exploration capabilities of the algorithm, empirically we
observe that decentralized PBT is quite robust to loss of
one or a few agents, especially with larger population sizes.
Alternatively, is is also possible to detect agent disconnects
in a decentralized way (e.g. by the lack of recent updates)
and exclude such agents from the selection process, effectively
reducing |P|.
IV. EXPERIMENTS
We conduct our experiments using instances with 8 CPU
cores and a single Nvidia V100 GPU with 16 Gb of VRAM.
Using the Isaac Gym engine [24] we are able to simulate
8192 parallel environments on each GPU. Combined with a
GPU-based vectorized RL implementation rl_games [23], this
allows us to reach training throughput of 5 × 104 samples per
second for single-arm tasks and 3.5 × 104 samples per second
for dual-arm scenarios. At this rate, to train successful policies
on 5×109 environment transitions, it takes 30 hours for single-
and 40 hours for dual-arm tasks (PBT and non-PBT training
having almost equivalent per-node throughput).
For non-PBT experiments we simply train policies starting
from multiple random seeds, each trained on a single instance.
In our PBT experiments we use |P| separate 1-GPU instances
that exchange information using low-bandwidth access to a
shared directory (in our case, an NFS/sshfs shared folder on a
Slurm/NGC cluster). Table II lists RL parameters and reward
shaping coefficients used in our experiments.
Figures 4 and 5 demonstrate performance of PBT with
|P| = 8 compared to regular PPO. We use equivalent amount
of compute in both cases and compare the best agent in the
population with the best agent among 8 independent PPO
runs. We find that PBT improves training substantially in all
scenarios, and in three of them PBT becomes the enabling
factor allowing the algorithm to reach non-trivial performance.
For example, in single-arm reorientation task, without PBT
none of the eight single-GPU training sessions reached the
0
1
2
3
4
5
Env. steps
×109
0
10
20
30
40
Num. successes
Dual-Arm Regrasping
0
1
2
3
4
5
Env. steps
×109
0
10
20
30
40
Dual-Arm Reorientation
PBT (best)
PBT (mean)
No PBT (best)
No PBT (mean)
Fig. 5: Training curves with and without PBT for dual-arm + hand
tasks. Shaded area is between the best and the worst policy among 8
agents in P or 8 seeds in non-PBT experiments.
3
hop
in
alt
SE.
ing
Tin
ne
_
WannAT EO
2
WN
Pa ALS
v
W
)
2
”
wr
N=
PRS)
/
1
2
-
Ae
/
y
i
IW
LTE
/
7
“4
Elo tans sannrss snes:
fo
Ap
AY Wo
5
-
nA
p
GATE
ls
SH
f
i
/
//
sanst,
/
~
ant
hl
I57
(I
TRKSOSN
A Le
rE


<!-- page 8 (ocr) -->
0.0
0.2
0.4
0.6
0.8
1.0
Env. steps
×1010
0
10
20
30
40
Num. successes Nsucc
0.0
0.2
0.4
0.6
0.8
1.0
Env. steps
×1010
0.00
0.01
0.02
0.03
Adaptive LR DKL(π|πold) threshold
0.0
0.2
0.4
0.6
0.8
1.0
Env. steps
×1010
0.985
0.990
0.995
Discount factor γ
0.0
0.2
0.4
0.6
0.8
1.0
Env. steps
×1010
0
2
4
6
8
Num. PPO epochs
No PBT, 8 seeds
PBT, 8 agents
PBT, 16 agents
PBT, 32 agents
Fig. 6: Extended PBT experiments on Single-Arm Reorientation task with |P| = 16 and |P| = 32 agents, trained on 10 billion environment
steps. 8-agent PBT run and non-PBT PPO (see Figure 4) trained to 5 billion steps superimposed for comparison. Leftmost plot shows the
performance of the best agent in P and the shaded area is between the best and the worst policy according to Nsucc. Additional plots show
hyperparameter schedules discovered by PBT: adaptive learning rate KL-divergence threshold (Section III-C), RL discount factor γ, and the
number of PPO epochs per training iteration (see Table II). We highlight the mean population value and shade the area between the minimum
and the maximum value of the hyperparameter in P.
target tolerance ε∗(rightmost plot in Figure 4). Of the three
types of scenarios, reorientation relies on exploration the
most: finding the correct approach to in-hand manipulation
is essential, and there are many local optima to get stuck
in. PBT excels at overcoming these challenges. It greatly
amplifies the exploration capabilities of RL by directing
computational resources towards promising agents and trying
multiple combinations of RL hyperparameters and reward
shaping coefficients.
Our learning approach scales well even to dual-arm tasks,
despite the significantly increased overall complexity and ex-
ploration challenges. Moreover, PBT dual-arm agent (Figure 5)
performed better in the reorientation task, reaching almost 40
out of Nmax = 50 successes. The dual-arm task requires the
agent to constantly pass the object from one hand to another,
as a result the policy became more confident at juggling and
tossing the object in-hand, while single-handed agents tend to
rely on more conservative in-hand rotations.
To test the scaling properties of the algorithm we train
populations of 16 and 32 agents on the single-arm reorienta-
tion task, allowing each agent to observe 1010 environment
transitions (the total amount of collected experience in the
|P| = 32 experiment is thus 0.32 trillion environment steps).
We observe that each increase in population size leads to
significant improvement of both convergence speed and final
agent performance, reaching Nsucc > 42 for the best agent
(see Figure 6).
Figure 6 additionally shows some hyperparameter schedules
discovered by PBT. Evidently, meta-optimization tends to prefer
smaller policy updates as training progresses, tightening the
adaptive learning rate KL-divergence threshold (Section III-C).
We hypothesize that high-performing policies become quite
sensitive to large SGD steps, and such schedule helps enforce
the trust region and prevent destructive parameter updates.
Curiously, only our largest experiment (|P| = 32) was able
to find solutions with higher γ. The highest-performing agent
in this experiment employs an alternative strategy: for certain
reorientations it chooses to place the object back on the table,
rotate it, and then pick up again and put the object into the
target position. While this approach is slower, it minimizes
the risk of dropping the object and leads to better long-term
outcomes. We demonstrate this and other learned behaviors in
supplementary videos.
V. CONCLUSIONS
In this paper, we demonstrate the ability of end-to-end
deep RL to learn control policies for sophisticated dexterous
manipulators. We employ Population-Based Training at scale to
train agents that are able to control high-DoF simulated robotic
systems in contact-rich conditions. Although our scenarios only
cover a small part of the robotic dexterity domain, we consider
solving these object reposing challenges to be an important step
on the path toward real-world deployment of robotic systems
with human-level object manipulation capabilities.
While our agents demonstrate strong performance in simu-
lation, many additional obstacles need to be overcome before
practical applications are feasible. Our policies demonstrate
aggressive control on the limits of robot capabilities which can
lead to equipment damage in the real world. One promising
approach is to utilize Riemannian Motion Policies [19] or
Geometric Fabrics [40] to improve safety on the real robot by
imposing conservative motion priors.
One of the most important future research directions is
closing the sim-to-real gap. One approach that has been shown
to improve sim-to-real transfer is the randomization of physical
parameters during training. Projects such as Dactyl [2, 31] have
demonstrated that training policies with domain randomization
is particularly challenging and can require substantial com-
putational budget. Our approach, similar to DeXtreme [10],
based on parallelized physics simulation and high-throughput
GPU-accelerated learning has the potential to significantly
reduce computational requirements for particularly challenging
experiments involving dual arm and hand systems and make
them accessible to a wider research community.
[5
"
J
&
Se
.
%
|
_
In
eat
i £
A.
RN
Ap


<!-- page 9 (ocr) -->
REFERENCES
[1] Arthur Allshire, Mayank Mittal, Varun Lodaya, Vik-
tor Makoviychuk, Denys Makoviichuk, Felix Widmaier,
Manuel Wüthrich, Stefan Bauer, Ankur Handa, and
Animesh Garg. Transferring dexterous manipulation from
GPU simulation to a remote real-world trifinger. CoRR,
abs/2108.09779, 2021. URL https://arxiv.org/abs/2108.
09779. 2, 3
[2] Marcin Andrychowicz, Bowen Baker, Maciek Chociej,
Rafal Józefowicz, Bob McGrew, Jakub Pachocki, Arthur
Petron, Matthias Plappert, Glenn Powell, Alex Ray, Jonas
Schneider, Szymon Sidor, Josh Tobin, Peter Welinder,
Lilian Weng, and Wojciech Zaremba. Learning dexterous
in-hand manipulation. Int. J. Robotics Res., 39(1), 2020.
doi: 10.1177/0278364919887447. URL https://doi.org/10.
1177/0278364919887447. 1, 2, 3, 4, 8
[3] Dhruv Batra, Angel X. Chang, Sonia Chernova, Andrew J.
Davison, Jia Deng, Vladlen Koltun, Sergey Levine, Jiten-
dra Malik, Igor Mordatch, Roozbeh Mottaghi, Manolis
Savva, and Hao Su. Rearrangement: A challenge for
embodied AI.
CoRR, abs/2011.01975, 2020.
URL
https://arxiv.org/abs/2011.01975. 2
[4] Sumeet Batra, Zhehui Huang, Aleksei Petrenko, Tushar
Kumar, Artem Molchanov, and Gaurav S. Sukhatme.
Decentralized control of quadrotor swarms with end-to-
end deep reinforcement learning. In Aleksandra Faust,
David Hsu, and Gerhard Neumann, editors, Confer-
ence on Robot Learning, 8-11 November 2021, London,
UK, volume 164 of Proceedings of Machine Learning
Research, pages 576–586. PMLR, 2021.
URL https:
//proceedings.mlr.press/v164/batra22a.html. 1
[5] Yevgen Chebotar, Ankur Handa, Viktor Makoviychuk,
Miles Macklin, Jan Issac, Nathan D. Ratliff, and Dieter
Fox. Closing the sim-to-real loop: Adapting simulation
randomization with real world experience. In International
Conference on Robotics and Automation, ICRA 2019,
Montreal, QC, Canada, May 20-24, 2019, pages 8973–
8979. IEEE, 2019. doi: 10.1109/ICRA.2019.8793789.
URL https://doi.org/10.1109/ICRA.2019.8793789. 1
[6] Yuanpei Chen, Yaodong Yang, Tianhao Wu, Shengjie
Wang, Xidong Feng, Jiechuang Jiang, Stephen Marcus
McAleer, Hao Dong, Zongqing Lu, and Song-Chun Zhu.
Towards human-level bimanual dexterous manipulation
with reinforcement learning, 2022. 2
[7] Arthur Flajolet, Claire Bizon Monroc, Karim Beguir, and
Thomas Pierrot.
Fast population-based reinforcement
learning on a single machine. In Kamalika Chaudhuri,
Stefanie Jegelka, Le Song, Csaba Szepesvári, Gang Niu,
and Sivan Sabato, editors, International Conference on
Machine Learning, ICML 2022, 17-23 July 2022, Balti-
more, Maryland, USA, volume 162 of Proceedings of Ma-
chine Learning Research, pages 6533–6547. PMLR, 2022.
URL https://proceedings.mlr.press/v162/flajolet22a.html.
2
[8] C. Daniel Freeman, Erik Frey, Anton Raichuk, Sertan
Girgin, Igor Mordatch, and Olivier Bachem. Brax - A
differentiable physics engine for large scale rigid body
simulation. In Joaquin Vanschoren and Sai-Kit Yeung,
editors, Proceedings of the Neural Information Processing
Systems Track on Datasets and Benchmarks 1, NeurIPS
Datasets and Benchmarks 2021, December 2021, virtual,
2021.
URL https://datasets-benchmarks-proceedings.
neurips.cc/paper/2021/hash/
d1f491a404d6854880943e5c3cd9ca25-Abstract-round1.
html. 2
[9] Abhishek Gupta, Justin Yu, Tony Z. Zhao, Vikash Kumar,
Aaron Rovinsky, Kelvin Xu, Thomas Devlin, and Sergey
Levine.
Reset-free reinforcement learning via multi-
task learning: Learning dexterous manipulation behaviors
without human intervention.
In IEEE International
Conference on Robotics and Automation, ICRA 2021,
Xi’an, China, May 30 - June 5, 2021, pages 6664–6671.
IEEE, 2021.
doi: 10.1109/ICRA48506.2021.9561384.
URL https://doi.org/10.1109/ICRA48506.2021.9561384.
2
[10] Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Alek-
sei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makovi-
ichuk, Karl Van Wyk, Alexander Zhurkevich, Balakumar
Sundaralingam, Yashraj Narang, Jean-Francois Lafleche,
Dieter Fox, and Gavriel State. DeXtreme: Transfer of
agile in-hand manipulation from simulation to reality. In
ICRA, 2023. URL https://arxiv.org/abs/2210.13702. 1, 2,
3, 5, 8
[11] Sepp Hochreiter and Jürgen Schmidhuber. Long short-
term memory. Neural Comput., 9(8):1735–1780, 1997.
doi: 10.1162/neco.1997.9.8.1735. URL https://doi.org/10.
1162/neco.1997.9.8.1735. 4
[12] Jemin Hwangbo, Joonho Lee, and Marco Hutter. Per-
contact iteration method for solving contact dynamics.
IEEE Robotics and Automation Letters, 3(2):895–902,
2018. URL www.raisim.com. 2
[13] Max Jaderberg, Valentin Dalibard, Simon Osindero, Wo-
jciech M. Czarnecki, Jeff Donahue, Ali Razavi, Oriol
Vinyals, Tim Green, Iain Dunning, Karen Simonyan,
Chrisantha Fernando, and Koray Kavukcuoglu. Population
based training of neural networks. CoRR, abs/1711.09846,
2017. URL http://arxiv.org/abs/1711.09846. 1, 2, 5
[14] Max Jaderberg, Wojciech M. Czarnecki, Iain Dunning,
Luke Marris, Guy Lever, Antonio García Castañeda,
Charles Beattie, Neil C. Rabinowitz, Ari S. Morcos,
Avraham Ruderman, Nicolas Sonnerat, Tim Green, Louise
Deason, Joel Z. Leibo, David Silver, Demis Hassabis,
Koray Kavukcuoglu, and Thore Graepel. Human-level
performance in first-person multiplayer games with
population-based deep reinforcement learning.
CoRR,
abs/1807.01281, 2018.
URL http://arxiv.org/abs/1807.
01281. 2, 6
[15] Dmitry Kalashnikov, Alex Irpan, Peter Pastor, Julian
Ibarz, Alexander Herzog, Eric Jang, Deirdre Quillen,
Ethan Holly, Mrinal Kalakrishnan, Vincent Vanhoucke,
and Sergey Levine. Qt-opt: Scalable deep reinforcement


<!-- page 10 (ocr) -->
learning for vision-based robotic manipulation. CoRR,
abs/1806.10293, 2018.
URL http://arxiv.org/abs/1806.
10293. 2
[16] Vikash Kumar, Emanuel Todorov, and Sergey Levine.
Optimal control with learned local models: Application
to dexterous manipulation. In Danica Kragic, Antonio
Bicchi, and Alessandro De Luca, editors, 2016 IEEE
International Conference on Robotics and Automation,
ICRA 2016, Stockholm, Sweden, May 16-21, 2016, pages
378–383. IEEE, 2016. doi: 10.1109/ICRA.2016.7487156.
URL https://doi.org/10.1109/ICRA.2016.7487156. 2
[17] Joonho Lee, Jemin Hwangbo, Lorenz Wellhausen, Vladlen
Koltun, and Marco Hutter. Learning quadrupedal loco-
motion over challenging terrain. Sci. Robotics, 5(47):
5986, 2020.
doi: 10.1126/scirobotics.abc5986.
URL
https://doi.org/10.1126/scirobotics.abc5986. 1, 2
[18] Sergey Levine, Chelsea Finn, Trevor Darrell, and Pieter
Abbeel. End-to-end training of deep visuomotor policies.
Journal of Machine Learning Research, 17(39):1–40,
2016. URL http://jmlr.org/papers/v17/15-522.html. 2
[19] Anqi Li, Ching-An Cheng, Muhammad Asif Rana, Man
Xie, Karl Van Wyk, Nathan D. Ratliff, and Byron Boots.
RMP2: A structured composable policy class for robot
learning.
In Dylan A. Shell, Marc Toussaint, and
M. Ani Hsieh, editors, Robotics: Science and Systems
XVII, Virtual Event, July 12-16, 2021, 2021.
doi:
10.15607/RSS.2021.XVII.092.
URL https://doi.org/10.
15607/RSS.2021.XVII.092. 8
[20] Zexiang Li, Ping Hsu, and Shankar Sastry. Grasping
and coordinated manipulation by a multifingered robot
hand. The International Journal of Robotics Research,
8(4):33–50, 1989. doi: 10.1177/027836498900800402.
URL https://doi.org/10.1177/027836498900800402. 2
[21] Richard Liaw, Eric Liang, Robert Nishihara, Philipp
Moritz, Joseph E. Gonzalez, and Ion Stoica.
Tune:
A research platform for distributed model selection
and training.
CoRR, abs/1807.05118, 2018.
URL
http://arxiv.org/abs/1807.05118. 6
[22] Siqi Liu, Guy Lever, Zhe Wang, Josh Merel, S. M. Ali
Eslami, Daniel Hennes, Wojciech M. Czarnecki, Yu-
val Tassa, Shayegan Omidshafiei, Abbas Abdolmaleki,
Noah Y. Siegel, Leonard Hasenclever, Luke Marris, Saran
Tunyasuvunakool, H. Francis Song, Markus Wulfmeier,
Paul Muller, Tuomas Haarnoja, Brendan D. Tracey, Karl
Tuyls, Thore Graepel, and Nicolas Heess. From motor
control to team play in simulated humanoid football. Sci.
Robotics, 7(69), 2022. doi: 10.1126/scirobotics.abo0235.
URL https://doi.org/10.1126/scirobotics.abo0235. 1
[23] Denys Makoviichuk and Viktor Makoviychuk. RL Games,
2021. URL https://github.com/Denys88/rl_games/. 4, 5,
7
[24] Viktor Makoviychuk, Lukasz Wawrzyniak, Yunrong Guo,
Michelle Lu, Kier Storey, Miles Macklin, David Hoeller,
Nikita Rudin, Arthur Allshire, Ankur Handa, and Gavriel
State. Isaac gym: High performance gpu-based physics
simulation for robot learning. CoRR, abs/2108.10470,
2021. URL https://arxiv.org/abs/2108.10470. 1, 2, 4, 7
[25] Matthew T. Mason and J. Kenneth Salisbury.
Robot
Hands and the Mechanics of Manipulation. MIT Press,
Cambridge, MA, USA, 1985. ISBN 0262132052. 2
[26] Matthew Matl, Vishal Satish, Michael Danielczuk, Bill
DeRose, Stephen McKinley, and Ken Goldberg. Learning
ambidextrous robot grasping policies. Sci. Robotics, 4
(26), 2019. doi: 10.1126/scirobotics.aau4984. URL https:
//doi.org/10.1126/scirobotics.aau4984. 1, 2
[27] Takahiro Miki, Joonho Lee, Jemin Hwangbo, Lorenz
Wellhausen, Vladlen Koltun, and Marco Hutter. Learning
robust perceptive locomotion for quadrupedal robots
in the wild.
Sci. Robotics, 7(62), 2022.
doi: 10.
1126/scirobotics.abk2822. URL https://doi.org/10.1126/
scirobotics.abk2822. 1
[28] Artem Molchanov, Tao Chen, Wolfgang Hönig, James A.
Preiss, Nora Ayanian, and Gaurav S. Sukhatme. Sim-to-
(multi)-real: Transfer of low-level robust control policies
to multiple quadrotors. In 2019 IEEE/RSJ International
Conference on Intelligent Robots and Systems, IROS 2019,
Macau, SAR, China, November 3-8, 2019, pages 59–
66. IEEE, 2019. doi: 10.1109/IROS40897.2019.8967695.
URL https://doi.org/10.1109/IROS40897.2019.8967695.
1
[29] Yashraj S. Narang, Kier Storey, Iretiayo Akinola, Miles
Macklin, Philipp Reist, Lukasz Wawrzyniak, Yunrong
Guo, Ádám Moravánszky, Gavriel State, Michelle Lu,
Ankur Handa, and Dieter Fox. Factory: Fast contact for
robotic assembly. CoRR, abs/2205.03532, 2022. doi: 10.
48550/arXiv.2205.03532. URL https://doi.org/10.48550/
arXiv.2205.03532. 1
[30] Allison M. Okamura, Niels Smaby, and Mark R. Cutkosky.
An overview of dexterous manipulation. In Proceedings
of the 2000 IEEE International Conference on Robotics
and Automation, ICRA 2000, April 24-28, 2000, San
Francisco, CA, USA, pages 255–262. IEEE, 2000. doi:
10.1109/ROBOT.2000.844067. URL https://doi.org/10.
1109/ROBOT.2000.844067. 3
[31] OpenAI, Ilge Akkaya, Marcin Andrychowicz, Maciek
Chociej, Mateusz Litwin, Bob McGrew, Arthur Petron,
Alex Paino, Matthias Plappert, Glenn Powell, Raphael
Ribas, Jonas Schneider, Nikolas Tezak, Jerry Tworek,
Peter Welinder, Lilian Weng, Qiming Yuan, Wojciech
Zaremba, and Lei Zhang. Solving rubik’s cube with a
robot hand. arXiv preprint, 2019. 1, 2, 3, 4, 5, 8
[32] Aleksei Petrenko, Zhehui Huang, Tushar Kumar, Gau-
rav S. Sukhatme, and Vladlen Koltun. Sample factory:
Egocentric 3d control from pixels at 100000 FPS with
asynchronous reinforcement learning. In Proceedings of
the 37th International Conference on Machine Learning,
ICML 2020, 13-18 July 2020, Virtual Event, volume 119
of Proceedings of Machine Learning Research, pages
7652–7662. PMLR, 2020. URL http://proceedings.mlr.
press/v119/petrenko20a.html. 2, 6
[33] Nikita Rudin, David Hoeller, Philipp Reist, and Marco
Hutter. Learning to walk in minutes using massively


<!-- page 11 (ocr) -->
parallel deep reinforcement learning. In Aleksandra Faust,
David Hsu, and Gerhard Neumann, editors, Proceedings
of the 5th Conference on Robot Learning, volume 164
of Proceedings of Machine Learning Research, pages 91–
100. PMLR, 08–11 Nov 2022. URL https://proceedings.
mlr.press/v164/rudin22a.html. 2
[34] J. Kenneth Salisbury and John J. Craig. Articulated hands:
Force control and kinematic issues. The International
Journal of Robotics Research, 1(1):4–17, 1982. doi: 10.
1177/027836498200100102. URL https://doi.org/10.1177/
027836498200100102. 2
[35] John Schulman, Philipp Moritz, Sergey Levine, Michael I.
Jordan, and Pieter Abbeel. High-dimensional continuous
control using generalized advantage estimation.
In
Yoshua Bengio and Yann LeCun, editors, 4th International
Conference on Learning Representations, ICLR 2016, San
Juan, Puerto Rico, May 2-4, 2016, Conference Track
Proceedings, 2016. URL http://arxiv.org/abs/1506.02438.
4, 5
[36] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec
Radford, and Oleg Klimov. Proximal policy optimization
algorithms. CoRR, abs/1707.06347, 2017. URL http:
//arxiv.org/abs/1707.06347. 4
[37] Yunlong Song, Mats Steinweg, Elia Kaufmann, and
Davide Scaramuzza.
Autonomous drone racing with
deep reinforcement learning. In IEEE/RSJ International
Conference on Intelligent Robots and Systems, IROS 2021,
Prague, Czech Republic, September 27 - Oct. 1, 2021,
pages 1205–1212. IEEE, 2021. doi: 10.1109/IROS51168.
2021.9636053. URL https://doi.org/10.1109/IROS51168.
2021.9636053. 1
[38] Oriol Vinyals, Igor Babuschkin, Wojciech M. Czarnecki,
Michaël Mathieu, Andrew Dudzik, Junyoung Chung,
David H. Choi, Richard Powell, Timo Ewalds, Petko
Georgiev, Junhyuk Oh, Dan Horgan, Manuel Kroiss,
Ivo Danihelka, Aja Huang, Laurent Sifre, Trevor Cai,
John P. Agapiou, Max Jaderberg, Alexander S. Vezhnevets,
Rémi Leblond, Tobias Pohlen, Valentin Dalibard, David
Budden, Yury Sulsky, James Molloy, Tom L. Paine, Caglar
Gulcehre, Ziyu Wang, Tobias Pfaff, Yuhuai Wu, Roman
Ring, Dani Yogatama, Dario Wünsch, Katrina McKinney,
Oliver Smith, Tom Schaul, Timothy Lillicrap, Koray
Kavukcuoglu, Demis Hassabis, Chris Apps, and David
Silver. Grandmaster level in starcraft ii using multi-agent
reinforcement learning. Nature, 575(7782):350–354, 2019.
2
[39] Xingchen Wan, Cong Lu, Jack Parker-Holder, Philip J.
Ball, Vu Nguyen, Binxin Ru, and Michael Osborne.
Bayesian generational population-based training.
In
First Conference on Automated Machine Learning (Main
Track), 2022.
URL https://openreview.net/forum?id=
HW4-ZaHUg5. 2
[40] Karl Van Wyk, Mandy Xie, Anqi Li, Muhammad Asif
Rana, Buck Babich, Bryan Peele, Qian Wan, Iretiayo
Akinola, Balakumar Sundaralingam, Dieter Fox, By-
ron Boots, and Nathan D. Ratliff. Geometric fabrics:
Generalizing classical mechanics to capture the physics
of behavior.
IEEE Robotics Autom. Lett., 7(2):3202–
3209, 2022.
doi: 10.1109/LRA.2022.3143311.
URL
https://doi.org/10.1109/LRA.2022.3143311. 8
[41] Tete Xiao, Ilija Radosavovic, Trevor Darrell, and Jitendra
Malik.
Masked visual pre-training for motor control.
arXiv preprint arXiv:2203.06173, 2022. 2
