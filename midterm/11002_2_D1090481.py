import cv2
import numpy as np
import time

def circle_draw(img, center, radius, color):
    cv2.circle(img, center, radius, color, 3)

if __name__ == '__main__':
    bg = np.zeros((720, 1280, 3), np.uint8)

    while cv2.waitKey(0) != 13:
        while cv2.waitKey(1) != 32:
            cx = np.random.randint(0, 1280)
            cy = np.random.randint(0, 720)
            r = np.random.randint(5, 100)
            color = np.random.randint(0, 256, size=3).tolist()

            circle_draw(bg, (cx, cy), r, color)
            cv2.imshow('LCD Protection D1090481', bg)
            time.sleep(0.1)

    cv2.destroyAllWindows()