#!/usr/bin/env python
# coding: utf-8

# In[8]:


#vamos a explorar un poco el dataset de iris
from sklearn import datasets
import pandas as pd

#df.corr(method ='kendall')

#vuelvo a cargar el dataset de iris
iris = datasets.load_iris()
#creo el dataframe de iris
iris_df=pd.DataFrame(iris.data)
iris_df.corr(method = 'pearson')


# In[9]:


import matplotlib.pyplot as plt
plt.matshow(iris_df.corr())


# In[ ]:


#Pearson
#El valor del índice de correlación varía en el intervalo [-1,1]
#Si este coeficiente es igual a 1 o -1 (o cercano a estos valores) significa que una variable es 
#fruto de una transformación lineal de la otra. 
#Teniendo una relación directa al tratarse de 1 (cuando una variable aumenta, la otra también),
#mientras que existirá una relación inversa al tratarse de -1 (cuando una variable aumenta la otra disminuye).
#Mientras que, Si r = 0 (o cercano a este valor) no existe relación lineal,
#aunque puede existir algún otro tipo de relación no lineal.


# In[12]:


print(iris_df)


# In[ ]:




