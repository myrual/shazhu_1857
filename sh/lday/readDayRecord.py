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
    print getHighestPrice(found)
