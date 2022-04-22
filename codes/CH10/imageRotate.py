import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/rural.jpg')
    cv2.imshow('Source', src)

    height, width = src.shape[0:2]
    M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)
    dsize = (width, height)
    dst1 = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Counterclockwise Rotate', dst1)

    M = cv2.getRotationMatrix2D((width / 2, height / 2), -30, 1)
    dst2 = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Clockwise Rotate', dst2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()