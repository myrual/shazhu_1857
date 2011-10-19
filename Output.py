"""
now is the output function
"""
HTML_START_STRING = "<html>\n" + "<body>\n" + "<h4> result of compare </h4>\n"
HTML_END_STRING = "</body>\n" + "</html>\n\n"
HTML_Table_StartString = "<table border = \"1\">"
HTML_Table_EndString = "</table>\n\n"
HTML_Table_ROW_Start = "<tr>\n"
HTML_Table_ROW_END = "</tr>\n\n"
HTML_Table_Col_Start = "  <td>\n"
HTML_Table_Col_END = "</td>\n\n"
def InsertRow(rowcontentlist):
    singleRow = ""
    for i in rowcontentlist:
        if type(i) == type(0.01) or type(i) == type(1):
            singleRow = singleRow + HTML_Table_Col_Start + str(i) + HTML_Table_Col_END
        if type(i) == type("aa") or type(i) == type('a'):
            singleRow = singleRow + HTML_Table_Col_Start + i + HTML_Table_Col_END
        if type(i) == type([]) and i == []:
            singleRow = singleRow + HTML_Table_Col_Start + "N/A" + HTML_Table_Col_END
    return HTML_Table_ROW_Start + singleRow + HTML_Table_ROW_END

def InsertRowText(rowcontentlist):
    singleRow = ""
    space = "    "
    for i in rowcontentlist:
        if type(i) == type(0.01) or type(i) == type(1):
            singleRow = singleRow + space + str(i)
        if type(i) == type("aa") or type(i) == type('a'):
            singleRow = singleRow + space + i
        if type(i) == type([]) and i == []:
            singleRow = singleRow + space + "N/A"
    return singleRow + "\n"
def InputTabletoHTMLTable(inputtable, title):
    table = ""
    for i in inputtable:
        table = table + InsertRow(i)
    return "<h4>" + title + "</h4>\n" + HTML_Table_StartString + table + HTML_Table_EndString

def InputTabletoTextTable(inputtable, title):
    table = ""
    for i in inputtable:
        table = table + InsertRowText(i)
    return "="*5 + title + "="*5 + "\n" + table
def OutputHTML(inputtable,title):
    tablepart = InputTabletoHTMLTable(inputtable, title)
    return HTML_START_STRING + tablepart + HTML_END_STRING
def OutputText(inputtable, title):

    tablepart = InputTabletoTextTable(inputtable, title)
    return tablepart

def OutputTextPadding(inputtable, title):
    tablelist = InputTable2PaddingList(inputtable, title)
    stri = PaddingListTable2Text(tablelist)
    return stri
def MergeMultiTable(inputtablegroup):
    """
    inputtablegroup is an list group, i[0] = inputtable, i[1] = title
    """
    colum_numb = len(inputtablegroup[0][0]) + 1
    result = []
    for i in range(0, colum_numb):

        result.append('')
    for i in inputtablegroup:
        tmp = InputTable2PaddingList(i[0], i[1])
        for j in range(0, colum_numb):
            result[j] = result[j] + tmp[j]
    return result
 
def FoundChineseName(inputid):
    id_map = open('id_matching_chinese.txt', 'r')
    whole = id_map.readlines()
    count = len(whole)
    for i in range(0, count):
        if whole[i] == inputid+'\n':
            return whole[i+1][0:-1]
    return inputid
def InputTable2PaddingList(inputtable, title):
    concatstr = '  '
    title_maxlen = len(title)
    name_maxlen = getMaxLenth_BlockName(inputtable)
    value_maxlen = getMaxLenth_BlockValue(inputtable)
    name_value_max = name_maxlen + value_maxlen + len(concatstr)
    if title_maxlen > name_value_max:
        final_max = title_maxlen
    else:
        final_max = name_value_max
    result = []
    result.append(Padding(title, final_max))
    for i in inputtable:
        name = FoundChineseName(i[0])
        value = str(i[1])
        result.append(Padding(Padding(name, name_maxlen) + concatstr + value, final_max))
    return result

def PaddingListTable2Text(paddinglist):
    result = ''
    for i in paddinglist:
        result =result + i+'\n'
    return result
def Padding(inputstring, maxlen):
    return inputstring + ' '*(maxlen-len(inputstring))

def getMaxLenth_BlockName(inputtable):
    max = 0
    for i in inputtable:
        if max < len(FoundChineseName(i[0])):
            max = len(FoundChineseName(i[0]))
    return max

def getMaxLenth_BlockValue(inputtable):
    max = 0
    for i in inputtable:
        if max < len(str(i[0])):
            max = len(str(i[0]))
    return max
