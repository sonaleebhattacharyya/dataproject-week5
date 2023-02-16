#!/usr/bin/env python
# coding: utf-8
# In[5]:
import pandas as pd
import streamlit as st
# In[6]:
df = pd.read_csv('supermarket.csv')
# In[7]:
df.head()
# In[8]:
'''Top 10 performing stores, 
   Top 5 performing areas, 
    Average daily customers overall'''
# Find the top 10 performing stores 
df.sort_values(['store_sales'], ascending=False).head(10)
# In[9]:
sales = df.groupby("store_area")["store_sales"].sum()
# In[10]:
top_areas = sales.sort_values(ascending=False).head(5)
# In[11]:
print(top_areas)
# In[12]:
avg_customers = df['daily_customer_count'].mean()
# In[15]:
st.write("Top 10 areas:")
st.write(top_areas)
# In[ ]:
st.write("Average Customer Count:")
st.write(avg_customers)
# In[ ]:




