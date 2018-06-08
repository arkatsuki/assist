from old.format_mybatis.modify_file_function import *
import os

"""
ok
"""

dir_path = r'E:\github\zheng'
old_str = 'master.redis.password=admin'
new_str = 'master.redis.password=admin\n'
config_dict = {'master.redis.password':'INTCvFvDmSsW99oliOHm7A==',
               'master.redis.ip':'192.168.159.128'
               }

for parent,dirnames,filenames in os.walk(dir_path):
    for filename in filenames:
        if filename.endswith('.properties'):
            # print('filename:',filename)
            replace_str(os.path.join(parent,filename), old_str, new_str)

# for parent,dirnames,filenames in os.walk(dir_path):
#     for filename in filenames:
#         if filename.endswith('.properties'):
#             # print('filename:',filename)
#             replace_str(os.path.join(parent,filename), old_str, new_str)
#             for k,v in config_dict.items():
#                 replace_config(os.path.join(parent,filename), k, v)

