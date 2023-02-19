import numpy as np


def binary_to_bgr_convert(bin_image: np.ndarray) -> np.ndarray:
    """バイナリイメージをBGRイメージに変換する.
    Args:
        bin_image(_type_):二次元配列のバイナリイメージ

    Returns:
        _type_:バイナリイメージの色を保ったままBGR形式にしたイメージ

    See Also:
    バイナリと同じサイズの全要素255配列を三次元方向に2個用意する
    ->連結->このままだと色がおかしいので三次元方向0番目の要素かつ、
    白であったらそれに合うように三次元方向の2個目3個目も変更
    ->np.uint8型に直して変換

    """
    binary_height, binary_width = bin_image.shape[:2]

    dummy_binary = np.full((binary_height, binary_width, 2), 255)
    dst_binary = np.dstack((bin_image, dummy_binary))
    dst_binary[:, :, 1] = np.where(dst_binary[:, :, 0] == 0, 0, 255)
    dst_binary[:, :, 2] = np.where(dst_binary[:, :, 0] == 0, 0, 255)
    dst_binary_eight = dst_binary.astype(np.uint8)
    return dst_binary_eight
