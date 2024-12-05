from PyQt6.QtWidgets import QDialog, QFileDialog, QMainWindow, QSizePolicy, QApplication, QPushButton, QWidget, \
    QVBoxLayout, \
    QListWidgetItem
from MainWindow import Library, Inf, AddLibrary
from PyQt6 import QtCore, QtGui
import sys, sqlite3, os


def selectau(text):
    data = []
    with sqlite3.connect("ForLibrary.db") as db:
        cursor = db.cursor()
        query = """SELECT id,title FROM Books WHERE author LIKE ?;"""
        cursor.execute(query, (text + "%",))
        for i in cursor:
            data.append(i)
        db.commit()
        return data


def selectna(text):
    data = []
    with sqlite3.connect("ForLibrary.db") as db:
        cursor = db.cursor()
        query = """SELECT id,title FROM Books WHERE title LIKE ?;"""
        cursor.execute(query, (f"{text}%",))
        for i in cursor:
            data.append(i)
        db.commit()
        return data


class Forlibrary(Library, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1001, 729)
        self.lookfor.clicked.connect(self.look)
        self.delet.clicked.connect(self.dele)
        self.add.clicked.connect(self.ad)
        self.current = None

    def ad(self):
        self.win = Addbook()
        self.win.exec()

    def dele(self):
        if self.current is not None:
            with sqlite3.connect("ForLibrary.db") as db:
                cursor = db.cursor()
                query = """DELETE FROM Books WHERE id = ?;"""
                cursor.execute(query, (int(self.current),))
                db.commit()
            self.look()

    def look(self):
        try:
            self.tableWidget.clear()
            text = self.lineEdit.text()
            if self.lineEdit.text() == "":
                res = []
                with sqlite3.connect("ForLibrary.db") as db:
                    cursor = db.cursor()
                    query = """SELECT id,title FROM Books WHERE 1 = 1;"""
                    cursor.execute(query)
                    for i in cursor:
                        res.append(i)
                    db.commit()
            else:
                if self.comboBox.currentText() == "                                  По автору":
                    res = selectau(text)
                else:
                    res = selectna(text)
            for i in res:
                item = QListWidgetItem(f"{i[0]}")
                self.tableWidget.addItem(item)

                button = QPushButton(f"{i[1]}")
                button.clicked.connect(self.click)
                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                button.setStyleSheet("color: black; background: #6E6E6E;")

                self.tableWidget.setItemWidget(item, button)

            main_layout = QVBoxLayout(self)
            main_layout.addWidget(self.tableWidget)
            self.setLayout(main_layout)

        except Exception as ex:
            print(ex)

    def click(self):
        self.current = self.tableWidget.currentItem().text()
        name = self.sender().text()
        with sqlite3.connect("ForLibrary.db") as db:
            cursor = db.cursor()
            query = """SELECT author, genre, image, year FROM Books WHERE title = ?;"""
            cursor.execute(query, (name,))
            data = cursor.fetchall()
            data = data[0]
            print(data)
            db.commit()
        try:
            self.win = Info(name, data[0], data[1], data[2], str(data[3]))
            self.win.move(self.x() + 225, self.y())
            self.win.show()
        except Exception as ex:
            print(ex)

class Info(Inf, QMainWindow):
    def __init__(self, title, author, genre, image, year):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.label_3.setText(title)
        self.label_5.setText(author)
        self.label_6.setText(genre)
        self.label_8.setText(year)
        if os.path.exists(image):
            pass
        else:
            image = "Photo/8f2b47ca613a0ace7ef7960c37974f30.jpeg"
        self.label.setPixmap(QtGui.QPixmap(image))

    def keyPressEvent(self, e):
        if e.key() == 16777216:
            self.close()


class Addbook(AddLibrary, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.add.clicked.connect(self.check)
        self.photo.clicked.connect(self.adphoto)
        self.photopath = False

    def adphoto(self):
        try:
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp)")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

            if file_dialog.exec():
                self.photopath = file_dialog.selectedFiles()
        except:
            return

    def check(self):
        try:
            if all([self.lineEdit_2.text(), self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text()]):
                image = "Photo/8f2b47ca613a0ace7ef7960c37974f30.jpeg"
                if self.photopath != False:
                    image = self.photopath[0]
                    print(image)
                with sqlite3.connect("ForLibrary.db") as db:
                    cursor = db.cursor()
                    query = """INSERT INTO Books (author, title, genre, year, image) VALUES (?, ?, ?, ?, ?);"""
                    cursor.execute(query, (
                        self.lineEdit_2.text(), self.lineEdit.text(), self.lineEdit_3.text(),
                        f"{self.lineEdit_4.text()}",
                        image))
                    db.commit()
                self.close()
            else:
                return
        except Exception as ex:
            print(ex)

    def keyPressEvent(self, e):
        if e.key() == 16777216:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Forlibrary()
    ex.show()
    sys.exit(app.exec())
