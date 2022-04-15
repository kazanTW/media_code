import cv2
import numpy as np

def onTrackbarChange(x):
    pass

def drawing(event, x, y, radius, color):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(background, (x, y), radius, color, -1)
        elif event == cv2.EVENT_RBUTTONDOWN:
            cv2.circle(background, (x, y), radius, color, 3)
        elif event == cv2.EVENT_LBUTTONDOWN:
            if key == 99:       # key 'c'
                cv2.rectangle(background, (x - radius, y - radius), (x + radius, y + radius), color, -1)
            elif key == 114:    # key 'r'
                cv2.rectangle(background, (x - radius, y - radius), (x + radius, y + radius), color, 3)
            elif key == 108:    # key 'l'
                cv2.line(background, (x, y - radius), (x, y + radius), color, 3)



def onMouse(event, x, y, flags, param):
    b = cv2.getTrackbarPos('Blue', 'Drawing')
    g = cv2.getTrackbarPos('Green', 'Drawing')
    r = cv2.getTrackbarPos('Red', 'Drawing')
    
    switch = cv2.getTrackbarPos('Colored', 'Drawing')
    radius = cv2.getTrackbarPos('radius', 'Drawing') + 4
    if switch == 0:
        drawing(event, x, y, radius, 0)
    else:
        drawing(event, x, y, radius, [b, g, r])


if __name__ == '__main__':
    background = np.ones((400, 500, 3), np.uint8) * 255
    cv2.namedWindow('Drawing')
    
    cv2.createTrackbar('Red', 'Drawing', 0, 255, onTrackbarChange)
    cv2.createTrackbar('Green', 'Drawing', 0, 255, onTrackbarChange)
    cv2.createTrackbar('Blue', 'Drawing', 0, 255, onTrackbarChange)
    cv2.createTrackbar('radius', 'Drawing', 0, 56, onTrackbarChange)
    cv2.createTrackbar('Colored', 'Drawing', 0, 1, onTrackbarChange)
    cv2.setMouseCallback('Drawing', onMouse)

    while True:
        cv2.imshow('Drawing', background)

        key = cv2.waitKey(100)
        if key == ord('q') or key == ord('Q'):
            break
    cv2.imwrite('myidea_D1090481.jpg', background)
    cv2.destroyAllWindows()