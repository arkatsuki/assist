
import excel_operation
import re


def bubble_sort(self, unsorted_list):
    """
    冒泡排序，升序排列
    :param unsorted_list:
    :return:
    """
    for i in range(0, len(unsorted_list) - 1):
        for j in range(0, len(unsorted_list) - 1 - i):
            if unsorted_list[j][0] > unsorted_list[j + 1][0]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp
                pass
            pass
        pass
    pass
