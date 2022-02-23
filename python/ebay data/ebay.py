#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# import relevant data
ebay = pd.read_csv('C:/Users/15165/Documents/531 licenses/ebay 531 cleaned python.csv')


# In[2]:


ebay.head()


# In[10]:


import numpy as np; np.random.seed()
import seaborn as sns; sns.set_theme()
uniform_data = ebay
ax = sns.heatmap(uniform_data, vmin=0, vmax=1)


# In[20]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[23]:


ebay.corr()


# In[24]:


sns.heatmap(ebay.corr());


# In[26]:


sns.heatmap(ebay.corr())
plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(ebay.corr(), vmin=-1, vmax=1, annot=True,cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);


# In[ ]:




