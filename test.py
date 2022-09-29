import cv2
import numpy as np

from functions.add_alpha_channel import add_alpha_channel_255
from functions.convert_bgra_bgr import convert_bgra_to_bgr

image = add_alpha_channel_255("girl.png")

image_wo_alpha, mask = convert_bgra_to_bgr(image, True)
image_hsv = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)

# image_hsv[:, :, 3] = np.where(((image_hsv[:,:,0]>74)&(image_hsv[:,:,0]<75))&
# ((image_hsv[:,:,1]>98)&(image_hsv[:,:,1]<101))&((image_hsv[:,:,2]>67)&(image_hsv[:,:,2]<69)),
#  0, 255)

image_hsv[:, :, 3] = np.where(
    (image_hsv[:, :, 0] > 74) & (image_hsv[:, :, 0] < 75), 0, 255
)

image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("demo", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
