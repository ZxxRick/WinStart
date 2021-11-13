from PyQt5.Qt import *

from Class.debug import Debug
from UIClass.zGroupList import ZGroupList

'''
    用于加载所有ZGroupList的控件
'''


class ZAllGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.debug = Debug("ZAllGroup")
        self.__initUI()

    def __initUI(self):
        self.layout = QHBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # 这个Preferred及其重要
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    # 进行数据填充
    def addGroupList(self, lists, hasListCount=None, shouldListCount=None):
        for li in lists:
            gl = ZGroupList(self)
            gl.addGroup(li.groups)
            self.layout.addWidget(gl)
            self.debug.dWarning("添加顺序需要优化")
        self.setLayout(self.layout)
