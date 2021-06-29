# -*- coding: utf-8 -*-
"""task4_deeplearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D6MHhkwJm6ykXzpkhZjvtipmDVsYds6U
"""

#point(a)
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

#Create the convolutional base
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#Add Dense layers on top
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.1, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
#plt.ylim([0.5, 1])
plt.legend(loc='upper right')
plt.savefig('pointa.png')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(test_acc)

#point(b)
import tensorflow as tf
from keras import optimizers
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

model.add(layers.Flatten(input_shape=(32, 32, 3)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))


#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.11, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
#plt.ylim([0.3, 0.8])
plt.legend(loc='upper right')
plt.savefig('pointp.png')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

#point(c)
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

#Create the convolutional base
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
#model.add(layers.Dropout(0.5))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
#model.add(layers.Dropout(0.5))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
#model.add(layers.Dropout(0.5))

#Add Dense layers on top
model.add(layers.Flatten(input_shape=(32, 32, 3)))

model.add(layers.Dense(512, activation='relu'))
#model.add(layers.Dropout(0.5))

model.add(layers.Dense(512, activation='relu'))
#model.add(layers.Dropout(0.5))

model.add(layers.Dense(512, activation='relu'))
#model.add(layers.Dropout(0.5))

model.add(layers.Dense(512, activation='relu'))
#model.add(layers.Dropout(0.5))

model.add(layers.Dense(512, activation='relu'))
#model.add(layers.Dropout(0.5))

model.add(layers.Dense(10, activation='softmax'))

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.11, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
#plt.ylim([0.3, 0.8])
plt.legend(loc='upper right')
plt.savefig('pointc.png')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

#point(d)
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

#Create the convolutional base
model.add(layers.Conv2D(32, (3, 3), activation='sigmoid', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='sigmoid'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='sigmoid'))
model.add(layers.MaxPooling2D((2, 2)))

#Add Dense layers on top
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='sigmoid'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.1, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
#plt.ylim([0.3, 0.8])
plt.legend(loc='upper right')
plt.savefig('pointd.png')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

#point(e) with dropout
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()
model.add(layers.Conv2D(filters=32, kernel_size = 2, padding = 'same',activation = 'relu',input_shape=(32,32,3)))
model.add(layers.MaxPooling2D(pool_size=2))

model.add(layers.Conv2D(filters=64, kernel_size = 2, padding = 'same',activation = 'relu'))
model.add(layers.MaxPooling2D(pool_size=2))

model.add(layers.Conv2D(filters=128, kernel_size = 2, padding = 'same',activation = 'relu'))
model.add(layers.MaxPooling2D(pool_size=2))
model.add(layers.Dropout(0.3))

model.add(layers.Flatten())
model.add(layers.Dense(128,activation='relu'))
model.add(layers.Dropout(0.4))
model.add(layers.Dense(10,activation='softmax'))

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.1, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
#plt.ylim([0.3, 1.0])
plt.legend(loc='lower right')
plt.savefig('pointe.png')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# point(e) with data augmentation
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

aug = ImageDataGenerator(
	rotation_range=20,
	zoom_range=0.15,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.15)

model = models.Sequential()
model.add(layers.Conv2D(filters=32, kernel_size = 2, padding = 'same',activation = 'relu',input_shape=(32,32,3)))
model.add(layers.MaxPooling2D(pool_size=2))

model.add(layers.Conv2D(filters=64, kernel_size = 2, padding = 'same',activation = 'relu'))
model.add(layers.MaxPooling2D(pool_size=2))

model.add(layers.Conv2D(filters=128, kernel_size = 2, padding = 'same',activation = 'relu'))
model.add(layers.MaxPooling2D(pool_size=2))
model.add(layers.Dropout(0.3))

model.add(layers.Flatten())
model.add(layers.Dense(128,activation='relu'))
model.add(layers.Dropout(0.4))
model.add(layers.Dense(10,activation='softmax'))

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(
    learning_rate=0.1, momentum=0.0, nesterov=True, name='SGD'),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

history = model.fit(aug.flow(train_images, train_labels), epochs=10, 
                    validation_data=(test_images, test_labels))

#Evaluate the model
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
#plt.ylim([0.3, 1.0])
plt.legend(loc='lower right')
plt.savefig('pointe.png')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# point(f)
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

def load_data():
  (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
  # Normalize pixel values to be between 0 and 1
  train_images, test_images = train_images / 255.0, test_images / 255.0
  return train_images, train_labels, test_images, test_labels


def define_model(train_images, train_labels, test_images, test_labels, epochs, Dropout = False, data_augmentation = False):

  aug = ImageDataGenerator(
	rotation_range=20,
	zoom_range=0.15,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.15, horizontal_flip=True)

  model = models.Sequential()
  #block_1
  model.add(layers.Conv2D(filters=32, kernel_size = 2, padding = 'same',activation = 'relu',input_shape=(32,32,3)))
  model.add(layers.MaxPooling2D(pool_size=2))

  #block_2
  model.add(layers.Conv2D(filters=64, kernel_size = 2, padding = 'same',activation = 'relu'))
  model.add(layers.MaxPooling2D(pool_size=2))

  
  if(Dropout == True):
    #block_3
    model.add(layers.Conv2D(filters=128, kernel_size = 2, padding = 'same',activation = 'relu'))
    model.add(layers.MaxPooling2D(pool_size=2))
    model.add(layers.Dropout(0.5))
    #block_4
    model.add(layers.Flatten())
    model.add(layers.Dense(128,activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(10,activation='softmax')) 

  
  else:
    #block_3
    model.add(layers.Conv2D(filters=128, kernel_size = 2, padding = 'same',activation = 'relu'))
    model.add(layers.MaxPooling2D(pool_size=2))
    #blcok_4
    model.add(layers.Flatten())
    model.add(layers.Dense(128,activation='relu'))
    model.add(layers.Dense(10,activation='softmax'))

  #Compile the model
  model.compile(optimizer=tf.keras.optimizers.SGD(
  learning_rate=0.1, momentum=0.0, nesterov=True, name='SGD'),
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])

  #train the model
  if(data_augmentation == True):
    history = model.fit(aug.flow(train_images, train_labels), epochs=epochs, 
                      validation_data=(test_images, test_labels))
  else:
    history = model.fit(train_images, train_labels, epochs=epochs, 
                      validation_data=(test_images, test_labels))
  return history, model

# without dropout & data augmentation

#load data
train_images, train_labels, test_images, test_labels = load_data()

history, model=define_model(train_images, train_labels, test_images, test_labels, 45, Dropout = False, data_augmentation = False)

#Evaluate the model
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
#plt.ylim([0.3, 1.0])
plt.legend(loc='lower right')
plt.savefig('pointf_witout aug&dropout.png')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

## with dropout only

#load data
train_images, train_labels, test_images, test_labels = load_data()

history, model=define_model(train_images, train_labels, test_images, test_labels, 45, Dropout = True, data_augmentation = False)

#Evaluate the model
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
#plt.ylim([0.3, 1.0])
plt.legend(loc='lower right')
plt.savefig('pointf_withdropout.png')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# with data augmentation
#load data
train_images, train_labels, test_images, test_labels = load_data()

history, model=define_model(train_images, train_labels, test_images, test_labels, 45, Dropout = False, data_augmentation = True)

#Evaluate the model
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('accuracy')
#plt.ylim([0.3, 1.0])
plt.legend(loc='lower right')
plt.savefig('pointf_with_aug.png')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)