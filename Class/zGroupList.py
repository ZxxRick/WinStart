from PyQt5.Qt import *
# 用于存放几个ZGroupBox的容器
from Class.debug import Debug
from Class.zGroupBox import ZGroupBox


class ZGroupList(QWidget):
    def __init__(self, parent, width=None):
        super().__init__()
        self.debug = Debug("ZGroupList")
        self.parent = parent
        self.width = width
        self.__initUI()
        self.__initStyle()
        self.__addGroup()

    def __initUI(self):
        self.layout = QVBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    def __addGroup(self):
        gr = ZGroupBox(self)
        gr2 = ZGroupBox(self)
        gr3 = ZGroupBox(self)
        self.layout.addWidget(gr)
        self.layout.addWidget(gr2)
        self.layout.addWidget(gr3)

        self.setLayout(self.layout)
        pass

    def __initStyle(self):
        # self.setStyleSheet("background-color:red;")
        self.debug.dLog("ZGroupList风格初始化完成", 7003)
