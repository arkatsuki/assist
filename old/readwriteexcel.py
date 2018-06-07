
import os
import sys
import xlrd
import xlwt
from xlutils.copy import copy

excelPath = r'E:\svn-all\svn-task\版本库\更新清单\代码清单\17-05\2017-05-30\TestUFL.xlsx'

data = xlrd.open_workbook(excelPath)

w= copy(data)
# print(w.get_tab_width())

'''
sheetList = w.get_sheet()

out = dir(sheetList)
f = open(r'F:\py\lib-svn\outputSvn.txt','w')
f.write('\n'.join(out))
'''

w.save(r'E:\svn-all\svn-task\版本库\更新清单\代码清单\17-05\2017-05-30\TestUFL2.xls')



"""


'''
reposPath = r'D:\svn\format'

f = open(r'F:\py\lib-svn\outputSvn.txt','w')

f.write(''.join(output))  # write的参数需要是字符串，不能是List
'''

excelPath = r'E:\svn-all\svn-task\版本库\更新清单\代码清单\17-05\2017-05-30\TestUFL.xlsx'

data = xlrd.open_workbook(excelPath)
'''
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
'''

def writeTable(tableFun):


tableList = data.sheets();
for item in tableList:
	# print(item.name)
	if item.name.find('cnweb_ss')!=-1:
		writeTable(item)
		break

'''
# 调试
out = dir(table)
f = open(r'F:\py\lib-svn\outputSvn.txt','w')
f.write('\n'.join(out))
'''


'''
for i in range(nrows): # 循环逐行打印
	print(table.row_values(i)[:3]) # 取前十三列	
'''

"""
