import cv2
from sympy import re

if __name__ == '__main__':
    img = cv2.imread('../media/img/colorbar.jpg')
    cv2.imshow('BGR', img)

    blue, green, red = cv2.split(img)
    cv2.imshow('Blue', blue)
    cv2.imshow('Green', green)
    cv2.imshow('Red', red)

    print(f'B channel shape = {blue.shape}')
    print(blue)

    cv2.waitKey(0)
    cv2.destroyAllWindows()