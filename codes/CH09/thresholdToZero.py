import cv2
import numpy as np

if __name__ == '__main__':
    src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)
    ret, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO)
    print(f'src =\n {src}\nthreshold = {ret}\ndst =\n {dst}')