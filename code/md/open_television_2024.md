# open_television_2024

source: https://github.com/OpenTeleVision/TeleVision


commit: e6e25afdb16c1b326b5bf37bd0ae79919bf79f26


## README

<h1 align="center"><img src="img/logo.png" width="40"> Open-TeleVision: Teleoperation with

Immersive Active Visual Feedback</h1>

<p align="center">
    <a href="https://chengxuxin.github.io/"><strong>Xuxin Cheng*</strong></a>
    ·
    <a href=""><strong>Jialong Li*</strong></a>
    ·
    <a href="https://aaronyang1223.github.io/"><strong>Shiqi Yang</strong></a>
    <br>
    <a href="https://www.episodeyang.com/"><strong>Ge Yang</strong></a>
    ·
    <a href="https://xiaolonw.github.io/"><strong>Xiaolong Wang</strong></a>
</p>

<p align="center">
    <img src="img/UCSanDiegoLogo-BlueGold.png" height=50"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    <img src="img/mit-logo.png" height="50">
</p>

<h3 align="center"> CoRL 2024 </h3>

<p align="center">
<h3 align="center"><a href="https://robot-tv.github.io/">Website</a> | <a href="https://arxiv.org/abs/2407.01512/">arXiv</a> | <a href="">Video</a> | <a href="">Summary</a> </h3>
  <div align="center"></div>
</p>

<p align="center">
<img src="./img/main.webp" width="80%"/>
</p>

## Introduction
This code contains implementation for teleoperation and imitation learning of Open-TeleVision.

## Installation

```bash
    conda create -n tv python=3.8
    conda activate tv
    pip install -r requirements.txt
    cd act/detr && pip install -e .
```

Install ZED sdk: https://www.stereolabs.com/developers/release/

Install ZED Python API:
```
    cd /usr/local/zed/ && python get_python_api.py
```

If you want to try teleoperation example in a simulated environment (teleop_hand.py):

Install Isaac Gym: https://developer.nvidia.com/isaac-gym/

## Teleoperation Guide

### Local streaming
For **Quest** local streaming, follow [this](https://github.com/OpenTeleVision/TeleVision/issues/12#issue-2401541144) issue.

**Apple** does not allow WebXR on non-https connections. To test the application locally, we need to create a self-signed certificate and install it on the client. You need a ubuntu machine and a router. Connect the VisionPro and the ubuntu machine to the same router. 
1. install mkcert: https://github.com/FiloSottile/mkcert
2. check local ip address: 

```
    ifconfig | grep inet
```
Suppose the local ip address of the ubuntu machine is `192.168.8.102`.

3. create certificate: 

```
    mkcert -install && mkcert -cert-file cert.pem -key-file key.pem 192.168.8.102 localhost 127.0.0.1
```
ps. place the generated `cert.pem` and `key.pem` files in `teleop`.

4. open firewall on server
```
    sudo iptables -A INPUT -p tcp --dport 8012 -j ACCEPT
    sudo iptables-save
    sudo iptables -L
```
or can be done with `ufw`:
```
    sudo ufw allow 8012
```
5.
```
    tv = OpenTeleVision(self.resolution_cropped, shm.name, image_queue, toggle_streaming, ngrok=False)
```

6. install ca-certificates on VisionPro
```
    mkcert -CAROOT
```
Copy the rootCA.pem via AirDrop to VisionPro and install it.

Settings > General > About > Certificate Trust Settings. Under "Enable full trust for root certificates", turn on trust for the certificate.

settings > Apps > Safari > Advanced > Feature Flags > Enable WebXR Related Features

7. open the browser on Safari on VisionPro and go to `https://192.168.8.102:8012?ws=wss://192.168.8.102:8012`

8. Click `Enter VR` and ``Allow`` to start the VR session.

### Network Streaming
For Meta Quest3, installation of the certificate is not trivial. We need to use a network streaming solution. We use `ngrok` to create a secure tunnel to the server. This method will work for both VisionPro and Meta Quest3.

1. Install ngrok: https://ngrok.com/download
2. Run ngrok
```
    ngrok http 8012
```
3. Copy the https address and open the browser on Meta Quest3 and go to the address.

ps. When using ngrok for network streaming, remember to call `OpenTeleVision` with:
```
    self.tv = OpenTeleVision(self.resolution_cropped, self.shm.name, image_queue, toggle_streaming, ngrok=True)
```

### Simulation Teleoperation Example
1. After setup up streaming with either local or network streaming following the above instructions, you can try teleoperating two robot hands in Issac Gym:
```
    cd teleop && python teleop_hand.py
```
2. Go to your vuer site on VisionPro, click `Enter VR` and ``Allow`` to enter immersive environment.

3. See your hands in 3D!
<img src=img/sim.png>

## Training Guide
1. Download dataset from https://drive.google.com/drive/folders/11WO96mUMjmxRo9Hpvm4ADz7THuuGNEMY?usp=sharing.

2. Place the downloaded dataset in ``data/recordings/``.

3. Process the specified dataset for training using ``scripts/post_process.py``.

4. You can verify the image and action sequences of a specific episode in the dataset using ``scripts/replay_demo.py``.

5. To train ACT, run:
```
    python imitate_episodes.py --policy_class ACT --kl_weight 10 --chunk_size 60 --hidden_dim 512 --batch_size 45 --dim_feedforward 3200 --num_epochs 50000 --lr 5e-5 --seed 0 --taskid 00 --exptid 01-sample-expt
```

6. After training, save jit for the desired checkpoint:
```
    python imitate_episodes.py --policy_class ACT --kl_weight 10 --chunk_size 60 --hidden_dim 512 --batch_size 45 --dim_feedforward 3200 --num_epochs 50000 --lr 5e-5 --seed 0 --taskid 00 --exptid 01-sample-expt\
                               --save_jit --resume_ckpt 25000
```

7. You can visualize the trained policy with inputs from dataset using ``scripts/deploy_sim.py``, example usage:
```
    python deploy_sim.py --taskid 00 --exptid 01 --resume_ckpt 25000
```

## Citation
```
@article{cheng2024tv,
title={Open-TeleVision: Teleoperation with Immersive Active Visual Feedback},
author={Cheng, Xuxin and Li, Jialong and Yang, Shiqi and Yang, Ge and Wang, Xiaolong},
journal={arXiv preprint arXiv:2407.01512},
year={2024}
}
```


## File tree (depth 3, assets pruned)

```
.gitignore
LICENSE
README.md
act/
  LICENSE
  README.md
  conda_env.yaml
  detr/
    LICENSE
    README.md
    main.py
    models/
    setup.py
    util/
  imitate_episodes.py
  policy.py
  utils.py
requirements.txt
scripts/
  deploy_sim.py
  plot_action.py
  post_process.py
  replay_demo.py
teleop/
  Preprocessor.py
  TeleVision.py
  constants_vuer.py
  dynamixel/
    active_cam.py
    agent.py
    driver.py
    dynamixel_robot.py
    robot.py
  inspire_hand.yml
  motion_utils.py
  teleop_active_cam.py
  teleop_hand.py
  webrtc/
    client.js
    index.html
    orig_webcam_example.py
    webcam.py
    webcam_server.py
    zed_server.py
```

## Config files (2)


### act/conda_env.yaml

```yaml
name: aloha
channels:
  - pytorch
  - nvidia
  - conda-forge
dependencies:
  - python=3.9
  - pip=23.0.1
  - pytorch=2.0.0
  - torchvision=0.15.0
  - pytorch-cuda=11.8
  - pyquaternion=0.9.9
  - pyyaml=6.0
  - rospkg=1.5.0
  - pexpect=4.8.0
  - mujoco=2.3.3
  - dm_control=1.0.9
  - py-opencv=4.7.0
  - matplotlib=3.7.1
  - einops=0.6.0
  - packaging=23.0
  - h5py=3.8.0
  - ipython=8.12.0

```

### teleop/inspire_hand.yml

```yaml
left:
  type: vector
  urdf_path: inspire_hand/inspire_hand_left.urdf
  wrist_link_name: "L_hand_base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  target_origin_link_names: [ "L_hand_base_link", "L_hand_base_link", "L_hand_base_link", "L_hand_base_link", "L_hand_base_link" ]
  target_task_link_names: [ "L_thumb_tip", "L_index_tip", "L_middle_tip", "L_ring_tip", "L_pinky_tip" ]
  scaling_factor: 1.1

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 9, 14, 19, 24 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.5

right:
  type: vector
  urdf_path: inspire_hand/inspire_hand_right.urdf
  wrist_link_name: "R_hand_base_link"

  # Target refers to the retargeting target, which is the robot hand
  target_joint_names: null
  target_origin_link_names: [ "R_hand_base_link", "R_hand_base_link", "R_hand_base_link", "R_hand_base_link", "R_hand_base_link" ]
  target_task_link_names: [ "R_thumb_tip", "R_index_tip", "R_middle_tip", "R_ring_tip", "R_pinky_tip" ]
  scaling_factor: 1.1

  # Source refers to the retargeting input, which usually corresponds to the human hand
  # The joint indices of human hand joint which corresponds to each link in the target_link_names
  target_link_human_indices: [ [ 0, 0, 0, 0, 0 ], [ 4, 9, 14, 19, 24 ] ]

  # A smaller alpha means stronger filtering, i.e. more smooth but also larger latency
  low_pass_alpha: 0.5
```

## Python signatures and reward/observation bodies (4 files)


### act/policy.py

```
class ACTPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
class CNNMLPPolicy(Module)
    def __init__(self, args_override)
    def __call__(self, qpos, image, actions, is_pad)
    def configure_optimizers(self)
def kl_divergence(mu, logvar)
```

### scripts/deploy_sim.py

```
def get_norm_stats(data_path)
def load_policy(policy_path, device)
def normalize_input(state, left_img, right_img, norm_stats, last_action_data)
def merge_act(actions_for_curr_step, k)
```

### teleop/teleop_hand.py

```
class VuerTeleop()
    def __init__(self, config_file_path)
    def step(self)
class Sim()
    def __init__(self, print_freq)
    def step(self, head_rmat, left_pose, right_pose, left_qpos, right_qpos)
    def end(self)
```