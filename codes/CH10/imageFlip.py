import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/python.jpg')
    cv2.imshow('Source', src)

    dst1 = cv2.flip(src, 0)
    cv2.imshow('dst1 - Vertical', dst1)
    dst2 = cv2.flip(src, 1)
    cv2.imshow('dst2 - Horizontal', dst2)
    dst3 = cv2.flip(src, -1)
    cv2.imshow('dst3 - Both', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()