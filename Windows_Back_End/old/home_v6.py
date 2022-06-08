import sqlite3
from os import sep
import datetime

import numpy
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QApplication
from matplotlib import pyplot as plt
from numpy import std, conj, subtract, var, polyfit, log10
from numpy import double

import pywt
from pyedflib import highlevel
from scipy.fft import fft
from PyQt5 import QtCore, QtGui, QtWidgets

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib
import pyqtgraph as pg


from add_patient_v2 import Ui_Add_DB_Patient
from photo_v1 import Ui_Photo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1786, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(960, 10, 20, 881))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 170, 81, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(980, 10, 801, 791))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = PlotWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 40, 779, 171))
        self.widget.setObjectName("widget")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget_2 = PlotWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(10, 250, 779, 171))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = PlotWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(10, 460, 779, 171))
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 430, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_5 = PlotWidget(self.tab_2)
        self.widget_5.setGeometry(QtCore.QRect(10, 40, 779, 171))
        self.widget_5.setObjectName("widget_5")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.widget_6 = PlotWidget(self.tab_2)
        self.widget_6.setGeometry(QtCore.QRect(10, 250, 779, 171))
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = PlotWidget(self.tab_2)
        self.widget_7.setGeometry(QtCore.QRect(10, 460, 779, 171))
        self.widget_7.setObjectName("widget_7")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(10, 430, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(10, 390, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 771, 271))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 420, 771, 271))
        self.label_16.setObjectName("label_16")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(10, 340, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(10, 700, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_8 = PlotWidget(self.tab_4)
        self.widget_8.setGeometry(QtCore.QRect(10, 40, 779, 171))
        self.widget_8.setObjectName("widget_8")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.widget_9 = PlotWidget(self.tab_4)
        self.widget_9.setGeometry(QtCore.QRect(10, 250, 779, 171))
        self.widget_9.setObjectName("widget_9")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(10, 220, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_31 = QtWidgets.QLabel(self.tab_4)
        self.label_31.setGeometry(QtCore.QRect(10, 430, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.widget_18 = PlotWidget(self.tab_4)
        self.widget_18.setGeometry(QtCore.QRect(10, 460, 779, 171))
        self.widget_18.setObjectName("widget_18")
        self.tabWidget.addTab(self.tab_4, "")
        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(10, 260, 781, 229))
        self.widget_4.setObjectName("widget_4")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(10, 230, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 260, 141, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 290, 141, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(500, 10, 431, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 510, 81, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget1.setGeometry(QtCore.QRect(10, 540, 461, 221))
        self.tabWidget1.setObjectName("tabWidget1")
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
        self.tabWidget1.addTab(self.Page1, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 510, 341, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1786, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ########################################################################################################################
        ########################################################################################################################

        self.pushButton.clicked.connect(self.open_edf)  # открыть EDF файл
        # self.pushButton_2.clicked.connect(self.open_photo)  # открыть изображение
        self.pushButton_3.clicked.connect(self.update_signal)  # считать ограничение сигнала
        # self.pushButton_4.clicked.connect(self.update_signal)  # кнопка обновить данные
        self.pushButton_5.clicked.connect(self.save_db)  # сохранить в БД
        self.pushButton_6.clicked.connect(self.report_data)  # Открыть отчет
        self.pushButton_7.clicked.connect(self.index_zn)  # Выбор индекса
        self.pushButton_8.clicked.connect(self.add_to_database_new_data)

        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        # self.action.setEnabled(False)
        self.action_2.setEnabled(False)
        # self.action_4.setEnabled(False)

        self.pushButton_4.hide()

        self.pushButton_3.setText('Добавить')

        self.action.triggered.connect(self.exit_app)  # вызов действия по вкладку в menu
        self.action_4.triggered.connect(self.add_DB_data_window)  # вызов действия по вкладку в menu
        self.pushButton_2.clicked.connect(self.photo_data_window)  # работа с изображениями


    """___________________________________________________________________________"""

    #################################################################################
    def customer_names(self):

        self.comboBox_2.clear()

        db = sqlite3.connect('/DataBase/database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT ID FROM patient")
        sql = cursor.fetchall()
        self.names = []
        for i in sql:
            self.names.append(i[0])
        self.comboBox_2.addItems(self.names)

    #################################################################################
    #################################################################################

    """____________________________Выход из программы_____________________________"""

    def exit_app(self):
        QApplication.quit()

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    """_________________Открытие окна "Добавить в Базу данных"____________________"""

    def add_DB_data_window(self):
        self.Add_DB_data = QtWidgets.QMainWindow()
        self.ui = Ui_Add_DB_Patient()
        self.ui.setupUi(self.Add_DB_data)
        self.Add_DB_data.show()

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    """_________________Открытие окна "Работа с изображениями"____________________"""

    def photo_data_window(self):
        self.photo_data = QtWidgets.QMainWindow()
        self.ui = Ui_Photo()
        self.ui.setupUi(self.photo_data)
        self.photo_data.show()

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    def index_zn(self):

        x = self.comboBox.currentText()
        global index_znach

        if x == 'V1':
            index_znach = '0'

        elif x == 'V2':
            index_znach = '1'

        elif x == 'V3':
            index_znach = '2'

        elif x == 'VR':
            index_znach = '3'

        elif x == 'VL':
            index_znach = '4'

        elif x == 'VF':
            index_znach = '5'

        else:
            print('Error_index_name')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не выбран индекс!')
            msg.setWindowTitle("Error")
            msg.exec_()

    """___________________________________________________________________________"""

    def save_db(self):
        pass

    def report_data(self):
        pass

    def open_edf(self):
        global edf_file

        edf_file, check = QFileDialog.getOpenFileName(None, "Выберите EDF файл",
                                                      'Data/EDF', "EDF Files (*.edf)")
        if check:
            self.label_4.setText(edf_file)
            self.label.setText('EDF файл закружен!')
            self.pushButton_2.setEnabled(False)
            self.pushButton.hide()

            self.lineEdit.setText('11250')
            self.lineEdit_2.setText('13500')

    # def open_photo(self):
    #     global photo_file
    #
    #     photo_file, check = QFileDialog.getOpenFileName(None, "Выберите Изображение",
    #                                                     'Data/Image', "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )")
    #     if check:
    #         self.label_6.setText(photo_file)
    #         self.label_5.setText('Изображение закружено!')
    #         self.pushButton.setEnabled(False)
    #         self.pushButton_2.hide()
    #
    #         # self.lineEdit.setText('11250')
    #         # self.lineEdit_2.setText('13500')

    def update_signal(self):

        global sig_1
        global sig_2

        self.widget.clear()
        self.widget_2.clear()
        self.widget_3.clear()

        self.widget_4.clear()

        self.widget_5.clear()
        self.widget_6.clear()
        self.widget_7.clear()

        self.widget_8.clear()
        self.widget_9.clear()
        self.widget_18.clear()

        sig_1 = self.lineEdit.text()
        sig_2 = self.lineEdit_2.text()

        self.long_signal()

    def long_signal(self):

        self.pushButton_3.setText('Обновить')

        global sig_1
        global sig_2
        global A

        sig_1 = self.lineEdit.text()
        sig_2 = self.lineEdit_2.text()
        print(sig_1)
        print(sig_2)

        signals, signal_headers, header = highlevel.read_edf(edf_file)
        A = signals[int(index_znach)]

        # self.show()

        """Длинна сигнала"""
        A_length = len(A)
        print(A_length)

        A_ = A[int(sig_1):int(sig_2)]
        A__length = len(A_)
        print(A__length)

        """Вывод входного сигнала"""
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_4.plot(A_, pen=pen)

        # self.widget_4.clear()  # очистить

        # filename = 'Norm.xlsx'
        # A = pd.read_excel(filename)
        # A.head()
        db1 = pywt.Wavelet('db4')
        Fr = 0.7143
        # Исправить частоты, рассчитанные по формуле
        Fr1 = 367.15
        Fr2 = 183.57
        Fr3 = 91.79
        # (cA2, cD2), (cA1, cD1) = pywt.swt(A, db1,  level=2)

        cD3, cD2, cD1 = pywt.wavedec(A_, db1, level=2)
        cA4 = pywt.wavedec(A_, db1, level=2)

        DDDcD1 = pywt.upcoef('d', cD1, wavelet=db1, level=2)
        DDDcD2 = pywt.upcoef('d', cD2, wavelet=db1, level=2)
        DDDcD3 = pywt.upcoef('d', cD3, wavelet=db1, level=2)

        print('################################################################################')
        print('"""Статическое среднее"""')

        Sd1 = std(cD1)
        Sd1 = (np.around(Sd1, 4))

        Sd2 = std(cD2)
        Sd2 = (np.around(Sd2, 4))

        Sd3 = std(cD3)
        Sd3 = (np.around(Sd3, 4))

        ScD1 = std(DDDcD1)
        ScD1 = (np.around(ScD1, 4))

        ScD2 = std(DDDcD2)
        ScD2 = (np.around(ScD2, 4))

        ScD3 = std(DDDcD3)
        ScD3 = (np.around(ScD3, 4))

        print(f'Вейвлет-коэффициент cD1: {Sd1}')
        print(f'Вейвлет-коэффициент cD2: {Sd2}')
        print(f'Вейвлет-коэффициент cD3: {Sd3}')
        print(f'Компонент сигнала ScD1: {ScD1}')
        print(f'Компонент сигнала ScD2: {ScD2}')
        print(f'Компонент сигнала ScD3: {ScD3}')

        self.label_15.setText(
            "<table width='100%'>" +
            "<tr><th>Вейвлет-коэффициент cD1:</th><th>Вейвлет-коэффициент cD2:</th><th>Вейвлет-коэффициент cD3:</th></tr>" +
            f"<tr><td align='center'>{Sd1}</td><td align='center'>{Sd2}</td><td align='center'>{Sd3}</td></td>" +
            "</table>"

            "<table width='100%'>" +
            "<tr><th></th></tr>" +
            f"<tr><td align='center'></td></td>" +
            f"<tr><td align='center'></td></td>" +
            f"<tr><td align='center'></td></td>" +
            "</table>"

            "<table width='100%'>" +
            "<tr><th>Компонент сигнала ScD1:</th><th>Компонент сигнала ScD2:</th><th>Компонент сигнала ScD3:</th></tr>" +
            f"<tr><td align='center'>{ScD1}</td><td align='center'>{ScD2}</td><td align='center'>{ScD3}</td></td>" +
            "</table>"
        )
        self.label_15.setStyleSheet("""
                            QLabel {
                                font-size: 15px;
                                border-radius: 25px;
                                color: #000000; 
                            }
                            """)

        print('################################################################################')

        print('"""Энтропия Шенона"""')

        data = pywt.wavedec(A_, db1)
        S = 0
        Etot = 0

        global result
        result = []
        for d in data:
            E = d ** 2
            P = E / np.sum(E)
            S = -np.sum(P * np.log(P))
            Etot = np.sum(E)
            S1 = (np.around(S, 4))

            print(f"К-т: {S1}")
            result.append(S1)
            # print(f"Энтропия Шенона: {S}")
            # print(f"Энергия: {Etot}")
            # E1 = Etot / S  # отношение энергии вейвлета к энтропии Шеннона
            #
            # print(f"Отношение энергии вейвлета к энтропии Шеннона: {E1}")

        ss = (', \n'.join(map(str, result)))
        # numpy.savetxt('ssssd111', result)

        self.label_16.setText(
            "<table width='100%'>" +
            "<tr><th>Энтропия:</th></tr>" +
            f'<tr><td align="center">{ss}</td></td>' +
            "</table>"
        )
        self.label_16.setStyleSheet("""
                                           QLabel {
                                               font-size: 15px;
                                               border-radius: 25px;
                                               color: #000000; 
                                           }
                                           """)
        print('################################################################################')

        print('"""Енергитический спектр"""')

        Len_s_1 = len(DDDcD1)
        YS1 = fft(DDDcD1)
        PS1 = YS1 * conj(YS1) / Len_s_1

        print(PS1)

        Len_s_2 = len(DDDcD2)
        YS2 = fft(DDDcD2)
        PS2 = YS2 * conj(YS2) / Len_s_2

        Len_s_3 = len(DDDcD3)
        YS3 = fft(DDDcD3)
        PS3 = YS3 * conj(YS3) / Len_s_3
        print('################################################################################')

        print('"""Покатели Херста"""')

        # # _____________________________________________________Вывод Графиков____________________________________________________
        #
        # plt.figure(figsize=(17, 5))
        # plt.title("Входной сигнал")
        # # plt.plot(A)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.plot(A_)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()
        #
        # plt.figure(figsize=(17, 5))
        # plt.title("Разложение сигнала до уровня 1")
        # plt.plot(cD1)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()
        self.widget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget.plot(cD1, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title("Разложение сигнала до уровня 2")
        # plt.plot(cD2)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()
        self.widget_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_2.plot(cD2, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title("Разложение сигнала до уровня 3")
        # plt.plot(cD3)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()
        self.widget_3.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_3.plot(cD3, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title(f"Компоненты сигнала на частоте {Fr1} Hz")
        # plt.plot(DDDcD1)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        self.widget_5.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_5.plot(DDDcD1, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title(f"Компоненты сигнала на частоте {Fr2} Hz")
        # plt.plot(DDDcD2)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        self.widget_6.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_6.plot(DDDcD2, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title(f"Компоненты сигнала на частоте {Fr3} Hz")
        # plt.plot(DDDcD3)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        self.widget_7.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_7.plot(DDDcD3, pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title("Энергетический спектр PS1")
        # plt.plot(PS1)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        self.widget_8.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_8.plot(double(PS1), pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title("Энергетический спектр PS2")
        # plt.plot(PS2)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        # self.widget_9.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))

        self.widget_9.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_9.plot(double(PS2), pen=pen)

        # plt.figure(figsize=(17, 5))
        # plt.title("Энергетический спектр PS3")
        # plt.plot(PS3)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        # self.widget_10.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        self.widget_18.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_18.plot(double(PS3), pen=pen)

        # self.add_to_database_new_data()

    #################################################################################
    #################################################################################

    """______________________Добавление в Базу Данных new data____________________"""

    def add_to_database_new_data(self):

        x = self.comboBox_2.currentText()

        db = sqlite3.connect('/DataBase/database.db')
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS patient(
                        ID TEXT PRIMARY KEY,
                        f_ TEXT,
                        i_ TEXT,
                        o_ TEXT,
                        address_ TEXT,
                        data_b_ TEXT,
                        diagnoz TEXT,
                        cD1_ TEXT,
                        cD2_ TEXT,
                        cD3_ TEXT
                        )''')
        try:
            cursor.execute(f'SELECT ID FROM patient WHERE ID ="{x}"')
            if cursor.fetchone() is None:
                print('ERROr_Add_ndvi_db')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('ID не найдено. БД не подключено!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                cursor.execute(f'SELECT ID FROM patient WHERE ID ="{x}"')
                ID = cursor.fetchall()
                id_ = []
                for i in ID:
                    id_.append(i[0])
                id__ = (''.join(map(str, id_)))
                self.label_26.setText(f'{id__}')


                # ID__ = (' '.join(map(str, ID)))
                # self.label_26.setText(f'{ID__}')

                cursor.execute(f'SELECT fio_ FROM patient WHERE ID ="{x}"')
                # fio = cursor.fetchall()
                # fio__ = []
                # for i in fio:
                #     fio__.append(i[1])
                # self.label_23.setText(f'{fio__}')

                fio = cursor.fetchall()
                fio_ = []
                for i in fio:
                    fio_.append(i[0])
                fio__ = (''.join(map(str, fio_)))
                self.label_23.setText(f'{fio__}')


                cursor.execute(f'SELECT address_ FROM patient WHERE ID ="{x}"')
                address = cursor.fetchall()
                address__ = []
                for i in address:
                    address__.append(i[0])
                address___ = (''.join(map(str, address__)))
                self.label_25.setText(f'{address___}')


                cursor.execute(f'SELECT data_b_ FROM patient WHERE ID ="{x}"')
                data_b_ = cursor.fetchall()
                data_b__ = []
                for i in data_b_:
                    data_b__.append(i[0])
                data_b___ = (''.join(map(str, data_b__)))
                self.label_24.setText(f'{data_b___}')
                self.label_21.setText('Дата рождения:')
                cursor.execute(f'SELECT diagnoz FROM patient WHERE ID ="{x}"')
                diagnoz = cursor.fetchall()
                diagnoz_ = []
                for i in diagnoz:
                    diagnoz_.append(i[0])
                diagnoz__ = (''.join(map(str, diagnoz_)))
                self.label_27.setText(f'{diagnoz__}')


        # self.tableWidget.setRowCount(len(result))
        # self.tableWidget.setColumnCount(len(result[0]))
        # for i, elem in enumerate(result):
        #     for j, val in enumerate(elem):
        #         self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

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

    ########################################################################################################################
    ########################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Открыть EDF файл"))
        self.comboBox.setItemText(0, _translate("MainWindow", "V1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "V2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "V3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "VR"))
        self.comboBox.setItemText(4, _translate("MainWindow", "VL"))
        self.comboBox.setItemText(5, _translate("MainWindow", "VF"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_7.setText(_translate("MainWindow", "Выбрать"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.label_2.setText(_translate("MainWindow", "Длинна сигнала"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить"))
        self.label_7.setText(_translate("MainWindow", "Разложение сигнала до уровня 1"))
        self.label_8.setText(_translate("MainWindow", "Разложение сигнала до уровня 2"))
        self.label_9.setText(_translate("MainWindow", "Разложение сигнала до уровня 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Разложение сигнала до 3 уровня"))
        self.label_10.setText(_translate("MainWindow", "Восстановленный сигнал по детализирующим коэфициентам на частоте:"))
        self.label_11.setText(_translate("MainWindow", "Восстановленный сигнал по детализирующим коэфициентам на частоте:"))
        self.label_12.setText(_translate("MainWindow", "Восстановленный сигнал по детализирующим коэфициентам на частоте:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Восстановленный сигнал по ДК"))
        self.label_13.setText(_translate("MainWindow", "Статическое среднее:"))
        self.label_14.setText(_translate("MainWindow", "Энтропия:"))
        self.label_15.setText(_translate("MainWindow", "-"))
        self.label_16.setText(_translate("MainWindow", "-"))
        self.label_29.setText(_translate("MainWindow", "Отклонение от нормы: -"))
        self.label_30.setText(_translate("MainWindow", "Отклонения от нормы: -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Статическое среднее и Энтропия"))
        self.label_17.setText(_translate("MainWindow", "Энергетический спектр PS1"))
        self.label_18.setText(_translate("MainWindow", "Энергетический спектр PS2"))
        self.label_31.setText(_translate("MainWindow", "Энергетический спектр PS3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Энергетический спектр"))
        self.label_32.setText(_translate("MainWindow", "Входной сигнал"))
        self.pushButton_5.setText(_translate("MainWindow", "Сохранить в БД"))
        self.pushButton_6.setText(_translate("MainWindow", "Открыть отчет"))
        self.label_5.setText(_translate("MainWindow", "Загрузить изображение"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать"))
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
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "База Данных"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Открыть Базу данных"))
        self.action_4.setText(_translate("MainWindow", "Добавить в Базу Данных"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
