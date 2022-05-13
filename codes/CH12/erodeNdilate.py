import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/linuxlogo.jpg')
    cv2.imshow('Source', src)

    kernel = np.ones((5, 5), np.uint8)
    dst_erosion = cv2.erode(src, kernel)
    cv2.imshow('Erosion', dst_erosion)

    dst_dilation = cv2.dilate(src, kernel)
    cv2.imshow('Dilation', dst_dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()