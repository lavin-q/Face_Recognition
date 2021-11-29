# 导入cv模块
import cv2 as cv


# 定义检测函数
def face_detect_demo(img):
    gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
    # 方法参数解释
    # image:传入的图片
    # scaleFactor: 每次循环缩放的比例
    # minNeighbors: 确定次数，输入数字表示多次确认后方可确定人脸
    # flags: 0
    # minSize: 图片中人脸最小有多小
    # maxSize: 图片中人脸最大有多大
    face = face_detect.detectMultiScale(gary)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)


# 读取视频或摄像头(输入参数为0,表示默认摄像头，其他表示视频或其他摄像头)
cap = cv.VideoCapture('../pictures/2021-11-25-105819.webm')
# cap = cv.VideoCapture(0)
cap.read()
# img = cv.imread('face5.jpeg')

while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(1):
        break
# 释放内存
cv.destroyAllWindows()
# 释放摄像头
cap.release()
