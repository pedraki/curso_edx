#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
print(os.getcwd())


# In[5]:


import pandas as pd
fichero=os.path.join(os.getcwd(),'datasets\\avocado.csv')
df=pd.read_csv(fichero)
 


# In[9]:


# saca el numero de filas que se le indica
df.head(3)
# lo mismo pero las ultimas
df.tail(2)


# In[11]:


#referirmos a una sola columna
df['AveragePrice'].head(2)


# In[14]:


#[df['region']=='Albany' devuelve True o False
# si cumple la condicion
#usandolo podemos crear un df con los de albany
df_albany=df[df['region']=='Albany']
df_albany.head(2)


# In[19]:


#la primera columna es el indice
df_albany.index


# In[28]:


#cambiar el orden, orden no str? devuelve otro dataframe ojo
# en el que el orden pasa a ser por fecha, puede ser el mismo
#df_albany=df_albany.set_index('Date')
#o df_albany.set_index('Date',inplace=True)
df2=df_albany.set_index('Date')


# In[35]:


#plotea con la columna index como eje X
df2['AveragePrice'].plot()


# In[ ]:




