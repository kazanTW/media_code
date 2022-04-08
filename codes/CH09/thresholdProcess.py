import cv2
import numpy as np

if __name__ == '__main__':
    thresh = 127
    maxValue = 255
    src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
    ret, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

    print(f'src =\n {src}\nthreshold = {ret}\ndst =\n {dst}')