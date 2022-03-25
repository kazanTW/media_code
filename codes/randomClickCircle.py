import cv2
import numpy as np

def onMouseAction(event, x, y, flags, param):
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), r, color, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), r, color, 3)

if __name__ == '__main__':
    height = 400
    width = 600
    image = np.ones((height, width, 3), np.uint8) * 255
    cv2.namedWindow('Circle')
    cv2.setMouseCallback('Circle', onMouseAction)

    while True:
        cv2.imshow('Circle', image)
        key = cv2.waitKey(100)
        if key == ord('Q') or key == ord('q'):
            break
    cv2.destroyAllWindows()