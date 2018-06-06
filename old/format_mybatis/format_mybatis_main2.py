from format_mybatis.format_mybatis_function import *
import os

"""
ok
"""
# file_path = r'E:\workplace-eclipse-0706\workplace-dev\mybatis-app\src\main\java\com\sl\preloan\model\SsOperationRecord.java'

# dir_path = r'E:\workplace-eclipse-0706\workplace-dev\mybatis-app\src\main\java\com\sl\preloan'

dir_path = r'C:\Users\Jiufu\Desktop\手机品牌导入\ProductSeries.java'

# project_dir = r'E:\workplace-eclipse-0706\workplace-dev\cnweb_ss'

remove_multiple_comment(dir_path, '/*', '*/')

# for parent,dirnames,filenames in os.walk(dir_path):
#     for filename in filenames:
#         remove_multiple_comment(os.path.join(parent,filename), '/*', '*/')
#         remove_multiple_comment(os.path.join(parent, filename), '<!--', '-->')

