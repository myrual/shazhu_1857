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
