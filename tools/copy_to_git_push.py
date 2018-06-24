# -*- coding: utf-8 -*-
# import file.file_operatioV4
from file import file_operatioV4
# from file.file_operatioV4 import copy_file_dir
# pip install gitpython
from git import repo
import git
from version_control.git_operation import add_commit_push

"""
success
"""


def push(repo_dir_path):
    add_commit_push(repo_dir_path)
    pass


if __name__ == "__main__":
    sour_dir_path = 'D:/file-all/file-life/ip/note/common edit'
    dest_dir_path = 'D:/file-all/file-life/ip/git/transfer2/common edit'
    # 先备份
    file_operatioV4.copy_file_dir(sour_dir_path)
    file_operatioV4.copy_file_dir(sour_dir_path, dest_dir_path)

    repo_dir_path = 'D:/file-all/file-life/ip/git/transfer2'
    push(repo_dir_path)
    pass
