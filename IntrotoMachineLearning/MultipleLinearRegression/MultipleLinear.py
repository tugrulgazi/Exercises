# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df= pd.read_csv('multiple_linear_regression_dataset.csv',sep=';')

y=df.maas.values.reshape(-1,1) # dependent value
x=df.iloc[:,[0,2]].values

multiplelinear = LinearRegression()
multiplelinear.fit(x,y)     # y = ax1+bx2+c
c = multiplelinear.intercept_[0]
ab = multiplelinear.coef_
a = ab[0][0]
b = ab[0][1]
print('Line equation: y={}*x1+{}*x2+{}'.format(a,b,c))

result=multiplelinear.predict([[10,35],[5,35]])
diff = abs(result[0][0]-result[1][0])
print('Same age(35) but 5 years of more works means {:.5}$ more.'.format(diff))