from __future__ import division
from readDayRecord import *
def getListofStockFromBlockFile(filename):
    """input is a filename, it is like DL.blk  
        output is an list, content is an stock code list
    """
    f = open(filename, 'r')
    codelist = []
    for i in f.readlines():
        if len(i) == 8:
            codelist.append(i[0:7])#remove last \n
    return codelist

def FindShenzhenMarketDayKFolder():
    return "sz\\lday\\"
def FindShanghaiMarketDayKFolder():
    return 'sh\\lday\\'

def GetStockDayKFileNameFromCodeInBlock(code):
    filename = ''
    if(code[0] == '0'):
        filename = FindShenzhenMarketDayKFolder() + 'sz' + code[1:] + '.day'
    else:
        #shanghai market
        filename = FindShanghaiMarketDayKFolder() + 'sh' + code[1:] + '.day'
    return filename
def GetStockIDFromCodeInBlock(code):
    stockid = code[1:]
    return stockid
def GetStockIDGroupKFromBlockFile(BlockFileName):
    f = open(BlockFileName, 'r')
    codelist = getListofStockFromBlockFile(BlockFileName)
    StockIDGroup = []
    for i in StockIDGroup:
        k = GetStockIDFromCodeInBlock(i)
        StockIDGroup.append(k)
    return StockIDGroup
def GetDayKFileNameGroupFromBlockFile(BlockFileName):
    f = open(BlockFileName, 'r')
    codelist = getListofStockFromBlockFile(BlockFileName)
    DayKFileNameGroup = []
    for i in codelist:
        k = GetStockDayKFileNameFromCodeInBlock(i)
        DayKFileNameGroup.append(k)
    return DayKFileNameGroup
def GetBlockSortTable(startime, endtime, BlockFileNameGroup):
    result = []
    for i in BlockFileNameGroup:
        result.append([i, GetBlockIndexAverage(startime, endtime, i)])
    return result
def GetBlockIndexAverage(startime, endtime, BlockFileName):
    groupresult = readDayRecord.GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('..\\T0002\\blocknew\\' + BlockFileName))
    counter  = len(groupresult)
    if counter == 0:
        return 'N/A'
    sum = 0
    for i in groupresult:
        if i[1] == []:
            counter = counter - 1
        else:
            sum = sum + i[1]
    average = (sum/counter)//1
    return average
