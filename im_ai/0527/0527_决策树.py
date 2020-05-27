#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
data = pd.read_csv('Iris.csv')
data = data.drop(['Id'], axis=1)
print(data)


# In[2]:


X = data.drop(['target','label'],axis=1)
y = data.loc[:,'label']


# In[5]:


from sklearn import tree
dc_tree = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=5)
dc_tree.fit(X,y)


# In[9]:


y_predict = dc_tree.predict(X)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,y_predict)
print(accuracy)


# In[18]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure(figsize=(10,10))
tree.plot_tree(dc_tree,
               filled='True',
               feature_names=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],
               class_names=['setosa','versicolor','virginica',''])


# In[21]:


from sklearn import tree
dc_tree = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=1)
dc_tree.fit(X,y)
fig2 = plt.figure(figsize=(50,50))
tree.plot_tree(dc_tree,
               filled='True',
               feature_names=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],
               class_names=['setosa','versicolor','virginica',''])

