import cv2
import numpy as np

if __name__ == '__main__':
    target = cv2.imread('../media/img/dollar.jpg', cv2.IMREAD_GRAYSCALE)
    face = cv2.imread('../media/img/lena.jpg', cv2.IMREAD_GRAYSCALE)

    roi_area = face[140:240, 135:225]
    target[105:205, 280:370] = roi_area

    cv2.imshow("Trans", target)
    retValue = cv2.waitKey(0)
    cv2.destroyAllWindows()