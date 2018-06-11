
import os
import configparser
from version_control.svn_record_operationV4T import SvnRecordOperation

'''
success
'''

# 从配置文件取数据
config = configparser.ConfigParser()
config.read('/config-uncommit.ini')
# svn_addr = config.get('svn','svn_addr')
# user_name = config.get('svn','user_name')
# version_num = config.get('svn','version_num')
# record_limit = config.get('svn','record_limit')
branch_name = config.get('svn','branch_name') # 哪个分支



def get_orig_svn_info():
    # svn_log_command = 'svn log --limit {0} --search {1} --search-and {2} -v {3}'
    # svn log -r {2017-12-29}:{2018-01-10} -v http://192.168.200.233:8888/svn/CN/Develop/projects/branches/DEV/cnweb_sc
    # svn log -r {2018-02-10}:{2017-12-29} --search 1647 --search-and duanyaochang -v http://192.168.200.233:8888/svn/CN/Develop/projects/branches/DEV/cnweb_sc
    svn_log_command = 'svn log --limit {0} --search {1} -v {2}'
    # svn_command_format = svn_log_command.format(
    #     record_limit,  user_name, svn_addr)

    # svn_command_format = 'svn log -r {2019-02-10}:{2017-12-29} --search 1804 --search-and duanyaochang ' \
    #                      '-v http://192.168.200.233:8888/svn/CN/Develop/projects/branches/DEV/cnweb_sc'
    svn_command_format = 'svn log -r {2019-02-10}:{2018-01-23} --search 2038 ' \
                         '-v http://192.168.200.233:8888/svn/CN/Develop/projects/branches/DEV/cnweb_sc'

    print('svn_command_format:', svn_command_format)
    svninfo = os.popen(svn_command_format).readlines()
    """
    结果是一个list，需要一行行处理。
    -----------  的下一行含有  版本号|提交人 。
    Changed paths:  的下一行是文件路径和动作，再下一行是空格表明结束。

    """
    return svninfo


def get_svn_rec_oper(svninfo):
    rec_oper = SvnRecordOperation()
    current_base_info = ['', '']  # 存放版本号、提交人信息，先存俩空字符串站位，避免第一次赋值报异常
    version_num_list = [] # 存放提交的所有版本号
    j = 0
    while j < len(svninfo) - 1:  # 最后一行--------没有价值，反而会让下面的if越界
        print('line info:', svninfo[j])
        if svninfo[j].startswith('----'):  # 一次提交记录的第一行
            j = j + 1  # 下一行，提取版本号、提交人信息
            # print('line info:',svninfo[j])
            # result: r39273 | name | 2017-08-11 10:23:03 +0800 (周五, 11 八月 2017) | 1 line

            svn_info_item = svninfo[j].split('|')
            current_base_info[0] = svn_info_item[0].strip()[1:]
            current_base_info[1] = svn_info_item[1].strip()

            # 存放所有版本号，不重复
            if not current_base_info[0] in version_num_list:
                version_num_list.append(current_base_info[0])

        # 英文版和中文版有区别startswith不一样
        elif svninfo[j].startswith('改变的路径'):
            j = j + 1  # 下一行
            # print('line info:', svninfo[j])
            while svninfo[j].strip() != '':
                original_file_path = svninfo[j].strip()
                idx_dev = original_file_path.find(branch_name)
                file_path = original_file_path[idx_dev:]
                if file_path.split('/')[-1].find('.') == -1:
                    # 是目录
                    print('find directory:', file_path)
                    j = j + 1
                    continue
                rec_oper.add_record(file_path=file_path, version_num=current_base_info[0],
                                    user_name=current_base_info[1], action=original_file_path[0])
                j = j + 1
        else:
            j = j + 1
            pass
        pass
    version_num_list.reverse()
    print('version_num_list:', ','.join(version_num_list))
    rec_oper.put_specific_list()
    return rec_oper


if __name__ == "__main__":
    svninfo = get_orig_svn_info()
    record_oper = get_svn_rec_oper(svninfo)
    excel_path = r'D:\svn info2.xls'
    record_oper.write_excel(excel_path)
    print('version_num_list record_oper:', ','.join(record_oper.version_num_list))
    pass
