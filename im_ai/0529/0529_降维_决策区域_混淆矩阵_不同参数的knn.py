#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
data = pd.read_csv('data_class_raw.csv')
print(data)


# In[43]:


X = data.drop(['y'],axis=1)
y = data.loc[:,'y']
print(X,y)


# In[41]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1= plt.figure()
plt.scatter(X.loc[:,'x1'][y==0],X.loc[:,'x2'][y==0])
plt.scatter(X.loc[:,'x1'][y==1],X.loc[:,'x2'][y==1])
plt.title('raw data')
plt.show()


# In[42]:


from sklearn.covariance import EllipticEnvelope
ad_model = EllipticEnvelope(contamination=0.02)
ad_model.fit(X[y==0])
y_predice_bad = ad_model.predict(X[y==0])
print(y_predice_bad)


# In[ ]:





# In[25]:


data = pd.read_csv('Iris.csv')
X = data.drop(['Id','target','label'],axis=1)
y = data.loc[:,'label']
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X_normal = StandardScaler().fit_transform(X)
pca = PCA(n_components=4)
X_reduce = pca.fit_transform(X_normal)
var_ratio = pca.explained_variance_ratio_
fig2 = plt.figure()
plt.bar(['p1','p2','p3','p4'],var_ratio)
# plt.xticks([1,2,3,4],['p1','p2','p3','p4'])
plt.show()
pca2 = PCA(n_components=2)
X_reduce = pca2.fit_transform(X_normal)
print(X_reduce.shape)


# In[27]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_reduce,y,random_state=4,test_size=0.5)
print(X_train.shape,X_test.shape,X_reduce.shape)


# In[ ]:





# In[29]:


from sklearn.neighbors import KNeighborsClassifier
knn_10 = KNeighborsClassifier(n_neighbors=10)
knn_10.fit(X_train,y_train)
y_train_predict = knn_10.predict(X_train)
y_test_predict = knn_10.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_train = accuracy_score(y_train,y_train_predict)
accuracy_test = accuracy_score(y_test,y_test_predict)
print(accuracy_train,accuracy_test)


# In[54]:


#可视化决策区域
X_train = pd.DataFrame(X_train)
y_train = pd.DataFrame(y_train)
fig3 = plt.figure()
plt.scatter(X_train.loc[:,0][y_train_predict==0],X_train.loc[:,1][y_train_predict==0])
plt.scatter(X_train.loc[:,0][y_train_predict==1],X_train.loc[:,1][y_train_predict==1])
plt.scatter(X_train.loc[:,0][y_train_predict==2],X_train.loc[:,1][y_train_predict==2])
plt.show()
#决策局域背景填充
xx,yy = np.meshgrid(np.arange(-4,4,0.05),np.arange(-4,4,0.05))
x_range = np.c_[xx.ravel(),yy.ravel()]
x_range_predict = knn_10.predict(x_range)
fig4 = plt.figure()
plt.scatter(x_range[:,0][x_range_predict==0],x_range[:,1][x_range_predict==0])
plt.scatter(x_range[:,0][x_range_predict==1],x_range[:,1][x_range_predict==1])
plt.scatter(x_range[:,0][x_range_predict==2],x_range[:,1][x_range_predict==2])
plt.scatter(X_train.loc[:,0],X_train.loc[:,1])
plt.show()


# In[ ]:





# In[55]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_test_predict)
print(cm)


# #计算不同n_neighbors值下的accura	 

# In[57]:


n = [i for i in range(1,21)]
accuracy_train_list = []
accuracy_test_list =[]
for i in n:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    y_train_predict = knn.predict(X_train)
    y_test_predict = knn.predict(X_test)
    accuracy_train_i = accuracy_score(y_train,y_train_predict)
    accuracy_test_i = accuracy_score(y_test,y_test_predict)
    accuracy_train_list.append(accuracy_train_i)
    accuracy_test_list.append(accuracy_test_i)
print('FROM train',accuracy_train_list)
print('FROM test',accuracy_test_list)


# In[64]:


fig5 = plt.figure(figsize=(12,5))
plt.plot(n,accuracy_train_list,marker='o')
plt.plot(n,accuracy_test_list,marker='x')
plt.title('train and test accuracy EACH n_neighbors')
plt.xlabel('n_neighbors')
plt.show()


# In[73]:


n = [i for i in range(1,21)]
accuracy_train_list = []
accuracy_test_list =[]
for i in n:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    y_train_predict = knn.predict(X_train)
    y_test_predict = knn.predict(X_test)
#     #可视化决策区域
#     X_train = pd.DataFrame(X_train)
#     y_train = pd.DataFrame(y_train)
#     fig3 = plt.figure()
#     plt.scatter(X_train.loc[:,0][y_train_predict==0],X_train.loc[:,1][y_train_predict==0])
#     plt.scatter(X_train.loc[:,0][y_train_predict==1],X_train.loc[:,1][y_train_predict==1])
#     plt.scatter(X_train.loc[:,0][y_train_predict==2],X_train.loc[:,1][y_train_predict==2])
#     plt.show()
    #决策局域背景填充
    xx,yy = np.meshgrid(np.arange(-4,4,0.05),np.arange(-4,4,0.05))
    x_range = np.c_[xx.ravel(),yy.ravel()]
    x_range_predict = knn.predict(x_range)
    fig4 = plt.figure()
    plt.scatter(x_range[:,0][x_range_predict==0],x_range[:,1][x_range_predict==0])
    plt.scatter(x_range[:,0][x_range_predict==1],x_range[:,1][x_range_predict==1])
    plt.scatter(x_range[:,0][x_range_predict==2],x_range[:,1][x_range_predict==2])
    plt.scatter(X_train.loc[:,0],X_train.loc[:,1])
    plt.title('D'+str(i))
    plt.show()

