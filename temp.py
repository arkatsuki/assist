import ftplib
# import paramiko
import os
import configparser
import datetime
import hashlib
import re
from file.file_operatioV4 import get_all_files


def rename_all_files():
    file_path_all = get_all_files('D:\\temp\\testdir')
    for file_path in file_path_all:
        os.rename(file_path, file_path.replace('发现自己舔的女神是别人的舔狗是种怎样的体验', '你喜欢的人和别人发生了关系你有什么感受'))
        pass
    pass

def find_str_in_files():
    dir_path = 'D:\\file_all\\file_life\\世相\\知乎\\舔狗到底有多卑微_爬虫_v1'
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            ext_name = filename[filename.rfind('.')+1:]
            # print('ext_name:', ext_name)
            if ext_name != 'txt':
                continue
            # 完整路径
            file_path_old = os.path.join(parent, filename).replace('\\', '/')
            print(file_path_old)
            with open(file_path_old, 'r', encoding='gb18030') as fp_content:
            # with open(file_path_old, 'r', encoding='utf-8') as fp_content:
                while True:
                    text_line = fp_content.readline()
                    if text_line:
                        if text_line.find('生理需求')!=-1:
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

    find_str_in_files()

    pass

