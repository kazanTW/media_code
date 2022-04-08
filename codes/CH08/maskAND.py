import cv2
import numpy as np

if __name__ == '__main__':
    src1 = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    src2 = np.zeros(src1.shape, dtype=np.uint8)

    src2[30:260, 70:260] = 255
    dst = cv2.bitwise_and(src1, src2)
    cv2.imshow('Pic', src1)
    cv2.imshow('Mask', src2)
    cv2.imshow('Result', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()