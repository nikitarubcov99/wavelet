import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Disease(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 290)
        MainWindow.setMinimumSize(QtCore.QSize(400, 290))
        MainWindow.setMaximumSize(QtCore.QSize(400, 290))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 390, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 390, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 201, 16))
        self.label_4.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 281, 20))
        self.label_5.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(51, 110, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(155, 217, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 71, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 149, 81, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 160, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
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

        self.lineEdit_2.setMaxLength(10)  # ограничения для kod
        validator_1 = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_2.setValidator(validator_1)  # валидация только на цифры

        validator = QRegExpValidator(QRegExp(r'[ a-zA-Zа-яА-Я]*'))
        self.lineEdit.setValidator(validator)  # валидация только на буквы


        #################################################################################

        self.pushButton.clicked.connect(self.add_db_name_of_the_disease)

        #################################################################################
    #################################################################################

    def add_db_name_of_the_disease(self):

        self.ID = uuid.uuid4()

        name = self.lineEdit.text()
        kod = self.lineEdit_2.text()

        if len(name) == 0:

            self.lineEdit.clear()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка НАЗВАНИЯ!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(kod) == 0:

            self.lineEdit_2.clear()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка КОДА БОЛЕЗНИ!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:

            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS disease(
                    ID TEXT PRIMARY KEY,
                    name_of_the_disease TEXT,
                    kod_disease TEXT
                    )''')

            db.commit()

            cursor.execute(f'SELECT name_of_the_disease FROM disease WHERE name_of_the_disease ="{name}"')
            if cursor.fetchone() is None:
                cursor.execute(f'SELECT kod_disease FROM disease WHERE kod_disease ="{kod}"')
                if cursor.fetchone() is None:
                    cursor.execute(f'INSERT INTO disease VALUES('
                                   f'"{self.ID}",'
                                   f'"{name}",'
                                   f'"{kod}")'
                                   )

                    db.commit()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)  # восклицательный
                    msg.setText("Добавлено!")
                    msg.setInformativeText('Результат добавлен в БД!')
                    msg.setWindowTitle("Add")
                    msg.exec_()

                    self.lineEdit_2.clear()
                    self.lineEdit.clear()
                else:
                    print('ERROr_Add_db')

                    self.lineEdit_2.clear()
                    self.lineEdit.clear()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Ошибка")
                    msg.setInformativeText('Такая запись уже имеется!')
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                print('ERROr_Add_db')

                self.lineEdit.clear()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('Такая запись уже имеется!')
                msg.setWindowTitle("Error")
                msg.exec_()

    #################################################################################
    #################################################################################

    """ ************************************************************************* """
    """ *                                                                       * """
    """ *                                 КОНЕЦ                                 * """
    """ *                                                                       * """
    """ ************************************************************************* """

    #################################################################################
    #################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Добавить название БОЛЕЗНИ"))
        self.label_4.setText(_translate("MainWindow", "Пример: 024"))
        self.label_5.setText(_translate("MainWindow", "Пример: не выявлено"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Введите название болезни:"))
        self.label_2.setText(_translate("MainWindow", "КОД болезни:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Disease()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
