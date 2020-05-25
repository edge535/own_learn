
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
data = pd.read_csv("examdata.csv")
data


# In[8]:


#visualize the data
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
fig1 = plt.figure()
plt.scatter(data.loc[:,'Exam1'],data.loc[:,'Exam2'])
plt.title("Exam1-Exam2")
plt.xlabel("Exam1")
plt.ylabel("Exam2")
plt.show()


# In[11]:


#add label mask
mask=data.loc[:,'Pass']==1
print(mask)


# In[15]:


fig1 = plt.figure()
passed = plt.scatter(data.loc[:,'Exam1'][mask],data.loc[:,'Exam2'][mask])
failed = plt.scatter(data.loc[:,'Exam1'][~mask],data.loc[:,'Exam2'][~mask], marker='^')
plt.title("Exam1-Exam2")
plt.xlabel("Exam1")
plt.ylabel("Exam2")
plt.legend((passed,failed),('passed','filed'))
plt.show()


# In[21]:


X = data.drop(['Pass'], axis=1)
y = data.loc[:,'Pass']
X1 = data.loc[:,'Exam1']
X2 = data.loc[:,'Exam2']


# In[22]:


print(X.shape, y.shape)


# In[24]:


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(X,y)


# In[25]:


#结果和评估表现
y_predict = LR.predict(X)
y_predict


# In[26]:


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)


# In[29]:


#exam1=70 exam2=65时的预测
y_test = LR.predict([[70,65]])
print('passed' if y_test==1 else 'failed')


# In[39]:


theta0 = LR.intercept_[0]
theta1, theta2 = LR.coef_[0][0],LR.coef_[0][1]
print(theta0,theta1,theta2)


# In[42]:


X2_new = -(theta0+theta1*X1)/theta2
X2_new 


# In[43]:


fig3 = plt.figure()
passed = plt.scatter(data.loc[:,'Exam1'][mask],data.loc[:,'Exam2'][mask])
failed = plt.scatter(data.loc[:,'Exam1'][~mask],data.loc[:,'Exam2'][~mask], marker='^')
plt.title("Exam1-Exam2")
plt.xlabel("Exam1")
plt.ylabel("Exam2")
plt.legend((passed,failed),('passed','filed'))
plt.plot(X1, X2_new)
plt.show()


# In[48]:


#create new data
X1_2 = X1*X1
X2_2 = X2*X2
X1_X2 = X1*X2
X_new = {'X1':X1, 'X2':X2, 'X1_2':X1_2, 'X2_2':X2_2, 'X1_x2':X1_X2}
X_new = pd.DataFrame(X_new)
print(X_new)


# In[49]:


#创建新的模型并且训练
LR2 = LogisticRegression()
LR2.fit(X_new,y)


# In[51]:


y2_predict = LR2.predict(X_new)
accuracy2 = accuracy_score(y,y2_predict)
print(accuracy2)


# In[61]:


X1_new = X1.sort_values()
print(X1_new)


# In[78]:


theta0 = LR2.intercept_
theta1,theta2,theta3,theta4,theta5=LR2.coef_[0][0],LR2.coef_[0][1],LR2.coef_[0][2],LR2.coef_[0][3],LR2.coef_[0][4]
a = theta4
b = theta5*X1_new+theta2
c = theta0+theta1*X1_new+theta3*X1_new*X1_new
X2_new_boundary = (-b + np.sqrt(np.abs(b*b-4*a*c)) )/(2*a)
print(X2_new_boundary)


# In[80]:


fig4 = plt.figure()
passed = plt.scatter(data.loc[:,'Exam1'][mask],data.loc[:,'Exam2'][mask])
failed = plt.scatter(data.loc[:,'Exam1'][~mask],data.loc[:,'Exam2'][~mask], marker='^')
plt.title("Exam1-Exam2")
plt.xlabel("Exam1")
plt.ylabel("Exam2")
plt.legend((passed,failed),('passed','filed'))
plt.plot(X1_new,X2_new_boundary)
plt.show()


# In[77]:


a = [1,-2,3,4]
a = np.array(a)
print(type(a),a)
a = np.sqrt(a)
print(type(a),a)

