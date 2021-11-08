from PyQt5.Qt import *

from UIClass.zGroupList import ZGroupList

'''
    用于加载所有ZGroupList的控件
'''


class ZAllGroup(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.layout = QHBoxLayout()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # 这个Preferred及其重要
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    # 进行数据填充
    def addGroupList(self, lists, hasListCount, shouldListCount):
        for li in lists:
            gl = ZGroupList(self)
            gl.addGroup(li.groups)
            self.layout.addWidget(gl)
        for i in range(int(shouldListCount)-int(hasListCount)):
            self.layout.addStretch()  # 占位符
        self.setLayout(self.layout)
