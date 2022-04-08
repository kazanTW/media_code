import cv2

if __name__ == '__main__':
    src = cv2.imread('../media/img/minnesota.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Origin', src)

    ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('Binary', dst)

    ret, dst_zero = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO)
    ret, dst_zero_inv = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('To Zero', dst_zero)
    cv2.imshow('Zero Inv', dst_zero_inv)

    dst_mean = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    dst_gauss = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
    cv2.imshow('Adaptive Mean', dst_mean)
    cv2.imshow('Adaptive Gaussian', dst_gauss)

    cv2.waitKey(0)
    cv2.destroyAllWindows()