import cv2
from cv2 import *

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")
    cv2.imshow("Original", img)
    img_ptX = 342
    img_ptY = 345

    for i in range(img_ptY - 50, img_ptY):
        for j in range(img_ptX):
            img[i, j] = (0, 255, 255)

    cv2.imshow("Modified", img)
    ret_value = cv2.waitKey(0)