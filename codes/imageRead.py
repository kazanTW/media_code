import cv2

if __name__ == '__main__':
    # img = cv2.imread("jk.jpg")
    # cv2.imshow("Image", img)
    
    # img2 = cv2.imread("jk.jpg", 0)
    # cv2.imshow("Gray Image", img2)
    # ret_value = cv2.waitKey(0)

    # cv2.destroyAllWindows()

    img = cv2.imread("../media/img/jk.jpg")
    cv2.imshow("My Picture", img)
    ret_value = cv2.waitKey(0)
    # ret_value = cv2.waitKey(0)
    # if ret_value == ord('Q') or ret_value == ord('q'):
    #     cv2.destroyWindow("My Picture")
    if ret_value == 13:
        cv2.destroyWindow("My Picture")
    print(f"{ret_value} = ")