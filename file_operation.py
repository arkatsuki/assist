# -*- coding: utf-8 -*-

import ftplib
import paramiko
import os
import configparser
import chardet
import json
import time
import datetime


def backup(path):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = 'timestamp'
    if os.path.isfile(path):
        # echo yes|copy "D:/test-file.txt" "D:/test-file.txt.bak"
        # cmd = 'echo yes|copy "' + path + '" "' + path + '.' + timestamp + '"'
        cmd = 'echo yes|copy "D:/test-file.txt" "D:/test-file1111.txt"'
        print('cmd:', cmd)
        rs = os.popen(cmd)
        # rs = os.popen('echo yes|copy "' + path + '" "' + path + '' + timestamp + '"')
        # print(chardet.detect(rs.read()))
        print(rs.read())
        backup_name = path + '.' + timestamp
        pass
    else:
        # echo d|xcopy "D:/test-dir" "D:/test-dir.bak" /e
        cmd = 'echo d|xcopy "' +path + '" "' +path + '-' + timestamp + '" /e'
        print('cmd:',cmd)
        rs = os.popen(cmd)
        print(rs.read())
        backup_name = path + '-' + timestamp
        pass
    return backup_name
    pass

def get_charset():
    dir_path='D:/test-file.txt'
    f=open(dir_path,'rb')
    data=f.read()

    # print('data:',data.decode())
    print(chardet.detect(data))
    # charset_dict=json.loads(chardet.detect(data))
    charset_dict=chardet.detect(data)
    print(charset_dict['encoding'])

    pass

def copy_file(path, path_new):
    if os.path.isdir(path):
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                # 完整路径
                file_path_old = os.path.join(parent, filename).replace('\\', '/')
                print('file_path_old:',file_path_old)
                file_path_new = file_path_old.replace(path, path_new)
                pass
            pass
        pass
    else:
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
    pass

def modify_charset():
    # 先把源文件改名，然后读取改名后的文件
    # dir_path='D:/test-file.txt'
    # bak_dir_path = dir_path + '.bak'
    # os.rename(dir_path, bak_dir_path)
    # file_new = open(dir_path, 'w', encoding='utf-8')
    # # line_list=[]
    # with open(bak_dir_path, 'r') as f:
    #     for line in f:
    #         # line_list.append(line.strip())
    #         file_new.write(line)
    #         pass
    #     pass
    # file_new.close()
    dir_path='D:/test-dir'
    backup_name = backup(dir_path)

    pass

if __name__ == "__main__":
    # modify_charset()
    dir_path = 'D:/test-dir'
    file_path = 'D:/test-file.txt'
    t=time.time()
    print(int(t))
    print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    # backup(dir_path)
    # backup(file_path)
    file_path2 = 'D:/testtt/testsub/test-file.txt'
    # file_new = open('', 'w', encoding='utf-8')
    # file_new.write('test')
    # file_new.close()
    print(os.path.dirname(file_path2))
    os.makedirs(os.path.dirname(file_path2))
    pass

