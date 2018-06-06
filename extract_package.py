import ftplib
import paramiko
import os
import configparser


def get_files_from_dir():
    path_dir = r'D:\抽取代码路径.txt'
    os.read(path_dir)
    pass

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config-uncommit.ini')

    pass

