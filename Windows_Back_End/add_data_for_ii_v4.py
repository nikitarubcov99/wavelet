import pickle
import sqlite3
import uuid

import numpy as np
import pandas as pd
from numpy.distutils.fcompiler import pg
from pyedflib import highlevel
from biosppy.signals import ecg
from sklearn import linear_model, model_selection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import pandas as pd
from PIL import Image
import cv2
import numpy as np
from itertools import groupby
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from matplotlib import pyplot as plt
from numpy import double
import pyqtgraph as pg
import numpy
from scipy.signal import find_peaks


class Ui_II(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 787)
        MainWindow.setMinimumSize(QtCore.QSize(620, 787))
        MainWindow.setMaximumSize(QtCore.QSize(620, 787))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 600, 31))
        self.label_3.setMinimumSize(QtCore.QSize(600, 31))
        self.label_3.setMaximumSize(QtCore.QSize(600, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 601, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 270, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 511, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 220, 511, 41))
        self.label.setObjectName("label")
        self.widget_4 = PlotWidget(self.tab)
        self.widget_4.setGeometry(QtCore.QRect(110, 330, 371, 271))
        self.widget_4.setObjectName("widget_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(110, 610, 371, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 300, 571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 511, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 270, 121, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_5 = PlotWidget(self.tab_2)
        self.widget_5.setGeometry(QtCore.QRect(110, 330, 371, 271))
        self.widget_5.setObjectName("widget_5")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(10, 300, 571, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(110, 610, 371, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 80, 511, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
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

        ################################################################################################################
        ################################################################################################################

        """вкладка работа с Изображением"""

        self.pushButton.clicked.connect(self.open_photo)  # Выбираем изображение
        self.pushButton_5.clicked.connect(self.test_gg_photo)  # активация кнопки "Произвести расчеты"
        self.pushButton_2.clicked.connect(self.in_classes_photo)  # активация кнопки "Начать обучение"
        self.pushButton_10.clicked.connect(self.save_W_photo)  # активация кнопки "сохранить веса"

        self.porog_comboBox()  # Вывод типа изоюражений в combobox_5
        self.disease_comboBox()  # Вывод название болезней в combobox_3
        # self.tip_image_comboBox()  # Вывод типа изоюражений в combobox_5

        ################################################################################################################

        """вкладка работа с Сигналом"""

        self.pushButton_8.clicked.connect(self.open_edf)  # Выбираем edf файл
        self.pushButton_7.clicked.connect(self.test_gg)  #
        self.pushButton_9.clicked.connect(self.in_classes)
        self.pushButton_6.clicked.connect(self.save_W)

        self.disease_comboBox()

        ################################################################################################################

    ####################################################################################################################
    #################################################################################

    def porog_comboBox(self):
        self.comboBox_5.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        cursor.execute("SELECT name FROM porog_photo")
        sql = cursor.fetchall()
        porog = []
        for i in sql:
            porog.append(i[0])
        self.comboBox_5.addItems(porog)

    #################################################################################
    #################################################################################

    """___________________________________________________________________________"""

    def tip_image_comboBox(self):

        # global index_znach_type_photo_1_ariec
        # global index_znach_type_photo_2_ariec
        # global index_znach_type_photo_3_ariec

        xxx = self.comboBox_5.currentText()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS porog_photo(
                            ID TEXT ,
                            name TEXT PRIMARY KEY,
                            porog_1 TEXT,
                            porog_2 TEXT,
                            porog_3 TEXT
                            )''')
        try:
            cursor.execute(f'SELECT name FROM porog_photo WHERE name ="{xxx}"')
            if cursor.fetchone() is None:
                print('ERROr_add_porog_db')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('ТИП ФОТО не найден. БД не подключено!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                cursor.execute(f'SELECT porog_1 FROM porog_photo WHERE name ="{xxx}"')
                porog_1 = cursor.fetchall()
                porog_1_ = []
                for i in porog_1:
                    porog_1_.append(i[0])
                # index_znach_type_photo_1_ariec = porog_1_
                self.index_znach_type_photo_1_ariecc = (''.join(map(str, porog_1_)))
                self.index_znach_type_photo_1_ariec = int(self.index_znach_type_photo_1_ariecc)
                print(self.index_znach_type_photo_1_ariec)

                cursor.execute(f'SELECT porog_2 FROM porog_photo WHERE name ="{xxx}"')
                porog_2 = cursor.fetchall()
                porog_2_ = []
                for i in porog_2:
                    porog_2_.append(i[0])
                # index_znach_type_photo_2_ariec = porog_2_
                self.index_znach_type_photo_2_ariecc = (''.join(map(str, porog_2_)))
                self.index_znach_type_photo_2_ariec = int(self.index_znach_type_photo_2_ariecc)

                print(self.index_znach_type_photo_2_ariec)

                cursor.execute(f'SELECT porog_3 FROM porog_photo WHERE name ="{xxx}"')
                porog_3 = cursor.fetchall()
                porog_3_ = []
                for i in porog_3:
                    porog_3_.append(i[0])
                # index_znach_type_photo_3_ariec = porog_3_
                self.index_znach_type_photo_3_ariecc = (''.join(map(str, porog_3_)))
                self.index_znach_type_photo_3_ariec = int(self.index_znach_type_photo_3_ariecc)

                print(self.index_znach_type_photo_3_ariec)

                db.close()
        except:

            print("таблица не существует")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Вы ввели ID, без выбора Таблицы БД!')
            msg.setWindowTitle("Error")
            msg.exec_()

        """___________________________________________________________________________"""

    ####################################################################################################################
    ####################################################################################################################

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

    ####################################################################################################################
    ####################################################################################################################

    def index_zn(self):

        x = self.comboBox_4.currentText()
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

    ####################################################################################################################
    ####################################################################################################################

    def index_zn_photo(self):

        x = self.comboBox_3.currentText()
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

    ####################################################################################################################
    ####################################################################################################################

    def open_edf(self):
        global edf_file

        edf_file, check = QFileDialog.getOpenFileName(None, "Выберите EDF файл",
                                                      'Data/EDF', "EDF Files (*.edf)")
        if check:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("OK")
            msg.setInformativeText('Файл выбран!')
            msg.setWindowTitle("ok")
            msg.exec_()

        if edf_file == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран EDF файл!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.open_edf()
    ####################################################################################################################
    ####################################################################################################################

    def open_photo(self):
        global photo_file

        photo_file, check = QFileDialog.getOpenFileName(
            None,
            "Выберите Изображение",
            'Data/Image',
            "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )"
        )
        if check:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("OK")
            msg.setInformativeText('PHOTO выбран!')
            msg.setWindowTitle("ok")
            msg.exec_()

        if photo_file == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбрано PHOTO!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.open_photo()
    ####################################################################################################################
    ####################################################################################################################

    def test_gg(self):
        global templates_edf

        self.index_zn()

        self.ID = uuid.uuid4()

        try:
            edf_file

            signals, signal_headers, header = highlevel.read_edf(edf_file)
            comp_signal = signals[1]

            print(comp_signal)

            """Длинна сигнала"""
            comp_signal_length = len(comp_signal)
            print(comp_signal_length)
            A__length = len(comp_signal)
            print(A__length)

            signal = comp_signal

            sampling_rate = 1000.0
            order = int(0.3 * sampling_rate)
            filtered, _, _ = ecg.st.filter_signal(signal=signal, ftype='FIR', band='bandpass', order=order,
                                                  frequency=[3, 45], sampling_rate=1000.)
            rpeaks = ecg.hamilton_segmenter(signal=filtered, sampling_rate=1000.)

            before = 200
            after = 400
            R = np.sort(rpeaks)
            print(rpeaks)

            length = len(comp_signal)

            templates_edf = []
            print(templates_edf)

            for j in R:
                for i in j:
                    a = i - before
                    if a < 0:
                        continue
                    b = i + after
                    if b > length:
                        break
                    templates_edf.append(comp_signal[a:b])
            templates_edf = np.array(templates_edf)
            self.widget_5.clear()
            self.widget_5.setBackground('w')
            pen = pg.mkPen(color=(255, 0, 0))

            for x in templates_edf:
                self.widget_5.plot(x, pen=pen)

            self.label_2.setText(f'Кол-во PQRST: {str(len(templates_edf))}')

        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран EDF файл!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.open_edf()

    ####################################################################################################################
    ####################################################################################################################

    def save_W(self):
        pen = pg.mkPen(color=(255, 0, 0))
        default_text = index_znach

        for x in templates_edf:
            self.widget_4.plot(x, pen=pen)
            with open("Data\\Pickle\\For II\\data.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(x)
            with open("Data\\Pickle\\For II\\data_target.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(default_text)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Add+")
        msg.setInformativeText('ВЕСА успешно сохранены!')
        msg.setWindowTitle("Add")
        msg.exec_()

    ####################################################################################################################
    ####################################################################################################################

    def test_gg_photo(self):

        self.index_zn_photo()
        self.tip_image_comboBox()

        try:
            photo_file

            index_znach_type_photo_1_ariec = self.index_znach_type_photo_1_ariec
            index_znach_type_photo_2_ariec = self.index_znach_type_photo_2_ariec
            index_znach_type_photo_3_ariec = self.index_znach_type_photo_3_ariec

            TestGG(photo_file, index_znach_type_photo_1_ariec, index_znach_type_photo_2_ariec, index_znach_type_photo_3_ariec)

            self.widget_4.clear()

            self.widget_4.setBackground('w')
            pen = pg.mkPen(color=(255, 0, 0))
            for x_ in templates_ariec:
                ff = x_
                df = 0 - ff[1]
                x_ = [y + df for y in x_]
                self.widget_4.plot(x_, pen=pen)

            self.label.setText(f'Кол-во PQRST: {str(len(templates_ariec))}')

            dddf = len(peaks2_ariec)
            ddde = len(templates_ariec)

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

        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбрано PHOTO!')
            msg.setWindowTitle("Error")
            msg.exec_()
            self.open_photo()

    ####################################################################################################################
    ####################################################################################################################
    def save_W_photo(self):

        default_text = index_znach_photoo

        for x_ in templates_ariec:
            ff = x_
            df = 0 - ff[1]
            x_ = [y + df for y in x_]

            with open("Data\\Pickle\\For II\\data_photo.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(x_)
            with open("Data\\Pickle\\For II\\data_target_photo.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(default_text)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Add+")
        msg.setInformativeText('ВЕСА успешно сохранены!')
        msg.setWindowTitle("Add")
        msg.exec_()

    ####################################################################################################################
    ####################################################################################################################

    def in_classes(self):

        data = pd.read_csv("Data\\Pickle\\For II\\data.csv", sep=";")
        data_target = pd.read_csv("Data\\Pickle\\For II\\data_target.csv")

        X = data
        Y = data_target

        best = 0
        for j in range(2000):
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.3)
            linear = linear_model.Perceptron()

            linear.fit(X_train, Y_train)
            acc = linear.score(X_test, Y_test)
            # print("Точность: " + str(acc))

            # Сохранение высочайшей точности
            if acc > best:
                best = acc
                with open("Data\\Pickle\\For II\\savedata.pickle", "wb") as f:
                    pickle.dump(linear, f)

    ####################################################################################################################
    ####################################################################################################################

    def in_classes_photo(self):


        data_photo = "Data\\Pickle\\For II\\data_photo.csv"
        data_target_photo = "Data\\Pickle\\For II\\data_target_photo.csv"

        II_in_classes_photo(data_photo, data_target_photo)

    ########################################################################################################################
    ########################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Добавление и Обучение Данных"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать обучение"))
        self.label_6.setText(_translate("MainWindow", "Работа с Изображением:"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать Файл"))
        self.label_7.setText(_translate("MainWindow", "Тип изображения:"))
        self.pushButton_5.setText(_translate("MainWindow", "Произвести расчет"))
        self.label_4.setText(_translate("MainWindow", "Выбор болезни:"))
        self.pushButton_10.setText(_translate("MainWindow", "Сохранить значения"))
        self.label.setText(_translate("MainWindow", "Кол-во PQRST: -"))
        self.label_8.setText(_translate("MainWindow", "Визуализация PQRST"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Работа с Изображением"))
        self.label_5.setText(_translate("MainWindow", "Работа с Сигналом:"))
        self.label_2.setText(_translate("MainWindow", "Кол-во PQRST: -"))
        self.pushButton_9.setText(_translate("MainWindow", "Начать обучение"))
        self.label_10.setText(_translate("MainWindow", "Визуализация PQRST"))
        self.label_11.setText(_translate("MainWindow", "Выбор болезни:"))
        self.pushButton_6.setText(_translate("MainWindow", "Сохранить значения"))
        self.pushButton_7.setText(_translate("MainWindow", "Произвести расчет"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать Файл"))
        self.label_13.setText(_translate("MainWindow", "Файл edf сигнала:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Работа с Сигналом"))

from pyqtgraph import PlotWidget



class TestGG():

    def __init__(self, photo_file, index_znach_type_photo_1_ariec, index_znach_type_photo_2_ariec, index_znach_type_photo_3_ariec):

        self.photo_file = photo_file
        self.index_znach_type_photo_1_ariec = index_znach_type_photo_1_ariec
        self.index_znach_type_photo_2_ariec = index_znach_type_photo_2_ariec
        self.index_znach_type_photo_3_ariec = index_znach_type_photo_3_ariec

        img1 = Image.open(self.photo_file)

        w = 650
        h = 100
        img1 = img1.resize((w, h))

        # img1.save('Data\\Image\\Temp\\new_img_for_ii.png')
        img1.save(r'D:\____Diplom____\Diploma_RubtsovN\Data\Image\Temp\new_img_for_ii.png')
        # img = cv2.imread('Data\\Image\\Temp\\new_img_for_ii.png')
        img = cv2.imread(r'D:\____Diplom____\Diploma_RubtsovN\Data\Image\Temp\new_img_for_ii.png')

        #############################################################
        im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imwrite('Data\\Image\\Temp\\im_gray_new_for_ii.png', im_gray)
        cv2.imwrite('D:\____Diplom____\Diploma_RubtsovN\Data\Image\Temp\im_gray_new_for_ii.png', im_gray)
        #############################################################

        # img_g = cv2.imread('Data\\Image\\Temp\\im_gray_new_for_ii.png')
        img_g = cv2.imread('D:\____Diplom____\Diploma_RubtsovN\Data\Image\Temp\im_gray_new_for_ii.png')

        mask = cv2.inRange(img_g, (0, 0, 0), ( self.index_znach_type_photo_1_ariec, self.index_znach_type_photo_2_ariec, self.index_znach_type_photo_3_ariec))
        mask = 255 - mask

        # save output
        # cv2.imwrite('Data\\Image\\Temp\\black_spots_mask_new_for_ii.png', mask)
        cv2.imwrite(r'D:\____Diplom____\Diploma_RubtsovN\Data\Image\Temp\black_spots_mask_new_for_ii.png', mask)

        # im = Image.open("Data\\Image\\Temp\\black_spots_mask_new_for_ii.png")
        im = Image.open("D:\\____Diplom____\\Diploma_RubtsovN\\Data\\Image\\Temp\\black_spots_mask_new_for_ii.png")

        # поворот изображения на 270
        angle = 270
        out = im.rotate(angle, expand=True)
        # out.save('Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')
        out.save('D:\\____Diplom____\\Diploma_RubtsovN\\Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')

        # img_1 = cv2.imread('Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')
        img_1 = cv2.imread('D:\\____Diplom____\\Diploma_RubtsovN\\Data\\Image\\Temp\\rotate-black_spots_mask_new_for_ii.png')

        arr = np.asarray(img_1)
        black_pixels = np.array(np.where(arr == 0))
        black_pixel_coordinates_2 = list(zip(black_pixels[0], black_pixels[1]))

        # print('длинна 2', len(black_pixel_coordinates_2))

        global res_g

        res_g = [max(g) for _, g in groupby(black_pixel_coordinates_2, lambda x: x[0])]

        #################################################################################

        ff = res_g[0]
        df = 0 - ff[1]
        d_res_g = [[y + df for y in x] for x in res_g]

        #################################################################################
        # self.widget_4.clear()
        # self.widget_4.setBackground('w')
        # pen1 = pg.mkPen(color=(255, 0, 0))
        # self.widget_4.plot(double(d_res_g), pen=pen1)

        #################################################################################
        #################################################################################

        arr_x_ariec = []
        arr_y_ariec = []

        for x_ariec, y_ariec in d_res_g:
            arr_y_ariec.append(y_ariec)

        for x_ariec, y_ariec in d_res_g:
            arr_x_ariec.append(x_ariec)

        y_ariec = numpy.array(arr_y_ariec)

        global peaks2_ariec

        peaks2_ariec, _ = find_peaks(y_ariec, prominence=30)  # BEST!

        # print(peaks2_ariec)
        global before_ariec
        global after_ariec

        before_ariec = 40
        after_ariec = 60

        R_ariec = np.sort(peaks2_ariec)
        # print(peaks2_ariec)

        length = len(y_ariec)

        global templates_ariec

        templates_ariec = []
        # templates_ = []
        # print(templates_ariec)

        # for j in R:
        for i in R_ariec:
            a = i - before_ariec
            if a < 0:
                continue
            b = i + after_ariec
            if b > length:
                break
            templates_ariec.append(y_ariec[a:b])

        templates_ariec = np.array(templates_ariec)

class II_in_classes_photo():

    def __init__(self, data_photo, data_target_photo):

        self.data_photo = data_photo
        self.data_target_photo = data_target_photo

        data = pd.read_csv(self.data_photo, sep=";")
        data_target = pd.read_csv(self.data_target_photo)

        X = data
        Y = data_target

        best = 0
        for j in range(2000):
            X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.3)
            linear = linear_model.Perceptron()

            linear.fit(X_train, Y_train.values.ravel())
            acc = linear.score(X_test, Y_test)
            # print("Точность: " + str(acc))

            # Сохранение высочайшей точности
            if acc > best:
                best = acc
                # with open("Data\\Pickle\\For II\\savedata_photo.pickle", "wb") as f:
                with open("D:\\____Diplom____\\Diploma_RubtsovN\\Data\\Pickle\\For II\\savedata_photo_test.pickle", "wb") as f:
                    pickle.dump(linear, f)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_II()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
