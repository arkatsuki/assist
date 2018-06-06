
"""
ok
"""

def remove_multiple_comment(file_path, start_symbol, end_symbol):
    """
    删除多行注释，
    也可以用fileinput
    :param file_path:   绝对路径
    :param start_symbol: 开始符号
    :param end_symbol: 结束符号
    :return:
    """
    output = []
    with open(file_path, 'r+', encoding="utf-8") as f:
        for line in f.readlines():
            if line.strip().endswith(end_symbol):
                # 如果是单行，不需要删除之前的
                if line.strip().startswith(start_symbol):
                    continue
                else:
                    while not output.pop().strip().startswith(start_symbol):
                        continue
            else:
                output.append(line)
        pass
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(''.join(output))  # write的参数需要是字符串，不能是List
