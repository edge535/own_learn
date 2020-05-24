
# coding: utf-8

# In[10]:


import pandas as pd
data = pd.read_csv('data.csv')
print(data,data.shape)


# In[11]:


x = data.loc[:,'x']
y = data.loc[:,'y']
print(x,y)


# In[12]:


from matplotlib import pyplot as plt
plt.figure(figsize=(10,10))
plt.scatter(x,y)
plt.show()


# In[15]:


from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()


# In[20]:


import numpy as np
x = np.array(x)
x = x.reshape(-1,1)
y = np.array(y)
y = y.reshape(-1,1)
print(type(x), x.shape)
print(type(y), y.shape)


# In[21]:


lr_model.fit(x,y)


# In[23]:


y_predict = lr_model.predict(x)
print(y_predict)
print(y_predict.shape)


# In[24]:


y_3 = lr_model.predict([[3.5]])
print(y_3)


# In[25]:


a = lr_model.coef_
b = lr_model.intercept_
print(a,b)


# In[30]:


from sklearn.metrics import mean_squared_error as mse, r2_score 
mse = mse(y,y_predict)
r2 = r2_score(y,y_predict)
print(mse)
print(r2)
plt.figure()
plt.plot(y,y_predict)
plt.show()

