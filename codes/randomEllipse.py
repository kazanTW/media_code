import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("../media/img/antarctic.jpg")
    cy = int(img.shape[0] / 2)
    cx = int(img.shape[1] / 2)
    size = (200, 100)

    for i in range(0, 15):
        angle = np.random.randint(0, 361)
        color = np.random.randint(0, 256, size=3).tolist()
        cv2.ellipse(img, (cx, cy), size, angle, 0, 360, color, 1)

    cv2.imshow("RandEllipse", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()