import os
from shutil import copy

dir_path = r'E:\git\ljs-eclipse\ljs'
dir_dest_path = r'E:\temp\auto\classpath2'

for parent,dirnames,filenames in os.walk(dir_path):
    for filename in filenames:
        # if filename == '.classpath':
        if filename == '.classpath':
            dest_dir_name_list = parent.split('\\')
            dest_dir_name = dest_dir_name_list[len(dest_dir_name_list) - 1]
            print('dest_dir_name:',dest_dir_name)
            print('file:',os.path.join(parent, filename))
            # print('dest:', dir_dest_path + dest_dir_name)
            # res = os.path.exists(dir_dest_path)
            # print('res:',res)
            # if not os.path.exists(dir_dest_path):
            #     os.mkdir(dir_dest_path)
            #     pass
            copy(os.path.join(parent, filename), os.path.join(dir_dest_path, dest_dir_name))
            pass
        pass
# for parent,dirnames,filenames in os.walk(dir_path):
#     print(dirnames)
#     print(filenames)
#     pass
