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

    first_judge = hsv_image_wo_alpha[:, :, 0] > 20
    # first_judge = ((hsv_image_wo_alpha[:,:,0]>73)&(hsv_image_wo_alpha[:,:,0]<74))&((hsv_image_wo_alpha[:,:,1]>253)&(hsv_image_wo_alpha[:,:,1]<254))&((hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172))
    # second_judge = (hsv_image_wo_alpha[:,:,1]>253)&(hsv_image_wo_alpha[:,:,1]<254)&(hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172)
    # third_judge = (hsv_image_wo_alpha[:,:,2]>170)&(hsv_image_wo_alpha[:,:,2]<172)

    hsv_image_wo_alpha[:, :, 0] = np.where(first_judge, 0, hsv_image_wo_alpha[:, :, 0])

    convert_bgr_image = cv2.cvtColor(hsv_image_wo_alpha, cv2.COLOR_HSV2BGR)
    return convert_bgr_image
