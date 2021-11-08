'''
    用于读写用户数据的（界面数据

'''
import os
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from Class.dataInforClass import *
from Class.debug import Debug


class DataIO:
    def __init__(self):
        self.debug = Debug("DataIO")
        self.dataFile = os.getcwd() + "/Data/userData.xml"

        # 如果不存在数据文件，需要创建一个。
        if not os.path.exists(self.dataFile):
            try:
                root = ET.Element('Root')  # 创建节点
                tree = ET.ElementTree(root)  # 创建文档
                tree.write(self.dataFile, encoding='utf-8', xml_declaration=True)

                self.debug.dLog(" 数据文件初始化完成", 3001)
            except:
                self.debug.dWarning("文件初始化错误")

    # 输入的程序名字，绝对路径，类型（exe,lnk)
    def writeXML(self, fileName, filePath, fileType):
        data = [fileName, filePath, fileType]  # 需要写入的数据
        with open(self.dataFile, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            self.debug.dLog(" 数据文件写入完成", 3002)

    def addGroup(self):
        pass

    def addButton(self):
        pass

    # 这里返回的是整个tree？还是单个的？？？？
    '''
        [“节点号”：xx,“节点位置”：[x,y],"节点名字"：xx,节点按钮组：[x,x,x,]]*N
        
        按钮组里面又有{}
        
    '''

    def readXML(self):
        osInfor = OSInfor()
        try:

            dom = minidom.parse(self.dataFile)  # 读取文档
            root = dom.documentElement  # 获取根节点
            osInfor.screenHeight = root.getElementsByTagName('screenHeight')[0].firstChild.data
            osInfor.screenWidth = root.getElementsByTagName('screenWidth')[0].firstChild.data
            osInfor.shouldListCount = root.getElementsByTagName('shouldListCount')[0].firstChild.data
            osInfor.hasListCount = root.getElementsByTagName('hasListCount')[0].firstChild.data

            # 嵌套循环读取数据
            lists = root.getElementsByTagName('list')
            for li in lists:
                groups = li.getElementsByTagName('group')
                listInfor = ListInfor(li.getAttribute("colNum"))
                for group in groups:
                    buttons = group.getElementsByTagName('button')
                    groupInfor = GroupInfor(group.getAttribute("groupNum"))
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
        self.debug.dLog("readXML over", 3003)

        return osInfor
