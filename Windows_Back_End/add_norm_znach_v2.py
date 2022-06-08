import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Norm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 370)
        MainWindow.setMinimumSize(QtCore.QSize(260, 370))
        MainWindow.setMaximumSize(QtCore.QSize(260, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 221, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 241, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
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

        self.pushButton.clicked.connect(self.add_db_norm)

        self.lineEdit.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit.setValidator(validator)

        self.lineEdit_2.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_2.setValidator(validator)

        self.lineEdit_3.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_3.setValidator(validator)

        self.lineEdit_4.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_4.setValidator(validator)

        self.lineEdit_5.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_5.setValidator(validator)

        self.lineEdit_6.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_6.setValidator(validator)

        self.lineEdit_7.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_7.setValidator(validator)

        self.lineEdit_8.setMaxLength(6)
        validator = QRegExpValidator(QRegExp(r'[0-9][.][0-9]*'))
        self.lineEdit_8.setValidator(validator)

    #################################################################################
    #################################################################################

    def add_db_norm(self):

        self.ID = uuid.uuid4()

        cd1 = self.lineEdit.text()
        cd2 = self.lineEdit_2.text()
        cd3 = self.lineEdit_3.text()
        scd1 = self.lineEdit_4.text()
        scd2 = self.lineEdit_5.text()
        scd3 = self.lineEdit_6.text()
        h = self.lineEdit_7.text()
        c = self.lineEdit_8.text()

        if len(cd1) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка cD1!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(cd2) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка cD2!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(cd3) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка cD3!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(scd1) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ScD1!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(scd2) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ScD2!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(scd3) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ScD3!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(h) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка H!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(c) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка c!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:
            ID = self.ID

            NormDB(ID, cd1, cd2, cd3, scd1, scd2, scd3, h, c)


            if en == 'Add':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # восклицательный
                msg.setText("Добавлено!")
                msg.setInformativeText('Результат добавлен в БД!')
                msg.setWindowTitle("Add")
                msg.exec_()

                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()
                self.lineEdit_8.clear()

            else:
                print('ERROr_Add_db')
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
        self.label_9.setText(_translate("MainWindow", "Добавление значений \"НОРМ\""))
        self.label.setText(_translate("MainWindow", "cD1:ᅠ "))
        self.label_2.setText(_translate("MainWindow", "cD2:"))
        self.label_3.setText(_translate("MainWindow", "cD3:"))
        self.label_4.setText(_translate("MainWindow", "ScD1:"))
        self.label_5.setText(_translate("MainWindow", "ScD2:"))
        self.label_6.setText(_translate("MainWindow", "ScD3:"))
        self.label_7.setText(_translate("MainWindow", "H:"))
        self.label_8.setText(_translate("MainWindow", "c:"))

class NormDB:
    def __init__(self, ID, cd1, cd2, cd3, scd1, scd2, scd3, h, c):
        global en

        self.ID = ID
        self.cD1 = cd1
        self.cD2 = cd2
        self.cD3 = cd3
        self.ScD1 = scd1
        self.ScD2 = scd2
        self.ScD3 = scd3
        self.H = h
        self.C = c

        # db = sqlite3.connect('DataBase\\database.db')
        db = sqlite3.connect(r'C:\Users\nero1\PycharmProjects\diplom\DataBase\database.db')
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

        db.commit()
        # cD1 = cd1
        # cD2 = cd2
        # cD3 = cd3
        # ScD1 = scd1
        # ScD2 = scd2
        # ScD3 = scd3
        # H = h
        # c = c

        cursor.execute(f'SELECT ID FROM norm WHERE ID ="{self.ID}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO norm VALUES('
                           f'"{self.ID}",'
                           f'"{self.cD1}",'
                           f'"{self.cD2}",'
                           f'"{self.cD3}",'
                           f'"{self.ScD1}",'
                           f'"{self.ScD2}",'
                           f'"{self.ScD3}",'
                           f'"{self.H}",'
                           f'"{self.C}")'
                           )

            db.commit()
            en = 'Add'

        else:
            en = 'Error'

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Norm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
