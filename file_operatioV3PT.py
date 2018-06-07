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
pass
将指定目录下的所有文件改写成utf-8编码。源目录会先进行备份。
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

def get_charset():
    """
    检测数据的编码类型
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
            rewrite_file_all_code(file_path, file_path_new)
            pass
        pass
    else:
        print('rewrite_file_dir, not dir')
        rewrite_file_all_code(path, path_new)
        pass
    pass


def rewrite_file_all_code(path, path_new):
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

    # 获取编码方式
    f = open(path_new, 'rb')
    data = f.read()
    # data = f.read(20)
    print(chardet.detect(data))
    charset_dict = chardet.detect(data)
    encoding = charset_dict['encoding']
    print('encoding:', encoding)
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
    """
    把指定目录下的所有文件改成utf-8编码。源文件夹先会备份。
    :return:
    """
    # path_sour='D:/test-dir'
    # path_sour='D:/test-sth/test-dir'
    # path_dest='D:/test-sth/test-dir-backup'
    path_sour='D:/test-sth/note-txt'
    # 先copy一份，然后用copy后的作为源文件，copy前的作为目的文件，重新用utf-8格式写
    # copy_file_dir(path_sour, path_dest)
    # 先清空原来的文件夹？
    # rewrite_file_dir(path_dest, path_sour)
    rewrite_file_dir(copy_file_dir(path_sour), path_sour)
    pass


def compare_file():
    """
    逐个字节比较文件内容
    :return:
    """
    file1_path = 'd:/LnAppCalcInfoServiceImpl1111.class'
    # file2_path = 'd:/LnAppAttachInfoServiceImpl.class'
    file2_path = 'd:/LnAppCalcInfoServiceImpl.class'
    file1 = open(file1_path, 'rb')
    file2 = open(file2_path, 'rb')
    # with open(file2_path, 'rb') as file2:
    #     file1.read()
    #     pass
    print('size:', os.path.getsize(file1_path))
    for i in range(0, os.path.getsize(file1_path)):
        # print(i)  # 到size-1
        file1.read(i)
        pass
    file1.close()
    file2.close()


    pass

if __name__ == "__main__":
    # modify_charset()
    compare_file()
    pass

