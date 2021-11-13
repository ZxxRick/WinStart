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

    def __initUI(self):
        self.layout = QVBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.debug.dLog("ZGroupList风格初始化完成", 7003)

    # 传入的是一个列表，其内元素为按钮组
    def addGroup(self, groups):
        """

        :param groups: groupInfor类型的数据
        :return:
        """
        for group in groups:
            gr = ZGroupBox(self, group.groupNum, group.groupName)

            self.layout.addWidget(gr)
        self.setLayout(self.layout)
        self.debug.dLog("addGroup加载完毕", 7003)

    def __initStyle(self):
        # self.setStyleSheet("background-color:red;")
        pass
