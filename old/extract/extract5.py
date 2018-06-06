
import xlrd
import xlwt
import os

# xlrt api : http://xlwt.readthedocs.io/en/latest/api.html

'''
功能正常，可以过滤、分类
'''

book = xlwt.Workbook()
sheet1 = book.add_sheet('cnweb_ss')

__author__ = 'dyc'

# repos_path = r'D:\svn\format'
repos_path = r'http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss'

search_num = 500 # 往前搜索的记录数
user_name = 'duanyaochang'
redmine_num = 983 # 需求编号，注释中必须有
filter_repeat = 'n'
filter_repeat_bool = False  # 默认false，不过滤重复路径
sort_category =  'y'
sort_category_bool = False # 是否按增删改分类，会打乱版本号

if filter_repeat == 'y':
    filter_repeat_bool = True

if sort_category == 'y':
    sort_category_bool = True

filter_repeat_bool_test = True

# svn log -r 30050:30125 -v D:\svn\format
# svn log -r 30050:30125 --search duanyaochang -v http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss
# svn log --limit 5 --search duanyaochang --search-and 983 -v http://192.168.200.232:8888/svn/CN/Develop/projects/branches/DEV/cnweb_ss

if redmine_num:
    svninfo = os.popen("svn log --limit %d --search %s --search-and %d -v %s" % (search_num, user_name, redmine_num, repos_path)).readlines()
else:
    print(' no begin svn info')
    svninfo = []


"""
结果是一个list，需要一行行处理。
-----------  的下一行含有  版本号|提交人 。
Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

"""

file_path_list = []   # 存放每个版本号提交记录的文件路径
file_path_all_list = []   # 存放所有提交记录的文件路径
output = []    # 整个输出文件
version_path_dict = {}   # key是版本号，value是所有信息
path_version_dict_a = {}   # key是路径，value是版本号、提交人list
path_version_dict_m = {}   # key是路径，value是版本号、提交人list
path_version_dict_d = {}   # key是路径，value是版本号、提交人list

current_base_info = []   # 保存版本号、提交人信息

file_path_list_a = []     # 增加的path
file_path_list_m = []     # 修改的path
file_path_list_d = []     # 删除的path

row_column_info = []  # 二维数组，元素是行信息（list）
row_info = []   # 行信息

logLen = len(svninfo)
j = 0

def check_path_exists (new_path_info, version_num):
    # print('new_path_info:', new_path_info)
    # print('new_path_info type',type(new_path_info))
    for k, v in version_path_dict.items():
        # print('v type',type(v))
        for old_path_info in v:
            # print('begin for in v')
            # print('find return:',new_path_info.find('CommonConstants'))

            # if new_path_info.find('CommonConstants')>0:
                # print('v len',len(v))
                # print('new_path_info:',new_path_info)
                # print('old_path_info:', old_path_info)
                # print('k:',k)
                # print('version_num:', version_num)

            if old_path_info==new_path_info and k>version_num:
                return True
            else:
                continue
    return False


def write_output_file(pathItem, current_base_info_fun):
    output.append(current_base_info_fun[0])  # 版本号
    output.append('\t')
    output.append(current_base_info_fun[1])  # 提交人
    output.append('\t')

    action = pathItem[0]

    path_item_path = pathItem[1:]
    idxDev = path_item_path.find('DEV')
    path_item_path = path_item_path[idxDev:]

    output.append(action)
    output.append('\t')
    output.append(path_item_path)

    output.append('\n')


def put_dict (filePathListFun, currentBaseInfoFun):
    """
        filePathListFun  文件路径的list
        outputFun	用于输出的list
        currentBaseInfoFun   版本号、提交人信息
    """
    print('filePathListFun len:',len(filePathListFun))
    file_path_set_fun = set(filePathListFun)
    print('file_path_set_fun len:', len(file_path_set_fun))

    for pathItem in file_path_set_fun:

        # 如果需要过滤重复路径，检验是否存在更大版本号的相同路径
        if filter_repeat_bool_test:
            if check_path_exists(pathItem,currentBaseInfoFun[0]):
                # 已经存在，继续下一次循环
                # print('continue')
                continue
            else:
                # print('pass')
                pass

        version_user = [currentBaseInfoFun[0], currentBaseInfoFun[1]]
        if sort_category_bool:
            if pathItem[0]=='A':
                # file_path_list_a.append(pathItem)
                # 注意作用域
                path_version_dict_a[pathItem] = version_user
            elif pathItem[0]=='M':
                # file_path_list_m.append(pathItem)
                path_version_dict_m[pathItem] = version_user
            elif pathItem[0] == 'D':
                # file_path_list_d.append(pathItem)
                path_version_dict_d[pathItem] = version_user
        else:
            write_output_file(pathItem, current_base_info)

    version_path_dict[currentBaseInfoFun[0]] = []
    version_path_dict[currentBaseInfoFun[0]].extend(file_path_set_fun)

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
            j = j + 1
        put_dict(file_path_list, current_base_info)
        continue
    j = j + 1

if sort_category_bool:
    for k, v in path_version_dict_a.items():
        write_output_file(k, v)
    for k, v in path_version_dict_m.items():
        write_output_file(k, v)
    for k, v in path_version_dict_d.items():
        write_output_file(k, v)
else:
    pass

with open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(output))  # write的参数需要是字符串，不能是List







