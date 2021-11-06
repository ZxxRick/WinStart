class Debug():
    def __init__(self, className=""):
        self.name = className

    def dLog(self, msg, logID=0, ):
        print(self.name + " Log." + msg + " run msgID:" + str(logID))

    def dWarning(self, msg, warningID=0):
        print(self.name + " Warning." + msg + " msgID:" + str(warningID))
