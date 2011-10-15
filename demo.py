from readDayRecord import *
from Output import *
recordfile = open('sh600834.day', 'rb')
resetfilePointertoHead(recordfile)
firstline = GetOneDayContent(recordfile)
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
    print InsertRow(i)
    print i[1]
outfile = open('percentage.html', 'w')
outfile.write(OutputHTML(sortedgroup, str(startime) + "->" + str(endtime)))
outfile.close()
