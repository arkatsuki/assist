# -*- coding: utf-8 -*-
from file import excel_filter
from file import excel_operation


def include_keyword():
    excel_read_path = r'D:\test_dir\深圳市公务员考试成绩-2018笔试.xlsx'
    excel_write_path = r'D:\test_dir\深圳成绩2018.xls'

    rule_list = [10, 'i', 'A|B', 3]
    data_dict = excel_operation.read_excel_all(excel_read_path)
    excel_operation.write_excel_all(excel_write_path, excel_filter.filter_rule6(data_dict, rule_list))
    pass

if __name__ == "__main__":
    include_keyword()
    pass
