import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

#importing Dataset

dataset=pd.read_csv('Data.csv')
print(dataset)
x=dataset.iloc[:,:-1].values
print(x)
y=dataset.iloc[:,3].values
print(y)

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)  #strategy=median,most_frequent
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)

#Encoding Categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])
print(x)
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
print(x)
labelencoder_y=LabelEncoder()
y=labelencoder_x.fit_transform(y)
print(y)

#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

