import cv2
import numpy as np
import os
# coding=utf-8
import urllib
import urllib.request
import hashlib

# 加载训练数据集文件
recogizer = cv2.face.LBPHFaceRecognizer_create()
recogizer.read('../trainer/trainer.yml')
names = []
warningtime = 0


# 准备识别的图片
def face_detect_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度
    # 检测人脸
    face_detector = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detector.detectMultiScale(gray)
    # face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    for x, y, w, h in face:
        # 未捕捉到人脸时画面继续采样
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        print('标签id:', ids, '置信评分：', confidence)
        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
                # warning()
                warningtime = 0
            cv2.putText(img, 'unknown', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            # str(names[names.index(ids)])
            # print(names.index(str(ids)))
            cv2.putText(img, names[names.index(str(ids))], (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                        (0, 255, 0), 1)
    cv2.imshow('result', img)
    # print('bug:',ids)


def name():
    path = '../pictures/'
    # names = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.', 2)[0])
        names.append(name)


cap = cv2.VideoCapture(0)
name()
while True:
    flag, frame = cap.read()
    # cv2.imshow('vi', frame)
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
cap.release()
# print(names)
