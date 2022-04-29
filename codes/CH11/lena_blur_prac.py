import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/lena.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Source', src)

    height, width = src.shape
    dst = np.zeros((int(height / 2), int(width / 2)), np.uint8)

    for y in range(int(height / 2)):
        for x in range(int(width / 2)):
            dst[y, x] = src[y * 2 - 1, x * 2 - 1]

    dst = cv2.blur(dst, (3, 3))
    cv2.imshow('Dst 1', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()