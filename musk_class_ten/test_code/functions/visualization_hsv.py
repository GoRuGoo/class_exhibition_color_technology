import cv2
import matplotlib.pyplot as plt


def show_img(path):
    img = cv2.imread(path)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = img2[:, :, 0], img2[:, :, 1], img2[:, :, 2]
    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])
    plt.plot(hist_h, color="r", label="h")
    plt.plot(hist_s, color="g", label="s")
    plt.plot(hist_v, color="b", label="v")
    plt.legend()
    plt.show()

    return hist_h, hist_s, hist_v


h, s, v = show_img("komura.png")
#
