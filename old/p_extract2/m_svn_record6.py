class SvnRecord(object):
    records_add = []
    records_delete = []
    records_modify = []

    def __init__(self,version_num=0, user_name='', submit_time='', action='', file_path='', comment='',
                 raw_path=''):
        """

        :param version_num:
        :param user_name:
        :param submit_time:
        :param action:
        :param file_path:
        :param comment:
        """
        self.version_num = version_num
        self.user_name = user_name
        self.submit_time = submit_time
        self.action = action
        self.file_path = file_path
        self.comment = comment
        self.raw_path = raw_path
        # self.resolve_raw_path()
        self.version_num_action = {}
        self.version_num_action_li = []
        pass

    def add_ver_num_action(self, ver_num, action):
        self.version_num_action[ver_num] = action
        self.version_num_action_li.append(ver_num + '|' + action)
        pass

    def put_list(self):
        # last_elem = self.version_num_action_li.pop()
        # first_elem = self.version_num_action_li.pop(0)
        last_elem = self.version_num_action_li[0]
        first_elem = self.version_num_action_li[-1]
        # res_li = self.convert_ver_num_act(first_elem,last_elem)
        res_li = SvnRecord.convert_ver_num_act(first_elem, last_elem)
        if len(res_li) == 0:
            pass
        else:
            self.version_num = res_li[0]
            self.action = res_li[1]
            if res_li[1] == 'A':
                SvnRecord.records_add.append(self)
            elif res_li[1] == 'D':
                SvnRecord.records_delete.append(self)
            elif res_li[1] == 'M':
                SvnRecord.records_modify.append(self)
            pass

        pass

    @staticmethod
    def convert_ver_num_act(first_elem,last_elem):
        last_act = last_elem.split('|')[1]
        first_act = first_elem.split('|')[1]
        if first_act == 'A':
            if last_act != 'D':
                return [first_elem.split('|')[0],first_elem.split('|')[1]]
            else:
                return []
        elif first_act == 'D':
            if last_act != 'D':
                return [last_elem.split('|')[0], last_elem.split('|')[1]]
            else:
                return [first_elem.split('|')[0], first_elem.split('|')[1]]
        elif first_act == 'M' and last_act != 'D':
            if last_act != 'D':
                return [first_elem.split('|')[0], first_elem.split('|')[1]]
            else:
                return [last_elem.split('|')[0], last_elem.split('|')[1]]

        else:
            return [first_elem.split('|')[0],first_elem.split('|')[1]]

