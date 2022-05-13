import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/btree.jpg')
    kernel = np.ones((3, 3), np.uint8)
    dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Source', src)
    cv2.imshow('Opening', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()