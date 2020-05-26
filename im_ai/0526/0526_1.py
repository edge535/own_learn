
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
data = pd.read_csv('data.csv')
data.head()


# In[8]:


X = data
print(X)


# In[14]:


from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
fig1 = plt.figure()
plt.scatter(X.loc[:,'x'],X.loc[:,'y'])
plt.show()


# In[16]:


from sklearn.cluster import KMeans
KM = KMeans(n_clusters=3, random_state=0)
KM.fit(X)


# In[21]:


centers = KM.cluster_centers_
print(centers)


# In[22]:


fig3 = plt.figure()
plt.scatter(centers[:,0],centers[:,1])
plt.scatter(X.loc[:,'x'],X.loc[:,'y'])
plt.show()


# In[27]:


#test data x=0.8 y=0.6
y_predict_test = KM.predict([[0.8,0.6]])
print(y_predict_test)


# In[ ]:


y_predict = KM.predict(X)


# In[35]:


from sklearn.cluster import estimate_bandwidth, MeanShift
bandwidth = estimate_bandwidth(X,n_samples=500)
MS = MeanShift(bandwidth=bandwidth)
MS.fit(X)


# In[38]:


y_predict_ms = MS.predict(X)
print(pd.value_counts(y_predict_ms), MS.cluster_centers_)


# In[40]:


fig4 = plt.figure()
plt.scatter(MS.cluster_centers_[:,0],MS.cluster_centers_[:,1])
plt.scatter(X.loc[:,'x'][y_predict_ms==0],X.loc[:,'y'][y_predict_ms==0])
plt.scatter(X.loc[:,'x'][y_predict_ms==1],X.loc[:,'y'][y_predict_ms==1])
plt.scatter(X.loc[:,'x'][y_predict_ms==2],X.loc[:,'y'][y_predict_ms==2])
plt.show()

