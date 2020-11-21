# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('polynomial+regression.csv',sep=';')

y = df.araba_max_hiz.values.reshape(-1,1)
x = df.araba_fiyat.values.reshape(-1,1)
plt.ylabel('araba_max_hiz')
plt.xlabel('araba_fiyat')
plt.scatter(x,y)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x,y)
y_head = lr.predict(x)
plt.plot(x,y_head,'r',label='linear')

# y = ax^2+bx+c
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(x)

lr2 = LinearRegression()
lr2.fit(x_poly, y)

newy = lr2.predict(x_poly)
plt.plot(x,newy,'b',label='poly')
plt.legend()



