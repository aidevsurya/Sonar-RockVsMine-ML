# import os

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import accuracy_score

# ------------ Custom Libs -----------
#import dataset

def write(*text):
    print("\t\t OUTPUT: \n",text,end="\n")

print("Successfully Imported Libraries")

#directory = dataset.dataset()
#filename = os.listdir(directory)[0]
#write(filename)
#path = os.path.join(directory,filename)

path = "sonar data.csv"
write("Taking Data from - ",path)

df = pd.read_csv(path,header=None)

write(df.head())
write(df.describe())
write(df.info())
write(df.isna().sum)
write(df[60].value_counts())

X = df.drop(columns=60,axis=1)
Y = df[60]

write("Features - ", X)
write("Labels - ", Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, stratify=Y, random_state=2)

model = LR()
model.fit(X,Y)
result = model.predict(X_test)

write(accuracy_score(Y_test,result))
write(model.score(X_test,Y_test))

write("Prediction on last row data : ", model.predict(X.tail(1))[0])
write("Actual Answer on last row data : ", np.asarray(Y)[-1])