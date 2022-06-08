from PIL import Image
import cv2
import numpy as np
from itertools import groupby
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from numpy import double
import pyqtgraph as pg
from pyqtgraph import PlotWidget


class Ui_Photo(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1699, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 20, 41, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(673, 10, 20, 761))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 540, 461, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.Page1 = QtWidgets.QWidget()
        self.Page1.setObjectName("Page1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Page1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_23 = QtWidgets.QLabel(self.Page1)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 1, 1, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.Page1)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.Page1)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.Page1)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.Page1)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.Page1)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.Page1)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.Page1)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 1, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.Page1)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 2, 1, 1, 4)
        self.label_27 = QtWidgets.QLabel(self.Page1)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 3, 1, 1, 4)
        self.tabWidget.addTab(self.Page1, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 20, 131, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 510, 341, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 510, 81, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 641, 111))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 641, 111))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 641, 111))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(710, 20, 961, 741))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget1 = PlotWidget(self.widget)
        self.widget1.setObjectName("widget1")
        self.verticalLayout.addWidget(self.widget1)
        self.widget_2 = PlotWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = PlotWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1699, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
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

        self.pushButton.clicked.connect(self.open_photo)
        # self.pushButton_2.clicked.connect(self.photo_lets_go)
        self.pushButton_2.clicked.connect(self.rek_tomakova)

        #################################################################################

    def open_photo(self):
        global photo_file

        photo_file, check = QFileDialog.getOpenFileName(None, "Выберите Изображение",
                                                        'Data/Image', "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )")
        if check:
            # self.label_6.setText(photo_file)
            # self.label_5.setText('Изображение закружено!')
            # self.pushButton.setEnabled(False)
            self.pushButton_2.show()

            # self.lineEdit.setText('11250')
            # self.lineEdit_2.setText('13500')

    def photo_lets_go(self):

        self.widget1.clear()
        self.widget_2.clear()
        self.widget_3.clear()

        img = cv2.imread('Data\\Image\\IMG_4597.jpg')

        #############################################################
        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('Grayscale', im_gray)
        cv2.imwrite('Data\\Image\\Temp\\im_gray.png', im_gray)

        #############################################################

        img_g = cv2.imread('Data\\Image\\Temp\\im_gray.png')
        # low = (0,0,0)
        # high = (0,0,0)

        mask = cv2.inRange(img_g, (0, 0, 0), (127, 127, 127))
        # mask = cv2.inRange(img, (0, 0, 0), (127, 127, 127))
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
        black_pixel_coordinates = list(zip(black_pixels[0], black_pixels[1]))
        global res
        res = [max(g) for _, g in groupby(black_pixel_coordinates, lambda x: x[0])]

        self.widget1.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget1.plot(double(res), pen=pen)


    def rek_tomakova(self):

        self.photo_lets_go()


        # img1 = cv2.imread(photo_file)
        img1 = Image.open(photo_file)
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


        img_pil = Image.open('Data\\Image\\IMG_4597.jpg')
        w , h = img_pil.size

        new_img = img1.resize((w, h))
        new_img.save('Data\\Image\\Temp\\new_img.png')
        # self.widget1.clear()
        self.widget_2.clear()
        self.widget_3.clear()

        img = cv2.imread('Data\\Image\\Temp\\new_img.png')

        #############################################################
        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('Grayscale', im_gray)
        cv2.imwrite('Data\\Image\\Temp\\im_gray1.png', im_gray)

        #############################################################

        img_g = cv2.imread('Data\\Image\\Temp\\im_gray1.png')
        # low = (0,0,0)
        # high = (0,0,0)

        mask = cv2.inRange(img_g, (0, 0, 0), (127, 127, 127))
        # mask = cv2.inRange(im_gray, (0,0,0), (127, 127, 127))
        # mask = cv2.inRange(img, (0, 0, 0), (127, 127, 127))
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
        black_pixel_coordinates_2 = list(zip(black_pixels[0], black_pixels[1]))
        global res_g
        # res_g = [max(g,key=lambda x: x[1]) for _, g in groupby(black_pixel_coordinates_2, lambda x: x[0])]

        black_pixel_coordinates_2.sort(key=lambda x: x[0])
        res_g = list(dict(black_pixel_coordinates_2).items())


        self.widget_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_2.plot(double(res_g), pen=pen)

        self.widget_3.setBackground('w')
        pen1 = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(12,190, 80))
        self.widget_3.plot((double(res_g)), pen=pen1)
        self.widget_3.plot((double(res)), pen=pen2)




        from scipy.signal import find_peaks, find_peaks_cwt
        arr_x = []
        arr_y = []
        for x,y in res_g:

        # for i in black_pixel_coordinates_2[1]:
            arr_y.append(y)
        for x,y in res_g:

        # for i in black_pixel_coordinates_2[1]:
            arr_x.append(x)

        # print(arr)

        import matplotlib.pyplot as plt
        from scipy.signal import find_peaks, find_peaks_cwt

        # x = np.sin(2 * np.pi * (2 ** np.linspace(2, 10, 1000)) * np.arange(1000) / 48000) + np.random.normal(0, 1,
        #                                                                                                      1000) * 0.15
        import numpy

        x = numpy.array(arr_y)

        peaks, _ = find_peaks(x, distance=250)
        peaks2, _ = find_peaks(x, prominence=80)  # BEST!
        peaks3, _ = find_peaks(x, width=20)
        peaks4, _ = find_peaks(x,
                               threshold=0.4)  # Required vertical distance to its direct neighbouring samples, pretty useless
        plt.subplot(2, 2, 1)
        plt.plot(peaks, x[peaks], "xr")
        plt.plot(x)
        plt.legend(['distance'])
        plt.subplot(2, 2, 2)
        plt.plot(peaks2, x[peaks2], "ob")
        plt.plot(x)
        plt.legend(['prominence'])
        plt.subplot(2, 2, 3)
        plt.plot(peaks3, x[peaks3], "vg")
        plt.plot(x)
        plt.legend(['width'])
        plt.subplot(2, 2, 4)
        plt.plot(peaks4, x[peaks4], "xk")
        plt.plot(x)
        plt.legend(['threshold'])
        plt.show()



        print(peaks2)

        before = 50
        after = 150
        R = np.sort(peaks2)
        print(peaks2)

        length = len(x)
        templates = []
        print(templates)

        # for j in R:
        for i in R:
            a = i - before
            if a < 0:
                continue
            b = i + after
            if b > length:
                break
            templates.append(x[a:b])
        templates = np.array(templates)

        self.widget1.clear()
        self.widget1.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates:
            self.widget1.plot(x_, pen=pen)



        # from biosppy.signals import ecg
        #
        # sampling_rate = 1000.0
        # order = int(0.3 * sampling_rate)
        # filtered, _, _ = ecg.st.filter_signal(signal=arr, ftype='FIR', band='bandpass', order=order,
        #                                       frequency=[3, 45], sampling_rate=1000.)
        # rpeaks = ecg.hamilton_segmenter(signal=filtered, sampling_rate=1000.)
        #
        # before = 200
        # after = 400
        # R = np.sort(rpeaks)
        # print(rpeaks)
        #
        # length = len(arr)
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
        #         templates.append(arr[a:b])
        # templates = np.array(templates)
        #
        # self.widget1.clear()
        # self.widget1.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        # for x in rpeaks:
        #     self.widget1.plot(x, pen=pen)
        #



        # peaks2, _ = find_peaks(arr, width=20)
        # peaks2, _ = find_peaks(arr,threshold=0.4)  # Required vertical distance to its direct neighbouring samples, pretty useless

        # peaks2, _ = find_peaks(arr, prominence=1)  # BEST!
        # print(peaks2)
        # self.srawnenie()

    #
    # def srawnenie(self):
    #     result = []
    #     for  x, y in res:
    #         for a, b, in res_g:
    #             if x == a and y == b:
    #                 x_=a
    #                 y_=b
    #             else:
    #                 x_ = x
    #                 y_ = y
    #             result.append([x_, y_])
    #

        # self.widget_3.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        # self.widget_3.plot(double(*LineString(intersection).xy), pen=pen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Выбрать изображение"))
        self.label_23.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "-"))
        self.label_24.setText(_translate("MainWindow", "-"))
        self.label_20.setText(_translate("MainWindow", "ФИО: "))
        self.label_22.setText(_translate("MainWindow", "Адрес:"))
        self.label_28.setText(_translate("MainWindow", "Диагноз:"))
        self.label_19.setText(_translate("MainWindow", "Пациент № "))
        self.label_21.setText(_translate("MainWindow", "Возраст:"))
        self.label_25.setText(_translate("MainWindow", "-"))
        self.label_27.setText(_translate("MainWindow", "-"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать сравнение"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Photo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
