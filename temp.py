import ftplib
# import paramiko
import os
import configparser
import datetime
import hashlib
import re
from file.file_operatioV4 import get_all_files
from socket import *


def rename_all_files():
    file_path_all = get_all_files('D:\\temp\\testdir')
    for file_path in file_path_all:
        os.rename(file_path, file_path.replace('发现自己舔的女神是别人的舔狗是种怎样的体验', '你喜欢的人和别人发生了关系你有什么感受'))
        pass
    pass

def find_str_in_files():
    # dir_path = 'D:\\file_all\\file_life\\世相\\知乎\\舔狗到底有多卑微_爬虫_v1'
    # dir_path = 'D:\\file_all\\file_life\\世相\\知乎\\舔狗到底有多卑微_300415423_爬虫_v1'
    # dir_path = 'D:\\file_all\\file_life\\世相\\知乎\\你喜欢的人和别人发生了关系 你有什么感受_爬虫_v1'
    dir_path = 'D:\\file_all\\file_life\\世相\\知乎\\发现自己舔的女神是别人的舔狗是种怎样的体验_爬虫_v1'
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            ext_name = filename[filename.rfind('.')+1:]
            # print('ext_name:', ext_name)
            if ext_name != 'txt':
                continue
            # 完整路径
            file_path_old = os.path.join(parent, filename).replace('\\', '/')
            # print(file_path_old)
            with open(file_path_old, 'r', encoding='gb18030') as fp_content:
            # with open(file_path_old, 'r', encoding='utf-8') as fp_content:
                while True:
                    text_line = fp_content.readline()
                    if text_line:
                        if text_line.find('生理')!=-1:
                            print('find:', file_path_old)
                            with open('D:\\temp\\testdir\\find_files.txt', 'a+', encoding='gb18030') as fp_find:
                                fp_find.write(file_path_old + '\n')
                                pass
                            pass
                    else:
                        break
                pass
            pass
        pass
    pass


def anagramSolution1(s1, s2):
    if len(s1)!=len(s2):
        return False
    alist = list(s2)  # 复制s2
    pos1 = 0
    stillok = True
    while pos1 < len(s1) and stillok:  # 循环s1的所有字符
        pos2 = 0
        found = False  # 初始化标识符
        while pos2 < len(alist) and not found:  # 与s2的字符逐个对比
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None  # 找到对应，标记
        else:
            stillok = False  # 没有找到，失败
        pos1 = pos1 + 1
    return stillok


if __name__ == "__main__":
    # file2_path = 'D:/file-all/file-history/玖富/2017年会-跨年盛典全程.mp4'

    # time1 = datetime.datetime.now()
    # print(time1)
    # if re.search('.txt|.mp4|.jpg|.png', file1_path) is not None:
    #     print('searched')
    #     pass
    # print('file1:', file1_path.find('http'))
    # print('file2:', file2_path.find('http'))

    # find_str_in_files()

    # print(anagramSolution1('abcd', 'dcb'))
    # print(anagramSolution2('abc', 'dcba'))
    HOST = '192.168.246.129'  # or 'localhost'
    PORT = 3690
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    print('end')

    pass

