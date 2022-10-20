import cv2
import numpy as np
from functions.binary_bgr_convert import binary_bgr_convert
from functions.create_black_image_array import create_black_image_array

fg_img = cv2.imread("/home/gorugo/musk_class_ten/girl.png")

bg_img = create_black_image_array(fg_img)


hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)

binary_image = cv2.inRange(hsv, (62, 100, 0), (79, 255, 255))
binary_image = cv2.bitwise_not(binary_image)
binary_image = binary_bgr_convert(binary_image)

transparent = (255, 255, 255)
result = np.where(binary_image == transparent, fg_img, binary_image)
print(result.shape)
cv2.imwrite("result.png", result)
