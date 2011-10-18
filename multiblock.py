from readDayRecord import *
import readBlock
import sys
import time

BlockFileNameGroup_WithoutFileType = sys.argv[1:]
BlockFileGroup = []
StockIDGroup = []
milestonegroup = []
for i in BlockFileNameGroup_WithoutFileType:
    if len(i) == 6 and i.isdigit():
        #if it is all digi and six number len
        StockIDGroup.append(i)
    else:
        if len(i) == 8 and i.isdigit():
            #it is milestone.
            milestonegroup.append(i)
        else:
            BlockFileGroup.append(i+'.blk')

milestonegroup_sorted = sorted(milestonegroup, key = lambda x: int(x))
today = time.localtime()
today_instring = str(today.tm_year*10000 + today.tm_mon*100 + today.tm_mday)
milestonegroup_sorted.append(today_instring)
total = len(milestonegroup_sorted)
if total == 1:
    print "you have to input start time like 20110718"
    exit()
period_group = []
#first is start and today
period_group.append([milestonegroup_sorted[0], milestonegroup_sorted[-1]])
if total <> 2:
    i = 0
    while i < (total -1):
        period_group.append([milestonegroup_sorted[i], milestonegroup_sorted[i+1]])
        i = i + 1
for i in period_group:
    print i[0] + "->" + i[1]
    
raw_input("pause")
for i in period_group:
    startime = int(i[0])
    endtime =  int(i[1])
    BlockCompareTable = readBlock.GetBlockSortTable(startime, endtime, BlockFileGroup)
    StockIDCompareTable = []
    for i in StockIDGroup:
        tmp = [i, Percentage_byStockID(startime, endtime, i)]
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
