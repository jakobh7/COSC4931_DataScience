
# coding: utf-8

# In[8]:

#libraries
import pandas as pd
import numpy as np
import matplotlib
import cufflinks as cf
import plotly
plotly.offline.init_notebook_mode()
import plotly.offline as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

print(pd.__version__)


# In[2]:

#loading iris.csv
df = pd.read_csv('Gotham.csv',sep=",",header='infer')
df.head(5)


# In[6]:

jandf = df.loc[df['month'] == 1]
#jandf = jandf.loc[jandf['flow'] != NaN]
jandf.describe()


# In[7]:

dc = df.datecode.values
tmp = df.temp.values
flw = df.flow.values


# In[9]:

plt.plot(dc,tmp,"bo")
plt.xlabel("Datecode")
plt.ylabel("Temp")
plt.show()


# In[10]:

plt.plot(dc,flw,"bo")
plt.xlabel("Datecode")
plt.ylabel("Flow")
plt.show()


# In[11]:

jundf = df.loc[df['month'] == 6]
#jundf = jundf.loc[jundf['flow'] != NaN]
jundf.describe()


# In[ ]:



