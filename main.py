from sys import argv
import numpy as np
import parsing as par

CHAR_RAMP = "@%#*+=-:. "
CANT_CAR = len(CHAR_RAMP)-1


def obtain_char(p):
    ind = 0
    bright = (p[0] * 0.299 + p[1] * 0.587 + p[2] * 0.144)/1.3
    if bright != 0:
        ind = int(bright*CANT_CAR)
    return CHAR_RAMP[ind]


def obtain_ascci(narr: np.ndarray):
    result = []
    for fil in narr:
        for pixel in fil:
            result.append(obtain_char(pixel))
            result.append(" ")
        result.append("\n")
    return "".join(result).rstrip()


if __name__ == "__main__":
    if len(argv) != 2:
        print("Use: python3 main.py <image-name>")
    else:
        try:
            if argv[1].endswith(".png"):
                img = par.parse_png(argv[1])
                print(obtain_ascci(img))
        except FileNotFoundError:
            print("File doesn't exist")
