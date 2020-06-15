#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load the Mnist DataSet model
import keras
mnist=keras.datasets.fashion_mnist
(X_train,y_train),(X_test,y_test)=mnist.load_data()


# In[2]:


# printing the number of samples in x_train, x_test, y_train, y_test
print("Initial shape or dimensions of X_train", str(X_train.shape))
print ("Number of samples in our training data: " + str(len(X_train)))
print ("Number of labels in our training data: " + str(len(y_train)))

print("\nInitial shape or dimensions of X_test", str(X_test.shape))
print ("Number of samples in our test data: " + str(len(X_test)))
print ("Number of labels in our test data: " + str(len(y_test)))


# In[3]:


# Data processing
X_train=X_train/255.0
X_test=X_test/255.0
class_name=['top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
print("class_name=",class_name)


# In[4]:


# Import Library for model creation
from keras.models import Sequential
from keras.layers import Dense,Flatten 
from keras.optimizers import RMSprop
from keras.layers import Conv2D
from keras.layers import MaxPool2D


# In[5]:


# Train model function
def train_model(neurons,model,epochs,test):
    model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(28,28,1),activation='relu'))
    model.add(MaxPool2D())
    model.add(Flatten())
    model.add(Dense(units=256, activation='relu'))
    model.add(Dense(units=neurons,activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    model.compile(optimizer=RMSprop(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


# In[6]:


def validate(fit_model,epochs):
    text=fit_model.history
    accuracy=text['accuracy'][epochs-1]*100
    accuracy=float(accuracy)
    f=open("accuracy.txt","w+")
    f.write(str(accuracy))
    f.close()
    print("Accuravy for this Itteration is : ",accuracy," %")
    return accuracy


# In[9]:


# Fitting data in model
neurons=16
accuracy=0
epochs=1
test=1
flag=0
X_train=X_train.reshape(60000,28,28,1)
X_test=X_test.reshape(10000,28,28,1)
while int(accuracy)<90:
    if flag==1:
        model=keras.backend.clear_session()
        neurons=neurons+neurons
        epochs=epochs+1
        test=test+1
    model=Sequential()
    model=train_model(neurons,model,epochs,test)
    fit_model=model.fit(X_train, y_train, epochs=epochs)
    accuracy=validate(fit_model,epochs)
    flag=1


# In[10]:


# Send mail
print("Sending mail...")
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("krishana250799@gmail.com","cnuewvclgolepekn")
message1="success"
s.sendmail("krishana250799@gmail.com","krishana250799@gmail.com",message1)
s.quit()
print("Mail send..")


