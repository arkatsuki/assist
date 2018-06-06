
import os

from extract.extract_version_2_fun3 import *

'''

'''

__author__ = 'dyc'

# 配置信息

branch_name = 'DEV2' # 哪个分支

out_put_info_txt_path = r'F:\py\lib-svn\outputSvn.txt'   # 输出的txt文件路径
out_put_info_excel_path = r'F:\py\lib-svn\outputSvn.xls'   # 输出的excel文件路径
out_put_diff_info_txt_path = r'F:\py\lib-svn\outputSvn111.txt'   # 输出的表信息的txt文件路径

file_path_list = []   # 存放每个版本号提交记录的文件路径
file_path_all_list = []   # 存放所有提交记录的文件路径
file_path_different_list = []    # 存放不一致的文件
output = []    # 整个输出文件
version_path_dict = {}   # key是版本号，value是所有信息

path_version_list_a = []   # add      &分隔路径、版本号、提交人
path_version_list_m = []   # modify   &分隔路径、版本号、提交人
path_version_list_d = []   # delete   &分隔路径、版本号、提交人

current_base_info = []   # 保存版本号、提交人信息

file_path_list_a = []     # 增加的path
file_path_list_m = []     # 修改的path
file_path_list_d = []     # 删除的path

row_info_all = []  # 二维数组，元素是行信息（list）

version_num_list = []

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
        print('line info:',svninfo[j])
        # result: r39273 | duanyaochang | 2017-08-11 10:23:03 +0800 (周五, 11 八月 2017) | 1 line

        svn_info_item = svninfo[j].split('|')
        if len(current_base_info) < 2:
            current_base_info.append(svn_info_item[0].strip()[1:])
            current_base_info.append(svn_info_item[1].strip())
        else:
            current_base_info[0] = svn_info_item[0].strip()[1:]
            current_base_info[1] = svn_info_item[1].strip()

        # 存放所有版本号
        if(not current_base_info[0] in version_num_list):
            version_num_list.append(current_base_info[0])

    elif svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        # debug
        print('line info:', svninfo[j])
        # result: M /Develop/projects/branches/DEV2/cnweb_ss/src/main/java/com/ss/product/model/ProductSeries.java

        while svninfo[j].strip() != '':
            original_file_path = svninfo[j].strip()
            file_path_list.append(svninfo[j].strip()) #  delete ？？？
            put_original_path(original_file_path, current_base_info, version_path_dict)
            j = j + 1
    else:
        j = j + 1

output = []
row_info_all = []
file_path_all_list = []
# extract_version_2_fun.format_output_list(path_version_list_a, branch_name,
#                                          output, row_info_all, file_path_all_list)
# extract_version_2_fun.format_output_list(path_version_list_m, branch_name,
#                                          output, row_info_all, file_path_all_list)
# extract_version_2_fun.format_output_list(path_version_list_d, branch_name,
#                                          output, row_info_all, file_path_all_list)

write_excel(row_info_all, out_put_info_excel_path)

with open(out_put_info_txt_path, 'w', encoding='utf-8') as f:
    f.write(''.join(output))  # write的参数需要是字符串，不能是List

print('version_num_list len :', len(version_num_list))
version_num_list.reverse()
print('version_num_list:', ','.join(version_num_list))
