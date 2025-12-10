# Model Card — wv_k_8_c_5_80_small.tflite

- **Source / training**: Wake Vision dataset (link)
- **Format**: TensorFlow Lite
- **Input shape**: [1, 80, 80, 3] (RGB)
- **Input dtype**: int8 or float32 (see file)
- **Output shape**: [1, 2] (logits)
- **Classes**: 0 → No Person, 1 → Person
- **Quantization**:  may be int8; always inspect model quantization with the TFLite interpreter:
- **Notes**: model expects RGB, 80×80 crop. If running on microcontrollers using `ml.Model` that only accepts grayscale, re-export or quantize accordingly.

```python
  from tflite_runtime.interpreter import Interpreter
  interpreter = Interpreter("model.tflite")
  interpreter.allocate_tensors()
  print(interpreter.get_input_details())
  print(interpreter.get_output_details())
```