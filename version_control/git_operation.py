# -*- coding: utf-8 -*-
# pip install gitpython
import git
import datetime

"""
success
"""


def add_commit_push(repo_dir_path, comment=None):
    """
    success
    :param repo_dir_path:
    :param comment:
    :return:
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if comment is None:
        comment = timestamp
    # git仓库根目录
    repo = git.Repo(repo_dir_path)
    # print('reset', repo.git.execute('git reset --hard'))
    # print('clean', repo.git.execute('git clean -df'))
    rs = repo.git.execute('git add .')
    print('add', rs)
    rs = repo.git.execute('git status')
    print('status', rs)
    if rs.index('nothing to commit') == -1:
        print('commit', repo.git.execute('git commit -m "' + comment + '"'))
        print('push', repo.git.execute('git push origin master'))
        pass

    pass


def pull(repo_dir_path, comment):
    # git仓库根目录
    repo = git.Repo(repo_dir_path)
    print('pull', repo.git.execute('git pull'))
    pass


if __name__ == "__main__":
    pass
