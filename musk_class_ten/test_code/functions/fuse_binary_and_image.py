from email.mime import image
from multiprocessing.sharedctypes import Value
from turtle import heading
from typing import Tuple
import cv2
import numpy as np

def add_alpha_channel_255(image:np.ndarray) -> np.ndarray:
    """アルファチャンネルが無いpng画像に透過0%のアルファチャンネルを追加する.

    Args:
        image_path (_type_): アルファチャンネルを追加したい画像のパス
    Returns:
        _type_: 色変更した画像のnumpy配列
    """

    height, width = image.shape[:2]
    b_ch, g_ch, r_ch = cv2.split(image[:, :, :3])
    alpha_ch = np.full((height, width), 255)
    dst = np.dstack((b_ch, g_ch, r_ch, alpha_ch))
    dst_eight = dst.astype(np.uint8)

    return dst_eight


def fuse_binary_and_image(image_wo_alpha:np.ndarray,bin_image:np.ndarray)->Tuple[np.ndarray,np.ndarray]:
    image_height,image_width = image_wo_alpha.shape[:2]
    binary_height,binary_width = bin_image.shape[:2]
    if (image_height!=binary_height) and (image_width!=binary_width):
        raise ValueError("Image size and binary image size are different")

    dst_image = add_alpha_channel_255(image_wo_alpha)

    dummy_binary = np.full((binary_height,binary_width,2),255)
    binary_alpha = np.full((binary_height,binary_width),255)
    first_binary,second_binary = cv2.split(dummy_binary[:,:,:2])
    dst_binary = np.dstack((bin_image,first_binary,second_binary,binary_alpha))
    dst_binary[:,:,1] = np.where(dst_binary[:,:,0]==0,0,255)
    dst_binary[:,:,2] = np.where(dst_binary[:,:,0]==0,0,255)
    cv2.imwrite("binary.png",dst_binary)
    dst_binary_eight = dst_binary.astype(np.uint8)
    return dst_image,dst_binary_eight
