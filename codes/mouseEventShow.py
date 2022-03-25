import cv2
import numpy as np

def OnMouseAction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'Click left button at x={x}, y={y}')
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print(f'Click right button at x={x}, y={y}')
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        print(f'Click middle button at x={x}, y={y}')
    elif flags == cv2.EVENT_FLAG_LBUTTON:
        print(f'Hold left button and shift at x={x}, y={y}')
    elif flags == cv2.EVENT_FLAG_RBUTTON:
        print(f'Hold right button and shift at x={x}, y={y}')

if __name__ == '__main__':
    img = np.ones((200, 300, 3), np.uint8) * 255
    cv2.namedWindow('OpenCV Mouse Event')
    cv2.setMouseCallback('OpenCV Mouse Event', OnMouseAction)
    cv2.imshow('OpenCV Mouse Event', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
