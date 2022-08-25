#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np


# # Question 6 solution : 

# Firstly lets get data for each  literacy group speaking how many languages so this data is available in 'DDW-C19-0000.xlsx' file which is mentioned in Assignment 2. So lets read it and then pre-process it to find literacy group wise language spoken data.

# In[2]:


Language_data = pd.read_excel('DDW-C19-0000.xlsx',usecols=['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 8'])
Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Area','Unnamed: 3':'TRU','Unnamed: 4':'Educational_level',
                                'Unnamed: 5':'People_speaking_2_or_more_languaguages',
                                'Unnamed: 8':'People_speaking_3_or_more_languaguages'}, inplace = True)
Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[(Language_data['TRU'] == 'Total') & (Language_data['Educational_level'] != 'Total')]
### Language_data = Language_data.sort_values('Area',ignore_index=True)
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","TRU"])
Language_data["Code"] = Language_data["Code"].astype(int)
# Language_data.head(10)


# We also want literacy group wise population data that in each literacy group how many peoples are there so lets fetch this data from 'DDW-0000C-08.xlsx' file and then pre-process it to find required data.

# In[3]:


population_data = pd.read_excel('DDW-0000C-08.xlsx',usecols=['Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 9',
                                                             'Unnamed: 12','Unnamed: 18','Unnamed: 21','Unnamed: 24',
                                                             'Unnamed: 27','Unnamed: 30','Unnamed: 33','Unnamed: 36',
                                                             'Unnamed: 39'])
population_data.rename(columns = {'Unnamed: 3':'Area','Unnamed: 4':'TRU','Unnamed: 5':'Age_Groups','Unnamed: 9':'Illiterate',
                                 'Unnamed: 12':'Literate','Unnamed: 18':'Literate but below primary',
                                  'Unnamed: 21':'Primary but below middle','Unnamed: 24':'Middle but below matric/secondary',
                                  'Unnamed: 39':'Temp'},
                                   inplace = True)
population_data['Matric/Secondary but below graduate'] = population_data['Unnamed: 27'] + population_data['Unnamed: 30'] + population_data['Unnamed: 33'] + population_data['Unnamed: 36']
population_data = population_data.drop(population_data.index[[0,1,2,3,4,5]])
population_data = population_data.loc[(population_data['TRU'] == 'Total') & (population_data['Age_Groups'] == 'All ages')]
population_data['Graduate and above'] = population_data['Temp']
population_data = population_data.reset_index()
population_data = population_data.drop(columns=["index","TRU","Age_Groups","Unnamed: 27","Unnamed: 30","Unnamed: 33","Unnamed: 36","Temp"])
population_data['Area'] = population_data.Area.str.replace('State - ?' , '')
population_data = population_data.set_index(['Area'])

# population_data = population_data.sort_values('Graduate_above',ignore_index=True)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(population_data)

# population_data.head(10)


# In[4]:


Processed_data = Language_data.copy()
Processed_data.at[0,'Total'] = 0
for i in Processed_data.index:
    area = Processed_data.iat[i,1]
    E_level = Processed_data.iat[i,2]
    Processed_data.iat[i,5] = population_data.at[area,E_level]
    
Processed_data = Processed_data[['Code','Area','Educational_level','Total','People_speaking_3_or_more_languaguages']]
Processed_data["Total"] = Processed_data["Total"].astype(int)
# Processed_data


# In[5]:


Processed_data['Percentage'] = (Processed_data['People_speaking_3_or_more_languaguages'] / Processed_data['Total']) * 100
# Processed_data


# In[6]:


temp_d1 = pd.DataFrame()
list = ['state/ut','Name','literacy-group','percentage']
temp_d2 = pd.DataFrame(columns=list)
pre_final = pd.DataFrame()
gb = Processed_data.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    percentage = temp_d1[["Percentage"]].to_numpy()
    max_p = np.argmax(percentage) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['literacy-group'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['percentage'] = temp_d1.at[max_p,'Percentage']
    pre_final = pre_final.append(temp_d2, ignore_index=True)
#     break
pre_final = pre_final.sort_values('state/ut',ignore_index=True)
# pre_final.head()


# In[7]:


pre_final.to_csv('literacy-india.csv')


# # Q6 Completed :)
