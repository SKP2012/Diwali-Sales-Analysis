#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[9]:


df= pd.read_csv(r'C:\Users\SHUBHAM PAWAR\Desktop\PowerBI\EDA projects\Diwali Sales Data.csv' ,encoding='unicode_escape')


# In[14]:


df.head()


# ## 1.Let's Understand the data:

# In[15]:


df.shape


# In[20]:


df.info()


# In[23]:


#drop unrelated coulumns or columns without any values and relations
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[24]:


df.head()


# In[53]:


df.describe()


# ## Preprocess the data: Cleaning and Replacing:

# In[28]:


#check if any null values present
pd.isnull(df).sum()


# In[32]:


#above data shows that the Amount columns has 12 null values, we can delete these rows. before that, to compare lets check the shape.
df.shape


# In[33]:


df.dropna(inplace=True)


# In[38]:


#lets check the shape again now.
df.shape


# In[45]:


#as the data type of the amount column is float, we need to update it into int. We have already removed null values.
df['Amount'] = df['Amount'].astype('int')


# In[46]:


df.info()


# In[48]:


df['Amount'].dtype


# In[49]:


df.columns


# In[50]:


#rename a column
#df.rename(columns={'Marital_Status':'is_married'})

#lets check the detail description.
df.describe()


# In[52]:


#check for the specific columns
df[['Age','Marital_Status','Orders']].describe()


# ## Exploratory Data Analysis:

# #### Gender based analysis:

# In[63]:


# Analysis on the basis on gender:
#lets visualize some counts of genders first.

ax = sns.countplot(x ='Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[61]:


#lets use groupby in python
df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[62]:


#lets check visuals on basis on groupby.
sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount', data = sales_gen)


# In[ ]:


# from the above graphs, it looks like the female buyers are more and the purchasing power of the females are also more.


# #### Age based analysis:

# In[65]:


# analysis on the basis on age:
sns.countplot(data= df, x = 'Age Group')


# In[67]:


# analysis on the basis on age and Gender:
ax= sns.countplot(data= df, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[68]:


# from above graphs, we can analyze that the age group 26-35 has more buyers and the females are in top


# #### State Based Analysis:

# In[74]:


# Check top 10 states for orders and sales:
sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
#re-size
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data=sales_state,x='State',y='Orders')


# In[80]:


# Check top 10 states for amounnt and sales:
sales_state = df.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
#re-size
sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data=sales_state,x='State',y='Amount')


# In[81]:


# from above graphs, we can say that most of the orders and sales are from UP, Maharashtra and Karnataka.


# #### Marital status based analysis:

# In[87]:


ax= sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[89]:


# check above graph on the basis on amount:
sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_state, x='Marital_Status',y='Amount',hue='Gender')


# In[90]:


# from abpve two graphs, we clearly see that married women are most of the buyers with high purchasing power.


# #### Occupation Based Analysis:

# In[102]:


ax= sns.countplot(data=df,x='Occupation')
sns.set(rc={'figure.figsize':(25,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[103]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_state, x='Occupation',y='Amount')


# In[104]:


# from above graphs, we can say that top 3 buyers are from IT sector, Healthcare and Aviation


# #### Product Category based analysis:

# In[112]:


ax= sns.countplot(data=df, x= 'Product_Category')


# In[113]:


ax= sns.countplot(data=df, x= 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[114]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_Category',y='Amount')


# In[115]:


# from above two graphs it can be analyzed that the Clothing food and electronics are leading categories.
# However in terms of Amount, food dominates.


# In[116]:


# lets check top selling products on the basis on product ID:
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_ID',y='Orders')


# In[117]:


sns.barplot(data=sales_state,  x='Product_ID', y= 'Orders')


# # Final Conclusion:

# ## From the above details, we can say that married womens are lead buyers from IT, Healthcare and Aviation sector with states UP,MH and KN.

# In[ ]:




