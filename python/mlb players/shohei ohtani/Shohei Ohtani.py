#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install pybaseball -q')


# In[2]:


import pybaseball as pyb


# In[51]:


pyb.playerid_lookup('ohtani', 'shohei')


# In[60]:


#make start date and end date
start_date = '2021-06-23'
end_date = '2021-07-23'

#name df so(shohei ohtani)_df
so_df = pyb.statcast_batter(start_date, end_date, 660271)

#show shape
so_df.shape


# In[61]:


#dataframe for homegames, where the LA angels were home
home_so_df = so_df.loc[so_df['home_team'] == 'LAA']

#show shape
home_so_df.shape


# In[62]:


pyb.spraychart(home_so_df, 'angels', title='Shohei Ohtani June 23rd - July 23rd 2021')


# In[69]:


pyb.spraychart(home_so_df, 'angels', title='Shohei Ohtani June 23rd - July 23rd 2021',colorby='pitch_type')


# In[ ]:




