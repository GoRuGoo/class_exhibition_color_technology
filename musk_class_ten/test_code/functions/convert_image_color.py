import cv2
import numpy as np


def convert_image_color(
    self,
    image: np.ndarray,
    hue: float,
    saturation: float,
    value: float,
    include_alpha_ch: bool,
) -> np.ndarray:
    """アルファチャンネル付きのRGB=(0,0,255)の画像の色を、指定したHSV数値の色に変更する.

    Args:
        image(_type_): B255で塗りつぶした透過メイク素材、1024x1024
        hue(_type_):HSVのHueの数値
        saturation(_type_):HSVのSaturationの数値
        value(_type_):HSVのVvalueの数値
        include_alpha_ch(_type_):returnする画像にアルファチャンネルを含むか否か
    Return:
        np.ndarray:任意の色、設定に変更したメイクのnumpy配列
    """
    image_wo_alpha, mask = self.convert_bgra_to_bgr(image, True)
    image_hsv = cv2.cvtColor(image_wo_alpha, cv2.COLOR_BGR2HSV)

    image_hsv[:, :, 0] = np.where(
        image_hsv[:, :, 0] == 120, hue / 2, image_hsv[:, :, 0]
    )
    image_hsv[:, :, 1] = np.where(
        image_hsv[:, :, 1] == 255, saturation, image_hsv[:, :, 1]
    )
    image_hsv[:, :, 2] = np.where(
        image_hsv[:, :, 2] != 0,
        (value * (image_hsv[:, :, 2] / 255)),
        image_hsv[:, :, 2],
    )
    # ↑グラデーションの比率を保ったまま、明度を変更する

    image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    if include_alpha_ch:
        b_ch, g_ch, r_ch = cv2.split(image_bgr[:, :, :3])
        image_bgr_w_alpha = cv2.merge((b_ch, g_ch, r_ch, mask))
        return image_bgr_w_alpha
    else:
        return image_bgr
