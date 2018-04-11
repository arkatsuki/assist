
import excel_operation
import re
import assist_util


def filter_rule2(data_dict):
    """
    有点问题，效果不对
    :param data_dict:
    :return:
    """
    for sheet_name, sheet_data in data_dict.items():
        title = sheet_data[0]
        for row_list in sheet_data:
            match = False
            for cell_data in row_list:
                # print('cell_data1:',cell_data)
                if type(cell_data) == str and cell_data.strip().find('深圳') > 0:
                    print('cell_data:',cell_data)
                    match = True
                    break
                pass
            if not match:
                print('not match')
                sheet_data.remove(row_list)
                pass
            data_dict[sheet_name] = sheet_data
            pass
        pass
    return data_dict


def filter_rule3(data_dict):
    """
    按规则过滤excel数据，返回一个dict，key是sheet的name，value是表示行列的二维数组
    :param data_dict: 一个dict，key是sheet的name，value是表示行列的二维数组
    :return:
    """
    rs_dict = {}  # 用于返回
    for sheet_name, sheet_data in data_dict.items():
        rs_dict[sheet_name] = []
        rs_dict[sheet_name].append(sheet_data[0])
        for row_list in sheet_data:
            rs_dict[sheet_name].append(row_list)

            pass
        pass
    return rs_dict


def filter_rule4(data_dict):
    """
    按规则过滤excel数据，返回一个dict，key是sheet的name，value是表示行列的二维数组
    :param data_dict: 一个dict，key是sheet的name，value是表示行列的二维数组
    :return:
    """
    rs_dict = {}  # 用于返回
    for sheet_name, sheet_data in data_dict.items():
        rs_dict[sheet_name] = []
        rs_dict[sheet_name].append(sheet_data[0])
        rs_dict[sheet_name].append(sheet_data[3])
        for row_list in sheet_data:
            print('row_list[10]:',row_list[10])
            # 正则表达式，包含A或者B
            if type(row_list[10]) == str and re.match('A|B', row_list[10]):
                print('find A')
                rs_dict[sheet_name].append(row_list)
                pass
            pass
        pass
    return rs_dict


def filter_rule5(data_dict):
    """
    按规则过滤excel数据，返回一个dict，key是sheet的name，value是表示行列的二维数组
    :param data_dict: 一个dict，key是sheet的name，value是表示行列的二维数组
    :return:
    """
    rs_dict = {}  # 用于返回

    for sheet_name, sheet_data in data_dict.items():
        rs_dict[sheet_name] = []
        rs_dict[sheet_name].append(sheet_data[0])
        rs_dict[sheet_name].append(sheet_data[3])
        for row_list in sheet_data:
            print('row_list[10]:',row_list[10])
            # 正则表达式，包含A或者B
            if type(row_list[10]) == str and re.match('A|B', row_list[10]):
                print('find A')
                rs_dict[sheet_name].append(row_list)
                pass
            pass
        pass
    return rs_dict

if __name__ == "__main__":
    # excel_read_path = r'C:\Users\duanyaochang\Desktop\temp\2017gj.xls'
    # excel_write_path = r'C:\Users\duanyaochang\Desktop\temp\2017gj222.xls'
    excel_read_path = r'D:\000001.xlsx'
    excel_write_path = r'D:\000002.xls'
    # data_list = excel_operation.read_excel(excel_read_path)
    # print('len(data_list):',len(data_list))
    # excel_operation.write_excel(excel_write_path,filter_rule2(data_list))

    data_dict = excel_operation.read_excel_all(excel_read_path)
    # for k, v in data_dict.items():
    #     print('k:',k)
    #     print('len v:', len(v))
    #     pass
    excel_operation.write_excel_all(excel_write_path, filter_rule4(data_dict))
    pass
