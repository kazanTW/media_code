import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../media/img/jk.jpg')
    dst = cv2.bitwise_not(src)
    cv2.imshow('Pics', src)
    cv2.imshow('Result', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()