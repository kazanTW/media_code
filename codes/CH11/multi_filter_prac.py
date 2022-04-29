import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/unistar.jpg')

    dst1_blur = cv2.blur(src, (5, 5))
    dst1_gauss = cv2.GaussianBlur(src, (5, 5), 0, 0)
    dst1_bilateral_50 = cv2.bilateralFilter(src, 5, 50, 50)
    dst1_bilateral_120 = cv2.bilateralFilter(src, 5, 120, 120)

    dst2_blur = cv2.blur(src, (7, 7))
    dst2_gauss = cv2.GaussianBlur(src, (7, 7), 0, 0)
    dst2_bilateral_50 = cv2.bilateralFilter(src, 7, 50, 50)
    dst2_bilateral_120 = cv2.bilateralFilter(src, 7, 120, 120)

    cv2.imshow('Source', src)
    cv2.imshow('Dst Blur 5*5', dst1_blur)
    cv2.imshow('Dst Gauss 5*5', dst1_gauss)
    cv2.imshow('Dst Bilateral 5*5 50*50', dst1_bilateral_50)
    cv2.imshow('Dst Bilateral 5*5 120*120', dst1_bilateral_120)
    cv2.imshow('Dst Blur 7*7', dst2_blur)
    cv2.imshow('Dst Gauss 7*7', dst2_gauss)
    cv2.imshow('Dst Bilateral 7*7 50*50', dst2_bilateral_50)
    cv2.imshow('Dst Bilateral 7*7 120*120', dst2_bilateral_120)

    cv2.waitKey(0)
    cv2.destroyAllWindows()