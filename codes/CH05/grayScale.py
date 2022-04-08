import cv2
import numpy as np

if __name__ == '__main__':
    height = 160
    width = 280

    image = np.zeros((height, width), np.uint8)
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()