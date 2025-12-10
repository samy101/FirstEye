# Nicla Vision — FirstEye

This folder contains the MicroPython script and instructions to run `wv_k_8_c_5_80_small.tflite` on Arduino Nicla Vision using OpenMV.

## Requirements
- Arduino Nicla Vision (STM32H747)
- OpenMV IDE (for flashing & serial)
- OpenMV firmware: v4.5.1 or v4.7.x depending on supported APIs (this repo tested with v4.7.x + ml)
- MicroPython / OpenMV with `ml` module (must support `img.to_ndarray`)

## Files
- `nicla_person_detect.py` — final script (drop into device)
- `model/wv_k_8_c_5_80_small.tflite` — model file (put in board root)

## Steps

1. Install OpenMV IDE: https://openmv.io/pages/download  
2. Connect Nicla Vision via USB-C and open the IDE.
3. Put the device into bootloader and flash the recommended OpenMV firmware if required.
4. Copy the model (`wv_k_8_c_5_80_small.tflite`) to the device file system (drag into OpenMV file explorer).
5. Copy `nicla_person_detect.py` to the board and run it.

### Run (in OpenMV REPL)
```python
>>> import nicla_person_detect
```
**Notes & troubleshooting**

  - If img.to_ndarray is missing, update firmware (or use grayscale model).

  - If you get Unsupported input typ: ensure input_dtype from net.input_dtype[0] matches to_ndarray(...). If firmware does not accept RGB, convert model to grayscale.

---
