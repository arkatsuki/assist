# -*- coding: utf-8 -*-
from file import excel_operation


def convert_gj_2017_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\国家公务员考试职位表2017.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        print(k)
        print(len(v))
        dest_sql_file_path = r'D:\test_dir\temp_generate\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`guojia2017_position` (`DEPARTMENT_CODE`, `DEPARTMENT_NAME`,' \
                             ' `AGENCY`, `AGENCY_TYPE`, `AGENCY_HIERARCHY`, `POSITION_PROPERTY`, `POSITION`, ' \
                             '`POSITION_DESCRIPTION`, `POSITION_CODE`, `TEST_TYPE`, `RECRUIT_QUOTA`, `MAJOR`, ' \
                             '`EDUCATIONAL_BACKGROUND`, `DEGREE`, `POLITICAL_STATUS`, `WORKING_EXPERIENCE`, ' \
                             '`SZYF_STUDENT`, `WEST_VOLUNTEER`, `STUDENT_VILLAGE_OFFICIAL`, `SPECIFIC_TEACHER`,' \
                             ' `UNLIMITED`, `INTERVIEW_MAJOR_TEST`, `INTERVIEW_RATIO`, `REMARK`, ' \
                             '`POSITION_DISTRIBUTION`, `DEPARTMENT_WEBSITE`, `CONSULT_LINE1`,' \
                             ' `CONSULT_LINE2`, `CONSULT_LINE3`) VALUES '
                row_len = len(row)
                print('row_len:', row_len)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[10], str) and (not row[10].isdigit()):
                    continue
                    pass

                # while row_len<14:
                #     row_len = row_len + 1
                #     row.append('')
                #     pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data).replace('\n', '').replace('\r', '').replace("'", "") + "'" + ", "
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


def convert_gj_2016_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\国家公务员考试职位表2016.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k,v in data_dict.items():
        print(k)
        print(len(v))
        dest_sql_file_path = r'D:\test_dir\temp_generate\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`guojia2016_position` (`DEPARTMENT_CODE`, `DEPARTMENT_NAME`,' \
                             ' `AGENCY`, `AGENCY_TYPE`, `AGENCY_HIERARCHY`, `POSITION_PROPERTY`, `POSITION`, ' \
                             '`POSITION_DESCRIPTION`, `POSITION_CODE`, `TEST_TYPE`, `RECRUIT_QUOTA`, `MAJOR`, ' \
                             '`EDUCATIONAL_BACKGROUND`, `DEGREE`, `POLITICAL_STATUS`, `WORKING_EXPERIENCE`, ' \
                             '`SZYF_STUDENT`, `WEST_VOLUNTEER`, `STUDENT_VILLAGE_OFFICIAL`, `SPECIFIC_TEACHER`,' \
                             ' `UNLIMITED`, `INTERVIEW_MAJOR_TEST`, `INTERVIEW_RATIO`, `REMARK`, ' \
                             '`POSITION_DISTRIBUTION`, `DEPARTMENT_WEBSITE`, `CONSULT_LINE1`,' \
                             ' `CONSULT_LINE2`, `CONSULT_LINE3`) VALUES '
                row_len = len(row)
                print('row_len:', row_len)
                if row_len < 10:
                    continue
                    pass
                elif isinstance(row[10], str) and (not row[10].isdigit()):
                    continue
                    pass

                # while row_len<14:
                #     row_len = row_len + 1
                #     row.append('')
                #     pass
                # value_str = str(i) + ', '
                value_str = ''
                value_str_start = value_str
                for cell_data in row:
                    value_str = value_str + "'" + str(cell_data).replace('\n', '').replace('\r', '').replace("'", "") + "'" + ", "
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
    # convert_gj_2017_position()
    convert_gj_2016_position()
    pass