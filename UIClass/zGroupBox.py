from PyQt5.Qt import *

from Class.debug import Debug
from UIClass.zButton import ZButton
from UIClass.zLineEdit import ZLineEdit


class ZGroupBox(QGroupBox):
    def __init__(self, parent):
        super().__init__()
        self.debug = Debug("ZGroupBox")
        self.parent = parent
        self.__initUI()
        # self.__addButton()

    # 新建一个对象时候所做的初始化工作
    def __initUI(self):
        self.installEventFilter(self)
        # 进行布局设定
        self.layout = QGridLayout()  # 界面采用表格布局，其中的控件可以跨列
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        # 每组的标题头
        self.debug.dWarning("组标题需要优化修改，使用系统自带的", 5006)
        lineEdit = ZLineEdit()
        self.layout.addWidget(lineEdit, 0, 0, 1, 6)
        # 用于占位的空白Label
        # for i in range(0, 6, 1):
        #     lable = QLabel()
        #     print(i)
        #     self.layout.addWidget(lable, 0, i)

    # 这里的Buttons应该是字典列表
    '''
        此函数比较复杂，暂时未写
    '''

    def addButton(self, buttons):
        for bu in buttons:
            button = ZButton(self, bu.buttonName, bu.buttonType, bu.buttonRunPath, bu.buttonX, bu.buttonY, bu.buttonW,
                             bu.buttonH)
            B = QPushButton()
            B.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            # print(bu.buttonX)
            # print(bu.buttonY)
            # print(bu.buttonW)
            # print(bu.buttonH)
            self.layout.addWidget(button, bu.buttonX, bu.buttonY, bu.buttonW, bu.buttonH)
            # print("AA")
        self.setLayout(self.layout)
        '''
        addWidget(QWidget widget, int   fromRow, int fromColumn, int    rowSpan, int columnSpan, intalignment)
        当所添加的控件跨越多行或多列时，使用这个函数
        fromRow：起始行
        fromColumn：起始列
        rowSpan：控件跨越的行
        columnSpan：控件跨越的列
        '''
