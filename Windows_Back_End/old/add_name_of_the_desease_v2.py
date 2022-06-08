import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Disease(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 301, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 21))
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

                    self.lineEdit.clear()
                else:
                    print('ERROr_Add_db')

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Введите название болезни"))
        self.label_2.setText(_translate("MainWindow", "КОД болезни ( 0 - 9 ):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Disease()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
