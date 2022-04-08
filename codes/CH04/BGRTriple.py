import cv2
import numpy as np

if __name__ == '__main__':
    height = 150
    width = 300

    img = np.zeros((height, width, 3), np.uint8)
    img[0:50, :, 0] = 255
    img[50:100, :, 1] = 255
    img[100:150, :, 2] = 255
    
    cv2.imshow("BGR", img)
    retValue = cv2.waitKey(0)
    cv2.destroyAllWindows()