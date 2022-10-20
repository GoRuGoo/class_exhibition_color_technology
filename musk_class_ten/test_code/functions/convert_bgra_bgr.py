import numpy as np


def convert_bgra_to_bgr(image: np.ndarray, return_mask: bool) -> np.ndarray:
    """Convert RGBA image to RGB image.

    Args:
        image (_type_): RGBA image
        return_mask (_type_):アルファチャンネルの配列をreutrnするかどうか
    Returns:
        _type_: BGR imageもしくは BGRとA
    """
    mask = image[:, :, 3]
    if return_mask:
        return (image[:, :, :3] * np.dstack([mask / 255] * 3)).astype(np.uint8), mask
    else:
        return (image[:, :, :3] * np.dstack([mask / 255] * 3)).astype(np.uint8)
