from cv2 import WINDOW_AUTOSIZE, WINDOW_NORMAL
import cv2

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")
    cv2.namedWindow("Colored Image", WINDOW_AUTOSIZE)
    cv2.imshow("Colored Image", img)
    
    img2 = cv2.imread("../media/img/jk.jpg", 0)
    cv2.namedWindow("Gray Image", WINDOW_NORMAL)
    cv2.imshow("Gray Image", img2)

    ret_value = cv2.waitKey(0)

    if ret_value == ord('q'):
        cv2.destroyWindow("Colored Image")
    elif ret_value == ord('x'):
        cv2.destroyWindow("Gray Image")
    else:
        pass