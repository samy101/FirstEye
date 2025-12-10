# FirstEye — On-Device Human Presence Detection
**Ultra-light, cross-platform Wake Vision model deployed on Raspberry Pi 5, Arduino Nicla Vision, and Android**

FirstEye is a privacy-preserving, on-device human presence detection system powered by an 80×80 TensorFlow Lite model trained using the Wake Vision dataset.

The project demonstrates efficient edge AI deployment across three hardware classes:
- Raspberry Pi 5 (Cortex-A76, Linux)
- Arduino Nicla Vision (Cortex-M7, Microcontroller)
- Android Mobile Devices (Cortex-A720-class CPUs)

This project showcases how a single, small-footprint ML model can be optimized and deployed seamlessly across heterogeneous compute devices while maintaining high performance, real-time inference, and robustness across environments.

---

## Quick links
- Android guide → `android/README.md`
- Nicla Vision guide → `nicla_vision/README.md`
- Raspberry Pi 5 guide → `raspberrypi/README.md`
- Model description → `model_card.md`

---

## ⭐ Core Features

- **Fully on-device inference** — no cloud, no streaming, privacy-first
- **Cross-platform deployment**
  - Android App (CameraX + TFLite)
  - Arduino Nicla Vision (OpenMV + MicroPython)
  - Raspberry Pi 5 (libcamera + OpenCV + TFLite Runtime)

- **Lightweight Wake Vision model**
  - wv_k_8_c_5_80_small.tflite
  - Input: 80×80 RGB
  - Outputs: Person / No Person (2 classes)

- **Optimized pipelines** for each device
- **Open-source model, training code, and deployment scripts**
---

## 🚀 Quick Start (By Device)
### 🔵 Raspberry Pi 5
Located in:
```
deployment/RaspberryPi-Cortex-A76/
```

Includes:
- `firsteye_pi.py` (MJPEG streaming + inference)
- `requirements.txt` (numpy<2, opencv-python, tflite-runtime)
- `model/wv_k_8_c_5_80_small.tflite`
- Full README with setup instructions (venv, libcamera streaming)

### 🟢 Arduino Nicla Vision
Located in:
```
deployment/Arduino_Nicla_Vision-Cortex-M7/
```

Includes:
- `nicla_person_detect.py`
- Instructions for OpenMV IDE
- Model placed under `/model/` folder

### 🟠 Android (ARM Cortex-A720 Class)
Located in:
```
deployment/Mobile-ARM-Cortex-A720/
```

Includes:
- Android app project
- Instructions to update TFLite model and labels
- Build/run steps

## 🧠 Model Description

Model Card: `model_card.md`

**Model Name:** `wv_k_8_c_5_80_small.tflite`
- Input: **80×80, RGB, 3 channels**
- Shape: `[1, 80, 80, 3]`
- Output: 2 classes
  - `0` — No Person
  - `1` — Person
- Type: TensorFlow Lite (uint8/int8 quantized)
- Designed for ultra-efficient edge inference
- The full training pipeline, SavedModel, and exploration notebooks are in:
```
model/
```

## 📁 Repository Structure
```
FirstEye/
│   .gitignore
│   LICENSE
│   model_card.md
│   README.md              <-- (You are reading this)
│
├── dataset/               <-- (Datasets / sample sets if required)
│
├── deployment/
│   ├── Arduino_Nicla_Vision-Cortex-M7/
│   │   ├── nicla_person_detect.py
│   │   ├── README.md
│   │   └── model/
│   │       └── wv_k_8_c_5_80_small.tflite
│   │
│   ├── Mobile-ARM-Cortex-A720/
│   │   ├── README.md
│   │   └── app/          <-- Android project
│   │
│   └── RaspberryPi-Cortex-A76/
│       ├── firsteye_pi.py
│       ├── README.md
│       ├── requirements.txt
│       └── model/
│           └── wv_k_8_c_5_80_small.tflite
│
└── model/
    ├── Metrics.xlsx
    ├── model_centric_track_small.py
    ├── README.md
    ├── TechnicalReport.md
    ├── wv_k_8_c_5_80_small.tflite
    │
    ├── wv_k_8_c_5/
    │   ├── model_centric_track.py
    │   ├── model_centric_track_orig.py
    │   ├── TechnicalReport.md
    │   ├── wv_k_8_c_5.tflite
    │   └── wv_k_8_c_5.tf/
    │       ├── fingerprint.pb
    │       ├── keras_metadata.pb
    │       ├── saved_model.pb
    │       └── variables/
    │           ├── variables.data-00000-of-00001
    │           └── variables.index
    │
    └── wv_k_8_c_5_80_small.tf/
        ├── fingerprint.pb
        ├── keras_metadata.pb
        ├── saved_model.pb
        └── variables/
            ├── variables.data-00000-of-00001
            └── variables.index

```
---

## 🎯 Why This Project Matters
- Shows how one TFLite model can run efficiently across three hardware classes
- Demonstrates scalable AI deployment from MCUs → Mobiles → SBCs
- Enables edge-only privacy for home monitoring, robotics, IoT presence sensing
- Lightweight model = low power, fast inference, tiny memory footprint

## 🛠️ How to Contribute
Pull requests are welcome!
You can contribute:
- New models
- Deployment examples
- ARM/NPU optimizations
- Benchmarking scripts

## 📜 License
This project is licensed under the MIT License — see LICENSE.

## 🙌 Acknowledgments
- Wake Vision dataset and challenge organizers
- TensorFlow Lite team
- Arduino + OpenMV tooling
- Raspberry Pi Foundation