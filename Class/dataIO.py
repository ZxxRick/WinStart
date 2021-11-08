'''
    用于读写用户数据的（界面数据

'''
import os
import csv
import xml.etree.ElementTree as ET
from Class.debug import Debug


class DataIO:
    def __init__(self):
        self.debug = Debug("DataIO")
        self.file = os.getcwd() + "/Data/userData.xml"

        # 如果不存在数据文件，需要创建一个。
        if not os.path.exists(self.file):
            try:
                root = ET.Element('Root')  # 创建节点
                tree = ET.ElementTree(root)  # 创建文档
                tree.write(self.file, encoding='utf-8', xml_declaration=True)
            except:
                self.debug.dWarning("文件初始化错误")

    # 输入的程序名字，绝对路径，类型（exe,lnk)
    def writeXML(self, fileName, filePath, fileType):
        data = [fileName, filePath, fileType]  # 需要写入的数据
        with open(self.file, 'a', newline="") as file:
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
            pass
