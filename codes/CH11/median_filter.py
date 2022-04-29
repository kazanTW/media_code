import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/jk.jpg')
    dst1 = cv2.medianBlur(src, 3)
    dst2 = cv2.medianBlur(src, 5)
    dst3 = cv2.medianBlur(src, 7)
    cv2.imshow('Source', src)
    cv2.imshow('Dst 1', dst1)
    cv2.imshow('Dst 2', dst2)
    cv2.imshow('Dst 3', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()