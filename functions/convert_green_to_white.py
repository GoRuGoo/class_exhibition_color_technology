from curses import mousemask
from distutils.archive_util import make_archive
import threading
from typing import Tuple
import cv2
import numpy as np

from functions.convert_bgra_bgr import convert_bgra_to_bgr


def convert_green_to_white(image_w_alpha: np.ndarray) -> np.ndarray:
    """Convert green element to white element.

    Args:
        image_w_alpha(_type_):背景が緑なアルファチャンネルを含んだ画像
    Returns:
        _type_:緑色の背景を白色に置換した画像
    """

    image_wo_alpha, mask = convert_bgra_to_bgr(image_w_alpha, True)
    hsv_image_wo_alpha = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)

    first_judge = (hsv_image_wo_alpha[:, :, 0] > 71.3) & (hsv_image_wo_alpha[:,:,0]<77.3)
    second_judge = (hsv_image_wo_alpha[:,:,0]==0) & ((hsv_image_wo_alpha[:,:,1]>230)&(hsv_image_wo_alpha[:,:,1]<255))
    third_judge = (hsv_image_wo_alpha[:,:,0]==0)&(hsv_image_wo_alpha[:,:,1]==0)&((hsv_image_wo_alpha[:,:,2]>150)&(hsv_image_wo_alpha[:,:,2]<155))
    # first_judge = ((hsv_image_wo_alpha[:,:,0]>73)&(hsv_image_wo_alpha[:,:,0]<74))&((hsv_image_wo_alpha[:,:,1]>253)&(hsv_image_wo_alpha[:,:,1]<254))&((hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172))
    # second_judge = (hsv_image_wo_alpha[:,:,1]>253)&(hsv_image_wo_alpha[:,:,1]<254)&(hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172)
    # third_judge = (hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172)

    hsv_image_wo_alpha[:, :, 0] = np.where(first_judge, 0, hsv_image_wo_alpha[:, :, 0])
    hsv_image_wo_alpha[:,:,1] = np.where(second_judge,0,hsv_image_wo_alpha[:,:,1])
    hsv_image_wo_alpha[:,:,2] = np.where(third_judge,255,image_wo_alpha[:,:,2])

    convert_bgr_image = cv2.cvtColor(hsv_image_wo_alpha, cv2.COLOR_HSV2BGR)
    b_ch,g_ch,r_ch = cv2.split(convert_bgr_image[:,:,:3])
    convert_bgr_image_w_alpha = np.dstack((b_ch,g_ch,r_ch,mask))
    return convert_bgr_image_w_alpha