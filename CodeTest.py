from Class.dataIO import DataIO

from PyQt5 import QtWidgets
from Class.dataInforClass import *
from Class.getLink import GetLink
from Thread.getInput import GetInput
from Thread.hotKey import HotKey

import win32ui
import win32gui

if __name__ == '__main__':
    pass
    pp = r"E:\Tools\iconChange\iconChange.exe"
    bu = ButtonInfor("a", "exe", pp)
    dataIO = DataIO()
    dataIO.addButtonInNewGroup(bu)
