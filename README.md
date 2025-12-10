# FirstEye — On-device Person Detection (VIZ)

**FirstEye** (VIZ) is a lightweight, privacy-first on-device person detection project.
It demonstrates deploying the same Wake Vision–trained TFLite model to:

- Android (TensorFlow Lite + CameraX)
- Arduino Nicla Vision (OpenMV / MicroPython)
- Raspberry Pi 5 (TensorFlow Lite + OpenCV / camera)

This repo contains the app code, microcontroller script, and Raspberry Pi example to run the 80×80, 2-class model (`No Person`, `Person`) on edge devices.

---

## Quick links
- Android guide → `android/README.md`
- Nicla Vision guide → `nicla_vision/README.md`
- Raspberry Pi 5 guide → `raspberrypi/README.md`
- Model description → `model_card.md`

---

## Demo
(Add screenshots or animated GIFs here showing Nicla and Android running.)

---

## Model
Model file(s) are under each target’s `model/` folder. See `model_card.md` for input/output shape, quantization, and training notes.

---

## License
This project is released under the MIT license. See `LICENSE`.

---

## Contributing
Contributions welcome — open an issue or PR. See `CONTRIBUTING.md` (optional).

---

## Contact
Your Name — [GitHub profile link] — contact email
