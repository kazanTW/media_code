import cv2
import numpy as np

def onMouseAction(event, x, y, flags, param):
    blue = (255, 0, 0)
    r = 40
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), r, blue, -1)

if __name__ == '__main__':
    img = np.zeros((350, 500, 3), np.uint8)
    cv2.namedWindow('Blues')
    cv2.setMouseCallback('Blues', onMouseAction)
    
    while True:
        cv2.imshow('Blues', img)
        key = cv2.waitKey(100)
        if key == 27:
            break
    cv2.destroyAllWindows()