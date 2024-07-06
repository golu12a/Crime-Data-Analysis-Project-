#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install pymysql


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql


# In[6]:


conn = pymysql.connect(host="localhost",
                       user="root",
                       password="avinash.1",
                       database="crime")
conn


# In[7]:


query="select * from crime_data"
df=pd.read_sql(query,conn)
df.head()


# In[8]:


## Geographical hotspots for reported crimes

plt.style.use('ggplot')
plt.figure(figsize=(10,5))
sns.scatterplot(x=df['LAT'],y=df['LON'],color='red',label='crime hotspots')
plt.xlabel('latitude in degrees')
plt.ylabel('longitude in degrees')
plt.legend(loc='upper left')
plt.title('Geographical Hotspots')
plt.grid(which="minor", linestyle="-.", color="skyblue")
plt.show()




# In[9]:


## Distribution of victim ages in reported crime

plt.hist(df["Vict_Age"],bins=10,edgecolor="black")
plt.xlabel("Victim Ages")
plt.ylabel("Counts")
plt.title("Victim Ages in Years")
plt.show()


# In[10]:


## Difference in crime rates between male and female victims
sns.countplot(x=df['Vict_Sex'])
plt.title("Crime Rate Between Male and Female Victim")
plt.show()


# In[21]:


## Crimes Occured based on the "Location" column

count = df['Location'].value_counts()
count_t = count.head(10)
count_t


# In[24]:


count_v = count_t.values
count_v


# In[25]:


count_i = count_t.index
count_i


# In[26]:


plt.figure(dpi=100)
plt.pie(count_v,labels=count_i,autopct="%1.1f%%")
plt.show()


# In[15]:


## Distribution of reported crimes based on crime code

plt.hist(df["Crm_Cd"],bins=10,edgecolor="black")
plt.xlabel("Crime Code")
plt.ylabel("Counts")
plt.title("Reported Crime based on Crime Code")
plt.show()

