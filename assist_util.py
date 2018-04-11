
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


def binary_search(find, list1) :
    '''
    二分查找
    :param find:
    :param list1:
    :return:
    '''
    low = 0
    high = len(list1)
    while low <= high :
        mid = (low + high) / 2
        if list1[mid] == find :
            return mid
        #左半边
        elif list1[mid] > find :
            high = mid -1
        #右半边
        else :
            low = mid + 1
    #未找到返回-1
    return -1


def binary_search(new_num, num_list) :
    '''
    self 二分插入排序
    :param new_num:
    :param num_list:
    :return:
    '''
    low = 0
    high = len(num_list)
    while low <= high :
        mid = (low + high)//2
        if num_list[mid] == new_num:
            num_list.insert(mid, new_num)
            break
        # 左半边
        elif num_list[mid] > new_num :
            high = mid -1
        #右半边
        else :
            low = mid + 1
            pass
        if high<=low:
            num_list.insert(low, new_num)
            break
            pass
    return num_list


if __name__ == "__main__":
    list1 = [1,3,5,7,9,11,13,15,17,19]
    # list2 = binary_search(9, list1)
    # list2 = binary_search(10, list1)
    list2 = binary_search(11, list1)
    print('list2:',list2)
    pass