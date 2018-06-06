import xlwt
import time

def write_excel(row_info_all_fun, out_put_info_excel_path):
    """
    将一个保存excel数据的二维数组写成excel
    :param row_info_all_fun: 一个二维数组，第一维元素是保存行信息的数组，第二维元素是每行的每个单元格的数据
    :param out_put_info_excel_path: 输出的excel路径
    :return:
    """
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('cnweb_ss', cell_overwrite_ok=True)
    for i in range(0, len(row_info_all_fun)):
        for j in range(0, len(row_info_all_fun[i])):
            sheet1.write(i, j, row_info_all_fun[i][j])
    book.save(out_put_info_excel_path)


def check_path_exists (new_path_info, version_num, version_path_dict,
                       path_version_list_a, path_version_list_m):
    """
    校验是否已经存在版本号更大的路径
    新增的文件，后续提交是修改，此时需要把 M 改成 A
    :param new_path_info:待校验的路径
    :param version_num: 版本号
    :param version_path_dict: 一个dict，key是版本号，value是该版本号对应所有路径的数组
    :return:
    """
    for k, v in version_path_dict.items():
        for old_path_info in v:
            if old_path_info[1:]==new_path_info[1:] and k>version_num:
                # 新增的文件，后续提交是修改，此时需要把 M 改成 A
                # print('already exists')
                # 如果高版本是D就不管
                if new_path_info[0] == 'A' and old_path_info[0]=='M':
                    new_path_info = 'A' + new_path_info[1:]
                    # print('new_path_info:',new_path_info,version_num)
                    # print('old_path_info:', old_path_info, k)
                    # version_path_dict[k].append('A' + new_path_info[1:])
                    # print('len:',len(version_path_dict[k]))
                    # print('version_path_dict[k]:',version_path_dict[k])
                    # version_path_dict[k].remove(old_path_info)
                    # print('len:', len(version_path_dict[k]))
                    # print('version_path_dict[k]:', version_path_dict[k])
                return True
            else:
                continue
    return False

def compare_path(file_path_all_list_fun, compare_file_path_fun, out_put_diff_info_txt_path):
    file_path_different_list = []  # 存放不一致的文件
    with open(compare_file_path_fun, 'r') as f:
        file_path_different_list.append('多了')
        file_path_different_list.append('\n')
        for line in f:
            # li = line.split('\t')  # 如果是从excel中复制出来两列，可以用\t分割
            # for item in li:
            #     print(item)
            # line会包含\n
            if line.strip() not in file_path_all_list_fun:
                file_path_different_list.append(line.strip())
                file_path_different_list.append('\n')
            else:
                try:
                    file_path_all_list_fun.remove(line.strip())
                except Exception:    # KeyError    ValueError
                    # line有可能重复，此时file_all_set已经删除这个key了，就报KeyError
                    print('Exception, line:', line.strip())
    file_path_different_list.append('少了')
    file_path_different_list.append('\n')
    file_path_different_list.extend('\n'.join(file_path_all_list_fun))
    with open(out_put_diff_info_txt_path, 'w', encoding='utf-8') as f:
        f.write(''.join(file_path_different_list))  # write的参数需要是字符串，不能是List

def put_original_path(original_file_path, current_base_info, version_path_dict):
    for old_version_num, v in version_path_dict.items():
        for old_path_info_all in v:
            old_path_info_arr = old_path_info_all.split('&')
            # 如果已经存在路径，不管版本号和提交人
            if old_path_info_arr[2]==original_file_path[1:]:
                # 如果已经存在的版本号大，需要判断是否需要修改提交动作（M/A/D）
                if old_version_num>current_base_info[0]:
                    if original_file_path[0] == 'A' and old_path_info_arr[0]=='M':
                        # 只用改第一个字符提交动作，后面的不用改
                        version_path_dict[old_version_num].append('A' + old_path_info_all[1:])
                        version_path_dict[old_version_num].remove(old_path_info_all)
                        return
                    pass
                # 如果已经存在的版本号小，需要修改成大的版本号。暂时不需要考虑这种情况！！！
                else:
                    pass
            else:
                continue

    action = original_file_path[0]
    file_path_info_all = action + '&' + original_file_path[1:] + '&' + current_base_info[0] + '&' + \
                         current_base_info[1]
    # if action == 'A':
    #     path_version_list_a.append(file_path_info_all)
    # elif action == 'M':
    #     path_version_list_m.append(file_path_info_all)
    # elif action == 'D':
    #     path_version_list_d.append(file_path_info_all)
    if not current_base_info[0] in version_path_dict.keys():
        version_path_dict[current_base_info[0]] = []
        pass
    version_path_dict[current_base_info[0]].append(file_path_info_all)

def format_output(pathItem, current_base_info_fun, branch_name,
                  output, row_info_all, file_path_all_list):
    # 格式化，并写txt文件
    output.append(current_base_info_fun[0])  # 版本号
    output.append('\t')
    output.append(current_base_info_fun[1])  # 提交人
    output.append('\t')

    action = pathItem[0]

    path_item_path = pathItem[1:]
    idx_dev = path_item_path.find(branch_name)
    path_item_path = path_item_path[idx_dev:]

    output.append(action)
    output.append('\t')
    output.append(path_item_path)

    output.append('\n')

    # 用于写excel
    row_info_signal = []
    row_info_signal.append(path_item_path)
    if action=='A':
        action='新增'
    elif action=='M':
        action='修改'
    elif action=='D':
        action='删除'
    row_info_signal.append(action)
    current_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))
    row_info_signal.append(current_date)  # 时间
    row_info_signal.append('')  # 备注
    row_info_signal.append(current_base_info_fun[1])  # 提交人
    row_info_signal.append(current_base_info_fun[0])  # 版本号
    row_info_all.append(row_info_signal)

    # 存放所有路径，用于比较是否漏/多路径
    file_path_all_list.append(path_item_path)
    return output, row_info_all, file_path_all_list


def format_output_list(path_version_list_fun, branch_name,
                  output, row_info_all, file_path_all_list):
    for item in path_version_list_fun:
        item_list = item.split('&')
        format_output(item_list[0], item_list[1:], branch_name,
                  output, row_info_all, file_path_all_list)
