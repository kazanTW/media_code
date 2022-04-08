import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('../media/img/mountain.jpg')
    
    output = np.hstack((img, img))
    cv2.imshow("Sticked", output)
    retValue = cv2.waitKey(0)
    cv2.destroyAllWindows()