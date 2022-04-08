import cv2
import numpy as np

if __name__ == '__main__':
    jk = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Src', jk)

    row, column = jk.shape
    h7 = np.ones((row, column), dtype=np.uint8) * 254
    cv2.imshow('254', h7)
    new_jk = cv2.bitwise_and(jk, h7)
    cv2.imshow('New', new_jk)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
