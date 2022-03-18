import cv2
import numpy as np

if __name__ == '__main__':
    img = np.zeros((400, 600, 3), np.uint8)
    for i in range(0, 50):
        cx = np.random.randint(0, 600)
        cy = np.random.randint(0, 400)
        color = np.random.randint(0, 256, size=3).tolist()
        r = np.random.randint(5, 100)

        cv2.circle(img, (cx, cy), r, color, -1)

    cv2.imshow("RandCircle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()