import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../media/img/jk.jpg')
    mask = np.zeros(src.shape, dtype=np.uint8)

    mask[30:260, 70:260] = 255
    dst = cv2.bitwise_and(src, mask)
    cv2.imshow('Pics', src)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()