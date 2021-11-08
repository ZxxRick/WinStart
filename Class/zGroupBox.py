from PyQt5.Qt import *

from Class.debug import Debug
from Class.zButton import ZButton
from Class.zLineEdit import ZLineEdit


class ZGroupBox(QGroupBox):
    def __init__(self, parent):
        super().__init__()
        self.debug = Debug("ZGroupBox")
        self.parent = parent
        self.__initUI()
        self.__addButton()


    # 新建一个对象时候所做的初始化工作
    def __initUI(self):
        self.installEventFilter(self)
        # 进行布局设定
        self.layout = QGridLayout()  # 界面采用表格布局，其中的控件可以跨列
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        # 每组的标题头
        self.debug.dWarning("组标题需要优化修改，使用系统自带的",5006)
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

    def __addButton(self, buttons=None):
        # for bu in buttons:
        #     button = ZButton(self, bu.name, bu.row, bu.col, bu.allPath, bu.width, bu.height)
        #     self.layout.addWidget(button, button.row, button.col)
        # self.setLayout(self.layout)
        bu = ZButton(self, "exe", 1, 1, "pp", 2, 2)
        bu2 = ZButton(self, "exe2", 1, 1, "pp", 2, 2)
        bu3 = ZButton(self, "exe3", 1, 1, "pp", 2, 2)
        bu4 = ZButton(self, "exe4", 1, 1, "pp", 2, 1)

        '''
        addWidget(QWidget widget, int   fromRow, int fromColumn, int    rowSpan, int columnSpan, intalignment)
        当所添加的控件跨越多行或多列时，使用这个函数
        fromRow：起始行
        fromColumn：起始列
        rowSpan：控件跨越的行
        columnSpan：控件跨越的列
        '''
        self.layout.addWidget(bu, 2, 1, 2, 2)
        self.layout.addWidget(bu2, 2, 0, 1, 1)
        self.layout.addWidget(bu4, 1, 0, 1, 2)
        self.setLayout(self.layout)
