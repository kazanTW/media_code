import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/jk.jpg')
    dst1 = cv2.blur(src, (15, 15))
    dst2 = cv2.GaussianBlur(src, (15, 15), 0, 0)
    dst3 = cv2.bilateralFilter(src, 15, 100, 100)

    cv2.imshow('Source', src)
    cv2.imshow('Blur', dst1)
    cv2.imshow('Gauss Blur', dst2)
    cv2.imshow('Bilateral', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()