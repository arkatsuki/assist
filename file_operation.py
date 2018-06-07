# -*- coding: utf-8 -*-

import ftplib
import paramiko
import os
import configparser
import chardet
import json
import time
import datetime

"""
OK
"""

def copy_file_dir(sour_path, dest_path=''):
    """
    使用windows系统命令复制文件/文件夹
    :param sour_path:
    :param dest_path:
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = 'timestamp'
    if dest_path=='':
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
        print('cmd rs:', rs.read())
        pass
    else:
        if os.path.isdir(backup_name):
            cmd = 'echo A|xcopy "' + sour_path + '" "' + backup_name + '" /e'
            pass
        else:
            cmd = 'echo d|xcopy "' + sour_path + '" "' + backup_name + '" /e'
            pass
        print('cmd:',cmd)
        rs = os.popen(cmd)
        print('cmd rs:', rs.read())
        pass
    return backup_name

def get_charset():
    """
    检测数据的编码类型
    :return:
    """
    dir_path='D:/test-file.txt'
    f=open(dir_path,'rb')
    data=f.read()
    # print('data:',data.decode())
    print(chardet.detect(data))
    # charset_dict=json.loads(chardet.detect(data))
    charset_dict=chardet.detect(data)
    print(charset_dict['encoding'])
    pass


def rewrite_file_dir(path, path_new):
    """
    以utf-8格式重写文件/文件夹到指定路径
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
    else:
        rewrite_file(path, path_new)
        pass
    pass


def rewrite_file(path, path_new):
    """
    以utf-8格式重写文件到指定路径
    :param path:
    :param path_new:
    :return:
    """
    # 如果文件路径不存在，需要先建立文件路径
    if not os.path.isfile(path_new):
        os.makedirs(os.path.dirname(path_new))
        pass
    file_new = open(path_new, 'w', encoding='utf-8')
    with open(path, 'r') as f:
        for line in f:
            file_new.write(line)
            pass
        pass
    file_new.close()
    pass


def get_all_files(path):
    """
    获取文件夹中所有的文件的路径
    :param path:
    :return:
    """
    all_files = []
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # 完整路径
            file_path_old = os.path.join(parent, filename).replace('\\', '/')
            all_files.append(file_path_old)
            pass
        pass
    return all_files


def modify_charset():
    path_sour='D:/test-dir'
    path_dest='D:/test-dir-backup'
    # 先copy一份，然后用copy后的作为源文件，copy前的作为目的文件，重新用utf-8格式写
    copy_file_dir(path_sour, path_dest)
    # 先清空原来的文件夹？
    rewrite_file_dir(path_dest, path_sour)
    pass


def te_sth():
    """
    用来测试一些东西
    :return:
    """
    pass

if __name__ == "__main__":

    modify_charset()
    # te_sth()
    pass

