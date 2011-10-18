from readDayRecord import *
import readBlock
import sys

startime = int(raw_input("start time:"))
endtime =  int(raw_input("end time:"))
StockID = raw_input("input stock id:")
filepname = readBlock.GetStockDayKFileNameFromCodeInBlock(StockID)
def findTopValue(group_day_K_record):
    sortit = sorted(group_day_K_record
    return
def extractPeriodRecord(startime, endtime,filepointer):
    resetfilePointertoHead(filepointer)
    oneday = GetOneDayContent(filepointer)
    result = []
    while len(oneday) <> 0:
        if getTime(oneday) >= startime and getTime(oneday) <= endtime:
            result.append(oneday)
        oneday = GetOneDayContent(filepointer)
    return result
if os.path.isfile(filepname):
    filepointer = open(filepname, 'rb')
    matchedRecord = extractPeriodRecord(startime, endtime, filepointer)
    for i in matchedRecord:
        trading_time = getTime(i)
        end_price = getEndPrice(i)
        print str(trading_time) + " : " + str(end_price)
