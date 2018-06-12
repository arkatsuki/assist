import xlwt
import time
# import version_control.svn_record.SvnRecord
# 单用import的话在使用时需要带前缀。用from import就不用前缀。
from version_control.svn_record import SvnRecord
from common.algorithms import bubble_sort_asc


"""
success
"""

class SvnRecordOperation(object):
    """
    用法：使用svn log获取提交记录后，每个提交记录用add_record添加，全部添加完成后用put_specific_list分类放到指定的list，
    然后write_excel写到excel文件里。
    """
    def __init__(self):
        # 存放每个路径对应的版本号和动作，key是file_path，value是一个二维list，每个元素是版本号和动作组成的list
        # 这个属性只用于内部的方法。
        self.v_num_act_dict = {}
        # 存放不同类型的SvnRecord
        self.records_add = []
        self.records_delete = []
        self.records_modify = []

        self.record_all = {}  # 存放所有的记录，key是file_path, value是SvnRecord
        self._version_num_list = []  # 保存所有版本号，升序排列。# 这儿要不要下划线都行。

    @property
    def version_num_list(self):
        # 每次获取version_num_list的值的时候，进行升序排序
        # 属性名前面必须有一个下划线，否则会报无限递归错误。其它模块引用时不用带下划线。
        return bubble_sort_asc(self._version_num_list)

    # 不定义的话就没法设置version_num_list的值，及时__init__里面的self.也没法设置。
    @version_num_list.setter
    def version_num_list(self, value):
        # 属性名前面必须有一个下划线，否则会报无限递归错误
        self._version_num_list = value

    def add_record(self, file_path, version_num, user_name, action):
        """
        添加一个SvnRecord。保存到record_all。如果已经添加过同样路径的，就只添加版本号和action
        :param file_path: 路径
        :param version_num: 版本号
        :param user_name: 提交者
        :param action: 增删改
        :return:
        """
        if not version_num in self._version_num_list:
            self._version_num_list.append(version_num)
            # 统一在get的时候进行升序排序
            pass
        if file_path in self.v_num_act_dict.keys():
            # 说明已经添加过，只添加版本号和action
            v_num_act_val = self.v_num_act_dict[file_path]
            v_num_act_val_sub = []
            v_num_act_val_sub.append(version_num)
            v_num_act_val_sub.append(action)
            v_num_act_val.append(v_num_act_val_sub)
            pass
        else:
            # 以前没有添加过
            v_num_act_val = []
            v_num_act_val_sub = []
            v_num_act_val_sub.append(version_num)
            v_num_act_val_sub.append(action)
            v_num_act_val.append(v_num_act_val_sub)
            self.v_num_act_dict[file_path] = v_num_act_val
            record = SvnRecord(file_path=file_path, version_num=version_num, user_name=user_name, action=action)
            # self.record_all.append(record)
            self.record_all[file_path] = record
            pass
        pass

    def put_specific_list(self):
        """
        把record_all里面的所有SvnRecord分类放到不同list里面
        :return:
        """
        # 先清空
        self.records_add.clear()
        self.records_delete.clear()
        self.records_modify.clear()
        for file_path, record in self.record_all.items():
            # 调整版本号和action
            # print('before:', self.v_num_act_dict[file_path])
            SvnRecordOperation.amend_v_num_act(self.v_num_act_dict[file_path])
            # print('te_after2:', self.v_num_act_dict[file_path])
            v_num_act_final = SvnRecordOperation.convert_ver_num_act(self.v_num_act_dict[file_path][0],
                                                       self.v_num_act_dict[file_path][-1])
            # 如果返回的是空，说明这个文件最后一次操作是删除，不需要写进清单
            if len(v_num_act_final) < 1:
                continue
                pass
            record.version_num = v_num_act_final[0]
            record.action = v_num_act_final[1]

            if record.action == 'A':
                self.records_add.append(record)
            elif record.action == 'D':
                self.records_delete.append(record)
            elif record.action == 'M':
                self.records_modify.append(record)
            pass
        pass

    @staticmethod
    def amend_v_num_act(v_num_act_list):
        """
        不需要用self的东西，所以是static。单下划线开头的子类可以访问，双下划线开头的只有自己能访问。
        冒泡排序，按版本号升序排列
        :param v_num_act_list:
        :return:
        """
        for i in range(0, len(v_num_act_list)-1):
            for j in range(0, len(v_num_act_list)-1-i):
                if v_num_act_list[j][0]>v_num_act_list[j+1][0]:
                    temp = v_num_act_list[j]
                    v_num_act_list[j] = v_num_act_list[j+1]
                    v_num_act_list[j+1] = temp
                    pass
                pass
            pass
        pass

    @staticmethod
    def convert_ver_num_act(first, last):
        """
        不需要用self的东西，所以是static。单下划线开头的子类可以访问，双下划线开头的只有自己能访问。
        对于提交多次的，需要调整版本号和action（增删改）
        :param first:第一次提交
        :param last:最后一次提交
        :return:最终结果
        """
        last_act = last[1]
        first_act = first[1]
        if first_act == 'A':
            if last_act != 'D':
                # 版本号始终是最后一次提交的那个版本号
                return [last[0], first[1]]
            else:
                print('first:',first,'last:',last)
                return []
        elif first_act == 'D':
            if last_act != 'D':
                return [last[0], last[1]]
            else:
                return [last[0], last[1]]
        elif first_act == 'M':
            if last_act != 'D':
                return [last[0], last[1]]
            else:
                print('first:', first, 'last:', last)
                return []

        else:
            print('first:', first, 'last:', last)
            return []

    def write_excel(self, excel_path):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('1', cell_overwrite_ok=True)
        current_day = time.strftime('%Y/%m/%d', time.localtime(time.time()))
        # 行号
        i = 0
        for rec in self.records_add:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '新增')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_day)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in self.records_modify:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '修改')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_day)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in self.records_delete:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '删除')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_day)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        book.save(excel_path)
        pass
    pass
pass


def te_bubble_sort():
    """
    测试冒泡排序
    :return:
    """
    te_li = [4, 2, 6, 3, 7, 1, 9, 2]
    for i in range(0, len(te_li) - 1):
        for j in range(0, len(te_li) - 1 - i):
            if te_li[j] > te_li[j + 1]:
                temp = te_li[j]
                te_li[j] = te_li[j + 1]
                te_li[j + 1] = temp
                pass
            pass
        pass
    print(te_li)
    pass

if __name__ == "__main__":
    te_bubble_sort()
    pass
