import cv2
import numpy as np

if __name__ == '__main__':
    b = np.zeros((200, 250, 3), np.uint8)
    g = np.zeros((200, 250, 3), np.uint8)
    r = np.zeros((200, 250, 3), np.uint8)

    b[:, :, 0] = 255
    g[:, :, 1] = 255
    r[:, :, 2] = 255
    cv2.imshow("B channel", b)
    cv2.imshow("G channel", g)
    cv2.imshow("R channel", r)

    img1 = cv2.add(b, g)
    cv2.imshow('B + G', img1)
    img2 = cv2.add(g, r)
    cv2.imshow('G + R', img2)
    img3 = cv2.add(img1, r)
    cv2.imshow('B + G + R', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()