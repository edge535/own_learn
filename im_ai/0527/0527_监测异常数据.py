#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('anomaly_data.csv')
print(data)


# In[4]:


from matplotlib import pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure()
plt.scatter(data.loc[:,'x1'],data.loc[:,'x2'])


# In[5]:


x1 = data.loc[:,'x1']
x2 = data.loc[:,'x2']


# In[9]:


fig2 = plt.figure(figsize=(10,5))
plt.subplot(121)
plt.hist(x1,bins=100)
plt.title('x1 distribute')
plt.subplot(122)
plt.hist(x2,bins=100)
plt.title('x2的分布')
plt.show()


# In[12]:


#计算均值和标准差，为计算高斯分布做准备
x1_mean = x1.mean()
x1_sigma = x1.std()
x2_mean = x2.mean()
x2_sigma = x2.std()
print(x1_mean,x1_sigma,x2_mean,x2_sigma)
#计算高斯分布数值
from scipy.stats import norm
import numpy as np
x1_range = np.linspace(8,10,300)
y1_normal = norm.pdf(x1_range,x1_mean,x1_sigma)
x2_range = np.linspace(8,12,300)
y2_normal = norm.pdf(x2_range,x2_mean,x2_sigma)


# In[15]:


fig3 = plt.figure()
plt.subplot(121)
plt.plot(x1_range,y1_normal)
plt.subplot(122)
plt.plot(x2_range,y2_normal)
plt.show()


# In[18]:


from sklearn.covariance import EllipticEnvelope
ad_model = EllipticEnvelope()
ad_model.fit(data)


# In[21]:


y_predict = ad_model.predict(data)
print(pd.value_counts(y_predict))


# In[36]:


fig4 = plt.figure()
plt.scatter(data.loc[:,'x1'],data.loc[:,'x2'],marker='x')
plt.scatter(data.loc[:,'x1'][y_predict==-1],data.loc[:,'x2'][y_predict==-1],facecolor='none',edgecolor='red',marker='o')
plt.show()


# In[ ]:




