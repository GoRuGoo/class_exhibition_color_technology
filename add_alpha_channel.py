import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFilter

image_wo_alpha = cv2.imread("girl.png")

b_ch,g_ch,r_ch = cv2.split(image_wo_alpha[:,:,:3])

alpha_ch = np.full((1087,1600),255)

dst = np.dstack((b_ch,g_ch,r_ch,alpha_ch))
cv2.imwrite("test.png",dst)