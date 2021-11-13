from PyQt5.Qt import *
from PyQt5.QtWidgets import *
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
        self.selfFlash()

    def contextMenuEvent(self, event):
        """
        右键菜单
        :param event:
        """
        menu = QMenu(self)
        addButtonAction = menu.addAction("添加磁贴")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        # 添加磁贴的功能
        if action == addButtonAction:
            dataIO = DataIO()
            try:
                path=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
                #获取需要添加的程序
                fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", path,
                                                                           "*.exe;;*.lnk;;")  # 这一行代码是网上找的，并未细看
                if fileName!="":
                    getLink = GetLink(fileName)
                    button = ButtonInfor(getLink.fileName, getLink.fileExt, fileName)
                    # 向数据中添加按钮
                    tag = dataIO.addButtonInOldGroup(button, self.groupNum)
                    # 如果成功向文件中写入数据，则刷新此组的布局
                    if tag == 0:
                        self.selfFlash()
                        self.debug.dLog(self.groupNum + "组添加磁贴成功")
                    elif tag == 2:
                        msg_box = QMessageBox.about(self, '提示', '此程序已固定')
                        msg_box.exec_()
            except:
                self.debug.dWarning("执行取消固定失败")

    def __initUI(self):
        """
            新建一个对象时候所做的初始化工作
        """
        # self.installEventFilter(self)
        self.tagInit=True
        # 进行布局设定
        self.layout = QGridLayout()  # 界面采用表格布局，其中的控件可以跨列
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        # 每组的占位符
        lineEdit = ZLineEdit(self.groupName, self.groupNum)
        self.layout.addWidget(lineEdit, 0, 0, 1, 6)

        # 每组的标题头
        self.debug.dWarning("组标题需要优化修改", 5006)

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

    def selfFlash(self):
        """
            刷新该组的按钮
            buttons是一个列表，其中的元素是ButtonInfor()类
        """
        self.debug.dLog("selfFlash run ")
        # 在填充之前需要清理一遍组（但头标题不清理
        for i in range(1, self.layout.count(), 1):
            self.layout.itemAt(i).widget().deleteLater()
        dataIO = DataIO()
        buttons = dataIO.getGroup(self.groupNum).buttons

        for bu in buttons:
            button = ZButton(self, bu.buttonName, bu.buttonType, bu.buttonRunPath, bu.buttonX, bu.buttonY, bu.buttonW,
                             bu.buttonH)
            button.setParent(self)
            self.layout.addWidget(button, bu.buttonX, bu.buttonY, bu.buttonW, bu.buttonH)
        self.setLayout(self.layout)

