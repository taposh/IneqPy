
# coding: utf-8

# In[1]:


# load packages
import pandas as pd
import numpy as np
import ineqpy as ineq

# # First-steps

# In[2]:


# load data
from pathlib import Path
data = pd.read_csv(Path("ineq.__file__").parent / "examples" / 'eusilc.csv', index_col=0).dropna()
svy = ineq.api.Survey(data, weights='rb050')


# In[3]:


svy.gini('eqincome')


# In[4]:


svy.atkinson('eqincome')


# In[5]:


svy.theil('eqincome')


# In[6]:


svy.mean('eqincome')


# In[7]:


svy.percentile('eqincome')


# In[8]:


svy.kurt('eqincome')


# In[9]:


svy.skew('eqincome')


# In[10]:


svy.lorenz('eqincome').plot(figsize=(5,5))


# In[10]:

x = data.eqincome
w = data.rb050

ineq.var(variable=x, weights=w)