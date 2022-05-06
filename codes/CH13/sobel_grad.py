import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/map.jpg')
    # dst = cv2.Sobel(src, -1, 1, 0)
    dst = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dst = cv2.convertScaleAbs(dst)

    # dst1 = cv2.Sobel(src, -1, 0, 1)
    dst1 = cv2.Sobel(src, cv2.CV_32F, 0, 1)
    dst1 = cv2.convertScaleAbs(dst1)

    cv2.imshow('Source', src)
    cv2.imshow('Dst', dst)
    cv2.imshow('Dst 1', dst1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()