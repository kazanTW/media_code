import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/easy.jpg')
    cv2.imshow('Source', src)

    src_grayScale = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, dst_bin = cv2.threshold(src_grayScale, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(dst_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 5)
    cv2.imshow('Contours', dst)
    cv2.imshow('Source NOW', src)

    n = len(contours)
    imgLst = []

    for i in range(n):
        img = np.zeros(src.shape, np.uint8)
        imgLst.append(img)
        imgLst[i] = cv2.drawContours(imgLst[i], contours, i, (255, 255, 255), 5)
        cv2.imshow('Counters' + str(i), imgLst[i])


    cv2.waitKey(0)
    cv2.destroyAllWindows()