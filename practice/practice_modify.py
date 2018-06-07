import os

"""
ok
"""
# dir_path = r'E:\git\ljs\ljs\ljs-app-api'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-business\ljs-business-provider'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-business\ljs-business-api'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-common'
# dir_path = r'E:\git\ljs\ljs\ljs-data-transfer'
# dir_path = r'E:\git\ljs\ljs\ljs-portal'
# dir_path = r'E:\git\ljs\ljs\ljs-task'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-uc-api'
# dir_path = r'E:\git\ljs\ljs\ljs-wap'
# dir_path = r'E:\git\ljs-eclipse\ljs\ljs-web'

dir_path_list = [r'E:\git\ljs-eclipse\ljs\ljs-app-api',
                 r'E:\git\ljs-eclipse\ljs\ljs-business\ljs-business-provider',
                 r'E:\git\ljs-eclipse\ljs\ljs-business\ljs-business-api',
                 r'E:\git\ljs-eclipse\ljs\ljs-common',
                 r'E:\git\ljs-eclipse\ljs\ljs-data-transfer',
                 r'E:\git\ljs-eclipse\ljs\ljs-portal',
                 r'E:\git\ljs-eclipse\ljs\ljs-task',
                 r'E:\git\ljs-eclipse\ljs\ljs-uc-api',
                 r'E:\git\ljs-eclipse\ljs\ljs-wap',
                 r'E:\git\ljs-eclipse\ljs\ljs-web']



def delete_str(file_path):

    output = []
    # print('file_path:',file_path)

    with open(file_path, 'r+', encoding="utf-8") as f:
        doing = 0
        for line in f.readlines():
            print('line:',line)
            idx = line.find(r'/ljs/ljs-lib')
            if idx != -1:
                if line.find('<classpathentry') != -1:
                    if  line.find('</classpathentry>') == -1 and line.find('/>') == -1:
                        doing = 1
                        print('doing = 1')
                        continue
                        pass
                    else:
                        doing = 0
                        continue

            if doing == 0:
                print('append')
                output.append(line)
            elif line.find('<classpathentry') == -1 and line.find('</classpathentry>') != -1:
                print('set doing == 0')
                doing = 0

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(''.join(output))  # write的参数需要是字符串，不能是List

# for parent,dirnames,filenames in os.walk(dir_path):
#     for filename in filenames:
#         if filename == '.classpath':
#             delete_str(os.path.join(parent, filename))
#         pass

def traversal(dir_path):
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename == '.classpath':
                delete_str(os.path.join(parent, filename))
            pass

for path in dir_path_list:
    traversal(path)

