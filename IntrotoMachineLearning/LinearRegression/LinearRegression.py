# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df = pd.DataFrame(linear_regression_datasetcsv,columns=['deneyim','maas'])

df= pd.read_csv('linear_regression_dataset.csv',sep=';')
plt.scatter(df.deneyim, df.maas)
plt.xlabel('deneyim')
plt.ylabel('maas')

from sklearn.linear_model import LinearRegression
linearreg = LinearRegression()
x=df.deneyim.values.reshape(-1,1) # sklearn accepts (14,1)
y=df.maas.values.reshape(-1,1)

linearreg.fit(x,y)
b=linearreg.predict([[0]]) #y=ax+b
a=linearreg.coef_
coef=a[0][0]
b0=b[0][0]
print('Line equation: y={}*x+{}'.format(coef,b0))

linex = np.arange(1,16).reshape(-1,1)
fittedliney = linearreg.predict(linex)
plt.plot(linex,fittedliney,'r')