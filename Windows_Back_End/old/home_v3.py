import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QWidget, QVBoxLayout
from numpy import std, conj, subtract, var, polyfit, log10
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1786, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(960, 160, 20, 731))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 170, 771, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = PlotWidget(self.layoutWidget1)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 130, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(991, 99, 779, 83))
        self.widget_2.setObjectName("widget_2")
        self.widget_8 = PlotWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(991, 541, 779, 82))
        self.widget_8.setObjectName("widget_8")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(991, 11, 779, 82))
        self.widget.setObjectName("widget")
        self.widget_5 = PlotWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(991, 276, 779, 82))
        self.widget_5.setObjectName("widget_5")
        self.widget_3 = PlotWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(991, 188, 779, 82))
        self.widget_3.setObjectName("widget_3")
        self.widget_7 = PlotWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(991, 453, 779, 82))
        self.widget_7.setObjectName("widget_7")
        self.widget_9 = PlotWidget(self.centralwidget)
        self.widget_9.setGeometry(QtCore.QRect(991, 629, 779, 83))
        self.widget_9.setObjectName("widget_9")
        self.widget_6 = PlotWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(991, 364, 779, 83))
        self.widget_6.setObjectName("widget_6")
        self.widget_10 = PlotWidget(self.centralwidget)
        self.widget_10.setGeometry(QtCore.QRect(991, 718, 779, 82))
        self.widget_10.setObjectName("widget_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1786, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ########################################################################################################################
        ########################################################################################################################

        self.pushButton.clicked.connect(self.open_edf)  # открыть EDF файл
        self.pushButton_2.clicked.connect(self.open_photo)  # открыть изображение
        self.pushButton_3.clicked.connect(self.long_signal)  # считать ограничение сигнала
        self.pushButton_4.clicked.connect(self.update_signal)

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

    def open_photo(self):
        global photo_file

        photo_file, check = QFileDialog.getOpenFileName(None, "Выберите Изображение",
                                                        'Data/Image', "Image Files (*.png; *.jpg;*.jpeg;*.bmp;*.svg; )")
        if check:
            self.label_6.setText(photo_file)
            self.label_5.setText('Изображение закружено!')
            self.pushButton.setEnabled(False)
            self.pushButton_2.hide()

            # self.lineEdit.setText('11250')
            # self.lineEdit_2.setText('13500')

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
        self.widget_10.clear()
        # self.widget.clear()
        # self.widget_2.clear()
        # self.widget_3.clear()
        sig_1 = self.lineEdit.text()
        sig_2 = self.lineEdit_2.text()

        self.long_signal()

    def long_signal(self):

        global sig_1
        global sig_2
        global A

        sig_1 = self.lineEdit.text()
        sig_2 = self.lineEdit_2.text()
        print(sig_1)
        print(sig_2)

        signals, signal_headers, header = highlevel.read_edf(edf_file)
        A = signals[1]

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
        Sd2 = std(cD2)
        Sd3 = std(cD3)
        ScD1 = std(DDDcD1)
        ScD2 = std(DDDcD2)
        ScD3 = std(DDDcD3)
        print(f'Вейвлет-коэффициент cD1: {Sd1}')
        print(f'Вейвлет-коэффициент cD2: {Sd2}')
        print(f'Вейвлет-коэффициент cD3: {Sd3}')
        print(f'Компонент сигнала ScD1: {ScD1}')
        print(f'Компонент сигнала ScD2: {ScD2}')
        print(f'Компонент сигнала ScD3: {ScD3}')
        print('################################################################################')

        print('"""Энтропия Шенона"""')

        data = pywt.wavedec(A_, db1)
        S = 0
        Etot = 0
        for d in data:
            E = d ** 2
            P = E / np.sum(E)
            S = -np.sum(P * np.log(P))
            Etot = np.sum(E)
            print(f"Энтропия Шенона: {S}")
            # print(f"Энергия: {Etot}")
            # E1 = Etot / S  # отношение энергии вейвлета к энтропии Шеннона
            #
            # print(f"Отношение энергии вейвлета к энтропии Шеннона: {E1}")
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

        # self.widget_8.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        self.widget_8.plot(PS1)

        # plt.figure(figsize=(17, 5))
        # plt.title("Энергетический спектр PS2")
        # plt.plot(PS2)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        # self.widget_9.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        self.widget_9.plot(PS2)

        # plt.figure(figsize=(17, 5))
        # plt.title("Энергетический спектр PS3")
        # plt.plot(PS3)  # строим график - ось `X` - первый столбец, `Y` - второй
        # plt.show()

        # self.widget_10.setBackground('w')
        # pen = pg.mkPen(color=(255, 0, 0))
        self.widget_10.plot(PS3)

    ########################################################################################################################
    ########################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Открыть EDF файл"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label_5.setText(_translate("MainWindow", "Загрузить изображение"))
        self.label_2.setText(_translate("MainWindow", "Длинна сигнала"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
