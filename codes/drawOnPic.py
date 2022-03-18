import cv2

if __name__  == '__main__':
    img = cv2.imread("../media/img/antarctic.jpg")
    img[1:300, 1:300] = (0, 255, 255)

    cv2.line(img, (1, 1), (300, 1), (255, 0, 0))
    cv2.line(img, (300, 1), (300, 300), (255, 0, 0))
    cv2.line(img, (300, 300), (1, 300), (255, 0, 0))
    cv2.line(img, (1, 300), (1, 1), (255, 0, 0))

    for x in range(150, 300, 10):
        cv2.line(img, (x, 1), (300, x - 150), (255, 0, 0))
    for y in range(150, 300, 10):
        cv2.line(img, (1, y), (y - 150, 300), (255, 0, 0))

    cv2.imshow("Draw", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()