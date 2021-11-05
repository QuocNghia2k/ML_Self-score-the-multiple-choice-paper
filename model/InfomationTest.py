import numpy as np
import cv2
import imutils



def cut_infomation(cnt,img):
    x, y, w, h = cv2.boundingRect(cnt)
    # print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
    # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    new_img = img[y:y + h, x:x + w]
    return new_img

def cut_image(img_format):

    # convert image from BGR to GRAY to apply canny edge detection algorithm
    gray_img = cv2.cvtColor(img_format, cv2.COLOR_BGR2GRAY)

    # remove noise by blur image
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # apply canny edge detection algorithm
    img_canny = cv2.Canny(blurred, 100, 200)

    # find contours
    cnts = cv2.findContours(img_canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Tìm ra diện tích của toàn bộ các contours
    area_cnt = [cv2.contourArea(cnt) for cnt in cnts]
    area_sort = np.argsort(area_cnt)[::-1]
    # Top 10 contour có diện tích lớn nhất
    area_sort[:10]

    img_class= img_keyTest= img_mssv= img_res=cut_infomation(cnts[area_sort[0]],img_format)

    for i in range(len(area_sort)):
        x, y, w, h = cv2.boundingRect(cnts[area_sort[i]])
        # print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
        # cv2.imshow("hihi",cut_infomation(cnts[area_sort[i]],img_format))
        # cv2.waitKey()
        if y>=140 and y<=150 and h>=220 and h<=230:
            if x>=63 and x<=70 and w>=155 and w<=160:
                img_class= cut_infomation(cnts[area_sort[i]],img_format)
            elif x>=243 and x<=249 and w>=105 and w<=110:
                img_keyTest=cut_infomation(cnts[area_sort[i]],img_format)
            elif x>=370 and x<=377 and w>=205 and w<=215:
                img_mssv =cut_infomation(cnts[area_sort[i]],img_format)
            else :
                print("hiihi")

    list_coutour={"img_class": imutils.resize(img_class,width=150, height=240),
                 "img_keyTest": imutils.resize(img_keyTest,width=100, height=240),
                 "img_mssv":imutils.resize(img_mssv,width=200, height=240),
                  "img_res":imutils.resize(img_mssv,width=500, height=700)}
    return list_coutour



