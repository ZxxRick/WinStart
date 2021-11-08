"""
    用于和userData文件交互的类
"""


class ButtonInfor:
    def __init__(self, buttonName=None, buttonType=None, buttonRunPath=None, buttonX=None, buttonY=None, buttonW=None,
                 buttonH=None):
        self.buttonName = buttonName
        self.buttonType = buttonType
        self.buttonRunPath = buttonRunPath
        self.buttonX = buttonX
        self.buttonY = buttonY
        self.buttonW = buttonW
        self.buttonH = buttonH


class GroupInfor:
    def __init__(self, groupNum=None):
        self.groupNum = groupNum
        self.buttons = []


class ListInfor:
    def __init__(self, colNum=None):
        self.colNum = colNum
        self.groups = []


class OSInfor:
    def __init__(self):
        self.screenWidth = None
        self.screenHeight = None
        self.shouldListCount = None
        self.hasListCount = None
        self.listS = []
