import cv2
import numpy as np



def check_is_number(img):
    # cv2.imshow("hihih",img)
    # cv2.waitKey()


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    # Finding Contours
    # Use a copy of the image e.g. edged.copy()
    # since findContours alters the image
    contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # cnts = imutils.grab_contours(contours)

    # Tìm ra diện tích của toàn bộ các contours
    area_cnt = [cv2.contourArea(cnt) for cnt in contours]
    area_sort = np.argsort(area_cnt)[::-1]
    # Top 10 contour có diện tích lớn nhất
    area_sort[:10]
    # print("Number of Contours found = " + str(len(contours)))

    for i in range(len(area_sort)):
        x, y, w, h = cv2.boundingRect(contours[area_sort[i]])
        print('centroid: ({}, {}), (width, height): ({}, {})'.format(x, y, w, h))
        if 0<=x<=14 and 0<=y<=12 and 5<=w<=18 and 8<=h<=15:
            # cv2.imshow("hihi",img)
            # cv2.waitKey()
            return True
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)


    # cv2.imshow('Contours', img)
    # cv2.waitKey(0)
    # cv2.imshow("koko",img)
    # cv2.waitKey()
    return False

def get_mssv(img):
    mssv =""
    new_mssv = img[36:36+200,27:200]
    h ,w = new_mssv.shape[:2]
    print("{}:{}".format(h,w))
    # cv2.imshow("hihi",new_mssv)
    # cv2.waitKey()
    for i in range(7):
        for j in range(10):
            # print("{}:{}".format(i,j))
            cut_key = new_mssv[18*j:18*(j+1)-2,25*i:25*(i+1)-4]
            if check_is_number(cut_key):
                mssv = mssv+"{}".format(j)
                break
            # cv2.imshow("hihi",cut_key)
            # cv2.waitKey()

    return mssv

def get_keyTest(img):
    keyTest = ""
    new_keyTest = img[36:36 + 200, 27:100]
    h, w = new_keyTest.shape[:2]
    print("{}:{}".format(h, w))
    # cv2.imshow("hihi", new_keyTest)
    # cv2.waitKey()
    for i in range(3):
        # print("colum: {}".format(i))
        for j in range(10):
            # print("{}:{}".format(i, j))
            cut_key = new_keyTest[18 * j :18 * (j + 1) , 25 * i:25 * (i + 1) - 4]
            if check_is_number(cut_key):
                keyTest=keyTest + "{}".format(j)
                break
            # cv2.imshow("hihi", cut_key)
            # cv2.waitKey()

    return keyTest

def get_class(img):
    keyClass = ""
    new_keyClass = img[36:36 + 200, 27:150]
    h, w = new_keyClass.shape[:2]
    print("{}:{}".format(h, w))
    # cv2.imshow("hihi", new_keyClass)
    # cv2.waitKey()
    for i in range(5):
        # print("colum: {}".format(i))
        for j in range(10):
            # print("{}:{}".format(i, j))
            cut_key = new_keyClass[18 * j:18 * (j + 1) - 2, 25 * i:25 * (i + 1) - 4]
            if check_is_number(cut_key):
                keyClass = keyClass + "{}".format(j)
                break
            # cv2.imshow("hihi", cut_key)
            # cv2.waitKey()

    return keyClass
# img_ms = cv2.imread("../imageTest/img_cut/mssv.png")
# # check_is_number(img_ms)
# mssv =get_mssv(img_ms)
# print(mssv)
# img_cl = cv2.imread("../imageTest/img_cut/class.png")
# mssv =get_class(img_cl)
# print(mssv)
# img_kt = cv2.imread("../imageTest/img_cut/keyTest.png")
# mssv =get_keyTest(img_kt)
# print(mssv)