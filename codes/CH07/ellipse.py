import cv2

if __name__ == '__main__':
    img = cv2.imread("../media/img/antarctic.jpg")
    cy = int(img.shape[0] / 2)
    cx = int(img.shape[1] / 2)
    red = (0, 0, 255)
    yellow = (0, 255, 255)
    blue = (255, 0, 0)
    size = (200, 100)
    angle = 0

    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, red, 1)

    angle = 45
    cv2.ellipse(img, (cx, cy), size, angle, 0, 360, yellow, 5)
    cv2.ellipse(img, (cx, cy), size, angle, 45, 135, blue, 3)

    cv2.imshow("Ellipse", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()