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

# Convolution Neural Network

***Link***: https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148

# Training CNN
##### Image Preprocessing:
Face Images are resize into 180X180 pixel size and converted into gray scale and given image input to CNN.

For more than 2 class classification label is encoded with one hot encoding.

# Results
Confusion matrix for the Gender classification:

![alt text](http://url/to/img.png)

Confusion matrix for the Age Group classification:

![alt text](http://url/to/img.png)
