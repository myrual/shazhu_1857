from readDayRecord import *
from readBlock import *

startime = int(raw_input("start:"))
endtime =  int(raw_input("end  :"))
BlockFileName = raw_input("block file name:")

outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockFileName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockFileName + '.txt'
groupresult = GroupPercentage(startime, endtime, GetDayKFileNameGroupFromBlockFile('..\\T0002\\blocknew\\' + BlockFileName))
sortedgroup = GetSortedTable(groupresult)

outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedgroup, str(startime) + "->" + str(endtime)))
outfileText.write(OutputTextPadding(sortedgroup, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
