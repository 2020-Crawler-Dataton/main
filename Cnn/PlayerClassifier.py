import tensorflow as tf
from sklearn.utils import shuffle
import pandas as pd
import os
import cv2
import numpy as np

def load_img(folder):
    data_path = os.listdir(folder)
    for i in range(len(data_path)):
        img = cv2.imread(folder + "/" + data_path[i])
        img = cv2.resize(img, (256, 256))
        data.append(img)

insta1 = os.path.join("D:/Study/2020-Crawler-Dataton/main/Selenium/Instagram/img")

bugs_player = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/bugs/player")
bugs_playist = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/bugs/playlist")

melon_insta = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/melon/instagram")
melon_player = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/melon/player")
melon_playlist = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/melon/playerlist")

youtube_player = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/youtube_music/player")
youtube_playlist = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/correct_answer/youtube_music/playlist")

wrong_answer = os.path.join("D:/Study/2020-Crawler-Dataton/main/Cnn/wrong_answer")
data = []


load_img(insta1)
load_img(bugs_player)
load_img(bugs_playist)
load_img(melon_insta)
load_img(melon_player)
load_img(melon_playlist)
load_img(youtube_player)
load_img(youtube_playlist)
load_img(wrong_answer)


doc = pd.read_csv("output.csv", quotechar='.')
doc.info()
labels = doc.Class.tolist()
labels = np.array(labels).astype('float32')

data, y = shuffle(data, labels)

x = tf.image.resize(data, (224, 224))
y = tf.one_hot(y, 3)

print(x.shape)
print(y.shape)

x_train = x[:1000]
y_train = y[:1000]
x_test = x[1000:]
y_test = y[1000:]

print("!")
base_model = tf.keras.applications.ResNet50(weights='imagenet', input_shape=(224, 224, 3))
base_model = tf.keras.models.Model(base_model.inputs, base_model.layers[-2].output)
x = base_model.output
pred = tf.keras.layers.Dense(3, activation='softmax')(x)
print("!")
model = tf.keras.models.Model(inputs=base_model.input, outputs = pred)

opt = tf.keras.optimizers.Adam(learning_rate=0.0001)

model.compile(optimizer=opt,loss = 'categorical_crossentropy', metrics=['acc'])
if os.path.isfile("model.h5"):
     model = tf.keras.models.load_model("model.h5")
model.summary()

history = model.fit(x=x_train, y= y_train, batch_size=16,
                    epochs=5, validation_data=(x_test, y_test))

print('validation accuracy')
print(history.history['val_acc'][-1])

results = model.evaluate(x_test, y_test, batch_size=16)
print('test accuracy')
print(results[1])
model.save('./model.h5')