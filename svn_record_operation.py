import xlwt
import time
# import svn_record.SvnRecord
from svn_record import SvnRecord

current_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))


class SvnRecordOperation(object):


    def __init__(self):
        # 存放每个路径对应的版本号和动作，key是file_path，value是一个二维list，每个元素版本号和动作的list
        self.v_num_act_dict = {}
        # 存放不同类型的SvnRecord
        self.records_add = []
        self.records_delete = []
        self.records_modify = []
        # 存放所有的记录，key是file_path, value是SvnRecord
        self.record_all = {}

    def add_record(self, file_path, version_num, user_name, action):
        """
        添加一个SvnRecord。保存到record_all。如果已经添加过同样路径的，就只添加版本号和action
        :param file_path: 路径
        :param version_num: 版本号
        :param user_name: 提交者
        :param action: 增删改
        :return:
        """
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
            self.amend_v_num_act(self.v_num_act_dict[file_path])
            # print('te_after2:', self.v_num_act_dict[file_path])
            v_num_act_final = self.convert_ver_num_act(self.v_num_act_dict[file_path][0],
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

    def amend_v_num_act(self, v_num_act_list):
        """
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

    def convert_ver_num_act(self, first, last):
        """
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

    # @staticmethod
    def write_excel(self, excel_path):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('1', cell_overwrite_ok=True)
        # 行号
        i = 0
        for rec in self.records_add:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '新增')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in self.records_modify:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '修改')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in self.records_delete:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, '删除')
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        book.save(excel_path)
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
