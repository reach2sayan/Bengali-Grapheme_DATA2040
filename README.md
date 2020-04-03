# Team Onubaad - Bengali Handwritten letter Classification


This project was conducted by [Wanxin Ye](https://github.com/leavetina321) and [Sayan Samanta](https://github.com/reach2sayan), for partial fulfillment of the credit requirements for DATA 2040 - Hands on Deep Learning, working towards a masters degree in Data Science from the Data Science Initiative | Brown University. 

Bengali (used synonymous to Bangla) ranks in the top 5 spoken languages with more than hundreds of millions of speakers. In this repository, we attempt to classify bengali handwritten character into its 3 structural component -  Grapheme root, Vowel diacritic and Consonant diacritic. 

The problem statement and the data is obtained from the  [kaggle competition](https://www.kaggle.com/c/bengaliai-cv19/).

---

A detailed description of the work can be found in the series of medium post:

 1. [Bangla Character Recognition System - The Deep Learning way (1/n)](https://medium.com/analytics-vidhya/bangla-character-recognition-system-the-deep-learning-way-1-n-8671a33a7860)
 2. [Bangla Character Recognition System - The Deep Learning way (2/n)](https://medium.com/analytics-vidhya/bangla-character-recognition-system-the-deep-learning-way-2-n-d5b16333d77b)
 3. [Bangla Character Recognition System - The Deep Learning way (3/n)](https://medium.com/analytics-vidhya/bangla-character-recognition-system-the-deep-learning-way-3-n-17cb1d140a5f)
 
Here we do give a brief description about the content of the repository without going in to the implementation details or data description. You are requested to read the blog posts for further details.

---

### Major Notebooks:

 1. [**Image Processing**](https://github.com/reach2sayan/Bengali-Grapheme_DATA2040/blob/master/notebooks/Image%20processing.ipynb) - Contains code to De-Noise, Threshold and Crop based on Contours.
 2. [**Data Distribution**](https://github.com/reach2sayan/Bengali-Grapheme_DATA2040/blob/master/notebooks/Data%20Distribution.ipynb) - Primary EDA notebook. Contains all analysis of distribution and balance of different target classes in the dataset
 3. [**Augmentation,Generators,Architectures_2_colab**](https://github.com/reach2sayan/Bengali-Grapheme_DATA2040/blob/master/notebooks/Augmentation%2CGenerators%2CArchitectures_2_colab.ipynb) - Main notebook. Contains code for different architectures that were tried - AlexNet, BengaliNet (the kernel shared on piazza), ResNet (mini), InceptionNet (mini), InceptualNet (Inception + Residual net), FractalNet and in-house DenseNet (mini)
 
Note. there are redundant copies of similar named files. We had to shift to Google Colab and decided to load entire pre-processed dataset to RAM instead of input pipelines, hence the redundancy.
