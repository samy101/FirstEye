import sensor, image, time, ml
from ulab import numpy as np

net = ml.Model("wv_k_8_c_5_80_small.tflite", load_to_fb=True)

labels = ["No Person", "Person"]

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_windowing((80, 80))
sensor.skip_frames(time=2000)

input_shape = net.input_shape[0]   # e.g. (1, 80, 80, 3)
input_dtype = net.input_dtype[0]   # 'B', 'b', or 'f'

# No Python loops here ✂️
def snapshot_to_ndarray():
    img = sensor.snapshot()
    # Convert RGB565 -> ndarray (H, W, 3) with correct dtype
    arr = img.to_ndarray(input_dtype)   # dtype: 'B' / 'b' / 'f'
    return arr

clock = time.clock()

while True:
    clock.tick()

    arr = snapshot_to_ndarray()         # (80, 80, 3)
    arr = arr.reshape(input_shape)      # (1, 80, 80, 3)

    raw_outputs = net.predict([arr])
    raw_output = raw_outputs[0]
    output = raw_output.flatten().tolist()

    idx = output.index(max(output))
    label = labels[idx]
    confidence = max(output) / 255.0 if max(output) > 1 else max(output)

    if label == "Person":
        print(output)
        print("Prediction:", label, "Confidence:", confidence)

    print("FPS:", clock.fps())
