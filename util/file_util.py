import os

import filetype

FILE_TYPE_DIR = "DIR"
FILE_TYPE_FILE = "FILE"
FILE_TYPE_NOT_EXISTS = "NOT EXISTS"


def fileIfExists(path):
    return os.path.exists(path)


def getFileType(path):
    if not fileIfExists(path):
        return FILE_TYPE_NOT_EXISTS

    if os.path.isfile(path):
        return doFileType(path)

    if os.path.isdir(path):
        return FILE_TYPE_DIR

    return FILE_TYPE_NOT_EXISTS


def doFileType(path):
    kind = filetype.guess(path)
    if kind is None:
        print('Cannot guess file type!')
        return os.path.splitext(path)[-1].lower()

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    return kind.mime


if __name__ == '__main__':
    filetype = getFileType("/Users/zyw/Downloads/郎之万方程.gif")
    print(filetype)
