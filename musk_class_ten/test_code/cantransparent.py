import cv2
import numpy as np
from functions.create_black_image_array import create_black_image_array
from functions.binary_bgr_convert import binary_bgr_convert

# 画像を読み込む。
fg_img = cv2.imread("/home/gorugo/musk_class_ten/girl.png")

bg_img = create_black_image_array(fg_img)
# height,width = fg_img.shape[:2]
# dumy_binary = np.zeros((height,width,1))


# HSV に変換する。
hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)

binary_image = cv2.inRange(hsv, (62, 100, 0), (79, 255, 255))
binary_image = cv2.bitwise_not(binary_image)
binary_image = binary_bgr_convert(binary_image)
print(fg_img.shape,binary_image.shape)
# print(dumy_binary.shape)
# dst = np.dstack((binary_image,dumy_binary))
# dumy_binary_second = np.zeros((height,width,1))
# dumy_binary_third = np.full((height,width),255)
# dst_second = np.dstack((dumy_binary_second,dumy_binary_third))
# dst = np.dstack((dst,dst_second))
# cv2.imwrite("dst.png",dst)
transparent = (255,255,255)
result = np.where(binary_image==transparent,fg_img,binary_image)
cv2.imwrite("result.png",result)

















# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# output = cv2.drawContours(fg_img,contours,-1,(0,255,0),2)
# cv2.imwrite("output.png",output)
# # 面積が最大の輪郭を取得する
# contour = max(contours, key=lambda x: cv2.contourArea(x))

# # マスク画像を作成する。
# mask = np.zeros_like(binary_image)
# cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
# cv2.imwrite("mask.png",mask)
# # 貼り付け位置
# x, y = 30, 10

# # 幅、高さは前景画像と背景画像の共通部分をとる
# w = min(fg_img.shape[1], bg_img.shape[1] - x)
# h = min(fg_img.shape[0], bg_img.shape[0] - y)

# # 合成する領域
# fg_roi = fg_img[:h, :w]
# bg_roi = bg_img[y : y + h, x : x + w]

# # 合成する。
# dst = np.where(mask[:h, :w, np.newaxis] == 0, bg_roi, fg_roi)
# cv2.imwrite("tete.png",dst)