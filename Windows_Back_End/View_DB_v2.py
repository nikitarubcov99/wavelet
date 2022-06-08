import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


class Ui_View_DB(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 790)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 790))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 790))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 1381, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 1381, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 160, 1381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 140, 241, 31))
        self.label_2.setStyleSheet("color:rgb(200, 200, 200)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 120, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 90, 221, 20))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 91, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(589, 121, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
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
        self.vse_table_db()
        self.pushButton_2.clicked.connect(self.read_limited_rows)
        self.pushButton.clicked.connect(self.deleted_data)

    def vse_table_db(self):
        self.comboBox.clear()

        db = sqlite3.connect('DataBase\\database.db')
        cursor = db.cursor()
        self.conn = db
        self.cursor = cursor
        self.cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        sql = cursor.fetchall()
        self.names = []
        for i in sql:
            self.names.append(i[0])
        self.comboBox.addItems(self.names)

    def read_limited_rows(self):
        xxx = self.comboBox.currentText()

        ggg = (''.join(map(str, xxx)))

        if self.names is None:
            print('Error_name_table')
        else:

            # try:
            db = sqlite3.connect('DataBase\\database.db')
            cursor = db.cursor()

            cursor.execute(f"""SELECT * FROM '{ggg}'""")

            result = cursor.fetchall()

            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))

            column_names = [d[0] for d in cursor.description]
            global row_dict
            for row in result:
                row_dict = {column_names[index]: value for (index, value) in enumerate(row)}
                # print(row_dict)
            self.tableWidget.setHorizontalHeaderLabels(row_dict)

            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

            db.close()

    #################################################################################
    #################################################################################

    def deleted_data(self):

        text = self.lineEdit.text()
        xxx = self.comboBox.currentText()

        if xxx == 'patient':
            connections = sqlite3.connect('DataBase\\database.db')
            c = connections.cursor()
            c.execute(f'SELECT ID FROM {xxx} WHERE snils ="{text}"')

            if c.fetchone() is None:
                print('ERROr_Add_ndvi_db')
                self.lineEdit.setText('')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('Такой записи нет!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                c.execute(f'DELETE FROM {xxx} WHERE snils ="{text}"')
                connections.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Запись удалена")
                msg.setInformativeText(f'Запись {text} успешно удалена!')
                msg.setWindowTitle("Ok")
                msg.exec_()

                print(f"Запись {text} успешно удалена")

                self.lineEdit.setText('')
                self.read_limited_rows()

                print('Detele_DB_zapis')

        else:
            connections = sqlite3.connect('DataBase\\database.db')
            c = connections.cursor()
            c.execute(f'SELECT ID FROM {xxx} WHERE ID ="{text}"')

            if c.fetchone() is None:
                print('ERROr_Add_ndvi_db')
                self.lineEdit.setText('')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Ошибка")
                msg.setInformativeText('Такой записи нет!')
                msg.setWindowTitle("Error")
                msg.exec_()

            else:
                c.execute(f'DELETE FROM {xxx} WHERE ID ="{text}"')
                connections.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Запись удалена")
                msg.setInformativeText(f'Запись {text} успешно удалена!')
                msg.setWindowTitle("Ok")
                msg.exec_()

                print(f"Запись {text} успешно удалена")

                self.lineEdit.setText('')
                self.read_limited_rows()

                print('Detele_DB_zapis')

    """___________________________________________________________________________"""
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
        self.label.setText(_translate("MainWindow", "Работа с БАЗОЙ ДАННЫХ"))
        self.label_2.setText(_translate("MainWindow", "Пример: 000-000-000 46"))
        self.pushButton.setText(_translate("MainWindow", "Удалить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбрать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_View_DB()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
