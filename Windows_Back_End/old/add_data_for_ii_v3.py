import pickle
import sqlite3
import uuid

import numpy as np
import pandas as pd
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QApplication
from numpy import std, conj, subtract, var, polyfit, log10
from numpy import double

import pywt
from pyedflib import highlevel
from scipy.fft import fft
from PyQt5 import QtCore, QtGui, QtWidgets

# Imports
from PyQt5 import QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget


from add_patient_v2 import Ui_Add_DB_Patient
from View_DB_v1 import Ui_View_DB
from photo_v7 import Ui_Photo
from add_norm_znach import Ui_Add_Norm
from add_name_of_the_desease_v2 import Ui_Add_Disease

from hurst import compute_Hc

import pandas as pd
from sklearn import linear_model, model_selection
import pickle

from photo_v7 import *

class Ui_II(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 20, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 481, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 481, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 160, 481, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 110, 481, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 20, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 20, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 50, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 0, 21, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 20, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(550, 50, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 50, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(90, 300, 361, 271))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = PlotWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(630, 300, 361, 271))
        self.widget_5.setObjectName("widget_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 50, 131, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 190, 111, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 190, 131, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 190, 111, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 160, 111, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 160, 111, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 531, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 280, 531, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(550, 280, 541, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ################################################################################################################
        ################################################################################################################

        self.pushButton.clicked.connect(self.open_edf)
        self.pushButton_8.clicked.connect(self.open_photo)

        self.pushButton_5.clicked.connect(self.test_gg)
        self.pushButton_7.clicked.connect(self.test_gg_photo)

        self.pushButton_3.clicked.connect(self.customer_names_for_II)

        self.pushButton_2.clicked.connect(self.in_classes)
        self.pushButton_9.clicked.connect(self.in_classes_photo)

        self.customer_names()
        self.disease_comboBox()

        ################################################################################################################
        ################################################################################################################

########################################################################################################################
########################################################################################################################

    def customer_names(self):

        self.comboBox.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT snils FROM patient")
        sql = cursor.fetchall()
        self.names = []
        for i in sql:
            self.names.append(i[0])
        self.comboBox.addItems(self.names)

########################################################################################################################
########################################################################################################################

    def disease_comboBox(self):

        self.comboBox_3.clear()
        self.comboBox_4.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT name_of_the_disease FROM disease")
        sql = cursor.fetchall()
        self.disease = []
        for i in sql:
            self.disease.append(i[0])
        self.comboBox_3.addItems(self.disease)
        self.comboBox_4.addItems(self.disease)

########################################################################################################################
########################################################################################################################

    def index_zn(self):

        x = self.comboBox_3.currentText()
        global index_znach

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'SELECT kod_disease FROM disease WHERE name_of_the_disease ="{x}"')

        ID = cursor.fetchall()
        id_ = []
        for i in ID:
            id_.append(i[0])

        index_znach = id_
        print(index_znach)

        if index_znach == '':
            print('Error_index_name')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран индекс!')
            msg.setWindowTitle("Error")
            msg.exec_()

    """___________________________________________________________________________"""

########################################################################################################################
########################################################################################################################

    def index_zn_photo(self):

        x = self.comboBox_4.currentText()
        global index_znach_photoo

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'SELECT kod_disease FROM disease WHERE name_of_the_disease ="{x}"')

        ID = cursor.fetchall()
        id_ = []
        for i in ID:
            id_.append(i[0])

        index_znach_photoo = id_
        print(index_znach_photoo)

        if index_znach_photoo == '':
            print('Error_index_name')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран индекс!')
            msg.setWindowTitle("Error")
            msg.exec_()

    """___________________________________________________________________________"""

########################################################################################################################
########################################################################################################################

    def open_edf(self):
        global edf_file

        edf_file, check = QFileDialog.getOpenFileName(None, "Выберите EDF файл",
                                                      'Data/EDF', "EDF Files (*.edf)")
        if check:
            self.label_4.setText(edf_file)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("OK")
            msg.setInformativeText('Файл выбран!')
            msg.setWindowTitle("ok")
            msg.exec_()

########################################################################################################################
########################################################################################################################

    def open_photo(self):
        global photo_file

        photo_file, check = QFileDialog.getOpenFileName(
            None,
            "Выберите Изображение",
            'Data/Image',
            "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )"
        )
        if check:
            # self.label_4.setText(photo_file)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("OK")
            msg.setInformativeText('PHOTO выбран!')
            msg.setWindowTitle("ok")
            msg.exec_()

########################################################################################################################
########################################################################################################################

    def test_gg(self):

        self.index_zn()

        self.ID = uuid.uuid4()

        signals, signal_headers, header = highlevel.read_edf(edf_file)
        A = signals[1]

        print(A)

        # self.show()

        """Длинна сигнала"""
        A_length = len(A)
        print(A_length)

        # A_ = A[int(sig_1):int(sig_2)]
        A__length = len(A)
        print(A__length)

        signal = A

        from biosppy.signals import ecg

        sampling_rate = 1000.0
        order = int(0.3 * sampling_rate)
        filtered, _, _ = ecg.st.filter_signal(signal=signal, ftype='FIR', band='bandpass', order=order,
                                              frequency=[3, 45], sampling_rate=1000.)
        rpeaks = ecg.hamilton_segmenter(signal=filtered, sampling_rate=1000.)

        before = 200
        after = 400
        R = np.sort(rpeaks)
        print(rpeaks)

        length = len(A)

        global templates

        templates = []
        print(templates)

        for j in R:
            for i in j:
                a = i - before
                if a < 0:
                    continue
                b = i + after
                if b > length:
                    break
                templates.append(A[a:b])
        templates = np.array(templates)
        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        # for x in templates:
        #     ddd = len(x)
        # your_list = [i for i in range(0, ddd)]
        # with open("out.csv", "a") as p:
        #     import csv
        #     pr = csv.writer(p, delimiter=";", lineterminator='\n')
        #     pr.writerow(your_list)

        default_text = index_znach

        for x in templates:
            self.widget_4.plot(x, pen=pen)
            # dict_sample = dict({'Диагноз': 0, 'Данные': x})
            with open("Data\\Pickle\\For II\\data.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(x)
            with open("Data\\Pickle\\For II\\data_target.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(default_text)

        self.label.setText(str(len(templates)))


########################################################################################################################
########################################################################################################################

    def test_gg_photo(self):

        self.index_zn_photo()


        #
        #
        # ID = uuid.uuid4()
        #
        # signals, signal_headers, header = highlevel.read_edf(edf_file)
        # A = signals[1]
        #
        # print(A)
        #
        # # self.show()
        #
        # """Длинна сигнала"""
        # A_length = len(A)
        # print(A_length)
        #
        # # A_ = A[int(sig_1):int(sig_2)]
        # A__length = len(A)
        # print(A__length)
        #
        # signal = A
        #
        # from biosppy.signals import ecg
        #
        # sampling_rate = 1000.0
        # order = int(0.3 * sampling_rate)
        # filtered, _, _ = ecg.st.filter_signal(signal=signal, ftype='FIR', band='bandpass', order=order,
        #                                       frequency=[3, 45], sampling_rate=1000.)
        # rpeaks = ecg.hamilton_segmenter(signal=filtered, sampling_rate=1000.)
        #
        # before = 200
        # after = 400
        # R = np.sort(rpeaks)
        # print(rpeaks)
        #
        # length = len(A)
        #
        # global templates
        #
        # templates = []
        # print(templates)
        #
        # for j in R:
        #     for i in j:
        #         a = i - before
        #         if a < 0:
        #             continue
        #         b = i + after
        #         if b > length:
        #             break
        #         templates.append(A[a:b])
        # templates = np.array(templates)
        # self.widget_4.clear()
        # self.widget_4.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        # # for x in templates:
        # #     ddd = len(x)
        # # your_list = [i for i in range(0, ddd)]
        # # with open("out.csv", "a") as p:
        # #     import csv
        # #     pr = csv.writer(p, delimiter=";", lineterminator='\n')
        #     pr.writerow(your_list)

        # default_text = index_znach
        #
        # for x in templates:
        #     self.widget_4.plot(x, pen=pen)
        #     # dict_sample = dict({'Диагноз': 0, 'Данные': x})
        #     with open("Data\\Pickle\\For II\\data.csv", "a") as p:
        #         import csv
        #         pr = csv.writer(p, delimiter=";", lineterminator='\n')
        #         pr.writerow(x)
        #     with open("Data\\Pickle\\For II\\data_target.csv", "a") as p:
        #         import csv
        #         pr = csv.writer(p, delimiter=";", lineterminator='\n')
        #         pr.writerow(default_text)



        # img1 = cv2.imread(photo_file)
        img1 = Image.open(photo_file)

        w = 650
        h = 100
        img1 = img1.resize((w, h))
        # m = len(img)
        # n = len(img[0])
        # result = [[] for i in range(n)]
        # for i in range(m + 1):
        #     for j in range(n):
        #         if i == m:
        #             result[j].append(0)
        #         else:
        #             result[j].append(img[i][j])
        #
        # # changed = change(img)
        # print(img)

        # img_pil = Image.open(photo_file_ariec)
        # img_pil = Image.open('Data\\Image\\photo_2022-04-21_16-29-37.jpg')
        # w, h = img_pil.size

        # new_img = img1.resize((w, h))
        img1.save('Data\\Image\\Temp\\new_img_for_ii.png')
        # self.widget1.clear()
        img = cv2.imread('Data\\Image\\Temp\\new_img_for_ii.png')

        #############################################################
        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('Grayscale', im_gray)
        cv2.imwrite('Data\\Image\\Temp\\im_gray_new_for_ii.png', im_gray)

        #############################################################

        img_g = cv2.imread('Data\\Image\\Temp\\im_gray_new_for_ii.png')
        # low = (0,0,0)
        # high = (0,0,0)

        index_znach_type_photo_1_ariec = 127
        index_znach_type_photo_2_ariec = 127
        index_znach_type_photo_3_ariec = 90

        mask = cv2.inRange(img_g, (0, 0, 0),
                           (index_znach_type_photo_1_ariec, index_znach_type_photo_2_ariec, index_znach_type_photo_3_ariec))
        # mask = cv2.inRange(im_gray, (0,0,0), (127, 127, 127))
        # mask = cv2.inRange(img, (0, 0, 0), (127, 127, 127))
        mask = 255 - mask

        # save output
        cv2.imwrite('Data\\Image\\Temp\\black_spots_mask_new_for_ii.png', mask)

        im = Image.open("Data\\Image\\Temp\\black_spots_mask_new_for_ii.png")

        # поворот изображения на 270
        angle = 270
        out = im.rotate(angle, expand=True)
        out.save('Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')

        img_1 = cv2.imread('Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')

        arr = np.asarray(img_1)
        black_pixels = np.array(np.where(arr == 0))
        black_pixel_coordinates_2 = list(zip(black_pixels[0], black_pixels[1]))

        print('длинна 2', len(black_pixel_coordinates_2))

        global res_g

        res_g = [max(g) for _, g in groupby(black_pixel_coordinates_2, lambda x: x[0])]

        # black_pixel_coordinates_2.sort(key=lambda x: x[0])
        # res_g = list(dict(black_pixel_coordinates_2).items())

        #################################################################################

        ff = res_g[0]
        df = 0 - ff[1]
        #
        # print('первый элемент = ', ff)
        # print('0 - первый элемент = ', df)
        # ass = [0, df]

        d_res_g = [[y + df for y in x] for x in res_g]

        #################################################################################

        self.widget_4.setBackground('w')
        pen1 = pg.mkPen(color=(255, 0, 0))
        # self.widget_2.plot(double(d_res_g), pen=pen1)
        self.widget_4.plot(double(d_res_g), pen=pen1)


        # print('длинна 1 ', len(res_g))
        #
        # print('длинна 1_1 ', len(d_res_g))



        #################################################################################
        #################################################################################

        global before_patient
        global after_patient
        global templates_patient

        arr_x_patient = []
        arr_y_patient = []

        # for x_patient, y_patient in d_res_g:
        for x_patient, y_patient in d_res_g:
            arr_y_patient.append(y_patient)

        # for x_patient, y_patient in d_res_g:
        for x_patient, y_patient in d_res_g:
            arr_x_patient.append(x_patient)

        y_patient = np.array(arr_y_patient)
        peaks2_patient, _ = find_peaks(y_patient, prominence=30)  # BEST!
        # peaks2_patient, _ = find_peaks(y_patient, prominence=80)  # BEST!

        # plt.subplot(2, 2, 2)
        # plt.plot(peaks2_patient, y_patient[peaks2_patient], "ob")
        # plt.plot(y_patient)
        # plt.legend(['prominence'])
        # plt.figure(figsize=(17, 5))
        # plt.title(f"Компоненты сигнала на частоте {Fr1} Hz")
        # plt.plot(DDDcD1)  # строим график - ось `X` - первый столбец, `Y` - второй
        plt.show()
        print(peaks2_patient)
        print('Длинна :', len(peaks2_patient))

        self.label_2.setText(f'Кол-во: {str(len(peaks2_patient))}')

        # if len(peaks2_patient) == 6:
        before_patient = 40
        after_patient = 60

        # elif len(peaks2_patient) == 7:
        #     before_patient = 100
        #     after_patient = 150
        #
        # elif len(peaks2_patient) < 6:
        #     before_patient = 100
        #     after_patient = 160
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("Ошибка")
        #     msg.setInformativeText('Загрузите изображение, где больше 6 зубцов QRS.')
        #     msg.setWindowTitle("Error")
        #     msg.exec_()

        R_patient = np.sort(peaks2_patient)
        print(peaks2_patient)

        length_patient = len(y_patient)

        templates_patient = []
        # templates_ = []
        print(templates_patient)

        # for j in R:
        for i in R_patient:
            a = i - before_patient
            if a < 0:
                continue
            b = i + after_patient
            if b > length_patient:
                break
            templates_patient.append(y_patient[a:b])

        templates_patient = np.array(templates_patient)

        # with open("Data\\Pickle\\savedata.pickle", "wb") as f:
        #     pickle.dump(templates_patient, f)

        # self.widget_5.clear()
        # self.widget_5.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        # for x_ in templates_patient:
        #     ff = x_
        #     df = 0 - ff[1]
        #     x_ = [y + df for y in x_]
        #     self.widget_5.plot(x_, pen=pen)

        # len_temp_patient = len(templates_patient) - 1
        # self.horizontalSlider_2.setMaximum(len_temp_patient)
        # # ggd = self.horizontalSlider_2.value()
        # self.label_7.setText(str(len_temp_patient + 1))
        # self.label_8.setText('1')

        #################################################################################

        arr_x_ariec = []
        arr_y_ariec = []

        for x_ariec, y_ariec in d_res_g:
            arr_y_ariec.append(y_ariec)

        for x_ariec, y_ariec in d_res_g:
            arr_x_ariec.append(x_ariec)

        y_ariec = numpy.array(arr_y_ariec)
        peaks2_ariec, _ = find_peaks(y_ariec, prominence=30)  # BEST!
        # peaks2_ariec, _ = find_peaks(y_ariec, prominence=80)  # BEST!

        # plt.plot(peaks2_ariec, y_ariec[peaks2_ariec], "ob")
        # plt.plot(y_ariec)
        # plt.legend(['prominence'])

        print(peaks2_ariec)
        global before_ariec
        global after_ariec

        before_ariec = 40
        after_ariec = 60

        # if len(peaks2_ariec) == 6:
        #     before_ariec = 100
        #     after_ariec = 150
        #
        # elif len(peaks2_ariec) == 7:
        #     before_ariec = 100
        #     after_ariec = 150
        # # elif len(peaks2_ariec) < 6:
        # #     before_ariec = 100
        # #     after_ariec = 160
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("Ошибка")
        #     msg.setInformativeText('Загрузите изображение, где больше 6 зубцов QRS.')
        #     msg.setWindowTitle("Error")
        #     msg.exec_()

        R_ariec = np.sort(peaks2_ariec)
        print(peaks2_ariec)

        length = len(y_ariec)

        global templates_ariec

        templates_ariec = []
        # templates_ = []
        print(templates_ariec)

        # for j in R:
        for i in R_ariec:
            a = i - before_ariec
            if a < 0:
                continue
            b = i + after_ariec
            if b > length:
                break
            templates_ariec.append(y_ariec[a:b])

        # with open("Data\\file.txt", "w") as output:
        #     output.write(str(templates), )

        templates_ariec = np.array(templates_ariec)
        #
        # with open("Data\\file1.txt", "w") as output:
        #     output.write(str(templates), )
        default_text = index_znach_photoo
        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates_ariec:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]
            self.widget_4.plot(x_, pen=pen)

            with open("Data\\Pickle\\For II\\data_photo.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(x_)
            with open("Data\\Pickle\\For II\\data_target_photo.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(default_text)


        #################################################################################

        dddh = len(peaks2_patient)
        dddk = len(peaks2_ariec)

        if dddh != dddk:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText(
                f'Вы загрузили изображения с различным кол-вом PQRST пиков!!!\n\n '
                f'{dddk} PQRST "Идеального" изображеня  !=  {dddh} PQRST "Пользовательского" изображения.\n\n '
                f'Это скажется на КАЧЕСТВО дальнейшей работы!!!'
            )
            msg.setWindowTitle("Error")
            msg.exec_()
        #################################################################################

        dddf = len(peaks2_patient)
        ddde = len(templates_patient)

        if dddf > ddde:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText(
                f'Выведенно {ddde} PQRST, вместо {dddf} PQRST. \n\n'
                f'Так как недостаточно было данных для определения границ!'
            )
            msg.setWindowTitle("Error")
            msg.exec_()


########################################################################################################################
########################################################################################################################

    def customer_names_for_II(self):

        global linear_patient

        snils = self.comboBox.currentText()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT Array_S FROM patient WHERE snils = '{snils}'")
        sql = cursor.fetchall()

        names = []
        for i in sql:
            names.append(i[0])

        names__ = (''.join(map(str, names)))

        linear_patient = pd.read_csv(f'{names__}', sep=";")

        # pickle_in_ = open(f'{names__}', "r")
        # print(pickle_in_)
        #
        #
        # linear_patient = pickle.load(pickle_in_)
        # print(linear_patient)

        pickle_in = open("Data\\Pickle\\For II\\savedata.pickle", "rb")
        linear = pickle.load(pickle_in)
        # self.names = []
        # for i in sql:
        #     self.names.append(i[0])
        # self.comboBox_2.addItems(self.names)

        X_test1 = linear_patient
        predictions1 = linear.predict(X_test1)
        # print("Новые входные данные:          ", )

        print(predictions1)

        predictions1 = (''.join(map(str, predictions1)))

        print(predictions1)

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'SELECT name_of_the_disease FROM disease WHERE kod_disease ="{predictions1}"')

        ID = cursor.fetchall()
        id_ = []
        for i in ID:
            id_.append(i[0])
        id__ = (''.join(map(str, id_)))

        gg = id__

        # print("Прогнозируемая оценка для Врача:      "'\n', gg)
        self.label_4.setText(f"Прогнозируемая оценка для Врача:      {gg}")

        self.customer_names_for_II_photo()

########################################################################################################################
########################################################################################################################

    def customer_names_for_II_photo(self):

        global linear_patient_photo

        snils = self.comboBox.currentText()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT Array_P FROM patient WHERE snils = '{snils}'")
        sql = cursor.fetchall()

        names = []
        for i in sql:
            names.append(i[0])

        names__ = (''.join(map(str, names)))

        linear_patient_photo = pd.read_csv(f'{names__}', sep=";")

        # pickle_in_ = open(f'{names__}', "r")
        # print(pickle_in_)
        #
        #
        # linear_patient = pickle.load(pickle_in_)
        # print(linear_patient)

        pickle_in = open("Data\\Pickle\\For II\\savedata_photo.pickle", "rb")
        linear = pickle.load(pickle_in)
        # self.names = []
        # for i in sql:
        #     self.names.append(i[0])
        # self.comboBox_2.addItems(self.names)

        X_test1 = linear_patient_photo
        predictions1 = linear.predict(X_test1)
        # print("Новые входные данные:          ", )

        print(predictions1)

        predictions1 = (''.join(map(str, predictions1)))

        print(predictions1)

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'SELECT name_of_the_disease FROM disease WHERE kod_disease ="{predictions1}"')

        ID = cursor.fetchall()
        id_ = []
        for i in ID:
            id_.append(i[0])
        id__ = (''.join(map(str, id_)))

        gg = id__

        # print("Прогнозируемая оценка для Врача:      "'\n', gg)
        self.label_3.setText(f"Прогнозируемая оценка для Врача:      {gg}")

########################################################################################################################
########################################################################################################################

    def in_classes(self):

        data = pd.read_csv("Data\\Pickle\\For II\\data.csv", sep=";")
        data_target = pd.read_csv("Data\\Pickle\\For II\\data_target.csv")

        X = data
        Y = data_target

        best = 0
        for j in range(2000):
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.1)
            linear = linear_model.Perceptron()

            linear.fit(X_train, Y_train)
            acc = linear.score(X_test, Y_test)
            # print("Точность: " + str(acc))

            # Сохранение высочайшей точности
            if acc > best:
                best = acc
                with open("Data\\Pickle\\For II\\savedata.pickle", "wb") as f:
                    pickle.dump(linear, f)

########################################################################################################################
########################################################################################################################

    def in_classes_photo(self):

        data = pd.read_csv("Data\\Pickle\\For II\\data_photo.csv", sep=";")
        data_target = pd.read_csv("Data\\Pickle\\For II\\data_target_photo.csv")

        X = data
        Y = data_target

        best = 0
        for j in range(2000):
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.1)
            linear = linear_model.Perceptron()

            linear.fit(X_train, Y_train)
            acc = linear.score(X_test, Y_test)
            # print("Точность: " + str(acc))

            # Сохранение высочайшей точности
            if acc > best:
                best = acc
                with open("Data\\Pickle\\For II\\savedata_photo.pickle", "wb") as f:
                    pickle.dump(linear, f)

########################################################################################################################
########################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать Файл"))
        self.label.setText(_translate("MainWindow", "Кол-во: "))
        self.label_2.setText(_translate("MainWindow", "Кол-во:"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать обучение"))
        self.pushButton_3.setText(_translate("MainWindow", "Запуск"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить ВЕСА"))
        self.pushButton_5.setText(_translate("MainWindow", "ТЕСТ"))
        self.pushButton_6.setText(_translate("MainWindow", "Сохранить ВЕСА"))
        self.pushButton_7.setText(_translate("MainWindow", "ТЕСТ"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать Файл"))
        self.pushButton_9.setText(_translate("MainWindow", "Начать обучение"))
        self.label_5.setText(_translate("MainWindow", "Работа с Изображениями:"))
        self.label_6.setText(_translate("MainWindow", "Работа с Сигналом:"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_II()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
