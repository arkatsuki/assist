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
        self.resolve_raw_path()
        pass

    def resolve_raw_path(self):
        """

        :param raw_path:
        :return:
        """
        idx_dev = self.raw_path.find('DEV2')
        self.file_path = self.raw_path[idx_dev:]

        self.action = self.raw_path[0]

        version_action = self.put_list
        if version_action[0] < self.version_num:

            pass


        if self.raw_path[0] == 'A':
            SvnRecord.records_add.append(self)
        elif self.raw_path[0] == 'D':
            SvnRecord.records_delete.append(self)
        elif self.raw_path[0] == 'M':
            SvnRecord.records_modify.append(self)
        pass

    def put_list(self):
        """
        之前svn log返回的结果，版本号是从大到小。可能的情况：
        a .... d
        d.a.d
        :return:
        """
        for existing_rec in SvnRecord.records_add:
            if self.file_path == existing_rec.file_path:
                if self.version_num < existing_rec.version_num:# 肯定是当前版本号小
                    pass

        for existing_rec in SvnRecord.records_delete:
            if self.file_path == existing_rec.file_path:
                if self.version_num < existing_rec.version_num:
                    if self.action == 'A':
                        pass

        for existing_rec in SvnRecord.records_modify:
            if self.file_path == existing_rec.file_path:
                version_action.append(existing_rec.version_num)
                version_action.append(existing_rec.action)
                return version_action

