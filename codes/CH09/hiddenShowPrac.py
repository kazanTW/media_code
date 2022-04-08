import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../media/img/number1.jpg')
    maxValue = 255
    ret, dst = cv2.threshold(src, 1, maxValue, cv2.THRESH_BINARY)
    cv2.imshow('Src', src)
    cv2.imshow('Dst - 127', dst)

    ret, dst = cv2.threshold(src, 1, maxValue, cv2.THRESH_BINARY_INV)
    cv2.imshow('Dst - 80', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
