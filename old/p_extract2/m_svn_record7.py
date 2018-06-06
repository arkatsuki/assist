import xlwt
import time

current_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))


class SvnRecord(object):
    records_add = []
    records_delete = []
    records_modify = []

    def __init__(self,version_num=0, user_name='', submit_time='', action='', file_path='', comment=''):
        self.version_num = version_num
        self.user_name = user_name
        self.submit_time = submit_time
        self.action = action
        self.file_path = file_path
        self.comment = comment
        self.version_num_action = {}
        self.version_num_action_li = []

    def add_ver_num_action(self, ver_num, action):
        self.version_num_action[ver_num] = action
        self.version_num_action_li.append(ver_num + '|' + action)

    def put_list(self):
        # last_elem = self.version_num_action_li.pop()
        # first_elem = self.version_num_action_li.pop(0)
        last_elem = self.version_num_action_li[0]
        first_elem = self.version_num_action_li[-1]
        if len(self.version_num_action_li) == 1:
            print('only submit one time:',self.file_path)
            pass
        print('first_elem:',first_elem.split('|')[0],', last_elem:',last_elem.split('|')[0])
        print('first_elem action:', first_elem.split('|')[1], ', last_elem:', last_elem.split('|')[1])
        print('file path:',self.file_path)
        res_li = SvnRecord.convert_ver_num_act(first_elem, last_elem)

        if len(res_li) == 0:
            print('res_li len == 0:')
            pass
        else:
            print('res_li:', res_li[0], ', ', res_li[1])
            self.version_num = res_li[0]
            self.action = res_li[1]
            if res_li[1] == 'A':
                self.action = '新增'
                SvnRecord.records_add.append(self)
            elif res_li[1] == 'D':
                self.action = '删除'
                SvnRecord.records_delete.append(self)
            elif res_li[1] == 'M':
                self.action = '修改'
                SvnRecord.records_modify.append(self)

    @staticmethod
    def convert_ver_num_act(first_elem,last_elem):
        last_act = last_elem.split('|')[1]
        first_act = first_elem.split('|')[1]
        if first_act == 'A':
            if last_act != 'D':
                # 版本号始终是最后一次提交的那个版本号
                return [last_elem.split('|')[0],first_elem.split('|')[1]]
            else:
                return []
        elif first_act == 'D':
            if last_act != 'D':
                return [last_elem.split('|')[0], last_elem.split('|')[1]]
            else:
                return [last_elem.split('|')[0], last_elem.split('|')[1]]
        elif first_act == 'M':
            if last_act != 'D':
                return [last_elem.split('|')[0], last_elem.split('|')[1]]
            else:
                return []

        else:
            return []

    @staticmethod
    def write_excel(excel_path):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('cnweb_ss', cell_overwrite_ok=True)
        # 行号
        i = 0
        for rec in SvnRecord.records_add:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, rec.action)
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in SvnRecord.records_modify:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, rec.action)
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        for rec in SvnRecord.records_delete:
            sheet1.write(i, 0, rec.file_path)
            sheet1.write(i, 1, rec.action)
            sheet1.write(i, 2, rec.version_num)
            sheet1.write(i, 3, current_date)
            sheet1.write(i, 4, '')
            sheet1.write(i, 5, rec.user_name)
            i = i+1
        book.save(excel_path)