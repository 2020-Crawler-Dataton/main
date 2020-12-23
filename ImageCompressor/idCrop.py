import cv2
import glob

src = "../Cnn/correct_answer/youtube_music/player/*.png"
i = 0
for img in glob.glob("../Cnn/correct_answer/youtube_music/player/*.jpg"):
       grayimg= cv2.imread(img, cv2.IMREAD_GRAYSCALE)
       cv2.imwrite(img, grayimg)
       print(i)
       i+=1

