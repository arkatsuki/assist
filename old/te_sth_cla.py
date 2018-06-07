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
        SvnRecord.records_add.append(self.file_path)
        print('resolve_raw_path end')
