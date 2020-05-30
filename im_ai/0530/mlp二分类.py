#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd
import numpy as np
#加载数据
data = pd.read_csv('data.csv')
data.head()


# In[136]:


X = data.drop(['y'],axis=1)
y = data.loc[:,'y']


# In[137]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure()
passed = plt.scatter(X.loc[:,'x1'][y==1],X.loc[:,'x2'][y==1])
passed = plt.scatter(X.loc[:,'x1'][y==0],X.loc[:,'x2'][y==0])
plt.show()


# In[142]:


#数据分离
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33, random_state=10)
print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)


# In[144]:


from keras.models import Sequential
from keras.layers import Dense, Activation
mlp = Sequential()
mlp.add(Dense(units=20,input_dim=2,activation='sigmoid'))
mlp.add(Dense(units=1,activation='sigmoid'))
mlp.summary()


# In[147]:


#配置模型训练方式
mlp.compile(optimizer='adam',loss='binary_crossentropy')


# In[164]:


mlp.fit(X_train,y_train,epochs=6000)


# In[171]:


#准确率
y_train_predict = mlp.predict_classes(X_train)
from sklearn.metrics import accuracy_score
accuracy_train = accuracy_score(y_train,y_train_predict)
print(accuracy_train)


# In[172]:


#准确率
y_test_predict = mlp.predict_classes(X_test)
accuracy_test = accuracy_score(y_test,y_test_predict)
print(accuracy_test)


# In[167]:


#转换到pd.series
y_train_predict_form = pd.Series(i[0] for i in y_train_predict)
print(y_train_predict_form)


# In[168]:


#用于画图的数据点
xx,yy = np.meshgrid(np.arange(0,1,0.01),np.arange(0,1,0.01))
x_range = np.c_[xx.ravel(),yy.ravel()]
y_range_predict = mlp.predict_classes(x_range)
print(type(y_range_predict))


# In[169]:


#转换输出格式
y_range_predict_form = pd.Series(i[0] for i in y_range_predict)
print(y_range_predict_form,type(y_range_predict_form))


# In[174]:


fig2 = plt.figure()
passed_predict = plt.scatter(x_range[:,0][y_range_predict_form==1], x_range[:,1][y_range_predict_form==1])
failed_predict = plt.scatter(x_range[:,0][y_range_predict_form==0], x_range[:,1][y_range_predict_form==0])
passed = plt.scatter(X.loc[:,'x1'][y==1],X.loc[:,'x2'][y==1])
failed = plt.scatter(X.loc[:,'x1'][y==0],X.loc[:,'x2'][y==0])
plt.legend((passed,failed,passed_predict,failed_predict),('passed','failed','passed_predict','failed_predict'))
plt.show()


# In[ ]:




