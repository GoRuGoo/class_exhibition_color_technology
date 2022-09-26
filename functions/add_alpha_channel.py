from pickletools import uint1, uint8
from sys import addaudithook
from turtle import width
import cv2
import numpy as np


def add_alpha_channel_255(image_path:str)->np.ndarray:
    """アルファチャンネルが無いpng画像に透過0%のアルファチャンネルを追加する

    Args:
        image_path (_type_): アルファチャンネルを追加したい画像のパス
    Returns:
        _type_: 色変更した画像のnumpy配列
    """

    image_wo_alpha = cv2.imread(image_path)
    height,width = image_wo_alpha.shape[:2]
    b_ch,g_ch,r_ch = cv2.split(image_wo_alpha[:,:,:3])
    alpha_ch = np.full((height,width),255)
    dst = np.dstack((b_ch,g_ch,r_ch,alpha_ch))
    dst_eight = dst.astype(np.uint8)

    return dst_eight
