import pickle
import sqlite3

from PIL import Image
import cv2
import numpy as np
from itertools import groupby
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from matplotlib import pyplot as plt
from numpy import double
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import numpy
from scipy.signal import find_peaks


class Ui_Photo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1708, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(673, 10, 20, 821))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 200, 161, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 661, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(700, 10, 991, 821))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget_2 = PlotWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 959, 201))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = PlotWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(10, 578, 959, 201))
        self.widget_3.setObjectName("widget_3")
        self.widget = PlotWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 320, 959, 201))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 941, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 941, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 550, 941, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(10, 270, 961, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(10, 530, 961, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_4 = PlotWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(20, 50, 381, 291))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = PlotWidget(self.tab_2)
        self.widget_5.setGeometry(QtCore.QRect(20, 440, 381, 291))
        self.widget_5.setObjectName("widget_5")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(20, 370, 951, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(130, 740, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 740, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 740, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(300, 740, 31, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(110, 740, 16, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(210, 760, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(830, 740, 121, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(470, 490, 191, 21))
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(680, 480, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 420, 621, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.Page1_3 = QtWidgets.QWidget()
        self.Page1_3.setObjectName("Page1_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Page1_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_43 = QtWidgets.QLabel(self.Page1_3)
        self.label_43.setObjectName("label_43")
        self.gridLayout_6.addWidget(self.label_43, 3, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.Page1_3)
        self.label_44.setObjectName("label_44")
        self.gridLayout_6.addWidget(self.label_44, 0, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.Page1_3)
        self.label_45.setObjectName("label_45")
        self.gridLayout_6.addWidget(self.label_45, 4, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.Page1_3)
        self.label_46.setObjectName("label_46")
        self.gridLayout_6.addWidget(self.label_46, 3, 1, 1, 4)
        self.label_47 = QtWidgets.QLabel(self.Page1_3)
        self.label_47.setObjectName("label_47")
        self.gridLayout_6.addWidget(self.label_47, 1, 4, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.Page1_3)
        self.label_48.setObjectName("label_48")
        self.gridLayout_6.addWidget(self.label_48, 0, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.Page1_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_6.addWidget(self.comboBox_6, 0, 2, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.Page1_3)
        self.label_50.setObjectName("label_50")
        self.gridLayout_6.addWidget(self.label_50, 1, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.Page1_3)
        self.label_51.setObjectName("label_51")
        self.gridLayout_6.addWidget(self.label_51, 1, 3, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.Page1_3)
        self.label_52.setObjectName("label_52")
        self.gridLayout_6.addWidget(self.label_52, 1, 1, 1, 2)
        self.label_53 = QtWidgets.QLabel(self.Page1_3)
        self.label_53.setObjectName("label_53")
        self.gridLayout_6.addWidget(self.label_53, 2, 1, 1, 4)
        self.label_54 = QtWidgets.QLabel(self.Page1_3)
        self.label_54.setObjectName("label_54")
        self.gridLayout_6.addWidget(self.label_54, 2, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.Page1_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_6.addWidget(self.pushButton_12, 4, 4, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.Page1_3)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_6.addWidget(self.comboBox_7, 4, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.Page1_3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_6.addWidget(self.pushButton_13, 0, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Page1_3)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(473, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_49 = QtWidgets.QLabel(self.Page1_3)
        self.label_49.setObjectName("label_49")
        self.gridLayout_6.addWidget(self.label_49, 4, 1, 1, 2)
        self.tabWidget.addTab(self.Page1_3, "")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 50, 661, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 431, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 390, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 730, 661, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 810, 661, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(400, 750, 251, 54))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1708, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #################################################################################
        #################################################################################

        """ ************************************************************************* """
        """ *                                                                       * """
        """ *                               ПОЕХАЛИ                                 * """
        """ *                                                                       * """
        """ ************************************************************************* """

        #################################################################################
        #################################################################################

        self.pushButton.clicked.connect(self.open_photo_ariec)
        self.pushButton_4.clicked.connect(self.open_photo_patient)
        # self.pushButton_2.clicked.connect(self.photo_lets_go)
        self.pushButton_2.clicked.connect(self.rek_tomakova)
        self.pushButton_13.clicked.connect(self.add_to_database_new_data)
        self.pushButton_3.clicked.connect(self.save_array_pic_data_db)
        self.pushButton_5.clicked.connect(self.pic_graf2)
        self.pushButton_6.clicked.connect(self.pic_graf2_cl)

        self.customer_names()
        self.index_zn_type_photo()

    #################################################################################
    #################################################################################

    def open_photo_ariec(self):
        global photo_file_ariec_
        global photo_file_ariec

        photo_file_ariec_, check = QFileDialog.getOpenFileName(
            None,
            "Выберите 'ИДЕАЛЬНОЕ'Изображение",
            'Data/Image',
            "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )"
        )
        if check:
            photo_file_ariec = photo_file_ariec_

            self.pushButton_2.show()

    #################################################################################
    #################################################################################

    def no_pic(self):
        global photo_file_ariec

        if self.checkBox.isChecked():
            photo_file_ariec = 'Data\\Image\\2.png'

        else:
            self.open_photo_ariec()
            photo_file_ariec = photo_file_ariec_

    #################################################################################
    #################################################################################

    def open_photo_patient(self):
        global photo_file_patient

        photo_file_patient, check = QFileDialog.getOpenFileName(
            None,
            "Выберите 'ПОЛЬЗОВАТЕЛЬСКОЕ' Изображение",
            'Data/Image',
            "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )"
        )
        if check:
            self.pushButton_2.show()

    #################################################################################
    #################################################################################

    """___________________________________________________________________________"""

    def index_zn_type_photo(self):

        x = self.comboBox.currentText()
        global index_znach_type_photo_1
        global index_znach_type_photo_2
        global index_znach_type_photo_3

        if x == 'Светлое':
            index_znach_type_photo_1 = 127
            index_znach_type_photo_2 = 127
            index_znach_type_photo_3 = 127

        elif x == 'Среднее':
            index_znach_type_photo_1 = 127
            index_znach_type_photo_2 = 127
            index_znach_type_photo_3 = 100

        elif x == 'Темное':
            index_znach_type_photo_1 = 127
            index_znach_type_photo_2 = 127
            index_znach_type_photo_3 = 95

        else:
            print('Error_index_name')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('ТИП ПОЛЬЗОВАТЕЛЬСКОГО ИЗОБРАЖЕНИЯ НЕ ВЫБРАН!')
            msg.setWindowTitle("Error")
            msg.exec_()

        """___________________________________________________________________________"""

########################################################################################################################
    #################################################################################

    def photo_lets_go(self):

        self.widget.clear()
        self.widget_2.clear()
        self.widget_3.clear()

        # img = cv2.imread('Data\\Image\\IMG_4597.jpg')
        # img = cv2.imread('Data\\Image\\photo_2022-04-21_16-29-37.jpg')
        # if photo_file_ariec == '':
        #     photo_file_ariec = photo_file_ariec_no_pic
        imga = Image.open(photo_file_ariec)

        w = 650
        h = 100
        imga = imga.resize((w, h))

        imga.save('Data\\Image\\Temp\\new_img_ariec.png')

        img = cv2.imread('Data\\Image\\Temp\\new_img_ariec.png')


        ##############_Перевод_в_отенки_серого_######################

        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('Data\\Image\\Temp\\im_gray.png', im_gray)

        #############################################################

        img_g = cv2.imread('Data\\Image\\Temp\\im_gray.png')

        mask = cv2.inRange(img_g, (0, 0, 0), (127, 127, 127))
        mask = 255 - mask

        # save output
        cv2.imwrite('Data\\Image\\Temp\\black_spots_mask.png', mask)

        im = Image.open("Data\\Image\\Temp\\black_spots_mask.png")

        # rotate image by 90 degrees
        angle = 270
        out = im.rotate(angle, expand=True)
        out.save('Data\\Image\\Temp\\rotate-black_spots_mask.png')

        img_1 = cv2.imread('Data\\Image\\Temp\\rotate-black_spots_mask.png')

        arr = np.asarray(img_1)
        black_pixels = np.array(np.where(arr == 0))

        global black_pixel_coordinates

        black_pixel_coordinates = list(zip(black_pixels[0], black_pixels[1]))
        global res
        res = [max(g) for _, g in groupby(black_pixel_coordinates, lambda x: x[0])]

        ##############################_Выравнивание_под_0_###############################

        ff = res[0]
        df = 0 - ff[1]

        global dres
        dres = [[y + df for y in x] for x in res]

        #################################################################################

        self.widget_2.setBackground('w')
        pen2 = pg.mkPen(color=(12, 190, 80))
        self.widget_2.plot(double(dres), pen=pen2)

    #################################################################################
    #################################################################################

    def rek_tomakova(self):

        if self.checkBox.isChecked():
            self.no_pic()

        self.photo_lets_go()
        self.index_zn_type_photo()


        # img1 = cv2.imread(photo_file)
        img1 = Image.open(photo_file_patient)

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
        img1.save('Data\\Image\\Temp\\new_img.png')
        # self.widget1.clear()
        self.widget.clear()
        self.widget_3.clear()

        img = cv2.imread('Data\\Image\\Temp\\new_img.png')

        #############################################################
        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('Grayscale', im_gray)
        cv2.imwrite('Data\\Image\\Temp\\im_gray_new.png', im_gray)

        #############################################################

        img_g = cv2.imread('Data\\Image\\Temp\\im_gray_new.png')
        # low = (0,0,0)
        # high = (0,0,0)

        mask = cv2.inRange(img_g, (0, 0, 0), (index_znach_type_photo_1, index_znach_type_photo_2, index_znach_type_photo_3))
        # mask = cv2.inRange(im_gray, (0,0,0), (127, 127, 127))
        # mask = cv2.inRange(img, (0, 0, 0), (127, 127, 127))
        mask = 255 - mask

        # save output
        cv2.imwrite('Data\\Image\\Temp\\black_spots_mask_new.png', mask)

        im = Image.open("Data\\Image\\Temp\\black_spots_mask_new.png")

        # поворот изображения на 270
        angle = 270
        out = im.rotate(angle, expand=True)
        out.save('Data\\Image\\Temp\\rotate-black_spots_mask_new.png')

        img_1 = cv2.imread('Data\\Image\\Temp\\rotate-black_spots_mask_new.png')

        arr = np.asarray(img_1)
        black_pixels = np.array(np.where(arr == 0))
        black_pixel_coordinates_2 = list(zip(black_pixels[0], black_pixels[1]))

        print('длинна 1', len(black_pixel_coordinates))
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

        self.widget.setBackground('w')
        pen1 = pg.mkPen(color=(255, 0, 0))
        # self.widget_2.plot(double(d_res_g), pen=pen1)
        self.widget.plot(double(d_res_g), pen=pen1)

        self.widget_3.setBackground('w')
        pen1 = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(12, 190, 80))
        self.widget_3.plot((double(d_res_g)), pen=pen1)
        self.widget_3.plot((double(dres)), pen=pen2)

        print('длинна 1 ', len(res_g))
        print('длинна 2 ', len(res))
        print('длинна 1_1 ', len(d_res_g))
        print('длинна 2_1 ', len(dres))

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
        print('Длинна :',len(peaks2_patient))

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

        self.widget_5.clear()
        self.widget_5.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates_patient:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]
            self.widget_5.plot(x_, pen=pen)

        len_temp_patient = len(templates_patient) - 1
        self.horizontalSlider_2.setMaximum(len_temp_patient)
        # ggd = self.horizontalSlider_2.value()
        self.label_7.setText(str(len_temp_patient + 1))
        self.label_8.setText('1')


        #################################################################################

        arr_x_ariec = []
        arr_y_ariec = []

        for x_ariec, y_ariec in dres:
            arr_y_ariec.append(y_ariec)

        for x_ariec, y_ariec in dres:
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

        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates_ariec:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]
            self.widget_4.plot(x_, pen=pen)





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

        #################################################################################

        # peaks, _ = find_peaks(x, distance=250)
        # peaks3, _ = find_peaks(x, width=20)
        # peaks4, _ = find_peaks(x,
        #                        threshold=0.4)  # Required vertical distance to its direct neighbouring samples, pretty useless
        # plt.subplot(2, 2, 1)
        # plt.plot(peaks, x[peaks], "xr")
        # plt.plot(x)
        # plt.legend(['distance'])
        # plt.subplot(2, 2, 2)
        # plt.plot(peaks2, x[peaks2], "ob")
        # plt.plot(x)
        # plt.legend(['prominence'])
        # plt.subplot(2, 2, 3)
        # plt.plot(peaks3, x[peaks3], "vg")
        # plt.plot(x)
        # plt.legend(['width'])
        # plt.subplot(2, 2, 4)
        # plt.plot(peaks4, x[peaks4], "xk")
        # plt.plot(x)
        # plt.legend(['threshold'])
        # plt.show()




            # print(x_)
            # templates_.append(x_)
            # templates__ = (','.join(map(str, x_)))

        # print(templates_)
        # print(templates)
        # print(len(templates))


        # self.save_array_pic_data_db()

    #################################################################################
    #################################################################################
    #
    # def kjsh(self):
    #     ggd = self.horizontalSlider_2.value()
    #     self.label_9.setText(str(ggd))

    #################################################################################
    #################################################################################

    def pic_graf2(self):

        ggd = self.horizontalSlider_2.value()
        self.label_9.setText(str(ggd + 1))
        nnnnn = str(ggd)
        nnnnn_a = ggd - 1

        jdh_1 = templates_patient[int(nnnnn)]
        jdh_2 = templates_ariec[int(nnnnn_a)]

        ff = jdh_1
        ff_1 = jdh_2
        df = 0 - ff[1]
        df_1 = 0 - ff_1[1]
        jdh_1 = [y + df for y in jdh_1]
        jdh_2 = [y + df_1 for y in jdh_2]

        self.widget_5.clear()
        self.widget_5.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_5.plot(jdh_1, pen=pen)

        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_4.plot(jdh_2, pen=pen)

    #################################################################################
    #################################################################################

    def pic_graf2_cl(self):

        self.widget_5.clear()
        self.widget_5.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates_patient:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]
            self.widget_5.plot(x_, pen=pen)

        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates_ariec:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]
            self.widget_4.plot(x_, pen=pen)

    #################################################################################
    #################################################################################

    def customer_names(self):

        self.comboBox_6.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT snils FROM patient")
        sql = cursor.fetchall()
        self.names = []
        for i in sql:
            self.names.append(i[0])
        self.comboBox_6.addItems(self.names)

    #################################################################################
    #################################################################################

    """_________________________Вывод данных о пользователе_______________________"""

    def add_to_database_new_data(self):
        global xxx

        if self.lineEdit_5.text() == '':
            xxx = self.comboBox_6.currentText()
            self.lineEdit_5.setText('')

        else:
            xxx = self.lineEdit_5.text()
            self.lineEdit_5.setText('')

            while len(xxx) < 11:
                xxx = '0' + xxx
            xxx = f'{xxx[0:3]}-{xxx[3:6]}-{xxx[6:9]} {xxx[9:11]}'

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS patient(
                ID TEXT PRIMARY KEY,
                fio_ TEXT,
                address_ TEXT,
                data_b_ TEXT,
                diagnoz TEXT,
                snils TEXT,
                cD1_ TEXT,
                cD2_ TEXT,
                cD3_ TEXT,
                ScD1_ TEXT,
                ScD2_ TEXT,
                ScD3_ TEXT,
                H_ TEXT,
                c_ TEXT,
                Array_S BLOB,
                Array_P BLOB
                )''')
        try:
            cursor.execute(f'SELECT snils FROM patient WHERE snils ="{xxx}"')
            if cursor.fetchone() is None:
                print('ERROr_add_patient_db')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('СНИЛС не найден. БД не подключено!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                cursor.execute(f'SELECT ID FROM patient WHERE snils ="{xxx}"')
                ID = cursor.fetchall()
                id_ = []
                for i in ID:
                    id_.append(i[0])
                id__ = (''.join(map(str, id_)))
                self.label_48.setText(f'{id__}')

                cursor.execute(f'SELECT fio_ FROM patient WHERE snils ="{xxx}"')
                fio = cursor.fetchall()
                fio_ = []
                for i in fio:
                    fio_.append(i[0])
                fio__ = (''.join(map(str, fio_)))
                self.label_52.setText(f'{fio__}')

                cursor.execute(f'SELECT snils FROM patient WHERE snils ="{xxx}"')
                snils = cursor.fetchall()
                snils_ = []
                for i in snils:
                    snils_.append(i[0])
                snils__ = (''.join(map(str, snils_)))
                self.label_53.setText(f'{snils__}')

                cursor.execute(f'SELECT address_ FROM patient WHERE snils ="{xxx}"')
                address = cursor.fetchall()
                address__ = []
                for i in address:
                    address__.append(i[0])
                address___ = (''.join(map(str, address__)))
                self.label_46.setText(f'{address___}')

                cursor.execute(f'SELECT data_b_ FROM patient WHERE snils ="{xxx}"')
                data_b_ = cursor.fetchall()
                data_b__ = []
                for i in data_b_:
                    data_b__.append(i[0])
                data_b___ = (''.join(map(str, data_b__)))
                self.label_47.setText(f'{data_b___}')
                self.label_51.setText('Дата рождения:')

                cursor.execute(f'SELECT diagnoz FROM patient WHERE snils ="{xxx}"')
                diagnoz = cursor.fetchall()
                diagnoz_ = []
                for i in diagnoz:
                    diagnoz_.append(i[0])
                diagnoz__ = (''.join(map(str, diagnoz_)))
                self.label_49.setText(f'{diagnoz__}')

                db.close()

        except:

            print("таблица не существует")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Вы ввели ID, без выбора Таблицы БД!')
            msg.setWindowTitle("Error")
            msg.exec_()

        self.customer_names()
        # self.disease_comboBox()

    ####################################################################################################################
    ####################################################################################################################

    def save_array_pic_data_db(self):

        snils = self.comboBox_6.currentText()
        id__ = self.label_48.text()
        # dz = self.comboBox_4.currentText()
        # templates__ = (''.join(map(str, templates)))

        # with open(f"Data\\Pickle\\Image\\{snils}_i.pickle", "wb") as f:
        #     pickle.dump(templates_patient, f)
        #
        # DATA_JJ = f"Data\\Pickle\\Image\\{snils}_i.pickle"

        ggd = self.horizontalSlider_2.value()
        # self.label_30.setText(str(ggd + 1))
        nnnnn = str(ggd)

        for x in templates_patient:
            ddd = len(x)
        your_list = [i for i in range(0, ddd)]
        # with open(f"Data\\Patient CSV\\{xxx}.csv", "a") as p:
        #     import csv
        #     pr = csv.writer(p, delimiter=";", lineterminator='\n')
        #

        with open(f"Data\\Patient CSV\\Image\\{xxx}.csv", "w") as p:
            import csv
            pr = csv.writer(p, delimiter=";", lineterminator='\n')
            pr.writerow(your_list)
            pr.writerow(templates_patient[int(nnnnn)])

        DATA_JJ = f"Data\\Patient CSV\\Image\\{xxx}.csv"


        try:
            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f"""UPDATE patient SET 
                    Array_P = '{DATA_JJ}'
                    WHERE snils = '{snils}'""")

            db.commit()
            print("Запись успешно обновлена")
            cursor.close()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ура!")
            msg.setInformativeText('Данные успешно сохранены!')
            msg.setWindowTitle("=)")
            msg.exec_()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    ####################################################################################################################
    ####################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать сравнение"))
        self.label_2.setText(_translate("MainWindow", "График \"Идеальные\" значения:"))
        self.label_3.setText(_translate("MainWindow", "График \"Пользовательские\" значения:"))
        self.label_13.setText(_translate("MainWindow", "График сравнения \"Идеальные\" и \"Пользовательские\" значения:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Входные данные"))
        self.label_5.setText(_translate("MainWindow", "PQRST \"Идеальные\" значения:"))
        self.label_6.setText(_translate("MainWindow", "PQRST Пользователя:"))
        self.pushButton_5.setText(_translate("MainWindow", "Выбрать"))
        self.pushButton_6.setText(_translate("MainWindow", "Сбросить"))
        self.label_7.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "Использовать ИИ"))
        self.label_14.setText(_translate("MainWindow", "Прогнозируемая оценка для Врача: "))
        self.label_17.setText(_translate("MainWindow", "-"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Выходные данные"))
        self.label_43.setText(_translate("MainWindow", "Адрес:"))
        self.label_44.setText(_translate("MainWindow", "Пациент №:"))
        self.label_45.setText(_translate("MainWindow", "Диагноз:"))
        self.label_46.setText(_translate("MainWindow", "-"))
        self.label_47.setText(_translate("MainWindow", "-"))
        self.label_48.setText(_translate("MainWindow", "-"))
        self.label_50.setText(_translate("MainWindow", "ФИО: "))
        self.label_51.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_52.setText(_translate("MainWindow", "-"))
        self.label_53.setText(_translate("MainWindow", "-"))
        self.label_54.setText(_translate("MainWindow", "Снилс:"))
        self.pushButton_12.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_13.setText(_translate("MainWindow", "Выбрать"))
        self.label_49.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "Тип пользовательского изображения"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Выбрать\"Идеальное\" изображение "))
        self.label_10.setText(_translate("MainWindow", "Выбрать \"Пользовательское\" изображение"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Светлое"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Среднее"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Темное"))
        self.label_15.setText(_translate("MainWindow", "Работа с ИЗОБРАЖЕНИЯМИ"))
        self.label_16.setText(_translate("MainWindow", "ИНФОРМАЦИЯ:"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить в Базу данных"))
        self.pushButton_8.setText(_translate("MainWindow", "Создать отчет"))
        self.pushButton_9.setText(_translate("MainWindow", "Печать"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Photo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
