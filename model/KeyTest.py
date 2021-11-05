import imutils
import numpy as np
from InfomationTest import cut_image
import cv2

img_sour =cv2.imread("../imageTest/edit.png")

list_img = cut_image(img_sour)

img_class=list_img["img_class"]

def cut_id(img,isKey):
    i=0
    if isKey==True:
        i=3
    else:i=5

    for j in range(i):
        x1, y1, w1, h1 = 40+38*j, 50, 40, 238
        img = cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

        new_img = img[(y1+2):(y1 + h1-3), (x1+5):(x1 + w1-5)]
        cv2.imwrite("../outImg/result/{}.png".format(j),new_img)
        result_key(new_img)
        # cv2.imshow("hihi",new_img)
        # cv2.waitKey()
    cv2.imshow("hihi", img)
    cv2.waitKey()

def result_key(img):

    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # chuyển ảnh xám thành ảnh grayscale
    thresh = cv2.Canny(imgray, 127, 255) # nhị phân hóa ảnh
    cnts, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] ;
    # cnts = imutils.grab_contours(cnts)
    questionCnts = []
    for cnt in cnts:
        (x, y, w, h) = cv2.boundingRect(cnt)
        ar = w / float(h)
        # print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
        if w>=5 and h>=5:
            print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
            # cv2.drawContours(img, cnts, -1, (0, 255, 0), 1)  # vẽ lại ảnh contour vào ảnh gốc
            # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.drawContours(img, cnts, -1, (0, 255, 0), 2) # vẽ lại ảnh contour vào ảnh gốc
    # show ảnh lên
    cv2.imshow("ballons", img)
    cv2.waitKey(0)




cut_id(img_class,False)




