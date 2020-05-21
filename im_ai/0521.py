
# coding: utf-8

# In[2]:


print('OK')


# In[25]:


import pandas as pd
data = pd.read_csv('data.csv')
print(type(data))
print(data)


# In[29]:


x = data.loc[:,'x']
print(x)
y = data.loc[:,'y']
print(y)


# In[32]:


c = data.loc[:,'x'][y>50]
print(c)


# In[33]:


import numpy as np
data_array = np.array(data)
print(type(data_array))
print(data_array)


# In[36]:


data_new = data+10
data_new.head()


# In[37]:


data_new.to_csv('data_new.csv')


# In[39]:


from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
#低版本无法显示
fig1 = plt.figure(figsize=(5,5)) #初始化一个图形，并设置尺寸
plt.plot(x,y) #线性图
plt.title('y vs x') #设置标题
plt.xlabel('x') #x的标签
plt.ylabel('y') #y的标签
plt.show() #显示

plt.scatter(x,y) #散点图



import numpy as np
a = np.eye(5)
print(type(a))
print(a)


b = np.ones([8,5])
print(type(b))
print(b)
print(b.shape) #显示纬度

