import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../media/img/forest.jpg')
    key = np.random.randint(0, 256, src.shape, np.uint8)

    print(src.shape)

    cv2.imshow('Plain Image', src)
    cv2.imshow('Key', key)

    encryptImage = cv2.bitwise_xor(src, key)
    decryptImage = cv2.bitwise_xor(key, encryptImage)
    cv2.imshow('Encry', encryptImage)
    cv2.imshow('Decry', decryptImage)

    cv2.waitKey(0)
    cv2.destroyAllWindows()