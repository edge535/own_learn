
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv("chip_test.csv")
mask=data.loc[:,'pass']==1
get_ipython().magic('matplotlib inline')
fig1 = plt.figure()
passed = plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed = plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask], marker='^')
plt.title("test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")
plt.legend((passed,failed),('passed','filed'))
print(data)
plt.show()


# In[21]:


X = data.drop(['pass'], axis=1)
y = data.loc[:,'pass']
X1 = data.loc[:,'test1']
X2 = data.loc[:,'test2']
X1_2 = X1*X1
X2_2 = X2*X2
X1_X2 = X1*X2
X_new = {'X1':X1, 'X2':X2, 'X1_2':X1_2, 'X2_2':X2_2, 'X1_x2':X1_X2}
X_new = pd.DataFrame(X_new)
print(X_new)


# In[22]:


from sklearn.linear_model import LogisticRegression
LR2 = LogisticRegression()
LR2.fit(X_new,y)


# In[23]:


from sklearn.metrics import accuracy_score
y2_predict = LR2.predict(X_new)
accuracy = accuracy_score(y,y2_predict)
print(accuracy)


# In[24]:


X1_new = X1.sort_values()
theta0 = LR2.intercept_
theta1,theta2,theta3,theta4,theta5=LR2.coef_[0][0],LR2.coef_[0][1],LR2.coef_[0][2],LR2.coef_[0][3],LR2.coef_[0][4]
a = theta4
b = theta5*X1_new+theta2
c = theta0+theta1*X1_new+theta3*X1_new*X1_new
X2_new_boundary = (-b + np.sqrt(b*b-4*a*c) )/(2*a)
print(X2_new_boundary)


# In[25]:


fig4 = plt.figure()
passed = plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed = plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask], marker='^')
plt.title("test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")
plt.legend((passed,failed),('passed','filed'))
plt.plot(X1_new,X2_new_boundary)
plt.show()


# In[37]:


def f(x):
    a = theta4
    b = theta5*x+theta2
    c = theta0+theta1*x+theta3*x*x
    X2_new_boundary1 = (-b + np.sqrt( np.abs(b*b-4*a*c) ) )/(2*a)
    X2_new_boundary2 = (-b - np.sqrt( np.abs(b*b-4*a*c) ) )/(2*a)
    return X2_new_boundary1, X2_new_boundary2


# In[32]:


X2_new_boundary1 = []
X2_new_boundary2 = []
for x in X1_new:
    X2_new_boundary1.append(f(x)[0])
    X2_new_boundary2.append(f(x)[1])
print(X2_new_boundary1,X2_new_boundary2)


# In[33]:


fig5 = plt.figure()
passed = plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed = plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask], marker='^')
plt.plot(X1_new,X2_new_boundary1)
plt.plot(X1_new,X2_new_boundary2)
plt.title("test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")
plt.legend((passed,failed),('passed','filed'))
plt.show()


# In[40]:


X1_range = [-0.9 + x/10000 for x in range(0,19000)]
X1_range = np.array(X1_range)
X2_new_boundary1 = []
X2_new_boundary2 = []
for x in X1_range:
    X2_new_boundary1.append(f(x)[0])
    X2_new_boundary2.append(f(x)[1])
fig6 = plt.figure()
passed = plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed = plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask], marker='^')
plt.plot(X1_range,X2_new_boundary1)
plt.plot(X1_range,X2_new_boundary2)
plt.title("test1-test2")
plt.xlabel("test1")
plt.ylabel("test2")
plt.legend((passed,failed),('passed','filed'))
plt.show()

