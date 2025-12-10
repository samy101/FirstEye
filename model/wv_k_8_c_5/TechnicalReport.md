# **Model-Centric Track**

Team: Pandarasamy Arjunan, IISc Bangalore (samy@iisc.ac.in)

List of changes made to the original solution:
1. input_shape = (144,144,3) - Ressonably large image size is requird for detecting persons
2. batch_size = 1024         - (~0.1% of training samples. Increased this to handle large number of training samples.
3. epochs = 5 (couldn't train for longer epochs due to longer training time)
4. Removed all data augmentation techniques - data augmentation doesn't make sense bcoz samples are already diverse and idellay humans are expected to use the system in a normal position (heads up)