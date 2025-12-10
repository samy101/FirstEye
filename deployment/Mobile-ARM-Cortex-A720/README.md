# Android — FirstEye (VIZ)

This folder contains an Android Studio project based on TensorFlow Lite `image_classification` sample.

## Prerequisites
- Android Studio
- Android device (ARM CPU) for testing
- Model: `wv_k_8_c_5_80_small.tflite`

## Files
- `app/src/main/assets/model.tflite` — replace with `wv_k_8_c_5_80_small.tflite`
- `app/src/main/assets/labels.txt` — 2 lines: `No Person` and `Person`
- `ImageClassifier` helper — update input size if necessary

## Steps
1. Open this folder in Android Studio.
2. Replace `app/src/main/assets/model.tflite` with your model.
3. Replace labels file with:
```
No Person
Person
```
---
4. Update any code where input size is hard-coded (default sample uses 224x224). Change model input dimensions (80×80) in the classifier helper or task options.
5. Build and run on ARM device.

## Remarks
- Use TFLite Task Library or custom Interpreter depending on model ops.
- For better performance, add GPU delegate if model is float and device supports it.
