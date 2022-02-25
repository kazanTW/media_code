import cv2
from cv2 import *

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")
    img_ptX = 118
    img_ptY = 169

    img_blue = img[img_ptY, img_ptX, 0]
    img_green = img[img_ptY, img_ptX, 1]
    img_red = img[img_ptY, img_ptX, 2]

    print(f'BGR = {img_blue}, {img_green}, {img_red}')
