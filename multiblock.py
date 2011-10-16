from readDayRecord import *
import readBlock
import sys

print sys.argv # returns: ['param.py']
startime = int(raw_input("start time:"))
endtime =  int(raw_input("end time:"))
BlockFileNameGroup_WithoutFileType = sys.argv[1:]
BlockFileGroup = []
for i in BlockFileNameGroup_WithoutFileType:
    BlockFileGroup.append(i+'.blk')
BlockCompareTable = readBlock.GetBlockSortTable(startime, endtime, BlockFileGroup)
sortedTable = GetSortedTable(BlockCompareTable)

BlockGroupName = "MultiBlock"
outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.txt'
outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedTable, str(startime) + "->" + str(endtime)))
outfileText.write(OutputText(sortedTable, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
