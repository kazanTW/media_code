import cv2
import numpy as np
import time
from random import *

if __name__ == '__main__':
    width = 640
    height = 480
    r = 15
    speed = 0.1
    x = int(width / 2) - r
    y = 50
    random_step = [3, 4, 5, 6, 7]
    shuffle(random_step)
    x_step = random_step[0]
    y_step = 5

    while cv2.waitKey(1) == -1:
        if x > width - r or x < r:
            x_step = -x_step
        if y > height - r or y < r:
            y_step = -y_step
        x += x_step
        y += y_step

        img = np.ones((height, width, 3), np.uint8) * 255
        cv2.circle(img, (x, y), r, (255, 0, 0), -1)
        cv2.imshow("Bounce", img)
        time.sleep(speed)

    cv2.destroyAllWindows()