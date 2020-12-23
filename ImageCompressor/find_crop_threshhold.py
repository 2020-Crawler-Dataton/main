import cv2
import numpy as np
def img_crop(src):
    one = None
    two = None
    dst = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    row = int(np.size(dst, axis=0) * 0.3)
    start = dst[0][0]
    col = 0
    condition = True
    while (condition):
        if dst[row][col] > start * 2:
            one = col
            condition = False
        col += 1
    col = np.size(dst, axis=1) - int(one * 0.5)
    condition = True
    while (condition):
        if dst[row][col] > start * 2:
            two = col
            condition = False
        col -= 1
    print(one,two)
    dst = dst[:, one:two + 1]
    condition = True
    row = 0
    cut = None
    while (condition):
        if dst[row][0] > start:
            cut = row
            condition = False
        row += 1
    dst = dst[cut:np.size(dst, axis=0) - 1 - cut, :]
    print(cut)
    return dst