import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../media/img/geneva.jpg')
    mask = np.zeros(src.shape, dtype=np.uint8)
    mask[:, 155:280, :] = 255
    mask[100:200, :, :] = 255
    cv2.imshow('Original', src)
    cv2.imshow('Mask', mask)

    dst1 = cv2.bitwise_or(src, mask)
    dst2 = cv2.bitwise_and(src, mask)
    cv2.imshow('Result 1', dst1)
    cv2.imshow('Result 2', dst2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()