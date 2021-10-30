import os

from util.json_util import json2dict


class FileIndex:
    def __init__(self, dirPath):
        self.dirPath = dirPath
        # 解析配置文件
        self._getConfig()
        self.files = []
        self._findFile(self.dirPath)

    def _getConfig(self):
        jsonDirFile = "config/"
        self.db_config = json2dict("db_config.json", jsonDirFile)
        print(self.db_config)

        self.file_manage = json2dict("file_manage.json", jsonDirFile)
        print(self.file_manage)

    def _findFile(self, dirPath):
        fileList = os.listdir(dirPath)
        for file in fileList:
            filePath = dirPath + "/" + file
            if os.path.isdir(filePath):
                self._findFile(filePath)
            else:
                self.files.append(filePath)

    def _buildFileIndex(self):
        pass

    def searchFile(self):
        pass

    def searchDir(self):
        pass

    def searchContext(self):
        pass

    def listGroupByDir(self):
        """
        按文件目录排列文件
        :return:
        """
        pass

    def listGroupByFileType(self):
        """
        按文件类型排列文件
        :return:
        """
        pass

    def listGroupByTime(self):
        """
        按周、月、年排列文件
        :return:
        """
        pass

    def moveFile(self):
        """
        移动文件
        :return:
        """
        pass

    def removeFile(self):
        """
        删除文件
        :return:
        """
        pass

    def recoveryFile(self):
        """
        恢复文件
        :return:
        """
        pass


if __name__ == '__main__':
    dirPath = "/Users/zyw/test"
    fileIndex = FileIndex(dirPath)
    print(fileIndex.files)
