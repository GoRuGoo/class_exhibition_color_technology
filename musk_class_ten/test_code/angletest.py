import cv2

front_image = cv2.imread("/home/gorugo/musk_class_ten/girl.png")
hsv_image = cv2.cvtColor(front_image, cv2.COLOR_BGR2HSV)
binary_image = cv2.inRange(hsv_image, (62, 100, 0), (79, 255, 255))

contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(front_image, contours, -1, (0, 255, 0), 2)
cv2.imwrite("tst.png", output)

# # 面積が最大の輪郭を取得する
# contour = max(contours, key=lambda x: cv2.contourArea(x))
# cv2.imwrite("tst.png",contour)
# # マスク画像を作成する。
# mask = np.zeros_like(bin_img)
# cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
# imshow(mask)
