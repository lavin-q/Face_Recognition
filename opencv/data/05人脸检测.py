# 导包
import cv2 as cv


# 定义人脸识别函数
def face_detect_demo(img_file):
    # 图片变为灰色，减少像素噪点影响
    gary = cv.cvtColor(img_file, cv.COLOR_BGR2GRAY)
    # 模型地址
    face_detect = cv.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')

    face = face_detect.detectMultiScale(gary, 1.01)
    for x, y, w, h in face:
        cv.rectangle(img_file, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img_file)


img = cv.imread('../pictures/1123.jpg')
# gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gary', gary)
face_detect_demo(img)
while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()
