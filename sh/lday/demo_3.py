from readDayRecord import *
from readBlock import *
startime = 20110830
endtime = 20110930
BlockFileNameGroup_WithoutFileType = ['BX', 'DL', 'DLSB', 'DQ', 'DZXX', 'FDC', 'FCFZ', 'GCJZ', 'GSGQ', 'GSGQ', 'GT', 'HGHX'
        , 'HJG', 'HTJG', 'JC', 'JSJ', 'JTGJ', 'JTSS', 'JX', 'JYCM', 'LYJD', 'MHG', 'MTSY', 'NJSP', 'QS', 'QTXY', 'SYLS',
        'TJG', 'TLJJ', 'TX', 'WM', 'WNB', 'XNY', 'YDYB', 'YSJS', 'YSJS', 'YSWL', 'YXL']
BlockFileGroup = []
for i in BlockFileNameGroup_WithoutFileType:
    BlockFileGroup.append(i+'.blk')
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
