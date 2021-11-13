from PyQt5.Qt import *

from Class.dataIO import DataIO


class ZLineEdit(QLineEdit):
    def __init__(self, titleText, groupNum):
        super().__init__()
        self.__titleText = titleText
        self.groupNum = groupNum
        self.__initUI()
        self.__initStyle()

    def setTitleText(self, titleText):
        self.__titleText = titleText

    def getTitleText(self):
        return self.__titleText

    # 事件过滤器
    def eventFilter(self, element, event):

        if element == self:
            # 双击控件的时候可以修改内容
            if event.type() == QEvent.MouseButtonDblClick:
                self.setDisabled(False)
            # 当控件的尺寸发生改变时，重塑其高度
            if event.type() == QEvent.Resize:
                self.setFixedHeight(int(self.width() / 10))

            # 当控件失焦的时候禁止修改,并且检查是否修改
            if event.type() == QEvent.FocusOut:
                te = self.text()
                if te != self.__titleText:
                    ''''
                        修改数据
                    '''
                    dataOI = DataIO()
                    dataOI.alterGroupName(self.groupNum, self.text())
                self.setDisabled(True)

        return QWidget.eventFilter(self, element, event)

    def __initUI(self):
        """
            用于初始化UI的数据
        """
        # 事件过滤器注册
        self.installEventFilter(self)
        self.setText(self.__titleText)
        # 初始时标题栏不能点击
        self.setDisabled(True)
        # 设置标题栏的高度
        self.setFixedHeight(int(self.width() / 10))

    def __initStyle(self):
        self.setStyleSheet(
            "ZLineEdit{border-radius: 3px}"
            "ZLineEdit{font-size:17px;font-family:'楷体'}")
