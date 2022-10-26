from multiprocessing.sharedctypes import Value
from turtle import width
import cv2
import numpy as np

def create_black_image_array(image:np.array)->np.ndarray:
    """入力された画像と同じサイズの黒画像を生成する
    Args:
        image(_type_):アルファチャンネルを含まない画像のnumpy配列
    Returns:
        _type_:入力画像と同じサイズの黒画像のnumpy配列
    """
    height,width = image.shape[:2]
    black_image = np.zeros((height,width,3))
    return black_image