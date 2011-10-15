from readDayRecord import *
from readBlock import *
startime = int(raw_input("start time:"))
endtime =  int(raw_input("end time:"))
BlockFileNameGroup_WithoutFileType = ['BX', 'DL', 'DLSB', 'DQ', 'DZXX', 'FDC', 'FZFZ', 'GCJZ', 'GSGQ', 'GT', 'HGHX'
        ,'HJG', 'HTJG', 'JC', 'JSJ', 'JTGJ', 'JTSS', 'JX', 'JYCM', 'LYJD', 'MHG', 'MTSY', 'NJSP', 'QS', 'QTXY', 'SYLS',
        'TJG', 'TLJJ', 'TX', 'WM', 'XNY', 'YDYB', 'YSJS', 'YSWL', 'YXL']
BlockFileGroup = []
for i in BlockFileNameGroup_WithoutFileType:
    BlockFileGroup.append(i+'.blk')
BlockCompareTable = GetBlockSortTable(startime, endtime, BlockFileGroup)
sortedTable = GetSortedTable(BlockCompareTable)

BlockGroupName = "AllBlock"
outfileName_HTML = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.html'
outfileName_TEXT = str(startime) + '_'+ str(endtime) + '_' + BlockGroupName + '.txt'
outfile = open(outfileName_HTML, 'w')
outfileText = open(outfileName_TEXT, 'w')

outfile.write(OutputHTML(sortedTable, str(startime) + "->" + str(endtime)))
outfileText.write(OutputText(sortedTable, str(startime) + "->" + str(endtime)))
outfile.close()
outfileText.close()
