import os
from PyQt5.Qt import *
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
        self.buttonParent = parent  # 父控件
        self.buttonName = buttonName
        self.buttonRunPath = buttonRunPath  # 需要加载的程序,完全文件路径
        self.buttonType = buttonType
        print(buttonName + "-" + buttonRunPath + "-" + buttonType)
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
            os.startfile(self.buttonRunPath)

        if event.button() == Qt.RightButton:
            self.debug.dLog("自定义按钮右键被按下", 2002)

    # 事件过滤器，在控件尺寸发生改变时，计算其高度
    def eventFilter(self, element, event):
        if element == self and event.type() == QEvent.Resize:
            self.setFixedHeight(int(self.width() * (self.buttonH / self.buttonW)))
        return QWidget.eventFilter(self, element, event)

    # 初始化按钮的信息
    def __initUI(self):
        self.installEventFilter(self)
        # self.installEventFilter(self)

        self.setText(self.buttonName)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)  # 第二个参数的确是高度
        self.debug.dLog("按钮位置，尺寸初始化完成", 2004)

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
        self.debug.dLog("按钮风格初始化完成", 2003)