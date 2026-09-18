# asymdex_2024

source: https://github.com/GT-STAR-Lab/AsymDex


commit: 40b29f950f8ee12024f685a5300e0e4a57729026


## README

# AsymDex

**Installation**

Details regarding installation of IsaacGym can be found [here](https://developer.nvidia.com/isaac-gym). It is suggested to create a conda environment following the instruction in IsaacGym documentation.

After activating the conda environment, in the AsymDex root directory, `pip install -e .`

in the Isaac Gym Release python folder, `pip install -e .`

**Running**

```
cd ./bidexhands
```

Training AsymDex policy:

`python train.py --task=AllegroHandDualArmGraspAndPlaceAsymDex --algo=ppo --bimanual_action`

`python train.py --task=AllegroHandDualArmGraspAndPlaceAsymDex --algo=ppo --bimanual_action --num_envs=2048 --headless `

Rollout the trained AsymDex policy:

`python train.py --task=AllegroHandDualArmGraspAndPlaceAsymDex --algo=ppo --bimanual_action --test --model_dir=./logs/AllegroHandDualArmGraspAndPlaceAsymDex/ppo/ppo_seed-1/model_best.pt`

## File tree (depth 3, assets pruned)

```
.gitignore
README.md
bidexhands/
  __init__.py
  algorithms/
    __init__.py
    marl/
    metarl/
    mtrl/
    offrl/
    rl/
    utils/
  cfg/
    AbilityHandGraspAndPlaceRelative.yaml
    AllegroHandCatchUnderarm.yaml
    AllegroHandDualArmGraspAndPlaceAsymDex.yaml
    AllegroHandDualArmGraspAndPlaceAsymOnly.yaml
    AllegroHandDualArmGraspAndPlaceHardwareAsymDex.yaml
    AllegroHandDualArmGraspAndPlaceMonolithic.yaml
    AllegroHandDualArmGraspAndPlaceRelOnly.yaml
    AllegroHandDualArmPourAsymDex.yaml
    AllegroHandDualArmPourAsymOnly.yaml
    AllegroHandDualArmPourBallHardwareAsymDex.yaml
    AllegroHandDualArmPourHardwareAsymDex.yaml
    AllegroHandDualArmPourMonolithic.yaml
    AllegroHandDualArmPourRelOnly.yaml
    AllegroHandDualArmStirHardwareAsymDex.yaml
    AllegroHandDualArmTwistLidAsymDex.yaml
    AllegroHandDualArmTwistLidAsymOnly.yaml
    AllegroHandDualArmTwistLidHardwareAsymDex.yaml
    AllegroHandDualArmTwistLidMonolithic.yaml
    AllegroHandDualArmTwistLidRelOnly.yaml
    AllegroHandGraspAndPlaceDualArmRandom.yaml
    AllegroHandGraspAndPlaceRelative.yaml
    AllegroHandGraspAndPlaceRelativeDualArm.yaml
    AllegroHandGraspAndPlaceRelativeRealWorld.yaml
    AllegroHandOver.yaml
    ShadowHandBlockStack.yaml
    ShadowHandBottleCap.yaml
    ShadowHandBottleCapInteractionNaive.yaml
    ShadowHandBottleCapInteractionRelative.yaml
    ShadowHandBottleCapNaive.yaml
    ShadowHandBottleCapOneStage.yaml
    ShadowHandBottleCapPreGrasp.yaml
    ShadowHandBottleCapRelOnly.yaml
    ShadowHandBottleCapRelative.yaml
    ShadowHandBottleCapTwoStages.yaml
    ShadowHandBottleCapTwoStagesNaive.yaml
    ShadowHandBottleCapTwoStagesRelative.yaml
    ShadowHandCatchAbreast.yaml
    ShadowHandCatchOver2Underarm.yaml
    ShadowHandCatchUnderarm.yaml
    ShadowHandDoorCloseInward.yaml
    ShadowHandDoorCloseOutward.yaml
    ShadowHandDoorOpenInward.yaml
    ShadowHandDoorOpenOutward.yaml
    ShadowHandGraspAndPlace.yaml
    ShadowHandGraspAndPlaceDominantPreGrasp.yaml
    ShadowHandGraspAndPlaceFacilitatingPreGrasp.yaml
    ShadowHandGraspAndPlaceInteractionNaive.yaml
    ShadowHandGraspAndPlaceInteractionRelative.yaml
    ShadowHandGraspAndPlaceNaive.yaml
    ShadowHandGraspAndPlaceOneStage.yaml
    ShadowHandGraspAndPlacePreGrasp.yaml
    ShadowHandGraspAndPlaceRelOnly.yaml
    ShadowHandGraspAndPlaceRelative.yaml
    ShadowHandGraspAndPlaceRelativeTrueBimanual.yaml
    ShadowHandGraspAndPlaceTwoStagesNaive.yaml
    ShadowHandGraspAndPlaceTwoStagesRelative.yaml
    ShadowHandKettle.yaml
    ShadowHandKettleAsymOnly.yaml
    ShadowHandKettleNaive.yaml
    ShadowHandKettleRelOnly.yaml
    ShadowHandKettleRelative.yaml
    ShadowHandLiftUnderarm.yaml
    ShadowHandOver.yaml
    ShadowHandPen.yaml
    ShadowHandPenOnTableNaive.yaml
    ShadowHandPenOnTableRelative.yaml
    ShadowHandPenRelative.yaml
    ShadowHandPushBlock.yaml
    ShadowHandReOrientation.yaml
    ShadowHandScissors.yaml
    ShadowHandScissorsRelative.yaml
    ShadowHandStackCup.yaml
    ShadowHandStackCupNaive.yaml
    ShadowHandStackCupRelOnly.yaml
    ShadowHandStackCupRelative.yaml
    ShadowHandSwingCup.yaml
    ShadowHandSwitch.yaml
    ShadowHandSwitchNaive.yaml
    ShadowHandSwitchRelOnly.yaml
    ShadowHandSwitchRelative.yaml
    ShadowHandTakeOutBlockRelative.yaml
    ShadowHandTwoCatchUnderarm.yaml
    ShadowSingleHandBottleCap.yaml
    ShadowSingleHandPen.yaml
    bcq/
    ddpg/
    happo/
    hatrpo/
    ippo/
    iql/
    maddpg/
    mamlppo/
    mappo/
    meta_env_cfg/
    mtppo/
    mtsac/
    mttrpo/
    ppo/
    ppo_collect/
    random/
    sac/
    td3/
    td3_bc/
    trpo/
  check_log.py
  plot.py
  tasks/
    __init__.py
    ability_hand_grasp_and_place_relative.py
    allegro_hand_catch_underarm.py
    allegro_hand_dual_arm_grasp_and_place_asym_only.py
    allegro_hand_dual_arm_grasp_and_place_asymdex.py
    allegro_hand_dual_arm_grasp_and_place_hardware_asymdex.py
    allegro_hand_dual_arm_grasp_and_place_monolithic.py
    allegro_hand_dual_arm_grasp_and_place_rel_only.py
    allegro_hand_dual_arm_pour_asym_only.py
    allegro_hand_dual_arm_pour_asymdex.py
    allegro_hand_dual_arm_pour_ball_hardware_asymdex.py
    allegro_hand_dual_arm_pour_hardware_asymdex.py
    allegro_hand_dual_arm_pour_monolithic.py
    allegro_hand_dual_arm_pour_rel_only.py
    allegro_hand_dual_arm_stir_hardware_asymdex.py
    allegro_hand_dual_arm_twist_lid_asym_only.py
    allegro_hand_dual_arm_twist_lid_asymdex.py
    allegro_hand_dual_arm_twist_lid_hardware_asymdex.py
    allegro_hand_dual_arm_twist_lid_monolithic.py
    allegro_hand_dual_arm_twist_lid_rel_only.py
    allegro_hand_grasp_and_place_dual_arm_random.py
    allegro_hand_grasp_and_place_relative.py
    allegro_hand_grasp_and_place_relative_dual_arm.py
    allegro_hand_grasp_and_place_relative_real_world.py
    allegro_hand_over.py
    hand_base/
    shadow_hand_block_stack.py
    shadow_hand_bottle_cap.py
    shadow_hand_bottle_cap_interaction_naive.py
    shadow_hand_bottle_cap_interaction_relative.py
    shadow_hand_bottle_cap_naive.py
    shadow_hand_bottle_cap_one_stage.py
    shadow_hand_bottle_cap_pre_grasp.py
    shadow_hand_bottle_cap_rel_only.py
    shadow_hand_bottle_cap_relative.py
    shadow_hand_bottle_cap_two_stages.py
    shadow_hand_bottle_cap_two_stages_naive.py
    shadow_hand_bottle_cap_two_stages_naive_train_with_first_stage.py
    shadow_hand_bottle_cap_two_stages_relative.py
    shadow_hand_bottle_cap_two_stages_relative_train_with_first_stage.py
    shadow_hand_catch_abreast.py
    shadow_hand_catch_over2underarm.py
    shadow_hand_catch_underarm.py
    shadow_hand_door_close_inward.py
    shadow_hand_door_close_outward.py
    shadow_hand_door_open_inward.py
    shadow_hand_door_open_outward.py
    shadow_hand_grasp_and_place.py
    shadow_hand_grasp_and_place_dominant_pre_grasp.py
    shadow_hand_grasp_and_place_facilitating_pre_grasp.py
    shadow_hand_grasp_and_place_interaction_naive.py
    shadow_hand_grasp_and_place_interaction_relative.py
    shadow_hand_grasp_and_place_naive.py
    shadow_hand_grasp_and_place_one_stage.py
    shadow_hand_grasp_and_place_pre_grasp.py
    shadow_hand_grasp_and_place_rel_only.py
    shadow_hand_grasp_and_place_relative.py
    shadow_hand_grasp_and_place_relative_true_bimanual.py
    shadow_hand_grasp_and_place_two_stages_naive.py
    shadow_hand_grasp_and_place_two_stages_relative.py
    shadow_hand_kettle.py
    shadow_hand_kettle_asym_only.py
    shadow_hand_kettle_naive.py
    shadow_hand_kettle_rel_only.py
    shadow_hand_kettle_relative.py
    shadow_hand_lift_underarm.py
    shadow_hand_meta/
    shadow_hand_over.py
    shadow_hand_pen.py
    shadow_hand_pen_on_table_naive.py
    shadow_hand_pen_on_table_relative.py
    shadow_hand_pen_relative.py
    shadow_hand_point_cloud.py
    shadow_hand_push_block.py
    shadow_hand_re_orientation.py
    shadow_hand_scissors.py
    shadow_hand_scissors_relative.py
    shadow_hand_stack_cup.py
    shadow_hand_stack_cup_naive.py
    shadow_hand_stack_cup_rel_only.py
    shadow_hand_stack_cup_relative.py
    shadow_hand_swing_cup.py
    shadow_hand_switch.py
    shadow_hand_switch_naive.py
    shadow_hand_switch_rel_only.py
    shadow_hand_switch_relative.py
    shadow_hand_switch_relative_temp.py
    shadow_hand_take_out_block_relative.py
    shadow_hand_two_catch_underarm.py
    shadow_single_hand_bottle.py
    shadow_single_hand_bottle_cap.py
    shadow_single_hand_bottle_cap_temp.py
    shadow_single_hand_pen.py
  train.py
  train_customize.py
  train_rlgames.py
  utils/
    __init__.py
    config.py
    logger/
    o3dviewer.py
    package_utils.py
    parse_task.py
    process_marl.py
    process_metarl.py
    process_mtrl.py
    process_offrl.py
    process_sarl.py
    torch_jit_utils.py
    util.py
requirements.txt
setup.py
```

## Config files (119)


### bidexhands/cfg/AbilityHandGraspAndPlaceRelative.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "ability_hand_grasp_and_place_relative"
  numEnvs: 128
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.5
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "Ability_URDF/ability_hand_right_large.urdf"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandCatchUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_catch_underarm"
  numEnvs: 8
  envSpacing: 1.25
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmGraspAndPlaceAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_asymdex"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 250 # 50
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmGraspAndPlaceAsymOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_asym_only"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 250 # 50
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmGraspAndPlaceHardwareAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_grasp_and_place_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmGraspAndPlaceMonolithic.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_monolithic"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 250 # 50
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmGraspAndPlaceRelOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_rel_only"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 250 # 50
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_pour_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 350
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourAsymOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 350
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourBallHardwareAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourHardwareAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourMonolithic.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 350
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmPourRelOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 350
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmStirHardwareAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_stir_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 100
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmTwistLidAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_twist_lid_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.5
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmTwistLidAsymOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_twist_lid_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.5
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmTwistLidHardwareAsymDex.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_twist_lid_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.5
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmTwistLidMonolithic.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_twist_lid_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.5
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandDualArmTwistLidRelOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_dual_arm_twist_lid_hardware_asymdex"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 0.5
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandGraspAndPlaceDualArmRandom.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_dual_arm_random"
  numEnvs: 1
  envSpacing: 1.0
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandGraspAndPlaceRelative.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandGraspAndPlaceRelativeDualArm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_real_world"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 50
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 5 # 12 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandGraspAndPlaceRelativeRealWorld.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_grasp_and_place_relative_real_world"
  numEnvs: 1
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/AllegroHandOver.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "allegro_hand_over"
  numEnvs: 8
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: False
  pointCloudDebug: False
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.005
  startRotationNoise: 0.0

  resetPositionNoise: 0.005
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # 
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBlockStack.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_block_stack"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.2
  orientation_scale: 0.02
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "block" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCap.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap_relative"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapInteractionNaive.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapInteractionRelative.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapNaive.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapOneStage.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 120
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapPreGrasp.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapRelOnly.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapRelative.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 400
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapTwoStages.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 200
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapTwoStagesNaive.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 120
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandBottleCapTwoStagesRelative.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_bottle_cap"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 120
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 0.1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 4
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandCatchAbreast.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_abreast"
  numEnvs: 256
  envSpacing: 0.75
  episodeLength: 150
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  transition_scale: 0.5
  orientation_scale: 1
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.65
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandCatchOver2Underarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_over2underarm"
  numEnvs: 256
  envSpacing: 1
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.1
  orientation_scale: 2
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 2
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandCatchUnderarm.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_catch_underarm"
  numEnvs: 256
  envSpacing: 0.75
  episodeLength: 75
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.01
  startRotationNoise: 0.0

  resetPositionNoise: 0.01
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.2
  resetDofVelRandomInterval: 0.0

  distRewardScale: 50
  transition_scale: 0.05
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.65
  fallPenalty: 0.0

  objectType: "egg" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

### bidexhands/cfg/ShadowHandDoorCloseInward.yaml

```yaml
# if given, will override the device setting in gym. 
env: 
  env_name: "shadow_hand_door_close_inward"
  numEnvs: 256
  envSpacing: 1.5
  episodeLength: 250
  enableDebugVis: False
  cameraDebug: True
  pointCloudDebug: True
  aggregateMode: 1

  stiffnessScale: 1.0
  forceLimitScale: 1.0
  useRelativeControl: False
  dofSpeedScale: 20.0
  actionsMovingAverage: 1.0
  controlFrequencyInv: 1 # 60 Hz

  startPositionNoise: 0.0
  startRotationNoise: 0.0

  resetPositionNoise: 0.0
  resetRotationNoise: 0.0
  resetDofPosRandomInterval: 0.0
  resetDofVelRandomInterval: 0.0

  distRewardScale: 20
  transition_scale: 0.5
  orientation_scale: 0.5
  rotRewardScale: 1.0
  rotEps: 0.1
  actionPenaltyScale: -0.0002
  reachGoalBonus: 250
  fallDistance: 0.4
  fallPenalty: 0.0

  objectType: "pot" # can be block, egg or pen
  observationType: "full_state" # point_cloud or full_state
  handAgentIndex: "[[0, 1, 2, 3, 4, 5]]"
  asymmetric_observations: False
  successTolerance: 0.1
  printNumSuccesses: False
  maxConsecutiveSuccesses: 0

  asset:
    assetRoot: "../assets"
    assetFileName: "mjcf/open_ai_assets/hand/shadow_hand.xml"
    assetFileNameBlock: "urdf/objects/cube_multicolor.urdf"
    assetFileNameEgg: "mjcf/open_ai_assets/hand/egg.xml"
    assetFileNamePen: "mjcf/open_ai_assets/hand/pen.xml"

task:
  randomize: False
  randomization_params:
    frequency: 600   # Define how many simulation steps between generating new randomizations
    observations:
      range: [0, .002] # range for the white noise
      range_correlated: [0, .001 ] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"   # "constant" is to turn on noise after `schedule_steps` num steps
      schedule_steps: 40000
    actions:
      range: [0., .05]
      range_correlated: [0, .015] # range for correlated noise, refreshed with freq `frequency`
      operation: "additive"
      distribution: "gaussian"
      schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
      schedule_steps: 40000
    sim_params: 
      gravity:
        range: [0, 0.4]
        operation: "additive"
        distribution: "gaussian"
        schedule: "linear"  # "linear" will linearly interpolate between no rand and max rand
        schedule_steps: 40000
    actor_params:
      hand:
        color: True
        tendon_properties:
          damping:
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness:
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        dof_properties:
          damping: 
            range: [0.3, 3.0]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          stiffness: 
            range: [0.75, 1.5]
            operation: "scaling"
            distribution: "loguniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          lower:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
          upper:
            range: [0, 0.01]
            operation: "additive"
            distribution: "gaussian"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction: 
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
      object:
        scale:
          range: [0.95, 1.05]
          operation: "scaling"
          distribution: "uniform"
          schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
          schedule_steps: 30000
        rigid_body_properties:
          mass: 
            range: [0.5, 1.5]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by ``min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000
        rigid_shape_properties:
          friction:
            num_buckets: 250
            range: [0.7, 1.3]
            operation: "scaling"
            distribution: "uniform"
            schedule: "linear"  # "linear" will scale the current random sample by `min(current num steps, schedule_steps) / schedule_steps`
            schedule_steps: 30000

sim:
  substeps: 2
  physx:
    num_threads: 4
    solver_type: 1  # 0: pgs, 1: tgs
    num_position_iterations: 8
    num_velocity_iterations: 0
    contact_offset: 0.002
    rest_offset: 0.0
    bounce_threshold_velocity: 0.2
    max_depenetration_velocity: 1000.0
    default_buffer_size_multiplier: 5.0
  flex:
    num_outer_iterations: 5
    num_inner_iterations: 20
    warm_start: 0.8
    relaxation: 0.75

```

## Python signatures and reward/observation bodies (206 files)


### bidexhands/algorithms/marl/actor_critic.py

```
class Actor(Module)
    """Actor network class for HAPPO. Outputs actions given observations.
:param args: (argparse.Namespace) arguments containing relevant model information.
:param obs_space: (gym.Space) observation space.
:param action_space: (gym.Space) action space.
:param device: (torch.device) specifies the device to """
    def __init__(self, config, obs_space, action_space, device)
    def forward(self, obs, rnn_states, masks, available_actions, deterministic)
    def evaluate_actions(self, obs, rnn_states, action, masks, available_actions, active_masks)
class Critic(Module)
    """Critic network class for HAPPO. Outputs value function predictions given centralized input (HAPPO) or local observations (IPPO).
:param args: (argparse.Namespace) arguments containing relevant model information.
:param cent_obs_space: (gym.Space) (centralized) observation space.
:param device: (torc"""
    def __init__(self, config, cent_obs_space, device)
    def forward(self, cent_obs, rnn_states, masks)
```

### bidexhands/algorithms/marl/happo_policy.py

```
class HAPPO_Policy()
    """HAPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function in"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/happo_trainer.py

```
class HAPPO()
    """Trainer class for HAPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (HAPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/hatrpo_policy.py

```
class HATRPO_Policy()
    """HATRPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function i"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/hatrpo_trainer.py

```
class HATRPO()
    """Trainer class for MATRPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (HATRPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def flat_grad(self, grads)
    def flat_hessian(self, hessians)
    def flat_params(self, model)
    def update_model(self, model, new_params)
    def kl_approx(self, q, p)
    def kl_divergence(self, obs, rnn_states, action, masks, available_actions, active_masks, new_actor, old_actor)
    def conjugate_gradient(self, actor, obs, rnn_states, action, masks, available_actions, active_masks, b, nsteps, residual_tol)
    def fisher_vector_product(self, actor, obs, rnn_states, action, masks, available_actions, active_masks, p)
    def trpo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/ippo_policy.py

```
"""# @Time    : 2021/7/1 6:53 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : rMAPPOPolicy.py
refer to ....."""
class IPPO_Policy()
    """IPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function inp"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/ippo_trainer.py

```
"""# @Time    : 2021/7/1 6:52 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : r_mappo.py"""
class IPPO()
    """Trainer class for IPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (IPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/maddpg/module.py

```
def get_activation(act_name)
def mlp(sizes, activation, output_activation)
class MLPActLayer(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class Actor(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation, device)
    def act(self, obs)
class Critic(Module)
    def __init__(self, share_observation_space, share_action_space, hidden_sizes, activation, device)
    def get_value(self, share_obs, share_acts)
class MADDPG_policy()
    def __init__(self, config, obs_space, cent_obs_space, act_space, cent_act_space, device)
    def get_actions(self, obs, deterministic)
    def get_values(self, cent_obs, cent_acts)
    def act(self, obs, deterministic)
class MADDPG()
    def __init__(self, config, policy, num_agents, device)
    def cal_value_loss(self, data, nid)
    def cal_pi_loss(self, data, id)
    def ddpg_update(self, samples)
    def train(self, buffer)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/maddpg/runner.py

```
def _t2n(x)
class Runner()
    def __init__(self, vec_env, config, model_dir)
    def run(self)
    def collect(self, step)
    def insert(self, data)
    def log_train(self, train_infos, total_num_steps)
    def train(self)
    def save(self)
    def restore(self)
    def log_train(self, train_infos, total_num_steps)
    def log_env(self, env_infos, total_num_steps)
    def eval(self, total_num_steps)
```

### bidexhands/algorithms/marl/maddpg/storage.py

```
class ReplayBuffer()
    def __init__(self, config, obs_shape, share_obs_shape, actions_shape, joint_actions_shape, device)
    def add_transitions(self, observations, share_obs, actions, joint_actions, rewards, next_obs, next_state, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/marl/mappo_policy.py

```
"""# @Time    : 2021/7/1 6:53 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : rMAPPOPolicy.py"""
class MAPPO_Policy()
    """MAPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.

:param args: (argparse.Namespace) arguments containing relevant model and policy information.
:param obs_space: (gym.Space) observation space.
:param cent_obs_space: (gym.Space) value function in"""
    def __init__(self, config, obs_space, cent_obs_space, act_space, device)
    def lr_decay(self, episode, episodes)
    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks, available_actions, deterministic)
    def get_values(self, cent_obs, rnn_states_critic, masks)
    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks, available_actions, active_masks)
    def act(self, obs, rnn_states_actor, masks, available_actions, deterministic)
```

### bidexhands/algorithms/marl/mappo_trainer.py

```
"""# @Time    : 2021/7/1 6:52 下午
# @Author  : hezhiqiang01
# @Email   : hezhiqiang01@baidu.com
# @File    : r_mappo.py"""
class MAPPO()
    """Trainer class for MAPPO to update policies.
:param args: (argparse.Namespace) arguments containing relevant model, policy, and env information.
:param policy: (R_MAPPO_Policy) policy to update.
:param device: (torch.device) specifies the device to run on (cpu/gpu)."""
    def __init__(self, config, policy, device)
    def cal_value_loss(self, values, value_preds_batch, return_batch, active_masks_batch)
    def ppo_update(self, sample, update_actor)
    def train(self, buffer, update_actor)
    def prep_training(self)
    def prep_rollout(self)
```

### bidexhands/algorithms/marl/runner.py

```
def _t2n(x)
class Runner()
    def __init__(self, vec_env, config, model_dir)
    def run(self)
    def warmup(self)
    def collect(self, step)
    def insert(self, data)
    def log_train(self, train_infos, total_num_steps)
    def train(self)
    def save(self)
    def restore(self)
    def log_train(self, train_infos, total_num_steps)
    def log_env(self, env_infos, total_num_steps)
    def eval(self, total_num_steps)
    def compute(self)
```

### bidexhands/algorithms/marl/utils/multi_discrete.py

```
class MultiDiscrete(Space)
    """- The multi-discrete action space consists of a series of discrete action spaces with different parameters
- It can be adapted to both a Discrete action space or a continuous (Box) action space
- It is useful to represent game controllers or keyboards where each key can be represented as a discrete """
    def __init__(self, array_of_param_array)
    def sample(self)
    def contains(self, x)
    def shape(self)
    def __repr__(self)
    def __eq__(self, other)
```

### bidexhands/algorithms/marl/utils/popart.py

```
class PopArt(Module)
    """Normalize a vector of observations - across the first norm_axes dimensions"""
    def __init__(self, input_shape, norm_axes, beta, per_element_update, epsilon, device)
    def reset_parameters(self)
    def running_mean_var(self)
    def forward(self, input_vector, train)
    def denormalize(self, input_vector)
```

### bidexhands/algorithms/marl/utils/separated_buffer.py

```
def _flatten(T, N, x)
def _cast(x)
class SeparatedReplayBuffer(object)
    def __init__(self, config, obs_space, share_obs_space, act_space, device)
    def update_factor(self, factor)
    def insert(self, share_obs, obs, rnn_states, rnn_states_critic, actions, action_log_probs, value_preds, rewards, masks, bad_masks, active_masks, available_actions)
    def chooseinsert(self, share_obs, obs, rnn_states, rnn_states_critic, actions, action_log_probs, value_preds, rewards, masks, bad_masks, active_masks, available_actions)
    def after_update(self)
    def chooseafter_update(self)
    def compute_returns(self, next_value, value_normalizer)
    def feed_forward_generator(self, advantages, num_mini_batch, mini_batch_size)
    def naive_recurrent_generator(self, advantages, num_mini_batch)
    def recurrent_generator(self, advantages, num_mini_batch, data_chunk_length)
```

### bidexhands/algorithms/marl/utils/util.py

```
def check(input)
def get_gard_norm(it)
def update_linear_schedule(optimizer, epoch, total_num_epochs, initial_lr)
def huber_loss(e, d)
def mse_loss(e)
def get_shape_from_obs_space(obs_space)
def get_shape_from_act_space(act_space)
def tile_images(img_nhwc)
```

### bidexhands/algorithms/marl/utils/valuenorm.py

```
class ValueNorm(Module)
    """Normalize a vector of observations - across the first norm_axes dimensions"""
    def __init__(self, input_shape, norm_axes, beta, per_element_update, epsilon, device)
    def reset_parameters(self)
    def running_mean_var(self)
    def update(self, input_vector)
    def normalize(self, input_vector)
    def denormalize(self, input_vector)
```

### bidexhands/algorithms/metarl/maml/maml.py

```
class Trainer()
    def __init__(self, inner_algo, meta_actor_critic, vec_env, learning_rate, sampler, asymmetric)
    def train(self, train_epoch)
    def sample_batch_task(self, task_size)
    def meta_update(self, support_storage_list, query_storage_list)
    def inner_update(self, support_storage, i)
```

### bidexhands/algorithms/metarl/maml/mamlppo.py

```
class MAMLPPO()
    def __init__(self, vec_env, pseudo_actor_critic, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def sample_support_trajectory(self, support_set_size, log_interval)
    def sample_query_trajectory(self, query_set_size, meta_storage)
    def log(self, locs, width, pad, query)
    def update(self)
```

### bidexhands/algorithms/metarl/maml/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/metarl/maml/storage.py

```
class RolloutStorage(object)
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mtppo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/mtrl/mtppo/mtppo.py

```
class PPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, random)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/mtrl/mtppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mtsac/module.py

```
def mlp(sizes, activation, output_activation)
class SquashedGaussianMLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs, deterministic, with_logprob, epsilon)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/mtrl/mtsac/mtsac.py

```
def count_vars(module)
class SAC()
    def __init__(self, vec_env, actor_critic, ac_kwargs, num_transitions_per_env, num_learning_epochs, num_mini_batches, replay_size, gamma, polyak, learning_rate, max_grad_norm, entropy_coef, use_clipped_value_loss, reward_scale, batch_size, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/mtrl/mtsac/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/mtrl/mttrpo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/mtrl/mttrpo/mttrpo.py

```
class TRPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, damping, cg_nsteps, max_kl, max_num_backtrack, accept_ratio, step_fraction, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def conjugate_gradient(self, Av, b, nsteps, residual_tol)
    def line_search(self, evaluate_policy, full_step, old_actions_log_prob_batch, grad, max_num_backtrack, accept_ratio, step_fraction)
    def kl_hessian_times_vector(self, v, kl)
    def set_pi_flat_params(self, flat_params)
    def get_pi_flat_params(self)
    def get_aloss_logp(self, obs_batch, states_batch, actions_batch, advantages_batch, old_actions_log_prob_batch)
```

### bidexhands/algorithms/mtrl/mttrpo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/offrl/bcq/bcq.py

```
class BCQ()
    def __init__(self, vec_env, device, discount, tau, lmbda, phi, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/offrl/bcq/module.py

```
class Actor(Module)
    def __init__(self, state_dim, action_dim, max_action, phi)
    def forward(self, state, action)
class Critic(Module)
    def __init__(self, state_dim, action_dim)
    def forward(self, state, action)
    def q1(self, state, action)
class VAE(Module)
    def __init__(self, state_dim, action_dim, latent_dim, max_action, device)
    def forward(self, state, action)
    def decode(self, state, z)
class BCQ_Model(object)
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, lmbda, phi)
    def select_action(self, state)
    def train(self, replay_buffer, iterations, batch_size)
```

### bidexhands/algorithms/offrl/bcq/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/iql/iql.py

```
class IQL()
    def __init__(self, vec_env, device, discount, tau, expectile, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/offrl/iql/module.py

```
class TDNetwork(Module)
    def __init__(self, state_dim, action_dim, net_type)
    def forward(self, x)
class Policy(Module)
    def __init__(self, state_dim, action_dim, max_action)
    def forward_dist(self, states)
class IQL_Model()
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, expectile, beta)
    def expectile_loss(self, value, expectile_prediction)
    def square_loss(self, value, mean_prediction)
    def L_V(self, states, actions)
    def L_Q(self, q_net, states, actions, rewards, next_states, terminals)
    def target_update(self)
    def TD_networks_update(self, states, actions, rewards, next_states, terminals)
    def L_pi(self, states, actions)
    def policy_update(self, states, actions)
    def select_action(self, state)
    def train(self, replay_buffer, interaction, batch_size)
```

### bidexhands/algorithms/offrl/iql/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/ppo_collect/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/offrl/ppo_collect/ppo_collect.py

```
class PPO()
    def __init__(self, vec_env, actor_critic_class, num_transitions_per_env, num_learning_epochs, num_mini_batches, clip_param, gamma, lam, init_noise_std, value_loss_coef, entropy_coef, learning_rate, max_grad_norm, use_clipped_value_loss, schedule, desired_kl, model_cfg, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, data_size)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/offrl/ppo_collect/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/offrl/td3_bc/module.py

```
class Actor(Module)
    def __init__(self, state_dim, action_dim, max_action)
    def forward(self, state)
class Critic(Module)
    def __init__(self, state_dim, action_dim)
    def forward(self, state, action)
    def Q1(self, state, action)
class TD3_BC_Model(object)
    def __init__(self, state_dim, action_dim, max_action, device, discount, tau, policy_noise, noise_clip, policy_freq, alpha)
    def select_action(self, state)
    def train(self, replay_buffer, interaction, batch_size)
```

### bidexhands/algorithms/offrl/td3_bc/storage.py

```
class ReplayBuffer(object)
    def __init__(self, state_dim, action_dim, device, max_size)
    def sample(self, batch_size)
    def convert(self, data_dir)
```

### bidexhands/algorithms/offrl/td3_bc/td3_bc.py

```
class TD3_BC()
    def __init__(self, vec_env, device, discount, tau, alpha, policy_freq, batch_size, max_timesteps, iterations, log_dir, datatype, algo)
    def run(self, num_learning_iterations, log_interval)
```

### bidexhands/algorithms/rl/ddpg/ddpg.py

```
def count_vars(module)
class DDPG()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/ddpg/module.py

```
def mlp(sizes, activation, output_activation)
class MLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, act_noise, device, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/ddpg/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/ppo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/rl/ppo/ppo.py

```
class PPO()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric, eval_bimanual, pre_grasp_policy)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
```

### bidexhands/algorithms/rl/ppo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/sac/module.py

```
def mlp(sizes, activation, output_activation)
class SquashedGaussianMLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs, deterministic, with_logprob, epsilon)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/sac/sac.py

```
def count_vars(module)
class SAC()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/sac/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/td3/module.py

```
def mlp(sizes, activation, output_activation)
class MLPActor(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation, act_limit)
    def forward(self, obs)
class MLPQFunction(Module)
    def __init__(self, obs_dim, act_dim, hidden_sizes, activation)
    def forward(self, obs, act)
class MLPActorCritic(Module)
    def __init__(self, observation_space, action_space, act_noise, device, hidden_sizes, activation)
    def act(self, obs, deterministic)
```

### bidexhands/algorithms/rl/td3/storage.py

```
class ReplayBuffer()
    def __init__(self, num_envs, replay_size, batch_size, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, next_obs, dones)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/td3/td3.py

```
def count_vars(module)
class TD3()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def compute_loss_q(self, data)
    def compute_loss_pi(self, data)
```

### bidexhands/algorithms/rl/trpo/module.py

```
class ActorCritic(Module)
    def __init__(self, obs_shape, states_shape, actions_shape, initial_std, model_cfg, asymmetric)
    def init_weights(sequential, scales)
    def forward(self)
    def act(self, observations, states)
    def act_inference(self, observations)
    def evaluate(self, observations, states, actions)
def get_activation(act_name)
```

### bidexhands/algorithms/rl/trpo/storage.py

```
class RolloutStorage()
    def __init__(self, num_envs, num_transitions_per_env, obs_shape, states_shape, actions_shape, device, sampler)
    def add_transitions(self, observations, states, actions, rewards, dones, values, actions_log_prob, mu, sigma)
    def clear(self)
    def compute_returns(self, last_values, gamma, lam)
    def get_statistics(self)
    def mini_batch_generator(self, num_mini_batches)
```

### bidexhands/algorithms/rl/trpo/trpo.py

```
class TRPO()
    def __init__(self, vec_env, cfg_train, device, sampler, log_dir, is_testing, print_log, apply_reset, asymmetric)
    def test(self, path)
    def load(self, path)
    def save(self, path)
    def run(self, num_learning_iterations, log_interval)
    def log(self, locs, width, pad)
    def update(self)
    def conjugate_gradient(self, Av, b, nsteps, residual_tol)
    def line_search(self, evaluate_policy, full_step, old_actions_log_prob_batch, grad, max_num_backtrack, accept_ratio, step_fraction)
    def kl_hessian_times_vector(self, v, kl)
    def set_pi_flat_params(self, flat_params)
    def get_pi_flat_params(self)
    def get_aloss_logp(self, obs_batch, states_batch, actions_batch, advantages_batch, old_actions_log_prob_batch)
```

### bidexhands/algorithms/utils/act.py

```
class ACTLayer(Module)
    """MLP Module to compute actions.
:param action_space: (gym.Space) action space.
:param inputs_dim: (int) dimension of network input.
:param use_orthogonal: (bool) whether to use orthogonal initialization.
:param gain: (float) gain of the output layer of the network."""
    def __init__(self, action_space, inputs_dim, use_orthogonal, gain, args)
    def forward(self, x, available_actions, deterministic)
    def get_probs(self, x, available_actions)
    def evaluate_actions(self, x, action, available_actions, active_masks)
    def evaluate_actions_trpo(self, x, action, available_actions, active_masks)
```

### bidexhands/algorithms/utils/cnn.py

```
class Flatten(Module)
    def forward(self, x)
class CNNLayer(Module)
    def __init__(self, obs_shape, hidden_size, use_orthogonal, use_ReLU, kernel_size, stride)
    def forward(self, x)
class CNNBase(Module)
    def __init__(self, args, obs_shape)
    def forward(self, x)
```

### bidexhands/algorithms/utils/distributions.py

```
class FixedCategorical(Categorical)
    def sample(self)
    def log_probs(self, actions)
    def mode(self)
class FixedNormal(Normal)
    def log_probs(self, actions)
    def entrop(self)
    def mode(self)
class FixedBernoulli(Bernoulli)
    def log_probs(self, actions)
    def entropy(self)
    def mode(self)
class Categorical(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x, available_actions)
class DiagGaussian(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain, config)
    def forward(self, x, available_actions)
class Bernoulli(Module)
    def __init__(self, num_inputs, num_outputs, use_orthogonal, gain)
    def forward(self, x)
class AddBias(Module)
    def __init__(self, bias)
    def forward(self, x)
```

### bidexhands/algorithms/utils/mlp.py

```
class MLPLayer(Module)
    def __init__(self, input_dim, hidden_size, layer_N, use_orthogonal, use_ReLU)
    def forward(self, x)
class MLPBase(Module)
    def __init__(self, config, obs_shape, cat_self, attn_internal)
    def forward(self, x)
```

### bidexhands/algorithms/utils/rnn.py

```
class RNNLayer(Module)
    def __init__(self, inputs_dim, outputs_dim, recurrent_N, use_orthogonal)
    def forward(self, x, hxs, masks)
```

### bidexhands/algorithms/utils/util.py

```
def init(module, weight_init, bias_init, gain)
def get_clones(module, N)
def check(input)
```

### bidexhands/plot.py

```
def plot_training_curve(task_name_list, seed_list)
def plot_grouped_comparison(task_name_list, seed_list)
def plot_all()
def plot_all_dual_arm()
```

### bidexhands/tasks/ability_hand_grasp_and_place_relative.py

```
class AbilityHandGraspAndPlaceRelative(BaseTask)
    """This class corresponds to the GraspAndPlace task. This environment consists of dual-hands, an
object and a bucket that requires us to pick up the object and put it into the bucket.

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dextero"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        block_right_handle_pos (tensor): The position of the right block handle

        block_left_handle_pos (tensor): The position of the left block handle

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    r
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, 11 * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 11 * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.1)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, 11 * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 11 * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.bl
```

### bidexhands/tasks/allegro_hand_catch_underarm.py

```
class AllegroHandCatchUnderarm(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, allegro_left_hand_pos, allegro_right_hand_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, allegro_left_hand_pos, allegro_right_hand_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.1, torch.ones_like(reset_buf), reset_buf)
    resets = torch.where(allegro_right_hand_pos[:, 1] <= -0.8, torch.ones_like(resets), resets)

    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, successes, cons_successes
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.allegro_left_hand_pos, self.allegro_right_hand_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.allegro_right_hand_pos = self.rigid_body_states[:, 6, 0:3]
        self.allegro_right_hand_rot = self.rigid_body_states[:, 6, 3:7]

        self.allegro_left_hand_pos = self.rigid_body_states[:, 6 + 23, 0:3]
        self.allegro_left_hand_rot = self.rigid_body_states[:, 6 + 23, 3:7]

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_grasp_and_place_asym_only.py

```
class AllegroHandDualArmGraspAndPlaceAsymOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 28)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2

    n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_grasp_and_place_asymdex.py

```
class AllegroHandDualArmGraspAndPlaceAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2

    net_force_mag
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_grasp_and_place_hardware_asymdex.py

```
class AllegroHandDualArmGraspAndPlaceHardwareAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_grasp_and_place_monolithic.py

```
class AllegroHandDualArmGraspAndPlaceMonolithic(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 44)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2

    n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_grasp_and_place_rel_only.py

```
class AllegroHandDualArmGraspAndPlaceRelOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 38)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2

    n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_asym_only.py

```
class AllegroHandDualArmPourAsymOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100 * (22 / 28)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
      
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_asymdex.py

```
class AllegroHandDualArmPourAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.norm(block_ri
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
      
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_ball_hardware_asymdex.py

```
class AllegroHandDualArmPourBallHardwareAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.norm(block_ri
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)

        self.ball_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 4, 0:3]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_hardware_asymdex.py

```
class AllegroHandDualArmPourHardwareAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, next_phase, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, next_phase,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:], self.next_phase[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis, self.next_phase,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes
        self.extras['entering_pouring_phase'] = self.next_phase

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.01)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
    
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_monolithic.py

```
class AllegroHandDualArmPourMonolithic(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100 * (22 / 44)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
      
```
```

### bidexhands/tasks/allegro_hand_dual_arm_pour_rel_only.py

```
class AllegroHandDualArmPourRelOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, cup_mouth_pos, kettle_spout_pose, net_force_tensor, kettle_up_axis, cup_up_axis,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    # left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(cup_mouth_pos - kettle_spout_pose, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    # left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    kettle_dist_penalty = torch.clamp(right_hand_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 100 * (22 / 38)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.exp(-10 * torch.n
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.kettle_spout_pose, self.net_force_tensor, 
            self.kettle_up_axis, self.cup_up_axis,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.kettle_spout_pose = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.05)
        self.kettle_spout_pose = self.kettle_spout_pose + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.1)

        self.kettle_up_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
      
```
```

### bidexhands/tasks/allegro_hand_dual_arm_stir_hardware_asymdex.py

```
class AllegroHandDualArmStirHardwareAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, stick_bottom_pos, cup_up_axis, right_hand_grasping_axis, stick_grasping_axis, stick_grasping_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, stick_bottom_pos, cup_up_axis, right_hand_grasping_axis,
    stick_grasping_axis, stick_grasping_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - stick_bottom_pos, p=2, dim=-1)
    right_hand_stick_dist = torch.norm(stick_grasping_pos - right_hand_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.wher
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor, self.stick_bottom_pos,
            self.cup_up_axis, self.right_hand_grasping_axis, self.stick_grasping_axis, self.stick_grasping_pos,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.3)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.cup_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.stick_bottom_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.stick_grasping_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -0.15)
        self.stick_grasping_axis = quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * -1.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]

        self.right_hand_grasping_axis = quat_apply(self.right_hand_rot, to_torch([0, -1, 0], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal
```
```

### bidexhands/tasks/allegro_hand_dual_arm_twist_lid_asym_only.py

```
class AllegroHandDualArmTwistLidAsymOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_finger_reward(index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis, wrapped_rotated_diff, finger_dist_rew, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_finger_reward(
    index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos
):
    # get the minimal distance between index finger tip and all markers
    index_tip_dist = torch.min(torch.norm(marker1to8_pos - index_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    middle_tip_dist = torch.min(torch.norm(marker1to8_pos - middle_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    ring_tip_dist = torch.min(torch.norm(marker1to8_pos - ring_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    thumb_tip_dist = torch.min(torch.norm(marker1to8_pos - thumb_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]

    coe = 50.0
    index_tip_dist_rew = 1 / (1 + coe * index_tip_dist)
    middle_tip_dist_rew = 1 / (1 + coe * middle_tip_dist)
    ring_tip_dist_rew = 1 / (1 + coe * ring_tip_dist)
    whumb_tip_dist_rew = 1 / (1 + coe * thumb_tip_dist)

    finger_tip_dist_rew = index_tip_dist_rew + middle_tip_dist_rew + ring_tip_dist_rew + whumb_tip_dist_rew

    return finger_tip_dist_rew
```

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis,
    wrapped_rotated_diff, finger_dist_rew,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 28)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew 
```

```python
def compute_reward(self, actions):

        self.finger_dist_rew = compute_finger_reward(self.right_index_tip_pos, self.right_middle_tip_pos, 
                              self.right_ring_tip_pos, self.right_thumb_tip_pos, self.bottle_lid_marker1to8_pos)
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.rotated_angle, self.bottle_up_axis, self.wrapped_rotated_diff, self.finger_dist_rew,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # bottle body
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        # bottle lid
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_rotate_joint_pos = self.bottle_joint_pos[:, 0]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = sel
```

### bidexhands/tasks/allegro_hand_dual_arm_twist_lid_asymdex.py

```
class AllegroHandDualArmTwistLidAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_finger_reward(index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis, wrapped_rotated_diff, finger_dist_rew, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_finger_reward(
    index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos
):
    # get the minimal distance between index finger tip and all markers
    index_tip_dist = torch.min(torch.norm(marker1to8_pos - index_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    middle_tip_dist = torch.min(torch.norm(marker1to8_pos - middle_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    ring_tip_dist = torch.min(torch.norm(marker1to8_pos - ring_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    thumb_tip_dist = torch.min(torch.norm(marker1to8_pos - thumb_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]

    coe = 50.0
    index_tip_dist_rew = 1 / (1 + coe * index_tip_dist)
    middle_tip_dist_rew = 1 / (1 + coe * middle_tip_dist)
    ring_tip_dist_rew = 1 / (1 + coe * ring_tip_dist)
    whumb_tip_dist_rew = 1 / (1 + coe * thumb_tip_dist)

    finger_tip_dist_rew = index_tip_dist_rew + middle_tip_dist_rew + ring_tip_dist_rew + whumb_tip_dist_rew

    return finger_tip_dist_rew
```

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis,
    wrapped_rotated_diff, finger_dist_rew,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(
```

```python
def compute_reward(self, actions):

        self.finger_dist_rew = compute_finger_reward(self.right_index_tip_pos, self.right_middle_tip_pos, 
                              self.right_ring_tip_pos, self.right_thumb_tip_pos, self.bottle_lid_marker1to8_pos)
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.rotated_angle, self.bottle_up_axis, self.wrapped_rotated_diff, self.finger_dist_rew,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # bottle body
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        # bottle lid
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_rotate_joint_pos = self.bottle_joint_pos[:, 0]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self
```

### bidexhands/tasks/allegro_hand_dual_arm_twist_lid_hardware_asymdex.py

```
class AllegroHandDualArmTwistLidHardwareAsymDex(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_finger_reward(index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis, wrapped_rotated_diff, finger_dist_rew, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_finger_reward(
    index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos
):
    # get the minimal distance between index finger tip and all markers
    index_tip_dist = torch.min(torch.norm(marker1to8_pos - index_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    middle_tip_dist = torch.min(torch.norm(marker1to8_pos - middle_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    ring_tip_dist = torch.min(torch.norm(marker1to8_pos - ring_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    thumb_tip_dist = torch.min(torch.norm(marker1to8_pos - thumb_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]

    coe = 50.0
    index_tip_dist_rew = 1 / (1 + coe * index_tip_dist)
    middle_tip_dist_rew = 1 / (1 + coe * middle_tip_dist)
    ring_tip_dist_rew = 1 / (1 + coe * ring_tip_dist)
    whumb_tip_dist_rew = 1 / (1 + coe * thumb_tip_dist)

    finger_tip_dist_rew = index_tip_dist_rew + middle_tip_dist_rew + ring_tip_dist_rew + whumb_tip_dist_rew

    return finger_tip_dist_rew
```

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis,
    wrapped_rotated_diff, finger_dist_rew,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(
```

```python
def compute_reward(self, actions):

        self.finger_dist_rew = compute_finger_reward(self.right_index_tip_pos, self.right_middle_tip_pos, 
                              self.right_ring_tip_pos, self.right_thumb_tip_pos, self.bottle_lid_marker1to8_pos)
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.rotated_angle, self.bottle_up_axis, self.wrapped_rotated_diff, self.finger_dist_rew,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # bottle body
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        # bottle lid
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_rotate_joint_pos = self.bottle_joint_pos[:, 0]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_ro
```

### bidexhands/tasks/allegro_hand_dual_arm_twist_lid_monolithic.py

```
class AllegroHandDualArmTwistLidMonolithic(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_finger_reward(index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis, wrapped_rotated_diff, finger_dist_rew, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_finger_reward(
    index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos
):
    # get the minimal distance between index finger tip and all markers
    index_tip_dist = torch.min(torch.norm(marker1to8_pos - index_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    middle_tip_dist = torch.min(torch.norm(marker1to8_pos - middle_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    ring_tip_dist = torch.min(torch.norm(marker1to8_pos - ring_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    thumb_tip_dist = torch.min(torch.norm(marker1to8_pos - thumb_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]

    coe = 50.0
    index_tip_dist_rew = 1 / (1 + coe * index_tip_dist)
    middle_tip_dist_rew = 1 / (1 + coe * middle_tip_dist)
    ring_tip_dist_rew = 1 / (1 + coe * ring_tip_dist)
    whumb_tip_dist_rew = 1 / (1 + coe * thumb_tip_dist)

    finger_tip_dist_rew = index_tip_dist_rew + middle_tip_dist_rew + ring_tip_dist_rew + whumb_tip_dist_rew

    return finger_tip_dist_rew
```

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis,
    wrapped_rotated_diff, finger_dist_rew,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 44)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew 
```

```python
def compute_reward(self, actions):

        self.finger_dist_rew = compute_finger_reward(self.right_index_tip_pos, self.right_middle_tip_pos, 
                              self.right_ring_tip_pos, self.right_thumb_tip_pos, self.bottle_lid_marker1to8_pos)
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.rotated_angle, self.bottle_up_axis, self.wrapped_rotated_diff, self.finger_dist_rew,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # bottle body
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        # bottle lid
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_rotate_joint_pos = self.bottle_joint_pos[:, 0]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = s
```

### bidexhands/tasks/allegro_hand_dual_arm_twist_lid_rel_only.py

```
class AllegroHandDualArmTwistLidRelOnly(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_finger_reward(index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis, wrapped_rotated_diff, finger_dist_rew, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_finger_reward(
    index_tip_pos, middle_tip_pos, ring_tip_pos, thumb_tip_pos, marker1to8_pos
):
    # get the minimal distance between index finger tip and all markers
    index_tip_dist = torch.min(torch.norm(marker1to8_pos - index_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    middle_tip_dist = torch.min(torch.norm(marker1to8_pos - middle_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    ring_tip_dist = torch.min(torch.norm(marker1to8_pos - ring_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]
    thumb_tip_dist = torch.min(torch.norm(marker1to8_pos - thumb_tip_pos.unsqueeze(1), p=2, dim=-1), dim=-1)[0]

    coe = 50.0
    index_tip_dist_rew = 1 / (1 + coe * index_tip_dist)
    middle_tip_dist_rew = 1 / (1 + coe * middle_tip_dist)
    ring_tip_dist_rew = 1 / (1 + coe * ring_tip_dist)
    whumb_tip_dist_rew = 1 / (1 + coe * thumb_tip_dist)

    finger_tip_dist_rew = index_tip_dist_rew + middle_tip_dist_rew + ring_tip_dist_rew + whumb_tip_dist_rew

    return finger_tip_dist_rew
```

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, bottle_rotated_angle, bottle_up_axis,
    wrapped_rotated_diff, finger_dist_rew,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50 * (22 / 38)
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew 
```

```python
def compute_reward(self, actions):

        self.finger_dist_rew = compute_finger_reward(self.right_index_tip_pos, self.right_middle_tip_pos, 
                              self.right_ring_tip_pos, self.right_thumb_tip_pos, self.bottle_lid_marker1to8_pos)
        
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.rotated_angle, self.bottle_up_axis, self.wrapped_rotated_diff, self.finger_dist_rew,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # bottle body
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_up_axis = quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 1.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        # bottle lid
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.bottle_rotate_joint_pos = self.bottle_joint_pos[:, 0]
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self
```

### bidexhands/tasks/allegro_hand_grasp_and_place_dual_arm_random.py

```
class AllegroHandGraspAndPlaceDualArmRandom(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos, net_force_tensor,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_rew = torch.exp(-block_dist)
    block_dist_penalty = torch.clamp(block_dist, max = 1.5)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, self.net_force_tensor,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_net_contact_force_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_grasp_and_place_relative.py

```
class AllegroHandGraspAndPlaceRelative(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2
    # up_rew =  torch.where(right_hand_finger_dist <= 0.3, torch.norm(bottle_cap_up - bottle_pos, p=2, dim=-1) * 30, up_rew)

    # reward = torch.exp(-0.1*(right_hand_dist_rew * dis
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, 17 * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 17 * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.1)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, 17 * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 17 * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 0 + 17, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 0 + 17, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 0, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 0, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_grasp_and_place_relative_dual_arm.py

```
class AllegroHandGraspAndPlaceRelativeDualArm(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def _dls_ik(self, dpose_right, dpose_left, Lambda)
    def substep(self)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)
def orientation_error(desired, current)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2
    # up_rew =  torch.where(right_ha
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_jacobian_tensors(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        # if self.obs_type == "full_state" or self.asymmetric_obs:
        #     self.gym.refresh_force_sensor_tensor(self.sim)
        #     self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.15)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, self.num_hand_arm_bodies * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 10 + self.num_hand_arm_bodies, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 10, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 10, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_grasp_and_place_relative_real_world.py

```
class AllegroHandGraspAndPlaceRelativeRealWorld(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, left_hand_goal_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, left_hand_goal_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    left_goal_dist = torch.norm(target_pos - block_left_handle_pos, p=2, dim=-1)
    right_goal_dist = torch.norm(target_pos - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_cup_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_block_dist = torch.norm(block_left_handle_pos - left_hand_pos, p = 2, dim=-1)
    left_hand_dist = torch.norm(left_hand_goal_pos - left_hand_pos, p=2, dim=-1)
    right_hand_dist = torch.norm(left_hand_goal_pos - right_hand_pos, p=2, dim=-1)
    # print("********************")
    # print(left_hand_goal_pos[0])
    # print(left_hand_pos[0])
    # print(block_right_handle_pos[0])
    block_dist = torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)

    # print(left_hand_goal_pos)

    # right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_right_handle_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_right_handle_pos - right_hand_th_pos, p=2, dim=-1))
    # left_hand_finger_dist = (torch.norm(block_left_handle_pos - left_hand_ff_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(block_left_handle_pos - left_hand_rf_pos, p=2, dim=-1) + torch.norm(block_left_handle_pos - left_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(block_left_handle_pos - left_hand_th_pos, p=2, dim=-1))
    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    right_hand_dist_rew = torch.exp(-10 * right_hand_cup_dist)
    left_hand_dist_rew = torch.exp(-10 * left_hand_block_dist)
    right_hand_goal_dist_rew = torch.exp(-1 * right_hand_dist)
    left_hand_goal_dist_rew = torch.exp(-1 * left_hand_dist)
    block_dist_penalty = block_dist
    block_dist_rew = torch.exp(-1 * block_dist)

    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1) / 50
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, :6] ** 2, dim=-1)) - 1 + torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # action_penalty = torch.exp(0.01 * torch.sum(actions[:, 26:32] ** 2, dim=-1)) - 1
    # print("action:")
    # print(action_penalty[0])

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    # reward = torch.exp(-0.05*(up_rew * dist_reward_scale)) + torch.exp(-0.05*(right_hand_dist_rew * dist_reward_scale)) + torch.exp(-0.05*(left_hand_dist_rew * dist_reward_scale))
    # up_rew = torch.zeros_like(right_hand_dist_rew)
    # up_rew = torch.where(right_hand_finger_dist < 0.6,
    #                 torch.where(left_hand_finger_dist < 0.4,
    up_rew = torch.zeros_like(right_hand_dist_rew)
    up_rew = torch.exp(-10 * torch.norm(block_right_handle_pos - block_left_handle_pos, p=2, dim=-1)) * 2
    # up_rew =  torch.where(right_ha
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.left_hand_goal_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        # cup?
        self.block_right_handle_pos = self.rigid_body_states[:, 17 * 2 + 1, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 17 * 2 + 1, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        #position left hand should reach to drop the block
        self.left_hand_goal_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.1)
        self.left_hand_goal_pos = self.left_hand_goal_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)

        # block?
        self.block_left_handle_pos = self.rigid_body_states[:, 17 * 2 + 2, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 17 * 2 + 2, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.left_hand_pos = self.rigid_body_states[:, 0 + 17, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 0 + 17, 3:7]

        self.right_hand_pos = self.rigid_body_states[:, 0, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 0, 3:7]
        
        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/allegro_hand_over.py

```
class AllegroHandOver(BaseTask)
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    # Distance from the hand to the object
    goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    if ignore_z_rot:
        success_tolerance = 2.0 * success_tolerance

    # Orientation alignment for the cube in hand and goal cube
    quat_diff = quat_mul(object_rot, quat_conjugate(target_rot))
    rot_dist = 2.0 * torch.asin(torch.clamp(torch.norm(quat_diff[:, 0:3], p=2, dim=-1), max=1.0))

    dist_rew = goal_dist
    # rot_rew = 1.0/(torch.abs(rot_dist) + rot_eps) * rot_reward_scale

    action_penalty = torch.sum(actions ** 2, dim=-1)

    # Total reward is: position distance + orientation alignment + action regularization + success bonus + fall penalty
    reward = torch.exp(-0.2*(dist_rew * dist_reward_scale + rot_dist))

    # Find out which envs hit the goal and update successes count
    goal_resets = torch.where(torch.abs(goal_dist) <= 0, torch.ones_like(reset_goal_buf), reset_goal_buf)
    successes = successes + goal_resets

    # Success bonus: orientation is within `success_tolerance` of goal orientation
    reward = torch.where(goal_resets == 1, reward + reach_goal_bonus, reward)

    # Fall penalty: distance to the goal is larger than a threashold
    reward = torch.where(object_pos[:, 2] <= 0.2, reward + fall_penalty, reward)

    # Check env termination conditions, including maximum success number
    resets = torch.where(object_pos[:, 2] <= 0.2, torch.ones_like(reset_buf), reset_buf)
    if max_consecutive_successes > 0:
        # Reset progress buffer on goal envs if max_consecutive_successes > 0
        progress_buf = torch.where(torch.abs(rot_dist) <= success_tolerance, torch.zeros_like(progress_buf), progress_buf)
        resets = torch.where(successes >= max_consecutive_successes, torch.ones_like(resets), resets)
    resets = torch.where(progress_buf >= max_episode_length, torch.ones_like(resets), resets)

    # Apply penalty for not reaching the goal
    if max_consecutive_successes > 0:
        reward = torch.where(progress_buf >= max_episode_length, reward + 0.5 * fall_penalty, reward)

    num_resets = torch.sum(resets)
    finished_cons_successes = torch.sum(successes * resets.float())

    cons_successes = torch.where(num_resets > 0, av_factor*finished_cons_successes/num_resets + (1.0 - av_factor)*consecutive_successes, consecutive_successes)

    return reward, resets, goal_resets, progress_buf, successes, cons_successes
```

```python
def compute_reward(self, actions):
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot,
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)

        if self.obs_type == "full_state" or self.asymmetric_obs:
            self.gym.refresh_force_sensor_tensor(self.sim)
            self.gym.refresh_dof_force_tensor(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.goal_pose = self.goal_states[:, 0:7]
        self.goal_pos = self.goal_states[:, 0:3]
        self.goal_rot = self.goal_states[:, 3:7]

        # self.fingertip_state = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:13]
        # self.fingertip_pos = self.rigid_body_states[:, self.fingertip_handles][:, :, 0:3]
        # self.fingertip_another_state = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:13]
        # self.fingertip_another_pos = self.rigid_body_states[:, self.fingertip_another_handles][:, :, 0:3]

        self.compute_full_state()

        if self.asymmetric_obs:
            self.compute_full_state(True)
```
```

### bidexhands/tasks/hand_base/base_task.py

```
class BaseTask()
    def __init__(self, cfg, enable_camera_sensors, is_meta, task_num)
    def set_sim_params_up_axis(self, sim_params, axis)
    def create_sim(self, compute_device, graphics_device, physics_engine, sim_params)
    def step(self, actions)
    def get_states(self)
    def render(self, sync_frame_time)
    def get_actor_params_info(self, dr_params, env)
    def apply_randomizations(self, dr_params)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
def get_attr_val_from_sample(sample, offset, prop, attr)
```

### bidexhands/tasks/hand_base/meta_vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def uniform_random_strategy(self, num_tasks, _)
    def round_robin_strategy(self, num_tasks, last_task)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MetaVecTaskPython(VecTask)
    def set_task(self, task)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _active_task_one_hot(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/multi_task_vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def uniform_random_strategy(self, num_tasks, _)
    def round_robin_strategy(self, num_tasks, last_task)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MultiTaskVecTaskPython(VecTask)
    def set_task(self, task)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _active_task_one_hot(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/multi_vec_task.py

```
class MultiVecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class MultiVecTaskPython(MultiVecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)
class SingleVecTaskPythonArm()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)

```python
def observation_space(self):
        return self.obs_space
```

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/vec_task.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)
class VecTaskPythonArm(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/hand_base/vec_task_rlgames.py

```
class VecTask()
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def has_action_masks(self)
    def get_number_of_agents(self)
    def get_env_info(self)
    def seed(self, seed)
    def set_train_info(self, env_frames)
    def get_env_state(self)
    def set_env_state(self, env_state)
    def step(self, actions)
    def reset(self)
    def get_number_of_agents(self)
    def observation_space(self)
    def action_space(self)
    def num_envs(self)
    def num_acts(self)
    def num_obs(self)
    def get_env_info(self)
class VecTaskCPU(VecTask)
    def __init__(self, task, rl_device, sync_frame_time, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class VecTaskGPU(VecTask)
    def __init__(self, task, rl_device, clip_observations, clip_actions)
    def step(self, actions)
    def reset(self)
class RLgamesVecTaskPython(VecTask)
    def get_state(self)
    def step(self, actions)
    def reset(self)
    def _to_device(self, inp)

```python
def observation_space(self):
        return self.obs_space
```
```

### bidexhands/tasks/shadow_hand_block_stack.py

```
class ShadowHandBlockStack(BaseTask)
    """This class corresponds to the Block Stack task. This environment involves dual hands and two blocks, and we need to stack the block
as a tower.

Args:
    cfg (dict): The configuration file of the environment, which is the parameter defined in the
        dexteroushandenvs/cfg folder

    sim_params"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, max_episode_length, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes,
    max_episode_length: float, object_pos, object_rot, target_pos, target_rot, block_right_handle_pos, block_left_handle_pos,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        block_right_handle_pos (tensor): The position of the right block

        block_left_handle_pos (tensor): The position of the left block

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    
    # Distance from the hand to the object
    stack_pos1 = target_pos.clone()
    stack_pos2 = target_pos.clone()

    stack_pos1[:, 1] -= 0.1
    stack_pos2[:, 1] -= 0.1
    # stack_pos1[:, 2] += 0.025
    stack_pos1[:, 2] += 0.05

    goal_dist1 = torch.norm(stack_pos1 - block_left_handle_pos, p=2, dim=-1)
    goal_dist2 = torch.norm(stack_pos2 - block_right_handle_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(block_right_handle_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(block_left_handle_pos - left_hand_pos, p=2, dim=-1)

    right_hand_finger_dist = (torch.norm(block_right_handle_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(block_right_handle_pos - r
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], self.consecutive_successes[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.block_right_handle_pos, self.block_left_handle_pos, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.left_hand_ff_pos, self.left_hand_mf_pos, self.left_hand_rf_pos, self.left_hand_lf_pos, self.left_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['successes'] = self.successes
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.block_pose = self.root_state_tensor[self.block_indices, 0:7]
        self.block_pos = self.root_state_tensor[self.block_indices, 0:3]
        self.block_rot = self.root_state_tensor[self.block_indices, 3:7]
        self.block_linvel = self.root_state_tensor[self.block_indices, 7:10]
        self.block_angvel = self.root_state_tensor[self.block_indices, 10:13]

        self.block_right_handle_pos = self.rigid_body_states[:, 26 * 2, 0:3]
        self.block_right_handle_rot = self.rigid_body_states[:, 26 * 2, 3:7]
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_right_handle_pos = self.block_right_handle_pos + quat_apply(self.block_right_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

        self.block_left_handle_pos = self.rigid_body_states[:, 26 * 2 + 1, 0:3]
        self.block_left_handle_rot = self.rigid_body_states[:, 26 * 2 + 1, 3:7]
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.block_left_handle_pos = self.block_left_handle_pos + quat_apply(self.block_left_handle_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)

   
```

### bidexhands/tasks/shadow_hand_bottle_cap.py

```
class ShadowHandBottleCap(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_hand_m
```

### bidexhands/tasks/shadow_hand_bottle_cap_interaction_naive.py

```
class ShadowHandBottleCapInteractionNaive(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_target_pos = self.root_state_tensor[self.another_hand_indices, 0:3] +\
              quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([0.0, -0.045, 0.365], device=self.device).repeat(self.num_envs, 1))
        
        self.bottle_up_vector = quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1))
        self.another_hand_thumb_vector = quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1))

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
     
```

### bidexhands/tasks/shadow_hand_bottle_cap_interaction_relative.py

```
class ShadowHandBottleCapInteractionRelative(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_target_pos = self.root_state_tensor[self.another_hand_indices, 0:3] +\
              quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([0.0, -0.045, 0.365], device=self.device).repeat(self.num_envs, 1))
        
        self.bottle_up_vector = quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1))
        self.another_hand_thumb_vector = quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1))

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
  
```

### bidexhands/tasks/shadow_hand_bottle_cap_naive.py

```
class ShadowHandBottleCapNaive(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right_h
```

### bidexhands/tasks/shadow_hand_bottle_cap_one_stage.py

```
class ShadowHandBottleCapOneStage(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_target_pos = self.root_state_tensor[self.another_hand_indices, 0:3] +\
              quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([0.0, -0.045, 0.365], device=self.device).repeat(self.num_envs, 1))
        
        self.bottle_up_vector = quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1))
        self.another_hand_thumb_vector = quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1))

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.
```

### bidexhands/tasks/shadow_hand_bottle_cap_pre_grasp.py

```
class ShadowHandBottleCapPreGrasp(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, bottle_target_pos, object_rot, bottle_up_vector, bottle_pos, another_hand_thumb_vector, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, bottle_target_pos, object_rot, bottle_up_vector, bottle_pos, another_hand_thumb_vector,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        bottle_target_pos (tensor): The target position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    # right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    # right_hand_finger_dist = (to
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.bottle_target_pos, self.object_rot, self.bottle_up_vector, self.bottle_pos, self.another_hand_thumb_vector, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_target_pos = self.root_state_tensor[self.another_hand_indices, 0:3] +\
              quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([0.0, -0.045, 0.365], device=self.device).repeat(self.num_envs, 1))
        
        self.bottle_up_vector = quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1))
        self.another_hand_thumb_vector = quat_apply(self.root_state_tensor[self.another_hand_indices, 3:7], to_torch([1, 0, 0], device=self.device).repeat(self.num_envs, 1))

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repe
```

### bidexhands/tasks/shadow_hand_bottle_cap_rel_only.py

```
class ShadowHandBottleCapRelOnly(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.right
```

### bidexhands/tasks/shadow_hand_bottle_cap_relative.py

```
class ShadowHandBottleCapRelative(BaseTask)
    """This class corresponds to the Bottle Cap task. This environment involves two hands and a bottle, we 
need to hold the bottle with one hand and open the bottle cap with the other hand. This skill requires 
the cooperation of two hands to ensure that the cap does not fall.

Args:
    cfg (dict): The c"""
    def __init__(self, cfg, sim_params, physics_engine, device_type, device_id, headless, agent_index, is_multi_agent)
    def create_sim(self)
    def _create_ground_plane(self)
    def _create_envs(self, num_envs, spacing, num_per_row)
    def compute_reward(self, actions)
    def compute_observations(self)
    def compute_full_state(self, asymm_obs)
    def compute_point_cloud_observation(self, collect_demonstration)
    def reset_target_pose(self, env_ids, apply_reset)
    def reset(self, env_ids, goal_env_ids)
    def pre_physics_step(self, actions)
    def post_physics_step(self)
    def add_debug_lines(self, env, pos, rot)
    def rand_row(self, tensor, dim_needed)
    def sample_points(self, points, sample_num, sample_mathed)
    def camera_visulization(self, is_depth_image)
def depth_image_to_point_cloud_GPU(camera_tensor, camera_view_matrix_inv, camera_proj_matrix, u, v, width, height, depth_bar, device)
def compute_hand_reward(rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate, max_episode_length, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up, left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos, dist_reward_scale, rot_reward_scale, rot_eps, actions, action_penalty_scale, success_tolerance, reach_goal_bonus, fall_dist, fall_penalty, max_consecutive_successes, av_factor, ignore_z_rot)
def randomize_rotation(rand0, rand1, x_unit_tensor, y_unit_tensor)
def randomize_rotation_pen(rand0, rand1, max_angle, x_unit_tensor, y_unit_tensor, z_unit_tensor)

```python
def compute_hand_reward(
    rew_buf, reset_buf, reset_goal_buf, progress_buf, successes, consecutive_successes, cons_successes_candidate,
    max_episode_length: float, object_pos, object_rot, bottle_cap_pos, bottle_pos, bottle_cap_up,
    left_hand_pos, right_hand_pos, right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos,
    dist_reward_scale: float, rot_reward_scale: float, rot_eps: float,
    actions, action_penalty_scale: float,
    success_tolerance: float, reach_goal_bonus: float, fall_dist: float,
    fall_penalty: float, max_consecutive_successes: int, av_factor: float, ignore_z_rot: bool
):
    """
    Compute the reward of all environment.

    Args:
        rew_buf (tensor): The reward buffer of all environments at this time

        reset_buf (tensor): The reset buffer of all environments at this time

        reset_goal_buf (tensor): The only-goal reset buffer of all environments at this time

        progress_buf (tensor): The porgress buffer of all environments at this time

        successes (tensor): The successes buffer of all environments at this time

        consecutive_successes (tensor): The consecutive successes buffer of all environments at this time

        max_episode_length (float): The max episode length in this environment

        object_pos (tensor): The position of the object

        object_rot (tensor): The rotation of the object

        target_pos (tensor): The position of the target

        target_rot (tensor): The rotate of the target

        bottle_cap_pos (tensor): The position of the bottle's cap

        bottle_pos (tensor): The position of the bottle's body

        bottle_cap_up (tensor): The height at which the bottle cap is raised

        left_hand_pos, right_hand_pos (tensor): The position of the bimanual hands
        
        right_hand_ff_pos, right_hand_mf_pos, right_hand_rf_pos, right_hand_lf_pos, right_hand_th_pos (tensor): The position of the five fingers 
            of the right hand

        left_hand_ff_pos, left_hand_mf_pos, left_hand_rf_pos, left_hand_lf_pos, left_hand_th_pos (tensor): The position of the five fingers 
            of the left hand

        dist_reward_scale (float): The scale of the distance reward

        rot_reward_scale (float): The scale of the rotation reward

        rot_eps (float): The epsilon of the rotation calculate

        actions (tensor): The action buffer of all environments at this time

        action_penalty_scale (float): The scale of the action penalty reward

        success_tolerance (float): The tolerance of the success determined

        reach_goal_bonus (float): The reward given when the object reaches the goal

        fall_dist (float): When the object is far from the Shadowhand, it is judged as falling

        fall_penalty (float): The reward given when the object is fell

        max_consecutive_successes (float): The maximum of the consecutive successes

        av_factor (float): The average factor for calculate the consecutive successes

        ignore_z_rot (bool): Is it necessary to ignore the rot of the z-axis, which is usually used 
            for some specific objects (e.g. pen)
    """
    # Distance from the hand to the object
    # goal_dist = torch.norm(target_pos - object_pos, p=2, dim=-1)
    # goal_dist = target_pos[:, 2] - object_pos[:, 2]

    right_hand_dist = torch.norm(bottle_cap_pos - right_hand_pos, p=2, dim=-1)
    left_hand_dist = torch.norm(bottle_pos - left_hand_pos, p=2, dim=-1)

    # right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_mf_pos, p=2, dim=-1)
    #                         + torch.norm(bottle_cap_pos - right_hand_rf_pos, p=2, dim=-1) + torch.norm(bottle_cap_pos - right_hand_lf_pos, p=2, dim=-1) 
    #                         + torch.norm(bottle_cap_pos - right_hand_th_pos, p=2, dim=-1))
    right_hand_finger_dist = (torch.norm(bottle_cap_pos - right_hand_ff
```

```python
def compute_reward(self, actions):
        """
        Compute the reward of all environment. The core function is compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes,
            self.max_episode_length, self.object_pos, self.object_rot, self.goal_pos, self.goal_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )
        , which we will introduce in detail there

        Args:
            actions (tensor): Actions of agents in the all environment 
        """
        self.rew_buf[:], self.reset_buf[:], self.reset_goal_buf[:], self.progress_buf[:], self.successes[:], \
            self.consecutive_successes[:], self.cons_successes_candidate[:] = compute_hand_reward(
            self.rew_buf, self.reset_buf, self.reset_goal_buf, self.progress_buf, self.successes, self.consecutive_successes, self.cons_successes_candidate,
            self.max_episode_length, self.object_pos, self.object_rot, self.bottle_cap_pos, self.bottle_pos, self.bottle_cap_up, 
            self.left_hand_pos, self.right_hand_pos, self.right_hand_ff_pos, self.right_hand_mf_pos, self.right_hand_rf_pos, self.right_hand_lf_pos, self.right_hand_th_pos, 
            self.dist_reward_scale, self.rot_reward_scale, self.rot_eps, self.actions, self.action_penalty_scale,
            self.success_tolerance, self.reach_goal_bonus, self.fall_dist, self.fall_penalty,
            self.max_consecutive_successes, self.av_factor, (self.object_type == "pen")
        )

        self.extras['realtime_success'] = self.successes
        self.extras['successes'] = self.cons_successes_candidate
        self.extras['consecutive_successes'] = self.consecutive_successes

        if self.print_success_stat:
            self.total_resets = self.total_resets + self.reset_buf.sum()
            direct_average_successes = self.total_successes + self.successes.sum()
            self.total_successes = self.total_successes + (self.successes * self.reset_buf).sum()

            # The direct average shows the overall result more quickly, but slightly undershoots long term
            # policy performance.
            print("Direct average consecutive successes = {:.1f}".format(direct_average_successes/(self.total_resets + self.num_envs)))
            if self.total_resets > 0:
                print("Post-Reset average consecutive successes = {:.1f}".format(self.total_successes/self.total_resets))
```

```python
def compute_observations(self):
        """
        Compute the observations of all environment. The core function is self.compute_full_state(True), 
        which we will introduce in detail there

        """
        self.gym.refresh_dof_state_tensor(self.sim)
        self.gym.refresh_actor_root_state_tensor(self.sim)
        self.gym.refresh_rigid_body_state_tensor(self.sim)
        self.gym.refresh_force_sensor_tensor(self.sim)
        self.gym.refresh_dof_force_tensor(self.sim)

        if self.obs_type in ["point_cloud"]:
            self.gym.render_all_camera_sensors(self.sim)
            self.gym.start_access_image_tensors(self.sim)

        self.object_pose = self.root_state_tensor[self.object_indices, 0:7]
        self.object_pos = self.root_state_tensor[self.object_indices, 0:3]
        self.object_rot = self.root_state_tensor[self.object_indices, 3:7]
        self.object_linvel = self.root_state_tensor[self.object_indices, 7:10]
        self.object_angvel = self.root_state_tensor[self.object_indices, 10:13]

        self.bottle_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * 0.0)
        self.bottle_pos = self.bottle_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.0)
        
        self.bottle_cap_up = self.rigid_body_states[:, 26 * 2 + 3, 0:3].clone()
        self.bottle_cap_pos = self.object_pos + quat_apply(self.object_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.0)
        self.bottle_cap_pos = self.bottle_cap_pos + quat_apply(self.object_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.15)

        self.left_hand_pos = self.rigid_body_states[:, 3 + 26, 0:3]
        self.left_hand_rot = self.rigid_body_states[:, 3 + 26, 3:7]
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.left_hand_pos = self.left_hand_pos + quat_apply(self.left_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        self.right_hand_pos = self.rigid_body_states[:, 3, 0:3]
        self.right_hand_rot = self.rigid_body_states[:, 3, 3:7]
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.08)
        self.right_hand_pos = self.right_hand_pos + quat_apply(self.right_hand_rot, to_torch([0, 1, 0], device=self.device).repeat(self.num_envs, 1) * -0.02)

        # right hand finger
        self.right_hand_ff_pos = self.rigid_body_states[:, 7, 0:3]
        self.right_hand_ff_rot = self.rigid_body_states[:, 7, 3:7]
        self.right_hand_ff_pos = self.right_hand_ff_pos + quat_apply(self.right_hand_ff_rot, to_torch([0, 0, 1], device=self.device).repeat(self.num_envs, 1) * 0.02)
        self.right_hand_mf_pos = self.rigid_body_states[:, 11, 0:3]
        self.righ
```