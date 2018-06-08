import os

def delete_str(str, file_path):
    pass


def replace_str(file_path, old_str, new_str):
    """
    替换文件中的某个字符串，不支持跨行的情况
    如果是刪除，替换为空字符串就行
    :param file_path: 文件绝对路径
    :param new_str: 新字符串
    :param old_str: 旧字符串
    :return:
    """
    output = []
    # print('file_path:',file_path)
    with open(file_path, 'r+', encoding="utf-8") as f:
        for line in f.readlines():
            idx = line.find(old_str)
            if idx != -1:
                print('file_path:', file_path)
                print('old line:', line)
                line = line.replace(old_str, new_str)
                print('new line:', line)
            output.append(line)

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(''.join(output))  # write的参数需要是字符串，不能是List


def update_config(file_path, key, value):
    """
    修改.properties文件里面某个key的value，必须是key=value的形式，必须是单独占一行
    :param file_path:
    :param key:
    :param value:
    :return:
    """
    output = []
    # print('file_path:',file_path)
    with open(file_path, 'r+', encoding="utf-8") as f:
        for line in f.readlines():
            idx = line.find(key)
            if idx != -1:
                print('file_path:', file_path)
                print('old line:', line)
                line = key + '=' + value + '\n'
                print('new line:', line)
            output.append(line)

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(''.join(output))  # write的参数需要是字符串，不能是List

dir_path = r'D:\temp\test'

# 递归遍历文件夹
for parent, dirnames, filenames in os.walk(dir_path):
    for filename in filenames:
        # 拼接文件完整路径
        file_path = os.path.join(parent, filename);
        if filename == '':
            pass
        replace_str(file_path, "ok", '')
        pass
