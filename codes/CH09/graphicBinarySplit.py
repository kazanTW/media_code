import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/jk.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Src', img)
    row, column = img.shape
    x = np.zeros((row, column, 8), dtype=np.uint8)
    for i in range(8):
        x[:, :, i] = 2 ** i
    result = np.zeros((row, column, 8), dtype=np.uint8)
    for i in range(8):
        result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
        mask = result[:, :, i] > 0
        result[mask] = 255
        cv2.imshow(str(i), result[:, :, i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()