import cv2
import numpy as np

if __name__ == '__main__':
    src1 = cv2.imread('../media/img/lake.jpg')
    cv2.imshow('Lake', src1)
    src2 = cv2.imread('../media/img/geneva.jpg')
    cv2.imshow('Genava', src2)

    dst = cv2.addWeighted(src1, 1, src2, 0.2, 1)
    cv2.imshow('Sum', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()