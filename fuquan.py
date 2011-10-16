# coding=utf-8
import readDayRecord
import csv
"""

"""    

STDTFQinfo = [[20110617, 0.3, 0, 0.6, 0, 0],
        [20100617, 0.3, 0, 0.6, 0, 0],
        [20090617, 0.3, 0, 0.6, 0, 0],
        [20080617, 0.3, 0, 0.6, 0, 0],
        [20070617, 0.3, 0, 0.6, 0, 0]]

def GetMatchedFuquanFromWholeFuquan(starttime, endtime, WholeFuquanData):
    recordNumber = len(WholeFuquanData)
    if len(WholeFuquanData) == 0:
        return []
    part1 = []
    part2 = []
    for i in WholeFuquanData:
        if i[0] < endtime:
            part1.append(i)

    for i in part1:
        if i[0] > starttime:
            part2.append(i)
    #part2 is Fuquan info between start and endtime
    return part2
def SingleFuqian_Forward(FQinfo, filepointer):
    """FQinfo is : [time(trade time), free(how many), gift(How many), bonus(how much), cheaper_price(how much), cheaper_count(how many)]
    """
    earlierprice = readDayRecord.GetYesterDayEndPrice(filepointer, FQinfo[0])
    bonus = FQinfo[3]
    free = FQinfo[1]
    gift = FQinfo[2]
    cheaper_price = FQinfo[4]
    cheaper_count = FQinfo[5]
    print "earlieprice is :" + str(earlierprice)
    print "bonus is: " + str(bonus)
    fq_1 = (earlierprice - bonus)
    print "fq_1" + str(fq_1)
    fq_2 = (fq_1)/(1 + free + gift) 
    print "fq_2" + str(fq_2)
    fq_3 = ((fq_2) + cheaper_price*cheaper_count)/(1+cheaper_count)
    return fq_3/earlierprice 
def periodFuquan_factor_Forward(FQPeriodTable, filepointer):
    result  = 1.0
    if FQPeriodTable == []:
        return 1
    if type(FQPeriodTable[0]) == type([]):
        for i in FQPeriodTable:
            result = result * SingleFuqian_Forward(i, filepointer)
    else:
        result = result * SingleFuqian_Forward(FQPeriodTable, filepointer)
    return result
def GetFuquanedPrice(starttime, endtime, Kdayfilepointer, WholeFuquanInfo):
    matchFuquanTable = GetMatchedFuquanFromWholeFuquan(starttime, endtime, WholeFuquanInfo)
    index = periodFuquan_factor_Forward(matchFuquanTable, Kdayfilepointer)
    print "index is :" + str(index)
    return readDayRecord.getEndPrice(readDayRecord.findMatchedTimeRecord(Kdayfilepointer, starttime))* index
def getFuquanedPrice_fromFile(starttime, endtime, Kdayfilepointer, fuquanfilepointer):
    FullFQInfo = GetFuquanInfoFromFile(fuquanfilepointer)
    print FullFQInfo
    return GetFuquanedPrice(starttime, endtime, Kdayfilepointer, FullFQInfo)
#print periodFuquan_factor_Forward(STDTFQinfo)
def GetFuquanInfoFromFile(filenpointer):
    FQReader = csv.reader(filenpointer)

    result = []
    for row in FQReader:
        result.append(map(float, row))
    return result
"""
print GetMatchedFuquanFromWholeFuquan(20050930, 20110430, STDTFQinfo)
print GetMatchedFuquanFromWholeFuquan(20050930, 20110430, [])
print GetMatchedFuquanFromWholeFuquan(20050930, 20110930, [[20110617, 0.3, 0, 0.6, 0, 0]])
KdayFileName = 'sh\\lday\\sh600497.day'
filepointer = open(KdayFileName, 'rb')
print periodFuquan_factor_Forward(GetMatchedFuquanFromWholeFuquan(20090930, 20110930, STDTFQinfo), filepointer)
fqfilename = raw_input("input fuquan file name:")
FullFQInfo = GetFuquanInfoFromFile(open(fqfilename + '.csv'))
print "Full fuquan info is :"
print FullFQInfo
print GetFuquanedPrice(20110524, 20110930, filepointer, FullFQInfo)
"""
