#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np


# # Question 9 solution : 

# Firstly lets get data for each  literacy group speaking how many languages so this data is available in 'DDW-C19-0000.xlsx' file which is mentioned in Assignment 2. So lets read it and then pre-process it to find literacy group wise language spoken data.

# In[2]:


Language_data = pd.read_excel('DDW-C19-0000.xlsx',usecols=['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 6',
                                                           'Unnamed: 7','Unnamed: 9','Unnamed: 10'])
Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Area','Unnamed: 3':'TRU','Unnamed: 4':'Educational_level',
                                'Unnamed: 6':'Male speaking 2 or more languaguages',
                                'Unnamed: 7':'Female speaking 2 or more languaguages',
                                'Unnamed: 9':'Male speaking 3 or more languaguages',
                                'Unnamed: 10':'Female speaking 3 or more languaguages',}, inplace = True)

Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[(Language_data['TRU'] == 'Total') & (Language_data['Educational_level'] != 'Total')]
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","TRU"])
Language_data["Code"] = Language_data["Code"].astype(int)
# Language_data.head(10)


# We also want literacy group wise population data that in each literacy group how many peoples are there so lets fetch this data from 'DDW-0000C-08.xlsx' file and then pre-process it to find required data.

# In[3]:


population_data = pd.read_excel('DDW-0000C-08.xlsx',usecols=['Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 10','Unnamed: 11',
                                                             'Unnamed: 13','Unnamed: 14','Unnamed: 19','Unnamed: 20','Unnamed: 22','Unnamed: 23','Unnamed: 25','Unnamed: 26',
                                                             'Unnamed: 28','Unnamed: 29','Unnamed: 31','Unnamed: 32','Unnamed: 34','Unnamed: 35','Unnamed: 37','Unnamed: 38',
                                                             'Unnamed: 40','Unnamed: 41'])
population_data.rename(columns = {'Unnamed: 3':'Area','Unnamed: 4':'TRU','Unnamed: 5':'Age_Groups','Unnamed: 10':'Illiterate (Males)','Unnamed: 11':'Illiterate (Females)',
                                 'Unnamed: 13':'Literate (Males)','Unnamed: 14':'Literate (Females)','Unnamed: 19':'Literate but below primary (Males)','Unnamed: 20':'Literate but below primary (Females)',
                                  'Unnamed: 22':'Primary but below middle (Males)','Unnamed: 23':'Primary but below middle (Females)','Unnamed: 25':'Middle but below matric/secondary (Males)','Unnamed: 26':'Middle but below matric/secondary (Females)',
                                  'Unnamed: 40':'Temp1','Unnamed: 41':'Temp2'},inplace = True)

population_data['Matric/Secondary but below graduate (Males)'] = population_data['Unnamed: 28'] + population_data['Unnamed: 31'] + population_data['Unnamed: 34'] + population_data['Unnamed: 37']
population_data['Matric/Secondary but below graduate (Females)'] = population_data['Unnamed: 29'] + population_data['Unnamed: 32'] + population_data['Unnamed: 35'] + population_data['Unnamed: 38']

population_data = population_data.drop(population_data.index[[0,1,2,3,4,5]])
population_data = population_data.loc[(population_data['TRU'] == 'Total') & (population_data['Age_Groups'] == 'All ages')]
population_data['Graduate and above (Males)'] = population_data['Temp1']
population_data['Graduate and above (Females)'] = population_data['Temp2']
population_data = population_data.reset_index()
population_data = population_data.drop(columns=["index","TRU","Age_Groups","Unnamed: 28","Unnamed: 29","Unnamed: 31","Unnamed: 32","Unnamed: 34","Unnamed: 35","Unnamed: 37","Unnamed: 38","Temp1","Temp2"])
population_data['Area'] = population_data.Area.str.replace('State - ?' , '')
population_data = population_data.set_index(['Area'])

# population_data = population_data.sort_values('Graduate_above',ignore_index=True)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(population_data)

# population_data.head(10)


# In[4]:


Processed_data = Language_data.copy()
Processed_data.at[0,'Total Males'] = 0
Processed_data.at[0,'Total Females'] = 0
for i in Processed_data.index:
    area = Processed_data.iat[i,1]
    E_level = Processed_data.iat[i,2]
    males = E_level + ' (Males)'
    females = E_level + ' (Females)'
    Processed_data.iat[i,7] = population_data.at[area,males]
    Processed_data.iat[i,8] = population_data.at[area,females]    
#     break
Processed_data["Total Males"] = Processed_data["Total Males"].astype(int)
Processed_data["Total Females"] = Processed_data["Total Females"].astype(int)

Processed_data['Males speaking exactly 1 languaguage'] = Processed_data['Total Males'] - Processed_data['Male speaking 2 or more languaguages']
Processed_data['Females speaking exactly 1 languaguage'] = Processed_data['Total Females'] - Processed_data['Female speaking 2 or more languaguages']

Processed_data['Males speaking exactly 2 languaguage'] = Processed_data['Male speaking 2 or more languaguages'] - Processed_data['Male speaking 3 or more languaguages']
Processed_data['Females speaking exactly 2 languaguage'] = Processed_data['Female speaking 2 or more languaguages'] - Processed_data['Female speaking 3 or more languaguages']

Processed_data = Processed_data[['Code','Area','Educational_level','Total Males','Males speaking exactly 1 languaguage',
                                 'Males speaking exactly 2 languaguage','Male speaking 3 or more languaguages',
                                  'Total Females','Females speaking exactly 1 languaguage','Females speaking exactly 2 languaguage',
                                   'Female speaking 3 or more languaguages']]
# Processed_data


# In[5]:


Processed_data['Ratio of 3 (Males)'] = Processed_data['Male speaking 3 or more languaguages'] / Processed_data['Total Males']
Processed_data['Ratio of 2 (Males)'] = Processed_data['Males speaking exactly 2 languaguage'] / Processed_data['Total Males']
Processed_data['Ratio of 1 (Males)'] = Processed_data['Males speaking exactly 1 languaguage'] / Processed_data['Total Males']

Processed_data['Ratio of 3 (Females)'] = Processed_data['Female speaking 3 or more languaguages'] / Processed_data['Total Females']
Processed_data['Ratio of 2 (Females)'] = Processed_data['Females speaking exactly 2 languaguage'] / Processed_data['Total Females']
Processed_data['Ratio of 1 (Females)'] = Processed_data['Females speaking exactly 1 languaguage'] / Processed_data['Total Females']

Processed_data = Processed_data[['Code','Area','Educational_level','Ratio of 1 (Males)','Ratio of 2 (Males)',
                                 'Ratio of 3 (Males)','Ratio of 1 (Females)','Ratio of 2 (Females)',
                                 'Ratio of 3 (Females)']]

# Processed_data


# ### So finally we processed data, now lets do what is asked in question :
# #### Part (a) :- Find the literacy group separately for males and females that has the highest ratio of population that can speak 3 or more languages.

# In[6]:


temp_d1 = pd.DataFrame()
list = ['state/ut','Name','literacy-group-males','ratio-males','literacy-group-females','ratio-females']
temp_d2 = pd.DataFrame(columns=list)
pre_final = pd.DataFrame()
gb = Processed_data.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 3 (Males)"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['literacy-group-males'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 3 (Males)']
    ratio = temp_d1[["Ratio of 3 (Females)"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['literacy-group-females'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 3 (Females)']
    pre_final = pre_final.append(temp_d2, ignore_index=True)
#     break
pre_final = pre_final.sort_values('state/ut',ignore_index=True)
# pre_final.head()


# #### Saving this in "literacy-gender-a.csv " as an output file.

# In[7]:


pre_final.to_csv('literacy-gender-a.csv')


# #### Part (b) :- Find the literacy group separately for males and females that has the highest ratio of population that speaks exactly 2 languages.

# In[8]:


pre_final1 = pd.DataFrame()
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 2 (Males)"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['literacy-group-males'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 2 (Males)']
    ratio = temp_d1[["Ratio of 2 (Females)"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['literacy-group-females'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 2 (Females)']
    pre_final1 = pre_final1.append(temp_d2, ignore_index=True)
#     break
pre_final1 = pre_final1.sort_values('state/ut',ignore_index=True)
# pre_final1.head()


# #### Saving this in "literacy-gender-b.csv " as an output file.

# In[9]:


pre_final1.to_csv('literacy-gender-b.csv')


# #### Part (c) :- Find the literacy group separately for males and females that has the highest ratio of population that can speak only 1 language.

# In[10]:


pre_final2 = pd.DataFrame()
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 1 (Males)"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['literacy-group-males'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 1 (Males)']
    ratio = temp_d1[["Ratio of 1 (Females)"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['literacy-group-females'] = temp_d1.at[max_p,'Educational_level']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 1 (Females)']
    pre_final2 = pre_final2.append(temp_d2, ignore_index=True)
#     break
pre_final2 = pre_final2.sort_values('state/ut',ignore_index=True)
# pre_final2.head()


# #### Saving this in "literacy-gender-c.csv " as an output file.

# In[11]:


pre_final2.to_csv('literacy-gender-c.csv')


# # Q9 Completed :)
