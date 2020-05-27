#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
data = pd.read_csv('Iris.csv')
print(data)


# In[34]:


X = data.drop(['target','label','Id'],axis=1)
y = data.loc[:,'label']
y.head()


# In[35]:


from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(X,y)
y_predict = KNN.predict(X)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)


# # PCA

# In[36]:


from sklearn.preprocessing import StandardScaler
X_norm = StandardScaler().fit_transform(X)
print(X_norm)


# In[37]:


x1_mean = X.loc[:,'SepalLengthCm'].mean()
x1_norm_mean = X_norm[:,0].mean()
x1_sigma = X.loc[:,'SepalLengthCm'].std()
x1_norm_sigma = X_norm[:,0].std()
print(x1_mean,x1_norm_mean,x1_sigma,x1_norm_sigma)


# In[38]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure(figsize=(20,5))
plt.subplot(121)
plt.hist(X.loc[:,'SepalLengthCm'],bins=100)
plt.subplot(122)
plt.hist(X_norm[:,0],bins=100)
plt.show()


# In[39]:


print(X.shape)


# In[41]:


from sklearn.decomposition import PCA
pca = PCA(n_components=4)
X_pca = pca.fit_transform(X_norm)
var_radio = pca.explained_variance_ratio_
print(var_radio)


# In[42]:


fig2 = plt.figure()
plt.bar([1,2,3,4],var_radio)
plt.xticks([1,2,3,4],['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])
plt.show()


# In[44]:


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_norm)
X_pca.shape


# In[60]:


fig3 = plt.figure()
setosa = plt.scatter(X_pca[:,0][y==0],X_pca[:,1][y==0])
versicolor = plt.scatter(X_pca[:,0][y==1],X_pca[:,1][y==1])
virginica = plt.scatter(X_pca[:,0][y==2],X_pca[:,1][y==2])
plt.legend((setosa,versicolor,virginica),('setosa','versicolor','virginica'))
plt.show()


# In[62]:


KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(X_pca,y)
y_predict = KNN.predict(X_pca)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)

