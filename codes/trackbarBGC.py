import cv2
import numpy as np

def onChange(x):
    b = cv2.getTrackbarPos('B', 'Canvas')
    g = cv2.getTrackbarPos('G', 'Canvas')
    r = cv2.getTrackbarPos('R', 'Canvas')
    canvas[:] = [b, g, r]

if __name__ == '__main__':
    canvas = np.ones((200, 640, 3), np.uint8) * 255
    cv2.namedWindow('Canvas')
    cv2.createTrackbar('B', 'Canvas', 0, 255, onChange)
    cv2.createTrackbar('G', 'Canvas', 0, 255, onChange)
    cv2.createTrackbar('R', 'Canvas', 0, 255, onChange)

    while True:
        cv2.imshow('Canvas', canvas)
        key = cv2.waitKey(100)
        if key == 27:
            break
    cv2.destroyAllWindows()