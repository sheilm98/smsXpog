#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
# from sklearn.cluster import KMeans
import seaborn as sns
import mpld3
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.io as pio
# In[2]:


df = pd.read_csv('smsRadarPlot.csv')
df = df.dropna()


# In[3]:


df1 = pd.read_csv('pogradarPlot.csv')
df1 = df1.dropna()


# In[4]:

pio.renderers.default = 'png'
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
  r=df["Percentile"],
  theta=df["Statistic"],
  fill='toself', name='SMS'
))

fig.add_trace(go.Scatterpolar(
      r=df1["Percentile"],
      theta=df1["Statistic"],
      fill='toself',
      name='Pogba'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
#          range=[0, 1]
    ),
  ),
  showlegend=True,
  title="Comparing Milikovic-Savic and Pogba"

)
fig.update_layout(paper_bgcolor= '#000000')
fig.update_layout(polar_bgcolor='#1a3300')
fig.show()


# In[5]:


# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


# In[6]:


dfws = pd.read_csv("pogWS.csv")
dfws


# In[7]:


dfws1 = pd.read_csv("smsWs.csv")
dfws1


# In[8]:


fig,ax = plt.subplots(figsize=(13.5,8))
fig.set_facecolor('#333300')
ax.patch.set_facecolor('#333300')

pitch = Pitch(pitch_type='statsbomb', orientation='horizontal',
             pitch_color='#22312b', line_color='#c7d5cc', figsize=(16,11),
             constrained_layout=True, tight_layout=False)
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

mc = 'MC (Midfielder Centre)'
# if(dfws1['Position']== mc):
# SMS
# MC
plt.scatter(60,40, color='blue',s=dfws1['Apps'][0]*50,marker='h',label='sms@MC')

# Pogba
# MC
plt.scatter(60,40, color='red',s=dfws['Apps'][3]*80,label='MC',marker='s')

# Left wing
plt.scatter(100,70, color='red',s=dfws['Apps'][0]*80,label='LW')

# dm
plt.scatter(40,40, color='red',s=dfws['Apps'][1]*80,label='DM',marker='^')

plt.legend(fontsize=12)

# for x in range(len(dfws1['Rating'])):
#     if dfws1['Position'] == 'MC (Midfielder Centre)':
#         plt.scatter(0,0, color='blue',size=dfws1['Apps'])


# In[9]:


manU = pd.read_csv('mutd1.csv')
laz = pd.read_csv('lazio1.csv')
manU['Player'] = manU['Player'].str.split('\\').str[0]
laz['Player'] = laz['Player'].str.split('\\').str[0]
manU.head()


# In[10]:


pog = manU.loc[manU['Player'] == 'Paul Pogba']
sms = laz.loc[laz['Player'] == 'Sergej Milinković-Savić']
pog.squeeze()
sms.squeeze()


# In[11]:


sms = sms.drop(columns=['MP','Starts','90s'])
sms['Min'] = sms['Min']/90
sms


# In[12]:


pog = pog.drop(columns=['MP','Starts','90s'])
pog['Min'] = pog['Min']/90
pog


# In[13]:


# sms.columns
sms = sms.drop(columns=['Gls.1', 'Ast.1', 'G+A', 'G-PK.1', 'G+A-PK','xG.1', 'xA.1', 'xG+xA', 'npxG.1','npxG+xA.1','Matches'])
pog = pog.drop(columns=['Gls.1', 'Ast.1', 'G+A', 'G-PK.1', 'G+A-PK','xG.1', 'xA.1', 'xG+xA', 'npxG.1','npxG+xA.1','Matches'])


# In[19]:


from matplotlib.pyplot import figure


# In[24]:


# figure(figsize=(16, 32), dpi=150)
# sm1 = sms.plot.bar()
# pg1 = pog.plot.bar()
# plt.bar_label(sm1, label_type='edge')

