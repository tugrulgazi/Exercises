# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# iris_dict = {'Sepal_Length':[5,4,3,2,1],
#               'Sepal_Width':[10,8,6,4,2],
#               'Petal_Length':[1,1,1,1,1],
#               'Petal_Width':[2,2,2,2,2,],
#               'Species':['setosa','setosa','virginica','virginica','virginica']
#               }
# iris = pd.DataFrame(iris_dict)
# print(iris)
# print(iris.columns)
# iris['assbig'] = 1
# print(iris.index)
# print(iris.shape)

# sutunlar = pd.MultiIndex.from_product([['Sepal','Petal'],['Length','Width']])
# veri = np.array([5,10,1,2,
#                  4,8,1,2,
#                  3,6,1,2,
#                  2,4,1,2,
#                  1,2,1,2])
# veri = veri.reshape(5,4)
# a = np.repeat(['A','B'],[2,3],axis = 0)
# iriss = pd.DataFrame(veri,columns = sutunlar,index = a )
# iriss['Species']=['setosa','setosa','virginica','virginica','virginica']
# # print(iriss[['Sepal','Petal']].min())
# # ir = iriss[iriss['Sepal']['Length']==5]
# # print(ir.iloc[:,:3])
# # print(iriss.Sepal.Length.describe())
# # print(iriss.Species.describe())

# print(iriss['Sepal']['Width'][iriss['Sepal']['Length']>3])
# irisss = iriss.loc['A']
# print(irisss[irisss['Sepal']['Length']>4])












































