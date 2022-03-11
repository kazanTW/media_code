import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/mountain.jpg')
    cv2.imshow("BGR", img)

    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    cv2.imshow("RGB Color Space", img_RGB)

    img_BGR = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("BGR Color Space", img_BGR)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
