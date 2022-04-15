from cv2 import FONT_HERSHEY_PLAIN, FONT_HERSHEY_SIMPLEX
import cv2
import numpy as np
import time


if __name__ == '__main__':
    cv2.namedWindow('snakeline')
    score = 0
    flag = 1

    bg = np.zeros((400, 650, 3), np.uint8)
    cv2.putText(bg, 'GAME OVER', (60, 225), FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 12)
    cv2.putText(bg, f'Score: {score}', (250, 275), FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
    cv2.imshow('snakeline', bg)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()       