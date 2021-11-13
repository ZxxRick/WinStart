import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDrag
import time

from PyQt5.Qt import *

from UIClass.zAllGroup import ZAllGroup
from UI.TestDialog import Ui_Dialog


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.iniDragCor = [0, 0]

    def mousePressEvent(self, e):
        print("ppp", e.pos())
        self.iniDragCor[0] = e.x()
        self.iniDragCor[1] = e.y()

    def mouseMoveEvent(self, e):
        x = e.x() - self.iniDragCor[0]
        y = e.y() - self.iniDragCor[1]

        cor = QPoint(x, y)
        self.move(self.mapToParent(cor))  # 需要maptoparent一下才可以的,否则只是相对位置。

        print('drag button event,', time.time(), e.pos(), e.x(), e.y())


class TestDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # tt.setText("???")
        # tt.exe = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge"
        self.ly = self.layout()

        button1 = DraggableButton("mybutton", self)
        button1.move(50, 20)

        self.ly.addWidget(button1)
        self.setLayout(self.ly)
        # self.setWindowTitle("Click or Move")
        # self.setGeometry(300, 300, 280, 150)

    def mouseMoveEvent(self, e):
        print('main', e.x(), e.y())

        # qq=ZGroupBox(self)
        # qq.addButton()

        # qq=ZGroupList(self)
        # qq.addGroup()
        #
        # qq = ZAllGroup(3,self)
        # # qq.addGroupList()
        # qq=QPushButton()
        # self.ly.addWidget(qq)
        # self.setLayout(self.ly)
