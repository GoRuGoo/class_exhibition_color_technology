import cv2
import numpy as np

from .binary_to_bgr_convert import binary_to_bgr_convert


def convert_green_to_black(image_wo_alpha: np.ndarray) -> np.ndarray:
    """Convert green element to white element.

    Args:
        image_w_alpha(_type_):背景が緑なアルファチャンネルを含まない画像
    Returns:
        _type_:緑色の背景を黒色に置換した画像
    """
    hsv_img = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)
    binary_image = cv2.inRange(hsv_img, (60, 0, 0), (90, 255, 255))
    binary_image = cv2.bitwise_not(binary_image)

    cv2.imwrite("default_binary.png", binary_image)

    countours, hierarchy = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # 2値化する
    binary_image = binary_to_bgr_convert(binary_image)
    output = cv2.drawContours(binary_image, countours, -1, (255, 0, 0), 3)

    cv2.imwrite("binary_rinkaku.png", output)
    cv2.fillPoly(output, countours, 255)

    cv2.imwrite("fill.png", output)
    transparent = (255, 255, 255)
    result_image = np.where(binary_image == transparent, image_wo_alpha, binary_image)
    return result_image
