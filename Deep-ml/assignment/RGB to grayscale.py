# https://www.scaler.com/academy/mentee-dashboard/class/399321/assignment/problems/251644?navref=cl_tt_nv

import numpy as np


def rgb_to_gray(image: np.ndarray) -> np.ndarray:
    """
    input:
      image -> np.ndarray, shape (H, W, 3), dtype uint8
    output:
      np.ndarray, shape (H, W), dtype float64, values in [0,1]
    """
    # Normalize to [0,1]
    global gray
    image = image.astype(np.float64) / 255

    if image.ndim == 1 and image.shape[0] == 1:
        gray = 0.2126 * image[0] + 0.7152 * image[1] + 0.0722 * image[2]

    if image.ndim == 3 and image.shape[2] == 3:
        gray = (0.2126 * image[:, :, 0] +
                0.7152 * image[:, :, 1] +
                0.0722 * image[:, :, 2])
    return gray
