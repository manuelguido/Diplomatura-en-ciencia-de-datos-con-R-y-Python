#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import snowflake.connector


# Conexión a la Base de datos
conn = snowflake.connector.connect(
                user='Usuario',
                password='Clave',
                account='Servidor',http....
                mbre del Warehouse',
                database='Nombre de la base de datos',
                schema='Nombrwarehouse='Noe del esquema'
                )

# Creación del Cursor
cur = conn.cursor()

# Ejecución del Select 
cur.execute("select * from nombre de la tabla;")
pd_df = cur.fetch_pandas_all()

