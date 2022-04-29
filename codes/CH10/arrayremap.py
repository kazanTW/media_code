import cv2
import numpy as np

if __name__ == '__main__':
    src = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
    rows, columns = src.shape
    mapx = np.ones(src.shape, np.float32) * 3
    mapy = np.ones(src.shape, np.float32) * 2
    dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)

    print(f'src =\n {src}\mapx =\n {mapx}\nmapy =\n {mapy}\ndst =\n {dst}')