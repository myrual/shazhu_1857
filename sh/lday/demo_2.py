from readDayRecord import *
from readBlock import *

f = open('DL.blk', 'r')
startime = int(raw_input("start time: 20110830:"))
endtime = int(raw_input("end time:20110830:"))
groupresult = GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('DL.blk'))
sortedgroup = GetSortedTable(groupresult)
outfile = open('percentage_BLock.html', 'w')
outfile.write(OutputHTML(sortedgroup, str(startime) + "->" + str(endtime)))
outfile.close()
