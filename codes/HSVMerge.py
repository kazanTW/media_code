import cv2

if __name__ == '__main__':
    img = cv2.imread('../media/img/street.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue, saturation, value = cv2.split(hsv_img)
    hsv_img = cv2.merge([hue, saturation, value])

    cv2.imshow('Image', img)
    cv2.imshow('HSV Merge', hsv_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()