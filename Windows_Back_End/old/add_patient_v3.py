import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_DB_Patient(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 465)
        MainWindow.setMinimumSize(QtCore.QSize(410, 465))
        MainWindow.setMaximumSize(QtCore.QSize(410, 465))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 390, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 391, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 221, 20))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 61, 41))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 340, 141, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 61, 41))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 61, 41))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 81, 41))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 210, 221, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 203, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 170, 221, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 61, 41))
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 300, 121, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 130, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 61, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 250, 101, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
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

        self.lineEdit_5.setMaxLength(11)  # ?????????????????????? ?????? ????????????
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_5.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????

        validator = QRegExpValidator(QRegExp(r'[a-zA-Z??-????-??]*'))
        self.lineEdit.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????
        self.lineEdit_2.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????
        self.lineEdit_3.setValidator(validator)  # ?????????????????? ???????????? ???? ??????????

        #################################################################################

        self.pushButton.clicked.connect(self.add_db_patient)
        self.norm_comboBox()

        #################################################################################
    #################################################################################

    def norm_comboBox(self):

        self.comboBox.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("SELECT name_of_the_disease FROM disease")
        sql = cursor.fetchall()
        self.disease = []
        for i in sql:
            self.disease.append(i[0])
        self.comboBox.addItems(self.disease)

    #################################################################################
    def add_db_patient(self):

        patient = 'patient'
        self.ID = uuid.uuid4()

        f = self.lineEdit.text()
        i = self.lineEdit_2.text()
        o = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        snils = self.lineEdit_5.text()
        data_b = self.dateEdit.text()
        diagnoz = self.comboBox.currentText()


        snils = str(snils)
        if len(snils) > 11 or len(snils) == 0:
            self.lineEdit_5.setText('')

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ??????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(f) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ??????????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(i) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ??????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(o) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ????????????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(address) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
            msg.setText("ERROR!")
            msg.setInformativeText('???????????? ????????????!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:
            while len(snils) < 11:
                snils = '0' + snils
            snils = f'{snils[0:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:11]}'

            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS patient(
                    ID TEXT,
                    fio_ TEXT,
                    address_ TEXT,
                    data_b_ TEXT,
                    diagnoz TEXT,
                    snils TEXT PRIMARY KEY,
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

            db.commit()
            cD1 = ''
            cD2 = ''
            cD3 = ''
            ScD1 = ''
            ScD2 = ''
            ScD3 = ''
            H = ''
            c = ''
            Array_S = ''
            Array_P = ''
            fio__ = f'{f} {i} {o}'

            cursor.execute(f'SELECT snils FROM patient WHERE snils ="{snils}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO patient VALUES('
                               f'"{self.ID}",'
                               f'"{fio__}",'
                               f'"{address}",'
                               f'"{data_b}",'
                               f'"{diagnoz}",'
                               f'"{snils}",'
                               f'"{cD1}",'
                               f'"{cD2}",'
                               f'"{cD3}",'
                               f'"{ScD1}",'
                               f'"{ScD2}",'
                               f'"{ScD3}",'
                               f'"{H}",'
                               f'"{c}",'
                               f'"{Array_S}",'
                               f'"{Array_P}")'
                               )
            #     cursor.execute("ALTER TABLE patient ADD COLUMN Array_P BLOW")
                # cursor.execute("ALTER TABLE patient DROP COLUMN Array_S")
                db.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # ??????????????????????????????
                msg.setText("??????????????????!")
                msg.setInformativeText('?????????????????? ???????????????? ?? ????!')
                msg.setWindowTitle("Add")
                msg.exec_()

                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()

            else:
                print('ERROr_Add_db')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("????????????")
                msg.setInformativeText('?????????? ???????????? ?????? ??????????????!')
                msg.setWindowTitle("Error")
                msg.exec_()

    #################################################################################
    #################################################################################

    """ ************************************************************************* """
    """ *                                                                       * """
    """ *                                 ??????????                                 * """
    """ *                                                                       * """
    """ ************************************************************************* """

    #################################################################################
    #################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "???????????????? ????????????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.label_7.setText(_translate("MainWindow", "??????????????:"))
        self.label_4.setText(_translate("MainWindow", "????????????????:"))
        self.label_2.setText(_translate("MainWindow", "??????????????:"))
        self.label_6.setText(_translate("MainWindow", "?????? ????????????????:"))
        self.label_5.setText(_translate("MainWindow", "??????????:"))
        self.label_8.setText(_translate("MainWindow", "??????????:"))
        self.label_3.setText(_translate("MainWindow", "??????:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_DB_Patient()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
