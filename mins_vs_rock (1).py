# -*- coding: utf-8 -*-
"""Mins VS Rock

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z5bT0hzsbT8XrQG4KJs60IKvaYbTL2gl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

dataset=pd.read_csv("Copy of sonar data.csv",header=None)

dataset.head(2)

dataset.shape

dataset.describe()

dataset[60].value_counts()

#M----- Mine
#R------ Rock

dataset.groupby(60).mean()

"""seprating dataset"""

x= dataset.drop(columns=60,axis=1)
y=dataset[60]

print(x)
print(y)

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.1,stratify=y, random_state=1)

"""Logistic regression model"""

model=LogisticRegression()

model.fit(x_train,y_train)

#accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on training data : ', training_data_accuracy)

y_test

"""# **Making a Predictive system**"""

input_data= (0.0216,0.0124,0.0174,0.0152,0.0608,0.1026,0.1139,0.0877,0.116,0.0866,0.1564,0.078,0.0997,0.0915,0.0662,0.1134,0.174,0.2573,0.3294,0.391,0.5438,0.6115,0.7022,0.761,0.7973,0.9105,0.8807,0.7949,0.799,0.718,0.6407,0.6312,0.5929,0.6168,0.6498,0.6764,0.6253,0.5117,0.389,0.3273,0.2509,0.153,0.1323,0.1657,0.1215,0.0978,0.0452,0.0273,0.0179,0.0092,0.0018,0.0052,0.0049,0.0096,0.0134,0.0122,0.0047,0.0018,0.0006,0.0023)
    #changing the input data into numpy array
input_data_as_numpy_array=np.asarray(input_data)
# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]=='R'):
  print("This is Rock")
else:
  print("This is Mine")