from cv2 import blur
import cv2

if __name__ == '__main__':
    img = cv2.imread('../media/img/street.jpg')
    blue, green, red = cv2.split(img)

    bgr_img = cv2.merge([blue, green, red])
    cv2.imshow('B -> G -> R', bgr_img)

    rgb_img = cv2.merge([red, green, blue])
    cv2.imshow('R -> G -> B', rgb_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
