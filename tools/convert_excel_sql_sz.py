# -*- coding: utf-8 -*-
from file import excel_operation


def convert_sz_2018_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2018.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        # print(k)
        # print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            i = 0
            for row in v:
                if i<3:
                    i = i + 1
                    continue
                    pass
                # sql_insert = r'insert into shenzhen2018_position values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, ' \
                #              r'{8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})'
                # f.write(sql_insert.format(row[0]))
                sql_insert = 'insert into shenzhen2018_position values'
                # sql_insert = 'INSERT INTO `gwy`.`shenzhen2017_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                #              '`AGENCY`, `POSITION`, `POSITION_PROPERTY`, `POSITION_DESCRIPTION`, ' \
                #              '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                #              ' `DEGREE`, `MAJOR`, `TWO_YEARS_EXPERIENCE`, `OTHER_REQUIREMENT`, ' \
                #              '`TEST_SUBJECT`, `REMARK`) VALUES'
                row_len = len(row)
                while row_len<17:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                i = i + 1
                pass
            pass
        pass
    pass


def convert_sz_2017_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2017.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        # print(k)
        # print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            i = 0
            for row in v:
                i = i + 1
                # if i < 3:
                #     continue
                #     pass
                sql_insert = 'INSERT INTO `gwy`.`shenzhen2017_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                             '`AGENCY`, `POSITION`, `POSITION_PROPERTY`, `POSITION_DESCRIPTION`, ' \
                             '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                             ' `DEGREE`, `MAJOR`, `TWO_YEARS_EXPERIENCE`, `OTHER_REQUIREMENT`, ' \
                             '`TEST_SUBJECT`, `REMARK`) VALUES '
                row_len = len(row)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[6], str) and (not row[6].isdigit()):
                    continue
                    pass

                while row_len<16:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                pass
            pass
        pass
    pass


def convert_sz_2016_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2016.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        # print(k)
        # print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            i = 0
            for row in v:
                i = i + 1
                # if i < 3:
                #     continue
                #     pass
                sql_insert = 'INSERT INTO `gwy`.`shenzhen2016_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                             '`AGENCY`, `POSITION`, `POSITION_PROPERTY`, `POSITION_DESCRIPTION`, ' \
                             '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                             ' `DEGREE`, `MAJOR`, `TWO_YEARS_EXPERIENCE`, `OTHER_REQUIREMENT`, ' \
                             '`TEST_SUBJECT`, `REMARK`) VALUES'
                row_len = len(row)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[6], str) and (not row[6].isdigit()):
                    continue
                    pass

                while row_len<16:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                pass
            pass
        pass
    pass


def convert_sz_2015_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2015.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        # print(k)
        # print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`shenzhen2015_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                             '`AGENCY`, `POSITION`,  `POSITION_DESCRIPTION`, ' \
                             '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                             ' `DEGREE`, `MAJOR`, `TWO_YEARS_EXPERIENCE`, `OTHER_REQUIREMENT`, ' \
                             '`TEST_SUBJECT`, `REMARK`) VALUES'
                row_len = len(row)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[6], str) and (not row[6].isdigit()):
                    continue
                    pass

                while row_len<16:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                pass
            pass
        pass
    pass


def convert_sz_2014_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2014.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        # print(k)
        # print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`shenzhen2014_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                             '`AGENCY`, `POSITION`,  `POSITION_DESCRIPTION`, ' \
                             '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                             ' `DEGREE`, `MAJOR`, `TWO_YEARS_EXPERIENCE`, `OTHER_REQUIREMENT`, ' \
                             '`TEST_SUBJECT`, `REMARK`) VALUES'
                row_len = len(row)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[6], str) and (not row[6].isdigit()):
                    continue
                    pass

                while row_len<16:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                pass
            pass
        pass
    pass


def convert_sz_2013_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\深圳市公务员职位表2013.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        print(k)
        print(len(v))
        dest_sql_file_path = r'D:\test_dir\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`shenzhen2013_position` (`POSITION_CODE`, `HIGHER_AUTHORITY`, ' \
                             '`AGENCY`, `POSITION`,  `POSITION_DESCRIPTION`, ' \
                             '`RECRUIT_QUOTA`, `INTERVIEW_QUOTA`, `SEX`, `AGE_LIMIT`, `EDUCATIONAL_BACKGROUND`,' \
                             ' `DEGREE`, `MAJOR`,  `OTHER_REQUIREMENT`, ' \
                             '`TEST_SUBJECT`, `REMARK`) VALUES'
                row_len = len(row)
                print('row_len:', row_len)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[6], str) and (not row[6].isdigit()):
                    continue
                    pass

                while row_len<14:
                    row_len = row_len + 1
                    row.append('')
                    pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data) + "'" + ", "
                    pass
                if value_str != value_str_start:
                    value_str = "(" + value_str[:len(value_str)-2] + ");\n"
                    pass
                print('value_str:', value_str)
                f.write(sql_insert + value_str)
                pass
            pass
        pass
    pass


if __name__ == "__main__":
    # convert_sz_2018_position()
    # convert_sz_2017_position()
    # convert_sz_2016_position()
    # convert_sz_2015_position()
    # convert_sz_2014_position()
    convert_sz_2013_position()

    # s = 1.0
    # if isinstance(s,str) and (not s.isdigit()):
    #     print('n')
    #     pass
    pass