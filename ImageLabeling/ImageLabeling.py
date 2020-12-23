import cv2
import csv
import glob
import numpy as np

src = "../Cnn/correct_answer/youtube_music/player/*.png"
i = 0
import pandas as pd
doc = pd.read_csv("output.csv", quotechar='.')
doc.info()
a = doc.filename.tolist()
for i in a:
    filename = "./img/"+i


