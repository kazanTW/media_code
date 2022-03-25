import cv2
import numpy as np

if __name__ == '__main__':
    value = 20
    img = cv2.imread('../media/img/jk.jpg')
    coff = np.ones(img.shape, dtype=np.uint8) * value

    res = cv2.add(img, coff)
    cv2.imshow('Pic1', img)
    cv2.imshow('Pic2', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()