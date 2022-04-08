import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/lena.jpg')

    watermark = np.zeros((150, 100, 3), np.uint8)
    watermark[0:50, :] = 255
    watermark[50:100, :] = 128
    watermark[100:150, :] = 0

    img[0:150, 0:100] = watermark

    cv2.imshow("Watermark", img)
    retValue = cv2.waitKey(0)
    cv2.destroyAllWindows()
