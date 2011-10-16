from readDayRecord import *
import readBlock
import sys

startime = int(raw_input("start time:"))
endtime =  int(raw_input("end time:"))
BlockFileNameGroup_WithoutFileType = sys.argv[1:]
BlockFileGroup = []
StockIDGroup = []
for i in BlockFileNameGroup_WithoutFileType:
    if len(i) == 6 and i.isdigit():
        #if it is all digi and six number len
        StockIDGroup.append(i)
    else:
        BlockFileGroup.append(i+'.blk')
BlockCompareTable = readBlock.GetBlockSortTable(startime, endtime, BlockFileGroup)
StockIDCompareTable = []
for i in StockIDGroup:
    tmp = [i, Percentage_byStockID(startime, endtime, i)]
    print tmp
    StockIDCompareTable.append(tmp)
sortedTable = GetSortedTable(BlockCompareTable + StockIDCompareTable)

BlockGroupName = "MultiBlock"
outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.txt'
outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedTable, str(startime) + "->" + str(endtime)))
outfileText.write(OutputText(sortedTable, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
