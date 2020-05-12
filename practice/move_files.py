# -*- coding: utf-8 -*-
import datetime
# from file import file_operatioV4
import shutil
import os


def move_files_specify():
    """
    把指定文件夹下面rmrb/sztqb开头的文件移动到对应的存档文件夹下面
    :return:
    """
    # sor_dir1_path = 'D:/temp/test_dir/a1'
    # rmrb_dir2_path = 'D:/temp/test_dir/b1'
    # sztqb_dir2_path = 'D:/temp/test_dir/c1'
    sor_dir1_path = 'D:/迅雷下载'
    rmrb_dir2_path = 'D:/file_all/file_common/gwy/报纸存档/人民日报'
    sztqb_dir2_path = 'D:/file_all/file_common/gwy/报纸存档/深圳特区报'

    for parent, dirnames, filenames in os.walk(sor_dir1_path):
        for filename in filenames:
            file_path_old = os.path.join(parent, filename)
            if filename.find('rmrb')!=-1:
                print('filename:', filename)

                shutil.move(file_path_old, rmrb_dir2_path)
                pass
            elif filename.find('sztqb')!=-1:
                print('filename:', filename)
                shutil.move(file_path_old, sztqb_dir2_path)
                pass

            pass
        pass

    os.popen('start ' + sor_dir1_path)
    os.popen('start ' + rmrb_dir2_path)
    os.popen('start ' + sztqb_dir2_path)
    pass


if __name__ == "__main__":
    move_files_specify()
    pass
