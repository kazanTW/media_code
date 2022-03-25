import cv2

if __name__ == '__main__':
    eventList = [i for i in dir(cv2) if "EVENT" in i]
    for e in eventList:
        print(e)