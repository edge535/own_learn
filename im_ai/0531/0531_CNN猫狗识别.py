#!/usr/bin/env python
# coding: utf-8

# In[2]:


from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('./training_set',target_size=(50,50),batch_size=32,class_mode='binary')


# In[3]:


#建立CNN模型
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten,Dense
model = Sequential()
#卷积层
model.add(Conv2D(32,(3,3), input_shape=(50,50,3), activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#卷积层
model.add(Conv2D(32,(3,3), activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#Flatten
model.add(Flatten())
#全连接层
model.add(Dense(units=128, activation='relu'))
#输出层
model.add(Dense(units=1, activation='sigmoid'))


# In[4]:


#设置模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()


# In[6]:


from IPython.display import display
from PIL import Image
model.fit_generator(training_set, epochs=25)


# In[7]:


#查看准确率
accuracy_train = model.evaluate_generator(training_set)
print(accuracy_train)


# In[8]:


# 测试数据的准确率
train_datagen = ImageDataGenerator(rescale=1./255)
test_set = train_datagen.flow_from_directory('./test_set',target_size=(50,50),batch_size=32,class_mode='binary')
accuracy_test = model.evaluate_generator(test_set)
print(accuracy_test)


# In[29]:


from matplotlib import pyplot as plt
#加载单张图片
from keras.preprocessing.image import load_img, img_to_array
pic_cat_test = 'cat_test.jpg'
pic_cat_test = load_img(pic_cat_test, target_size=(50,50))
pic_cat_test = img_to_array(pic_cat_test)
pic_cat_test = pic_cat_test/255
pic_cat_test = pic_cat_test.reshape(1,50,50,3)
#调用模型
result = model.predict_classes(pic_cat_test)
print(result)

pic_dog_test = 'dog_test.jpg'
pic_dog_test = load_img(pic_dog_test, target_size=(50,50))
pic_dog_test = img_to_array(pic_dog_test)
pic_dog_test = pic_dog_test/255
pic_dog_test = pic_dog_test.reshape(1,50,50,3)
#调用模型
result = model.predict_classes(pic_dog_test)
print(result)

