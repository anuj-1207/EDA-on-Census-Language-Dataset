#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np


# ## Lets divide India into 6 regions and do for each region separately. 

# In[2]:


Output_1 = pd.DataFrame(columns=['region','language-1','language-2','language-3'])
Output_2 = pd.DataFrame(columns=['region','language-1','language-2','language-3'])
Output_a = pd.DataFrame()
Output_b = pd.DataFrame()


# ### Northern Region

# In[3]:


location = './Q7_Dataset/North/'
extension = '.xlsx'


# In[4]:


overall = pd.DataFrame()
mother_tongue= pd.DataFrame()

for i in range(1,8):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'North'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'North'
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'North'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'North'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'North'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# ### Western Region

# In[5]:


location = './Q7_Dataset/West/'


# In[6]:


overall = pd.DataFrame()
mother_tongue = pd.DataFrame()

for i in range(23,29):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'West'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'West'
    overall = overall.append(language_data, ignore_index=True)

    language_data=lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data=language_data.dropna()
    language_data.columns=['Language', 'Total']
    language_data['Region']='West'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'West'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'West'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# ### Central Region

# In[7]:


location = './Q7_Dataset/Central/'


# In[8]:


overall = pd.DataFrame()
mother_tongue = pd.DataFrame()

for i in range(1,4):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'Central'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'Central'
    overall = overall.append(language_data, ignore_index=True)

    language_data=lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data=language_data.dropna()
    language_data.columns=['Language', 'Total']
    language_data['Region']='Central'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'Central'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'Central'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# ### Eastern Region

# In[9]:


location = './Q7_Dataset/East/'


# In[10]:


overall = pd.DataFrame()
mother_tongue = pd.DataFrame()

for i in range(1,5):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'East'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'East'
    overall = overall.append(language_data, ignore_index=True)

    language_data=lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data=language_data.dropna()
    language_data.columns=['Language', 'Total']
    language_data['Region']='East'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'East'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'East'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# ### Southern Region

# In[11]:


location = './Q7_Dataset/South/'


# In[12]:


overall = pd.DataFrame()
mother_tongue = pd.DataFrame()

for i in range(29,35):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'South'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'South'
    overall = overall.append(language_data, ignore_index=True)

    language_data=lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data=language_data.dropna()
    language_data.columns=['Language', 'Total']
    language_data['Region']='South'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'South'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'South'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# ### North Eastern Region

# In[13]:


location = './Q7_Dataset/North_East/'


# In[14]:


overall = pd.DataFrame()
mother_tongue = pd.DataFrame()

for i in range(11,20):
    file_name = location + str(i) + extension
    lang_data_original = pd.read_excel(file_name)
    lang_data_original.drop(1,inplace=True)
    lang_data_original.drop(2,inplace=True)
    lang_data_original.drop(3,inplace=True)
    lang_data_original.drop(4,inplace=True)
    
    language_data = lang_data_original[['Unnamed: 3','Unnamed: 4']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'North-East'
    mother_tongue = mother_tongue.append(language_data, ignore_index=True)
    overall = overall.append(language_data, ignore_index=True)

    language_data = lang_data_original[['Unnamed: 8','Unnamed: 9']].copy()
    language_data = language_data.dropna()
    language_data.columns = ['Language', 'Total']
    language_data['Region'] = 'North-East'
    overall = overall.append(language_data, ignore_index=True)

    language_data=lang_data_original[['Unnamed: 13','Unnamed: 14']].copy()
    language_data=language_data.dropna()
    language_data.columns=['Language', 'Total']
    language_data['Region']='North-East'
    overall = overall.append(language_data, ignore_index=True)
    
aggregation = {'Total': 'sum'}
overall = overall.groupby(overall['Language'],as_index=False).aggregate(aggregation).reindex(columns = overall.columns)
overall['Region'] = 'North-East'
overall = overall.sort_values(['Total'], ascending=[False])
overall = overall.reset_index()
overall.drop('index',axis=1,inplace=True)

mother_tongue = mother_tongue.groupby(mother_tongue['Language'],as_index=False).aggregate(aggregation).reindex(columns = mother_tongue.columns)
mother_tongue['Region'] = 'North-East'
mother_tongue = mother_tongue.sort_values(['Total'], ascending=[False])
mother_tongue = mother_tongue.reset_index()
mother_tongue.drop('index',axis=1,inplace=True)

Output_1['region'] = [mother_tongue.iat[0,2]]
Output_1['language-1'] = mother_tongue.iat[0,0]
Output_1['language-2'] = mother_tongue.iat[1,0]
Output_1['language-3'] = mother_tongue.iat[2,0]

Output_2['region'] = [overall.iat[0,2]]
Output_2['language-1'] = overall.iat[0,0]
Output_2['language-2'] = overall.iat[1,0]
Output_2['language-3'] = overall.iat[2,0]

Output_a = Output_a.append(Output_1, ignore_index=True)
Output_b = Output_b.append(Output_2, ignore_index=True)


# In[15]:


Output_a.to_csv('region-india-a.csv')
Output_b.to_csv("region-india-b.csv")


# # Q7 Completed :)
