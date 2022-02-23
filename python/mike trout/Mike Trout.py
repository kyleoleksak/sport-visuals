#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import pybaseball as pyb


# In[8]:


stadium = pd.read_csv('https://raw.githubusercontent.com/jldbc/pybaseball/master/pybaseball/data/mlbstadiums.csv')

stadium['y'] = stadium['y'] * -1
stadium = stadium.loc[:,'team':]

stadium.head()


# In[9]:


def plot_stadium(team, color):

    team_df = stadium[stadium['team'] == team.lower()]
    for i in stadium['segment'].unique():
        data = team_df[team_df['segment'] == i]
        plt.plot(data['x'],data['y'], linestyle = '-', color = color)
    plt.suptitle(team.capitalize(), y=1.01, fontsize=15)
    plt.title(team_df['location'].any(), fontsize=10)
    plt.axis('off');


# In[10]:


pyb.playerid_lookup('trout', 'mike')


# In[18]:


start_date = '2019-03-23'
end_date = '2019-11-23'

trout_df = pyb.statcast_batter(start_date, end_date, 545361)

home_trout_df = trout_df.loc[trout_df['home_team'] == 'LAA']

HR_LAA = home_trout_df[home_trout_df['events'] == 'home_run']


# In[19]:


plot_stadium('yankees','navy')
plot_stadium('angels','crimson')

plt.plot(HR_LAA['hc_x'],HR_LAA['hc_y']*-1, 'o',color= 'black')

plt.suptitle(None)
plt.title('Yankees (Navy) and Angels (Crimson)',fontsize = 15);


# In[ ]:




