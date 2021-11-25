# 导入cv模块
import cv2 as cv

# 读取图片
img = cv.imread('face3.jpg')
# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示图片
cv.imshow('read_img', img)
# 显示修改后的图片
cv.imshow('resize_img', resize_img)
# 打印原图尺寸大小
print('未修改', img.shape)
# 打印修改后的图尺寸大小
print('修改后', resize_img.shape)
# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
