import cv2
import numpy as np

if __name__ == '__main__':
    thresh = 127
    maxValue = 255
    src = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Src', src)
    ret, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
    cv2.imshow('Dst - 127', dst)

    thresh = 0
    ret, dst = cv2.threshold(src, thresh=thresh, maxval=maxValue, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Dst - Otsu', dst)
    print(f'threshold = {ret}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()