from readDayRecord import *
from readBlock import *

startime = int(raw_input("input start time:")
endtime = int(raw_input("input end time:")
BlockFileName = raw_input("input block file name:")

outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockFileName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockFileName + '.txt'
groupresult = GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('..\\T0002\\blocknew\\' + BlockFileName))
sortedgroup = GetSortedTable(groupresult)

outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedgroup, str(startime) + "->" + str(endtime)))
outfileText.write(OutputText(sortedgroup, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
