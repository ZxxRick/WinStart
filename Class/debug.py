from datetime import datetime


class Debug():
    def __init__(self, className=""):
        self.name = className
        self.dieList = [5001, 2004, 2003]

    def dLog(self, msg, logID=0, ):
        if logID in self.dieList:  # 屏蔽掉按钮的log
            return

        dt = datetime.now()
        print(self.name + " Log." + msg + " run msgID:" + str(logID), end="  ")
        print(f'运行时间：{dt.hour}:{dt.minute}:{dt.second}')

    def dWarning(self, msg, warningID=0):
        return
        print(self.name + " Warning." + msg + " msgID:" + str(warningID))
