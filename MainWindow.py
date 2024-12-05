from PyQt6 import QtCore, QtGui, QtWidgets
class Library(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 714)
        MainWindow.setStyleSheet("background: #6E6E6E;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add.setGeometry(QtCore.QRect(810, 30, 181, 131))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add.setStyleSheet("QPushButton{\n"
"border: 5px solid #ffaa7f;\n"
"color: #ffaa7f;\n"
"background: #6E6E6E;\n"
"border-radius: 60;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #6E6E6E;\n"
"background: #ffaa7f;\n"
"color:#6E6E6E;\n"
"border-radius: 60;\n"
"}")
        self.add.setObjectName("add")
        self.lookfor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.lookfor.setGeometry(QtCore.QRect(620, 30, 181, 131))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.lookfor.setFont(font)
        self.lookfor.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lookfor.setStyleSheet("QPushButton{\n"
"border: 5px solid #ffaa7f;\n"
"color: #ffaa7f;\n"
"background: #6E6E6E;\n"
"border-radius: 60;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #6E6E6E;\n"
"background: #ffaa7f;\n"
"color:#6E6E6E;\n"
"border-radius: 60;\n"
"}")
        self.lookfor.setObjectName("lookfor")
        self.delet = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delet.setGeometry(QtCore.QRect(430, 30, 181, 131))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.delet.setFont(font)
        self.delet.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delet.setStyleSheet("QPushButton{\n"
"border: 5px solid #ffaa7f;\n"
"color: #ffaa7f;\n"
"background: #6E6E6E;\n"
"border-radius: 60;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #6E6E6E;\n"
"background: #ffaa7f;\n"
"color:#6E6E6E;\n"
"border-radius: 60;\n"
"}")
        self.delet.setObjectName("delet")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 381, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 5px solid #ffaa7f;\n"
"color: rgb(0, 0, 0);\n"
"background: #6E6E6E;\n"
"border-radius: 30;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border: 5px solid #ffaa7f;\n"
"color:#ffaa7f;\n"
"background: #6E6E6E;\n"
"border-radius: 30;")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 200, 1002, 511))
        self.tableWidget.setStyleSheet("background: rgb(255, 170, 127);")
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library"))
        self.add.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.lookfor.setText(_translate("MainWindow", "НАЙТИ"))
        self.delet.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "писать тут"))
        self.comboBox.setItemText(0, _translate("MainWindow", "                                  По автору"))
        self.comboBox.setItemText(1, _translate("MainWindow", "                                  По названия"))


class Inf(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 735)
        MainWindow.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 60;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(125, 40, 300, 261))
        self.label.setStyleSheet("background: white;\n"
"border-radius: 0\n"
"")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 310, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(5, 360, 540, 61))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 430, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 0;\n"
"color:#ffaa7f;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(5, 480, 540, 61))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(5, 580, 540, 61))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 530, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(125, 680, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(125, 650, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: 0;\n"
"color:#ffaa7f;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "НАЗВАНИЕ"))
        self.label_4.setText(_translate("MainWindow", "АВТОР"))
        self.label_7.setText(_translate("MainWindow", "ЖАНР"))
        self.label_9.setText(_translate("MainWindow", "ГОД ВЫПУСКА"))

class AddLibrary(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 275)
        Dialog.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 190, 291, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 291, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 110, 291, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.photo = QtWidgets.QPushButton(parent=Dialog)
        self.photo.setGeometry(QtCore.QRect(630, 20, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.photo.setFont(font)
        self.photo.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.photo.setIconSize(QtCore.QSize(103, 64))
        self.photo.setObjectName("photo")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 291, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.add = QtWidgets.QPushButton(parent=Dialog)
        self.add.setGeometry(QtCore.QRect(630, 170, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(44)
        font.setBold(False)
        font.setWeight(50)
        self.add.setFont(font)
        self.add.setStyleSheet("border: 5px solid #ffaa7f;\n"
"background: #6E6E6E; \n"
"border-radius: 30;\n"
"color: rgb(0, 0, 0);")
        self.add.setIconSize(QtCore.QSize(103, 64))
        self.add.setObjectName("add")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "ЖАНР"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "НАЗВАНИЕ"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "ГОД ВЫПУСКА"))
        self.photo.setText(_translate("Dialog", "+"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "АВТОР"))
        self.add.setText(_translate("Dialog", "0"))