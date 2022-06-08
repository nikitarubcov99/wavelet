import sqlite3

from PIL import Image
import cv2
import numpy as np
from itertools import groupby
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
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
        self.comboBox_2.setGeometry(QtCore.QRect(50, 510, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 510, 81, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 251, 111))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 251, 111))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 251, 111))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 20, 961, 741))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = PlotWidget(self.layoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = PlotWidget(self.layoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = PlotWidget(self.layoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(340, 200, 321, 261))
        self.widget_4.setObjectName("widget_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 480, 661, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 510, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(504, 510, 161, 23))
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.pushButton_8.clicked.connect(self.add_to_database_new_data)
        self.pushButton_3.clicked.connect(self.save_array_pic_data_db)

        self.customer_names()
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

        self.widget.clear()
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

        mask = cv2.inRange(img_g, (0, 0, 0), (127, 127, 80))
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

        self.widget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget.plot(double(res), pen=pen)


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

        mask = cv2.inRange(img_g, (0, 0, 0), (127, 127, 70))
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

        # peaks, _ = find_peaks(x, distance=250)
        peaks2, _ = find_peaks(x, prominence=80)  # BEST!
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



        print(peaks2)
        global before
        global after
        if len(peaks2) == 6:
            before = 70
            after = 130

        elif len(peaks2) == 7:
            before = 100
            after = 160
        elif len(peaks2) < 6:
            before = 100
            after = 160


        R = np.sort(peaks2)
        print(peaks2)

        length = len(x)

        global templates

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

        self.widget_4.clear()
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x_ in templates:
            self.widget_4.plot(x_, pen=pen)

        # self.save_array_pic_data_db()

    def customer_names(self):

        self.comboBox_2.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT snils FROM patient")
        sql = cursor.fetchall()
        self.names = []
        for i in sql:
            self.names.append(i[0])
        self.comboBox_2.addItems(self.names)
    #################################################################################

    """_________________________Вывод данных о пользователе_______________________"""

    def add_to_database_new_data(self):
        global xxx

        if self.lineEdit.text() == '':
            xxx = self.comboBox_2.currentText()
            self.lineEdit.setText('')

        else:
            xxx = self.lineEdit.text()
            self.lineEdit.setText('')

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
                Array_S BLOW,
                Array_P BLOW
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
                self.label_26.setText(f'{id__}')

                cursor.execute(f'SELECT fio_ FROM patient WHERE snils ="{xxx}"')
                fio = cursor.fetchall()
                fio_ = []
                for i in fio:
                    fio_.append(i[0])
                fio__ = (''.join(map(str, fio_)))
                self.label_23.setText(f'{fio__}')

                cursor.execute(f'SELECT snils FROM patient WHERE snils ="{xxx}"')
                snils = cursor.fetchall()
                snils_ = []
                for i in snils:
                    snils_.append(i[0])
                snils__ = (''.join(map(str, snils_)))
                self.label_25.setText(f'{snils__}')

                cursor.execute(f'SELECT address_ FROM patient WHERE snils ="{xxx}"')
                address = cursor.fetchall()
                address__ = []
                for i in address:
                    address__.append(i[0])
                address___ = (''.join(map(str, address__)))
                self.label_27.setText(f'{address___}')

                cursor.execute(f'SELECT data_b_ FROM patient WHERE snils ="{xxx}"')
                data_b_ = cursor.fetchall()
                data_b__ = []
                for i in data_b_:
                    data_b__.append(i[0])
                data_b___ = (''.join(map(str, data_b__)))
                self.label_24.setText(f'{data_b___}')
                self.label_21.setText('Дата рождения:')

                cursor.execute(f'SELECT diagnoz FROM patient WHERE snils ="{xxx}"')
                diagnoz = cursor.fetchall()
                diagnoz_ = []
                for i in diagnoz:
                    diagnoz_.append(i[0])
                diagnoz__ = (''.join(map(str, diagnoz_)))
                # self.label_34.setText(f'{diagnoz__}')

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

    ########################################################################################################################

    def save_array_pic_data_db(self):

        snils = self.comboBox_2.currentText()
        # dz = self.comboBox_4.currentText()

        try:
            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f"""UPDATE patient SET 
                    Array_P = '{templates}'
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
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить в Базу данных"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Photo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
