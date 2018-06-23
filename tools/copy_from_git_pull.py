# -*- coding: utf-8 -*-
# import file.file_operatioV4
from file import file_operatioV4
# from file.file_operatioV4 import copy_file_dir


def backup_dir(local_dir_path):

    pass


def copy_dir():
    pass


def backup_copy_dir():
    pass

if __name__ == "__main__":
    sour_dir_path = 'D:/file-all/file-life/ip/git/transfer/common edit'
    dest_dir_path = 'D:/file-all/file-life/ip/note/common edit'
    file_operatioV4.copy_file_dir(dest_dir_path)
    file_operatioV4.copy_file_dir(sour_dir_path, dest_dir_path)
    # copy_file_dir(dest_dir_path)
    pass
