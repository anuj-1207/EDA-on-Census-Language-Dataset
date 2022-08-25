#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries that will be useful :-

# In[1]:


import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np


# # Question 8 solution : 

# ##### Reading language data from 'DDW-C18-0000.xlsx' file which is mentioned in Assignment 2 and then pre-processing it to find age wise language spoken data.

# In[2]:


Language_data=pd.read_excel('DDW-C18-0000.xlsx',usecols=['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4',
                                                         'Unnamed: 6','Unnamed: 7','Unnamed: 9','Unnamed: 10'])

Language_data.rename(columns = {'Unnamed: 0':'Code','Unnamed: 2':'Area',
                                'Unnamed: 3':'TRU','Unnamed: 4':'Age Groups','Unnamed: 6':'Male speaking 2 languaguages',
                                'Unnamed: 7':'Female speaking 2 languaguages','Unnamed: 9':'Male speaking 3 or more languaguages',
                                    'Unnamed: 10':'Female speaking 3 or more languaguages'}, inplace = True)

Language_data = Language_data.drop(Language_data.index[[0,1,2,3,4]])
Language_data = Language_data.loc[(Language_data['TRU'] == 'Total') & (Language_data['Age Groups'] != 'Total')]
Language_data = Language_data.reset_index()
Language_data = Language_data.drop(columns=["index","TRU"])
Language_data["Code"] = Language_data["Code"].astype(int)

Language_data = Language_data.sort_values('Code',ignore_index=True)
# Language_data#.head(20)
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(Language_data)


# ##### Reading population data from 'DDW-0000C-13.xls' file which is mentioned in Assignment 2 and then pre-processing it to find age and gender wise population data.

# In[3]:


population_data = pd.read_excel('DDW-0000C-13.xls',usecols=['Unnamed: 3','Unnamed: 4','Unnamed: 6','Unnamed: 7'])
population_data.rename(columns = {'Unnamed: 3':'Area','Unnamed: 4':'Age Groups','Unnamed: 6':'Male total Population',
                                  'Unnamed: 7':'Female total Population'}, inplace = True)

population_data = population_data.loc[(population_data['Age Groups'] != 'All ages') & (population_data['Age Groups'] != 0)
                                     & (population_data['Age Groups'] != 1) & (population_data['Age Groups'] != 2) & 
                                     (population_data['Age Groups'] != 3) & (population_data['Age Groups'] != 4)]
# population_data = population_data.loc[(population_data['Area'] != 'India')]
population_data = population_data.drop(population_data.index[[0,1,2,3,4]])
population_data = population_data.reset_index()
population_data = population_data.drop(columns=["index"])
population_data['Area'] = population_data.Area.str.replace('State - ?' , '')
population_data['Area'] = population_data.Area.str.replace('India' ,'INDIA')
population_data['Area'] = population_data['Area'].str.split('(').str[0]
# population_data['Area'] = population_data.Area.str.replace('? - (' , '')
# population_data
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(population_data)


# In[4]:


population_data1 = population_data.copy()
list = ['Area','Age Groups','Male population','Female population']
temp = pd.DataFrame(columns=list)
pre_final = pd.DataFrame()
i = 0
while i < len(population_data):
    
    if population_data1.iat[i,1] in [30,50]:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '-' + str(population_data1.iat[i+19,1])
        temp['Age Groups'] = age_group
        temp['Male population'] = population_data1.iloc[i : i+20,2].sum(axis = 0)
        temp['Female population'] = population_data1.iloc[i : i+20,3].sum(axis = 0)        
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 20
        
    elif population_data1.iat[i,1] == 70:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '+'
        temp['Age Groups'] = age_group
        temp['Male population'] = population_data1.iloc[i : i+30,2].sum(axis = 0)
        temp['Female population'] = population_data1.iloc[i : i+30,3].sum(axis = 0)        
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 31
        
    elif population_data1.iat[i,1] == 'Age not stated':
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1])
        temp['Age Groups'] = age_group
        temp['Male population'] = population_data1.iat[i,2]
        temp['Female population'] = population_data1.iat[i,3]        
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 1
        
    else:
        temp['Area'] = [population_data1.iat[i,0]]
        age_group = str(population_data1.iat[i,1]) + '-' + str(population_data1.iat[i+4,1])
        temp['Age Groups'] = age_group
        temp['Male population'] = population_data1.iloc[i : i+5,2].sum(axis = 0)
        temp['Female population'] = population_data1.iloc[i : i+5,3].sum(axis = 0)        
        pre_final = pre_final.append(temp, ignore_index=True)
        i += 5

# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(pre_final)
# pre_final


# In[5]:


pre_final['Area'] = pre_final['Area'].str.strip()
Language_data['Area'] = Language_data['Area'].str.strip()
Processed_data = pd.merge(pre_final, Language_data, left_on = ['Area','Age Groups'], right_on = ['Area','Age Groups'])
# Processed_data
# with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 4,):
#     display(Processed_data)


# So now we need to find males and females in all age groups who are speaking exactly one, exactly 2 and 3 or more languages so lets do that. 

# In[6]:


Processed_data1 = Processed_data.copy()
# Processed_data1['Percentage'] = (Processed_data1['People_speaking_3_languaguages'] / Processed_data1['Population']) * 100
# Processed_data1

Processed_data1['Males speaking exactly 1 languaguages'] = Processed_data1['Male population'] - Processed_data1['Male speaking 2 languaguages']
Processed_data1['Males speaking exactly 2 languaguages'] = Processed_data1['Male speaking 2 languaguages'] - Processed_data1['Male speaking 3 or more languaguages']

Processed_data1['Females speaking exactly 1 languaguages'] = Processed_data1['Female population'] - Processed_data1['Female speaking 2 languaguages']
Processed_data1['Females speaking exactly 2 languaguages'] = Processed_data1['Female speaking 2 languaguages'] - Processed_data1['Female speaking 3 or more languaguages']

# Processed_data1


# In[7]:


Processed_data1 = Processed_data1.drop(columns=["Male speaking 2 languaguages","Female speaking 2 languaguages"])


# In[8]:


# Processed_data1 = Processed_data1.drop(Processed_data1.index[[0,1,2,3,4]])
Processed_data1 = Processed_data1[['Code','Area','Age Groups','Male population','Males speaking exactly 1 languaguages',
                                   'Males speaking exactly 2 languaguages','Male speaking 3 or more languaguages',
                                   'Female population','Females speaking exactly 1 languaguages',
                                   'Females speaking exactly 2 languaguages',
                                   'Female speaking 3 or more languaguages']]
Processed_data1["Code"] = pd.to_numeric(Processed_data1["Code"])
# Processed_data1


# In[9]:


Processed_data1['Ratio of 3 Male'] = Processed_data1['Male speaking 3 or more languaguages'] / Processed_data1['Male population'] 
Processed_data1['Ratio of 2 Male'] = Processed_data1['Males speaking exactly 2 languaguages'] / Processed_data1['Male population'] 
Processed_data1['Ratio of 1 Male'] = Processed_data1['Males speaking exactly 1 languaguages'] / Processed_data1['Male population'] 

Processed_data1['Ratio of 3 Female'] = Processed_data1['Female speaking 3 or more languaguages'] / Processed_data1['Female population'] 
Processed_data1['Ratio of 2 Female'] = Processed_data1['Females speaking exactly 2 languaguages'] / Processed_data1['Female population'] 
Processed_data1['Ratio of 1 Female'] = Processed_data1['Females speaking exactly 1 languaguages'] / Processed_data1['Female population']
# Processed_data1


# In[10]:


Processed_data2 = Processed_data1.copy()
Processed_data2 = Processed_data2.drop(columns=['Male population','Female population','Male speaking 3 or more languaguages',
                                                'Males speaking exactly 2 languaguages','Males speaking exactly 1 languaguages',
                                                'Female speaking 3 or more languaguages','Females speaking exactly 2 languaguages',
                                                'Females speaking exactly 1 languaguages'])
# Processed_data2


# ### So finally we processed data, now lets do what is asked in question :
# #### Part (a) :- Find the age group separately for males and females that has the highest ratio of population that can speak 3 or more languages.

# In[11]:


temp_d1 = pd.DataFrame()
list = ['state/ut','Name','age-group-males','ratio-males','age-group-females','ratio-females']
temp_d2 = pd.DataFrame(columns=list)
pre_final1 = pd.DataFrame()
gb = Processed_data2.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 3 Male"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['age-group-males'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 3 Male']
    ratio = temp_d1[["Ratio of 3 Female"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['age-group-females'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 3 Female']
    pre_final1 = pre_final1.append(temp_d2, ignore_index=True)
#     break
pre_final1 = pre_final1.sort_values('state/ut',ignore_index=True)
# pre_final1.head()


# #### Saving this in "age-gender-a.csv" as an output file.

# In[12]:


pre_final1.to_csv('age-gender-a.csv')


# #### Part (b) :- Find the age group separately for males and females that has the highest ratio of population that can speak exactly 2 languages.

# In[13]:


# temp_d1 = pd.DataFrame()
# list = ['state/ut','Name','age-group-males','ratio-males','age-group-females','ratio-females']
# temp_d2 = pd.DataFrame(columns=list)
pre_final2 = pd.DataFrame()
# gb = Processed_data2.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 2 Male"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['age-group-males'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 2 Male']
    ratio = temp_d1[["Ratio of 2 Female"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['age-group-females'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 2 Female']
    pre_final2 = pre_final2.append(temp_d2, ignore_index=True)
#     break
pre_final2 = pre_final2.sort_values('state/ut',ignore_index=True)
# pre_final2.head()


# #### Saving this in "age-gender-b.csv" as an output file.

# In[14]:


pre_final2.to_csv('age-gender-b.csv')


# #### Part (c) :- Find the age group separately for males and females that has the highest ratio of population that can speak only 1 language.

# In[15]:


# temp_d1 = pd.DataFrame()
# list = ['state/ut','Name','age-group-males','ratio-males','age-group-females','ratio-females']
# temp_d2 = pd.DataFrame(columns=list)
pre_final3 = pd.DataFrame()
# gb = Processed_data2.groupby(['Area'])
for x in gb.groups:
    temp_d1 = gb.get_group(x)
    temp_d1 = temp_d1.reset_index()
    ratio = temp_d1[["Ratio of 1 Male"]].to_numpy()
    max_p = np.argmax(ratio) 
    temp_d2['state/ut'] = [temp_d1.at[max_p,'Code']]
    temp_d2['Name'] = [temp_d1.at[max_p,'Area']]    
    temp_d2['age-group-males'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-males'] = temp_d1.at[max_p,'Ratio of 1 Male']
    ratio = temp_d1[["Ratio of 1 Female"]].to_numpy()
    max_p = np.argmax(ratio)
    temp_d2['age-group-females'] = temp_d1.at[max_p,'Age Groups']
    temp_d2['ratio-females'] = temp_d1.at[max_p,'Ratio of 1 Female']
    pre_final3 = pre_final3.append(temp_d2, ignore_index=True)
#     break
pre_final3 = pre_final3.sort_values('state/ut',ignore_index=True)
# pre_final3.head()


# #### Saving this in "age-gender-c.csv" as an output file.

# In[16]:


pre_final3.to_csv('age-gender-c.csv')


# # Q8 Completed :)
