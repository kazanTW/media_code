import cv2
from cv2 import blur

if __name__ == '__main__':
    src = cv2.imread('../../media/img/jk.jpg')
    dst1 = cv2.blur(src, (3, 3))
    dst2 = cv2.blur(src, (5, 5))
    dst3 = cv2.blur(src, (7, 7))
    dst_29 = cv2.blur(src, (29, 29))

    cv2.imshow('Source', src)
    cv2.imshow('Dst 1', dst1)
    cv2.imshow('Dst 2', dst2)
    cv2.imshow('Dst 3', dst3)
    cv2.imshow('Dst 29 * 29', dst_29)

    cv2.waitKey(0)
    cv2.destroyAllWindows()