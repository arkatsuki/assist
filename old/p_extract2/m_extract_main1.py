
import os

from p_extract2.m_svn_record6 import *

'''
note:
    已经能实现准确分类
'''

__author__ = 'dyc'

# 配置信息

branch_name = 'DEV2' # 哪个分支

current_base_info = ['','']   # 保存版本号、提交人信息，先存俩空字符串站位，避免第一次赋值报异常

version_num_list = []

path_obj_dic = {}

svninfo = os.popen("svn log --limit %d --search %s --search-and %d -v %s" %
                       (500, 'duanyaochang', 1242,
                        r'http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV2/cnweb_ss')).readlines()

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
        # 每次提交记录开始的时候，清空file path。因为每条提交记录一次put_dict，防止重复put_dict之前的
        file_path_list = []
        j = j + 1  # 下一行，提取版本号、提交人信息
        # debug
        # print('line info:',svninfo[j])
        # result: r39273 | duanyaochang | 2017-08-11 10:23:03 +0800 (周五, 11 八月 2017) | 1 line

        svn_info_item = svninfo[j].split('|')
        current_base_info[0] = svn_info_item[0].strip()[1:]
        current_base_info[1] = svn_info_item[1].strip()

        # 存放所有版本号
        if(not current_base_info[0] in version_num_list):
            version_num_list.append(current_base_info[0])

    elif svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        # debug
        # print('line info:', svninfo[j])
        # result: M /Develop/projects/branches/DEV2/cnweb_ss/src/main/java/com/ss/product/model/ProductSeries.java

        while svninfo[j].strip() != '':
            original_file_path = svninfo[j].strip()

            idx_dev = original_file_path.find('DEV2')
            file_path = original_file_path[idx_dev:]

            if not file_path in path_obj_dic:
                rec = SvnRecord(file_path=file_path,version_num=current_base_info[0],
                      user_name=current_base_info[1])
                rec.add_ver_num_action(current_base_info[0],original_file_path[0])
                path_obj_dic[file_path] = rec
                pass
            else:
                rec = path_obj_dic[file_path]
                rec.add_ver_num_action(current_base_info[0], original_file_path[0])
                pass
            j = j + 1
    else:
        j = j + 1

for rec in path_obj_dic.values():
    rec.put_list()

print('SvnRecord.records_modify len',len(SvnRecord.records_modify))

for rec in SvnRecord.records_modify:
    print('rec in modify:',rec.file_path,' , ',rec.version_num)

print('version_num_list len :', len(version_num_list))
version_num_list.reverse()
print('version_num_list:', ','.join(version_num_list))
