from PyQt5.Qt import *
# 用于存放几个ZGroupBox的容器
from Class.debug import Debug
from UIClass.zGroupBox import ZGroupBox


class ZGroupList(QWidget):
    def __init__(self, parent, width=None):
        super().__init__()
        self.debug = Debug("ZGroupList")
        self.parent = parent
        self.width = width
        self.__initUI()
        self.__initStyle()
        # self.__addGroup()

    def __initUI(self):
        self.layout = QVBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    # 传入的是一个列表，其内元素为按钮组
    def addGroup(self, groups):
        for group in groups:
            gr = ZGroupBox(self)
            gr.addButton(group.buttons)
            self.layout.addWidget(gr)
        self.setLayout(self.layout)
        self.debug.dLog("addGroup加载完毕", 7003)

    def __initStyle(self):
        # self.setStyleSheet("background-color:red;")
        self.debug.dLog("ZGroupList风格初始化完成", 7003)
