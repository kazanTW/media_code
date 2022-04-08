import cv2
import numpy as np

if __name__ == '__main__':
    src = np.ones((3, 4), dtype=np.uint8) * 120
    src[0:2, 0:2] = 108
    # ret, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)
    ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print(f'src =\n {src}\nthreshold = {ret}\ndst =\n {dst}')