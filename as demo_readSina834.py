#-*-coding:GB2312-*-
import urllib
import re
urlitem = urllib.urlopen("http://money.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/600834.phtml")
htmlsource = urlitem.read()
fenghong_String = 'sharebonus_1'
Peigu_String = 'sharebonus_2'

StartFromFenghong = htmlsource[htmlsource.find(fenghong_String):]
end_position_fenghong = StartFromFenghong.find('table')
fenghong = StartFromFenghong[0: end_position_fenghong]
print fenghong

StartFromPeigu= htmlsource[htmlsource.find(Peigu_String):]
end_position_peigu= StartFromPeigu.find('table')
print end_position_peigu
print StartFromPeigu[0:end_position_peigu]
