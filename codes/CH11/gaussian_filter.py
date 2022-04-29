import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/jk.jpg')
    dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)
    dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)
    dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)

    cv2.imshow('Source', src)
    cv2.imshow('Dst 1', dst1)
    cv2.imshow('Dst 2', dst2)
    cv2.imshow('Dst 3', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()