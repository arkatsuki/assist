"""
修改文件内容。
replace_str：替换文件中的某个字符串，不支持跨行的情况。
replace_config：替换文件中的某个字符串，不支持跨行的情况
"""


def replace_str(file_path, old_str, new_str):
    """
    success
    替换文件中的某个字符串，不支持跨行的情况。
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


def replace_config(file_path, key, value):
    """
    success
    替换文件中的某个字符串，不支持跨行的情况
    :param file_path: 文件绝对路径
    :param new_str: 新字符串
    :param old_str: 旧字符串
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


if __name__ == "__main__":
    # p = r'E:\github\zheng\zheng-cms\zheng-cms-admin\src\main\resources\profiles\dev.properties'
    # old_str = 'rdserver'
    # new_str = '192.168.159.128'
    # replace_str(p, new_str, old_str)
    pass
