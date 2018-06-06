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

        pass

    def resolve_raw_path(self, raw_path):
        """

        :param raw_path:
        :return:
        """
        idx_dev = raw_path.find('DEV2')
        self.file_path = raw_path[idx_dev:]

        self.action = raw_path[0]

        version_action = self.check_same_file_path
        if version_action[0] < self.version_num:

            pass


        if raw_path[0] == 'A':
            SvnRecord.records_add.append(self)
        elif raw_path[0] == 'D':
            SvnRecord.records_delete.append(self)
        elif raw_path[0] == 'M':
            SvnRecord.records_modify.append(self)
        pass

    def check_same_file_path(self):
        """
        依次循环三个数组，碰到路径相同的就返回。每个路径只出现一次，所以不必全部循环完。
        :return:
        """
        version_action = []
        for existing_rec in SvnRecord.records_add:
            if self.file_path == existing_rec.file_path:
                version_action.append(existing_rec.version_num)
                version_action.append(existing_rec.action)
                return version_action

        for existing_rec in SvnRecord.records_delete:
            if self.file_path == existing_rec.file_path:
                version_action.append(existing_rec.version_num)
                version_action.append(existing_rec.action)
                return version_action


        for existing_rec in SvnRecord.records_modify:
            if self.file_path == existing_rec.file_path:
                version_action.append(existing_rec.version_num)
                version_action.append(existing_rec.action)
                return version_action


