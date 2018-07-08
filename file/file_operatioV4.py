# -*- coding: utf-8 -*-

import ftplib
import paramiko
import os
import configparser
import chardet
import json
import time
import datetime
import shutil


"""
success
copy_file_dir: 使用windows系统命令复制文件/目录。复制目录可行，复制文件有问题待调试。
copy_file_dir2: 使用shutil复制文件/目录。
get_charset: 未使用。检测数据的编码类型。
rewrite_file_dir: 以utf-8格式重写文件/文件夹到指定路径。
rewrite_file: 以utf-8格式重写文件（不包括目录）到指定路径。
get_all_files: 获取指定目录中所有的文件的路径，包括子目录下的文件。
modify_charset: 把指定目录下的所有文件改成utf-8编码。源目录会先复制备份。
compare_file_byte: 逐个字节比较文件是否相等。
compare_dir：比较两个目录是否相等。包括子目录及其文件的内容、数量、路径。
print_list: 打印list的元素，可以指定打印结果的前后缀。
"""


def copy_file_dir(sour_path, dest_path=''):
    """
    使用windows系统命令复制文件/目录。复制目录可行，复制文件有问题待调试。
    也可以用库进行复制，比如shutil.copy（似乎只能复制文件）
    :param sour_path:
    :param dest_path:
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if dest_path == '':
        backup_name = sour_path + '-' + timestamp
        pass
    else:
        backup_name = dest_path
        pass
    if os.path.isfile(sour_path):
        # echo yes|copy "D:/test-file.txt" "D:/test-file.txt.bak"
        # cmd = 'echo yes|copy "' + sour_path + '" "' + sour_path + '.' + timestamp + '"'
        cmd = 'echo yes|copy "' + sour_path + '" "' + backup_name + '"'
        # cmd = 'echo yes|copy "D:/test-file.txt" "D:/test-file1111.txt"'
        print('cmd:', cmd)
        rs = os.popen(cmd)
        # rs = os.popen('echo yes|copy "' + path + '" "' + path + '' + timestamp + '"')
        # print(chardet.detect(rs.read()))
        print(rs.read())
        pass
    else:
        # echo d|xcopy "D:/test-dir" "D:/test-dir.bak" /e
        # cmd = 'echo d|xcopy "' +sour_path + '" "' +sour_path + '-' + timestamp + '" /e'
        if os.path.isdir(backup_name):
            cmd = 'echo A|xcopy "' + sour_path + '" "' + backup_name + '" /e'
            pass
        else:
            cmd = 'echo d|xcopy "' + sour_path + '" "' + backup_name + '" /e'
            pass
        print('cmd:',cmd)
        rs = os.popen(cmd)
        print(rs.read())
        pass
    return backup_name


def copy_file_dir2(sour_path, dest_path='', backup=True):
    """
    success
    :param sour_path:
    :param dest_path:
    :param backup: 复制前是否先进行备份
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = sour_path + '-' + timestamp
    # 如果目的地址是空的，就是备份操作。
    if dest_path == '':
        backup = False
        dest_path = backup_name
        pass

    if os.path.isfile(sour_path):
        # 先备份
        if backup:
            shutil.copy(sour_path, backup_name)
            pass
        shutil.copy(sour_path, dest_path)
        pass
    else:
        all_files_sour_list = get_all_files(sour_path)

        # 先备份
        if backup:
            for file_sour in all_files_sour_list:

                file_dest = file_sour.replace(sour_path, backup_name)
                new_dir = file_dest[:file_dest.rfind('/')]
                if not os.path.isdir(new_dir):
                    os.mkdir(new_dir)
                    pass
                shutil.copy(file_sour, file_dest)
                pass
            pass

        for file_sour in all_files_sour_list:
            file_dest = file_sour.replace(sour_path, dest_path)
            print('file_sour:', file_sour)
            print('file_dest:', file_dest)
            # 注意是从后往前找，用rfind而不是find。也不是index，index找不到不是-1是异常。
            new_dir = file_dest[:file_dest.rfind('/')]
            if not os.path.isdir(new_dir):
                print('new_dir:', new_dir)
                os.mkdir(new_dir)
                pass
            # 文件如果不存在会创建，但是路径上的目录如果不存在不会创建
            shutil.copy(file_sour, file_dest)
            pass
        pass
    return backup_name


def get_charset():
    """
    未使用。检测数据的编码类型。
    :return:
    """
    dir_path='D:/test-file.txt'
    f=open(dir_path,'rb')
    data=f.read(10)
    # print('data:',data.decode())
    print(chardet.detect(data))
    # charset_dict=json.loads(chardet.detect(data))
    charset_dict=chardet.detect(data)
    print(charset_dict['encoding'])
    pass


def rewrite_file_dir(path, path_new):
    """
    以utf-8格式重写文件/文件夹到指定路径。
    :param path:
    :param path_new:
    :return:
    """
    all_files = []
    if os.path.isdir(path):
        all_files.extend(get_all_files(path))
        for file_path in all_files:
            file_path_new = file_path.replace(path, path_new)
            print('file_path_new:', file_path_new)
            rewrite_file(file_path, file_path_new)
            pass
        pass
    else:
        print('rewrite_file_dir, not dir')
        rewrite_file(path, path_new)
        pass
    pass


def rewrite_file(path, path_new):
    """
    以utf-8格式重写文件（不包括目录）到指定路径。
    :param path:
    :param path_new:
    :return:
    """
    # 如果文件路径不存在，需要先建立文件路径
    if not os.path.isfile(path_new):
        os.makedirs(os.path.dirname(path_new))
        pass

    # 获取编码方式
    f = open(path_new, 'rb')
    data = f.read()
    # data = f.read(20)
    # print(chardet.detect(data))
    charset_dict = chardet.detect(data)
    encoding = charset_dict['encoding']
    # print('encoding:', encoding)
    # print('find uti-8:', encoding.lower().find('utf-8'))
    # if encoding!=None and encoding.lower().find('utf-8')<0:
    #     encoding='gbk'
    if encoding!=None and charset_dict['confidence']<0.6:
        encoding = 'gbk'

    file_new = open(path_new, 'w', encoding='utf-8')
    with open(path, 'r', encoding=encoding) as f:
        for line in f:
            file_new.write(line)
            pass
        pass
    file_new.close()
    pass


def get_all_files(dir_path):
    """
    获取指定目录中所有的文件的路径，包括子目录下的文件。
    :param dir_path:
    :return:
    """
    all_files = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # 完整路径
            file_path_old = os.path.join(parent, filename).replace('\\', '/')
            all_files.append(file_path_old)
            pass
        pass
    return all_files


def modify_charset(dir_path):
    """
    success
    把指定目录下的所有文件改成utf-8编码。源目录会先复制备份。
    :return:
    """
    # path_sour='D:/test-dir'
    # path_sour='D:/test-sth/test-dir'
    # path_dest='D:/test-sth/test-dir-backup'
    # dir_path= 'D:/test-sth/note-txt'
    # 先copy一份，然后用copy后的作为源文件，copy前的作为目的文件，重新用utf-8格式写
    # copy_file_dir(path_sour, path_dest)
    # 先清空原来的文件夹？
    # rewrite_file_dir(path_dest, path_sour)
    rewrite_file_dir(copy_file_dir(dir_path), dir_path)
    pass


def compare_file_byte(file1_path, file2_path):
    """
    Success
    逐个字节比较文件内容。
    :return: False or True
    """
    # file1_path = 'd:/LnAppCalcInfoServiceImpl1111.class'
    # file2_path = 'd:/LnAppAttachInfoServiceImpl.class'
    # file2_path = 'd:/LnAppCalcInfoServiceImpl.class'
    file1 = open(file1_path, 'rb')
    file2 = open(file2_path, 'rb')
    file1_size = os.path.getsize(file1_path)
    file2_size = os.path.getsize(file2_path)
    # print('file1_size:', file1_size, 'file2_size:', file2_size)
    if file1_size != file2_size:
        # print('not equal')
        return False
    for i in range(0, file1_size):
        # print(i)  # 从 0 到 file1_size - 1
        # print(file1.read(i)==file2.read(i))
        if file1.read(i) != file2.read(i):
            return  False
        pass
    file1.close()
    file2.close()
    return  True


def compare_dir(dir1_path, dir2_path):
    """
    success
    比较两个目录是否相等：所有文件数量、路径相同，内容相同（逐个字节比较），最后print比较结果。
    可能是因为字节比较的原因，速度略慢。
    :return:
    """
    # dir1_path = 'D:/test-sth/classes-rel'
    # dir2_path = 'D:/test-sth/classes-uat'
    # 路径必须正斜杠分隔，因为get_all_files返回的是正斜杠分隔。必须一致。
    dir1_path = dir1_path.replace('\\', '/')
    dir2_path = dir2_path.replace('\\', '/')
    dir1_all_files = get_all_files(dir1_path)
    dir2_all_files = get_all_files(dir2_path)
    dir1_surplus = []   # dir1多余的文件
    dir2_surplus = []   # dir2多余的文件
    unequal_files = []    # 不相同的文件
    dir1_surplus.extend(dir1_all_files)
    dir2_surplus.extend(dir2_all_files)
    # if len(dir1_all_files) != len(dir2_all_files):
    #     pass
    for dir1_file in dir1_all_files:
        dir2_file = dir1_file.replace(dir1_path, dir2_path)
        # print('dir1_file:', dir1_file)
        # print('dir2_file:', dir2_file)
        if dir2_file not in dir2_all_files:
            continue
        dir1_surplus.remove(dir1_file)
        dir2_surplus.remove(dir2_file)
        if not compare_file_byte(dir1_file, dir2_file):
            unequal_files.append(dir1_file)
            pass
        pass
    print_list(unequal_files, 'unequal_files:')
    print_list(dir1_surplus, 'dir1_surplus:')
    print_list(dir2_surplus, 'dir2_surplus:')
    pass


def print_list(list, prefix='', surfix=''):
    for elem in list:
        print(prefix, elem, surfix)
        pass
    pass


if __name__ == "__main__":

    dir1_path = 'D:/test_dir/a1'
    dir2_path = 'D:/test_dir/b1'

    # dir1_path = 'D:/test_dir/a1/a1f.txt'
    # dir2_path = 'D:/test_dir/b1/a1f.txt'

    copy_file_dir2(dir1_path, dir2_path)


    # pos = dir2_path.rfind('/')
    # dir2_path = dir2_path[:dir2_path.rfind('/')]
    # print(pos)
    # print(dir2_path)
    pass

