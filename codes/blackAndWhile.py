import cv2
import numpy as np

if __name__ == '__main__':
    bg = np.zeros((160, 280), np.uint8)
    bg[40:120, 70:210] = 255

    cv2.imshow("Image", bg)
    retValue = cv2.waitKey(0)
    cv2.destroyAllWindows()
    