import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('../../media/img/tunnel.jpg')
    cv2.imshow('Source', src)

    height, width = src.shape[0:2]
    srcp = np.float32([[0, 0], [width, 0], [0, height], [width - 1, height - 1]])
    dstp = np.float32([[150, 0], [width - 150, 0], [0, height - 1], [width - 1, height - 1]])
    M = cv2.getPerspectiveTransform(srcp, dstp)
    dst = cv2.warpPerspective(src, M, (width, height))
    cv2.imshow('Dst', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()