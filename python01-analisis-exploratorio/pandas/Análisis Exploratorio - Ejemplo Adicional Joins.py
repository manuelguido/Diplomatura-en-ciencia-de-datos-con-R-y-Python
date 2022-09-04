#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Países y Capitales
capitales = pd.DataFrame(
    {'Country':['Afghanistan','Argentina','Australia','Canada','China','France','India','Nepal','Russia','Spain'],
     'ISO' : ['AF','AR','AU','CA','CN','FR','IN','NP','RU','ES'],
     'Capital' : ['Kabul','Buenos_Aires','Canberra','Ottawa','Beijing','Paris','New_Delhi','Katmandu','Moscow','Madrid'] },
    columns=['Country', 'ISO', 'Capital'])

# País y su moneda
moneda = pd.DataFrame(
    {'Country':['France','India','Nepal','Russia','Spain','Sri_Lanka','United_Kingdom','USA','Uzbekistan','Zimbabwe'],
     'Currency' : ['Euro','Indian_Rupee','Nepalese_Rupee','Rouble','Euro','Rupee','Pound','US_Dollar','Sum_Coupons','Zimbabwe_Dollar'],
     'Digraph' : ['FR','IN','NP','RU','ES','LK','GB','US','UZ','ZW'] },
    columns=['Country', 'Currency', 'Digraph'])


# In[2]:


print(capitales)


# In[3]:


print (moneda)


# In[4]:


# Inner Join
pd.merge(left = capitales, right = moneda, how = 'inner')


# In[5]:


pd.merge(left = capitales, right = moneda, how = 'inner', on = 'Country' )


# In[6]:


pd.merge(left = capitales, 
         right = moneda,
        how= 'inner',
        left_on='ISO',
        right_on='Digraph',
        suffixes=('_x', '_y'))


# In[7]:


# Filtrar una columna por una expresión regular
pd.merge(left = capitales,
         right = moneda,
        how= 'inner',
        left_on='ISO',
        right_on='Digraph',
        suffixes=('', '_drop')).filter(regex='^(?!.*_drop)')


# In[8]:


# Outer Join

pd.merge(left = capitales, right = moneda, how = 'outer')


# In[9]:


# Filtrar una columna por una expresión regular

pd.merge(left = capitales,
         right = moneda,
        how= 'outer',
        left_on='ISO',
        right_on='Digraph',
        suffixes=('', '_drop')).filter(regex='^(?!.*_drop)')


# In[10]:


# Left Join

pd.merge(left = capitales, right = moneda, how = 'left')


# In[11]:


# Right Join

pd.merge(left = capitales, right = moneda, how = 'right')


# In[ ]:




