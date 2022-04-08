from cv2 import IMREAD_GRAYSCALE, WINDOW_NORMAL
import numpy as np
import cv2

if __name__ == '__main__':
    # img = np.zeros((160, 280), dtype=np.uint8)
    # for y in range(0, 160, 20):
    #     img[y: y + 10, :] = 255
    # cv2.namedWindow('Image', WINDOW_NORMAL)
    # cv2.imshow('Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img = np.random.randint(256, size=(160, 280, 3), dtype=np.uint8)
    cv2.namedWindow('Image', WINDOW_NORMAL)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()