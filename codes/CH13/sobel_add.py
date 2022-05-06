import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/map.jpg')

    dst_x = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dst_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
    dst_x = cv2.convertScaleAbs(dst_x)
    dst_y = cv2.convertScaleAbs(dst_y)

    dst = cv2.addWeighted(dst_x, 0.5, dst_y, 0.5, 0)

    cv2.imshow('Source', src)
    cv2.imshow('Dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()