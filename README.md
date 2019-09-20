# Age Group and Gender estimation from face image using CNN.

Two Custom CNN layers are trained for age group and gender estimation.

For the Age Group classification trained CNN over the 23000 images, and for the Gender Classification trained CNN 4000+ images of indian face.

###

#### Age Group parameters are :
```
Kid = 0 - 14,
Youth = 15-40,
Middle Age = 41-60,
Senior = 60+.
```
#### Gender parameters are :
```
1) Male
2) Female
```
The name of dataset is "UTKFace" where the information about age, gender, and ethnicity is given in the image title.
***Link***: https://www.kaggle.com/jangedoo/utkface-new

# Usage
1. Install Following libraries using pip
- numpy 1.16.2
- opencv-python 4.0.1.24
- face-recognition 1.2.3
- tensorflow 1.11.0
- tensorflow-gpu 1.11.0 (Optional if you have Nvidia CUDA Supported GPU)
- keras 2.2.4
- PyQt5 5.12.1
2. Clone or download the repository and extract it into a folder and open it.
3. Run gui.py using cmd 
```
python gui.py
```
# Convolution Neural Network

***Link***: https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148

# Training CNN
##### Image Preprocessing:
Face Images are resize into 180X180 pixel size and converted into gray scale and given image input to CNN.

For more than 2 class classification label is encoded with one hot encoding.

# Results
![alt text](https://github.com/prashantmokani/age_and_gender_classifier/blob/master/male-senior-modi.JPG)

![alt text](https://github.com/prashantmokani/age_and_gender_classifier/blob/master/op1.PNG)

![alt text](https://github.com/prashantmokani/age_and_gender_classifier/blob/master/dubai.jpg)

###### Confusion matrix for the Gender classification:

![alt text](https://github.com/prashantmokani/age_and_gender_classifier/blob/master/conf_gender.PNG)

###### Confusion matrix for the Age Group classification:

![alt text](https://github.com/prashantmokani/age_and_gender_classifier/blob/master/conf_age.PNG)

