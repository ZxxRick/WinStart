# 此线程用于：用户唤醒界面后检测用户输入，当用户输如任意非指定键后将界面隐藏
import threading
from threading import Thread

import ctypes
import ctypes.wintypes

import win32con


class GetInput(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        shotControl_command=None
        exitControl_command=None
        user32 = ctypes.windll.user32
        while (True):
            if not user32.RegisterHotKey(None, 98, win32con.MOD_WIN, win32con.VK_F9):  # win+f9=screenshot
                print("Unable to register id", 98)
            if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.VK_F10):  # win+f10=exit program
                print("Unable to register id", 99)
            try:
                msg = ctypes.wintypes.MSG()
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == 99:
                            exitControl_command = True
                            return
                        elif msg.wParam == 98:
                            shotControl_command = True
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))
            finally:
                del msg
                user32.UnregisterHotKey(None, 98)
                user32.UnregisterHotKey(None, 99)
