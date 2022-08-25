#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd


# # Question 4 solution : 

# ##### Reading population data from 'DDW_PCA0000_2011_Indiastatedist.xlsx' file which was given in Assignment 1

# In[2]:


population_data= pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx',usecols=['Level','Name','TRU','TOT_P'])
population_data_Total = population_data.loc[(population_data['TRU'] == 'Total') & (population_data['Level'] == 'STATE')]
population_data_Total = population_data_Total.reset_index()
population_data_Total = population_data_Total.drop(columns=["index","Level","TRU"])
# overall_data = pd.DataFrame(columns=["Name","TOT_P"])
# overall_data['Name'] = ['1_INDIA']
# overall_data['TOT_P'] = population_data_Total['TOT_P'].sum()
# population_data_Total = population_data_Total.append(overall_data, ignore_index=True)

''' This we have done to add overall population i.e India's in the dataframe '''

population_data_Total = population_data_Total.sort_values('Name',ignore_index=True)
population_data_Total.loc[len(population_data_Total.index)] = ['INDIA', 1210854977]
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
Language_data["Code"] = Language_data["Code"].astype(str).astype(int)
Language_data = Language_data.sort_values('Code',ignore_index=True)
# Language_data.head(5)


# Since in Language_data dataframe, coloumn 'People_speaking_2_languaguages' also contains people who can speak 3 languages so to get no of peoples speaking exactly 2 languages we've to subtract first coloumn from second. Similarly we'll do for finding people speaking exactly 1 language..

# In[4]:


Processed_data = pd.merge(population_data_Total,Language_data,left_on='Name', right_on='Name')
Processed_data['TOT_A'] = Processed_data['TOT_P'] - Processed_data['People_speaking_2_languaguages']
Processed_data['People_speaking_2_languaguages'] -= Processed_data['People_speaking_3_languaguages']
Processed_data.rename(columns = {'TOT_A':'No_PSE_1_language',
                                 'People_speaking_2_languaguages':'No_PSE_2_language',
                                'People_speaking_3_languaguages':'No_PSE_3_language'}, inplace = True)
''' 
    No.PSE means Number of People Speaking Exactly
'''
Processed_data['3_to_2_Ratio'] = Processed_data['No_PSE_3_language'] / Processed_data['No_PSE_2_language']
Processed_data['2_to_1_Ratio'] = Processed_data['No_PSE_2_language'] / Processed_data['No_PSE_1_language']
# Processed_data.iat[0,0] = 'INDIA'
Processed_data = Processed_data[['Code','Name','3_to_2_Ratio','2_to_1_Ratio']]
Processed_data = Processed_data.sort_values('Code',ignore_index=True)
# Processed_data#.head(5)


# Now as we have 3-1 ratio and 2-1 ratio so first lets find  the top-3 states where the ratio of population speaking three languages or more to exactly two languages is the best and the worst-3 states as well.

# In[5]:


Processed_data1 = Processed_data.sort_values('3_to_2_Ratio',ascending=False,ignore_index=True).copy()
Processed_data2 = Processed_data.sort_values('2_to_1_Ratio',ascending=False,ignore_index=True).copy() 


# In[6]:


# display(Processed_data1.head())
# display(Processed_data2.head())
# Processed_data1


# In[7]:


_3_to_2_Ratio = Processed_data1.iloc[[0,1,2,35,34,33],0:3]
_3_to_2_Ratio = _3_to_2_Ratio.reset_index()
_3_to_2_Ratio = _3_to_2_Ratio.drop(columns=["index"])
# display(_3_to_2_Ratio)


# #### So now saving 3_to_2_Ratio and 2_to_1_Ratio dataframes as "3-to-2-ratio.csv" and "2-to-1-ratio.csv" respectively :-

# In[8]:


_3_to_2_Ratio.to_csv('3-to-2-ratio.csv')


# # Q4 Completed :)
