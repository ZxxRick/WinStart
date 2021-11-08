from PyQt5.Qt import *

from Class.zGroupList import ZGroupList

'''
    用于加载所有ZGroupList的控件
'''


class ZAllGroup(QWidget):
    def __init__(self, colCount, parent=None):
        super().__init__()
        self.parent = parent
        self.colCount = colCount
        self.__initUI()
        self.__addGroupList()

    def __initUI(self):
        self.layout = QHBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # 这个Preferred及其重要

        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    # 进行数据填充
    def __addGroupList(self):
        for i in range(2):
            gl = ZGroupList(self)

            self.layout.addWidget(gl)
        self.layout.addStretch()  # 占位符
        self.setLayout(self.layout)
