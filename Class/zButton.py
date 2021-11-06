import os

from PyQt5.Qt import *

from Class.debug import Debug


class ZButton(QPushButton):

    def __init__(self):
        super().__init__()

        self.debug = Debug("ZButton")
        self.exe = None  # 需要加载的程序
        self.icon = None  # 显示的尺寸
        # self.size()#显示的尺寸
        self.__initStyle()

    # 重写按钮点击事件
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.debug.dLog("自定义按钮左键被按下", 2001)
            os.startfile(self.exe)

        if event.button() == Qt.RightButton:
            self.debug.dLog("自定义按钮右键被按下", 2002)

    def __initStyle(self):

        self.setStyleSheet('''
                            QPushButton
                            { 
                                background:transparent;border-radius:5px;
                                border:none; #去除边框
                            }
                            QPushButton#pushButton:hover{background:transparent;}#将按钮设置为透明
                            '''
                           )
        self.debug.dLog("界面风格初始化完成", 2003)
