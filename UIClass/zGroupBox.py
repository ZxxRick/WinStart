from PyQt5.Qt import *
from PyQt5 import QtWidgets
from Class.dataIO import DataIO
from Class.dataInforClass import ButtonInfor
from Class.debug import Debug
from Class.getLink import GetLink
from UIClass.zButton import ZButton
from UIClass.zLineEdit import ZLineEdit


class ZGroupBox(QGroupBox):
    def __init__(self, parent, groupNum, groupName):
        super().__init__()
        self.debug = Debug("ZGroupBox")
        self.parent = parent
        self.groupNum = groupNum
        self.groupName = groupName

        self.__initUI()
        self.__initStyle()

    # 右键菜单
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        addButtonAction = menu.addAction("添加磁贴")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        # 添加磁贴的功能
        if action == addButtonAction:
            dataIO = DataIO()
            try:
                # dataIO.addButton(button,self.groupNum)

                fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "",
                                                                           "*.exe;;*.lnk;;")  # 这一行代码是网上找的，并未细看

                getLink = GetLink(fileName)
                button = ButtonInfor(getLink.fileName, getLink.fileExt, fileName)
                print(button.buttonName, end=" ---- ")
                print(button.buttonType, end=" ---- ")
                print(button.buttonRunPath)
                dataIO.addButtonInOldGroup(button, self.groupNum)
                self.debug.dLog(self.groupNum + "组添加磁贴成功")
                pass
            except:
                self.debug.dWarning("执行取消固定失败")

    # 新建一个对象时候所做的初始化工作
    def __initUI(self):
        # self.installEventFilter(self)

        # 进行布局设定
        self.layout = QGridLayout()  # 界面采用表格布局，其中的控件可以跨列
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        # 每组的占位符
        lineEdit = ZLineEdit(self.groupName, self.groupNum)
        self.layout.addWidget(lineEdit, 0, 0, 1, 6)

        # 每组的标题头
        self.debug.dWarning("组标题需要优化修改", 5006)

    def addButton(self, buttons):
        """
            向组内添加按钮
            参数是一个列表，其中的元素是ButtonInfor类
        """
        for bu in buttons:
            button = ZButton(self, bu.buttonName, bu.buttonType, bu.buttonRunPath, bu.buttonX, bu.buttonY, bu.buttonW,
                             bu.buttonH)
            self.layout.addWidget(button, bu.buttonX, bu.buttonY, bu.buttonW, bu.buttonH)
        self.setLayout(self.layout)

    def __initStyle(self):

        # 设置栅格布局的边距,左、上、右、下
        self.layout.setContentsMargins(10, 0, 10, 0)
        # 设置按钮见的间距
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        """
            
            "ZGroupBox{color:transparent}"
        """
        self.setStyleSheet(
            "ZGroupBox{border:None}"
            "ZGroupBox{font-size:17px;font-family:'楷体'}"
        )
