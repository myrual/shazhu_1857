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
        else:
            singleRow = singleRow + HTML_Table_Col_Start + i + HTML_Table_Col_END
    return HTML_Table_ROW_Start + singleRow + HTML_Table_ROW_END
def InputTabletoHTMLTable(inputtable, title):
    table = ""
    for i in inputtable:
        table = table + InsertRow(i)
    return "<h4>" + title + "</h4>\n" + HTML_Table_StartString + table + HTML_Table_EndString
def OutputHTML(inputtable,title):
    tablepart = InputTabletoHTMLTable(inputtable, title)
    return HTML_START_STRING + tablepart + HTML_END_STRING
