import cv2
import numpy as np


def transparent_black_ground(image_w_alpha_black_background: np.ndarray) -> np.ndarray:
    """Transparent black ground.

    Args:
        image_w_alpha_black_background(_type_):背景が黒なアルファチャンネルを含んだ画像
    Returns:
        _type_:黒背景を透過した画像
    """
    b_ch, g_ch, r_ch, a_ch = cv2.split(image_w_alpha_black_background[:, :, :4])

    judge = (
        (image_w_alpha_black_background[:, :, 0] < 7)
        & (image_w_alpha_black_background[:, :, 1] < 7)
        & (image_w_alpha_black_background[:, :, 2] < 7)
    )

    image_w_alpha_black_background[:, :, 3] = np.where(
        judge, 0, image_w_alpha_black_background[:, :, 3]
    )

    return image_w_alpha_black_background
