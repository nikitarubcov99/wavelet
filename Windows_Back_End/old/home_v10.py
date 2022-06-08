import pickle
import sqlite3

import numpy as np
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
from photo_v4 import Ui_Photo
from add_norm_znach import Ui_Add_Norm
from add_name_of_the_desease import Ui_Add_Disease

from hurst import compute_Hc


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
        self.label_14.setGeometry(QtCore.QRect(10, 360, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 771, 171))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 390, 771, 51))
        self.label_16.setObjectName("label_16")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(10, 240, 771, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        self.label_35.setGeometry(QtCore.QRect(10, 450, 781, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        self.label_36.setGeometry(QtCore.QRect(10, 480, 771, 51))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setGeometry(QtCore.QRect(10, 540, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
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
        self.tabWidget1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget1.setGeometry(QtCore.QRect(10, 510, 601, 281))
        self.tabWidget1.setObjectName("tabWidget1")
        self.Page1 = QtWidgets.QWidget()
        self.Page1.setObjectName("Page1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Page1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_28 = QtWidgets.QLabel(self.Page1)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.Page1)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.Page1)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 4, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.Page1)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 3, 1, 1, 4)
        self.label_24 = QtWidgets.QLabel(self.Page1)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.Page1)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.Page1)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 4, 1, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.Page1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.Page1)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.Page1)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 1, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.Page1)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 1, 1, 1, 2)
        self.label_25 = QtWidgets.QLabel(self.Page1)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 2, 1, 1, 4)
        self.label_22 = QtWidgets.QLabel(self.Page1)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.Page1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 4, 4, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.Page1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_4.addWidget(self.comboBox_4, 4, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.Page1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 0, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Page1)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(473, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget1.addTab(self.Page1, "")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(7, 490, 961, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 320, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(844, 20, 101, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(650, 20, 181, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.widget_10 = PlotWidget(self.centralwidget)
        self.widget_10.setGeometry(QtCore.QRect(620, 530, 331, 261))
        self.widget_10.setObjectName("widget_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 510, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1786, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
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
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ########################################################################################################################
        ########################################################################################################################

        self.pushButton.clicked.connect(self.open_edf)  # открыть EDF файл
        # self.pushButton_2.clicked.connect(self.open_photo)  # открыть изображение
        self.pushButton_3.clicked.connect(self.update_signal)  # считать ограничение сигнала
        # self.pushButton_4.clicked.connect(self.update_signal)  # кнопка обновить данные
        # self.pushButton_5.clicked.connect(self.save_db)  # сохранить в БД
        # self.pushButton_6.clicked.connect(self.report_data)  # Открыть отчет
        self.pushButton_7.clicked.connect(self.index_zn)  # Выбор индекса
        self.pushButton_8.clicked.connect(self.add_to_database_new_data)

        self.pushButton_5.clicked.connect(self.save_new_data_db)
        # self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        # self.action.setEnabled(False)
        # self.action_2.setEnabled(False)
        # self.action_5.setEnabled(False)
        # self.action_4.setEnabled(False)

        self.pushButton_4.hide()

        self.pushButton_3.setText('Добавить')

        self.action.triggered.connect(self.exit_app)  # вызов действия по вкладку в menu
        self.action_2.triggered.connect(self.View_DB)  # вызов действия по вкладку в menu
        self.action_3.triggered.connect(self.photo_data_window)  # вызов действия по вкладку в menu работа с изображениями
        self.action_4.triggered.connect(self.add_DB_data_window)  # вызов действия по вкладку в menu
        self.action_5.triggered.connect(self.add_DB_data_norm)  # вызов действия по вкладку в menu
        self.action_6.triggered.connect(self.add_db_name_of_the_disease)  # вызов действия по вкладку в menu

        self.lineEdit_3.setMaxLength(11)  # ограничения для снилса
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_3.setValidator(validator)  # валидация только на цифры

        self.pushButton_9.clicked.connect(self.norm_comboBox)
        self.pushButton_10.clicked.connect(self.disease_text)

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    def norm_comboBox(self):

        self.comboBox_3.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT ID FROM norm")
        sql = cursor.fetchall()
        self.norm_c = []
        for i in sql:
            self.norm_c.append(i[0])
        self.comboBox_3.addItems(self.norm_c)

    #################################################################################
    #################################################################################

    def disease_comboBox(self):

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
        self.comboBox_4.addItems(self.disease)

    #################################################################################
    #################################################################################

    def disease_text(self):

        dz_text = self.comboBox_4.currentText()

        self.label_34.setText(dz_text)

    #################################################################################
    #################################################################################

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

    """_________________Открытие окна "Просмотрт Базы Данных"_____________________"""

    def View_DB(self):
        self.view_db = QtWidgets.QMainWindow()
        self.ui = Ui_View_DB()
        self.ui.setupUi(self.view_db)
        self.view_db.show()

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    """_________________Открытие окна "Добавить в Базу данных"____________________"""

    def add_DB_data_norm(self):
        self.Add_DB_data_norm = QtWidgets.QMainWindow()
        self.ui = Ui_Add_Norm()
        self.ui.setupUi(self.Add_DB_data_norm)
        self.Add_DB_data_norm.show()

    """___________________________________________________________________________"""

    #################################################################################
    #################################################################################

    """_____________Открытие окна "Добавить Болезнь в Базу данных"________________"""

    def add_db_name_of_the_disease(self):
        self.Add_Disease = QtWidgets.QMainWindow()
        self.ui = Ui_Add_Disease()
        self.ui.setupUi(self.Add_Disease)
        self.Add_Disease.show()

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

    def open_edf(self):
        global edf_file

        edf_file, check = QFileDialog.getOpenFileName(None, "Выберите EDF файл",
                                                      'Data/EDF', "EDF Files (*.edf)")
        if check:
            self.label_4.setText(edf_file)
            # self.label.setText('EDF файл закружен!')
            # self.pushButton.hide()

            self.lineEdit.setText('11250')
            self.lineEdit_2.setText('13500')

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
        global Sd1
        global Sd2
        global Sd3
        global ScD1
        global ScD2
        global ScD3

        sig_1 = self.lineEdit.text()
        sig_2 = self.lineEdit_2.text()
        print(sig_1)
        print(sig_2)

        signals, signal_headers, header = highlevel.read_edf(edf_file)
        A = signals[int(index_znach)]

        print(A)

        # self.show()

        """Длинна сигнала"""
        A_length = len(A)
        print(A_length)

        A_ = A[int(sig_1):int(sig_2)]
        A__length = len(A_)
        print(A__length)

        import numpy as np
        from biosppy.signals import ecg

        # load raw ECG signal
        signal = A_

        # process it and plot
        # out = ecg.ecg(signal, sampling_rate=1000., show=True)
        #
        # print(out)

        # with open("Data\\file.txt", "w") as output:
        #     output.write(str(out))


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

        length = len(A_)

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
                templates.append(A_[a:b])
        templates = np.array(templates)

        self.widget_10.clear()
        self.widget_10.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        for x in templates:
            self.widget_10.plot(x, pen=pen)

        print("участки", templates)
        print(len(templates))


        # templates_ = list(templates)
        # templates__ = []
        # for i in templates_[0]:
        #     templates__.append(i)
        # print("участки", templates__)
        # # print("участки", templates)

        """Вывод R-пиков"""
        rpeaks_ = list(rpeaks)
        arr = []
        for i in rpeaks_[0]:
            arr.append(i)
        print("Обычные пики:", arr)

        """Рассчет частоты серцебиения"""
        hr = sampling_rate * (60. / np.diff(rpeaks))

        hr = list(hr)
        hr_ = []
        for i in hr[0]:
            hr_.append(i)
        print("серцебиение:", hr_)

        """Рассчет для частоты"""
        gg = signal_headers[int(index_znach)]

        try:
            SF = gg.get('sample_frequency')
            print(SF)

        except KeyError:
            print('Такого ключа нет')

        """Вывод входного сигнала"""
        self.widget_4.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_4.plot(A_, pen=pen)

        # self.widget_4.clear()  # очистить

        db1 = pywt.Wavelet('db4')

        """Рассчет частоты"""
        Fr = 0.7143
        # Исправить частоты, рассчитанные по формуле
        # Fr1 = 367.15
        Fr1 = Fr*SF/2
        Fr1_ = (np.around(Fr1, 2))

        Fr2 = Fr*Fr1/2
        Fr2_ = (np.around(Fr2, 2))

        Fr3 = Fr*Fr2/2
        Fr3_ = (np.around(Fr3, 2))

        # (cA2, cD2), (cA1, cD1) = pywt.swt(A, db1,  level=2)

        cD3, cD2, cD1 = pywt.wavedec(A_, db1, level=2)
        # cA4 = pywt.wavedec(A_, db1, level=2)

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

        H, c, data = compute_Hc(A_, kind='random_walk')

        print("H={:.4f}, c={:.4f}".format(H, c))
        global H1
        global c1
        H1 = (np.around(H, 4))
        c1 = (np.around(c, 4))

        self.label_36.setText(
            "<table width='100%'>" +
            "<tr><th>Показатель Херста:</th><th>Фрактальная размерность:</th></tr>" +
            f"<tr><td align='center'>{H1}</td><td align='center'>{c1}</td></td>" +
            "</table>"

        )
        self.label_36.setStyleSheet("""
                                            QLabel {
                                                font-size: 15px;
                                                border-radius: 25px;
                                                color: #000000; 
                                            }
                                            """)
        # _____________________________________________________Вывод Графиков_________________________________________

        self.widget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget.plot(cD1, pen=pen)

        self.widget_2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_2.plot(cD2, pen=pen)

        self.widget_3.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_3.plot(cD3, pen=pen)

        self.label_10.setText(f'Восстановленный сигнал по детализирующим коэфициентам на частоте: {Fr1_} Hz')

        self.widget_5.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_5.plot(DDDcD1, pen=pen)

        self.label_11.setText(f'Восстановленный сигнал по детализирующим коэфициентам на частоте: {Fr2_} Hz')

        self.widget_6.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_6.plot(DDDcD2, pen=pen)

        self.label_12.setText(f'Восстановленный сигнал по детализирующим коэфициентам на частоте: {Fr3_} Hz')

        self.widget_7.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_7.plot(DDDcD3, pen=pen)

        self.widget_8.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_8.plot(double(PS1), pen=pen)

        self.widget_9.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_9.plot(double(PS2), pen=pen)

        self.widget_18.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.widget_18.plot(double(PS3), pen=pen)

        self.otk_norm()
    #################################################################################
    #################################################################################

    def otk_norm(self):

        id_norm = self.comboBox_3.currentText()

        print(id_norm)

        # id_norm = '26f12a91-2ac6-40e4-8331-eba04f3ecea9'

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS norm(
                ID TEXT PRIMARY KEY,
                cD1_n TEXT,
                cD2_n TEXT,
                cD3_n TEXT,
                ScD1_n TEXT,
                ScD2_n TEXT,
                ScD3_n TEXT,
                H_n TEXT,
                c_n TEXT
                )''')

        try:
            cursor.execute(f"""SELECT ID FROM norm WHERE ID = '{id_norm}'""")
            if cursor.fetchone() is None:
                print('ERROr_Add_ndvi_db')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('ID не найдено. БД не подключено!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                cursor.execute(f'SELECT ID FROM norm WHERE ID = "{id_norm}"')
                ID = cursor.fetchall()
                id_ = []
                for i in ID:
                    id_.append(i[0])
                ID__ = (''.join(map(str, id_)))

                cursor.execute(f'SELECT cD1_n FROM norm WHERE ID = "{id_norm}"')
                cD1_n = cursor.fetchall()
                cD1_n_ = []
                for i in cD1_n:
                    cD1_n_.append(i[0])
                cD1_n__ = (''.join(map(str, cD1_n_)))

                cursor.execute(f'SELECT cD2_n FROM norm WHERE ID = "{id_norm}"')
                cD2_n = cursor.fetchall()
                cD2_n_ = []
                for i in cD2_n:
                    cD2_n_.append(i[0])
                cD2_n__ = (''.join(map(str, cD2_n_)))

                cursor.execute(f'SELECT cD3_n FROM norm WHERE ID = "{id_norm}"')
                cD3_n = cursor.fetchall()
                cD3_n_ = []
                for i in cD3_n:
                    cD3_n_.append(i[0])
                cD3_n__ = (''.join(map(str, cD3_n_)))

                cursor.execute(f'SELECT ScD1_n FROM norm WHERE ID = "{id_norm}"')
                ScD1_n = cursor.fetchall()
                ScD1_n_ = []
                for i in ScD1_n:
                    ScD1_n_.append(i[0])
                ScD1_n__ = (''.join(map(str, ScD1_n_)))

                cursor.execute(f'SELECT ScD2_n FROM norm WHERE ID = "{id_norm}"')
                ScD2_n = cursor.fetchall()
                ScD2_n_ = []
                for i in ScD2_n:
                    ScD2_n_.append(i[0])
                ScD2_n__ = (''.join(map(str, ScD2_n_)))

                cursor.execute(f'SELECT ScD3_n FROM norm WHERE ID = "{id_norm}"')
                ScD3_n = cursor.fetchall()
                ScD3_n_ = []
                for i in ScD3_n:
                    ScD3_n_.append(i[0])
                ScD3_n__ = (''.join(map(str, ScD3_n_)))

                cursor.execute(f'SELECT H_n FROM norm WHERE ID = "{id_norm}"')
                H_n = cursor.fetchall()
                H_n_ = []
                for i in H_n:
                    H_n_.append(i[0])
                H_n__ = (''.join(map(str, H_n_)))

                cursor.execute(f'SELECT c_n FROM norm WHERE ID = "{id_norm}"')
                c_n = cursor.fetchall()
                c_n_ = []
                for i in c_n:
                    c_n_.append(i[0])
                c_n__ = (''.join(map(str, c_n_)))

                print(H1)
                print(H_n__)

                # otk_Sd1 = double(cD1_n__) - double(Sd1)

                otk_Sd1 = ((Sd1 - float(cD1_n__)) / float(cD1_n__)) * 100
                otk_Sd2 = ((Sd2 - float(cD2_n__)) / float(cD2_n__)) * 100
                otk_Sd3 = ((Sd3 - float(cD3_n__)) / float(cD3_n__)) * 100
                otk_Sd1_ = (np.around(otk_Sd1, 2))
                otk_Sd2_ = (np.around(otk_Sd2, 2))
                otk_Sd3_ = (np.around(otk_Sd3, 2))

                otk_ScD1 = ((ScD1 - float(ScD1_n__)) / float(ScD1_n__)) * 100
                otk_ScD2 = ((ScD2 - float(ScD2_n__)) / float(ScD2_n__)) * 100
                otk_ScD3 = ((ScD3 - float(ScD3_n__)) / float(ScD3_n__)) * 100
                otk_ScD1_ = (np.around(otk_ScD1, 2))
                otk_ScD2_ = (np.around(otk_ScD2, 2))
                otk_ScD3_ = (np.around(otk_ScD3, 2))

                otk_H = ((H1 - float(H_n__)) / float(H_n__)) * 100
                otk_c = ((c1 - float(c_n__)) / float(c_n__)) * 100
                otk_H_ = (np.around(otk_H, 2))
                otk_c_ = (np.around(otk_c, 2))

                sum_otk1 = (otk_Sd1_ + otk_Sd2_ + otk_Sd3_)/3
                sum_otk2 = (otk_ScD1_ + otk_ScD2_ + otk_ScD3_)/3
                sum_otk1_ = (np.around(sum_otk1, 4))
                sum_otk2_ = (np.around(sum_otk2, 4))


                # self.label_29.setText(
                #     "<table width='100%'>" +
                #     "<tr><th>Среднее сумарное отклонение от нормы cD:</th><th>Среднее сумарное отклонение от нормы ScD:</th></tr>" +
                #     f"<tr><td align='center'>{sum_otk1_}%</td><td align='center'>{sum_otk2_}%</td></td>" +
                #     "</table>"
                #
                # )
                self.label_29.setText(
                    "<table width='100%'>" +
                    "<tr><th>Отклонение cD1:</th><th>Отклонение cD2:</th><th>Отклонение cD3:</th></tr>" +
                    f"<tr><td align='center'>{otk_Sd1_}%</td><td align='center'>{otk_Sd2_}%</td><td align='center'>{otk_Sd3_}%</td></td>" +
                    "</table>"

                    "<table width='100%'>" +
                    "<tr><th>Отклонение ScD1:</th><th>Отклонение ScD2:</th><th>Отклонение ScD3:</th></tr>" +
                    f"<tr><td align='center'>{otk_ScD1_}%</td><td align='center'>{otk_ScD2_}%</td><td align='center'>{otk_ScD3_}%</td></td>" +
                    "</table>"

                )
                self.label_29.setStyleSheet("""
                                                            QLabel {
                                                                font-size: 12px;
                                                                border-radius: 25px;
                                                                color: #000000; 
                                                            }
                                                            """)

                self.label_37.setText(
                    "<table width='100%'>" +
                    "<tr><th>Отклонение от нормы H:</th><th>Отклонение от нормы c:</th></tr>" +
                    f"<tr><td align='center'>{otk_H_}%</td><td align='center'>{otk_c_}%</td></td>" +
                    "</table>"

                )
                self.label_37.setStyleSheet("""
                                                                            QLabel {
                                                                                font-size: 12px;
                                                                                border-radius: 25px;
                                                                                color: #000000; 
                                                                            }
                                                                            """)

                print(f'ПОДКЛЮЧЕНИЕ УСПЕШНО')
                db.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            print("таблица не существует gg")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Вы ввели ID, без выбора Таблицы БД!')
            msg.setWindowTitle("Error")
            msg.exec_()

    #################################################################################
    #################################################################################

    """_________________________Вывод данных о пользователе_______________________"""

    def add_to_database_new_data(self):
        global xxx

        if self.lineEdit_3.text() == '':
            xxx = self.comboBox_2.currentText()
            self.lineEdit_3.setText('')

        else:
            xxx = self.lineEdit_3.text()
            self.lineEdit_3.setText('')

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
                print('ERROr_Add_ndvi_db')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('ID не найдено. БД не подключено!')
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
                self.label_34.setText(f'{diagnoz__}')

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
        self.disease_comboBox()

    ########################################################################################################################
    ########################################################################################################################

    def save_new_data_db(self):

        dz = self.label_34.text()
        # dz = self.comboBox_4.currentText()
        with open(f"Data\\Pickle\\Signal\\{xxx}_s.pickle", "wb") as f:
            pickle.dump(templates, f)

        DATA_JJ = f"Data\\Pickle\\Signal\\{xxx}_s.pickle"

        try:
            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()
            if xxx == '':

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('Вы не ввели СНИЛС')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                cursor.execute(f"""UPDATE patient SET 
                                        diagnoz = '{dz}', 
                                        cD1_ = '{Sd1}', 
                                        cD2_ = '{Sd2}', 
                                        cD3_ = '{Sd3}', 
                                        ScD1_ = '{ScD1}',
                                        ScD2_ = '{ScD2}', 
                                        ScD3_ = '{ScD3}', 
                                        H_ = '{H1}',
                                        H_ = '{c1}',
                                        Array_S = '{DATA_JJ}' 
                                        WHERE snils = '{xxx}'""")
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
        self.label_35.setText(_translate("MainWindow", "Стохастические характеристики компонент кардиосигнала:"))
        self.label_36.setText(_translate("MainWindow", "-"))
        self.label_37.setText(_translate("MainWindow", "Отклонения от нормы: -"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Статическое среднее и Энтропия"))
        self.label_17.setText(_translate("MainWindow", "Энергетический спектр PS1"))
        self.label_18.setText(_translate("MainWindow", "Энергетический спектр PS2"))
        self.label_31.setText(_translate("MainWindow", "Энергетический спектр PS3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Энергетический спектр"))
        self.label_32.setText(_translate("MainWindow", "Входной сигнал"))
        self.pushButton_5.setText(_translate("MainWindow", "Сохранить в БД"))
        self.pushButton_6.setText(_translate("MainWindow", "Открыть отчет"))
        self.label_28.setText(_translate("MainWindow", "Адрес:"))
        self.label_19.setText(_translate("MainWindow", "Пациент № "))
        self.label_33.setText(_translate("MainWindow", "Диагноз:"))
        self.label_27.setText(_translate("MainWindow", "-"))
        self.label_24.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "-"))
        self.label_34.setText(_translate("MainWindow", "-"))
        self.label_20.setText(_translate("MainWindow", "ФИО: "))
        self.label_21.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_23.setText(_translate("MainWindow", "-"))
        self.label_25.setText(_translate("MainWindow", "-"))
        self.label_22.setText(_translate("MainWindow", "Снилс:"))
        self.pushButton_10.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_8.setText(_translate("MainWindow", "Выбрать"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "Выбрать НОРМу"))
        self.label_5.setText(_translate("MainWindow", "PQRST:"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "База Данных"))
        self.menu_3.setTitle(_translate("MainWindow", "Дополнения"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Открыть Базу данных"))
        self.action_4.setText(_translate("MainWindow", "Добавить \"Пациента\" в Базу Данных"))
        self.action_3.setText(_translate("MainWindow", "Работа с изображениями"))
        self.action_5.setText(_translate("MainWindow", "Добавить значение \"Норм\" в Базу Данных"))
        self.action_6.setText(_translate("MainWindow", "Добавить название \"Болезни\" в Базу данных"))
        self.action_7.setText(_translate("MainWindow", "Работа с ИИ"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
