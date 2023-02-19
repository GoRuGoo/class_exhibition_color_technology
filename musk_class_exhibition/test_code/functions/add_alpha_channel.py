import cv2
import numpy as np


def add_alpha_channel_255(image: np.ndarray) -> np.ndarray:
    """アルファチャンネルが無いpng画像に透過0%のアルファチャンネルを追加する.

    Args:
        image_path (_type_): アルファチャンネルを追加したい画像のnumpy配列
    Returns:
        _type_: 色変更した画像のnumpy配列
    """
    if len(image.shape) != 3:
        raise ValueError("The number of dimensions of the image is different")
    height, width = image.shape[:2]
    b_ch, g_ch, r_ch = cv2.split(image[:, :, :3])
    alpha_ch = np.full((height, width), 255)
    dst = np.dstack((b_ch, g_ch, r_ch, alpha_ch))
    dst_eight = dst.astype(np.uint8)

    return dst_eight
