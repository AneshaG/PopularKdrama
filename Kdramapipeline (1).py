#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[4]:


#Extraction
csv_file_path = "~/Downloads/kdrama.csv"
df = pd.read_csv(csv_file_path)


# In[ ]:


print("Sample of the K-drama dataset:")
print(df.head())


# In[6]:


#Transform
df['Watchers'] = pd.to_numeric(df['Watchers'], errors='coerce')


# In[7]:


db_connection = sqlite3.connect("kdrama_database.db")
query_result = pd.read_sql_query("SELECT * FROM kdramas LIMIT 5;", db_connection)
db_connection.close()


# In[ ]:


print("\nSample of the data loaded into SQLite:")
print(query_result)

