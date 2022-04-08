import cv2

if __name__ == '__main__':
    img = cv2.imread('../media/img/mountain.jpg')
    cv2.imshow("BGR Color Space", img)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV Color Space", img_HSV)

    cv2.waitKey(0)
    cv2.destroyAllWindows()