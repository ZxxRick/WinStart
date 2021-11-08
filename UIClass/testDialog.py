
from PyQt5.Qt import *

from UIClass.zAllGroup import ZAllGroup
from UI.TestDialog import Ui_Dialog


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
