from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QSystemTrayIcon

from Thread.hotKey import HotKey
from UI.mian import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__initSelf()
        self.__initStyle()

        print("Log.mainUI init over")

    def Exit(self):
        self.close()

    def hide(self):  # 自己改写隐藏功能
        super().hide()
        self.isShowTag = False

    def show(self):
        super().show()
        self.isShowTag = True

    def eventFilter(self, element, event):
        # 通过事件过滤器使得界面在不是焦点的时候隐藏
        if element == self and event.type() == QEvent.ActivationChange:
            if QApplication.activeWindow() != self:
                self.hide()

        return QWidget.eventFilter(self, element, event)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("Butt")

    # 自己写的初始化函数，防止初始化函数内容太多太乱
    def __initSelf(self):
        self.installEventFilter(self)  # 注册事件过滤器
        self.isShowTag = True  # 如果是false，表示没显示
        self.hotKey = HotKey()
        self.hotKey.HotKeySignal.connect(self.__getHotKey)
        self.hotKey.start()

        # 在系统托盘处显示图标

    # 运行HotKey线程后获取返回值的函数
    def __getHotKey(self, tag):
        # print("Log.run __getHotKey()")
        if tag == 0:
            if self.isShowTag:
                self.hide()
                pass
            else:
                self.show()
            # 这里采用了一个非常笨的写法，在调用热键线程后，销毁它，然后在重新初始化一个热键线程
            del self.hotKey
            self.hotKey = HotKey()
            self.hotKey.HotKeySignal.connect(self.__getHotKey)
            self.hotKey.start()
        print("Log.over __getHotKey()")

    # 窗体风格初始化
    def __initStyle(self):
        self.setWindowOpacity(0.8)  # 设置窗口透明度
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏最小化按钮
        self.setWindowState(Qt.WindowMaximized)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明