import cv2

image = cv2.imread("demo.png", cv2.IMREAD_UNCHANGED)

print(image.shape)
