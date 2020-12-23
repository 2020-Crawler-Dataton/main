import tensorflow as tf
import os
import numpy as np
import cv2
import shutil

def move_file():
    print()

class classify():
    data = []
    tmp = os.path.join("D:/Study/2020-Crawler-Dataton/main/Selenium/Instagram/tmp")
    filenames = []
    def __init__(self):
        print()

    def predict(self, data,filename):
        data = data/255.
        data = tf.image.resize([data], (224, 224))
        if os.path.isfile("./model.h5"):
            base_model = tf.keras.applications.ResNet50(input_shape=(224, 224, 3))
            base_model = tf.keras.models.Model(base_model.inputs, base_model.layers[-2].output)
            x = base_model.output
            pred = tf.keras.layers.Dense(3, activation='softmax')(x)

            model = tf.keras.models.Model(inputs=base_model.input, outputs=pred)
            opt = tf.keras.optimizers.Adam(learning_rate=0.0001)

            model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['acc'])
            model = tf.keras.models.load_model("./model.h5")
            predict = np.argmax(model.predict(data))
            dir = "./"+str(predict)+"/"+filename
            shutil.move(self.tmp+"/"+filename, dir+filename)

    def load_img(self,folder):
        data_path = os.listdir(folder)
        for i in range(len(data_path)):
            img = cv2.imread(folder + "/" + data_path[i])
            img = cv2.resize(img, (256, 256))
            self.data.append(img)
            self.filenames.append(data_path[i])

        return True

    def run(self):
        if self.load_img(self.tmp):
            self.data = np.array(self.data)
            for i in range(np.size(self.data, axis=0)):
                self.predict(self.data[i],self.filenames[i])

a = classify()
a.run()