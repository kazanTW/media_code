import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    res = cv2.add(img, img)
    res2 = img + img
    cv2.imshow('Pic1', img)
    cv2.imshow('Pic2', res)
    cv2.imshow('Pic3', res2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()