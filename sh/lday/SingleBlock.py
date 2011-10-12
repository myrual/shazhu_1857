from readDayRecord import *
from readBlock import *

startime = 20110830
endtime = 20110930
BlockFileName = 'MTSY.blk'

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
