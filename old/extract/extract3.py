
import xlrd
import xlwt
import os

# xlrt api : http://xlwt.readthedocs.io/en/latest/api.html

book = xlwt.Workbook()
sheet1 = book.add_sheet('cnweb_ss')

__author__ = 'dyc'

# repos_path = r'D:\svn\format'
repos_path = r'http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss'

# versionNumBegin = 30050   29076
# versionNumEnd = 30125   30750
# user_name = 'duanyaochang'
version_num_begin = 31398 # 29076
version_num_end = 31398 # 30750
user_name = 'duanyaochang'
filter_repeat = 'n'
filter_repeat_bool = False  # 默认false，不过滤重复路径
filter_category =  'n'
filter_category_bool = False # 是否按增删改分类，会打乱版本号

if filter_repeat == 'y':
    filter_repeat_bool = True

if filter_category == 'y':
    filter_category_bool = True

# svn log -r 30050:30125 -v D:\svn\format
# svn log -r 30050:30125 -v http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss

if version_num_begin and version_num_end and user_name:
    svninfo = os.popen("svn log -r %s:%s -v %s --search %s" % (version_num_begin ,version_num_end ,repos_path, user_name)).readlines()
else:
    svninfo = []
"""
结果是一个list，需要一行行处理。
-----------  的下一行含有  版本号|提交人 。
Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

"""

file_path_list = []   # 存放每个版本号提交记录的文件路径
file_path_all_list = []   # 存放所有提交记录的文件路径
output = []    # 整个输出文件

current_base_info = []   # 保存版本号、提交人信息

row_column_info = []  # 二维数组，元素是行信息（list）
row_info = []   # 行信息

logLen = len(svninfo)
j = 0


def write_file_path (filePathListFun, outputFun, currentBaseInfoFun):
    """
        filePathListFun  文件路径的list
        outputFun	用于输出的list
        currentBaseInfoFun   版本号、提交人信息
    """
    filePathSetFun = set(filePathListFun)

    for pathItem in filePathSetFun:
        outputFun.append(currentBaseInfoFun[0])
        outputFun.append('\t')
        outputFun.append(currentBaseInfoFun[1])
        outputFun.append('\t')

        action = pathItem[0]

        path_item_path = pathItem[1:]
        idxDev = path_item_path.find('DEV')
        path_item_path = path_item_path[idxDev:]

        outputFun.append(action)
        outputFun.append('\t')
        outputFun.append(path_item_path)

        outputFun.append('\n')

while j < logLen- 1:  # 最后一行--------没有价值，反而会让下面的if越界
    if svninfo[j].startswith('----'):  # 一次提交记录的第一行
        file_path_list = []    # 每次提交记录开始的时候，清空file path
        j = j + 1  # 下一行，提取版本号、提交人信息
        svninfoItem = svninfo[j].split('|')
        if len(current_base_info) < 2:
            current_base_info.append(svninfoItem[0].strip()[1:])
            current_base_info.append(svninfoItem[1].strip())
        else:
            current_base_info[0] = svninfoItem[0].strip()[1:]
            current_base_info[1] = svninfoItem[1].strip()

        continue

    if svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行

        if svninfo[j].strip() in file_path_all_list and filter_repeat_bool:
            pass
        else:
            file_path_list.append(svninfo[j].strip())
            file_path_all_list.append(svninfo[j].strip())
        # filePathList.append(svninfo[j].strip())

        while svninfo[j].strip() != '':
            if svninfo[j].strip() in file_path_all_list and filter_repeat_bool:
                pass
            else:
                file_path_list.append(svninfo[j].strip())
                file_path_all_list.append(svninfo[j].strip())
            # filePathList.append(svninfo[j].strip())
            j = j + 1
        write_file_path(file_path_list, output, current_base_info)
        continue
    j = j + 1

f = open(r'F:\py\lib-svn\outputSvn.txt', 'w')
f.write(''.join(output))  # write的参数需要是字符串，不能是List







