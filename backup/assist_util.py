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
    二分查找，未充分测试
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


def binary_search_asc(new_num, num_list) :
    '''
    初步测试通过，未覆盖所有情况
    二分插入有序列表，升序排列
    :param new_num:
    :param num_list:
    :return:
    '''
    low = 0
    high = len(num_list)
    if high==0:
        num_list.append(new_num)
        return
        pass
    while low <= high :
        mid = (low + high)//2
        print('lhm',low,high,mid)
        # print('num_list:',num_list)
        if num_list[mid] == new_num:
            num_list.insert(mid, new_num)
            print('num_list:', num_list)
            break
        # 左半边
        elif num_list[mid] > new_num :
            high = mid - 1
            if low == high:
                num_list.insert(low + 1, new_num)
                print('num_list:', num_list)
                break
                pass
        #右半边
        else :
            low = mid + 1
            if low == high:
                num_list.insert(low, new_num)
                print('num_list:', num_list)
                break
                pass
            pass

        if high<low:
            num_list.insert(low, new_num)
            print('num_list:',  num_list)
            break
            pass
    return num_list


def binary_search_desc(new_num, num_list) :
    '''
    初步测试通过，未覆盖所有情况
    二分插入有序列表，降序排列
    :param new_num:
    :param num_list:
    :return:
    '''
    low = 0
    high = len(num_list)
    if high==0:
        num_list.append(new_num)
        return
        pass
    while low <= high :
        mid = (low + high)//2
        print('lhm',low,high,mid)
        if num_list[mid] == new_num:
            num_list.insert(mid, new_num)
            break
        # 左半边
        elif num_list[mid] < new_num :
            high = mid - 1
            if low == high:
                if num_list[low]==new_num:
                    num_list.insert(low, new_num)
                elif num_list[low]>new_num:
                    num_list.insert(low+1, new_num)
                else:
                    num_list.insert(low, new_num)
                    pass
                print('L num_list:', num_list)
                break
                pass
        #右半边
        else :
            low = mid + 1
            if low == high:
                if low>=len(num_list):
                    num_list.insert(low-1, new_num)
                    pass
                if num_list[low]==new_num:
                    num_list.insert(low, new_num)
                elif num_list[low]>new_num:
                    num_list.insert(low+1, new_num)
                else:
                    num_list.insert(low, new_num)
                    pass
                print('R num_list:', num_list)
                break
                pass
            pass

        if high<low:
            num_list.insert(low, new_num)
            print('< num_list:',  num_list)
            break
            pass
    return num_list


def binary_insert_list_desc(new_elem, num_list, index):
    '''
    二分插入有序列表，降序排列
    :param new_elem: 待插入的新元素
    :param num_list: 降序排列的数量
    :param index: 用元素的第几个子元素进行大小比较
    :return:
    '''
    data = new_elem[index]
    if not isinstance(data, float):
        try:
            data = float(data)
            pass
        except Exception:
            # print('data:',data)
            return
        pass
    low = 0
    high = len(num_list)
    if high==0:
        num_list.append(new_elem)
        return
        pass
    while low <= high :
        mid = (low + high)//2
        # print('lhm', low, high, mid)
        num_list_val = float(num_list[mid][index])
        if num_list_val == data:
            num_list.insert(mid, new_elem)
            break
        # 左半边
        elif num_list_val < data:
            high = mid - 1
            if low == high:
                num_list_low_val = float(num_list[low][index])
                if num_list_low_val == data:
                    num_list.insert(low, new_elem)
                elif num_list_low_val > data:
                    num_list.insert(low + 1, new_elem)
                else:
                    num_list.insert(low, new_elem)
                    pass
                break
                pass
        #右半边
        else :
            low = mid + 1
            if low == high:
                if low>=len(num_list):
                    num_list.insert(low-1, new_elem)
                    pass
                num_list_low_val_r = float(num_list[low][index])
                if num_list_low_val_r == data:
                    num_list.insert(low, new_elem)
                elif num_list_low_val_r > data:
                    num_list.insert(low + 1, new_elem)
                else:
                    num_list.insert(low, new_elem)
                    pass
                break
                pass
            pass

        if high<low:
            num_list.insert(low, new_elem)
            break
            pass
    return num_list


if __name__ == "__main__":
    # list1 = [1,3,5,7,9,11,13,15,17,19]
    # list2 = binary_search(9, list1)
    # list2 = binary_search(10, list1)
    # list2 = binary_search_desc(11, list1)
    # list1 = [1, 11, 13, 15, 7, 5, 3, 2, 1, 17, 19, 10]

    list1 = [11, 1, 13, 15, 7, 5, 3, 2, 1, 3, 5, 17, 19, 10, 100]
    # list1 = [1, 11, 13, 15, 7, 5, 3, 2, 1, 3, 5, 17, 19, 10]
    list2 = []
    for elem in list1:
        binary_search_desc(elem, list2)
        # binary_search_asc(elem, list2)
        pass

    print('list2:',list2)

    # print(1//2)
    pass