import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/rural.jpg')
    cv2.imshow('Source', src)

    height, width = src.shape[0:2]
    srcp = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
    dstp = np.float32([[30, 0], [width - 1, 0], [0, height - 1]])
    M = cv2.getAffineTransform(srcp, dstp)
    dsize = (width, height)
    dst = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Dst', dst)

    dstp = np.float32([[0, 0], [width - 1 - 30, 0], [30, height - 1]])
    M = cv2.getAffineTransform(srcp, dstp)
    dst1 = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Dst 1', dst1)

    a = [0, height * 0.2]
    b = [width * 0.8, height * 0.2]
    c = [width * 0.1, height * 0.9]
    dstp = np.float32([a, b, c])
    M = cv2.getAffineTransform(srcp, dstp)
    dst2 = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Dst2 - resize', dst2)

    a = [0, height * 0.4]
    dstp = np.float32([a, b, c])
    M = cv2.getAffineTransform(srcp, dstp)
    dst3 = cv2.warpAffine(src, M, dsize)
    cv2.imshow('Dst3 - tilt resize', dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()