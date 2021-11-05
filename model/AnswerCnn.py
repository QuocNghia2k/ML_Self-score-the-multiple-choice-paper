import cv2
import numpy as np
import tflearn

import tensorflow as tf
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers import regression

def anser_Test(img):
    # img = cv2.imread("../imageTest/rt_2.png", 0)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite("../imageTest/tienXuLy/afterGaussianBlur.png", blur)
    # chống bị bóng lang tỏa
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imwrite("../imageTest/tienXuLy/afterThresh.png", thresh)


    horizal = thresh
    vertical = thresh


    scale_height = 20  # Scale này để càng cao thì số dòng dọc xác định sẽ càng nhiều
    scale_long = 15

    long = int(img.shape[1] / scale_long)
    height = int(img.shape[0] / scale_height)


    # xóa các điểm nhỏ gân nhiểu có hình
    horizalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (long, 1))
    horizal = cv2.erode(horizal, horizalStructure, (-1, -1))
    horizal = cv2.dilate(horizal, horizalStructure, (-1, -1))

    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, height))
    vertical = cv2.erode(vertical, verticalStructure, (-1, -1))
    vertical = cv2.dilate(vertical, verticalStructure, (-1, -1))
    #

    mask = vertical + horizal
    cv2.imwrite("../imageTest/tienXuLy/mask.png", mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #tìm table lớn nhất
    max = -1
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if cv2.contourArea(cnt) > max:
            x_max, y_max, w_max, h_max = x, y, w, h
            max = cv2.contourArea(cnt)
    #
    table = img[y_max:y_max + h_max, x_max:x_max + w_max]

    cropped_thresh_img = []
    cropped_origin_img = []
    countours_img = []
    #
    NUM_ROWS = 21
    START_ROW = 1
    for i in range(START_ROW, NUM_ROWS):
        thresh1 = thresh[y_max + round(i * h_max / NUM_ROWS):y_max + round((i + 1) * h_max / NUM_ROWS)-3,
                  x_max + round(w_max / 6)+32:x_max + round(w_max / 2)]

        contours_thresh1, hierarchy_thresh1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        origin1 = img[y_max + round(i * h_max / NUM_ROWS):y_max + round((i + 1) * h_max / NUM_ROWS)-3,
                  x_max + round(w_max / 6)+32:x_max + round(w_max / 2)]

        cropped_thresh_img.append(thresh1)
        cropped_origin_img.append(origin1)
        countours_img.append(contours_thresh1)


    for i in range(START_ROW, NUM_ROWS):
        thresh1 = thresh[y_max + round(i * h_max / NUM_ROWS)+1:y_max + round((i + 1) * h_max / NUM_ROWS)-1,
                  x_max + round(2 * w_max / 3)+32:x_max + round(w_max)]
        contours_thresh1, hierarchy_thresh1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        origin1 = img[y_max + round(i * h_max / NUM_ROWS)+1:y_max + round((i + 1) * h_max / NUM_ROWS)-1,
                  x_max + round(2 * w_max / 3)+32:x_max + round(w_max)]

        cropped_thresh_img.append(thresh1)
        cropped_origin_img.append(origin1)
        countours_img.append(contours_thresh1)

    # #tạo mô hình CNN
    BATCH_SIZE = 32
    IMG_SIZE = 28
    N_CLASSES = 4
    LR = 0.001
    N_EPOCHS = 50

    tf.compat.v1.reset_default_graph()


    network = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1]) #1

    network = conv_2d(network, 32, 3, activation='relu') #2
    network = max_pool_2d(network, 2) #3

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 32, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = conv_2d(network, 64, 3, activation='relu')
    network = max_pool_2d(network, 2)

    network = fully_connected(network, 1024, activation='relu') #4
    network = dropout(network, 0.8) #5

    network = fully_connected(network, N_CLASSES, activation='softmax')#6
    network = regression(network)

    model = tflearn.DNN(network) #7
    #
    model.load('../modelCNN/Modell_CNNs/mymodel.tflearn')

    def prepare(filepath):
        IMG_SIZE = 28 # This value must be the same as the value in Part1
        # img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(filepath, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    def result_answer(res):
        letter = ['A', 'B', 'C', 'D']
        return letter[int(res[0])]


    res = {}
    # res.append(np.argmax(model.predict(answer), axis=-1))
    for i, countour_img in enumerate(countours_img):
        res.update({"{}".format(i):"0"})
        for cnt in countour_img:
            if cv2.contourArea(cnt) > 20:
                # print(i)
                x, y, w, h = cv2.boundingRect(cnt)
                if x > cropped_origin_img[i].shape[1] * 0.1 and x < cropped_origin_img[i].shape[1] * 0.9:
                    answer = cropped_origin_img[i][y:y + h, x:x + w]
                    answer = cv2.threshold(answer, 160, 255, cv2.THRESH_BINARY_INV)[1]
                    res.update({"{}".format(i):result_answer(np.argmax(model.predict(prepare(answer)), axis=-1))})
                    # np.argmax(model.predict(prepare(answer)), axis=-1)
                    # name = "../outImg/imgRes/" + str(i+1) + ".jpg"
                    # cv2.imwrite(name, answer)

    return res