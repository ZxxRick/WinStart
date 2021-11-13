'''
    用于读写用户数据的（界面数据
'''
import os
import csv
import xml.dom.minidom as minidom

from Class.dataInforClass import *
from Class.debug import Debug


class DataIO:

    def __init__(self):
        self.debug = Debug("DataIO")
        self.dataFile = os.getcwd() + "/Data/userData.xml"

        # 如果不存在数据文件，需要创建一个。
        if not os.path.exists(self.dataFile):
            self.debug.dWarning("数据文件建立未写", 3019)

            # try:
            #     root = ET.Element('Root')  # 创建节点
            #     tree = ET.ElementTree(root)  # 创建文档
            #     tree.write(self.dataFile, encoding='utf-8', xml_declaration=True)
            #     self.debug.dLog(" 数据文件初始化完成", 3001)
            # except:
            #     self.debug.dWarning("文件初始化错误")

        self.dom = minidom.parse(self.dataFile)  # 读取文档
        self.root = self.dom.documentElement  # 获取根节点

    def __saveData(self):
        """
            本类自用的文件保存函数
        """
        try:
            with open(self.dataFile, 'wb') as fp:
                fp.write(self.dom.toxml(encoding='utf-8'))
                self.debug.dLog("userData保存完成", 3000)
        except:

            self.debug.dWarning("userData文件保存错误", 3111)

    # 输入的程序名字，绝对路径，类型（exe,lnk)
    def writeXML(self, fileName, filePath, fileType):
        data = [fileName, filePath, fileType]  # 需要写入的数据
        with open(self.dataFile, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            self.debug.dLog(" 数据文件写入完成", 3002)

    def addList(self, colNum):
        """
            添加列表,用于新建按钮或者改动按钮位置导致的新建列表
            :param colNum: 需要添加的列的位置
        """
        # 创建一个节点，命名为list
        newList = self.dom.createElement('list')
        self.debug.dLog("新建11group")
        # 将节点添加到父节点上
        self.root.appendChild(newList)
        # 给标签添加属性
        newList.attributes['colNum'] = '1'
        newGroup = self.dom.createElement("group")
        newList.appendChild(newGroup)
        newGroup.attributes['groupNum'] = '11'
        newGroup.attributes['groupName'] = ''

        # 修改布局中的列数
        hasListCount = self.root.getElementsByTagName("hasListCount")[0]
        newHasCount = int(hasListCount.firstChild.data) + 1
        # 添加数据需要使用doc.createTextNode函数
        hasListCount.appendChild(self.dom.createTextNode(str(newHasCount)))

    def delButton(self, buttonPath):
        """
            根据传入的文件路径来删除按钮
        :param buttonPath:字符串类型
        :return:返回一个bool类型的，标志是否完成


        注意：删除节点后未写界面刷新功能

        """
        lists = self.root.getElementsByTagName("list")
        for li in lists:
            groups = li.getElementsByTagName("group")
            for group in groups:
                buttons = group.getElementsByTagName("button")
                for button in buttons:
                    delpath = button.getElementsByTagName("buttonRunPath")[0].firstChild.data
                    if delpath == buttonPath:
                        try:
                            # 全部删除的tag
                            allDelTag = False
                            # 如果删除的是该组内最后一个磁贴，则删除这个组
                            if len(buttons) == 1:
                                group.parentNode.removeChild(group)
                                allDelTag = True
                            else:
                                button.parentNode.removeChild(button)

                            self.__saveData()
                            # #如果不删除组
                            # if not allDelTag:
                            #     groupNum=group.getElementsByTagName("groupNum")[0].firstChild.data
                            #     groupInfor=self.readGroup(groupNum)

                            self.debug.dLog("删除按钮执行成功")
                        except:
                            self.debug.dWarning("删除按钮执行失败")
                        return True

    def addButtonInNewGroup(self, button):
        """
            用户通过一定的方法来添加磁贴
            如果有同名的，看文件的路径
            此方法是添加未知组的，添加到第一列，最后一个组中
            :param button:参数是一个ButtonInfor()类型的对象
            :return: 返回值是一个int代码，返回0表示成功，返回1表示未知错误，返回2表示重复添加
        """
        # 检测是否有重复添加
        if self.__isRepeatingButton(button.buttonRunPath):
            return 2

        try:
            li = self.root.getElementsByTagName('list')[0]
            groups = li.getElementsByTagName("group")

            # 获取最大的组
            newGroup = None
            maxNum = 11  # 最大的组个数
            buX = ""  # 新按钮的位置
            buY = ""
            for gr in groups:
                num = int(gr.getAttribute("groupNum"))
                # 获取最大的组号
                if num >= maxNum:
                    newGroup = gr
                    maxNum = num + 1

            # 已经存在的组的个数小于三,新建组，否则用上边的newGroup
            if maxNum <= 13:
                # 新建组
                newGroup = self.dom.createElement("group")
                li.appendChild(newGroup)
                newGroup.attributes['groupNum'] = str(maxNum)
                newGroup.attributes['groupName'] = ''
                buX = "1"
                buY = "0"

            else:
                return 1
                # 如果不新建组，需要计算新按钮在组中的位置
                buX, buY = self.__getNewButtonXY(newGroup)
                '''
                    如果不新建组，需要计算新的按钮高度
                '''
            newButton = self.__fillButton(button, buX, buY)
            newGroup.appendChild(newButton)

            self.__saveData()
            self.debug.dLog("按钮添加成功", 3005)

        except:
            self.debug.dWarning("按钮（磁贴）添加失败", 3015)

    def addButtonInOldGroup(self, button, groupNum):
        """
            :param button: 新添加的按钮,buttonInfor类型
            :param groupNum: 需要添加的组
            :return: 返回0表示成功，返回2表示重复
        """
        # 检测是否有重复添加
        if self.__isRepeatingButton(button.buttonRunPath):
            return 2
        lists = self.root.getElementsByTagName("list")
        for li in lists:
            groups = li.getElementsByTagName("group")
            for group in groups:
                domGroupNum = group.getAttribute("groupNum")
                if groupNum == domGroupNum:
                    self.debug.dLog("查找到组")
                    try:
                        buX, buY = self.__getNewButtonXY(group)
                        newButton = self.__fillButton(button, buX, buY)
                        group.appendChild(newButton)
                        self.__saveData()
                        self.debug.dLog("向" + groupNum + "中添加磁贴成功")
                    except:
                        self.debug.dWarning("向" + groupNum + "中添加磁贴失败")

    def alterGroupName(self, groupNum, newGroupName):
        """
            :param groupNum: 需要修改的组编号（三位）
            :param newGroupName: 组的新名字
        """
        try:
            lists = self.root.getElementsByTagName('list')
            for li in lists:
                groups = li.getElementsByTagName('group')
                for gr in groups:
                    if gr.getAttribute("groupNum") == groupNum:
                        gr.setAttribute('groupName', newGroupName)
                        self.__saveData()
                        self.debug.dLog("groupNum 修改完毕", 3004)
                        return
        except:
            self.debug.dWarning("groupNum 修改错误", 3014)

    def readXML(self):
        """
            将整个数据树返回，其返回值是一个OSInfor()类的对象，其中包括所有的数据
            :return: OSInfor()
        """
        osInfor = OSInfor()
        try:

            osInfor.screenHeight = self.root.getElementsByTagName('screenHeight')[0].firstChild.data
            osInfor.screenWidth = self.root.getElementsByTagName('screenWidth')[0].firstChild.data
            osInfor.shouldListCount = self.root.getElementsByTagName('shouldListCount')[0].firstChild.data
            osInfor.hasListCount = self.root.getElementsByTagName('hasListCount')[0].firstChild.data

            # 嵌套循环读取数据
            lists = self.root.getElementsByTagName('list')
            for li in lists:
                groups = li.getElementsByTagName('group')
                listInfor = ListInfor(li.getAttribute("colNum"))
                for group in groups:
                    buttons = group.getElementsByTagName('button')
                    groupInfor = GroupInfor(group.getAttribute("groupNum"), group.getAttribute("groupName"))
                    for button in buttons:
                        buttonInfor = ButtonInfor(
                            button.getElementsByTagName('buttonName')[0].firstChild.data,
                            button.getElementsByTagName('buttonType')[0].firstChild.data,
                            button.getElementsByTagName('buttonRunPath')[0].firstChild.data,
                            int(button.getElementsByTagName('buttonX')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonY')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonW')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonH')[0].firstChild.data))
                        groupInfor.buttons.append(buttonInfor)
                    listInfor.groups.append(groupInfor)
                osInfor.listS.append(listInfor)

        except:
            self.debug.dWarning("xml文件读取错误", 3011)
        self.debug.dLog("readXML over", 3001)

        return osInfor

    def readGroup(self, groupNum):
        """
        通过组号查找组内容，返回的是一个GroupInfor()类型的数据
        :param groupNum:
        :return:
        """
        groupInfor = GroupInfor(groupNum)

        lists = self.root.getElementsByTagName("list")
        for li in lists:
            groups = li.getElementsByTagName("group")
            for gr in groups:
                if gr.getAttribute("groupNum") == groupNum:
                    groupInfor.groupName = gr.getAttribute("groupName")
                    buttons = gr.getElementsByTagName("button")
                    for button in buttons:
                        buttonInfor = ButtonInfor(
                            button.getElementsByTagName('buttonName')[0].firstChild.data,
                            button.getElementsByTagName('buttonType')[0].firstChild.data,
                            button.getElementsByTagName('buttonRunPath')[0].firstChild.data,
                            int(button.getElementsByTagName('buttonX')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonY')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonW')[0].firstChild.data),
                            int(button.getElementsByTagName('buttonH')[0].firstChild.data))
                        groupInfor.buttons.append(buttonInfor)
                    return groupInfor

        return groupInfor

    def __isRepeatingButton(self, buttonPath):
        """
            在添加按钮的时候需要检测是否重复
            :param buttonPath: 新建的按钮程序路径
            :return: 返回bool值,True表示有重复的
        """
        data = self.readXML()
        lists = data.listS
        for li in lists:
            groups = li.groups
            for gr in groups:
                buttons = gr.buttons
                for bu in buttons:
                    if bu.buttonRunPath == buttonPath:
                        return True
        return False

    def __getNewButtonXY(self, group):
        """
            传入一个xml的节点，根节点是group，然后读取其中的按钮排列，最后给出新按钮需要放置的位置
        :param group: 一个xml节点
        :return: 返回X,Y（返回前需要将其转为str类型
        """
        buX = 0
        buY = 0
        # arr=list()
        # arr = [[0, 0, 0, 0, 0, 0]] * 200
        # 六列两百行的数组
        arr = [([0] * 6) for _ in range(200)]
        buttons = group.getElementsByTagName("button")
        for button in buttons:
            """遍历所有按钮"""

            x = int(button.getElementsByTagName('buttonX')[0].firstChild.data)
            y = int(button.getElementsByTagName('buttonY')[0].firstChild.data)
            w = int(button.getElementsByTagName('buttonW')[0].firstChild.data)
            h = int(button.getElementsByTagName('buttonH')[0].firstChild.data)

            for i in range(w):
                for j in range(h):
                    arr[x + j][y + i] = 1

        for i in range(1, 198, 1):
            for j in range(0, 5, 1):
                if arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1] == 0:
                    return str(i), str(j)

    def __fillButton(self, button, buX, buY):
        """
        用于创建按钮节点，代码复用
        :param button:参数是一个ButtonInfor()类型的对象
        :param buX:新建按钮的x位置
        :param buY:新建按钮的y位置
        :return: 返回的是一个dom节点
        """

        # 新建按钮节点
        newButton = self.dom.createElement("button")
        # 构建按钮属性
        buttonName = self.dom.createElement("buttonName")
        buttonType = self.dom.createElement("buttonType")
        buttonRunPath = self.dom.createElement("buttonRunPath")
        buttonW = self.dom.createElement("buttonW")
        buttonH = self.dom.createElement("buttonH")
        buttonX = self.dom.createElement("buttonX")
        buttonY = self.dom.createElement("buttonY")

        # 按钮下添加节点
        newButton.appendChild(buttonName)
        newButton.appendChild(buttonType)
        newButton.appendChild(buttonRunPath)
        newButton.appendChild(buttonW)
        newButton.appendChild(buttonH)
        newButton.appendChild(buttonX)
        newButton.appendChild(buttonY)

        # 填充按钮属性
        buttonName.appendChild(self.dom.createTextNode(button.buttonName))
        buttonType.appendChild(self.dom.createTextNode(button.buttonType))
        buttonRunPath.appendChild(self.dom.createTextNode(button.buttonRunPath))
        buttonW.appendChild(self.dom.createTextNode("2"))
        buttonH.appendChild(self.dom.createTextNode("2"))
        buttonX.appendChild(self.dom.createTextNode(buX))
        buttonY.appendChild(self.dom.createTextNode(buY))

        return newButton
