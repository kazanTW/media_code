import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/hung.jpg')
    dst = cv2.bilateralFilter(src, 5, 50, 50)
    cv2.imshow('Source', src)
    cv2.imshow('Dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()