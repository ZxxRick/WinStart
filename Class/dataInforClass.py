'''
        {“节点号”：xx,“节点位置”：[x,y],"节点名字"：xx,节点按钮组：[x,x,x,]}*N

        按钮组里面又有{}

    '''


class ButtonInfor():
    '''
    parent, name, row, col,allPath,wid=0,hei=0
    '''
    def __init__(self):
        self.buttonparentID=None
        self.buttonname=None
        self.buttonrow=None
        self.buttoncol=None
        self.buttonallPath=None
        self.buttonwidth=None
        self.buttonheight=None

    def getInforDict(self):

        pass

class GroupInfor():
    def __init__(self):
        self.GroupID = None
        self.GroupName = None
        self.GroupLocal = [0, 0]
        self.GroupButtons = []
