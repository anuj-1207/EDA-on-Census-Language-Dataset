#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
import scipy
from scipy import stats


# # Question 3 solution : 

# ##### Reading population data of males and females from 'DDW_PCA0000_2011_Indiastatedist.xlsx' file which was given in Assignment 1

# In[2]:


population_data = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx',usecols=['Level','Name','TRU','TOT_P'])
population_data_Total = population_data.loc[((population_data['TRU'] == 'Rural') | (population_data['TRU'] == 'Urban')) & (population_data['Level'] == 'STATE')]
population_data_Total = population_data_Total.reset_index()
population_data_Total = population_data_Total.drop(columns=["index","Level"])
population_data_Total.loc[len(population_data_Total.index)] = ['INDIA','Rural',833748852]
population_data_Total.loc[len(population_data_Total.index)] = ['INDIA','Urban',377106125]

population_data_Total = population_data_Total.sort_values('Name',ignore_index=True)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(population_data_Total)
# population_data_Total#.head()


# In[3]:


pre_final1 = pd.DataFrame()
pre_final1 = population_data_Total.reset_index().groupby(['Name', 'TRU'])['TOT_P'].aggregate('first').unstack()
pre_final1.reset_index(level=0, inplace=True)
# pre_final1["Rural"] = pre_final1["Rural"].astype(int)
# pre_final1["Urban"] = pre_final1["Urban"].astype(int)
pre_final1.columns=['Name','Rural','Urban']
# pre_final1


# In[4]:


# pre_final1.dtypes


# ##### Reading language data from 'DDW-C18-0000.xlsx' file which is mentioned in Assignment 2

# In[5]:


Language_data= pd.read_excel('DDW-C18-0000.xlsx',usecols=['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 8'])
Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Name','Unnamed: 3':'TRU','Unnamed: 4':'Age_group',
                                'Unnamed: 5':'People speaking 2 or more languaguages',
                                'Unnamed: 8':'People speaking 3 or more languaguages',}, inplace = True)

Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[((Language_data['TRU'] == 'Rural') | (Language_data['TRU'] == 'Urban')) & (Language_data['Age_group'] == 'Total')]
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","Age_group"])
# Language_data = Language_data.sort_values('Code',ignore_index=True)
Language_data["Code"] = Language_data["Code"].astype(int)

Language_data = Language_data.sort_values('Code',ignore_index=True)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(Language_data)
# Language_data.head(5)


# In[6]:


list = ['Code','Name','People speaking 2 or more languaguages (Rural)','People speaking 2 or more languaguages (Urban)','People speaking 3 or more languaguages (Rural)','People speaking 3 or more languaguages (Urban)']
temp_d3 = pd.DataFrame(columns=list)
pre_final2 = pd.DataFrame()
i = 0
while i < len(Language_data.index):
    temp_d3['Code'] = [Language_data.iat[i,0]]    
    temp_d3['Name'] = [Language_data.iat[i,1]]
    temp_d3['People speaking 2 or more languaguages (Rural)'] = Language_data.iat[i,3]
    temp_d3['People speaking 2 or more languaguages (Urban)'] = Language_data.iat[i+1,3]
    temp_d3['People speaking 3 or more languaguages (Rural)'] = [Language_data.iat[i,4]]
    temp_d3['People speaking 3 or more languaguages (Urban)'] = [Language_data.iat[i+1,4]]    
#     pre_final2 = pre_final2.append(temp_d3, ignore_index=True)
    if i == 69:
        i += 1
    else: 
        i += 2
#     break
pre_final2 = Language_data.reset_index().groupby(['Code','Name','TRU'])[['People speaking 2 or more languaguages','People speaking 3 or more languaguages']].aggregate('first').unstack()
pre_final2 = pre_final2.reset_index()
pre_final2.columns = ['Code','Name','People speaking 2 or more languaguages (Rural)','People speaking 2 or more languaguages (Urban)','People speaking 3 or more languaguages (Rural)','People speaking 3 or more languaguages (Urban)']
pre_final2["Code"] = pre_final2["Code"].astype(str).astype(int)
pre_final2 = pre_final2.sort_values('Code',ignore_index=True)
# pre_final2#.head()


# In[7]:


Processed_data = pd.merge(pre_final1,pre_final2,left_on = 'Name', right_on = 'Name')

# Processed_data['TOT_A'] = Processed_data['TOT_P'] - Processed_data['People_speaking_2_languaguages']
# Processed_data['People_speaking_2_languaguages'] -= Processed_data['People_speaking_3_languaguages']
# Processed_data.rename(columns = {'TOT_A':'No_PSE_1_language',
#                                  'People_speaking_2_languaguages':'No_PSE_2_language',
#                                 'People_speaking_3_languaguages':'No_PSE_3_language'}, inplace = True)
''' 
    No.PSE means Number of People Speaking Exactly
'''
# Processed_data.iat[0,0] = 'INDIA'
# Processed_data = Processed_data[['Name','TOT_P','No_PSE_1_language','No_PSE_2_language','No_PSE_3_language']]
Processed_data = Processed_data.sort_values('Code',ignore_index=True)
# Processed_data.head(5)


# In[8]:


Processed_Data = Processed_data.copy()

Processed_Data['Percentage rural speaking only 1 language'] = ((Processed_Data['Rural'] - Processed_Data['People speaking 2 or more languaguages (Rural)']) / Processed_Data['Rural']) * 100
Processed_Data['Percentage rural speaking exactly 2 language'] = ((Processed_Data['People speaking 2 or more languaguages (Rural)'] - Processed_Data['People speaking 3 or more languaguages (Rural)']) / Processed_Data['Rural']) * 100
Processed_Data['Percentage rural speaking 3 or more languaguages'] = ((Processed_Data['People speaking 3 or more languaguages (Rural)']) / Processed_Data['Rural']) * 100

Processed_Data['Percentage urban speaking only 1 language'] = ((Processed_Data['Urban'] - Processed_Data['People speaking 2 or more languaguages (Urban)']) / Processed_Data['Urban']) * 100
Processed_Data['Percentage urban speaking exactly 2 language'] = ((Processed_Data['People speaking 2 or more languaguages (Urban)'] - Processed_Data['People speaking 3 or more languaguages (Urban)']) / Processed_Data['Urban']) * 100
Processed_Data['Percentage urban speaking 3 or more languaguages'] = (Processed_Data['People speaking 3 or more languaguages (Urban)'] / Processed_Data['Urban']) * 100

Processed_Data['ratio_1'] = (Processed_Data['Urban'] - Processed_Data['People speaking 2 or more languaguages (Urban)']) / (Processed_Data['Rural']-Processed_Data['People speaking 2 or more languaguages (Rural)'])
Processed_Data['ratio_2'] = (Processed_Data['People speaking 2 or more languaguages (Urban)'] - Processed_Data['People speaking 3 or more languaguages (Urban)']) / (Processed_Data['People speaking 2 or more languaguages (Rural)'] - Processed_Data['People speaking 3 or more languaguages (Rural)'])
Processed_Data['ratio_3'] = Processed_Data['People speaking 3 or more languaguages (Urban)'] / Processed_Data['People speaking 3 or more languaguages (Rural)']
Processed_Data['ratio_pop'] = Processed_Data['Urban'] / Processed_Data['Rural']

Processed_Data['p-value'] = Processed_Data.apply(lambda row: scipy.stats.ttest_1samp([row.ratio_1, row.ratio_2, row.ratio_3], popmean=row.ratio_pop)[1], axis=1)

Processed_Data = Processed_Data[['Code','Name','Percentage rural speaking only 1 language',
                                 'Percentage urban speaking only 1 language',
                                 'Percentage rural speaking exactly 2 language',
                                 'Percentage urban speaking exactly 2 language',
                                 'Percentage rural speaking 3 or more languaguages',
                                 'Percentage urban speaking 3 or more languaguages','p-value']]
                                                                       
# Processed_Data#.head()


# In[9]:



final_1 = Processed_Data[['Code','Name','Percentage rural speaking only 1 language','Percentage urban speaking only 1 language','p-value']].copy()
final_2 = Processed_Data[['Code','Name','Percentage rural speaking exactly 2 language','Percentage urban speaking exactly 2 language','p-value']].copy()
final_3 = Processed_Data[['Code','Name','Percentage rural speaking 3 or more languaguages','Percentage urban speaking 3 or more languaguages','p-value']].copy()

final_1.columns=['State_code','Name','rural-percentage','urban-percentage','p-value']
final_2.columns=['State_code','Name','rural-percentage','urban-percentage','p-value']
final_3.columns=['State_code','Name','rural-percentage','urban-percentage','p-value']

final_1.to_csv('gender-india-a.csv')
final_2.to_csv('gender-india-b.csv')
final_3.to_csv('gender-india-c.csv')


# ## Q3 Completed..:)
