import cv2
import numpy as np

if __name__ == '__main__':
    src = np.zeros((400, 400), dtype=np.uint8)
    cv2.circle(src, (200, 200), 140, 255, -1)
    cv2.imshow('Source', src)

    dst_none = cv2.Sobel(src, -1, 1, 0)
    cv2.imshow('Dst None', dst_none)

    dst_x = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dst_x = cv2.convertScaleAbs(dst_x)
    cv2.imshow('Dst - Abs X', dst_x)
    dst_y = cv2.Sobel(src, cv2.CV_32F, 0, 1)
    dst_y = cv2.convertScaleAbs(dst_y)
    cv2.imshow('Dst - Abs Y', dst_y)

    dst = cv2.addWeighted(dst_x, 0.5, dst_y, 0.5, 0)
    cv2.imshow('Dst - Abs Full', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()