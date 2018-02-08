
class SvnRecord(object):

    def __init__(self, version_num=0, user_name='', submit_time='', action='', file_path='', comment=''):
        self.version_num = version_num
        self.user_name = user_name
        self.submit_time = submit_time
        self.action = action
        self.file_path = file_path
        self.comment = comment
        pass
