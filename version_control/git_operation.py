# -*- coding: utf-8 -*-
# pip install gitpython
import git
import datetime

"""
success
"""


def add_commit_push(repo_dir_path, comment):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if comment==None:
        comment = timestamp
    # git仓库根目录
    repo = git.Repo(repo_dir_path)
    print('add', repo.git.execute('git add .'))
    print('commit', repo.git.execute('git commit -m "' + comment +'"'))
    print('push', repo.git.execute('git push origin master'))
    pass


if __name__ == "__main__":
    pass
