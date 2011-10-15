#-*-coding:GB2312-*-
import urllib
import re
import csv
def extractFQRecordFromWeb(linestr):
    result = []
    free = 0
    gift = 0
    bonus = 0
    tradingtime = 0
    #report time
    tmp = extractOneline(linestr, 'td')
    tmp = extractOneline(tmp[1], 'td')
    if(tmp[0] == [] or tmp[0] == '\0'):#not found effective value
        return [tradingtime, free, gift, bonus, 0, 0]
    free = float(tmp[0])/10.0
    tmp = extractOneline(tmp[1], 'td')
    gift = float(tmp[0])/10.0
    tmp = extractOneline(tmp[1], 'td')
    bonus = float(tmp[0])/10.0
    tmp = extractOneline(tmp[1], 'td')
    #trading time
    tmp = extractOneline(tmp[1], 'td')
    if tmp[0] == '--':
        tradingtime = 0
    else:
        tradingtime = int(tmp[0][:4] + tmp[0][5:7] + tmp[0][8:10])
    return [tradingtime, free, gift, bonus, 0, 0]
def extractOneline(linestr, mark):
    first = linestr.find(mark)
    first_extract_position = len(mark)+1 + first
    second = linestr[first_extract_position:].find(mark)
    return (linestr[first_extract_position:first_extract_position+ second-2], linestr[first_extract_position+ second+3:])
def CreateFquanByStockID(stockid):
    urlitem = urllib.urlopen("http://money.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/" + stockid + ".phtml")
    htmlsource = urlitem.read()
    fenghong_String = 'sharebonus_1'
    Peigu_String = 'sharebonus_2'

    stdtcsv = open('fq\\' + stockid + ".csv", 'w')
    FQWriter = csv.writer(stdtcsv)
    StartFromFenghong = htmlsource[htmlsource.find(fenghong_String):]
    end_position_fenghong = StartFromFenghong.find('table')
    fenghong = StartFromFenghong[0: end_position_fenghong]
    end_thead = fenghong.find('tbody')
    removedThread = fenghong[end_thead + len('tbody'):]
    firstline = extractOneline(removedThread, 'tr')
    singlerow =  extractFQRecordFromWeb(firstline[0])
    FQWriter.writerow(map(str, singlerow))
    recordNumber = removedThread.count('tr')/2
    recordNumber = recordNumber - 1
    while recordNumber > 0:
        """
        firstline = extractOneline(removedThread, 'tr')
        singlerow =  extractFQRecordFromWeb(firstline[0])
        FQWriter.writerow(map(str, singlerow))
        """
        firstline = extractOneline(firstline[1], 'tr')
        singlerow =  extractFQRecordFromWeb(firstline[0])
        FQWriter.writerow(map(str, singlerow))
        recordNumber = recordNumber - 1
    stdtcsv.close()
    return

"""
stockid = raw_input("input stock id:")
urlitem = urllib.urlopen("http://money.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/" + stockid + ".phtml")
htmlsource = urlitem.read()
fenghong_String = 'sharebonus_1'
Peigu_String = 'sharebonus_2'

stdtcsv = open(stockid + ".csv", 'w')
FQWriter = csv.writer(stdtcsv)
StartFromFenghong = htmlsource[htmlsource.find(fenghong_String):]
end_position_fenghong = StartFromFenghong.find('table')
fenghong = StartFromFenghong[0: end_position_fenghong]
end_thead = fenghong.find('tbody')
removedThread = fenghong[end_thead + len('tbody'):]
firstline = extractOneline(removedThread, 'tr')
singlerow =  extractFQRecordFromWeb(firstline[0])
FQWriter.writerow(map(str, singlerow))
firstline = extractOneline(firstline[1], 'tr')
singlerow =  extractFQRecordFromWeb(firstline[0])
FQWriter.writerow(map(str, singlerow))
stdtcsv.close()
StartFromPeigu= htmlsource[htmlsource.find(Peigu_String):]
end_position_peigu= StartFromPeigu.find('table')
print end_position_peigu
print StartFromPeigu[0:end_position_peigu]
"""
CreateFquanByStockID('000562')
