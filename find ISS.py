#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


pip install plotly


# In[2]:


import pandas as pd
import plotly.express as px


# In[3]:


URL = "http://api.open-notify.org/iss-now.json"


# In[4]:


df=pd.read_json(URL)


# In[5]:


df


# In[6]:


df['latitude']=df.loc['latitude', 'iss_position']
df['longitude']=df.loc['longitude', 'iss_position']
df.reset_index(inplace = True)


# In[7]:


df


# In[8]:


df = df.drop(['index', 'message'], axis=1)


# In[9]:


df


# In[10]:


fig = px.scatter_geo(df, lat= 'latitude', lon = 'longitude')
fig.show()


# In[ ]:





# In[ ]:




