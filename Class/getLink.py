import os


class GetLink:
    def __init__(self, filePathAndName):
        self.filePathAndName = filePathAndName  # 这个path包含路径，文件名，文件后缀,应该是个绝对路径
        self.filepath, self.fileNameAndExt = os.path.split(filePathAndName)
        self.fileName, self.fileExt = os.path.splitext(self.fileNameAndExt)
