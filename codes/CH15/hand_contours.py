from cv2 import COLOR_BGR2GRAY
import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/myhand.jpg')
    cv2.imshow('Source', src)
    src_grarScale = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    ret, dst_bin = cv2.threshold(src_grarScale, 50, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(dst_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)
    cv2.imshow('Contours', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()