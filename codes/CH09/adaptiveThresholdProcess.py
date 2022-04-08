import cv2

if __name__ == '__main__':
    src = cv2.imread('../media/img/school.jpg', cv2.IMREAD_GRAYSCALE)
    ret, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

    # Adaptive Mean
    dst_mean = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)

    # Adaptive Gauss
    dst_gauss = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

    cv2.imshow('Src', src)
    cv2.imshow('Thresh Binary', dst)
    cv2.imshow('Adaptive Mean', dst_mean)
    cv2.imshow('Adaptive Gaussian', dst_gauss)

    cv2.waitKey(0)
    cv2.destroyAllWindows()