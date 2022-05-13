import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/lena.jpg')
    kernel = np.ones((3, 3), np.uint8)
    dst_morpholGrad = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
    
    dst_sobel_x = cv2.convertScaleAbs(cv2.Sobel(src, cv2.CV_32F, 1, 0))
    dst_sobel_y = cv2.convertScaleAbs(cv2.Sobel(src, cv2.CV_32F, 0, 1))
    dst_sobel = cv2.addWeighted(dst_sobel_x, 0.5, dst_sobel_y, 0.5, 0)

    dst_scharr_x = cv2.convertScaleAbs(cv2.Scharr(src, cv2.CV_32F, 1, 0))
    dst_scharr_y = cv2.convertScaleAbs(cv2.Scharr(src, cv2.CV_32F, 0, 1))
    dst_scharr = cv2.addWeighted(dst_scharr_x, 0.5, dst_scharr_y, 0.5, 0)

    dst_laplacian = cv2.convertScaleAbs(cv2.Laplacian(src, cv2.CV_32F, ksize=5))

    cv2.imshow('Source', src)
    cv2.imshow('Morphological Gradient', dst_morpholGrad)
    cv2.imshow('Sobel', dst_sobel)
    cv2.imshow('Scharr', dst_scharr)
    cv2.imshow('Laplacian', dst_laplacian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()