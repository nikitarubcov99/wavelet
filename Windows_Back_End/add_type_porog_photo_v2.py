import sqlite3
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox


class Ui_Porog_Photo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 350)
        Form.setMinimumSize(QtCore.QSize(344, 350))
        Form.setMaximumSize(QtCore.QSize(344, 350))
        Form.setAccessibleName("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 80, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 291, 61))
        self.label_6.setStyleSheet("color: rgb(128, 128, 128);")
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 120, 293, 110))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #################################################################################
        #################################################################################

        """ ************************************************************************* """
        """ *                                                                       * """
        """ *                               ПОЕХАЛИ                                 * """
        """ *                                                                       * """
        """ ************************************************************************* """

        #################################################################################
        #################################################################################

        self.pushButton.clicked.connect(self.add_type_porog_photo)

        self.lineEdit.setMaxLength(30)

        self.lineEdit_2.setMaxLength(3)
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_2.setValidator(validator)

        self.lineEdit_3.setMaxLength(3)
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_3.setValidator(validator)

        self.lineEdit_4.setMaxLength(3)
        validator = QRegExpValidator(QRegExp(r'[0-9]*'))
        self.lineEdit_4.setValidator(validator)

    #################################################################################
    #################################################################################

    def add_type_porog_photo(self):

        self.ID = uuid.uuid4()

        name = self.lineEdit.text()
        por_1 = self.lineEdit_2.text()
        por_2 = self.lineEdit_3.text()
        por_3 = self.lineEdit_4.text()

        if len(name) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка НАЗВАНИЯ!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(por_1) == 0 or int(por_1) > 254:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ПОРОГа 1!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(por_2) == 0 or int(por_2) > 254:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ПОРОГа 2!')
            msg.setWindowTitle("Add")
            msg.exec_()

        elif len(por_3) == 0 or int(por_3) > 254:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)  # восклицательный
            msg.setText("ERROR!")
            msg.setInformativeText('Ошибка ПОРОГа 3!')
            msg.setWindowTitle("Add")
            msg.exec_()

        else:

            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f'''CREATE TABLE IF NOT EXISTS porog_photo(
                    ID TEXT ,
                    name TEXT PRIMARY KEY,
                    porog_1 TEXT,
                    porog_2 TEXT,
                    porog_3 TEXT
                    )''')

            db.commit()

            cursor.execute(f'SELECT name FROM porog_photo WHERE name ="{name}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO porog_photo VALUES('
                               f'"{self.ID}",'
                               f'"{name}",'
                               f'"{por_1}",'
                               f'"{por_2}",'
                               f'"{por_3}")'
                               )

                db.commit()

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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_5.setText(_translate("Form", "Добавление порогов для\n"
                                                "ТИПА ИЗОЗОБРАЖЕНИЯ:"))
        self.label_6.setText(_translate("Form", "Минимальное  значение:          (0, 0, 0)\n"
                                                "Рекомендуемое  значение:      (127, 127, 127)\n"
                                                "Максимальное значение:         (254, 254, 254)"))
        self.label_4.setText(_translate("Form", "Порог 3:"))
        self.label_2.setText(_translate("Form", "Порог 1:"))
        self.label_3.setText(_translate("Form", "Порог 2:"))
        self.label_7.setText(_translate("Form", "ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠ ᅠᅠ ᅠᅠ"))
        self.label.setText(_translate("Form", "Название типа\n"
                                              "изображения:"))
        self.label_8.setText(_translate("Form", "ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠ ᅠᅠ ᅠᅠ"))
        self.label_9.setText(_translate("Form", "ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠ ᅠᅠ ᅠᅠ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Porog_Photo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
