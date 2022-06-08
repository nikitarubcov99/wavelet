import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Add_DB_Patient(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 590)
        MainWindow.setMinimumSize(QtCore.QSize(410, 590))
        MainWindow.setMaximumSize(QtCore.QSize(410, 590))
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
        self.pushButton.setGeometry(QtCore.QRect(150, 520, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 391, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(50, 100, 301, 20))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 450, 61, 61))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 470, 201, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 61, 31))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 410, 81, 41))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 310, 301, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 280, 61, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 240, 301, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 350, 61, 61))
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(150, 420, 201, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 301, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 61, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 370, 201, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 291, 16))
        self.label_9.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 190, 291, 16))
        self.label_10.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 260, 291, 16))
        self.label_11.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 330, 291, 16))
        self.label_12.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 390, 201, 20))
        self.label_13.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_13.setObjectName("label_13")
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
        """ *                               ПОЕХАЛИ                                 * """
        """ *                                                                       * """
        """ ************************************************************************* """

        #################################################################################
        #################################################################################

        self.lineEdit_5.setMaxLength(11)  # ограничения для снилса
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_5.setValidator(validator)  # валидация только на цифры

        validator = QRegExpValidator(QRegExp(r'[a-zA-Zа-яА-Я]*'))
        self.lineEdit.setValidator(validator)  # валидация только на буквы
        self.lineEdit_2.setValidator(validator)  # валидация только на буквы
        self.lineEdit_3.setValidator(validator)  # валидация только на буквы

        #################################################################################

        self.pushButton.clicked.connect(self.add_db_patient)
        self.disease_comboBox()

        #################################################################################
    #################################################################################

    def disease_comboBox(self):

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
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка СНИЛС!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(f) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ФАМИЛИИ!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(i) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ИМЕНИ!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(o) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ОТЧЕСТВА!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(address) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка АДРЕСА!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:
            while len(snils) < 11:
                snils = '0' + snils
            snils = f'{snils[0:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:11]}'

            ID = self.ID

            AddPatient(ID, f, i, o, snils, address, data_b, diagnoz)

            print(ID)
            print(f)
            print(i)
            print(o)
            print(snils)
            print(address)
            print(data_b)
            print(diagnoz)
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
        self.label.setText(_translate("MainWindow", "Добавить пациента"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_7.setText(_translate("MainWindow", "Диагноз:"))
        self.label_4.setText(_translate("MainWindow", "Отчество:"))
        self.label_2.setText(_translate("MainWindow", "Фамилия:"))
        self.label_6.setText(_translate("MainWindow", "Год рождения:"))
        self.label_5.setText(_translate("MainWindow", "Адрес:"))
        self.label_8.setText(_translate("MainWindow", "Снилс:"))
        self.label_3.setText(_translate("MainWindow", "Имя:"))
        self.label_9.setText(_translate("MainWindow", "Пример: Петров"))
        self.label_10.setText(_translate("MainWindow", "Пример: Григорий"))
        self.label_11.setText(_translate("MainWindow", "Пример: Тимофеевич"))
        self.label_12.setText(_translate("MainWindow", "Пример: Курская область, пгт. Губа, ул. Ленина, д. 46"))
        self.label_13.setText(_translate("MainWindow", "Пример: 00000000046"))

class AddPatient:
    def __init__(self, ID, f, i, o, snils, address, data_b, diagnoz):

        global en

        self.ID = ID
        self.f = f
        self.i = i
        self.o = o
        self.snils = snils
        self.address = address
        self.data_b = data_b
        self.diagnoz = diagnoz

        # db = sqlite3.connect('DataBase\\database.db')
        db = sqlite3.connect(r'C:\Users\nero1\PycharmProjects\diplom\DataBase\database.db')
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
        fio__ = f'{self.f} {self.i} {self.o}'

        cursor.execute(f'SELECT snils FROM patient WHERE snils ="{self.snils}"')
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
            en = 'Add'

        else:
            en = 'Error'
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_DB_Patient()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
