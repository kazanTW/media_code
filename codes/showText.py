import cv2
import numpy as np

if __name__ == '__main__':
    # img = np.ones((300, 600, 3), np.uint8) * 255
    # font = cv2.FONT_HERSHEY_SIMPLEX

    # cv2.putText(img, 'Python', (120, 120), font, 3, (255, 0, 0), 12)
    # cv2.putText(img, 'Python', (120, 120), font, 3, (0, 255, 255), 5)
    # cv2.putText(img, 'Python', (120, 180), font, 3, (0, 255, 0), 12, cv2.LINE_8, True)

    # cv2.imshow("Text", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img = cv2.imread("../media/img/antarctic.jpg")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'Antarctic', (120, 120), font, 3, (255, 0, 0), 12)

    cv2.imshow("Antarctic", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()