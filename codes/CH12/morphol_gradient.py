import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/lena.jpg')
    kernel = np.ones((3, 3), np.uint8)
    dst_erode = cv2.erode(src, kernel)
    dst_dilate = cv2.dilate(src, kernel)
    cv2.imshow('Source', src)
    cv2.imshow('Erosion', dst_erode)
    cv2.imshow('Dilation', dst_dilate)

    dst_morpholGrad = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('Morphological Gradient', dst_morpholGrad)

    cv2.waitKey(0)
    cv2.destroyAllWindows()