
import os

from p_extract2.m_svn_record7 import *

'''
note:
    抽取所有，不分类合并。
'''

__author__ = 'dyc'

# 配置信息

branch_name = 'DEV2' # 哪个分支

current_base_info = ['','']   # 保存版本号、提交人信息，先存俩空字符串站位，避免第一次赋值报异常
row_info_all = []
current_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))
version_num_list = []

def write_excel(row_info_all_fun):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('cnweb_ss', cell_overwrite_ok=True)
    for i in range(0, len(row_info_all_fun)):
        for j in range(0, len(row_info_all_fun[i])):
            sheet1.write(i, j, row_info_all_fun[i][j])
    book.save(r'D:\svn info all.xls')

svn_log_command = 'svn log --limit {0} --search {1} -v {2}'
svn_command_format = svn_log_command.format(
    1000,  'lifang',r'http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV2/cnweb_ss')
svninfo = os.popen(svn_command_format).readlines()

if len(svninfo)==0:
    print('svn info is empty')

"""
结果是一个list，需要一行行处理。
-----------  的下一行含有  版本号|提交人 。
Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

"""

logLen = len(svninfo)
print('len svninfo:',logLen)
j = 0
while j < logLen- 1:  # 最后一行--------没有价值，反而会让下面的if越界
    if svninfo[j].startswith('----'):  # 一次提交记录的第一行
        j = j + 1  # 下一行，提取版本号、提交人信息
        svn_info_item = svninfo[j].split('|')
        current_base_info[0] = svn_info_item[0].strip()[1:]
        current_base_info[1] = svn_info_item[1].strip()

        # 存放所有版本号
        if not current_base_info[0] in version_num_list:
            version_num_list.append(current_base_info[0])

    elif svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        while svninfo[j].strip() != '':
            original_file_path = svninfo[j].strip()

            idx_dev = original_file_path.find('DEV2')
            file_path = original_file_path[idx_dev:]
            # 用于写excel
            row_info_signal = []
            row_info_signal.append(file_path)
            action = original_file_path[0]
            if action == 'A':
                action = '新增'
            elif action == 'M':
                action = '修改'
            elif action == 'D':
                action = '删除'
            row_info_signal.append(action)

            row_info_signal.append(current_date)  # 时间
            row_info_signal.append('')  # 备注
            row_info_signal.append(current_base_info[1])  # 提交人
            row_info_signal.append(current_base_info[0])  # 版本号
            row_info_all.append(row_info_signal)
            j = j + 1
    else:
        j = j + 1

write_excel(row_info_all)
