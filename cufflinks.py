#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cufflinks as cf
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd
import numpy as np
cf.go_offline()


# In[2]:


x1 =[1,2,3,4,5]
y1 = [10,20,30,40,50]
z1= [5,4,3,2,1]
dataset = pd.DataFrame({'id':x1,'name':y1,'remarks':z1})
dataset.iplot(kind='surface')


# In[3]:


df = pd.DataFrame(np.random.randn(200, 2), columns=['X', 'Y']).cumsum()
fig = df.iplot(asFigure=True, xTitle="The X Axis",
                    yTitle="The Y Axis", title="The Figure Title")
pyo.plot(fig,filename='timeseries.html')
fig.show()


# In[4]:


df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
fig = df.iplot(asFigure=True, kind="bar")
pyo.plot(fig,filename='bar.html')
fig.show()


# In[5]:


df = pd.DataFrame({'a': np.random.randn(500) + 1,'b': np.random.randn(500),'c': np.random.randn(500) - 1})
fig = df.iplot(asFigure=True, kind="histogram")
pyo.plot(fig,filename='histogram.html')
fig.show()


# In[6]:


fig = df.iplot(asFigure=True, kind="box")
pyo.plot(fig,filename='boxplot.html')
fig.show()


# In[7]:


df=cf.datagen.lines(5)
fig = df.iplot(asFigure=True, subplots=True, shape=(5,1), shared_xaxes=True, fill=True)
pyo.plot(fig,filename='timeseries.html')
fig.show()


# In[ ]:




