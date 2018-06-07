
import xlwt
import os
import time

# xlwt api : http://xlwt.readthedocs.io/en/latest/api.html

'''
功能正常，可以过滤、分类，可以写excel，可以比较是否漏/多文件，待优化
改进：
    line 171 删除set用list，try except，防止比较时KeyError/ValueError阻塞流程
'''

__author__ = 'dyc'

# 配置信息
# repos_path = r'D:\svn\format'
repos_path = r'http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss'

search_num = 1000 # 往前搜索的记录数
user_name = 'lifang'
redmine_num = 1081 # 需求编号，注释中必须有
# 也可以按版本号范围查询
begin_version_num = ''
end_version_num = ''

branch_name = 'DEV' # 哪个分支

filter_repeat = 'y'
sort_category = 'n'

compare_path = 'y'
compare_file_path = r'F:\py\lib-svn\readInfo.txt'

out_put_info_txt_path = r'F:\py\lib-svn\outputSvn.txt'   # 输出的txt文件路径
out_put_info_excel_path = r'F:\py\lib-svn\outputSvn.xls'   # 输出的excel文件路径
out_put_diff_info_txt_path = r'F:\py\lib-svn\outputSvn111.txt'   # 输出的表信息的txt文件路径

filter_repeat_bool = False  # 默认false，不过滤重复路径
if filter_repeat == 'y':
    filter_repeat_bool = True

sort_category_bool = False # 是否按增删改分类，会打乱版本号
if sort_category == 'y':
    sort_category_bool = True

compare_path_bool = False
if compare_path == 'y':
    compare_path_bool = True


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
# row_info_signal = []   # 行信息


def write_excel(row_info_all_fun):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('cnweb_ss', cell_overwrite_ok=True)
    for i in range(0, len(row_info_all_fun)):
        for j in range(0, len(row_info_all_fun[i])):
            sheet1.write(i, j, row_info_all_fun[i][j])
    book.save(out_put_info_excel_path)


def check_path_exists (new_path_info, version_num):
    for k, v in version_path_dict.items():
        for old_path_info in v:
            if old_path_info==new_path_info and k>version_num:
                return True
            else:
                continue
    return False


def write_output_file(pathItem, current_base_info_fun):
    # 格式化，并写txt文件
    output.append(current_base_info_fun[0])  # 版本号
    output.append('\t')
    output.append(current_base_info_fun[1])  # 提交人
    output.append('\t')

    action = pathItem[0]

    path_item_path = pathItem[1:]
    idx_dev = path_item_path.find(branch_name)
    path_item_path = path_item_path[idx_dev:]

    output.append(action)
    output.append('\t')
    output.append(path_item_path)

    output.append('\n')

    # 用于写excel
    row_info_signal = []
    row_info_signal.append(path_item_path)
    if action=='A':
        action='新增'
    elif action=='M':
        action='修改'
    elif action=='D':
        action='删除'
    row_info_signal.append(action)
    current_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))
    row_info_signal.append(current_date)  # 时间
    row_info_signal.append('')  # 备注
    row_info_signal.append(current_base_info_fun[1])  # 提交人
    row_info_signal.append(current_base_info_fun[0])  # 版本号
    row_info_all.append(row_info_signal)

    # 存放所有路径，用于比较是否漏/多路径
    file_path_all_list.append(path_item_path)


def put_dict (file_path_list_fun, current_base_info_fun):
    """
        filePathListFun  文件路径的list
        outputFun	用于输出的list
        currentBaseInfoFun   版本号、提交人信息
    """
    file_path_set_fun = set(file_path_list_fun)
    for pathItem in file_path_set_fun:
        # 如果需要过滤重复路径，检验是否存在更大版本号的相同路径
        if filter_repeat_bool:
            if check_path_exists(pathItem, current_base_info_fun[0]):
                # 已经存在，继续下一次循环
                continue
        if sort_category_bool:
            if pathItem[0]=='A':
                path_version_list_a.append(pathItem + '&' + current_base_info_fun[0] + '&' + current_base_info_fun[1])
            elif pathItem[0]=='M':
                path_version_list_m.append(pathItem + '&' + current_base_info_fun[0] + '&' + current_base_info_fun[1])
            elif pathItem[0] == 'D':
                path_version_list_d.append(pathItem + '&' + current_base_info_fun[0] + '&' + current_base_info_fun[1])
        else:
            write_output_file(pathItem, current_base_info)
    version_path_dict[current_base_info_fun[0]] = []
    version_path_dict[current_base_info_fun[0]].extend(file_path_set_fun)


def compare_path(file_path_all_list_fun, compare_file_path_fun):
    with open(compare_file_path_fun, 'r') as f:
        file_path_different_list.append('多了')
        file_path_different_list.append('\n')
        for line in f:
            # li = line.split('\t')  # 如果是从excel中复制出来两列，可以用\t分割
            # for item in li:
            #     print(item)
            # line会包含\n
            if line.strip() not in file_path_all_list_fun:
                file_path_different_list.append(line.strip())
                file_path_different_list.append('\n')
            else:
                try:
                    file_path_all_list_fun.remove(line.strip())
                except Exception:    # KeyError    ValueError
                    # line有可能重复，此时file_all_set已经删除这个key了，就报KeyError
                    print('Exception, line:', line.strip())
    file_path_different_list.append('少了')
    file_path_different_list.append('\n')
    file_path_different_list.extend('\n'.join(file_path_all_list_fun))
    with open(out_put_diff_info_txt_path, 'w', encoding='utf-8') as f:
        f.write(''.join(file_path_different_list))  # write的参数需要是字符串，不能是List


def write_output_list(path_version_list_fun):
    for item in path_version_list_fun:
        item_list = item.split('&')
        write_output_file(item_list[0], item_list[1:])

# svn log -r 30050:30125 --search duanyaochang -v http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss
# svn log --limit 5 --search duanyaochang --search-and 983 -v http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss

if redmine_num:
    svninfo = os.popen("svn log --limit %d --search %s --search-and %d -v %s" %
                       (search_num, user_name, redmine_num, repos_path)).readlines()
    # svninfo = os.popen("svn log --limit 1000 --search 1081 -v %s"  % repos_path).readlines()
else:
    print('svn param error')
    svninfo = []

if len(svninfo)==0:
    print('svn info is empty')

"""
结果是一个list，需要一行行处理。
-----------  的下一行含有  版本号|提交人 。
Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

"""

logLen = len(svninfo)
j = 0
while j < logLen- 1:  # 最后一行--------没有价值，反而会让下面的if越界
    if svninfo[j].startswith('----'):  # 一次提交记录的第一行
        file_path_list = []    # 每次提交记录开始的时候，清空file path
        j = j + 1  # 下一行，提取版本号、提交人信息
        svn_info_item = svninfo[j].split('|')
        if len(current_base_info) < 2:
            current_base_info.append(svn_info_item[0].strip()[1:])
            current_base_info.append(svn_info_item[1].strip())
        else:
            current_base_info[0] = svn_info_item[0].strip()[1:]
            current_base_info[1] = svn_info_item[1].strip()
    elif svninfo[j].startswith('Changed paths'):
        j = j + 1  # 下一行
        file_path_list.append(svninfo[j].strip())
        while svninfo[j].strip() != '':
            file_path_list.append(svninfo[j].strip())
            j = j + 1
        put_dict(file_path_list, current_base_info)
    else:
        j = j + 1

if sort_category_bool:
    write_output_list(path_version_list_a)
    write_output_list(path_version_list_m)
    write_output_list(path_version_list_d)

write_excel(row_info_all)

if compare_path_bool and compare_file_path!='':
    compare_path(file_path_all_list, compare_file_path)

with open(out_put_info_txt_path, 'w', encoding='utf-8') as f:
    f.write(''.join(output))  # write的参数需要是字符串，不能是List

