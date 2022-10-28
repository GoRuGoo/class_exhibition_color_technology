import cv2
import numpy as np

from .binary_to_bgr_convert import binary_to_bgr_convert


def convert_green_to_black(
    image_wo_alpha: np.ndarray,
    min_hue: int,
    max_hue: int,
    min_sat: int,
    max_sat: int,
    judge_mani_black: int,
    detect_min_bright: int,
) -> np.ndarray:
    """Convert green element to white element.

    Args:
        image_w_alpha(_type_):背景が緑なアルファチャンネルを含まない画像
        min_hue(_type_):最小値のHUE
        max_hue(_type_):最大値のHUE
        min_sat(_type_):最小値のSAT
        max_sat(_type_):最大値のSAT
        judge_min_bright(_type_):黒の服に対応するかどうか判定。boolでないのはFormからintが送信されるから
        detect_min_bright(_type_):検出する最小の明るさ
    Returns:
        _type_:緑色の背景を黒色に置換した画像
    """

    if judge_mani_black:
        gray_scale_img = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2GRAY)
        ret, binary_image = cv2.threshold(
            gray_scale_img, detect_min_bright, 255, cv2.THRESH_BINARY
        )
        binary_image = cv2.bitwise_not(binary_image)
        print(judge_mani_black)
    else:
        hsv_img = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)
        binary_image = cv2.inRange(
            hsv_img, (min_hue, min_sat, 0), (max_hue, max_sat, 255)
        )
        binary_image = cv2.bitwise_not(binary_image)

    # 輪郭を取る
    countours, hierarchy = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    binary_image = binary_to_bgr_convert(binary_image)
    # バイナリ画像に輪郭を描画して塗りつぶす
    after_fill_binary_image = cv2.drawContours(
        binary_image, countours, -1, (255, 0, 0), 3
    )
    cv2.fillPoly(after_fill_binary_image, countours, 255)
    after_fill_binary_image[:, :, 1] = np.where(
        after_fill_binary_image[:, :, 0] == 0, 0, 255
    )
    after_fill_binary_image[:, :, 2] = np.where(
        after_fill_binary_image[:, :, 0] == 0, 0, 255
    )

    transparent = (255, 255, 255)
    result_image = np.where(
        after_fill_binary_image == transparent, image_wo_alpha, after_fill_binary_image
    )
    return result_image
