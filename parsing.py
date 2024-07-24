import matplotlib.image as mpimg
import numpy as np
import cv2

MAX_PIXELS = 4000


def parse_png(filename: str) -> np.ndarray:
    img = mpimg.imread(filename)
    h, w, _ = img.shape
    while h*w > MAX_PIXELS and h > 10 and w > 10:
        h //= 2
        w //= 2
    resized_img = cv2.resize(img, (w, h))
    return resized_img
