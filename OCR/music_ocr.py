import io  # 파일을 읽고 쓰기위한 모듈
import os  # os의 기능을 사용하기 위한 모듈

# Imports the Google Cloud client library
from google.cloud import vision

client = vision.ImageAnnotatorClient()
filenames = os.listdir('./music_image')

for filename in filenames:
    path = os.path.join('./music_image', filename)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    with open('./music_txt/' + filename[0:-4] + '.txt', "w") as f:
        f.write(texts[0].description)
