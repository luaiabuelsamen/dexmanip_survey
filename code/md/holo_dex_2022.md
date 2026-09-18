# holo_dex_2022

source: https://github.com/SridharPandian/Holo-Dex


commit: 3a5c201124cd6a26b13cbdac5982640fd0607646


## README

# Holo-Dex: Teaching Dexterity with Immersive Mixed Reality

**Authors**: [Sridhar Pandian Arunachalam](https://sridharpandian.github.io), [Irmak Guzey](https://irmakguzey.github.io/), [Soumith Chintala](https://soumith.ch/), [Lerrel Pinto](https://lerrelpinto.com)

This repository contains the official implementation of [Holo-Dex](https://arxiv.org/abs/2210.06463) including the unity scripts for the VR application, robot demonstration collection pipeline, training scripts and deployment modules. The VR application's APK can be found [here](https://github.com/SridharPandian/Holo-Dex/releases/tag/VR).

## Robot Runs
<p align="center">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/planar-rotation.gif">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/object-flipping.gif">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/can-spinning.gif">
 </p>

 <p align="center">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/bottle-opening.gif">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/card-sliding.gif">
  <img width="30%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/main_task/postit-note-sliding.gif">
 </p>

 ## Method
![Holo-Dex](https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/Intro.png)
Holo-Dex consists of two phases: demonstration colleciton, which is performed in real-time with visual feedback to VR Headset, and demonstration-based policy learning, which can learn to solve dexterous tasks from a limited number of demonstrations.

## Pipeline Installation and Setup
The pipeline requires [ROS](http://wiki.ros.org/noetic/Installation/Ubuntu) for Server-Robot communication. This Package uses the Allegro Hand and Kinova Arm controllers from [DIME-Controllers](https://github.com/NYU-robot-learning/DIME-Controllers). This implementation uses Realsense cameras and which require the [`librealsense`](https://github.com/IntelRealSense/librealsense#installation-guide) API. Also, [OpenCV](https://pypi.org/project/opencv-python/) is required for image compression and other purposes.

After installing all the prerequisites, you can install this pipeline as a package with pip:
```
pip install -e .
```

You can test if it has installed correctly by running `import holodex` from a python shell.

Install the VR Application in your Oculus Headset using the APK provided [here](https://github.com/SridharPandian/Holo-Dex/releases/tag/VR). To setup the VR Application in your Oculus Headset and enter the robot server's IP address (should be in the same network). The following stream border color codes indicate the following:
- Green - the right hand keypoints are being streamed
- Blue - the left hand keypoints are being stream. 
- Red - the stream is paused and gives access to the menu.

<p align="center">
  <img width="70%" src="https://github.com/holo-dex/holo-dex.github.io/blob/website/mfiles/color-code-indicator.gif">
</p>

## Running the teleop
To use the Holo-Dex teleop module, open the VR Application in your Oculus Headset. On the robot server side, start the [controllers](https://github.com/NYU-robot-learning/DIME-Controllers) first followed by the following command to start the teleop:
```
python teleop.py
```
The Holo-Dex teleop configurations can be adjusted in `configs/tracker/oculus.yaml`. The robot camera configurations can be adjusted in `configs/robot_camera.yaml`.

The package also contains an 30 Hz teleop implementation of [DIME](https://arxiv.org/abs/2203.13251) and you can run it using the following command:
```
python teleop.py tracker=mediapipe tracker/cam_serial_num=<realsense_camera_serial_number>
``` 

## Data
All our data can be found in this URL: [https://drive.google.com/drive/folders/1PiuqYkG7O1sIxE7YewVkni6ohLuNY7vF?usp=sharing](https://drive.google.com/drive/folders/1PiuqYkG7O1sIxE7YewVkni6ohLuNY7vF?usp=sharing)

To collect demonstrations using this framework, run the following command:
```
python record_data.py -n <demonstration_number>
```

To filter and process data from the raw demonstrations run the following command:
```
python extract_data.py
```
You can change the data extraction configurations in `configs/demo_extract.yaml`.

## Training Neural Networks
You can train encoders using Self-Supervised methods such as [BYOL](https://arxiv.org/abs/2006.07733), [VICReg](https://arxiv.org/abs/2105.04906), [SimCLR](https://arxiv.org/abs/2002.05709) and [MoCo](https://arxiv.org/abs/2104.02057). Use the following command to train a resnet encoder using the above mentioned SSL methods:
```
python train_ssl.py ssl_method=<byol|vicreg|simclr|mocov3>
```
The training configurations can be changed in `configs/train_ssl.yaml`. 

You can also train:
- Behavior Cloning:
```
python train_bc.py encoder_gradient=true
```
- [Behavior Cloning-Rep](https://arxiv.org/abs/2008.04899):
```
python train_bc.py encoder_gradient=false
```
The training configurations can be changed in `configs/train_bc.yaml`.

## Deploying Models
This implementation can deploy BC, BC-Rep and INN (all visual) on the robot. To deploy BC or BC-Rep, use the following command:
```
python deploy.py model=BC task/bc.model_weights=<bc_model-weights>
```

To deploy INN use the following command:
```
python deploy.py model=VINN task/vinn.encoder_weights_path=<ssl_encoder_weights_path>
```

You can set a control loop instead of pressing the `Enter` key to get actions using the following command:
```
python deploy.py model=<BC|VINN> run_loop=true loop_frequency=<action_loop_frequency>
```

## Customizing the VR Application
To use Holo-Dex's VR side source code `vr/Holo-Dex`, you need to install Unity along with other dependencies which can be downloaded through Nuget:
- Oculus SDK
- NetMQ
- TextMeshPro

## Citation

If you use this repo in your research, please consider citing the paper as follows:
```
@article{arunachalam2022holodex,
  title={Holo-Dex: Teaching Dexterity with Immersive Mixed Reality},
  author={Sridhar Pandian Arunachalam and Irmak Guzey and Soumith Chintala and Lerrel Pinto},
  journal={arXiv preprint arXiv:2210.06463},
  year={2022}
}


## File tree (depth 3, assets pruned)

```
.gitignore
README.md
configs/
  dataset/
    bottle_opening/
    can_spinning/
    card_sliding/
    object_flipping/
    planar_rotation/
    postit_note_sliding/
  demo_extract.yaml
  demo_record.yaml
  deploy.yaml
  encoder/
    resnet18.yaml
    resnet34.yaml
    resnet50.yaml
  image_parameters/
    bottle_opening.yaml
    can_spinning.yaml
    card_sliding.yaml
    object_flipping.yaml
    planar_rotation.yaml
    postit_note_sliding.yaml
  robot_camera.yaml
  ssl_method/
    byol.yaml
    mocov3.yaml
    simclr.yaml
    vicreg.yaml
  task/
    bottle_opening.yaml
    can_spinning.yaml
    card_sliding.yaml
    object_flipping.yaml
    planar_rotation.yaml
    postit_note_sliding.yaml
  teleop.yaml
  tracker/
    mediapipe.yaml
    oculus.yaml
  train_bc.yaml
  train_ssl.yaml
deploy.py
detect.py
extract_data.py
holodex/
  camera/
    camera_streamer.py
    realsense_camera.py
    video.py
  components/
    __init__.py
    deployer/
    detectors/
    keypoint_transforms.py
    robot_operators/
  constants.py
  models/
    __init__.py
    bc.py
    knn.py
    self_supervised_pretraining/
  robot/
    __init__.py
    allegro.py
    allegro_joint_controller.py
    allegro_kdl.py
    allegro_kdl_controller.py
    configs/
    kinova.py
  utils/
    augmentations.py
    files.py
    images.py
    logger.py
    losses.py
    models.py
    network.py
    optimizers.py
    vec_ops.py
  viz/
    __init__.py
    image.py
    plotters/
    visualizer_2d.py
    visualizer_3d.py
processes.py
record_data.py
robot_cam.py
setup.py
teleop.py
train_bc.py
train_ssl.py
vr/
  HoloDex/
    .gitignore
    .vsconfig
    Assets/
    Packages/
    ProjectSettings/
```

## Config files (46)


### configs/dataset/bottle_opening/filtered.yaml

```yaml
name: Bottle Opening Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_274
  - demonstration_275
  - demonstration_276
  - demonstration_277
  - demonstration_278

train_demos:
  - demonstration_274
  - demonstration_275
  - demonstration_276
  - demonstration_277

test_demos:
  - demonstration_278
```

### configs/dataset/bottle_opening/ssl.yaml

```yaml
name: Bottle Opening SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_274
  - demonstration_275
  - demonstration_276
  - demonstration_277
  - demonstration_278

train_demos:
  - demonstration_274
  - demonstration_275
  - demonstration_276
  - demonstration_277

test_demos:
  - demonstration_278
```

### configs/dataset/can_spinning/filtered.yaml

```yaml
name: Can Spinning Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_87
  - demonstration_88
  - demonstration_89
  - demonstration_90
  - demonstration_92
  - demonstration_93
  - demonstration_94
  - demonstration_95
  - demonstration_96
  - demonstration_98
  - demonstration_99
  - demonstration_100
  - demonstration_101
  - demonstration_103
  - demonstration_107
  - demonstration_109
  - demonstration_110
  - demonstration_111
  - demonstration_112
  - demonstration_113
  - demonstration_114
  - demonstration_115
  - demonstration_116
  - demonstration_117
  - demonstration_119
  - demonstration_121
  - demonstration_122
  - demonstration_123
  - demonstration_124
  - demonstration_125
  - demonstration_126
  - demonstration_128
  - demonstration_129
  - demonstration_130
  - demonstration_131
  - demonstration_132
  - demonstration_133
  - demonstration_134
  - demonstration_135
  - demonstration_137
  - demonstration_138
  - demonstration_139
  - demonstration_140
  - demonstration_141
  - demonstration_143
  - demonstration_146
  - demonstration_147
  - demonstration_148
  - demonstration_150
  - demonstration_151

train_demos:
  - demonstration_87
  - demonstration_88
  - demonstration_89
  - demonstration_92
  - demonstration_93
  - demonstration_94
  - demonstration_95
  - demonstration_98
  - demonstration_99
  - demonstration_100
  - demonstration_101
  - demonstration_103
  - demonstration_107
  - demonstration_109
  - demonstration_110
  - demonstration_111
  - demonstration_112
  - demonstration_113
  - demonstration_114
  - demonstration_115
  - demonstration_116
  - demonstration_117
  - demonstration_119
  - demonstration_121
  - demonstration_122
  - demonstration_123
  - demonstration_129
  - demonstration_130
  - demonstration_131
  - demonstration_132
  - demonstration_133
  - demonstration_134
  - demonstration_135
  - demonstration_137
  - demonstration_138
  - demonstration_139
  - demonstration_140
  - demonstration_141
  - demonstration_143
  - demonstration_146
  - demonstration_147
  - demonstration_148
  - demonstration_150
  - demonstration_151

test_demos:
  - demonstration_90
  - demonstration_96
  - demonstration_124
  - demonstration_125
  - demonstration_126
  - demonstration_128
```

### configs/dataset/can_spinning/ssl.yaml

```yaml
name: Can Spinning SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_87
  - demonstration_88
  - demonstration_89
  - demonstration_90
  - demonstration_91 
  - demonstration_92
  - demonstration_93
  - demonstration_94
  - demonstration_95
  - demonstration_96
  - demonstration_97 
  - demonstration_98
  - demonstration_99
  - demonstration_100
  - demonstration_101
  - demonstration_102 
  - demonstration_103
  - demonstration_104 
  - demonstration_105 
  - demonstration_106 
  - demonstration_107
  - demonstration_108 
  - demonstration_109
  - demonstration_110
  - demonstration_111
  - demonstration_112
  - demonstration_113
  - demonstration_114
  - demonstration_115
  - demonstration_116
  - demonstration_117
  - demonstration_118 
  - demonstration_119
  - demonstration_120 
  - demonstration_121
  - demonstration_122
  - demonstration_123
  - demonstration_124
  - demonstration_125
  - demonstration_126
  - demonstration_127 
  - demonstration_128
  - demonstration_129
  - demonstration_130
  - demonstration_131
  - demonstration_132
  - demonstration_133
  - demonstration_134
  - demonstration_135
  - demonstration_136 
  - demonstration_137
  - demonstration_138
  - demonstration_139
  - demonstration_140
  - demonstration_141
  - demonstration_142 
  - demonstration_143
  - demonstration_144 
  - demonstration_145 
  - demonstration_146
  - demonstration_147
  - demonstration_148
  - demonstration_149 
  - demonstration_150
  - demonstration_151

train_demos:
  - demonstration_87
  - demonstration_88
  - demonstration_89
  - demonstration_91
  - demonstration_92
  - demonstration_93
  - demonstration_94
  - demonstration_95
  - demonstration_98
  - demonstration_99
  - demonstration_100
  - demonstration_101
  - demonstration_103
  - demonstration_107
  - demonstration_108 
  - demonstration_109
  - demonstration_110
  - demonstration_111
  - demonstration_112
  - demonstration_113
  - demonstration_114
  - demonstration_115
  - demonstration_116
  - demonstration_117
  - demonstration_118 
  - demonstration_119
  - demonstration_120 
  - demonstration_121
  - demonstration_122
  - demonstration_123
  - demonstration_129
  - demonstration_130
  - demonstration_131
  - demonstration_132
  - demonstration_133
  - demonstration_134
  - demonstration_135
  - demonstration_136 
  - demonstration_137
  - demonstration_138
  - demonstration_139
  - demonstration_140
  - demonstration_141
  - demonstration_142 
  - demonstration_143
  - demonstration_144 
  - demonstration_145 
  - demonstration_146
  - demonstration_147
  - demonstration_148
  - demonstration_149 
  - demonstration_150
  - demonstration_151

test_demos:
  - demonstration_90
  - demonstration_96
  - demonstration_124
  - demonstration_125
  - demonstration_126
  - demonstration_127 
  - demonstration_128
```

### configs/dataset/card_sliding/filtered.yaml

```yaml
name: Card Sliding Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_152 
  - demonstration_154
  - demonstration_155
  - demonstration_156
  - demonstration_159
  - demonstration_160
  - demonstration_163
  - demonstration_164
  - demonstration_167
  - demonstration_168
  - demonstration_170
  - demonstration_172
  - demonstration_173
  - demonstration_174
  - demonstration_176
  - demonstration_177
  - demonstration_179 
  - demonstration_182
  - demonstration_183
  - demonstration_184
  - demonstration_185
  - demonstration_189
  - demonstration_190
  - demonstration_193 
  - demonstration_198
  - demonstration_202
  - demonstration_204
  - demonstration_205
  - demonstration_208
  - demonstration_209

train_demos:
  - demonstration_152 
  - demonstration_154
  - demonstration_155
  - demonstration_156
  - demonstration_159
  - demonstration_160
  - demonstration_163
  - demonstration_164
  - demonstration_167
  - demonstration_168
  - demonstration_170
  - demonstration_172
  - demonstration_176
  - demonstration_177
  - demonstration_179 
  - demonstration_182
  - demonstration_183
  - demonstration_184
  - demonstration_185
  - demonstration_189
  - demonstration_193 
  - demonstration_198
  - demonstration_202
  - demonstration_204
  - demonstration_205
  - demonstration_208
  - demonstration_209

test_demos:
  - demonstration_173
  - demonstration_174
  - demonstration_190
```

### configs/dataset/card_sliding/ssl.yaml

```yaml
name: Card Sliding SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_152 
  - demonstration_153
  - demonstration_154
  - demonstration_155
  - demonstration_156
  - demonstration_157
  - demonstration_158
  - demonstration_159
  - demonstration_160
  - demonstration_161
  - demonstration_162
  - demonstration_163
  - demonstration_164
  - demonstration_165
  - demonstration_166
  - demonstration_167
  - demonstration_168
  - demonstration_169
  - demonstration_170
  - demonstration_171
  - demonstration_172
  - demonstration_173
  - demonstration_174
  - demonstration_175
  - demonstration_176
  - demonstration_177
  - demonstration_178
  - demonstration_179 
  - demonstration_180
  - demonstration_181
  - demonstration_182
  - demonstration_183
  - demonstration_184
  - demonstration_185
  - demonstration_186
  - demonstration_187
  - demonstration_188
  - demonstration_189
  - demonstration_190
  - demonstration_191
  - demonstration_192
  - demonstration_193 
  - demonstration_194
  - demonstration_195
  - demonstration_196
  - demonstration_197
  - demonstration_198
  - demonstration_199
  - demonstration_200
  - demonstration_201
  - demonstration_202
  - demonstration_203
  - demonstration_204
  - demonstration_205
  - demonstration_206
  - demonstration_207
  - demonstration_208
  - demonstration_209

train_demos:
  - demonstration_152 
  - demonstration_153
  - demonstration_154
  - demonstration_155
  - demonstration_156
  - demonstration_157
  - demonstration_158
  - demonstration_159
  - demonstration_160
  - demonstration_161
  - demonstration_162
  - demonstration_165
  - demonstration_166
  - demonstration_167
  - demonstration_168
  - demonstration_169
  - demonstration_170
  - demonstration_171
  - demonstration_172
  - demonstration_173
  - demonstration_174
  - demonstration_175
  - demonstration_176
  - demonstration_177
  - demonstration_178
  - demonstration_179 
  - demonstration_180
  - demonstration_181
  - demonstration_182
  - demonstration_183
  - demonstration_184
  - demonstration_185
  - demonstration_186
  - demonstration_187
  - demonstration_190
  - demonstration_191
  - demonstration_192
  - demonstration_193 
  - demonstration_194
  - demonstration_195
  - demonstration_196
  - demonstration_197
  - demonstration_198
  - demonstration_199
  - demonstration_200
  - demonstration_201
  - demonstration_202
  - demonstration_204
  - demonstration_205
  - demonstration_206
  - demonstration_207
  - demonstration_208
  - demonstration_209

test_demos:
  - demonstration_163
  - demonstration_164
  - demonstration_188
  - demonstration_189
  - demonstration_203
```

### configs/dataset/object_flipping/filtered.yaml

```yaml
name: Object Flipping Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_77
  - demonstration_78
  - demonstration_79
  - demonstration_80
  - demonstration_81
  - demonstration_82
  - demonstration_83
  - demonstration_84
  - demonstration_85
  - demonstration_86

train_demos:
  - demonstration_77
  - demonstration_78
  - demonstration_79
  - demonstration_81
  - demonstration_82
  - demonstration_83
  - demonstration_84
  - demonstration_85
  - demonstration_86

test_demos:
  - demonstration_80
  - demonstration_83
```

### configs/dataset/object_flipping/ssl.yaml

```yaml
name: Object Flipping SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_77
  - demonstration_78
  - demonstration_79
  - demonstration_80
  - demonstration_81
  - demonstration_82
  - demonstration_83
  - demonstration_84
  - demonstration_85
  - demonstration_86

train_demos:
  - demonstration_77
  - demonstration_78
  - demonstration_79
  - demonstration_81
  - demonstration_82
  - demonstration_83
  - demonstration_84
  - demonstration_85
  - demonstration_86

test_demos:
  - demonstration_80
  - demonstration_83
```

### configs/dataset/planar_rotation/clipped_trajectory.yaml

```yaml
name: Planar Rotation Filtered

dataset_path: ${data_path}/rotation/clipped_trajectory

complete_demos:
  - rotation_1
  - rotation_2
  - rotation_3
  - rotation_4
  - rotation_5
  - rotation_6
  - rotation_7
  - rotation_8
  - rotation_9
  - rotation_10
  - rotation_11
  - rotation_12
  - rotation_13
  - rotation_14
  - rotation_15
  - rotation_16
  - rotation_17
  - rotation_18
  - rotation_19
  - rotation_20
  - rotation_21
  - rotation_22
  - rotation_23
  - rotation_24
  - rotation_25
  - rotation_26
  - rotation_27
  - rotation_28
  - rotation_29
  - rotation_30
  - rotation_31
  - rotation_32
  - rotation_33
  - rotation_34
  - rotation_35
  - rotation_36
  - rotation_37
  - rotation_38
  - rotation_39
  - rotation_40
  - rotation_41
  - rotation_42
  - rotation_43
  - rotation_44
  - rotation_45
  - rotation_46
  - rotation_47
  - rotation_48
  - rotation_49
  - rotation_50
  - rotation_51
  - rotation_52
  - rotation_53
  - rotation_54
  - rotation_55
  - rotation_56
  - rotation_57
  - rotation_58
  - rotation_59
  - rotation_60
  - rotation_61
  - rotation_62
  - rotation_63
  - rotation_64
  - rotation_65
  - rotation_66
  - rotation_67
  - rotation_68
  - rotation_69
  - rotation_70
  - rotation_71
  - rotation_72
  - rotation_73
  - rotation_74
  - rotation_75
  - rotation_76
  - rotation_77
  - rotation_78
  - rotation_79
  - rotation_80
  - rotation_81
  - rotation_82
  - rotation_83
  - rotation_84
  - rotation_85
  - rotation_86
  - rotation_87
  - rotation_88
  - rotation_89
  - rotation_90
  - rotation_91
  - rotation_92
  - rotation_93
  - rotation_94
  - rotation_95
  - rotation_96
  - rotation_97
  - rotation_98
  - rotation_99
  - rotation_100
  - rotation_101
  - rotation_102
  - rotation_103
  - rotation_104
  - rotation_105
  - rotation_106
  - rotation_107
  - rotation_108
  - rotation_109
  - rotation_110
  - rotation_111
  - rotation_112
  - rotation_113
  - rotation_114
  - rotation_115
  - rotation_116
  - rotation_117
  - rotation_118
  - rotation_119
  - rotation_120
  - rotation_121
  - rotation_122
  - rotation_123
  - rotation_124
  - rotation_125
  - rotation_126
  - rotation_127
  - rotation_128
  - rotation_129
  - rotation_130
  - rotation_131
  - rotation_132

train_demos:
  - rotation_1
  - rotation_2
  - rotation_3
  - rotation_4
  - rotation_5
  - rotation_6
  - rotation_7
  - rotation_8
  - rotation_9
  - rotation_10
  - rotation_11
  - rotation_12
  - rotation_17
  - rotation_18
  - rotation_19
  - rotation_20
  - rotation_21
  - rotation_22
  - rotation_23
  - rotation_24
  - rotation_25
  - rotation_26
  - rotation_27
  - rotation_28
  - rotation_29
  - rotation_30
  - rotation_31
  - rotation_32
  - rotation_33
  - rotation_34
  - rotation_35
  - rotation_36
  - rotation_37
  - rotation_38
  - rotation_39
  - rotation_40
  - rotation_41
  - rotation_42
  - rotation_43
  - rotation_44
  - rotation_45
  - rotation_46
  - rotation_47
  - rotation_48
  - rotation_49
  - rotation_50
  - rotation_51
  - rotation_52
  - rotation_53
  - rotation_54
  - rotation_55
  - rotation_56
  - rotation_57
  - rotation_58
  - rotation_59
  - rotation_60
  - rotation_61
  - rotation_62
  - rotation_63
  - rotation_64
  - rotation_65
  - rotation_66
  - rotation_67
  - rotation_68
  - rotation_69
  - rotation_70
  - rotation_71
  - rotation_72
  - rotation_73
  - rotation_77
  - rotation_78
  - rotation_79
  - rotation_80
  - rotation_81
  - rotation_82
  - rotation_83
  - rotation_84
  - rotation_85
  - rotation_86
  - rotation_87
  - rotation_88
  - rotation_89
  - rotation_90
  - rotation_95
  - rotation_96
  - rotation_97
  - rotation_98
  - rotation_99
  - rotation_104
  - rotation_105
  - rotation_106
  - rotation_107
  - rotation_108
  - rotation_109
  - rotation_110
  - rotation_111
  - rotation_112
  - rotation_113
  - rotation_114
  - rotation_120
  - rotation_121
  - rotation_122
  - rotation_123
  - rotation_124
  - rotation_125
  - rotation_126
  - rotation_127
  - rotation_128
  - rotation_129
  - rotation_130
  - rotation_131
  - rotation_132

test_demos:
  - rotation_13
  - rotation_14
  - rotation_15
  - rotation_16
  - rotation_74
  - rotation_75
  - rotation_76
  - rotation_91
  - rotation_92
  - rotation_93
  - rotation_94
  - rotation_100
  - rotation_101
  - rotation_102
  - rotation_103
  - rotation_115
  - rotation_116
  - rotation_117
  - rotation_118
  - rotation_119
```

### configs/dataset/planar_rotation/filtered.yaml

```yaml
name: Planar Rotation Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_56
  - demonstration_57
  - demonstration_58
  - demonstration_59
  - demonstration_60
  - demonstration_61
  - demonstration_62
  - demonstration_63
  - demonstration_64
  - demonstration_65
  - demonstration_66
  - demonstration_67
  - demonstration_68
  - demonstration_69
  - demonstration_70
  - demonstration_71
  - demonstration_72
  - demonstration_73
  - demonstration_74
  - demonstration_75
  - demonstration_76

train_demos:
  - demonstration_56
  - demonstration_57
  - demonstration_58
  - demonstration_59
  - demonstration_60
  - demonstration_61
  - demonstration_62
  - demonstration_63
  - demonstration_64
  - demonstration_65
  - demonstration_66
  - demonstration_69
  - demonstration_70
  - demonstration_71
  - demonstration_72
  - demonstration_73
  - demonstration_74
  - demonstration_75
  - demonstration_76

test_demos:
  - demonstration_67
  - demonstration_68
```

### configs/dataset/planar_rotation/ssl.yaml

```yaml
name: Planar Rotation SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_5
  - demonstration_6
  - demonstration_7
  - demonstration_8
  - demonstration_9
  - demonstration_10
  - demonstration_11
  - demonstration_12
  - demonstration_15
  - demonstration_16
  - demonstration_17
  - demonstration_20
  - demonstration_21
  - demonstration_22
  - demonstration_56
  - demonstration_57
  - demonstration_58
  - demonstration_59
  - demonstration_60
  - demonstration_61
  - demonstration_62
  - demonstration_63
  - demonstration_64
  - demonstration_65
  - demonstration_66
  - demonstration_67
  - demonstration_68
  - demonstration_69
  - demonstration_70
  - demonstration_71
  - demonstration_72
  - demonstration_73
  - demonstration_74
  - demonstration_75
  - demonstration_76

train_demos:
  - demonstration_5
  - demonstration_6
  - demonstration_7
  - demonstration_8
  - demonstration_9
  - demonstration_10
  - demonstration_11
  - demonstration_12
  - demonstration_15
  - demonstration_16
  - demonstration_17
  - demonstration_56
  - demonstration_57
  - demonstration_58
  - demonstration_59
  - demonstration_60
  - demonstration_61
  - demonstration_62
  - demonstration_63
  - demonstration_64
  - demonstration_65
  - demonstration_66
  - demonstration_69
  - demonstration_70
  - demonstration_71
  - demonstration_72
  - demonstration_73
  - demonstration_74
  - demonstration_75
  - demonstration_76

test_demos:
  - demonstration_20
  - demonstration_21
  - demonstration_22
  - demonstration_67
  - demonstration_68
```

### configs/dataset/postit_note_sliding/filtered.yaml

```yaml
name: Postit Note Sliding Filtered

dataset_path: ${data_path}/demonstrations/filtered

complete_demos:
  - demonstration_211
  - demonstration_212
  - demonstration_215
  - demonstration_216
  - demonstration_217
  - demonstration_220
  - demonstration_221
  - demonstration_222
  - demonstration_223
  - demonstration_225
  - demonstration_226
  - demonstration_227
  - demonstration_228
  - demonstration_229
  - demonstration_230
  - demonstration_231
  - demonstration_232
  - demonstration_233
  - demonstration_234
  - demonstration_235
  - demonstration_236
  - demonstration_237
  - demonstration_238
  - demonstration_239
  - demonstration_240
  - demonstration_241
  - demonstration_242
  - demonstration_243
  - demonstration_244
  - demonstration_245
  - demonstration_246
  - demonstration_248
  - demonstration_249
  - demonstration_250
  - demonstration_251
  - demonstration_252
  - demonstration_253
  - demonstration_255
  - demonstration_256
  - demonstration_260
  - demonstration_262
  - demonstration_263
  - demonstration_264
  - demonstration_266
  - demonstration_267
  - demonstration_268
  - demonstration_269
  - demonstration_272
  - demonstration_273

train_demos:
  - demonstration_211
  - demonstration_212
  - demonstration_217
  - demonstration_220
  - demonstration_221
  - demonstration_222
  - demonstration_223
  - demonstration_225
  - demonstration_226
  - demonstration_227
  - demonstration_228
  - demonstration_229
  - demonstration_230
  - demonstration_231
  - demonstration_234
  - demonstration_235
  - demonstration_236
  - demonstration_237
  - demonstration_238
  - demonstration_239
  - demonstration_240
  - demonstration_241
  - demonstration_242
  - demonstration_243
  - demonstration_244
  - demonstration_245
  - demonstration_246
  - demonstration_248
  - demonstration_249
  - demonstration_250
  - demonstration_251
  - demonstration_252
  - demonstration_253
  - demonstration_254
  - demonstration_256
  - demonstration_260
  - demonstration_262
  - demonstration_263
  - demonstration_264
  - demonstration_266
  - demonstration_267
  - demonstration_268
  - demonstration_269
  - demonstration_272
  - demonstration_273

test_demos:
  - demonstration_215
  - demonstration_216
  - demonstration_232
  - demonstration_233
  - demonstration_255
```

### configs/dataset/postit_note_sliding/ssl.yaml

```yaml
name: Postit Note Sliding SSL

dataset_path: ${data_path}/demonstrations/ssl

complete_demos:
  - demonstration_210
  - demonstration_211
  - demonstration_212
  - demonstration_213
  - demonstration_214
  - demonstration_215
  - demonstration_216
  - demonstration_217
  - demonstration_218
  - demonstration_219
  - demonstration_220
  - demonstration_221
  - demonstration_222
  - demonstration_223
  - demonstration_224
  - demonstration_225
  - demonstration_226
  - demonstration_227
  - demonstration_228
  - demonstration_229
  - demonstration_230
  - demonstration_231
  - demonstration_232
  - demonstration_233
  - demonstration_234
  - demonstration_235
  - demonstration_236
  - demonstration_237
  - demonstration_238
  - demonstration_239
  - demonstration_240
  - demonstration_241
  - demonstration_242
  - demonstration_243
  - demonstration_244
  - demonstration_245
  - demonstration_246
  - demonstration_247
  - demonstration_248
  - demonstration_249
  - demonstration_250
  - demonstration_251
  - demonstration_252
  - demonstration_253
  - demonstration_254
  - demonstration_255
  - demonstration_256
  - demonstration_257
  - demonstration_258
  - demonstration_259
  - demonstration_260
  - demonstration_261
  - demonstration_262
  - demonstration_263
  - demonstration_264
  - demonstration_265
  - demonstration_266
  - demonstration_267
  - demonstration_268
  - demonstration_269
  - demonstration_270
  - demonstration_271
  - demonstration_272
  - demonstration_273

train_demos:
  - demonstration_210
  - demonstration_211
  - demonstration_212
  - demonstration_213
  - demonstration_214
  - demonstration_217
  - demonstration_218
  - demonstration_219
  - demonstration_220
  - demonstration_221
  - demonstration_222
  - demonstration_223
  - demonstration_224
  - demonstration_225
  - demonstration_226
  - demonstration_227
  - demonstration_228
  - demonstration_229
  - demonstration_230
  - demonstration_231
  - demonstration_234
  - demonstration_235
  - demonstration_236
  - demonstration_237
  - demonstration_238
  - demonstration_239
  - demonstration_240
  - demonstration_241
  - demonstration_242
  - demonstration_243
  - demonstration_244
  - demonstration_245
  - demonstration_246
  - demonstration_247
  - demonstration_248
  - demonstration_249
  - demonstration_250
  - demonstration_251
  - demonstration_252
  - demonstration_253
  - demonstration_254
  - demonstration_256
  - demonstration_257
  - demonstration_258
  - demonstration_259
  - demonstration_260
  - demonstration_261
  - demonstration_262
  - demonstration_263
  - demonstration_264
  - demonstration_265
  - demonstration_266
  - demonstration_267
  - demonstration_268
  - demonstration_269
  - demonstration_270
  - demonstration_271
  - demonstration_272
  - demonstration_273

test_demos:
  - demonstration_215
  - demonstration_216
  - demonstration_232
  - demonstration_233
  - demonstration_255
```

### configs/demo_extract.yaml

```yaml
defaults:
  - _self_
  - image_parameters: planar_rotation # Used just for crop sizes
  - override hydra/hydra_logging: disabled  
  - override hydra/job_logging: disabled  

# Data to extract from the pickle files
ssl_data: false
sample: true
color_images: true
depth_images: true
states: true
actions: true

# data paths
storage_path: 'recorded_data/'
filter_path: 'filtered_data/'
target_path: 'extracted_data/'

# Number of view images 
num_cams: 3

# Delta for extracting states
min_action_distance: 2 # cm
```

### configs/demo_record.yaml

```yaml
defaults:
  - _self_
  - override hydra/hydra_logging: disabled  
  - override hydra/job_logging: disabled  

# Recorded Demostration Number
demo_num: 1

# data paths
storage_path: 'recorded_data/'

# Number of view images 
num_cams: 3

# State Offset
offset: 0
```

### configs/deploy.yaml

```yaml
defaults:
  - _self_
  - robot_camera
  - task: planar_rotation
  - override hydra/hydra_logging: disabled  
  - override hydra/job_logging: disabled  

model: VINN
absolute_actions: true

data_path: extracted_data/

run_loop: false
loop_frequency: 1 # 1 move per second
```

### configs/encoder/resnet18.yaml

```yaml
name: ResNet18 RGB Encoder

settings:
  _target_: holodex.utils.models.load_encoder
  encoder_type: 'resnet18'
  input_channels: 3
  weights_path: ${encoder_weights_path}
  pretrained: true

output_size: 512
```

### configs/encoder/resnet34.yaml

```yaml
name: ResNet34 RGB Encoder

settings:
  _target_: holodex.utils.models.load_encoder
  encoder_type: 'resnet34'
  input_channels: 3 
  weights_path: ${encoder_weights_path}
  pretrained: true

output_size: 512
```

### configs/encoder/resnet50.yaml

```yaml
name: ResNet50 RGB Encoder

settings:
  _target_: holodex.utils.models.load_encoder
  encoder_type: 'resnet50'
  input_channels: 3 
  weights_path: ${encoder_weights_path}
  pretrained: true

output_size: 2048
```

### configs/image_parameters/bottle_opening.yaml

```yaml
image_size: 224

crop_sizes:
  - [425, 325, 780, 720]
  - [740, 390, 1280, 720]
  - [35, 240, 500, 570]

mean_tensors:
  - [0.1263, 0.1659, 0.1996]
  - [0.2965, 0.3189, 0.3149]
  - [0.3692, 0.3976, 0.4237]
  - [0.6536]
  - [0.6181]
  - [0.6402]

std_tensors:
  - [0.1447, 0.1443, 0.1587]
  - [0.2839, 0.2585, 0.2476]
  - [0.2775, 0.2682, 0.2610]
  - [0.2007]
  - [0.3108]
  - [0.3012]
```

### configs/image_parameters/can_spinning.yaml

```yaml
image_size: 224

crop_sizes:
  - [386, 144, 835, 685]
  - [565, 55, 1195, 600]
  - [180, 60, 645, 450]

mean_tensors:
  - [0.3949, 0.4167, 0.4338]
  - [0.4747, 0.5043, 0.5243]
  - [0.4503, 0.4983, 0.5393]
  - [0.6563]
  - [0.8641]
  - [1.2326]

std_tensors:
  - [0.2126, 0.1988, 0.1989]
  - [0.2449, 0.2296, 0.2329]
  - [0.2514, 0.2351, 0.2363]
  - [0.4296]
  - [0.6276]
  - [1.1214]
```

### configs/image_parameters/card_sliding.yaml

```yaml
image_size: 224

crop_sizes:
  - [485, 175, 895, 590]
  - [580, 350, 1075, 705]
  - [245, 325, 660, 665]

mean_tensors:
  - [0.2390, 0.2669, 0.2912]
  - [0.3843, 0.3791, 0.3811]
  - [0.4851, 0.4383, 0.4330]
  - [0.4960]
  - [0.6240]
  - [0.7219]

std_tensors:
  - [0.2246, 0.2145, 0.2135]
  - [0.2882, 0.2556, 0.2378]
  - [0.3132, 0.2799, 0.2530]
  - [0.7618]
  - [0.2841]
  - [0.3259]
```

### configs/image_parameters/object_flipping.yaml

```yaml
image_size: 224

crop_sizes:
  - [386, 144, 835, 685]
  - [565, 55, 1195, 600]
  - [180, 60, 645, 450]

mean_tensors:
  - [0.3949, 0.4167, 0.4338]
  - [0.4747, 0.5043, 0.5243]
  - [0.4503, 0.4983, 0.5393]
  - [0.6563]
  - [0.8641]
  - [1.2326]

std_tensors:
  - [0.2126, 0.1988, 0.1989]
  - [0.2449, 0.2296, 0.2329]
  - [0.2514, 0.2351, 0.2363]
  - [0.4296]
  - [0.6276]
  - [1.1214]
```

### configs/image_parameters/planar_rotation.yaml

```yaml
image_size: 224

crop_sizes:
  - [386, 144, 835, 685]
  - [565, 55, 1195, 600]
  - [180, 60, 645, 450]

mean_tensors:
  - [0.3949, 0.4167, 0.4338]
  - [0.4747, 0.5043, 0.5243]
  - [0.4503, 0.4983, 0.5393]
  - [0.6563]
  - [0.8641]
  - [1.2326]

std_tensors:
  - [0.2126, 0.1988, 0.1989]
  - [0.2449, 0.2296, 0.2329]
  - [0.2514, 0.2351, 0.2363]
  - [0.4296]
  - [0.6276]
  - [1.1214]
```

### configs/image_parameters/postit_note_sliding.yaml

```yaml
image_size: 224

crop_sizes:
  - [485, 175, 895, 590]
  - [580, 350, 1075, 705]
  - [245, 325, 660, 665]

mean_tensors:
  - [0.2402, 0.2693, 0.2936]
  - [0.3908, 0.3933, 0.3906]
  - [0.4939, 0.4597, 0.4475]
  - [0.4953]
  - [0.6228]
  - [0.7241]

std_tensors:
  - [0.2246, 0.2151, 0.2132]
  - [0.2907, 0.2617, 0.2411]
  - [0.3204, 0.2880, 0.2596]
  - [0.7371]
  - [0.2850]
  - [0.3322]
```

### configs/robot_camera.yaml

```yaml
robot_cam_serial_numbers:
  - "023322061741"
  - "021422062804"
  - "023322062082"

# Robot camera stream resolution
resolution: [1280, 720]

# Visualize image streams
visualize_stream: false
```

### configs/ssl_method/byol.yaml

```yaml
name: BYOL

project_name: byol-pretraining
```

### configs/ssl_method/mocov3.yaml

```yaml
name: MoCo

project_name: moco-pretraining

momentum: 0.9
temperature: 0.1

expander:
  # Input size is the encoder's output size
  output_size: 8192
  hidden_sizes: [8192]
  enable_batchnorm: true

projector:
  # Input size is the expander's output size
  output_size: 8192
  hidden_sizes: [8192]
  enable_batchnorm: true
```

### configs/ssl_method/simclr.yaml

```yaml
name: SimCLR

project_name: simclr-pretraining

color_jitter_const: 1
temperature: 0.1

projector:
  # Input size is the encoder's output size
  output_size: 8192
  hidden_sizes: [8192]
  enable_batchnorm: true
```

### configs/ssl_method/vicreg.yaml

```yaml
name: VICReg

project_name: vicreg-pretraining

projector:
  # Input size is the encoder's output size
  output_size: 8192
  hidden_sizes: [8192]
  enable_batchnorm: true

sim_coef: 25
std_coef: 25
cov_coef: 1
```

### configs/task/bottle_opening.yaml

```yaml
defaults:
  - _self_
  - /dataset: bottle_opening/filtered
  - /encoder: resnet18
  - /image_parameters: bottle_opening

arm_position: bottle
selected_view: 1

run_store_path: deploy_runs/bottle_opening/${model}

vinn:
  min_action_distance: 0.02

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Bottle Opening SSL/BYOL - ${encoder.name} - View ${selected_view} - Bottle Opening SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Bottle Opening Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Bottle Opening Filtered_best.pt
```

### configs/task/can_spinning.yaml

```yaml
defaults:
  - _self_
  - /dataset: can_spinning/filtered
  - /encoder: resnet18
  - /image_parameters: can_spinning

arm_position: flat
selected_view: 1

run_store_path: deploy_runs/can_spinning/${model}

vinn:
  min_action_distance: 0.02

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Can Spinning SSL/BYOL - ${encoder.name} - View ${selected_view} - Can Spinning SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Can Spinning Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Can Spinning Filtered_best.pt
```

### configs/task/card_sliding.yaml

```yaml
defaults:
  - _self_
  - /dataset: card_sliding/filtered
  - /encoder: resnet18
  - /image_parameters: card_sliding

arm_position: slide
selected_view: 3

run_store_path: deploy_runs/card_sliding/${model}

vinn:
  min_action_distance: 0.02

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Card Sliding SSL/BYOL - ${encoder.name} - View ${selected_view} - Card Sliding SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Card Sliding Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Card Sliding Filtered_best.pt
```

### configs/task/object_flipping.yaml

```yaml
defaults:
  - _self_
  - /dataset: object_flipping/filtered
  - /encoder: resnet18
  - /image_parameters: object_flipping

arm_position: flat
selected_view: 1

run_store_path: deploy_runs/object_flipping/${model}

vinn:
  min_action_distance: 0.005

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Object Flipping SSL/BYOL - ${encoder.name} - View ${selected_view} - Object Flipping SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Object Flipping Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Object Flipping Filtered_best.pt
```

### configs/task/planar_rotation.yaml

```yaml
defaults:
  - _self_
  - /dataset: planar_rotation/clipped_trajectory
  - /encoder: resnet18
  - /image_parameters: planar_rotation
 
arm_position: flat
selected_view: 1

run_store_path: deploy_runs/planar_rotation/${model}

vinn:
  min_action_distance: 0.02 

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Planar Rotation SSL/BYOL - ${encoder.name} - View ${selected_view} - Planar Rotation SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Planar Rotation Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Planar Rotation Filtered_best.pt
```

### configs/task/postit_note_sliding.yaml

```yaml
defaults:
  - _self_
  - /dataset: postit_note_sliding/filtered
  - /encoder: resnet18
  - /image_parameters: postit_note_sliding

arm_position: slide
selected_view: 3

run_store_path: deploy_runs/postit_note_sliding/${model}

vinn:
  min_action_distance: 0.02

  data_path: ${task.dataset.dataset_path}
  demos_list: ${task.dataset.complete_demos}

  nn_buffer_limit: 10

  encoder_weights_path: model_weights/BYOL - ${encoder.name} - View ${selected_view} - Postit Note Sliding SSL/BYOL - ${encoder.name} - View ${selected_view} - Postit Note Sliding SSL_best.pt
  absolute_actions: ${absolute_actions}

bc:
  predictor:
    input_dim: 512
    output_dim: 12
    hidden_dims: [1024, 2024, 512, 512] 
    use_batchnorm: true

  model_weights: model_weights/Behavior Cloning - ${encoder.name} - View ${selected_view} - Postit Note Sliding Filtered/Behavior Cloning - ${encoder.name} - View ${selected_view} - Postit Note Sliding Filtered_best.pt
```

### configs/teleop.yaml

```yaml
defaults:
  - _self_
  - robot_camera
  - tracker: oculus
  - override hydra/hydra_logging: disabled  
  - override hydra/job_logging: disabled  

finger_configs:
  freeze_index: false # Keep index finger fixed at [0, 0, 0, 0]
  freeze_middle: false # Keep middle finger fixed at [0, 0, 0, 0]
  three_dim: true

hydra:  
  output_subdir: null  
  run:  
    dir: .
```

### configs/tracker/mediapipe.yaml

```yaml
type: MP

# Realsense camera serial number
cam_serial_num: "138422075648"

# Camera resolution
resolution: [1280, 720]

# Moving average coefficient
alpha: 0.8

# Visualize 3D and 2D plots
visualize_graphs: true

# Visualize Predicted camera stream
visualize_pred_stream: true
pred_stream_rotation_angle: 180
```

### configs/tracker/oculus.yaml

```yaml
type: VR

# Host address
host: 172.24.71.211
keypoint_stream_port: 8087

# Streaming robot camera
stream_robot_cam: true
stream_camera_num: 1
stream_camera_rotation_angle: 180
robot_cam_stream_port: 10005

# Streaming Ports
plot_stream_port: 15001

# Visualize 3D and 2D plots
visualize_right_graphs: true

# Visualize left hand direction
visualize_left_graphs: false
```

### configs/train_bc.yaml

```yaml
defaults:
  - _self_
  - encoder: resnet18
  - dataset: planar_rotation/clipped_trajectory
  - image_parameters: planar_rotation

data_path: extracted_data/

encoder_gradient: false # True for full BC and false for BC Rep

# Datset settings
image_type: color
absolute_actions: true
selected_view: 1

# Encoder weight initialization
encoder_weights_path: null

# Predictor
predictor:
  input_dim: ${encoder.output_size}
  output_dim: 12
  hidden_dims: [1024, 2024, 512, 512]
  use_batchnorm: true
  dropout: null

# Training settings
device: 0
epochs: 1
num_workers: 12
train_test_split: true

# Hyperparameters
lr: 2e-4 
seed: 42
batch_size: 1024
momentum: 0.9
weight_decay: 1e-6
action_scaling_factor: 1e3

optimizer: Adam

# Logging
log_path: training_logs
project_name: behavior-cloning
wandb: true
tb: true

# Checkpointing
run_name: Behavior Cloning - ${encoder.name} - View ${selected_view} - ${dataset.name}
checkpoint_path: model_weights/${run_name}
checkpoint_interval: 10
```

### configs/train_ssl.yaml

```yaml
defaults:
  - _self_
  - ssl_method: byol
  - encoder: resnet18
  - dataset: planar_rotation/ssl
  - image_parameters: planar_rotation

# Directory settings
data_path: extracted_data/

# Encoder initialization
encoder_weights_path: null

# Data configs
image_type: color
selected_view: 1

# Training Settings
device: 0
epochs: 1
num_workers: 12

# Hyperparameters
lr: 2e-1
seed: 42
batch_size: 512
momentum: 0.9
weight_decay: 1.5e-6

optimizer: LARS

# Logging
log_path: training_logs
project_name: ${ssl_method.project_name}
wandb: false
tb: false

# Checkpointing
run_name: ${ssl_method.name} - ${encoder.name} - View ${selected_view} - ${dataset.name}
checkpoint_path: model_weights/${run_name}
checkpoint_interval: 10
```

### holodex/components/robot_operators/configs/allegro_mp.yaml

```yaml
index:
  x_coord: 0.0542 

  x_top: 0.1188
  x_bottom: 0.0417

  y_coord: 0.0532

  z_top: 0.1061
  z_bottom: -0.041

middle: 
  x_coord: 0.0542 
  
  x_top: 0.1188
  x_bottom: 0.0417

  y_coord: 0

  z_top: 0.1204
  z_bottom: -0.044

ring:
  x_coord: 0.0542 

  x_top: 0.1188
  x_bottom: 0.0417

  y_left: -0.0791
  y_right: -0.0141

  z_top: 0.1153
  z_bottom: -0.0386

thumb:
  x_coord: 0.0542

  x_top: 0.129
  x_bottom: 0.0367

  yz_top_right: 
    - 0.1126
    - -0.0217

  yz_bottom_right: 
    - 0.0752
    - -0.1037

  yz_bottom_left: 
    - -0.052
    - -0.0886
    
  yz_top_left: 
    - -0.0372
    - -0.0213
```

### holodex/components/robot_operators/configs/allegro_vr.yaml

```yaml
thumb:
  x_coord: 0.054

  index_x_top: 0.117
  index_x_bottom: 0.0169

  middle_x_top: 0.117
  middle_x_bottom: 0.054

  ring_x_top: 0.117
  ring_x_bottom: 0.0518
  
  bottom_right:
    - 0.1321
    - -0.0481

  top_right:
    - 0.1154
    - -0.0051

  index_top:
    - 0.0495
    - 0.0106

  index_bottom:
    - 0.0413
    - -0.1017

  middle_top:
    - 0.0094
    - 0.0124
    
  middle_bottom:
    -  0.0079
    - -0.0997

  ring_top:
    - -0.024
    - -0.0087

  ring_bottom:
    - -0.0373
    - -0.0961

```

### holodex/robot/configs/allegro_bounds.yaml

```yaml
# Joint movement bound per input coordinate
jointwise_angle_bounds: 
  # Index finger angles
  - 0.05
  - 0.2
  - 0.2
  - 0.2
  # Middle finger angles
  - 0.05
  - 0.2
  - 0.2
  - 0.2
  # Ring finger angles
  - 0.05
  - 0.2
  - 0.2
  - 0.2
  # Thumb finger angles
  - 0.2
  - 0.1
  - 0.2
  - 0.2

# Moving average time steps
time_steps: 1

# Angle scaling factors
linear_scaling_factors: [1.1, 1.1, 1.1]
rotatory_scaling_factors: 
  index: 0.02
  middle: 0.02
  ring: 0.05
```

### holodex/robot/configs/allegro_info.yaml

```yaml
total_num_joints: 16
joints_per_finger: 4

# Fingers and their offsets
fingers:
  index:
    name: 'Index'
    offset: 0
  
  middle:
    name: 'Middle'
    offset: 4

  ring:
    name: 'Ring'
    offset: 8

  thumb:
    name: 'Thumb'
    offset: 12
```

### holodex/robot/configs/allegro_link_info.yaml

```yaml
#  Finger info
links_info:

  # Base link 
  base:
    name: 'Base'
    link: 'base_link'

  # Index link
  index:
    name: 'Index'
    link: 'joint_0.0'
    offset: 0
    joint_min: 
      - -0.47
      - -0.196 
      - -0.174
      - -0.227
    joint_max: 
      - 0.47
      - 1.61
      - 1.709
      - 1.618

  # Middle link
  middle:
    name: 'Middle'
    link: 'joint_4.0'
    offset: 4
    joint_min: 
      - -0.47
      - -0.196 
      - -0.174
      - -0.227
    joint_max: 
      - 0.47
      - 1.61
      - 1.709
      - 1.618
  
  # Ring link
  ring:
    name: 'Ring'
    link: 'joint_8.0'
    offset: 8
    joint_min: 
      - -0.47
      - -0.196 
      - -0.174
      - -0.227
    joint_max: 
      - 0.47
      - 1.61
      - 1.709
      - 1.618

  # Thumb link
  thumb:
    name: 'Thumb'
    link: 'joint_12.0'
    offset: 12
    joint_min: 
      - 0.263 
      - -0.105
      - -0.189
      - -0.162
    joint_max: 
      - 1.396
      - 2
      - 1.644
      - 1.719
```

## Python signatures and reward/observation bodies (5 files)


### holodex/models/self_supervised_pretraining/mocov3.py

```
class MoCo(Module)
    def __init__(self, base_encoder, momentum_encoder, predictor, first_augment_fn, sec_augment_fn, temperature)
    def _update_momentum_encoder(self, m)
    def contrastive_loss(self, q, k)
    def encoder(self)
    def forward(self, x, m)
def adjust_moco_momentum(epoch, momentum, total_epochs)
def concat_all_gather(tensor)
```

### holodex/models/self_supervised_pretraining/simclr.py

```
class SimCLR(Module)
    def __init__(self, encoder, projector, augment_fn, sec_augment_fn, temperature)
    def get_image_representation(self, image, is_second_img)
    def forward(self, image)
    def get_encoder_weights(self)
```

### holodex/models/self_supervised_pretraining/vicreg.py

```
class VICReg(Module)
    def __init__(self, backbone, projector, augment_fn, sim_coef, std_coef, cov_coef)
    def get_image_representation(self, image)
    def forward(self, image)
    def get_encoder_weights(self)
```

### train_bc.py

```
class Workspace(object)
    def __init__(self, configs)
    def _init_datasets(self)
    def _init_model(self)
    def _init_optimizer(self)
    def train_one_epoch(self)
    def test_one_epoch(self)
    def _save_snapshot(self, obs_loss, epoch)
    def train(self)
def main(configs)
```

### train_ssl.py

```
class Workspace(object)
    def __init__(self, configs)
    def _init_datasets(self)
    def _init_model(self)
    def _init_optimizer(self)
    def train_one_epoch(self, epoch_num)
    def _save_snapshot(self, obs_loss, epoch)
    def train(self)
def main(configs)
```