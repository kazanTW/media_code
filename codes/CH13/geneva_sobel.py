import cv2
from math import sqrt
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/geneva.jpg', cv2.IMREAD_GRAYSCALE)

    height, width = src.shape
    dst = np.zeros((height + 2, width + 2), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            dst[y + 1, x + 1] = src[y, x]
    for y in range(height):
        dst[y, 0] = src[y, 0]
        dst[y, width + 1] = src[y, width - 1]
    for x in range(width):
        dst[0, x] = src[0, x]
        dst[height + 1, x] = src[height - 1, x]
    for y in range(height):
        for x in range(width):
            dst_x = (dst[y, x + 2] - dst[y, x]) + 2(dst[y + 1, x + 2] - dst[y + 1, x]) + (dst[y + 2, x + 2] - dst[y + 2, x])
            dst_y = (dst[y + 2, x] - dst[y, x]) + 2(dst[y + 2, x + 1] - dst[y, x + 1]) + (dst[y + 2, x + 2] - dst[y, x + 2])
            dst[y + 1, x + 1] = sqrt(dst_x * dst_x + dst_y * dst_y)
            if dst[y + 1, x + 1] > 255:
                dst[y + 1, x + 1] = 255
    cv2.imshow('Source', src)
    cv2.imshow('Dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()