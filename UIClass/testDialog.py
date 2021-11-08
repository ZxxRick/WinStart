
from PyQt5.Qt import *

from PyQt5 import QtCore

from Class.zAllGroup import ZAllGroup
from Class.zButton import ZButton
from Class.zGroupBox import ZGroupBox
from Class.zGroupList import ZGroupList
from UI.TestDialog import Ui_Dialog
from UI.TestQWidget import Ui_Form


class TestDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # tt.setText("???")
        # tt.exe = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge"
        self.ly = self.layout()

        # qq=ZGroupBox(self)
        # qq.addButton()

        # qq=ZGroupList(self)
        # qq.addGroup()
        #
        qq = ZAllGroup(3,self)
        qq.addGroupList()

        self.ly.addWidget(qq)
        self.setLayout(self.ly)
