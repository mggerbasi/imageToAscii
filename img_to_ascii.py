from sys import argv
import math
import cv2
import numpy as np
import matplotlib.image as mpimg

CHAR_RAMP = "@%#*+=-:. "
CANT_CAR = len(CHAR_RAMP)-1
MAX_PIXELS = 4000


def parse_png(filename: str) -> np.ndarray:
    img_narr = mpimg.imread(filename)
    h, w, _ = img_narr.shape
    while h*w > MAX_PIXELS and h > 10 and w > 10:
        h //= 2
        w //= 2
    resized_img = cv2.resize(img_narr, (w, h))
    return resized_img


def obtain_char(p) -> str:
    ind = 0
    bright = math.sqrt((p[0]**2 * 0.299 + p[1]**2 * 0.587 + p[2]**2 * 0.144)/1.03)
    if len(p) == 4 and p[3] == 0:
        bright = 1
    if bright != 0:
        ind = int(bright*CANT_CAR)
    return CHAR_RAMP[ind]


def obtain_ascci(img_narr: np.ndarray, file_res: str):
    if not file_res.endswith(".txt"):
        file_res += ".txt"
    with open(file_res, "w") as f:
        for row in img_narr:
            for px in row:
                f.write(obtain_char(px) + " ")
            f.write("\n")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Use: python3 img_to_ascii.py <image-name> <result-name>")
    else:
        try:
            if argv[1].endswith(".png"):
                f_res = "_.txt"
                if len(argv) > 2:
                    f_res = argv[2]
                img = parse_png(argv[1])
                obtain_ascci(img, f_res)

        except FileNotFoundError:
            print("File doesn't exist")
