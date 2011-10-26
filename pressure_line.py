from __future__ import division
import readDayRecord
EndPriceList = [12,13,14,15,10,10,7,11,13,9,8,10]
x1 = 2
x2 = 4
y1 = EndPriceList[x1]
y2 = EndPriceList[x2]
k = (y2-y1)/(x2-x1)
d = y2-k*x2
def GetKDfrom2Point(x1, x2, Ylist):
    if len(Ylist) == 0 or len(Ylist) == 1:
        return [0, 0]
    y1 = Ylist[x1]
    y2 = Ylist[x2]
    k = (y2-y1)/(x2-x1)
    d = y2-k*x2
    return [k, d]

def IsKDCoverAll(Ylist, k, d, DownUp):
    count = len(Ylist)
    if count == 0:
        return "false"
    for i in range(0, count):
        realY = Ylist[i]
        CalY = k*i + d
        if realY >= CalY and DownUp == "Down":
            return "false"
        if realY <= CalY and DownUp == "Up":
            return "false"

    return "true"
def GetYValue(k, d, x):
    return k*x +d
def FindPeakValue(Ylist, HighOrLow):
    return Ylist[FindPeakValueIndex(Ylist, HighOrLow)]
def FindPeakValueIndex(Ylist, HighOrLow):
    i = 0
    peak = Ylist[0]
    for j in range(1, len(Ylist)):
        if Ylist[j] >= peak and HighOrLow == "High":
            i = j
            peak = Ylist[j]
        if Ylist[j] <= peak and HighOrLow == "Low":
            i = j
            peak = Ylist[j]
    return i
[k, d] = GetKDfrom2Point(0, 4, EndPriceList)

def FoundKD_DownLine_seperate(Ylist):
    TopIndex = FindPeakValueIndex(Ylist, "High")
    toDoYlist = Ylist[TopIndex:]
    count = len(toDoYlist)
    for i in range(1, count):
        [k, d] = GetKDfrom2Point(0, i, toDoYlist)
        result = IsKDCoverAll(toDoYlist[1:], k, d, "Down")
        if result == "true":
            print "found k: " + str(k) +  "and d: " + str(d)
            return [k, d]
    return [0, 0]

def FoundKD_Line(Ylist, Peak, DownUp):
    TopIndex = FindPeakValueIndex(Ylist, Peak)
    if TopIndex == 0:
        toDoYlist = Ylist
    else:
        toDoYlist = Ylist[TopIndex:]
    count = len(toDoYlist)
    for i in range(1, count):
        [k, d] = GetKDfrom2Point(0, i, toDoYlist)
        result = IsKDCoverAll(toDoYlist[1:], k, d, DownUp)
        if result == "true":
            return [k, d, TopIndex]
    return [0, 0, 0]
def FoundKD_UpLine(Ylist):
    return FoundKD_Line(Ylist, "Low", "Up")

def FoundKD_DownLine(Ylist):
    return FoundKD_Line(Ylist, "High", "Down")
def GetDownPressureValue(Ylist, tday):
    [k, d, DownStartIndex] = FoundKD_DownLine(Ylist)
    if [k, d] == [0, 0]:
        print "failed to calc pressure for the input value"
        print Ylist
        return []
    return k*(len(Ylist[DownStartIndex:]) + tday) + d

def GetUpPressureValue(Ylist, tday):
    [k, d, DownStartIndex] = FoundKD_UpLine(Ylist)
    if [k, d] == [0, 0]:
        print "failed to calc pressure for the input value"
        print Ylist
        return []
    return k*(len(Ylist[DownStartIndex:]) + tday) + d
def GetUpPressureValue_ByStockID(stockid, starttime, endtime, nextdayoffset):
    end_price_group =  readDayRecord.GetGroupEndPrice(starttime, endtime, stockid)
    nexday_pressvalue = GetUpPressureValue(end_price_group, nextdayoffset)
    return nexday_pressvalue

def GetDownPressureValue_ByStockID(stockid, starttime, endtime, nextdayoffset):
    end_price_group =  readDayRecord.GetGroupEndPrice(starttime, endtime, stockid)
    nexday_pressvalue = GetDownPressureValue(end_price_group, nextdayoffset)
    return nexday_pressvalue
stockid = raw_input("input stockid:")

startday = int(raw_input("input start time"))
endday = int(raw_input("input end day:"))
nextday = int(raw_input("input how many days you want to know press value from end day:"))
print "downline pressure:" + str(GetDownPressureValue_ByStockID(stockid, startday, endday, nextday))
print "upline pressure:" + str(GetUpPressureValue_ByStockID(stockid, startday, endday, nextday))
"""

BottonIndex = FindPeakValueIndex(EndPriceList, "Low")
toDoDownList = EndPriceList[BottonIndex:]
[k, d] = GetKDfrom2Point(0, 1, toDoDownList)
print IsKDCoverAll(toDoDownList[1:], k, d, "Up")
"""
