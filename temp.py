import ftplib
# import paramiko
import os
import configparser
import datetime
import hashlib
import re
from file.file_operatioV4 import get_all_files


def compare_file_md5_win(file1_path, file2_path):
    """
    success
    调用windows命令比较文件md5值。经测试11G的mp4文件计算md5要用60s。不用担心内存不够。
    :return: False or True
    """
    comm_info1 = os.popen('certutil -hashfile ' + file1_path + ' md5').readlines()
    md5_val1 = '1'
    md5_val2 = '2'
    print(comm_info1)
    if len(comm_info1)==3:
        md5_val1 = comm_info1[1]
        pass
    else:
        return False
    comm_info2 = os.popen('certutil -hashfile ' + file2_path + ' md5').readlines()
    print(comm_info2)
    if len(comm_info2)==3:
        md5_val2 = comm_info2[1]
        pass
    if md5_val1 == md5_val2:
        return True
    else:
        return False


def compare_file_md5_py(file1_path, file2_path):
    """
    success
    比较文件md5值。用的是python自带的库，如果文件太大会报MemoryError
    :return: False or True
    """
    hash1 = '0'
    hash2 = '1'
    with open(file1_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash1 = md5obj.hexdigest()
        print(hash1)
    with open(file2_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash2 = md5obj.hexdigest()
        print(hash2)
    if hash1 == hash2:
        return True
    else:
        return False


if __name__ == "__main__":
    file1_path = 'Dhttp:/test_dir/1.txt'
    file2_path = 'http:/test_dir/2.txt'
    # file2_path = 'D:/file-all/file-history/玖富/2017年会-跨年盛典全程.mp4'

    # time1 = datetime.datetime.now()
    # print(time1)
    # if re.search('.txt|.mp4|.jpg|.png', file1_path) is not None:
    #     print('searched')
    #     pass
    # print('file1:', file1_path.find('http'))
    # print('file2:', file2_path.find('http'))

    file_path_all = get_all_files('D:\\temp\\testdir')
    for file_path in file_path_all:
        os.rename(file_path, file_path.replace('发现自己舔的女神是别人的舔狗是种怎样的体验', '你喜欢的人和别人发生了关系你有什么感受'))
        pass

    pass

