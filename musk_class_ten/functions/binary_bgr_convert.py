import cv2
import numpy as np


def binary_bgr_convert(bin_image: np.ndarray) -> np.ndarray:
    """バイナリイメージをBGRイメージに変換する."""
    binary_height, binary_width = bin_image.shape[:2]

    dummy_binary = np.full((binary_height, binary_width, 2), 255)
    first_binary, second_binary = cv2.split(dummy_binary[:, :, :2])
    dst_binary = np.dstack((bin_image, first_binary, second_binary))
    dst_binary[:, :, 1] = np.where(dst_binary[:, :, 0] == 0, 0, 255)
    dst_binary[:, :, 2] = np.where(dst_binary[:, :, 0] == 0, 0, 255)
    dst_binary_eight = dst_binary.astype(np.uint8)
    return dst_binary_eight
