#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
data_train = pd.read_csv("T-R-train.csv")
data_train


# In[72]:


X_train = data_train.loc[:,'T']
y_train = data_train.loc[:,'rate']


# In[73]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure()
plt.scatter(X_train,y_train)
plt.title('raw data')
plt.xlabel('temperature')
plt.ylabel('rate')
plt.show()


# In[74]:


X_train = np.array(X_train).reshape(-1,1)


# In[76]:


from sklearn.linear_model import LinearRegression
lr1 = LinearRegression()
lr1.fit(X_train,y_train)


# In[77]:


#load test data
data_test = pd.read_csv("T-R-test.csv")
data_test


# In[71]:


X_test = data_test.loc[:,'T']
y_test = data_test.loc[:,'rate']
X_test = np.array(X_test).reshape(-1,1)


# In[78]:


y_train_predict = lr1.predict(X_train)
y_test_predict = lr1.predict(X_test)
from sklearn.metrics import r2_score
r2_train = r2_score(y_train,y_train_predict)
r2_test = r2_score(y_test,y_test_predict)
print('From train:',r2_train)
print('From test:',r2_test)


# In[80]:


#可视化模型结果
X_range = np.linspace(40,90,300).reshape(-1,1)
y_range_predict = lr1.predict(X_range)
fig2 = plt.figure()
plt.scatter(X_train,y_train)
plt.plot(X_range,y_range_predict)
plt.title('predict data')
plt.xlabel('temperature')
plt.ylabel('rate')
plt.show()


# In[83]:


#多项式模型_2
from sklearn.preprocessing import PolynomialFeatures
poly2 = PolynomialFeatures(degree=2)
X_2_train = poly2.fit_transform(X_train)
X_2_test = poly2.transform(X_test)
lr2 = LinearRegression()
lr2.fit(X_2_train,y_train)

y_2_train_predict = lr2.predict(X_2_train)
y_2_test_predict = lr2.predict(X_2_test)
r2_2_train = r2_score(y_train,y_2_train_predict)
r2_2_test = r2_score(y_test,y_2_test_predict)
print('2_From train:',r2_2_train)
print('2_From test:',r2_2_test)


# In[87]:


X_2_range = np.linspace(40,90,300).reshape(-1,1)
X_2_range = poly2.transform(X_2_range)
y_2_range_predict = lr2.predict(X_2_range)
fig3 = plt.figure()
tr = plt.scatter(X_train,y_train)
te = plt.scatter(X_test,y_test)
plt.plot(X_range,y_2_range_predict)
plt.title('Poly=2 predict data')
plt.xlabel('temperature')
plt.ylabel('rate')
plt.legend((tr,te),("train","test"))
plt.show()


# In[90]:


#多项式模型_5
poly5 = PolynomialFeatures(degree=5)
X_5_train = poly5.fit_transform(X_train)
X_5_test = poly5.transform(X_test)
lr3 = LinearRegression()
lr3.fit(X_5_train,y_train)

y_5_train_predict = lr3.predict(X_5_train)
y_5_test_predict = lr3.predict(X_5_test)
r2_5_train = r2_score(y_train,y_5_train_predict)
r2_5_test = r2_score(y_test,y_5_test_predict)
print('5_From train:',r2_5_train)
print('5_From test:',r2_5_test)

X_5_range = np.linspace(40,90,300).reshape(-1,1)
X_5_range = poly5.transform(X_5_range)
y_5_range_predict = lr3.predict(X_5_range)
fig4 = plt.figure()
tr = plt.scatter(X_train,y_train)
te = plt.scatter(X_test,y_test)
plt.plot(X_range,y_5_range_predict)
plt.title('Poly=5 predict data')
plt.xlabel('temperature')
plt.ylabel('rate')
plt.legend((tr,te),("train","test"))
plt.show()

