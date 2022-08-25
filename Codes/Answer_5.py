#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np


# # Question 5 solution : 

# ##### Reading language data from 'DDW-C18-0000.xlsx' file which is mentioned in Assignment 2 and then pre-processing it to find age wise language spoken data.

# In[2]:


Language_data=pd.read_excel('DDW-C18-0000.xlsx',usecols=['Unnamed: 0', 'Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 8'])

Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Area',
                                'Unnamed: 3':'TRU','Unnamed: 4':'Age_group','Unnamed: 5':'People_speaking_2_languaguages',
                                'Unnamed: 8':'People_speaking_3_languaguages'}, inplace = True)

Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[(Language_data['TRU'] == 'Total') & (Language_data['Age_group'] != 'Total')]
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","TRU"])

Language_data["Code"] = Language_data["Code"].astype(int)
# Language_data.head(20)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(Language_data)


# ##### Reading population data from 'DDW-0000C-13.xls' file which is mentioned in Assignment 2 and then pre-processing it to find age wise population data.

# In[3]:


population_data = pd.read_excel('DDW-0000C-13.xls',usecols=['Unnamed: 3','Unnamed: 4','Unnamed: 5'])
population_data.rename(columns = {'Unnamed: 3':'Area','Unnamed: 4':'Age_Groups','Unnamed: 5':'Total_Population'}, inplace = True)

population_data = population_data.loc[(population_data['Age_Groups'] != 'All ages') & (population_data['Age_Groups'] != 0)
                                     & (population_data['Age_Groups'] != 1) & (population_data['Age_Groups'] != 2) & 
                                     (population_data['Age_Groups'] != 3) & (population_data['Age_Groups'] != 4)]
# population_data = population_data.loc[(population_data['Area'] != 'India')]
population_data = population_data.drop(population_data.index[[0,1,2,3,4]])
population_data = population_data.reset_index()
population_data = population_data.drop(columns=["index"])
population_data['Area'] = population_data.Area.str.replace('State - ?' , '')
population_data['Area'] = population_data.Area.str.replace('India' , 'INDIA')
population_data['Area'] = population_data['Area'].str.split('(').str[0]
# population_data['Area'] = population_data.Area.str.replace('? - (' , '')
# population_data
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(population_data)


# In[4]:


population_data1 = population_data.copy()
list = ['Area','Age_Groups','Population']
temp = pd.DataFrame(columns=list)
pre_final = pd.DataFrame()
i = 0
while i < len(population_data):
    
    if population_data1.iat[i,1] in [30,50]:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '-' + str(population_data1.iat[i+19,1])
        temp['Age_Groups'] = age_group
        temp['Population'] = population_data1.iloc[i : i+20,2].sum(axis = 0)
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 20
        
    elif population_data1.iat[i,1] == 70:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '+'
        temp['Age_Groups'] = age_group
        temp['Population'] = population_data1.iloc[i : i+30,2].sum(axis = 0)
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 31
        
    elif population_data1.iat[i,1] == 'Age not stated':
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1])
        temp['Age_Groups'] = age_group
        temp['Population'] = population_data1.iat[i,2]
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 1
        
    else:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '-' + str(population_data1.iat[i+4,1])
        temp['Age_Groups'] = age_group
        temp['Population'] = population_data1.iloc[i : i+5,2].sum(axis = 0)
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 5

# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(pre_final)
# pre_final


# In[5]:


pre_final['Area'] = pre_final['Area'].str.strip()
Language_data['Area'] = Language_data['Area'].str.strip()
Processed_data = pd.merge(pre_final, Language_data, left_on = ['Area','Age_Groups'], right_on = ['Area','Age_group'])
Processed_data.head()
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(Processed_data)


# In[6]:


Processed_data1 = Processed_data.copy()
Processed_data1 = Processed_data1.drop(columns=["Age_group",'People_speaking_2_languaguages'])
Processed_data1['Percentage'] = (Processed_data1['People_speaking_3_languaguages'] / Processed_data1['Population']) * 100
# Processed_data1


# In[7]:


temp_d1 = pd.DataFrame()
list = ['state/ut','Name','age-group','percentage']
temp_d2 = pd.DataFrame(columns=list)
pre_final1 = pd.DataFrame()
gb = Processed_data1.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    percentage = temp_d1[["Percentage"]].to_numpy()
    max_p = np.argmax(percentage) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['age-group'] = temp_d1.at[max_p,'Age_Groups']
    temp_d2['percentage'] = temp_d1.at[max_p,'Percentage']
    pre_final1 = pre_final1.append(temp_d2, ignore_index=True)
#     break
pre_final1 = pre_final1.sort_values('state/ut',ignore_index=True)
# pre_final1.head()


# In[8]:


pre_final1.to_csv('age-india.csv')


# # Q5 Completed :)
