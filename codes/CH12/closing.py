import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/snowman.jpg')
    kernel = np.ones((11, 11), np.uint8)
    dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Source', src)
    cv2.imshow('Closing', dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()