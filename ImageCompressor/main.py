import cv2
import glob
src = "../Cnn/correct_answer/youtube_music/player/*.png"
i = 0

for img in glob.glob("../Cnn/correct_answer/youtube_music/player/*.png"):
       grayimg= cv2.imread(img, cv2.IMREAD_GRAYSCALE)
       grayimg = cv2.resize(grayimg, dsize=(0, 0),fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
       grayimg = cv2.resize(grayimg, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
       dst_name = "./result/youtube/player/" + str(i) + ".png"
       cv2.imwrite(dst_name, grayimg)
       print(i)
       i+=1
