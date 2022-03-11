import numpy as np
import cv2

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")
    cv2.imshow("Original", img)

    mosaic = np.random.randint(256, size=(190, 170, 3), dtype=np.uint8)          
    img[25:215, 75:245] = mosaic
    cv2.imshow("Mosaicked", img)
    ret_value = cv2.waitKey(0)
    cv2.destroyAllWindows()