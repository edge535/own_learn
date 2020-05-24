
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


data = pd.read_csv('usa_housing_price.csv')
data.head()


# In[23]:


get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.figure(figsize = (10,10))
fig1 = plt.subplot(231)
plt.scatter(data.loc[:,'Avg.Area Income'],data.loc[:,'price'])
plt.title('price vs Income')
plt.show()

fig2 = plt.subplot(232)
plt.scatter(data.loc[:,'Avg.Area House Age'],data.loc[:,'price'])
plt.title('price vs  House Age')
plt.show()

fig3 = plt.subplot(233)
plt.scatter(data.loc[:,'Avg.Area Number of Rooms'],data.loc[:,'price'])
plt.title('price vs  Number of Rooms')
plt.show()

fig4 = plt.subplot(234)
plt.scatter(data.loc[:,'Avg.Area Population'],data.loc[:,'price'])
plt.title('price vs  Number of Population')
plt.show()

fig5 = plt.subplot(235)
plt.scatter(data.loc[:,'size'],data.loc[:,'price'])
plt.title('price vs  size')
plt.show()


# In[39]:


x = data.loc[:,'size']
y = data.loc[:,'price']
print(y.shape)


# In[48]:


x = np.array(x).reshape(-1,1)
print(x.shape)


# In[49]:


from sklearn.linear_model import LinearRegression
lr1 = LinearRegression()
lr1.fit(x, y)


# In[37]:


y_predict_1 = lr1.predict(x)
print(y_predict_1)


# In[40]:


from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y,y_predict_1)
r2 = r2_score(y,y_predict_1)
print(mse, r2)


# In[42]:


fig6 = plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.plot(x,y_predict_1,'r')
plt.show()


# In[50]:


#define x_multiple
x_mul = data.drop(['price'],axis=1)
x_mul.shape


# In[63]:


#set up 2nd linear model
lr_mul = LinearRegression()
lr_mul.fit(x_mul,y)


# In[55]:


y_predict_mul = lr_mul.predict(x_mul)
print(y_predict_mul)


# In[57]:


mse_mul = mean_squared_error(y,y_predict_mul)
r2_mul = r2_score(y,y_predict_mul)
print(mse_mul, r2_mul)


# In[58]:


print(mse, r2)


# In[59]:


fig7 = plt.figure(figsize=(8,5))
plt.scatter(y,y_predict_mul)
plt.show()


# In[60]:


fig7 = plt.figure(figsize=(8,5))
plt.scatter(y,y_predict_1)
plt.show()


# In[65]:


x_test = np.array([65000,5,5,30000,200]).reshape(1,-1)
print(x_test, x_test.shape)


# In[66]:


y_test_predict = lr_mul.predict(x_test)
print(y_test_predict)


# In[ ]:




