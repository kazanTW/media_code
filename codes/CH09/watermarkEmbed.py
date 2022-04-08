import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Origin', img)

    row, column = img.shape
    h7 = np.ones((row, column), dtype=np.uint8) * 254
    temp = cv2.bitwise_and(img, h7)
    watermark = cv2.imread('../media/img/copyright.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Copy Right', watermark)
    ret, wm = cv2.threshold(watermark, 0, 1, cv2.THRESH_BINARY)

    new_img = cv2.bitwise_or(temp, wm)
    cv2.imshow('New', new_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()