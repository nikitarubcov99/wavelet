import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_Disease(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 301, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
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
        """ *                               ??????????????                                 * """
        """ *                                                                       * """
        """ ************************************************************************* """

        #################################################################################
        #################################################################################

        # self.lineEdit_5.setMaxLength(11)  # ?????????????????????? ?????? ????????????
        # validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        # self.lineEdit_5.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????

        validator = QRegExpValidator(QRegExp(r'[ a-zA-Z??-????-??]*'))
        self.lineEdit.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????


        #################################################################################

        self.pushButton.clicked.connect(self.add_db_name_of_the_disease)

        #################################################################################

    def add_db_name_of_the_disease(self):

        self.ID = uuid.uuid4()

        name = self.lineEdit.text()

        if len(name) == 0:

            self.lineEdit.clear()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ????????????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:

            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS disease(
                    ID TEXT PRIMARY KEY,
                    name_of_the_disease TEXT
                    )''')

            db.commit()

            cursor.execute(f'SELECT name_of_the_disease FROM disease WHERE name_of_the_disease ="{name}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO disease VALUES('
                               f'"{self.ID}",'
                               f'"{name}")'
                               )

                db.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
                msg.setText("??????????????????!")
                msg.setInformativeText('?????????????????? ???????????????? ?? ????!')
                msg.setWindowTitle("Add")
                msg.exec_()

                self.lineEdit.clear()
            else:
                print('ERROr_Add_db')

                self.lineEdit.clear()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("????????????")
                msg.setInformativeText('?????????? ???????????? ?????? ??????????????!')
                msg.setWindowTitle("Error")
                msg.exec_()

    #################################################################################
    #################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????? ???????????????? ??????????????"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_Disease()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
