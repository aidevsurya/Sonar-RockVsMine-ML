import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

data = pd.read_csv("sonar.all-data.csv")
print(data.isnull().sum())

X = data.values[:,0:-1]
print(X)

Y = data.values[:,-1]
print(Y)

xTrain,xTest,yTrain,yTest = train_test_split(X,Y,test_size=0.2)

Model = LogisticRegression()
Model.fit(xTrain,yTrain)
print(Model.predict(xTest))
print(Model.score(xTest,yTest))