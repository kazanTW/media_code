import cv2
import numpy as np

if __name__ == '__main__':
    thresh = 127
    maxValue = 255
    src = cv2.imread('../media/img/jk.jpg')
    ret, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    cv2.imshow('Src', src)
    cv2.imshow('Dst - 127', dst)

    thresh = 80
    ret, dst = cv2.threshold(src, thresh=thresh, maxval=maxValue, type=cv2.THRESH_BINARY)
    cv2.imshow('Dst - 80', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()