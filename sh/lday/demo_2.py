from readDayRecord import *
from readBlock import *

startime = int(raw_input("start time: 20110830:"))
endtime = int(raw_input("end time:20110830:"))
BlockFileName = raw_input("BlockFileName: DL.blk")
outfileName = str(startime) + '_'+ str(endtime) + BlockFileName + '.html'
groupresult = GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('..\\T0002\\blocknew\\' + BlockFileName))
sortedgroup = GetSortedTable(groupresult)
outfile = open(outfileName, 'w')
outfile.write(OutputHTML(sortedgroup, str(startime) + "->" + str(endtime)))
outfile.close()
