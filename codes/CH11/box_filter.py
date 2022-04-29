from locale import DAY_1
import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/jk.jpg')
    dst = cv2.boxFilter(src, -1, (2, 2), normalize=0)
    dst1 = cv2.boxFilter(src, -1, (3, 3), normalize=0)
    dst2 = cv2.boxFilter(src, -1, (5, 5), normalize=0)

    cv2.imshow('Source', src)
    cv2.imshow('Dst', dst)
    cv2.imshow('Dst 1', dst1)
    cv2.imshow('Dst 2', dst2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()