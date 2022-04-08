from matplotlib.pyplot import draw
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def cv2_ZH_Text(img, text, left, top, color, fontSize):
    if(isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype("/usr/local/share/fonts/TW-Sung-98_1.ttf", fontSize, encoding="utf-8")
    draw.text((left, top), text, color, font=fontText)

    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

if __name__ == '__main__':
    img = cv2.imread("../media/img/antarctic.jpg")
    img = cv2_ZH_Text(img, "逢甲大學多媒體系統", 100, 100, (0, 0, 255), 50)

    cv2.imshow("ZH Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()