#!/usr/bin/env python
# coding: utf-8

# **Conexión a la Base de Datos**
# 
# import sqlite3
# 
# conn = sqlite3.connect('database.sqlite')
# 
# cursor = conn.cursor()
# 
# print("Conectado correctamente")

# **Creación de la Tabla**
# 
# cursor.execute('''CREATE TABLE Nombre
# 
#          (ID INT PRIMARY KEY     NOT NULL,
#          
#          Campo1           TEXT    NOT NULL,
#          
#          Campo2            INT     NOT NULL);''')
#          
# cursor.close()

# In[25]:


import sqlite3

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)
          ''')


# **Borrar Datos**
# 
# import sqlite3
# 
# conn = sqlite3.connect('my_database.sqlite')
# 
# cursor = conn.cursor()
# 
# conn.execute("DELETE from  Table where Campo = Valor")
# 
# conn.commit()
# 
# conn.close()

# In[26]:


conn.execute ("DELETE from products")
conn.commit()


# **Inserción de Valores**
# 
# import sqlite3
# 
# conn = sqlite3.connect('database.sqlite')
# 
# cursor = conn.cursor()
# 
# cursor.execute("INSERT INTO EMPLEADOS (ID,NAME,AGE) \
# 
#       VALUES (1, 'Razi', 14')");
#       
# cursor.execute("INSERT INTO EMPLEADOS (ID,NAME,AGE,ADDRESS,MARKS) \
# 
#       VALUES (2, 'Jon', 19, 'Bangalore', 150 )");
#       
# cursor.execute("INSERT INTO EMPLEADOS (ID,NAME,AGE) \
# 
#       VALUES (3, 'Martha', 35)");
#       
# conn.commit()
# 
# conn.close()

# In[27]:


c.execute('''
          INSERT INTO products (product_id, product_name, price)

                VALUES
                (1,'Computadora',800),
                (2,'Impresora',200),
                (3,'Tablet',300),
                (4,'Escritorio',450),
                (5,'Silla',150)
          ''')                     

conn.commit()


# In[29]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM products
                               ''', conn)

Tabla = pd.DataFrame(sql_query, columns = ['product_id', 'product_name', 'price'])
print (Tabla)


# In[30]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()
                 
c.execute('''
          SELECT
          *
          FROM products
          ''')

Tabla = pd.DataFrame(c.fetchall(), columns = ['product_id', 'product_name', 'price'])
print (Tabla)


# In[32]:


max_price = Tabla['price'].max()
print (max_price)


# In[33]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()
                 
c.execute('''
          SELECT
          *
          FROM productos
          ''')

Tabla = pd.DataFrame(c.fetchall(), columns = ['producto_id', 'producto_name', 'price'])

max_precio = Tabla['price'].max()
min_precio = Tabla['price'].min()
print (max_price)
print (min_precio)


# In[ ]:




