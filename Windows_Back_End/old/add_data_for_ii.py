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
from photo_v4 import Ui_Photo
from add_norm_znach import Ui_Add_Norm
from add_name_of_the_desease import Ui_Add_Disease

from hurst import compute_Hc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 481, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 481, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 160, 481, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 110, 481, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 20, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 20, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 50, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(523, 0, 31, 571))
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
        self.pushButton_5.setGeometry(QtCore.QRect(80, 50, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(80, 220, 381, 291))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = PlotWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(610, 220, 381, 291))
        self.widget_5.setObjectName("widget_5")
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
        self.pushButton_5.clicked.connect(self.test_gg)

        self.customer_names()

        ################################################################################################################
        ################################################################################################################

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

        ################################################################################################################
        ################################################################################################################

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

            # self.label.setText('EDF файл закружен!')
            # self.pushButton.hide()

            # self.lineEdit.setText('11250')
            # self.lineEdit_2.setText('13500')

        ################################################################################################################
        ################################################################################################################

    def test_gg(self):

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

        default_text = '3'

        for x in templates:
            self.widget_4.plot(x, pen=pen)
            # dict_sample = dict({'Диагноз': 0, 'Данные': x})
            with open("out.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(x)
            with open("output_1.csv", "a") as p:
                import csv
                pr = csv.writer(p, delimiter=";", lineterminator='\n')
                pr.writerow(default_text)
        # default_text = '1'
        # # Open the input_file in read mode and output_file in write mode
        # with open('out.csv', 'r') as read_obj, \
        #         open('output_1.csv', 'a') as write_obj:
        #     # Create a csv.reader object from the input file object
        #     csv_reader = csv.reader(read_obj)
        #     # Create a csv.writer object from the output file object
        #     csv_writer = csv.writer(write_obj, delimiter=";", lineterminator='\n')
        #     # Read each row of the input csv file as list
        #     for row in csv_reader:
        #         # Append the default text in the row / list
        #         row.append(default_text)
        #         # Add the updated row / list to the output file
        #         csv_writer.writerow(row)



        self.label.setText(str(len(templates)))

        # dict_sample = dict({'Диагноз': 1, 'Данные1': templates[0],'Данные2': templates[1]})
        # dict_sample = dict({'Диагноз': 0, 'Данные': templates, 'GG': 0})

        # pd.DataFrame(dict_sample).to_csv('out.csv', index=False)

        # with open(f"Data\\Pickle\\For II\\{self.ID}_ii.pickle", "wb") as f:
        #     pickle.dump(dict_sample, f)




        self.save_data()

        ################################################################################################################
        ################################################################################################################
    def save_data(self):
        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS data_for_ii(
                ID TEXT,
                data_dict TEXT
                )''')

        db.commit()
        data_dict = f"Data\\Pickle\\For II\\{self.ID}_ii.pickle"

        cursor.execute(f'SELECT data_dict FROM data_for_ii WHERE data_dict ="{data_dict}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO data_for_ii VALUES('
                           f'"{self.ID}",'
                           f'"{data_dict}")'
                           )
        db.commit()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)  # восклицательный
        msg.setText("Добавлено!")
        msg.setInformativeText('Результат добавлен в БД!')
        msg.setWindowTitle("Add")
        msg.exec_()

        ################################################################################################################
        ################################################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать Файл"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать обучение"))
        self.pushButton_3.setText(_translate("MainWindow", "Запуск"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить ВЕСА"))
        self.pushButton_5.setText(_translate("MainWindow", "ТЕСТ"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
