from readDayRecord import *
from readBlock import *
startime = 20110830
endtime = 20110930
BlockFileGroup = ['MTSY.blk', 'DL.blk']
BlockCompareTable = GetBlockSortTable(startime, endtime, BlockFileGroup)
sortedTable = GetSortedTable(BlockCompareTable)

BlockGroupName = ""
for i in BlockFileGroup:
    BlockGroupName =  BlockGroupName + i
outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.txt'
outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedTable, str(startime) + "->" + str(endtime)))
outfileText.write(OutputText(sortedTable, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
