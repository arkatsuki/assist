import os
from shutil import copy

dir_path = r'E:\git\ljs-eclipse\ljs'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-web'
dir_dest_path = r'E:\temp\auto\classpath2'
# dir_dest_path = r'C:\Users\duanyaochang\Desktop\temp\auto\build-gradle'

def recover(filename_proj,file_backup_path):
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # if filename == '.classpath':
            # print('filename:',filename)
            if filename == '.classpath':
                dest_dir_name_list = parent.split('\\')
                dest_dir_name = dest_dir_name_list[len(dest_dir_name_list) - 1]
                # print('dest_dir_name:', dest_dir_name)
                if dest_dir_name == filename_proj:
                    print('from:', file_backup_path)
                    print('to:', os.path.join(parent, filename))
                    copy(file_backup_path, os.path.join(parent, filename))
                    pass
                pass
            pass

for parent,dirnames,filenames in os.walk(dir_dest_path):
    for filename in filenames:
        if filename == 'ljs':
            proj_dir = os.path.join(dir_path, '.classpath')
        else:
            proj_dir = os.path.join(dir_path, filename, '.classpath')
            recover(filename,os.path.join(parent, filename))
        pass
    pass




