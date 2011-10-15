from __future__ import division
from Output import *
import os
from fuquan import *
from GenerateFuQuanInfo import *
def resetfilePointertoHead(FilePointer):
    FilePointer.seek(0)
    return

def GetOneDayContent(FilePointer):
    return FilePointer.read(32)

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
    return getElementFromrecordLine(recordline, 16, 20)


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
        return 0
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

def Percentage(starttime, endtime, filepointer, fuquanfilepointer = []):
    start_record = findMatchedTimeRecord(filepointer,starttime)
    end_record   = findMatchedTimeRecord(filepointer, endtime)
    if start_record <> []:
        if end_record <> []:
            end_price = getEndPrice(end_record)
            start_price = getEndPrice(start_record)
            if(fuquanfilepointer <> []):
                start_price = getFuquanedPrice_fromFile(starttime, endtime, filepointer, fuquanfilepointer)
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
                print "Creating Fuquan file:" + fuquanfilename
                CreateFquanByStockID(stockid)
                fuquanpointer = open(fuquanfilename, 'r')
            per = Percentage(starttime, endtime, KDayfilepointer, fuquanpointer)
            result.append([i, per])
        else:
            result.append([i, []])
    return result



def GetSortedTable(inputtable):
    return sorted(inputtable, key = lambda per:per[1])
