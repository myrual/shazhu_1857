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
    return 'sz'
def FindShanghaiMarketDayKFolder():
    return ''

def GetStockDayKFileNameFromCodeInBlock(code):
    filename = ''
    if(code[0] == '0'):
        filename = "sz" + code[1:] + '.day'
    else:
        #shanghai market
        filename = 'sh' + code[1:] + '.day'
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
