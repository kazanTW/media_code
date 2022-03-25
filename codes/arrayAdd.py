import cv2
import numpy as np

if __name__ == '__main__':
    src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
    src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
    res = src1 + src2
    # res = cv2.add(src1, src2)
    print(f'src1 = \n {src1}\nsrc2 = \n {src2}\ndst = \n {res}')