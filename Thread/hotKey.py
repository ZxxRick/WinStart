import win32con
import ctypes.wintypes
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
'''
    此处不用threading.Thread，而是用QThread，因为返回数据比较方便
'''


class HotKey(QThread):

    HotKeySignal = QtCore.pyqtSignal(int)  # 返回的数据

    def __init__(self, window=None, parent=None):
        super().__init__(parent)
        self.name = "HotKey"
        self.window = window

    def run(self):
        user32 = ctypes.windll.user32#加载user32.dll
        if not user32.RegisterHotKey(None, 30, win32con.MOD_WIN, win32con.VK_F10):  # win+f1
            print("Unable to register id", 30)

        while True:
            try:
                msg = ctypes.wintypes.MSG()
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == 30:
                            # print("Log.Press hotkeys")
                            self.HotKeySignal.emit(0)

            finally:
                del msg
                user32.UnregisterHotKey(None, 30)

