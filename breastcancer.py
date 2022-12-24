#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[42]:


data= pd.read_csv("F:/breast_cancer.csv")
data.head(10)


# In[43]:


data['diagnosis'].hist()


# In[44]:


corr = data.iloc[:-1].corr(method="pearson")
cmap=sns.diverging_palette(250,354,80,60,center = "dark",as_cmap=True)
sns.heatmap(corr, cmap=cmap,vmax=1, vmin=-.1, square=True, linewidth= .2)


# In[45]:


data=data[["radius_mean","texture_mean","mean_smoothness","diagnosis"]]


# In[47]:


data.head(10)


# In[54]:


fig,axes=plt.subplots(1,3, figsize=(18,6),sharey=True)
sns.histplot(data, ax=axes[0], x='radius_mean',kde=True,color='r')
sns.histplot(data, ax=axes[1], x='texture_mean',kde=True,color='g')
sns.histplot(data, ax=axes[2], x='mean_smoothness',kde=True,color='b')


# In[ ]:




