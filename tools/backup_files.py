# -*- coding: utf-8 -*-
import datetime
from file import file_operatioV4


def find_diff():
    # dir1_path = 'D:/test_dir/a1'
    # dir2_path = 'D:/test_dir/b1'
    # dir1_path = 'H:/file/picture'
    dir1_path = 'D:/file-all/file-life'
    # dir2_path = 'G:/file-life'
    dir2_path = 'F:/all/file-life'

    # dir1_path = 'D:/file-all/file-common'
    # dir2_path = 'G:/file-common'

    # dir1_path = 'D:/file-all/file-dev'
    # dir2_path = 'G:/file-dev'

    time1 = datetime.datetime.now()
    file_operatioV4.compare_dir(dir1_path, dir2_path)
    time2 = datetime.datetime.now()
    print(time1)
    print(time2)

    # file1 = 'D:/test_dir/1.txt'
    # with open(file1, 'r', encoding='utf-8') as f:
    #     for path in f:
    #         path = path.strip(' ').strip('\n').strip('\ufeff')
    #         print('path:', path)
    #         os.remove(path)
    #         # c = input('y or n')
    #         # if c == 'y':
    #         #     os.remove(path)
    #         #     pass
    #         pass
    #     pass
    pass


if __name__ == "__main__":
    find_diff()
    pass
