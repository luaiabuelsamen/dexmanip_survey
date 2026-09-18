# bunny_visionpro_2024

source: https://github.com/Dingry/BunnyVisionPro


commit: ea55fccf4d56209562310207b40395557fea778a


## README

<!-- PROJECT LOGO -->

<p align="center">

  <h1 align="center"><img src="docs/assets/logo/bunny.png" width="80">Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning></h1>
  <p align="center">
    <a href="https://dingry.github.io/"><strong>Runyu Ding</strong></a>
    ·
    <a href="https://yzqin.github.io/"><strong>Yuzhe Qin</strong></a>
    ·
    <a href="https://jiyuezh.github.io/"><strong>Jiyue Zhu</strong></a>
    ·
    <a href="https://www.researchgate.net/profile/Chengzhe-Jia"><strong>Chengzhe Jia</strong></a>
    <br>
    <a href="https://aaronyang1223.github.io/"><strong>Shiqi Yang</strong></a>
    ·
    <a href="https://rchalyang.github.io/"><strong>Ruihan Yang</strong></a>
    .
    <a href="https://xjqi.github.io/"><strong>Xiaojuan Qi</strong></a>
    .
    <a href="https://xiaolonw.github.io/"><strong>Xiaolong Wang</strong></a>
  </p>
  <h3 align="center"><a href="https://arxiv.org/abs/2407.03162">Paper</a> | <a href="https://dingry.github.io/projects/bunny_visionpro.html">Project Page</a> | <a href="https://dingry.github.io/BunnyVisionPro/">Documentation</a> | <a href="https://github.com/Dingry/bunny_teleop_server">Teleop Server Code</a> | <a href="https://docs.google.com/document/d/1V2H-Bgph3yEbQx_28yVG5igzBUv5WU2KjNU9RD1ZMk8/edit?usp=sharing">Haptics Implementation</a></h3>
  <div align="center"></div>
</p>

<img src="docs/assets/images/Multi_Robot.webp" alt="Teleoperation with various robots.">

## :wrench: Installation and Usage

Please refer to the [documentation](https://dingry.github.io/BunnyVisionPro/) for detailed installation and usage
instructions.

## :tada: News
- [2024/07/16] :fire: Release of real robot control code for the XArm7 and Ability Hand. Check out [README](real_control/README.md).
- [2024/05/06] Initial release with basic usage of bimanual teleoperation with Vision Pro. Check out
  the [documentation](https://dingry.github.io/BunnyVisionPro/).

## :white_check_mark: TODO

- [x] Tutorial for initialization
- [x] Tutorial for tips and troubleshooting
- [x] Tutorial for retargeting
- [x] Release haptic feedback device design 
- [x] Real control code of XArm7 and Ability Hand
- [ ] Robot collision avoidance
- [ ] Robot arm singularity avoidance
- [ ] Collision-free retargeting

## :seedling: Acknowledgement

Our code is built
upon [VisionProTeleop](https://github.com/Improbable-AI/VisionProTeleop), [dex-retargeting](https://github.com/dexsuite/dex-retargeting), [sim-web-visualizer](https://github.com/NVlabs/sim-web-visualizer).
We thank all these authors for their nicely open sourced code and their great contributions to the community.

## :rabbit: Citation

```
@article{bunny-visionpro,
    title   = {Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning}, 
    author  = {Runyu Ding and Yuzhe Qin and Jiyue Zhu and Chengzhe Jia and Shiqi Yang and Ruihan Yang and Xiaojuan Qi and Xiaolong Wang},
    year    = {2024},
    url     = {https://arxiv.org/abs/2407.03162}, 
}
```


## File tree (depth 3, assets pruned)

```
.editorconfig
.github/
  workflows/
    build_stable.yml
    doc.yml
.gitignore
LICENSE
README.md
bunny_teleop/
  __init__.py
  bimanual_teleop_client.py
  bimanual_teleop_server.py
  init_config.py
examples/
  minimal/
    minimal.py
  retargeting/
    README.md
    render_retargeting.py
    retargeting.py
    save_offline_avp_stream.py
  sapien/
    README.md
    sapien_teleop_example.py
mkdocs.yml
pyproject.toml
real_control/
  README.md
  teleop_bimanual_xarm7_ability.py
  xarm7_ability.py
setup.py
```

## Config files (0)


## Python signatures and reward/observation bodies (4 files)


### bunny_teleop/init_config.py

```
class BimanualAlignmentMode(Enum)
class InitializationConfig()
    def __post_init__(self)
    def validate(self, dof_left, dof_right)
    def get_joint_index_mapping(self, server_side_joint_names, hand_index)
    def to_dict(self)
    def from_dict(cls, config)
```

### examples/retargeting/render_retargeting.py

```
def render_by_sapien(meta_data, data, output_video_path)
def main(pickle_path, output_video_path)
```

### examples/retargeting/retargeting.py

```
def three_mat_mul(left_rot, mat, right_rot)
def two_mat_batch_mul(batch_mat, left_rot)
def joint_avp2hand(finger_mat)
def filter_data(data, fps, duration)
def retarget_video(left_retargeting, right_retargeting, data_path, output_path, config_paths)
def main(robot_name, data_path, output_path)
```

### examples/retargeting/save_offline_avp_stream.py

```
def main(avp_ip)
```