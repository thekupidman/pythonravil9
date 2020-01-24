#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
import random


class MyRaschet:

    def __init__(self):
        self.A = 0
        self.B = 0
        self.X = 0
        self.KK = [0,0,0,0,0,0,0,0,0,0]
        self.YY = [0,0,0,0,0,0,0,0,0,0]

    def setA(self, v):
        self.A = float(v)

    def setB(self, v):
        self.B = float(v)

    def setX(self, v):
        self.X = float(v)

    def setKK(self, i, v):
        self.KK[i] = float(v)

    def raschet(self):
        i = 0
        while i < 10:
            sum = 0
            proizv = 1
            p = 0
            while p <= i:
                proizv = proizv * self.KK[p]
                if p % 2 == 1:
                    sum = sum + self.KK[p]
                p = p + 1

            self.YY[i] = (((self.A * (self.X ** 4) + self.B * (self.X ** 3)) / (self.A ** 2 - self.B ** 3)) ** 3) / (proizv - sum)







            i = i + 1

    def getYY(self, i):
        return self.YY[i]


class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

    def initUI(self):
        self.table = QTableWidget(self)
        self.table.setGeometry(8, 8, 249, 400)
        self.table.setColumnCount(2)
        self.table.setRowCount(10)

        self.btn1 = QPushButton("Заполнить случайными числами", self)
        self.btn1.setGeometry(263, 288, 170, 57)

        self.btn2 = QPushButton("Очистить", self)
        self.btn2.setGeometry(439, 288, 170, 57)

        self.btn3 = QPushButton("Расчет", self)
        self.btn3.setGeometry(263, 351, 170, 57)

        self.btn4 = QPushButton("Выход", self)
        self.btn4.setGeometry(439, 351, 170, 57)

        self.label = QLabel(self)
        self.label.setGeometry(263, 8, 350, 55)
        pixmap = QPixmap('9.png')
        self.label.setPixmap(pixmap)

        self.label1 = QLabel(self)
        self.label1.setGeometry(263, 115, 50, 15)
        self.label1.setText("A = ")

        self.label2 = QLabel(self)
        self.label2.setGeometry(263, 155, 50, 15)
        self.label2.setText("B = ")

        self.label3 = QLabel(self)
        self.label3.setGeometry(263, 195, 50, 15)
        self.label3.setText("X = ")

        self.edit1 = QTextEdit(self)
        self.edit1.setGeometry(312, 112, 121, 21)

        self.edit2 = QTextEdit(self)
        self.edit2.setGeometry(312, 152, 121, 21)

        self.edit3 = QTextEdit(self)
        self.edit3.setGeometry(312, 192, 121, 21)

        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)

        self.setGeometry(300, 300, 635, 460)
        self.setWindowTitle('Test')
        self.show()

    def btn1Click(self):
        y = 0
        while y < 10:
            self.table.setItem(y, 0, QTableWidgetItem(str(random.randint(1, 99))))
            y = y + 1

    def btn2Click(self):
        y = 0
        while y < 10:
            self.table.setItem(y, 0, QTableWidgetItem(""))
            self.table.setItem(y, 1, QTableWidgetItem(""))
            y = y + 1

    def btn3Click(self):
        raschet = MyRaschet()

        raschet.setA(self.edit1.toPlainText())
        raschet.setB(self.edit2.toPlainText())
        raschet.setX(self.edit3.toPlainText())

        y = 0
        while y < 10:
            v = self.table.item(y, 0).text()
            raschet.setKK(y, v)
            y = y + 1

        raschet.raschet()

        y = 0
        while y < 10:
            self.table.setItem(y, 1, QTableWidgetItem(str(raschet.getYY(y))))
            y = y + 1

    def btn4Click(self):
       QApplication.exit()

if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
