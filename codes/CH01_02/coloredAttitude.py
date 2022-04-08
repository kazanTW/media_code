import cv2

if __name__ == '__main__':
    img = cv2.imread("../media/img/jk.jpg")

    print(f'Attitudes: ')
    print(f'Shape = {img.shape}')
    print(f'Size = {img.size}')
    print(f'Dtype = {img.dtype}')
    cv2.imshow('Result', img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
