import cv2
from cv2 import *

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg",cv2.IMREAD_GRAYSCALE)
    img_px = img[169, 118]
    print((type(img_px)))
    print(f'BGR = {img_px}')
