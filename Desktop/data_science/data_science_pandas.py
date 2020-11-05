#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[15]:


pd.read_csv('Desktop/data_science/aula0/ratings.csv')


# In[16]:


notas = pd.read_csv('Desktop/data_science/aula0/ratings.csv')  # atribuindo o aruivo csv a variavel notas...


# In[17]:


notas.head(5) # verificando os cinco primeiros itens do dataframe...


# In[18]:


notas.shape  # verificando a quantidade de itens e o numero de colunas...


# In[19]:


notas.columns = ['Id_usuario', 'Id_filme', 'nota', 'momento']  # redefine o nome da coluna...


# In[20]:


notas.head()


# In[21]:


notas.nota # verificando itens de uma só coluna...


# In[23]:


notas['nota'].unique() # verifica os valores dentro da coluna...


# In[24]:


notas['nota'].value_counts() # contando a quantidade de cada valor


# In[26]:


notas['nota'].mean()  # verificando a media dos valores


# In[ ]:




