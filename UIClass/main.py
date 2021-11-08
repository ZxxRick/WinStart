from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from Class.dataIO import DataIO
from Class.debug import Debug
from UIClass.zAllGroup import ZAllGroup
from Thread.hotKey import HotKey
from UI.mian import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.debug = Debug("MainUI")
        self.__initSelf()
        self.__initStyle()
        self.__addAllGroup()

    def Exit(self):
        self.close()

    def hide(self):  # 自己改写隐藏功能
        # super().hide()
        self.isShowTag = False

    def show(self):
        super().show()
        self.isShowTag = True

    def eventFilter(self, element, event):
        # 通过事件过滤器使得界面在不是焦点的时候隐藏
        if element == self and event.type() == QEvent.ActivationChange:
            if QApplication.activeWindow() != self:
                # self.hide()
                pass
        return QWidget.eventFilter(self, element, event)

    # 自己写的初始化函数，防止初始化函数内容太多太乱
    def __initSelf(self):
        self.installEventFilter(self)  # 注册事件过滤器
        self.isShowTag = True  # 如果是false，表示界面没显示
        self.hotKey = HotKey()
        self.hotKey.HotKeySignal.connect(self.__getHotKey)
        self.hotKey.start()

        # 在系统托盘处显示图标未写

        #

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
        # self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏最小化按钮
        self.setWindowState(Qt.WindowMaximized)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    # 加载控件
    def __addAllGroup(self):

        dataIO = DataIO()
        dataInfor = dataIO.readXML()
        ag = ZAllGroup(self)
        ag.addGroupList(dataInfor.listS, dataInfor.hasListCount, dataInfor.shouldListCount)
        self.scrollArea.setWidget(ag)
        self.debug.dLog("__addAllGroup 完毕", 1002)
