import cv2
import numpy as np

def onChange(x):
    pass

def onMouseAction(event, x, y, flags, param):
    color = np.random.randint(0, high=256, size=3).tolist()
    r = np.random.randint(10, 50)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), r, color, thickness)

if __name__ == '__main__':
    thickness = -1
    height = 400
    width = 600
    img = np.ones((height, width, 3), np.uint8) * 255

    cv2.namedWindow('Circles')
    cv2.setMouseCallback('Circles', onMouseAction)
    cv2.createTrackbar('Thickness', 'Circles', 0, 1, onChange)

    while True:
        cv2.imshow('Circles', img)
        key = cv2.waitKey(100)
        num = cv2.getTrackbarPos('Thickness', 'Circles')
        if num == 0:
            thickness = -1
        else:
            thickness = 3
        
        if key == ord('q') or key == ord('Q'):
            break
    cv2.destroyAllWindows()