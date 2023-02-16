#!/usr/bin/env python
# coding: utf-8
# In[5]:
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# In[6]:
df = pd.read_csv('supermarket.csv')
# In[7]:
df.head()
# In[8]:
'''Top 10 performing stores, 
   Top 5 performing areas, 
    Average daily customers overall'''
# Find the top 10 performing stores 
top_ten_stores = df.sort_values(['store_sales'], ascending=False).head(10)
# In[9]:
sales = df.groupby("store_area")["store_sales"].sum()
# In[10]:
top_5_areas = sales.sort_values(ascending=False).head(5)
# In[11]:
print(top_5_areas)
# In[12]:
avg_customers = df['daily_customer_count'].mean()
# In[15]:

st.write("Top 10 performing stores:") 
st.write(top_ten_stores)
st.write("Top 5 performing areas:")
st.write(top_5_areas)
# In[ ]:
st.write("Average Customer Count:")
st.write(avg_customers)
# In[ ]:


st.title("Store Performance Dashboard")
st.write("Average Number of Customers:", avg_customers) 
st.subheader("Top 10 Performing Stores")
for i, store_id in enumerate(top_ten_stores['store_id']): 
    st.write(f"{i+1}. {store_id} - ${top_ten_stores.iloc[i]['store_sales']:.2f}")
st.subheader("Top 5 Performing Areas")
for i, store_area in enumerate(top_5_areas.index):
    st.write(f"{i+1}. {store_area} - ${top_5_areas.loc[store_area]:,.2f}")
  
