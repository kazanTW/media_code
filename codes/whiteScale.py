import cv2
import numpy as np

if __name__ == '__main__':
    height = 160
    width = 280

    image = np.zeros((height, width), np.uint8)
    image.fill(255)
    # img = np.ones((height, width), np.uint8) * 255
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()