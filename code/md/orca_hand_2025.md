# orca_hand_2025

source: https://github.com/orcahand/orca_core


commit: 4a99afd8ef8b368d4cb84a10e4a1d5e732aca660


## README

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2504.04259" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2504.04259-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.gg/xvGyxaccRa" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-orcahand-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="https://x.com/orcahand" target="_blank"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/orcahand?style=social"/></a>
  <a href="https://orcahand.com" target="_blank"><img alt="Website" src="https://img.shields.io/badge/Website-orcahand.com-blue?style=flat&logo=google-chrome"/></a>
  <br>
  <a href="https://github.com/orcahand/orca_core" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/orcahand/orca_core?style=social"/></a>
  <a href="https://github.com/orcahand/orca_core/actions/workflows/test.yml" target="_blank"><img alt="Tests" src="https://github.com/orcahand/orca_core/actions/workflows/test.yml/badge.svg"/></a>
</div>

Orca Core is the core control package of the ORCA Hand. It's used to abstract hardware, provide scripts for calibration, tensioning and to control the hand with simple high-level control methods in joint space.

## Get Started

To get started with Orca Core, follow these steps:

1. **Sync a local development environment with `uv`**:

    ```sh
    uv sync --group dev
    ```

    This creates a local `.venv` and installs the package plus development dependencies.

2. **Run commands through `uv`**:

    ```sh
    uv run pytest
    ```

    If you prefer an activated shell, you can still use:

    ```sh
    source .venv/bin/activate      # macOS / Linux
    .venv\Scripts\activate         # Windows
    ```

    End users who do not use `uv` can still install the package with:

    ```sh
    pip install .
    ```

3. **Check the configuration file**:

    - Review the config file (e.g., `orca_core/models/v2/orcahand-right/config.yaml`) and make sure it matches your hardware setup.

4. **Run the tension and calibration scripts**:

    ```sh
    uv run python scripts/tension.py orca_core/models/v2/orcahand-right/config.yaml
    uv run python scripts/calibrate.py orca_core/models/v2/orcahand-right/config.yaml
    ```

    Replace the path with your specific hand model folder if needed.

5. **Move the hand to the neutral position**:

    ```sh
    uv run python scripts/neutral.py orca_core/models/v2/orcahand-right/config.yaml
    ```

---

## Troubleshooting

### Serial Port Permissions (Linux)

On Linux, the serial port (e.g., `/dev/ttyACM0`) is owned by the `dialout` group. If your user is not in this group, you will get a **permission denied** error and motors won't be detected.

**Permanent fix** (requires re-login):

```sh
sudo usermod -aG dialout $USER
```

**Temporary fix** (resets on reboot/replug):

```sh
sudo chmod 666 /dev/ttyACM0
```

### Windows

Supported on Windows 10 and 11; no permission setup is needed. Ports are named `COM3`, `COM4`, ... and are listed with:

```sh
uv run python -m serial.tools.list_ports -v
```

Driver notes, latency settings and the first-connection checklist: [Running on Windows](docs/pages/getting-started-docs/windows.md).

### Serial port, baudrate, and motor type

By default these are all **auto-detected** at connect time.

However, you can declare them explicitly in `config.yaml`. Useful when:

- **multiple hands are connected** at once → `port` disambiguates which one
- **motors run at a non-default baudrate** → `baudrate` skips the probe sweep
- **the auto-detection picks the wrong family** → `motor_type` forces a specific one

```yaml
# Optional overrides:   auto-detected if omitted
port: /dev/ttyACM0      # /dev/cu.usbmodemXXXX on macOS, COM3 on Windows
baudrate: 1000000       # 1M for v2; 3M for v1
motor_type: dynamixel   # or 'feetech'
```



## File tree (depth 3, assets pruned)

```
.github/
  workflows/
    downstream.yml
    release.yml
    test.yml
.gitignore
CLAUDE.md
LICENSE
README.md
examples/
  demo_runner.py
  main_demo.py
  main_demo_abduction.py
  record_angles.py
  record_continuous.py
  replay_angles.py
  replay_continuous.py
  sequences/
    kapandji_opposition.yaml
  taxel_frames.py
mkdocs.yml
orca_core/
  __init__.py
  api/
    __init__.py
    api.py
  base_hand.py
  calibration.py
  constants.py
  control/
    __init__.py
    constants.py
    joint_controller.py
    joint_loop.py
  demo_poses.py
  hand_config.py
  hand_factory.py
  hardware/
    __init__.py
    dynamixel_client.py
    feetech/
    feetech_client.py
    hand_serial_link.py
    joint_encoder_client.py
    mock_dynamixel_client.py
    mock_hand_serial_link.py
    motor_client.py
    motor_factory.py
    motor_resolution.py
    sensing/
    tactile_client.py
  hardware_hand.py
  hardware_hand_sensing.py
  joint_position.py
  kinematics/
    __init__.py
    frames.py
    hand_kinematics.py
    transforms.py
  maintenance/
    __init__.py
    calibration_routine.py
    motor_chain.py
    tensioning.py
  models/
    v1/
    v2/
  utils/
    __init__.py
    cli.py
    utils.py
  version.py
pyproject.toml
scripts/
  calibrate.py
  check_motor.py
  check_sensors.py
  configure_motor_chain.py
  manual_control.py
  monitor_sensors.py
  neutral.py
  setup.py
  stress_test.py
  tension.py
  zero.py
tests/
  __init__.py
  _encoder_helpers.py
  _hand_feedback_helpers.py
  _helpers.py
  _loop_helpers.py
  conftest.py
  reference/
    calibration_expected.yaml
  test_api.py
  test_base_hand_contract.py
  test_calibration.py
  test_calibration_reference.py
  test_calibration_routine.py
  test_connect_resolution.py
  test_core.py
  test_demo_poses.py
  test_dynamixel_client_locking.py
  test_encoder_anchor_sampling.py
  test_encoder_polarity_by_side.py
  test_encoder_protocol.py
  test_feetech_client.py
  test_hand_class_layout.py
  test_hand_config_loading.py
  test_hand_detection.py
  test_hand_factory.py
  test_hand_serial_link.py
  test_hardware_constants.py
  test_hardware_hand.py
  test_hardware_hand_full.py
  test_hardware_hand_joint_feedback.py
  test_jitter.py
  test_joint_controller.py
  test_joint_encoder_client.py
  test_joint_loop.py
  test_kinematics.py
  test_kinematics_extractor.py
  test_mock_sensing_connect.py
  test_model_dispatch.py
  test_motor_chain.py
  test_motor_client_contract.py
  test_motor_client_registry.py
  test_public_api_surface.py
  test_sensing_errors.py
  test_sensing_health.py
  test_serial_discovery.py
  test_tactile_protocol.py
  test_tactile_rearm.py
  test_tactile_sensor.py
  test_taxel_frames.py
  test_taxel_geometry.py
  test_tension.py
  test_touch_connect.py
  test_windows_compat.py
  test_yaml.py
tools/
  check_downstream.py
  extract_urdf_kinematics.py
uv.lock
```

## Config files (13)


### orca_core/hardware/sensing/models/touch-sensor-finger/config.yaml

```yaml
name: touch-sensor-finger
description: ORCA Fingertip - Finger
frame: sensor
units: mm
num_taxels: 87
coordinates:
- x: 4.03569563
  y: 28.08244307
  z: 3.72577291
- x: 6.62767274
  y: 24.49442143
  z: 2.9712037
- x: 6.53635781
  y: 24.33135486
  z: 5.83911297
- x: 4.09826233
  y: 27.00584015
  z: 7.05315498
- x: 5.72524942
  y: 23.13913822
  z: 8.34520194
- x: 1.215e-05
  y: 23.87765425
  z: 10.75159362
- x: 3.13511549
  y: 23.80404808
  z: 10.10288971
- x: -0.00135166
  y: 28.02324631
  z: 7.86111074
- x: -0.00041269
  y: 29.21465893
  z: 3.96386436
- x: 7.38872988
  y: -1.83843131
  z: 9.31075593
- x: 4.25469072
  y: -1.83842924
  z: 12.2044915
- x: 0.00139008
  y: -1.8375095
  z: 12.76352439
- x: 0.00118076
  y: 1.36767275
  z: 11.08371687
- x: 0.0010128
  y: 4.17300381
  z: 9.76182211
- x: 0.00088397
  y: 7.66127894
  z: 8.9032549
- x: 0.0007587
  y: 10.66833351
  z: 9.60998857
- x: 0.00054434
  y: 14.13917019
  z: 10.6290711
- x: 0.00037025
  y: 17.19870209
  z: 11.12688274
- x: 0.00017672
  y: 20.81310695
  z: 11.20073003
- x: 6.37805738
  y: 20.12836446
  z: 8.46599775
- x: 6.19975695
  y: 16.80815911
  z: 8.75863336
- x: 6.09392303
  y: 13.78451673
  z: 8.28088525
- x: 5.81396004
  y: 10.82948586
  z: 7.59170343
- x: 5.67589675
  y: 7.37239728
  z: 7.04781175
- x: 5.6229397
  y: 4.30120402
  z: 7.98710121
- x: 6.51658251
  y: 1.00320616
  z: 8.81523868
- x: 2.90784487
  y: 10.8145338
  z: 9.36445453
- x: 3.1353787
  y: 4.13280498
  z: 9.48359329
- x: 3.59420968
  y: 1.33607952
  z: 10.72327448
- x: 2.85383295
  y: 7.20978104
  z: 8.63989556
- x: 3.69669249
  y: 17.22514737
  z: 10.57684617
- x: 3.05173451
  y: 13.72904124
  z: 10.2126987
- x: 3.5724037
  y: 20.29029381
  z: 10.63665947
- x: 7.49702381
  y: 21.41133315
  z: 2.32287156
- x: 7.91191336
  y: 18.23690022
  z: 1.65530874
- x: 8.01628097
  y: 15.03729215
  z: 0.98243386
- x: 7.95638556
  y: 11.78169855
  z: 0.8304708
- x: 7.90871925
  y: 8.51014555
  z: 0.83046985
- x: 8.00305533
  y: 4.69426217
  z: 0.83047505
- x: 8.18310978
  y: 1.42714225
  z: 0.8304852
- x: 8.39343911
  y: -1.83824164
  z: 0.83051365
- x: 8.48951463
  y: -1.83844166
  z: 5.16629332
- x: 7.59496851
  y: 11.08610671
  z: 4.65554922
- x: 7.70174458
  y: 4.37108182
  z: 4.67018384
- x: 8.14369098
  y: 1.28202463
  z: 4.96284079
- x: 7.45041044
  y: 7.98683531
  z: 4.41370589
- x: 7.94076231
  y: 17.55570873
  z: 5.00276188
- x: 7.81258117
  y: 14.21466797
  z: 5.08267734
- x: 7.61104993
  y: 20.74950266
  z: 5.49770801
- x: -4.03569563
  y: 28.08244307
  z: 3.72577291
- x: -6.62767274
  y: 24.49442143
  z: 2.9712037
- x: -6.53635781
  y: 24.33135486
  z: 5.83911297
- x: -4.09826233
  y: 27.00584015
  z: 7.05315498
- x: -5.72524942
  y: 23.13913822
  z: 8.34520194
- x: -3.13511549
  y: 23.80404808
  z: 10.10288971
- x: -7.38872988
  y: -1.83843131
  z: 9.31075593
- x: -4.25469072
  y: -1.83842924
  z: 12.2044915
- x: -6.37805738
  y: 20.12836446
  z: 8.46599775
- x: -6.19975695
  y: 16.80815911
  z: 8.75863336
- x: -6.09392303
  y: 13.78451673
  z: 8.28088525
- x: -5.81396004
  y: 10.82948586
  z: 7.59170343
- x: -5.67589675
  y: 7.37239728
  z: 7.04781175
- x: -5.6229397
  y: 4.30120402
  z: 7.98710121
- x: -6.51658251
  y: 1.00320616
  z: 8.81523868
- x: -2.90784487
  y: 10.8145338
  z: 9.36445453
- x: -3.1353787
  y: 4.13280498
  z: 9.48359329
- x: -3.59420968
  y: 1.33607952
  z: 10.72327448
- x: -2.85383295
  y: 7.20978104
  z: 8.63989556
- x: -3.69669249
  y: 17.22514737
  z: 10.57684617
- x: -3.05173451
  y: 13.72904124
  z: 10.2126987
- x: -3.5724037
  y: 20.29029381
  z: 10.63665947
- x: -7.49702381
  y: 21.41133315
  z: 2.32287156
- x: -7.91191336
  y: 18.23690022
  z: 1.65530874
- x: -8.01628097
  y: 15.03729215
  z: 0.98243386
- x: -7.95638556
  y: 11.78169855
  z: 0.8304708
- x: -7.90871925
  y: 8.51014555
  z: 0.83046985
- x: -8.00305533
  y: 4.69426217
  z: 0.83047505
- x: -8.18310978
  y: 1.42714225
  z: 0.8304852
- x: -8.39343911
  y: -1.83824164
  z: 0.83051365
- x: -8.48951463
  y: -1.83844166
  z: 5.16629332
- x: -7.59496851
  y: 11.08610671
  z: 4.65554922
- x: -7.70174458
  y: 4.37108182
  z: 4.67018384
- x: -8.14369098
  y: 1.28202463
  z: 4.96284079
- x: -7.45041044
  y: 7.98683531
  z: 4.41370589
- x: -7.94076231
  y: 17.55570873
  z: 5.00276188
- x: -7.81258117
  y: 14.21466797
  z: 5.08267734
- x: -7.61104993
  y: 20.74950266
  z: 5.49770801

```

### orca_core/hardware/sensing/models/touch-sensor-pinky/config.yaml

```yaml
name: touch-sensor-pinky
description: ORCA Fingertip - Pinky
frame: sensor
units: mm
num_taxels: 51
coordinates:
- x: -7.31378277
  y: -1.79988568
  z: 0.39999828
- x: -7.35349939
  y: -1.79999907
  z: 3.44426423
- x: -7.14890952
  y: 2.23310916
  z: 0.39995294
- x: -7.239463
  y: 1.5965166
  z: 3.25227094
- x: -6.96664673
  y: 5.76010809
  z: 0.39988187
- x: -7.06807114
  y: 5.49744394
  z: 3.03648049
- x: -6.58421581
  y: 9.77742185
  z: 0.39989891
- x: -6.00996443
  y: -1.79999958
  z: 6.67266775
- x: -6.16505672
  y: 1.39784473
  z: 6.53131412
- x: -6.19950575
  y: 5.14650534
  z: 6.31004181
- x: -6.80097742
  y: 8.9453581
  z: 2.83870363
- x: -5.89906718
  y: 8.44673336
  z: 5.91034299
- x: -5.71308078
  y: 13.71144591
  z: 0.40007939
- x: -5.91467725
  y: 12.89776522
  z: 2.62718238
- x: -3.03222976
  y: -1.79999629
  z: 8.50433192
- x: -3.21085316
  y: 2.11997188
  z: 8.71002527
- x: -3.71209236
  y: 6.06174158
  z: 8.34183848
- x: -5.16324911
  y: 11.6529258
  z: 5.37155488
- x: -3.34056505
  y: 9.91752203
  z: 7.56053006
- x: -3.73628217
  y: 16.5905664
  z: 0.3999584
- x: -3.45158551
  y: 15.76622462
  z: 3.67837322
- x: -2.76185013
  y: 13.00866685
  z: 6.43839714
- x: -1.0e-08
  y: -1.8
  z: 8.66869815
- x: -1.0e-08
  y: 2.14667381
  z: 8.97522434
- x: -1.0e-08
  y: 6.09991603
  z: 8.84761706
- x: -1.0e-08
  y: 9.96543874
  z: 8.00437736
- x: -1.0e-08
  y: 13.63052494
  z: 6.51654897
- x: -1.0e-08
  y: 16.73346681
  z: 4.10241064
- x: -1.0e-08
  y: 17.90374908
  z: 0.39997619
- x: 2.76185013
  y: 13.00866685
  z: 6.43839714
- x: 3.03222976
  y: -1.79999629
  z: 8.50433192
- x: 3.71209236
  y: 6.06174158
  z: 8.34183848
- x: 3.34056505
  y: 9.91752203
  z: 7.56053006
- x: 3.45158551
  y: 15.76622462
  z: 3.67837322
- x: 3.21085316
  y: 2.11997188
  z: 8.71002527
- x: 3.73628217
  y: 16.5905664
  z: 0.3999584
- x: 5.16324911
  y: 11.6529258
  z: 5.37155488
- x: 6.00996443
  y: -1.79999958
  z: 6.67266775
- x: 6.16505672
  y: 1.39784473
  z: 6.53131412
- x: 6.19950575
  y: 5.14650534
  z: 6.31004181
- x: 5.89906718
  y: 8.44673336
  z: 5.91034299
- x: 5.91467725
  y: 12.89776522
  z: 2.62718238
- x: 7.35349939
  y: -1.79999907
  z: 3.44426423
- x: 7.31378277
  y: -1.79988568
  z: 0.39999828
- x: 7.239463
  y: 1.5965166
  z: 3.25227094
- x: 7.14890952
  y: 2.23310916
  z: 0.39995294
- x: 7.06807114
  y: 5.49744394
  z: 3.03648049
- x: 6.96664673
  y: 5.76010809
  z: 0.39988187
- x: 6.58421581
  y: 9.77742185
  z: 0.39989891
- x: 6.80097742
  y: 8.9453581
  z: 2.83870363
- x: 5.71308078
  y: 13.71144591
  z: 0.40007939

```

### orca_core/hardware/sensing/models/touch-sensor-thumb/config.yaml

```yaml
name: touch-sensor-thumb
description: ORCA Fingertip - Thumb
frame: sensor
units: mm
num_taxels: 51
coordinates:
- x: -9.98783684
  y: -0.99999966
  z: 0.83664511
- x: -9.22014693
  y: -0.60386497
  z: 4.2141522
- x: -9.98563473
  y: 3.01522059
  z: 0.83825563
- x: -9.34725868
  y: 3.12493816
  z: 3.96201581
- x: -9.86319537
  y: 7.025051
  z: 0.83668072
- x: -9.13066251
  y: 6.90457409
  z: 4.21467613
- x: -8.90947253
  y: 10.91402385
  z: 0.83668825
- x: -7.08587129
  y: -0.36341653
  z: 6.95899868
- x: -6.93554584
  y: 2.94656029
  z: 7.10574445
- x: -7.07510324
  y: 6.26486515
  z: 6.97833064
- x: -8.34358177
  y: 10.63405643
  z: 3.83946027
- x: -6.78658109
  y: 9.61401604
  z: 6.5180933
- x: -7.01397155
  y: 14.44094726
  z: 0.83664566
- x: -6.67742466
  y: 13.86389925
  z: 3.48169799
- x: -3.4990712
  y: -0.12231963
  z: 8.65774898
- x: -3.66401984
  y: 3.40154211
  z: 8.6618383
- x: -3.71268789
  y: 6.92448678
  z: 8.61804962
- x: -5.73110824
  y: 12.7621635
  z: 5.78836754
- x: -3.55144846
  y: 10.41168292
  z: 8.07657784
- x: -3.93225521
  y: 16.92530102
  z: 0.83665819
- x: -3.38716757
  y: 15.99481755
  z: 4.32509838
- x: -2.89494885
  y: 14.00354271
  z: 6.63864407
- x: 0.00021972
  y: 0.01158422
  z: 8.79792926
- x: 0.00015816
  y: 3.55089765
  z: 8.83782324
- x: 9.735e-05
  y: 7.09004225
  z: 8.82407653
- x: 3.779e-05
  y: 10.59777145
  z: 8.38341654
- x: 0.0
  y: 14.30397222
  z: 6.83198881
- x: 0.0
  y: 16.63586847
  z: 4.20815607
- x: 0.0
  y: 17.61962965
  z: 0.83666099
- x: 2.89494885
  y: 14.00354271
  z: 6.63864407
- x: 3.4990712
  y: -0.12231963
  z: 8.65774898
- x: 3.71268789
  y: 6.92448678
  z: 8.61804962
- x: 3.55144846
  y: 10.41168292
  z: 8.07657784
- x: 3.38716757
  y: 15.99481755
  z: 4.32509838
- x: 3.66401984
  y: 3.40154211
  z: 8.6618383
- x: 3.93225521
  y: 16.92530102
  z: 0.83665819
- x: 5.73110824
  y: 12.7621635
  z: 5.78836754
- x: 7.08587129
  y: -0.36341653
  z: 6.95899868
- x: 6.93554584
  y: 2.94656029
  z: 7.10574445
- x: 7.07510324
  y: 6.26486515
  z: 6.97833064
- x: 6.78658109
  y: 9.61401604
  z: 6.5180933
- x: 6.67742466
  y: 13.86389925
  z: 3.48169799
- x: 9.22014693
  y: -0.60386497
  z: 4.2141522
- x: 9.98783684
  y: -0.99999966
  z: 0.83664511
- x: 9.34725868
  y: 3.12493816
  z: 3.96201581
- x: 9.98563473
  y: 3.01522059
  z: 0.83825563
- x: 9.13066251
  y: 6.90457409
  z: 4.21467613
- x: 9.86319537
  y: 7.025051
  z: 0.83668072
- x: 8.90947253
  y: 10.91402385
  z: 0.83668825
- x: 8.34358177
  y: 10.63405643
  z: 3.83946027
- x: 7.01397155
  y: 14.44094726
  z: 0.83664566

```

### orca_core/models/v1/orcahand-left/config.yaml

```yaml
motor_type: dynamixel
baudrate: 3000000
port: auto
max_current: 400

type: left

# current, velocity, position, multi-turn- position, current_based_position
control_mode: current_based_position

motor_ids: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
joint_ids: [thumb_mcp, thumb_abd, thumb_pip, thumb_dip, index_abd, index_mcp, index_pip, middle_abd, middle_mcp, middle_pip, ring_abd, ring_mcp, ring_pip, pinky_abd, pinky_mcp, pinky_pip, wrist]

# Which motor ID is physically connected to which joint
joint_to_motor_map:
  thumb_mcp: -4
  thumb_abd: -3
  thumb_pip: -1
  thumb_dip: -2
  index_abd: 14
  index_mcp: -15
  index_pip: -16
  middle_abd: 13
  middle_mcp: -8
  middle_pip: -9
  ring_abd: -5
  ring_mcp: -7
  ring_pip: -6
  pinky_abd: 12
  pinky_mcp: -10
  pinky_pip: -11
  wrist: -17

joint_roms:
  thumb_mcp: [-50, 50]
  thumb_abd: [-20, 42]
  thumb_pip: [-12, 108]
  thumb_dip: [-20, 112]
  index_abd: [-37, 37]
  index_mcp: [-20, 95]
  index_pip: [-20, 108]
  middle_abd: [-37, 37]
  middle_mcp: [-20, 91]
  middle_pip: [-20, 107]
  ring_abd: [-37, 37]
  ring_mcp: [-20, 91]
  ring_pip: [-20, 107]
  pinky_abd: [-37, 37]
  pinky_mcp: [-20, 98]
  pinky_pip: [-20, 108]
  wrist: [-50, 30]

neutral_position:
  thumb_mcp: -13
  thumb_abd: 42
  thumb_pip: 33
  thumb_dip: 19
  index_abd: 25
  index_mcp: 0
  index_pip: 0
  middle_abd: -2
  middle_mcp: 0
  middle_pip: 0
  ring_abd: -20
  ring_mcp: -1
  ring_pip: 0
  pinky_abd: -37
  pinky_mcp: 1
  pinky_pip: 0
  wrist: 0

calibration_current: 350
calibration_step_size: 0.1
calibration_step_period: 0.001
calibration_num_stable: 10  # should be period * num_stable > 1
calibration_threshold: 0.01

calibration_sequence:
  - step: 1
    joints:
      thumb_mcp: flex
  - step: 2
    joints:
      thumb_mcp: extend
  - step: 3
    joints:
      thumb_abd: flex
  - step: 4
    joints:
      thumb_abd: extend
  - step: 5
    joints:
      thumb_pip: flex
  - step: 6
    joints:
      thumb_pip: extend
  - step: 7
    joints:
      thumb_dip: flex
  - step: 8
    joints:
      thumb_dip: extend
  - step: 9
    joints:
      index_abd: flex
      middle_abd: flex
      ring_abd: flex
      pinky_abd: flex
  - step: 10
    joints:
      index_abd: extend
      middle_abd: extend
      ring_abd: extend
      pinky_abd: extend
  - step: 11
    joints:
      index_mcp: flex
  - step: 12
    joints:
      index_mcp: extend
  - step: 13
    joints:
      index_pip: flex
  - step: 14
    joints:
      index_pip: extend
  - step: 15
    joints:
      middle_mcp: flex
  - step: 16
    joints:
      middle_mcp: extend
  - step: 17
    joints:
      middle_pip: flex
  - step: 18
    joints:
      middle_pip: extend
  - step: 19
    joints:
      ring_mcp: flex
  - step: 20
    joints:
      ring_mcp: extend
  - step: 21
    joints:
      ring_pip: flex
  - step: 22
    joints:
      ring_pip: extend
  - step: 23
    joints:
      pinky_mcp: flex
  - step: 24
    joints:
      pinky_mcp: extend
  - step: 25
    joints:
      pinky_pip: flex
  - step: 26
    joints:
      pinky_pip: extend
  - step: 27
    joints:
      wrist: flex
  - step: 28
    joints:
      wrist: extend

```

### orca_core/models/v1/orcahand-right/config.yaml

```yaml
motor_type: dynamixel
baudrate: 3000000
port: auto
max_current: 400

type: right

# current, velocity, position, multi-turn- position, current_based_position
control_mode: current_based_position

motor_ids: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
joint_ids: [thumb_mcp, thumb_abd, thumb_pip, thumb_dip, index_abd, index_mcp, index_pip, middle_abd, middle_mcp, middle_pip, ring_abd, ring_mcp, ring_pip, pinky_abd, pinky_mcp, pinky_pip, wrist]

# Which motor ID is physically connected to which joint
joint_to_motor_map:
  thumb_mcp: -4
  thumb_abd: -3
  thumb_pip: -1
  thumb_dip: -2
  index_abd: 14
  index_mcp: -15
  index_pip: -16
  middle_abd: 13
  middle_mcp: -8
  middle_pip: -9
  ring_abd: -5
  ring_mcp: -7
  ring_pip: -6
  pinky_abd: 12
  pinky_mcp: -10
  pinky_pip: -11
  wrist: -17

joint_roms:
  thumb_mcp: [-50, 50]
  thumb_abd: [-20, 42]
  thumb_pip: [-12, 108]
  thumb_dip: [-20, 112]
  index_abd: [-37, 37]
  index_mcp: [-20, 95]
  index_pip: [-20, 108]
  middle_abd: [-37, 37]
  middle_mcp: [-20, 91]
  middle_pip: [-20, 107]
  ring_abd: [-37, 37]
  ring_mcp: [-20, 91]
  ring_pip: [-20, 107]
  pinky_abd: [-37, 37]
  pinky_mcp: [-20, 98]
  pinky_pip: [-20, 108]
  wrist: [-50, 30]

neutral_position:
  thumb_mcp: -13
  thumb_abd: 42
  thumb_pip: 33
  thumb_dip: 19
  index_abd: 25
  index_mcp: 0
  index_pip: 0
  middle_abd: -2
  middle_mcp: 0
  middle_pip: 0
  ring_abd: -20
  ring_mcp: -1
  ring_pip: 0
  pinky_abd: -37
  pinky_mcp: 1
  pinky_pip: 0
  wrist: 0

calibration_current: 350
calibration_step_size: 0.1
calibration_step_period: 0.001
calibration_num_stable: 10  # should be period * num_stable > 1
calibration_threshold: 0.01

calibration_sequence:
  - step: 1
    joints:
      thumb_mcp: flex
  - step: 2
    joints:
      thumb_mcp: extend
  - step: 3
    joints:
      thumb_abd: flex
  - step: 4
    joints:
      thumb_abd: extend
  - step: 5
    joints:
      thumb_pip: flex
  - step: 6
    joints:
      thumb_pip: extend
  - step: 7
    joints:
      thumb_dip: flex
  - step: 8
    joints:
      thumb_dip: extend
  - step: 9
    joints:
      index_abd: flex
      middle_abd: flex
      ring_abd: flex
      pinky_abd: flex
  - step: 10
    joints:
      index_abd: extend
      middle_abd: extend
      ring_abd: extend
      pinky_abd: extend
  - step: 11
    joints:
      index_mcp: flex
  - step: 12
    joints:
      index_mcp: extend
  - step: 13
    joints:
      index_pip: flex
  - step: 14
    joints:
      index_pip: extend
  - step: 15
    joints:
      middle_mcp: flex
  - step: 16
    joints:
      middle_mcp: extend
  - step: 17
    joints:
      middle_pip: flex
  - step: 18
    joints:
      middle_pip: extend
  - step: 19
    joints:
      ring_mcp: flex
  - step: 20
    joints:
      ring_mcp: extend
  - step: 21
    joints:
      ring_pip: flex
  - step: 22
    joints:
      ring_pip: extend
  - step: 23
    joints:
      pinky_mcp: flex
  - step: 24
    joints:
      pinky_mcp: extend
  - step: 25
    joints:
      pinky_pip: flex
  - step: 26
    joints:
      pinky_pip: extend
  - step: 27
    joints:
      wrist: flex
  - step: 28
    joints:
      wrist: extend

```

### orca_core/models/v2/orcahand-full-left/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: left
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: -10
  thumb_abd: -13
  thumb_mcp: 12
  thumb_dip: 11
  index_abd: -7
  index_mcp: -8
  index_pip: -9
  middle_abd: -6
  middle_mcp: -17
  middle_pip: -2
  ring_abd: -5
  ring_mcp: 4
  ring_pip: -3
  pinky_abd: 14
  pinky_mcp: -15
  pinky_pip: 16
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
use_joint_feedback: true
joint_encoder_joints:
- all
encoder_serial_port: auto
encoder_baudrate: 2000000
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend
sensors:
  port: auto
  # baudrate auto-detected from the connected sensor; set an explicit int
  # only to force a specific rate.
  finger_to_sensor_id:
    thumb: 0
    index: 1
    middle: 2
    ring: 3
    pinky: 4

```

### orca_core/models/v2/orcahand-full-right/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: right
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: 17
  thumb_abd: 14
  thumb_mcp: 15
  thumb_dip: 16
  index_abd: 4
  index_mcp: 3
  index_pip: 2
  middle_abd: 5
  middle_mcp: 10
  middle_pip: 9
  ring_abd: 6
  ring_mcp: -7
  ring_pip: 8
  pinky_abd: -13
  pinky_mcp: 12
  pinky_pip: -11
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
use_joint_feedback: true
joint_encoder_joints:
- all
encoder_serial_port: auto
encoder_baudrate: 2000000
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend
sensors:
  port: auto
  finger_to_sensor_id:
    thumb: 0
    index: 1
    middle: 2
    ring: 3
    pinky: 4

```

### orca_core/models/v2/orcahand-joint-left/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: left
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: -10
  thumb_abd: -13
  thumb_mcp: 12
  thumb_dip: 11
  index_abd: -7
  index_mcp: -8
  index_pip: -9
  middle_abd: -6
  middle_mcp: -17
  middle_pip: -2
  ring_abd: -5
  ring_mcp: 4
  ring_pip: -3
  pinky_abd: 14
  pinky_mcp: -15
  pinky_pip: 16
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
use_joint_feedback: true
joint_encoder_joints:
- all
encoder_serial_port: auto
encoder_baudrate: 2000000
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend

```

### orca_core/models/v2/orcahand-joint-right/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: right
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: 17
  thumb_abd: 14
  thumb_mcp: 15
  thumb_dip: 16
  index_abd: 4
  index_mcp: 3
  index_pip: 2
  middle_abd: 5
  middle_mcp: 10
  middle_pip: 9
  ring_abd: 6
  ring_mcp: -7
  ring_pip: 8
  pinky_abd: -13
  pinky_mcp: 12
  pinky_pip: -11
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
use_joint_feedback: true
joint_encoder_joints:
- all
encoder_serial_port: auto
encoder_baudrate: 2000000
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend

```

### orca_core/models/v2/orcahand-left/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: left
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: -10
  thumb_abd: -13
  thumb_mcp: 12
  thumb_dip: 11
  index_abd: -7
  index_mcp: -8
  index_pip: -9
  middle_abd: -6
  middle_mcp: -17
  middle_pip: -2
  ring_abd: -5
  ring_mcp: 4
  ring_pip: -3
  pinky_abd: 14
  pinky_mcp: -15
  pinky_pip: 16
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend

```

### orca_core/models/v2/orcahand-right/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: right
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: 17
  thumb_abd: 14
  thumb_mcp: 15
  thumb_dip: 16
  index_abd: 4
  index_mcp: 3
  index_pip: 2
  middle_abd: 5
  middle_mcp: 10
  middle_pip: 9
  ring_abd: 6
  ring_mcp: -7
  ring_pip: 8
  pinky_abd: -13
  pinky_mcp: 12
  pinky_pip: -11
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend

```

### orca_core/models/v2/orcahand-touch-left/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: left
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: -10
  thumb_abd: -13
  thumb_mcp: 12
  thumb_dip: 11
  index_abd: -7
  index_mcp: -8
  index_pip: -9
  middle_abd: -6
  middle_mcp: -17
  middle_pip: -2
  ring_abd: -5
  ring_mcp: 4
  ring_pip: -3
  pinky_abd: 14
  pinky_mcp: -15
  pinky_pip: 16
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend
sensors:
  port: auto
  # baudrate auto-detected from the connected sensor; set an explicit int
  # only to force a specific rate.
  finger_to_sensor_id:
    thumb: 0
    index: 1
    middle: 2
    ring: 3
    pinky: 4

```

### orca_core/models/v2/orcahand-touch-right/config.yaml

```yaml
motor_type: dynamixel
port: auto
baudrate: 1000000
max_current: 300
type: right
control_mode: current_based_position
motor_ids:
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
joint_ids:
- wrist
- thumb_cmc
- thumb_abd
- thumb_mcp
- thumb_dip
- index_abd
- index_mcp
- index_pip
- middle_abd
- middle_mcp
- middle_pip
- ring_abd
- ring_mcp
- ring_pip
- pinky_abd
- pinky_mcp
- pinky_pip
joint_to_motor_map:
  thumb_cmc: 17
  thumb_abd: 14
  thumb_mcp: 15
  thumb_dip: 16
  index_abd: 4
  index_mcp: 3
  index_pip: 2
  middle_abd: 5
  middle_mcp: 10
  middle_pip: 9
  ring_abd: 6
  ring_mcp: -7
  ring_pip: 8
  pinky_abd: -13
  pinky_mcp: 12
  pinky_pip: -11
  wrist: -1
joint_roms:
  wrist:
  - -65
  - 35
  thumb_cmc:
  - -45
  - 33
  thumb_abd:
  - -18
  - 55
  thumb_mcp:
  - -25
  - 100
  thumb_dip:
  - -15
  - 107
  index_abd:
  - -25
  - 30
  index_mcp:
  - -25
  - 100
  index_pip:
  - -15
  - 107
  middle_abd:
  - -27
  - 27
  middle_mcp:
  - -25
  - 100
  middle_pip:
  - -15
  - 107
  ring_abd:
  - -27
  - 27
  ring_mcp:
  - -25
  - 100
  ring_pip:
  - -15
  - 107
  pinky_abd:
  - -30
  - 30
  pinky_mcp:
  - -25
  - 100
  pinky_pip:
  - -15
  - 107
neutral_position:
  thumb_cmc: 0
  thumb_abd: 50
  thumb_mcp: 33
  thumb_dip: 18
  index_abd: -14
  index_mcp: 2
  index_pip: 6
  middle_abd: -4
  middle_mcp: 2
  middle_pip: 4
  ring_abd: 10
  ring_mcp: -2
  ring_pip: 8
  pinky_abd: 22
  pinky_mcp: -4
  pinky_pip: -2
  wrist: -20
calibration_current: 300
calibration_step_size: 0.15
calibration_step_period: 0.0001
calibration_num_stable: 10
calibration_threshold: 0.01
calibration_sequence:
- step: 1
  joints:
    thumb_cmc: flex
- step: 2
  joints:
    thumb_cmc: extend
- step: 3
  joints:
    thumb_abd: flex
- step: 4
  joints:
    thumb_abd: extend
- step: 5
  joints:
    thumb_mcp: flex
- step: 6
  joints:
    thumb_mcp: extend
- step: 7
  joints:
    thumb_dip: flex
- step: 8
  joints:
    thumb_dip: extend
- step: 9
  joints:
    index_abd: flex
    middle_abd: flex
    ring_abd: flex
    pinky_abd: flex
- step: 10
  joints:
    index_abd: extend
    middle_abd: extend
    ring_abd: extend
    pinky_abd: extend
- step: 11
  joints:
    index_mcp: flex
    middle_mcp: flex
    ring_mcp: flex
    pinky_mcp: flex
- step: 12
  joints:
    index_mcp: extend
    middle_mcp: extend
    ring_mcp: extend
    pinky_mcp: extend
- step: 13
  joints:
    index_pip: flex
    middle_pip: flex
    ring_pip: flex
    pinky_pip: flex
- step: 14
  joints:
    index_pip: extend
    middle_pip: extend
    ring_pip: extend
    pinky_pip: extend
- step: 15
  joints:
    wrist: flex
- step: 16
  joints:
    wrist: extend
sensors:
  port: auto
  # baudrate auto-detected from the connected sensor; set an explicit int
  # only to force a specific rate.
  # Fixed production wiring: connector N carries finger N (slot = connector - 1).
  finger_to_sensor_id:
    thumb: 0
    index: 1
    middle: 2
    ring: 3
    pinky: 4

```

## Python signatures and reward/observation bodies (21 files)


### orca_core/base_hand.py

```
class BaseHand(ABC)
    """Abstract base class defining the shared joint-space interface for all ORCA hand backends.

Concrete subclasses implement :meth:`_get_joint_positions` and
:meth:`_set_joint_positions`.
All higher-level motion helpers (interpolation, normalisation, neutral
position) live here so they are available reg"""
    def __init__(self, config_path, config, model_version, model_name)
    def _get_joint_positions(self)
    def _set_joint_positions(self, joint_pos)
    def _coerce_joint_positions(self, joint_pos)
    def pose_from_fractions(self, fractions)
    def set_joint_positions(self, joint_pos, num_steps, step_size)
    def get_joint_position(self)
    def _linear_waypoints_to(self, target, num_steps)
    def register_position(self, name, joint_pos)
    def remove_position(self, name)
    def set_named_position(self, name, num_steps, step_size)
    def play_named_positions(self, names, cycles, num_steps, step_size, return_to_neutral, neutral_num_steps, neutral_step_size)
    def set_neutral_position(self, num_steps, step_size)
    def set_zero_position(self, num_steps, step_size)
```

### orca_core/hand_config.py

```
class HandConfigValidationError(ValueError)
    """Raised when a hand configuration is structurally invalid."""
def _resolve_model_name_from_type(hand_type)
def _resolve_config_path(config_path, model_version, model_name)
def _resolve_calibration_path(config_path, calibration_path)
def canonical_joint_ids(version, type)
def _canonical_joint_to_motor_map(raw_joint_to_motor_map)
class BaseHandConfig()
    """Base joint-space configuration for a hand model."""
    def model_path(self)
    def from_config_path(cls, config_path, model_version, model_name)
    def validate(self)
    def clamp_joint_positions(self, joint_pos)
    def _clamp_joint_value(self, joint_name, joint_pos)
class OrcaHandConfig(BaseHandConfig)
    """ORCA hand configuration layered on top of the shared base spec."""
    def motor_id_to_idx_dict(self)
    def motor_to_joint_dict(self)
    def has_joint_encoders(self)
    def joint_feedback_enabled(self)
    def from_config_path(cls, config_path, calibration_path, model_version, model_name)
    def validate_config(self)
    def __post_init__(self)
class OrcaHandTouchConfig(OrcaHandConfig)
    """ORCA hand configuration with tactile sensor support."""
    def from_config_path(cls, config_path, calibration_path, model_version, model_name)
    def validate_config(self)
```

### orca_core/hand_factory.py

```
"""Factory that selects the right hand class — and, by default, the right model.

A hand's capabilities are declared in ``config.yaml``: ``joint_encoder_joints``
plus ``use_joint_feedback`` decide whether the closed-loop joint-feedback
controller engages, and a ``sensors`` block declares tactile sensing.
:func:`load_hand` reads those once and returns the matching concrete class so
callers (and scripts) don't have to hand-pick hand classes.

| feedback | tactile | class                    |
|----------|---------|--------------------------|
| yes       | no      | ``OrcaHandJointFeedback``|
| yes  """
class HandDetection()
    """What :func:`detect_hand` found plugged in.

``model_name`` is the bundled v2 model matching the detected side and
sensing capabilities; the port fields carry what was discovered so the
hand can connect without re-probing. ``identity`` is ``None`` for hands
whose board doesn't report one."""
def detect_hand()
def _pin_detected_ports(config, detection)
def load_hand(config_path, calibration_path, model_version, model_name, mock, engage_feedback)
```

### orca_core/hardware/feetech/port_handler.py

```
class PortHandler(object)
    def __init__(self, port_name)
    def openPort(self)
    def closePort(self)
    def clearPort(self)
    def setPortName(self, port_name)
    def getPortName(self)
    def setBaudRate(self, baudrate)
    def getBaudRate(self)
    def getBytesAvailable(self)
    def readPort(self, length)
    def writePort(self, packet)
    def setPacketTimeout(self, packet_length)
    def setPacketTimeoutMillis(self, msec)
    def isPacketTimeout(self)
    def getCurrentTime(self)
    def getTimeSinceStart(self)
    def setupPort(self, cflag_baud)
    def getCFlagBaud(self, baudrate)
```

### orca_core/hardware/feetech/protocol_packet_handler.py

```
class protocol_packet_handler(object)
    def __init__(self, portHandler, protocol_end)
    def scs_getend(self)
    def scs_setend(self, e)
    def scs_tohost(self, a, b)
    def scs_toscs(self, a, b)
    def scs_makeword(self, a, b)
    def scs_makedword(self, a, b)
    def scs_loword(self, l)
    def scs_hiword(self, h)
    def scs_lobyte(self, w)
    def scs_hibyte(self, w)
    def getProtocolVersion(self)
    def getTxRxResult(self, result)
    def getRxPacketError(self, error)
    def txPacket(self, txpacket)
    def rxPacket(self)
    def txRxPacket(self, txpacket)
    def ping(self, scs_id)
    def action(self, scs_id)
    def readTx(self, scs_id, address, length)
    def readRx(self, scs_id, length)
    def readTxRx(self, scs_id, address, length)
    def read1ByteTx(self, scs_id, address)
    def read1ByteRx(self, scs_id)
    def read1ByteTxRx(self, scs_id, address)
    def read2ByteTx(self, scs_id, address)
    def read2ByteRx(self, scs_id)
    def read2ByteTxRx(self, scs_id, address)
    def read4ByteTx(self, scs_id, address)
    def read4ByteRx(self, scs_id)
    def read4ByteTxRx(self, scs_id, address)
    def writeTxOnly(self, scs_id, address, length, data)
    def writeTxRx(self, scs_id, address, length, data)
    def write1ByteTxOnly(self, scs_id, address, data)
    def write1ByteTxRx(self, scs_id, address, data)
    def write2ByteTxOnly(self, scs_id, address, data)
    def write2ByteTxRx(self, scs_id, address, data)
    def write4ByteTxOnly(self, scs_id, address, data)
    def write4ByteTxRx(self, scs_id, address, data)
    def regWriteTxOnly(self, scs_id, address, length, data)
    def regWriteTxRx(self, scs_id, address, length, data)
    def syncReadTx(self, start_address, data_length, param, param_length)
    def syncReadRx(self, data_length, param_length)
    def syncWriteTxOnly(self, start_address, data_length, param, param_length)
    def reOfsCal(self, scs_id, position)
    def reSet(self, scs_id)
```

### orca_core/hardware/hand_serial_link.py

```
"""Serial-link transport with a background frame demultiplexer.

Carries two kinds of frames on one port: synchronous responses to host
requests, and asynchronous broadcasts the device emits on its own clock.
Both are AA-XX framed; the second byte tags the type so a single demuxer
thread can route responses to ``send_register_request`` and broadcasts to
registered handlers. Frame shape and checksum are validated; payload
meaning is left to the handler."""
class LinkStats()
    """Diagnostic counters for the demuxer.

Frame counters are indexed by the second byte (XX) of AA-XX frames:
- 'AA' is the fixed header byte (0xAA)
- 'XX' identifies frame types and is used as the counter key"""
    def snapshot(self)
class HandSerialLink()
    """Serial-port owner and demultiplexer for AA-XX framed traffic.

Frame layout: ``AA`` header, ``XX`` type byte, payload, LRC checksum
on the last byte.

Lifecycle: ``connect()`` opens the port and starts the demuxer thread;
``disconnect()`` stops it and closes the port. Handlers may be
registered at a"""
    def __init__(self, port, baudrate, exclusive)
    def is_connected(self)
    def is_port_dead(self)
    def port_error(self)
    def connect(self)
    def disconnect(self)
    def register_frame_handler(self, second_byte, handler)
    def unregister_frame_handler(self, second_byte)
    def send_register_request(self, request_bytes, response_timeout_s)
    def _drain_response_queue(self)
    def get_link_stats(self)
    def _open_serial(self)
    def _close_serial(self)
    def _serial_write(self, data)
    def _serial_read(self, n)
    def _mark_port_dead(self, error)
    def _demux_loop(self)
    def _read_exact(self, n)
    def _handle_response_frame(self)
    def _handle_auto_frame(self, second_byte)
    def _enqueue_response(self, frame)
    def _log_handler_error(self, second_byte)
```

### orca_core/hardware/mock_hand_serial_link.py

```
"""In-memory test seam for ``HandSerialLink``.

Subclasses the real link and overrides only the four serial I/O methods;
the demuxer, dispatcher, and transaction lock are unchanged production
code, exercised through this mock so there is no parallel link
implementation to drift."""
class MockHandSerialLink(HandSerialLink)
    def __init__(self, port, baudrate)
    def feed_bytes(self, data)
    def simulate_port_death(self, error)
    def set_response_provider(self, provider)
    def response_provider(self)
    def serial_writes(self)
    def last_serial_write(self)
    def wait_for_write(self, count, timeout)
    def _open_serial(self)
    def _close_serial(self)
    def _serial_write(self, data)
    def _serial_read(self, n)
```

### orca_core/hardware_hand.py

```
class OrcaHand(BaseHand)
    """ORCA hand class.

Extends :class:`~orca_core.BaseHand` with a full lifecycle for a physical
hand: connection management, torque control, multi-mode motor control,
(automatic) calibration, and background task execution.

The recommended usage pattern is:

>>> from orca_core import OrcaHand, OrcaJoint"""
    def __init__(self, config_path, calibration_path, model_version, model_name, config)
    def __del__(self)
    def calibration(self)
    def calibration(self, value)
    def motor_limits_dict(self)
    def joint_to_motor_ratios_dict(self)
    def calibrated(self)
    def wrist_calibrated(self)
    def motor_client(self)
    def _create_motor_client(self)
    def _trial_probe(self, port)
    def _resolve_motor_driver(self, port)
    def _persist_resolved_driver(self, existing)
    def _connect_on_port(self, port, base_config)
    def _try_port(self, port, base_config)
    def _discard_motor_client(self)
    def connect(self, interactive, engage_feedback)
    def disconnect(self)
    def is_connected(self)
    def enable_torque(self, motor_ids)
    def disable_torque(self, motor_ids)
    def set_max_current(self, current)
    def set_control_mode(self, mode, motor_ids)
    def get_motor_pos(self, as_dict)
    def get_motor_current(self, as_dict)
    def wait_for_motion(self, timeout)
    def get_motor_temp(self, as_dict)
    def _get_joint_positions(self)
    def _set_joint_positions(self, joint_pos)
    def write_motor_pos(self, motor_ids, positions)
    def init_joints(self, force_calibrate, move_to_neutral)
    def is_calibrated(self, verbose, use_joint_feedback)
    def encoder_backed_joints(self)
    def _encoder_backed_joints(self)
    def _raw_to_joint_angle(self, raw_counts)
    def calibrate(self, blocking, force_wrist, joints, joint_encoder_client, progress_callback, persist)
    def _calibrate_and_apply(self)
    def set_neutral_position(self, num_steps, step_size)
    def _read_motor_pos_for_offsets(self, retries, retry_interval)
    def _compute_wrap_offsets_dict(self)
    def _clear_wrap_offset(self, motor_id)
    def _set_motor_pos(self, desired_pos, rel_to_current)
    def _warn_uncalibrated(self, motor_id, joint_name, missing)
    def _motor_to_joint_pos(self, motor_pos)
    def _joint_to_motor_pos(self, joint_pos)
    def _sanity_check(self)
    def tension(self, move_motors, blocking, progress_callback)
    def jitter(self, motor_ids, amplitude, frequency, duration, include_wrist, blocking)
    def _jitter(self, motor_ids, amplitude, frequency, duration, include_wrist)
    def _tension(self, move_motors, progress_callback)
    def _run_task(self, task_fn)
    def _start_task(self, task_fn)
    def task_running(self)
    def stop_task(self, timeout)
class MockMotorResolutionMixin()
    """Swaps the motor bus for an in-memory mock on ``Mock*`` hand classes.

Supplies the mock motor client and skips connect-time port/driver
resolution and yaml persistence: mock motors don't sit on a real bus, so
there is nothing to detect or probe (``port: auto`` must not handshake
real USB devices) an"""
    def __init__(self)
    def _install_mock_calibration(self)
    def connect(self, interactive)
    def _create_motor_client(self)
    def _resolve_motor_driver(self, port)
    def _persist_resolved_driver(self, existing)
class MockOrcaHand(MockMotorResolutionMixin, OrcaHand)
    """Drop-in :class:`OrcaHand` backed by an in-memory mock motor client,
for testing and prototyping.

All methods behave identically to :class:`OrcaHand` but no serial
port is opened and motor state is simulated in memory."""
```

### orca_core/hardware_hand_sensing.py

```
"""Sensing-equipped variants of :class:`~orca_core.OrcaHand`.

One class per sensing capability, plus their combination:

- :class:`OrcaHandTouch` — tactile fingertip sensing.
- :class:`OrcaHandJointFeedback` — closed-loop joint control from the
  joint-angle encoders.
- :class:`OrcaHandFull` — both, sharing one serial link when the two
  streams arrive on the same port.

Every variant follows the same shape so combiners (and future capabilities)
can be written by symmetry: construction seams for its link/client
(overridden by the ``Mock*`` classes at the bottom), an
attach-onto-open-link / open-"""
def _link_health(link)
class OrcaHandTouch(OrcaHand)
    """ORCA hand with integrated tactile sensing.

``connect()`` opens both the motor bus and the sensor serial link;
``disconnect()`` tears down both."""
    def __init__(self, config_path, calibration_path, model_version, model_name, config)
    def _create_tactile_link(self, port, baudrate)
    def _create_tactile_client(self, link)
    def _attach_tactile_client(self, link)
    def _open_tactile_on_port(self, port, baudrate)
    def _teardown_tactile(self)
    def _connect_sensor_with_fallback(self)
    def connect(self, interactive, engage_feedback)
    def connect_sensors_only(self)
    def disconnect(self)
    def _require_tactile_client(self)
    def get_tactile_forces(self)
    def get_tactile_taxels(self)
    def get_tactile_data(self)
    def start_tactile_stream(self, resultant, taxels, min_sensors)
    def stop_tactile_stream(self)
    def zero_tactile_sensors(self, num_samples, timeout_s)
    def clear_tactile_zero(self)
    def get_tactile_configuration(self)
    def get_tactile_stats(self)
    def get_tactile_link_health(self)
    def get_taxel_geometry(self)
    def kinematics(self)
    def set_base_pose(self, pose)
    def get_base_pose(self)
    def _resolve_joint_pos(self, joint_pos)
    def get_sensor_transforms(self, frame, joint_pos)
    def get_taxel_data(self, frame, joint_pos)
class OrcaHandJointFeedback(OrcaHand)
    """ORCA hand with closed-loop joint feedback on the encoder-backed joints.

``connect()`` opens the motor bus, the encoder serial link, and starts a
:class:`~orca_core.control.JointLoopThread` running a vectorised PI on
joint-encoder error. The motors stay in ``current_based_position``: the
host writes"""
    def __init__(self, config_path, calibration_path, model_version, model_name, config)
    def _create_encoder_link(self, port)
    def _create_encoder_client(self, link)
    def _attach_encoders(self, link)
    def _encoder_motor_ids(self)
    def _require_validated_feedback_side(self)
    def _loop_ready_joints(self)
    def loop_joint_names(self)
    def loop_skipped_joints(self)
    def connect(self, interactive, engage_feedback)
    def disconnect(self)
    def _teardown_joint_feedback(self)
    def _loop_writes_paused(self)
    def disable_torque(self, motor_ids)
    def enable_torque(self, motor_ids)
    def set_control_mode(self, mode, motor_ids)
    def _refuse_routine_while_loop_runs(self, routine)
    def calibrate(self)
    def tension(self)
    def jitter(self)
    def init_joints(self, force_calibrate, move_to_neutral)
    def _loop_engaged(self)
    def _set_joint_positions(self, joint_pos)
    def _get_joint_positions(self)
    def set_pid_gains(self, Kp, Ki, correction_max_deg, i_clamp_deg)
    def rebase_loop(self)
    def _require_live_loop(self)
    def get_measured_joints(self)
    def get_loop_correction(self)
    def get_encoder_link_health(self)
    def get_loop_stats(self)
class OrcaHandFull(OrcaHandTouch, OrcaHandJointFeedback)
    """ORCA hand with both tactile sensing and closed-loop joint feedback.

Combines :class:`OrcaHandTouch` and :class:`OrcaHandJointFeedback` without
duplicating either: each capability is inherited, and this class only owns
the ``connect``/``disconnect`` orchestration that decides how the two
sensing str"""
    def connect(self, interactive, engage_feedback)
    def _connect_without_feedback(self, interactive)
    def get_tactile_link_health(self)
    def disconnect(self)
class _MockEncoderFramePump()
    """Daemon thread feeding a fixed AA A9 frame to a mock link so the
encoder stream starts and its freshness watchdog stays satisfied."""
    def __init__(self, link, frame)
    def _run(self)
    def stop(self)
class MockOrcaHandTouch(MockMotorResolutionMixin, OrcaHandTouch)
    """Drop-in :class:`OrcaHandTouch` with in-memory mock motor + sensor
clients: no serial I/O, no port discovery, and register reads served
from an in-memory sensor state (all fingers connected)."""
    def __init__(self)
    def _create_tactile_link(self, port, baudrate)
    def _attach_tactile_client(self, link)
    def _connect_sensor_with_fallback(self)
    def tactile_mock_link(self)
class MockOrcaHandJointFeedback(MockMotorResolutionMixin, OrcaHandJointFeedback)
    """Drop-in :class:`OrcaHandJointFeedback` with in-memory mock motor +
encoder-link clients: no serial I/O and no port discovery. The encoder
client itself is real so the demuxer + AA A9 handler path is exercised;
a built-in pump keeps the mock link fed with encoder frames (override
:meth:`_mock_encoder"""
    def __init__(self)
    def _install_mock_calibration(self)
    def _mock_encoder_frame(self)
    def _create_encoder_link(self, port)
    def _teardown_joint_feedback(self)
class MockOrcaHandFull(MockOrcaHandTouch, MockOrcaHandJointFeedback, OrcaHandFull)
    """Drop-in :class:`OrcaHandFull` with in-memory mock motor + link clients.

The mock bases supply the in-memory motor client and mock serial links;
:class:`OrcaHandFull` supplies the shared-link connect/disconnect logic."""
    def tactile_mock_link(self)
```

### orca_core/kinematics/hand_kinematics.py

```
"""Forward kinematics for the ORCA hand from packaged URDF-derived constants.

Loads per-hand kinematic chains and tactile sensor mount poses from
``data/v*_kinematics.yaml`` (see that file's header for provenance) and
computes fingertip / sensor poses in the palm or base frame from orca_core
joint angles (degrees, orca_core joint ids and sign conventions)."""
class _ChainEntry()
    """One precompiled chain element: constant origin plus optional joint axis."""
    def __init__(self, entry)
    def transform(self, joint_pos_deg)
def _joint_transform(entry, joint_pos_deg)
class HandKinematics()
    """FK and sensor mounts for one hand (type + model version)."""
    def __init__(self, chains, sensor_mounts, hand_type)
    def load(cls, hand_type, version)
    def sensor_mounts(self)
    def fingertip_poses(self, joint_pos_deg, in_frame, fingers)
    def sensor_poses(self, joint_pos_deg, in_frame, fingers)
```

### scripts/configure_motor_chain.py

```
"""Configure the motor chain of a fresh ORCA hand: assign each motor its ID and baud rate.

Plug the motors in one at a time when prompted. Re-running resumes from wherever
the previous run stopped.

Usage:
    uv run python scripts/configure_motor_chain.py [CONFIG]
    uv run python scripts/configure_motor_chain.py CONFIG --reset
    uv run python scripts/configure_motor_chain.py CONFIG --baudrate 1000000"""
def motor_color(model_name)
def _print_motor_row(motor)
def _banner(title)
def play_success_beep()
def on_progress(event)
def on_prompt(prompt)
def _load_config(config_path_arg)
def _resolve_port(configured_port, motor_type)
def _resolve_motor_type(explicit, port)
def _loop_until_interrupt(label, once)
def main()
```

### tests/_hand_feedback_helpers.py

```
"""Fixtures for ``OrcaHandJointFeedback`` lifecycle tests.

The hand under test owns a real ``JointEncoderClient`` on a
``MockHandSerialLink``; the mock hand's built-in frame pump feeds AA A9
frames so ``start_stream`` returns within its first-frame timeout."""
def make_calibrated_joint_feedback_hand(config_path, raw_counts, install_encoder_calibration)
```

### tests/test_base_hand_contract.py

```
class DummyHand(BaseHand)
    def __init__(self, config_path)
    def _get_joint_positions(self)
    def _set_joint_positions(self, joint_pos)
def hand(tmp_path)
def test_accepts_dict_joint_commands(hand)
def test_accepts_orca_joint_position_commands(hand)
def test_accepts_ndarray_joint_commands_in_joint_order(hand)
def test_wrong_length_ndarray_raises(hand)
def test_joint_commands_are_clipped_to_joint_rom(hand)
def test_partial_commands_preserve_unspecified_joints(hand)
def test_get_joint_position_as_list_preserves_order(hand)
def test_get_joint_position_returns_typed_wrapper(hand)
def test_set_zero_position_commands_all_zeroes(hand)
def test_set_neutral_position_uses_configured_neutral_pose(hand)
def test_pose_from_fractions_defaults_to_neutral_for_unspecified_joints(hand)
def test_play_named_positions_reuses_registered_poses(hand)
def test_set_neutral_position_without_configured_neutral_pose_is_noop(tmp_path)
def test_interpolation_reaches_same_final_pose(hand)
def test_directory_config_path_is_rejected(tmp_path)
```

### tests/test_hand_class_layout.py

```
"""Pins the hand-class MRO and the deprecated module paths.

The OrcaHandFull diamond is load-bearing: base-tuple order decides which
class serves each seam, and the mock diamond must put the mixin before any
production connect logic. These tests fail loudly if a refactor reorders
the bases or moves a seam."""
def test_full_hand_mro_orders_capabilities_before_bases()
def test_mock_full_hand_resolves_the_mock_mixin_first()
def test_seam_resolves_to_expected_class(cls, method, expected_owner)
def test_all_hand_classes_import_from_package_root()
def test_every_declared_export_is_bound_at_the_package_root()
```

### tests/test_hand_config_loading.py

```
"""Config-loading edge cases: empty config files and sensors.baudrate values."""
def test_empty_config_yaml_raises_clear_error(tmp_path)
def test_comments_only_config_yaml_raises_clear_error(tmp_path)
def _touch_config_with_baudrate(tmp_path, baudrate)
def test_sensors_baudrate_auto_loads_as_auto(tmp_path)
def test_sensors_baudrate_int_loads_as_int(tmp_path)
def test_write_yaml_atomic_exported_from_utils()
```

### tests/test_hand_detection.py

```
"""Hand autodetection: identity parsing, the detection ladder, and load_hand()."""
def test_parse_full_identity_line()
def test_parse_unprovisioned_line_has_no_side()
def test_parse_ignores_unknown_fields_and_junk_values()
def test_parse_rejects_non_identity_lines(line)
def _patch_hardware(monkeypatch)
def test_detects_full_left_hand(monkeypatch)
def test_sideless_board_defaults_right(monkeypatch)
def test_detects_legacy_touch_adapter(monkeypatch)
def test_nothing_plugged_in_yields_plain_right_hand(monkeypatch)
def test_load_hand_autodetects_and_pins_ports(monkeypatch)
def test_load_hand_detection_fallback_is_default_model(monkeypatch)
def test_load_hand_skips_detection_when_told_what_to_load(monkeypatch, kwargs)
```

### tests/test_hand_factory.py

```
def _config(name)
def test_load_hand_selects_class_from_config(model, expected)
def test_load_hand_engage_feedback_false_returns_motor_only(model, expected)
def test_load_hand_warns_on_left_feedback_config(caplog, model, expected, fallback_model)
def test_load_hand_does_not_warn_when_loop_can_engage_or_is_suppressed(caplog, kwargs)
def test_load_hand_carries_full_config_when_feedback_suppressed(tmp_path)
def test_load_hand_respects_explicit_feedback_override(tmp_path)
def test_joint_feedback_enabled_with_encoders(tmp_path, use_joint_feedback, expected)
def test_joint_feedback_disabled_without_encoders(tmp_path)
def test_use_joint_feedback_true_without_encoders_is_rejected(tmp_path)
```

### tests/test_hand_serial_link.py

```
"""Tests for HandSerialLink + MockHandSerialLink.

Threading model: the link's demuxer runs on a background thread, so feeding
bytes is asynchronous. Tests synchronise via ``Condition.wait_for``"""
def _encoder_frame()
def _tactile_frame()
def _read_response(address, data)
class _Capture()
    """Frame-recording handler with a Condition-based ``wait_for(count)``.
    """
    def __init__(self)
    def __call__(self, frame)
    def wait_for(self, count, timeout)
def link()
def test_dispatch_routes_by_second_byte(link)
def test_frame_with_no_handler_is_dropped(link)
def test_register_request_round_trip(link)
def test_drain_before_send_discards_stale_response(link)
def test_demuxer_recovers_from_corruption(link)
def test_disconnect_unblocks_pending_register_request()
def test_handler_exception_does_not_kill_demuxer(link)
def test_send_before_connect_raises()
def test_register_handler_after_disconnect_raises()
def test_link_has_no_pause_api()
def test_port_death_stops_demuxer_and_flags_link(link)
def test_port_death_unblocks_pending_register_request()
def test_register_request_after_port_death_fails_fast(link)
def test_disconnect_after_port_death_is_clean()
def test_connect_after_port_death_raises()
def test_implausible_response_length_has_own_counter(link)
```

### tests/test_hardware_hand.py

```
def mock_hand()
def calibrated_hand(tmp_path)
def test_connect_disconnect_updates_connection_state(mock_hand)
def test_set_control_mode_preserves_wrist_special_case(mock_hand)
def test_set_max_current_supports_scalar_and_list(mock_hand)
def test_disconnect_disables_torque_and_discards_client(mock_hand)
def test_wait_for_motion_skips_the_bus_for_non_waiting_clients(mock_hand)
def test_wait_for_motion_delegates_for_waiting_clients(mock_hand)
def test_init_joints_can_skip_neutral_move(calibrated_hand)
def test_calibrated_joint_command_round_trips_through_motor_mapping(calibrated_hand)
def test_joint_to_motor_pos_applies_the_wrap_offset(calibrated_hand)
def test_calibrated_list_command_round_trips(calibrated_hand)
def test_construction_leaves_config_dir_untouched(tmp_path, hand_cls)
def test_sanity_check_demotes_stale_calibrated_flag_in_existing_file(tmp_path)
def test_sanity_check_does_not_rewrite_already_uncalibrated_file(tmp_path)
def test_sanity_check_demote_write_is_gated_on_persist_calibration(tmp_path, monkeypatch)
def test_mock_construction_never_rewrites_stale_calibration_file(tmp_path)
def test_second_connect_is_noop_returning_success(mock_hand)
def test_second_disconnect_succeeds_without_touching_the_bus(mock_hand)
def test_disconnect_with_raising_torque_off_still_closes_and_allows_reconnect(mock_hand)
def test_del_releases_hands_that_hold_no_motor_client(mock_hand)
def test_del_on_a_half_constructed_hand_does_not_raise()
def test_disconnect_reports_unacked_torque_disable_but_still_closes(mock_hand)
def test_torque_toggles_return_failed_ids_and_warn(mock_hand, caplog)
def test_failed_connect_after_client_open_closes_client(tmp_path, monkeypatch)
def test_failed_connect_logs_instead_of_printing(tmp_path, monkeypatch, capsys, caplog)
def fresh_mock_dir(tmp_path)
def test_mock_calibrate_defaults_to_in_memory_only(fresh_mock_dir)
def test_mock_calibrate_persist_true_opts_into_disk_write(fresh_mock_dir)
def test_init_joints_on_synthesized_mock_skips_calibration(fresh_mock_dir, monkeypatch)
def test_init_joints_force_calibrate_on_mock_leaves_disk_untouched(fresh_mock_dir)
def test_synthesized_mock_limits_fit_mock_motor_travel(fresh_mock_dir)
def test_widest_joint_rom_round_trips_on_synthesized_mock(fresh_mock_dir)
def test_applying_a_calibration_rearms_uncalibrated_warnings(mock_hand, caplog)
def test_raw_to_joint_angle_without_validated_side_raises_actionable_error(tmp_path)
def test_stop_task_reports_and_logs_a_well_formed_message(mock_hand, caplog)
def test_encoder_backed_joints_public_accessor(tmp_path)
```

### tests/test_hardware_hand_full.py

```
"""Lifecycle tests for ``OrcaHandFull`` — the hand that runs tactile sensing
and closed-loop joint feedback together.

The focus is the shared-link orchestration: when the tactile and encoder
streams resolve to the same port, both clients ride one
``HandSerialLink`` (demuxed by frame type), and ``disconnect`` tears the
whole stack down once without error."""
def full_config(tmp_path)
def make_full_hand(config_path)
def test_full_connect_shares_one_link_for_both_streams(full_config)
def test_full_disconnect_tears_down_cleanly(full_config)
def test_full_connect_rolls_back_on_missing_encoder_calibration(full_config)
def left_full_config(full_config, tmp_path)
def test_full_connect_refuses_left_config(left_full_config)
def test_full_left_connect_without_feedback_gets_motors_and_tactile(left_full_config)
def test_full_connect_without_feedback_refuses_while_the_loop_runs(full_config)
def test_full_reconnect_open_loop_after_disconnect(full_config)
def test_full_failed_motor_connect_preserves_sensors_only_tactile(full_config, monkeypatch)
def test_full_second_connect_is_noop_and_orphans_nothing(full_config)
def test_full_connect_after_sensors_only_orphans_no_link(full_config)
def test_full_link_health_and_mock_seam_use_shared_link(full_config)
```

### tests/test_hardware_hand_joint_feedback.py

```
"""Lifecycle and routing tests for ``OrcaHandJointFeedback``: connect
starts the loop without touching motor operating modes, disconnect tears
down cleanly, calibration gate raises on missing encoder calibration,
and the joint-position public API routes encoder joints through the loop
and the wrist through the inherited motor-position path."""
def joint_feedback_config(tmp_path)
def left_joint_feedback_config(tmp_path)
def test_connect_starts_loop_without_touching_operating_modes(joint_feedback_config)
def test_disconnect_stops_loop_and_clears_state(joint_feedback_config)
def test_connect_raises_when_encoder_calibration_missing(joint_feedback_config)
def test_connect_skips_uncalibrated_joints_and_keeps_loop(joint_feedback_config)
def test_set_joint_positions_routes_wrist_and_encoder_joints(joint_feedback_config)
def test_get_joint_positions_wrist_comes_from_motor_position(joint_feedback_config)
def test_estop_falls_back_to_open_loop_joint_io(joint_feedback_config)
def test_skipped_joint_stays_in_reads_and_interpolated_moves(joint_feedback_config, caplog)
def test_second_connect_is_noop_and_orphans_nothing(joint_feedback_config)
def test_connect_refuses_left_hand_config(left_joint_feedback_config)
def test_left_connect_without_feedback_opens_motor_bus_only(left_joint_feedback_config)
def test_connect_without_feedback_refuses_while_the_loop_runs(joint_feedback_config)
def test_open_loop_connect_after_disconnect_admits_calibration(joint_feedback_config)
def test_tension_jitter_and_calibrate_refused_while_loop_runs(joint_feedback_config)
def test_init_joints_tolerates_connect_admitted_partial_calibration(joint_feedback_config)
def test_measured_joints_and_correction_raise_after_estop(joint_feedback_config)
def test_encoder_link_health_reports_port_death(joint_feedback_config)
def test_teardown_warns_when_loop_join_times_out(joint_feedback_config, caplog)
```