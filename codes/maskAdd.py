import cv2
import numpy as np

if __name__ == '__main__':
    img1 = np.zeros((200, 300, 3), np.uint8)
    img1[:, :, 1] = 255
    cv2.imshow('Img1', img1)
    img2 = np.zeros((200, 300, 3), np.uint8)
    img2[:, :, 2] = 255
    cv2.imshow('Img2', img2)    
    mask = np.zeros((200, 300, 1), np.uint8)
    mask[50:150, 100:200, :] = 255
    cv2.imshow('Mask', mask)

    img3 = cv2.add(img1, img2)              # Without Mask
    cv2.imshow('Img1 + 2', img3)
    img4 = cv2.add(img1, img2, mask=mask)   # With Mask
    cv2.imshow('Add Mask', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()