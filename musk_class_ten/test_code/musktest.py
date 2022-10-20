from unittest import makeSuite
import cv2
import numpy as np
from create_black_image_array import create_black_image_array

initial_image = cv2.imread("/home/gorugo/musk_class_ten/girl.png")
gray_scale_image = cv2.cvtColor(initial_image,cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(initial_image,cv2.COLOR_BGR2HSV)
binary_image = cv2.inRange(hsv_image,(62,100,0),(79,255,255))
binary_image = cv2.bitwise_not(binary_image)
cv2.imwrite("binary.png",binary_image)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
