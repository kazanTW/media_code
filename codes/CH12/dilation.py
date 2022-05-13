import cv2
import numpy as np

if __name__ == '__main__':
    src = np.zeros((7, 7), np.uint8)
    src[2:5, 2:5] = 1
    kernel = np.ones((3, 3), np.uint8)
    dst = cv2.dilate(src, kernel)
    print(f'src = \n {src}\nkernel = \n {kernel}\ndst = \n {dst}')