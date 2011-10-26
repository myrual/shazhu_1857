from __future__ import division
from Output import *
import os
from fuquan import *
from GenerateFuQuanInfo import *
def resetfilePointertoHead(FilePointer):
    FilePointer.seek(0)
    return

TDX_One_Day_Record_Len = 32
def GetOneDayContent(FilePointer):
    return FilePointer.read(TDX_One_Day_Record_Len)

def Convert4ByteString2Int(timestring):
    result = ord(timestring[0]) + ord(timestring[1])*0x100 + ord(timestring[2])*0x10000 + ord(timestring[3])*0x1000000
    return result

def getElementFromrecordLine(inputLine, startOffset, endOffset):
    element = inputLine[startOffset: endOffset]
    result = Convert4ByteString2Int(element)
    return result
def getTime(recordline):
    length_of = len(recordline)
    return getElementFromrecordLine(recordline, 0, 4)
def getStartPrice(recordline):
    return getElementFromrecordLine(recordline, 4, 8)
def getHighestPrice(recordline):
    return getElementFromrecordLine(recordline, 8, 12)
def getLowestPrice(recordline):
    return getElementFromrecordLine(recordline, 12, 16)
def getEndPrice(recordline):
    return getElementFromrecordLine(recordline, 16, 20)/100


def findYesterDayRecord(filepointer, inputtime):
    resetfilePointertoHead(filepointer)
    oneday = GetOneDayContent(filepointer)
    Yesterday = oneday
    i = 1
    while len(oneday) <> 0:
        if getTime(oneday) == inputtime:
            #yesterday record is the price before fuquan happen
            oneday = GetOneDayContent(filepointer)
            return Yesterday
        Yesterday = oneday
        oneday = GetOneDayContent(filepointer)
        i = i + 1
    print "no found match record" + "with " + str(i) + "attem"
    return []

def GetYesterDayEndPrice(filepointer, inputtime):
    record = findYesterDayRecord(filepointer, inputtime)
    if record == []:
        return []
    else:
        return getEndPrice(record)
def findMatchedTimeRecord(filepointer, inputtime):
    resetfilePointertoHead(filepointer)
    oneday = GetOneDayContent(filepointer)
    i = 1
    while len(oneday) <> 0:
        if getTime(oneday) == inputtime:
            return oneday
        oneday = GetOneDayContent(filepointer)
        i = i + 1
    print "no found match record" + "with " + str(i) + "attem"
    return []

def findMatched_OrLastTimeRecordGroup(filepointer, inputtime, day_record_width):
    tmp = []
    resetfilePointertoHead(filepointer)
    oneday = GetOneDayContent(filepointer)
    while len(oneday) <> 0:
        if getTime(oneday) < inputtime:
            tmp.append(getTime(oneday))
            if len(tmp) > day_record_width:
                tmp.pop(0)
        if getTime(oneday) == inputtime:
            tmp.append(getTime(oneday))
            if len(tmp) > day_record_width:
                tmp.pop(0)
            break
        if getTime(oneday) > inputtime:
            print "not found: " + str(inputtime) + "in current file"
            break;
        oneday = GetOneDayContent(filepointer)
    return tmp
def findMatched_OrLastTimeRecord(filepointer, inputtime):
    resetfilePointertoHead(filepointer)
    oneday = GetOneDayContent(filepointer)
    i = 1
    tmp = []
    while len(oneday) <> 0:
        if getTime(oneday) < inputtime:
            tmp = oneday
        if getTime(oneday) == inputtime:
            return oneday
        oneday = GetOneDayContent(filepointer)
        i = i + 1
    print "no found match record" + "with " + str(inputtime) + "time"
    if tmp <> []:
        print "just found last trading time record with time: " + str(getTime(tmp))
    return tmp
def GetFileNameFromStockID(stockid):
    if stockid[0] == '6':
        stockid_in_block = '1'+stockid
    if stockid[0] == '0' or stockid[0] == '3':
        stockid_in_block = '0'+stockid
    filename = readBlock.GetStockDayKFileNameFromCodeInBlock(stockid_in_block)
    return filename
def GetFilePointerFromStockID(stockid):
    fname = GetFileNameFromStockID(stockid)
    filepointer = open(fname, 'rb')
    return filepointer
def GetGroupEndPrice(endtime, how_many_days, stockid):
    fpointer = GetFilePointerFromStockID(stockid)
    timelist = findMatched_OrLastTimeRecordGroup(fpointer, endtime, how_many_days)
    tmp = []
    for i in timelist:
        tmp.append(GetFuquanPrice_byStockID(i, endtime, stockid))
    return tmp
def GetFuquanPrice_byStockID(starttime, endtime, stockid):
    """stock id is an string like '600834'"""

    if stockid[0] == '6':
        stockid_in_block = '1'+stockid
    if stockid[0] == '0' or stockid[0] == '3':
        stockid_in_block = '0'+stockid
    filename = readBlock.GetStockDayKFileNameFromCodeInBlock(stockid_in_block)
    filepointer = open(filename, 'rb')
    fqfilename = 'fq\\' + stockid+'.csv'
    if os.path.isfile(fqfilename):
        fuquanfilepointer = open(fqfilename,'r')
    else:
        print "not found fuquan info: " + fqfilename
        fuquanfilepointer = []
    return getFuquanedPrice_fromFile(starttime, endtime, filepointer, fuquanfilepointer)
def Percentage_byStockID(starttime, endtime, stockid):
    """stock id is an string like '600834'"""

    if stockid[0] == '6':
        stockid_in_block = '1'+stockid
    if stockid[0] == '0' or stockid[0] == '3':
        stockid_in_block = '0'+stockid
    filename = readBlock.GetStockDayKFileNameFromCodeInBlock(stockid_in_block)
    filepointer = open(filename, 'rb')
    fqfilename = 'fq\\' + stockid+'.csv'
    if os.path.isfile(fqfilename):
        fuquanfilepointer = open(fqfilename,'r')
    else:
        print "not found fuquan info: " + fqfilename
        fuquanfilepointer = []
    return Percentage(starttime, endtime, filepointer, fuquanfilepointer)
def Percentage(starttime, endtime, filepointer, fuquanfilepointer = []):
    start_record = findMatchedTimeRecord(filepointer,starttime)
    end_record   = findMatched_OrLastTimeRecord(filepointer, endtime)
    if start_record <> []:
        if end_record <> []:
            end_price = getEndPrice(end_record)
            start_price = getEndPrice(start_record)
            if(fuquanfilepointer <> []):
                start_price = getFuquanedPrice_fromFile(starttime, endtime, filepointer, fuquanfilepointer)
                if start_price == []:
                    #if not found that time price
                    return []
            absvalue = abs(start_price - end_price)
            finalrate = absvalue/start_price
            finalrate = (finalrate * 100)//1
            if start_price < end_price:
                return finalrate
            else:
                return finalrate * -1
    return []

def GroupPercentage(starttime, endtime, filegroup):
    """ filegroup is: ["sh600000.day", "sh999999.day"]
    """
    result = []
    for i in filegroup:
        if os.path.isfile(i):
            KDayfilepointer = open(i, 'rb')
            stockid = i[-10:-4]
            fuquanfilename = 'fq\\' + stockid + '.csv'
            if os.path.isfile(fuquanfilename):
                fuquanpointer = open(fuquanfilename, 'r')
            else:
                #CreateFquanByStockID(stockid)
                fuquanpointer = []
            per = Percentage(starttime, endtime, KDayfilepointer, fuquanpointer)
            result.append([i, per])
        else:
            result.append([i, []])
    return result



def GetSortedTable(inputtable):
    return sorted(inputtable, key = lambda per:-1*per[1], reverse=False)
