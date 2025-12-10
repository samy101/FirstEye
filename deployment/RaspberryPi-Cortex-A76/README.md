# FirstEye — Raspberry Pi 5 (Bookworm) guide

This folder contains the Raspberry Pi 5 deployment for the Wake Vision person-detection model.

## Files
  - `firsteye_pi.py` — main detection script (uses rpicam-vid MJPEG pipe)
  - `download_model.sh` — helper to download the model (GitHub release or other hosted URL)
  - `model/` — place the `wv_k_8_c_5_80_small.tflite` here (or use the download script)

---

Quick start (on Pi 5, Bookworm 64-bit)

1. Clone this repo:
```
git clone https://github.com/samy101/FirstEye.git
cd FirstEye/raspberrypi
```

2. Create a virtual environment and activate it:
```
python3 -m venv firey
source firey/bin/activate
pip install --upgrade pip
```

3. Install required Python packages:
   Preferred (lightweight):
```
pip install opencv-python tflite-runtime numpy<2
```

Fallback (if tflite-runtime wheel not available):
```
pip install opencv-python tensorflow numpy<2
```

**Note:** If you install full tensorflow, change interpreter import in scripts if required (provided script auto-fallbacks).

4. Download model (if not present):
```
chmod +x download_model.sh
./download_model.sh
```

5. Run detection:
```
python3 firsteye_pi.py
```

Press q in the preview window to quit.

---

## Headless mode (no GUI)

Edit firsteye_pi.py and comment out cv2.imshow(...) and cv2.waitKey(...). The script will still print predictions to stdout.

---

## Performance tips

  - Use --width 320 --height 240 in the rpicam command (script is already configured to use 320×240 MJPEG).

  - For faster inference, use a quantized int8 model and set interpreter = Interpreter(model_path, num_threads=4).

--- 

## Troubleshooting

  - If rpicam-vid works but frames aren't decoded, make sure opencv-python is installed in the same virtualenv.

  - If tflite-runtime fails to install, install tensorflow as fallback.

  - If you see NumPy ABI errors, use pip install "numpy<2" --force-reinstall inside the venv.