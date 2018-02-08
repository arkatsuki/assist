
import os
import configparser


def compare_list(list1, list2):
    file_path_different_list = []  # 存放不一致的文件
    for elem in list1:
        if elem.strip() not in list2:
            file_path_different_list.append(elem.strip())
            file_path_different_list.append('\n')
        else:
            try:
                list2.remove(elem.strip())
            except Exception:  # KeyError    ValueError
                # line有可能重复，此时file_all_set已经删除这个key了，就报KeyError
                print('Exception, line:', elem.strip())
        pass

    # 如果有两个一样的行，少了一行也算少
    file_path_different_list.append('少了')
    file_path_different_list.append('\n')
    file_path_different_list.extend('\n'.join(list2))
    print(''.join(file_path_different_list)) # 参数需要是字符串，不能用list
    # with open('D:/out.txt', 'w', encoding='utf-8') as f:
    #     f.write(''.join(file_path_different_list))  # write的参数需要是字符串，不能是List
    pass


def compare_file(file1_path, file2_path):
    file1_list = []
    file2_list = []
    with open(file1_path, 'r') as f:
        for line in f:
            file1_list.append(line.strip())
            pass
        pass
    with open(file2_path, 'r') as f:
        for line in f:
            file2_list.append(line.strip())
            pass
        pass
    compare_list(file1_list, file2_list)
    pass

if __name__ == "__main__":

    file1 = 'D:/file_submit.txt'
    file2 = 'D:/file_self.txt'
    compare_file(file1, file2)
    pass
