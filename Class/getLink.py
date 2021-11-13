import os


from Class.dataIO import DataIO
from Class.debug import Debug

'''
    用于保存每个磁贴的属性，只有在新建磁贴的时候才会运行
    初始化的时候传入.exe或者.lnk的绝对完整路径。
'''


class GetLink:

    def __init__(self, filePathAndName):
        self.debug = Debug("GetLink")
        self.filePathAndName = filePathAndName  # 这个path包含路径，文件名，文件后缀,应该是个绝对路径
        self.filepath, self.fileNameAndExt = os.path.split(filePathAndName)
        self.fileName, self.fileExt = os.path.splitext(self.fileNameAndExt)
        if self.fileExt == "":
            self.fileExt = ".lnk"
        # self.__saveLinkData()


    # 保存图标
    def __saveIcon(self):
        # large, small = win32gui.ExtractIconEx(self.filePathAndName, 0, 10)
        # win32gui.DestroyIcon(small[0])
        # self.pixmap = QtGui.QPixmap.fromWinHBITMAP(self.bitmapFromHIcon(large[0]), 2)
        # self.pixmap = PyQt5.QtWinExtras.QtWin.fromHICON(large[0])

        self.debug.dLog("图标保存功能未完成", 4001)

        # self.pixmap.save("a.ico", "ico")
