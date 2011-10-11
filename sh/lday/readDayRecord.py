from __future__ import division
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

def Percentage(starttime, endtime, filepointer):
    start_record = findMatchedTimeRecord(filepointer,starttime)
    end_record   = findMatchedTimeRecord(filepointer, endtime)
    if start_record <> []:
        if end_record <> []:
            end_price = getEndPrice(end_record)
            print "got end time price" + str(end_price)
            start_price = getEndPrice(start_record)
            print "got start time price" + str(start_price)
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
        filepointer = open(i, 'rb')
        per = Percentage(starttime, endtime, filepointer)
        result.append([i, per])
    return result



def GetSortedTable(inputtable):
    return sorted(inputtable, key = lambda per:per[1])
recordfile = open('sh600000.day', 'rb')
resetfilePointertoHead(recordfile)
firstline = GetOneDayContent(recordfile)
print getTime(firstline)
print getStartPrice(firstline)
print getHighestPrice(firstline)
print getLowestPrice(firstline)
print getEndPrice(firstline)
firstline = GetOneDayContent(recordfile)
print getTime(firstline)
print "pufayinhang 20110824"
found = findMatchedTimeRecord(recordfile, 20110824)
if found == []:
    print "no found any record"
else:
    print getEndPrice(found)


print "percentage of 20110824-20110930 is: "
print Percentage(20110824, 20110930, recordfile)
startime = int(raw_input("start time: 20110830:"))
endtime = int(raw_input("end time:20110830:"))
print Percentage(startime, endtime, recordfile)
groupresult = GroupPercentage(startime, endtime, ["sh600000.day", "sh999999.day"])
sortedgroup = GetSortedTable(groupresult)
for i in sortedgroup:
    print i[0]
    print i[1]
