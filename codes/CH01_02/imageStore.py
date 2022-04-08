from matplotlib.pyplot import close
import cv2
from cv2 import *

def fileSaving(filename):
    if open(filename):
        print("Save file success.")
    else:
        print("Save file failed.")
    close(filename)

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")
    filename1 = "../media/img/out1_7_1.tiff"
    filename2 = "../media/img/out1_7_2.png"

    ret_tiff = cv2.imwrite(filename1, img)
    fileSaving(filename1)
    ret_png = cv2.imwrite(filename2, img)
    fileSaving(filename2)