import cv2
import numpy as np

from .binary_bgr_convert import binary_bgr_convert


def convert_green_to_black(image_wo_alpha: np.ndarray) -> np.ndarray:
    """Convert green element to white element.

    Args:
        image_w_alpha(_type_):背景が緑なアルファチャンネルを含まない画像
    Returns:
        _type_:緑色の背景を黒色に置換した画像
    """
    hsv_img = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)
    binary_image = cv2.inRange(hsv_img, (62, 100, 0), (79, 255, 255))
    binary_image = cv2.bitwise_not(binary_image)
    binary_image = binary_bgr_convert(binary_image)

    transparent = (255, 255, 255)
    result_image = np.where(binary_image == transparent, image_wo_alpha, binary_image)
    return result_image
