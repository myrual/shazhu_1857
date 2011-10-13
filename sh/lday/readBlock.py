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
def GetDayKFileNameGroupFromBlockFile(BlockFileName):
    f = open(BlockFileName, 'r')
    codelist = getListofStockFromBlockFile(BlockFileName)
    DayKFileNameGroup = []
    for i in codelist:
        print i + " : " 
        k = GetStockDayKFileNameFromCodeInBlock(i)
        print k
        DayKFileNameGroup.append(k)
    return DayKFileNameGroup
def GetBlockSortTable(startime, endtime, BlockFileNameGroup):
    result = []
    for i in BlockFileNameGroup:
        result.append([i, GetBlockIndexAverage(startime, endtime, i)])
    return result
def GetBlockIndexAverage(startime, endtime, BlockFileName):
    print BlockFileName
    groupresult = GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('..\\T0002\\blocknew\\' + BlockFileName))
    print groupresult
    counter  = len(groupresult)
    if counter == 0:
        return 'N/A'
    sum = 0
    for i in groupresult:
        print i[0]
        print i[1]
        if i[1] == []:
            counter = counter - 1
        else:
            sum = sum + i[1]
    print "sum is " + str(sum)
    print "counter is " + str(counter)
    average = (sum/counter)//1
    return average
