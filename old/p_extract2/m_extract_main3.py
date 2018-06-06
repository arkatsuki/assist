
import os
import configparser


from p_extract2.m_svn_record7 import *

'''
note:
    修改为从ini文件读取配置信息
'''

config = configparser.ConfigParser()
config.read('config.ini')
svn_addr = config.get('svn','svn_addr')
version_num = config.get('svn','version_num')
record_limit = config.get('svn','record_limit')
branch_name = config.get('svn','branch_name') # 哪个分支


current_base_info = ['','']   # 保存版本号、提交人信息，先存俩空字符串站位，避免第一次赋值报异常
version_num_list = []
path_obj_dic = {}

# svn_log_command = 'svn log --limit {0} --search {1} --search-and {2} -v {3}'

svn_log_command = 'svn log --limit {0} --search {1} -v {2}'
svn_command_format = svn_log_command.format(
    record_limit,  version_num, svn_addr)

svninfo = os.popen(svn_command_format).readlines()

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
        # debug
        # print('line info:',svninfo[j])
        # result: r39273 | name | 2017-08-11 10:23:03 +0800 (周五, 11 八月 2017) | 1 line

        svn_info_item = svninfo[j].split('|')
        current_base_info[0] = svn_info_item[0].strip()[1:]
        current_base_info[1] = svn_info_item[1].strip()

        # 存放所有版本号
        if not current_base_info[0] in version_num_list:
            version_num_list.append(current_base_info[0])

    elif svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        # debug
        # print('line info:', svninfo[j])

        while svninfo[j].strip() != '':
            original_file_path = svninfo[j].strip()

            idx_dev = original_file_path.find(branch_name)
            file_path = original_file_path[idx_dev:]
            if file_path.split('/')[-1].find('.') == -1:
                # 是目录
                print('find directory:',file_path)
                j = j + 1
                continue

            if file_path not in path_obj_dic:
                rec = SvnRecord(file_path=file_path,version_num=current_base_info[0],
                                user_name=current_base_info[1], action=original_file_path[0])
                rec.add_ver_num_action(current_base_info[0],original_file_path[0])
                path_obj_dic[file_path] = rec
            else:
                rec = path_obj_dic[file_path]
                rec.add_ver_num_action(current_base_info[0], original_file_path[0])
            j = j + 1
    else:
        j = j + 1

for rec in path_obj_dic.values():
    rec.put_list()

SvnRecord.write_excel(r'D:\svn info.xls')

print('version_num_list len :', len(version_num_list))
version_num_list.reverse()
print('version_num_list:', ','.join(version_num_list))
