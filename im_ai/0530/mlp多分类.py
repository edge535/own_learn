#!/usr/bin/env python
# coding: utf-8

# # 加载mnist数据集 

# In[1]:


from keras.datasets import mnist
(X_train,y_train),(X_test,y_test)=mnist.load_data()


# In[9]:


print(X_train.shape,type(X_train))
print(X_train[0])
print(y_train[0])


# #  可视化数据

# In[10]:


img1 = X_train[0]
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
fig1 = plt.figure()
plt.imshow(img1)
plt.title(y_train[0])
plt.show()


# #  格式化数据

# In[16]:


feature_size=img1.shape[0] * img1.shape[1]
X_train_fromat = X_train.reshape(X_train.shape[0],feature_size)
X_test_fromat = X_test.reshape(X_test.shape[0],feature_size)
print(X_train_fromat.shape)


# In[18]:


#归一化
#因为0-255太大，所以进行归一化， /255 = 0-1
X_train_normal = X_train_fromat/255
X_test_normal = X_test_fromat/255


# In[21]:


# 格式化输出数据
from keras.utils import to_categorical
y_train_formal = to_categorical(y_train)
y_test_formal = to_categorical(y_test)
print(y_train)
print(y_train_formal)


# # 模型

# In[24]:


from keras.models import Sequential
from keras.layers import Dense, Activation

mlp = Sequential()
mlp.add(Dense(units=392, activation='sigmoid', input_dim=feature_size))
mlp.add(Dense(units=392, activation='sigmoid'))
mlp.add(Dense(units=10, activation='softmax'))
mlp.summary()


# In[25]:


mlp.compile(loss='categorical_crossentropy', optimizer='adam')


# In[26]:


mlp.fit(X_train_normal,y_train_formal,epochs=10)


# In[30]:


from sklearn.metrics import accuracy_score

y_train_predict = mlp.predict_classes(X_train_normal)
accuracy_train = accuracy_score(y_train,y_train_predict)

y_test_predict = mlp.predict_classes(X_test_normal)
accuracy_test = accuracy_score(y_test,y_test_predict)

print("train:",accuracy_train)
print("test",accuracy_test)


# #  结果可视化

# In[40]:


img2 = X_test[9]
fig2 = plt.figure()

plt.subplot(221)
img2 = X_test[9]
plt.imshow(img2)
plt.title(y_test_predict[9])

plt.subplot(222)
img3 = X_test[19]
plt.imshow(img3)
plt.title(y_test_predict[19])

plt.subplot(223)
img4 = X_test[91]
plt.imshow(img4)
plt.title(y_test_predict[91])

plt.subplot(224)
img5 = X_test[100]
plt.imshow(img5)
plt.title(y_test_predict[100])

plt.show()

