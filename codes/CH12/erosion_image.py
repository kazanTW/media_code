import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/bw.jpg')
    kernel_5 = np.ones((5, 5), np.uint8)
    dst_1 = cv2.erode(src, kernel_5)
    kernel_11 = np.ones((11, 11), np.uint8)
    dst_2 = cv2.erode(src, kernel_11)
    cv2.imshow('Source', src)
    cv2.imshow('Dst - Erode 5 * 5', dst_1)
    cv2.imshow('Dst - Erode 11 * 11', dst_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()