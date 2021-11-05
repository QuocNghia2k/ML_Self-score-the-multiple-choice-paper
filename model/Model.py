from InfomationTest import cut_image
from ImagePretreatment import edit_image
from AnswerCnn import anser_Test
from AnswerTest import get_keyTest,get_class,get_mssv
from AnswerResult import get_result
import cv2

path = "../imageTest/img.png"
img = cv2.imread(path)
imgAfterEdit =edit_image(img)
cv2.imshow("hihi", imgAfterEdit)
cv2.waitKey()
img_format= cv2.imread("../imageTest/edit.png")
imgAfterCut= cut_image(img_format)

cv2.imshow("mssv",imgAfterCut['img_mssv'])
cv2.imwrite("../imageTest/img_cut/mssv.png",imgAfterCut['img_mssv'])
cv2.imshow("class",imgAfterCut['img_class'])
cv2.imwrite("../imageTest/img_cut/class.png",imgAfterCut['img_class'])
cv2.imshow("key",imgAfterCut['img_keyTest'])
cv2.imwrite("../imageTest/img_cut/keyTest.png",imgAfterCut['img_keyTest'])
cv2.waitKey()

img_ms = cv2.imread("../imageTest/img_cut/mssv.png")
mssv =get_mssv(img_ms)
# print(mssv)
img_cl = cv2.imread("../imageTest/img_cut/class.png")
cl =get_class(img_cl)
# print(cl)
img_kt = cv2.imread("../imageTest/img_cut/keyTest.png")
key =get_keyTest(img_kt)
# print(key)

anser= anser_Test(imgAfterEdit)
print("Đáp án của bạn:{}".format(anser))

print(get_result(mssv,cl,key,anser))



