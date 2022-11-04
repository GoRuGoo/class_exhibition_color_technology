import io

import cv2
import matplotlib.pyplot as plt
import numpy as np


def make_visualization_graph(image: np.ndarray) -> np.ndarray:
    h, s, v = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    hist_h = cv2.calcHist([h], [0], None, [256], [0, 256])
    hist_s = cv2.calcHist([s], [0], None, [256], [0, 256])
    hist_v = cv2.calcHist([v], [0], None, [256], [0, 256])
    plt.plot(hist_h, color="r", label="H")
    plt.plot(hist_s, color="g", label="S")
    plt.plot(hist_v, color="b", label="V")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    enc = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    dst = cv2.imdecode(enc, 1)
    w, h = dst.shape[:2]
    setting_w = 656
    setting_h = 496
    dst = cv2.resize(dst, dsize=(setting_w, setting_h), fx=w / 656, fy=h / 496)
    dst = cv2.resize(dst, dsize=None, fx=1.1, fy=1.1)

    plt.cla()

    return dst
