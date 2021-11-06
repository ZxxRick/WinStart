from PyQt5.QtWidgets import QDialog

from PyQt5 import QtCore
from Class.zButton import ZButton
from UI.TestDialog import Ui_Dialog


class TestDialog( QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        tt=ZButton()
        tt.setText("???")
        tt.exe=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge"
        self.ly=self.layout()
        self.ly.addWidget(tt)
        self.setLayout(self.ly)

        # qq=self.widget

        # qq.setC
        # self.widget.
        # self.setWidget(tt)
        # self.set
