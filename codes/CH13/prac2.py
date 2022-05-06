import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/Baboon256.bmp')
    cv2.imshow('Source', src)
    
    dst_sobel_x = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dst_sobel_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
    dst_sobel_x = cv2.convertScaleAbs(dst_sobel_x)
    dst_sobel_y = cv2.convertScaleAbs(dst_sobel_y)
    dst_sobel = cv2.addWeighted(dst_sobel_x, 0.5, dst_sobel_y, 0.5, 0)
    cv2.imshow('Dst - Sobel', dst_sobel)

    dst_canny = cv2.Canny(src, 50, 80)
    cv2.imshow('Dst - Canny', dst_canny)

    dst_laplacian = cv2.convertScaleAbs(cv2.Laplacian(src, cv2.CV_32F, ksize=3))
    cv2.imshow('Dst - Laplacian', dst_laplacian)

    dst_scharr_x = cv2.convertScaleAbs(cv2.Scharr(src, cv2.CV_32F, 1, 0))
    dst_scharr_y = cv2.convertScaleAbs(cv2.Scharr(src, cv2.CV_32F, 0, 1))
    dst_scharr = cv2.addWeighted(dst_scharr_x, 0.5, dst_scharr_y, 0.5, 0)
    cv2.imshow('Dst - Scharr', dst_scharr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()