import cv2

if __name__ == '__main__':
    src = cv2.imread('../../media/img/southpole.jpg')
    cv2.imshow('Source', src)

    dst = cv2.resize(src, None, fx=0.5, fy=1.1)
    cv2.imshow('Resize DST', dst)

    print(f'src.shape = {src.shape}\ndst.shape = {dst.shape}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()