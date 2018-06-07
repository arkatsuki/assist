import os
import shutil
import io.xml_util
# from io import xml_util

dir_path_sour = r'D:\workspace\eclipse-oxygen\p_web'
dir_path_dest = r'D:\workspace\eclipse-oxygen\p_web2'

if os.path.exists(dir_path_dest):
    # os.removedirs不能删除非空文件夹，shutil.rmtree可以
    # os.removedirs(dir_path_dest)
    shutil.rmtree(dir_path_dest)

# 这种复制，两文件的时间属性都不变
shutil.copytree(dir_path_sour, dir_path_dest)

"""
修改pom
修改.project
"""

# 递归遍历文件夹
for parent, dirnames, filenames in os.walk(dir_path_dest):
    for filename in filenames:
        file_path = os.path.join(parent, filename);
        print('filenames:',filename)
        if filename == 'pom.xml':
            file_path = r'D:\workspace\eclipse-oxygen\p_web2\pom.xml'
            content_dict = {}
            content_dict['groupId'] = 'groupId222'
            content_dict['artifactId'] = 'artifactId222'
            content_dict['source'] = 'source222'
            content_dict['target'] = 'target222'

            io.xml_util.set_tag_content(file_path, content_dict)
            pass
        pass

    for dirname in dirnames:
        print('dirname:',dirname)
        pass