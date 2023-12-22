#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[2]:


#Extraction
csv_file_path = "~/Downloads/kdrama.csv"
df = pd.read_csv(csv_file_path)


# In[3]:


#Clean and Transform
df['Watchers'] = pd.to_numeric(df['Watchers'], errors='coerce')
df.drop_duplicates(inplace=True)
df.dropna(subset=['Title', 'Genre'], inplace=True)


# In[4]:


#Load
db_connection = sqlite3.connect("kdrama_database.db")
df.to_sql("kdramas", db_connection, index=False, if_exists="replace")
db_connection.close()


# In[5]:


db_connection = sqlite3.connect("kdrama_database.db")
query_result = pd.read_sql_query("SELECT * FROM kdramas LIMIT 5;", db_connection)
db_connection.close()


# In[ ]:


print("\nSample of the data loaded into SQLite:")
print(query_result)

