import datetime
import time

FORMAT_DATE = "%Y-%m-%d"
FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
FORMAT_TIME = "%H:%M:%S"

FORMAT_NUM_DATE = "%Y%m%d"
FORMAT_NUM_DATETIME = "%Y%m%d%H%M%S"
FORMAT_NUM_TIME = "%H%M%S"


def getNowTime():
    return datetime.datetime.now()


def getYesterdayOnNowTime():
    return (datetime.datetime.now() - datetime.timedelta(days=1))


def addDayOnNowTime(days=0):
    return datetime.datetime.now() + datetime.timedelta(days=days)


def getNowTimeStr(format=FORMAT_DATE):
    return datetime.datetime.now().strftime(format)


def getYesterdayOnNowTimeStr(format=FORMAT_DATE):
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(format)


def addDayOnNowTimeStr(days=0, format=FORMAT_DATE):
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime(format)


def getDateTimeNumStr(dateTime=datetime.datetime.now()):
    return dateTime.strftime(FORMAT_NUM_DATETIME)


def getDateNumStr(dateTime=datetime.datetime.now()):
    return dateTime.strftime(FORMAT_NUM_DATE)


def getTimeNumStr(dateTime=datetime.datetime.now()):
    return dateTime.strftime(FORMAT_NUM_TIME)


def second2DateTime(dateSecond):
    return str2DateTime(time.strftime(FORMAT_DATETIME, time.localtime(dateSecond)))


def str2DateTime(dateTimeStr, format=FORMAT_DATETIME):
    return datetime.datetime.strptime(dateTimeStr, format)


def dateTime2Second(dateTime):
    return dateTime.timestamp()


def dateTime2Str(dateTime, format=FORMAT_DATETIME):
    return dateTime.strftime(format)


if __name__ == '__main__':
    print(getNowTime())
    print(getYesterdayOnNowTime())
    print(addDayOnNowTime(-7))
    print(getNowTimeStr(format=FORMAT_DATETIME))
    print(getYesterdayOnNowTimeStr())
    print(addDayOnNowTimeStr(-7))
    print(getDateTimeNumStr())
    print(getDateNumStr())
    print(getTimeNumStr())
    curDateTime = getNowTime()
    curDateTimeSecond = dateTime2Second(curDateTime)
    print(second2DateTime(curDateTimeSecond))
    print(str2DateTime("2021-07-09 10:30:30", format=FORMAT_DATETIME))
    print(dateTime2Second(curDateTime))
    print(dateTime2Str(curDateTime))
