import cv2
import numpy as np
import subprocess
import time
from tensorflow.lite.python.interpreter import Interpreter

# Model and labels
MODEL_PATH = "wv_k_8_c_5_80_small.tflite"
LABELS = ["No Person", "Person"]

# Start rpicam-vid MJPEG stream
cmd = [
    "rpicam-vid",
    "--timeout", "0",
    "--codec", "mjpeg",
    "--inline",              # ensures keyframes always included
    "--framerate", "30",
    "--width", "320",
    "--height", "240",
    "-o", "-"
]

camera = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=0)

# Load TFLite model
interpreter = Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

H, W = input_details[0]['shape'][1:3]  # 80x80
print("Model expects:", W, "x", H)

buffer = bytearray()
print("Starting FirstEye on Raspberry Pi 5...")

def decode_mjpeg(buffer):
    idx = buffer.find(b'\xff\xd9')
    if idx == -1:
        return None, buffer
    jpeg = buffer[:idx+2]
    buffer = buffer[idx+2:]
    img_array = np.frombuffer(jpeg, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return frame, buffer

while True:
    chunk = camera.stdout.read(4096)
    if not chunk:
        continue

    buffer.extend(chunk)

    frame, buffer = decode_mjpeg(buffer)
    if frame is None:
        continue

    t0 = time.time()

    # Preprocess for model (80x80 RGB)
    img = cv2.resize(frame, (W, H))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img.astype(np.uint8), 0)

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    out = interpreter.get_tensor(output_details[0]['index'])[0]

    # Dequantize output
    scale, zero = output_details[0]['quantization']
    real = (out - zero) * scale
    exp = np.exp(real - np.max(real))
    probs = exp / exp.sum()

    idx = np.argmax(probs)
    label = LABELS[idx]
    conf = float(probs[idx])

    fps = 1.0 / (time.time() - t0)

    # Draw result
    cv2.putText(frame, f"{label} ({conf:.2f}) FPS: {fps:.1f}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0) if label == "Person" else (0, 0, 255), 2)

    cv2.imshow("FirstEye - Raspberry Pi 5", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.terminate()
cv2.destroyAllWindows()
