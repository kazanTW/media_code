import cv2
import numpy as np

if __name__ == '__main__':
    src = np.random.randint(0, 255, (3, 5), dtype=np.uint8)
    mask = np.zeros((3, 5), dtype=np.uint8)
    mask[0:2, 0:2] = 255
    dst = cv2.bitwise_or(src, mask)
    print(f'src = \n {src}\nmask = \n {mask}\ndst = \n {dst}')