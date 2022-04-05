# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:17:23 2022

@author: 杜禹仙
"""

import pandas as pd
df=pd.read_csv("C:/Users/杜禹仙/Downloads/STI Nikkei(1).csv")
df=df.dropna()
X=df.loc[:, [' Nikkei Open']]
Y=df.loc[:, ['STI Open']]

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test=train_test_split(X,Y)

from sklearn import linear_model

model=linear_model.LinearRegression().fit(X_train,Y_train)
pred=model.predict(X_test)

from sklearn.metrics import mean_squared_error

print(mean_squared_error(Y_test, pred)**0.5)

import joblib
joblib.dump(model,"STI_REG")
