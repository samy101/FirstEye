# 🧠 FirstEye — Model Development
**ARM AI Developer Challenge: Edge Model Optimization Track**

Welcome to the Model Development component of FirstEye, an AI system designed for ultra-efficient person presence detection across three Arm-powered platforms:
- 📱 Android (Cortex-A720)
- 🍓 Raspberry Pi 5 (Cortex-A76)
- 🎯 Arduino Nicla Vision (Cortex-M7 Microcontroller)

This directory contains everything related to the design, training, optimization, and evaluation of the FirstEye model.

---

## 🚀 Overview

The ARM hackathon focuses on building performant, deployable AI models for Arm-based devices, emphasizing:
- Small memory footprint
- Low latency
- Energy-efficient inference
- Portability across heterogeneous Arm hardware

To achieve this, we designed a compact CNN model with:
⭐ Input resolution: 80 × 80 RGB
⭐ Output: 2 classes → `Person`, `No Person`
⭐ Format: Fully quantized TFLite (uint8)
⭐ Size: ~90 KB
⭐ Hardware-friendly ops: Conv2D, DepthwiseConv, ReLU, AvgPool

This model has been successfully deployed on:
- Android phone (real-time inference using CameraX + TFLite)
- Arduino Nicla Vision (OpenMV ML Engine + TensorFlow Lite Micro)
- Raspberry Pi 5 (TFLite Runtime + libcamera streaming)

This demonstrates the model’s true cross-platform edge deployment capability, which is a core judging criterion of this hackathon.

## 🧩 Model Architecture Summary
The architecture is based on principles of:
- Depthwise separable convolutions
- Early feature extraction
- Aggressive spatial downsampling
- Minimal parameter count
- Quantization-aware training

The model training script:
```
model_centric_track_small.py
```

implements the full training pipeline:
- Data preprocessing
- Model definition
- Training loop
- Evaluation
- Export to SavedModel and TFLite
- Post-training quantization

Final exported model:
```
wv_k_8_c_5_80_small.tflite
```

## 🎯 Why This Model is Ideal for ARM Edge Devices

| Platform                 | Reason It Works                                                     |
| ------------------------ | ------------------------------------------------------------------- |
| **Android (A720)**       | Exploits TFLite NNAPI acceleration, <1ms overhead per frame.        |
| **Raspberry Pi 5 (A76)** | Optimized for CPU-only inference at 50–80 FPS using TFLite Runtime. |
| **Nicla Vision (M7)**    | Fits inside RAM, uses CMSIS-NN via OpenMV, ~15 FPS sustained.       |

This cross-platform operability is intentional and aligns with hackathon categories around:
- Model portability
- Efficient inference on constrained hardware
- Real-world deployability

## 📦 Structure of This Directory
```
model/
│   README.md                 ← this file
│   Metrics.xlsx              ← accuracy & inference benchmarks
│   TechnicalReport.md        ← full architecture description
│   model_centric_track_small.py
│   wv_k_8_c_5_80_small.tflite ← final deployed model
│
├── wv_k_8_c_5/
│   ├── *.tflite
│   ├── *.pb
│   └── variables/
│
└── wv_k_8_c_5_80_small.tf/
    ├── saved_model.pb
    ├── fingerprint.pb
    └── variables/
```

## 🛠️ Training the Model

Training is optional for users of FirstEye; the repo already includes the final `.tflite` model.

But if you want to reproduce, retrain, or modify the model:

#### 1️⃣ Install Docker

Follow: https://docs.docker.com/engine/install/

#### 2️⃣ CPU Training (simplest)
```
sudo docker run -it --rm \
  -v $PWD:/workspace -w /workspace \
  tensorflow/tensorflow:latest \
  python model_centric_track_small.py
```

#### 3️⃣ GPU Training (if CUDA is available)
```
sudo docker run --gpus all -it --rm \
  -v $PWD:/workspace -w /workspace \
  tensorflow/tensorflow:latest-gpu \
  python model_centric_track_small.py
```

Outputs will appear in:
```
wv_k_8_c_5_80_small.tf/
wv_k_8_c_5_80_small.tflite
```

## 📊 Evaluation & Metrics

The file Metrics.xlsx includes:
- Accuracy on held-out validation set
- Confusion matrix
- TFLite inference time on:
  - Nicla Vision (Cortex-M7)
  - Raspberry Pi 5 (Cortex-A76)
  - Android (A720 phone)

Our model demonstrates strong performance while staying extremely small.

## 🔗 Integration With Deployment Targets

The model from this folder is used directly in:

| Platform           | Path                                         | Link                                                                           |
| ------------------ | -------------------------------------------- | ------------------------------------------------------------------------------ |
| **Android**        | `deployment/Mobile-ARM-Cortex-A720/app`      | → [Android Deployment Guide](../deployment/Mobile-ARM-Cortex-A720/README.md)   |
| **Nicla Vision**   | `deployment/Arduino_Nicla_Vision-Cortex-M7/` | → [Nicla Vision Guide](../deployment/Arduino_Nicla_Vision-Cortex-M7/README.md) |
| **Raspberry Pi 5** | `deployment/RaspberryPi-Cortex-A76/`         | → [Raspberry Pi 5 Guide](../deployment/RaspberryPi-Cortex-A76/README.md)       |


The same model file runs unchanged on all three devices — a core demonstration of Arm-based cross-platform ML deployment.

## 🤝 Contributions & Extensions
You may extend this model by:
- Adding MobileNetV3-style inverted residual blocks
- Pruning channels for even smaller memory footprint
- Trying int4 or mixed-precision quantization
- Adding post-processing (temporal smoothing, motion detection, etc.)
Pull requests (PRs) are welcome.

## 📬 Support

If you need help with model training or deployment:
→ Open an issue in the repository.
→ Or contact via GitHub Discussions.

## 🌟 Final Note

This model is the heart of FirstEye — a tiny, fast, cross-device person detector built specifically for Arm CPUs and microcontrollers.
It showcases:
- ML model design
- Hardware-aware optimization
- Real-world deployment engineering

All of which are key in the Arm AI Developer Challenge.