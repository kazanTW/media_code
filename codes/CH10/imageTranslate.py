import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/rural.jpg')
    cv2.imshow('Source', src)

    height, width = src.shape[0:2]
    dsize = (width, height)
    M = np.float32([[1, 0, 50],
                    [0, 1, 100]])
    dst = cv2.warpAffine(src, M, dsize)
    cv2.imshow('DST', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()