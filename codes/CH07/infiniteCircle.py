import cv2
import time
import numpy as np
from random import *

if __name__ == '__main__':
    img = cv2.imread("../media/img/antarctic.jpg")

    cy = int(img.shape[0] / 2)
    cx = int(img.shape[1] / 2)
    red = (0, 0, 255)
    yellow = (0, 255, 255)
    
    flag = False
    while True:
        img = cv2.imread("../media/img/antarctic.jpg")
        cv2.circle(img, (cx, cy), 30, red, -1)
        for r in range(40, 200, 20):
            cv2.circle(img, (cx, cy), r, yellow, 2)
            cv2.imshow("Circle", img)
            listener = cv2.waitKey(1)
            time.sleep(0.1)
            if listener != -1:
                cv2.destroyAllWindows()
                flag = True
                break
        if flag:
            cv2.destroyAllWindows()
            break