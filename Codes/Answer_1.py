#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd


# ##### Reading population data from 'DDW_PCA0000_2011_Indiastatedist.xlsx' file which was given in Assignment 1

# In[2]:


population_data= pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx',usecols=['Level','Name','TRU','TOT_P'])
population_data_Total = population_data.loc[(population_data['TRU'] == 'Total') & (population_data['Level'] == 'STATE')]
population_data_Total = population_data_Total.reset_index()
population_data_Total = population_data_Total.drop(columns=["index","Level","TRU"])
overall_data = pd.DataFrame(columns=["Name","TOT_P"])
overall_data['Name'] = ['INDIA']
overall_data['TOT_P'] = population_data_Total['TOT_P'].sum()
population_data_Total = population_data_Total.append(overall_data, ignore_index=True)

''' This we have done to add overall population i.e India's in the dataframe '''

population_data_Total = population_data_Total.sort_values('Name',ignore_index=True)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     print(population_data_Total)
# population_data_Total.head()


# ##### Reading language data from 'DDW-C18-0000.xlsx' file which is mentioned in Assignment 2

# In[3]:


Language_data= pd.read_excel('DDW-C18-0000.xlsx',usecols=['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 8'])
Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Name','Unnamed: 3':'TRU','Unnamed: 4':'Age_group',
                                'Unnamed: 5':'People_speaking_2_languaguages',
                                'Unnamed: 8':'People_speaking_3_languaguages'}, inplace = True)

Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[(Language_data['TRU'] == 'Total') & (Language_data['Age_group'] == 'Total')]
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","TRU","Age_group"])
# Language_data.iat[0,0] = 'INDIA'
Language_data = Language_data.sort_values('Code',ignore_index=True)
Language_data["Code"] = Language_data["Code"].astype(int)
# Language_data.head(5)


# In[4]:


# People_speaking_exactly_1_language
# population_data_Total


# Since in Language_data dataframe, coloumn 'People_speaking_2_languaguages' also contains people who can speak 3 languages so to get no of peoples speaking exactly 2 languages we've to subtract first coloumn from second. Similarly we'll do for finding people speaking exactly 1 language..

# In[5]:


Processed_data = pd.merge(population_data_Total,Language_data,left_on = 'Name', right_on = 'Name')
Processed_data['TOT_A'] = Processed_data['TOT_P'] - Processed_data['People_speaking_2_languaguages']
Processed_data['People_speaking_2_languaguages'] -= Processed_data['People_speaking_3_languaguages']
Processed_data.rename(columns = {'Code':'state-code','TOT_A':'No_PSE_1_language',
                                 'People_speaking_2_languaguages':'No_PSE_2_language',
                                'People_speaking_3_languaguages':'No_PSE_3_language'}, inplace = True)
''' 
    No.PSE means Number of People Speaking Exactly
'''
Processed_data.iat[0,0] = 'INDIA'
Processed_data = Processed_data[['state-code','Name','TOT_P','No_PSE_1_language','No_PSE_2_language','No_PSE_3_language']]
Processed_data = Processed_data.sort_values('state-code',ignore_index=True)
# Processed_data.head(5)


# In[6]:


# state-code, percent-one,
# percent-two, percent-three
Processed_data1 = Processed_data.copy() 
Processed_data1['percent-one'] = (Processed_data1['No_PSE_1_language'] / Processed_data1['TOT_P']) * 100
Processed_data1['percent-two'] = (Processed_data1['No_PSE_2_language'] / Processed_data1['TOT_P']) * 100
Processed_data1['percent-three'] = (Processed_data1['No_PSE_3_language'] / Processed_data1['TOT_P']) * 100
Processed_data1 = Processed_data1[['state-code','Name','percent-one','percent-two','percent-three']]
# Processed_data1


# In[7]:


Processed_data1.to_csv('percent-india.csv')


# ## Q1 Completed..:)
