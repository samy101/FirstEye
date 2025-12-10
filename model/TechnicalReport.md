# **Model-Centric Track**

**Team:** Pandarasamy Arjunan, IISc Bangalore ([samy@iisc.ac.in](mailto:samy@iisc.ac.in))  
**Model Name:** wv_k_8_c_5_80_small  

## List of Changes Made to the Original Solution:

1. **Input Shape:** Set to `(80,80,3)` – A reasonably large image size is required for person detection.  
2. **Batch Size:** Increased to `2048` (~0.2% of training samples).
3. **Epochs:** Limited to `5` due to long training times.  
4. **Data Augmentation:** Removed, as the dataset is already diverse, making augmentation unnecessary.  
5. **CNN Layers:** Adjusted filter sizes to `8, 16, 24, 32, and 40`. Removed the last CNN layer as it was not useful, and for reducing memory usage and MACs.  
6. **Representative Dataset:** Increased to `20,000` samples (~1.4% of training samples) for PTQ to improve model weight calibration and reduce quantization error.  



