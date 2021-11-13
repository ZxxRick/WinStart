import os
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qtpy import QtGui

from Class.dataIO import DataIO
from Class.debug import Debug


class ZButton(QPushButton):
    """
        宽高是1，2，3这些整数，
        行列是他们的起始位置，也是1，2，3
        行的起始是1，列的起始是0
    """

    def __init__(self, parent, buttonName, buttonType, buttonRunPath, buttonX, buttonY, buttonW, buttonH):
        super().__init__()
        self.debug = Debug("ZButton")
        self.parent = parent  # 父控件
        self.buttonName = buttonName
        self.buttonRunPath = buttonRunPath  # 需要加载的程序,完全文件路径
        self.buttonType = buttonType
        self.buttonX = buttonX  # 控件在父控件中的行列,及尺寸
        self.buttonY = buttonY
        self.buttonW = buttonW
        self.buttonH = buttonH
        self.__initUI()
        self.__initStyle()

    # 重写按钮点击事件
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.debug.dLog("自定义按钮左键被按下", 2001)
            # 这里必须用try，不然用户点击后未启动会导致程序错误
            try:
                os.startfile(self.buttonRunPath)
            except:
                self.debug.dWarning("磁贴程序未启动", 2011)

    # 右键菜单
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        delButtonAction = menu.addAction("取消固定")
        renameButtonAction = menu.addAction("重命名")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == delButtonAction:
            dataIO = DataIO()
            try:
                dataIO.delButton(self.buttonRunPath)
                self.parent.selfFlash()
            except:
                self.debug.dWarning("执行取消固定失败")
        elif action == renameButtonAction:
            try:
                pass
            except:
                self.debug.dWarning("我还没写呢、、、、")

    # 事件过滤器，在控件尺寸发生改变时，计算其高度
    def eventFilter(self, element, event):
        if element == self and event.type() == QEvent.Resize:
            self.setFixedHeight(int(self.width() * (self.buttonH / self.buttonW)))
        return QWidget.eventFilter(self, element, event)

    # 初始化按钮的信息
    def __initUI(self):
        self.installEventFilter(self)

        self.setText(self.buttonName)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)  # 第二个参数的确是高度
        self.debug.dLog("按钮位置，尺寸初始化完成", 2004)

    def __initStyle(self):

        """

                                # border-radius:5px;
                                # border:none; #去除边框
        """
        self.setStyleSheet('''
                            ZButton
                            { 
                                background:transparent;
                                border:1; #无效初始化
                            }
                            '''
                           )
        self.debug.dLog("按钮风格初始化完成", 2003)
