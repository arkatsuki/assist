# -*- coding: utf-8 -*-
from file import excel_operation


def convert_gj_2019_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\国家公务员考试职位表2019.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k, v in data_dict.items():
        print(k)
        print(len(v))
        dest_sql_file_path = r'D:\test_dir\temp_generate\\' + k + '.sql'
        with open(dest_sql_file_path, 'w', encoding='utf-8') as f:
            for row in v:
                sql_insert = 'INSERT INTO `gwy`.`guojia2019_position` (`DEPARTMENT_CODE`, `DEPARTMENT_NAME`, ' \
                             '`AGENCY`, `AGENCY_TYPE`, `POSITION`, `POSITION_PROPERTY`, `POSITION_DISTRIBUTION`, ' \
                             '`POSITION_DESCRIPTION`, `POSITION_CODE`, `AGENCY_HIERARCHY`, `TEST_TYPE`, ' \
                             '`RECRUIT_QUOTA`, `MAJOR`, `EDUCATIONAL_BACKGROUND`, `DEGREE`, `POLITICAL_STATUS`, ' \
                             '`WORKING_EXPERIENCE`, `SERVE_WORKING_EXPERIENCE`, `INTERVIEW_MAJOR_TEST`, ' \
                             '`INTERVIEW_RATIO`, `BASE`, `LUOHU_SITE`, `REMARK`, `DEPARTMENT_WEBSITE`, ' \
                             '`CONSULT_LINE1`, `CONSULT_LINE2`, `CONSULT_LINE3`) VALUES '
                row_len = len(row)
                print('row_len:', row_len)
                if row_len < 11:
                    continue
                    pass
                elif isinstance(row[11], str) and (not row[11].isdigit()):
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


def convert_gj_2017_position():
    """
    success
    :return:
    """
    excel_path = r'D:\test_dir\国家公务员考试职位表2017.xls'
    data_dict = excel_operation.read_excel_all(excel_path)
    for k, v in data_dict.items():
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
    for k, v in data_dict.items():
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
    # convert_gj_2016_position()
    # convert_gj_2017_position()
    convert_gj_2019_position()
    pass

# select * from guojia2019_position
# -- select POSITION_DISTRIBUTION from guojia2019_position
# where MAJOR REGEXP '电子信息'
# -- and EDUCATIONAL_BACKGROUND REGEXP '本科'
# and EDUCATIONAL_BACKGROUND REGEXP '本科'
# and POLITICAL_STATUS REGEXP '不限'
# and SERVE_WORKING_EXPERIENCE REGEXP '无限制'
# and POSITION_DISTRIBUTION REGEXP '其他职位'
# -- group by POSITION_DISTRIBUTION

# CREATE TABLE `guojia2019_position` (
#   `ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
#   `DEPARTMENT_CODE` varchar(500) DEFAULT NULL COMMENT '部门代码',
#   `DEPARTMENT_NAME` varchar(500) DEFAULT NULL COMMENT '部门名称',
#   `AGENCY` varchar(500) DEFAULT NULL COMMENT '用人司局',
#   `AGENCY_TYPE` varchar(500) DEFAULT NULL COMMENT '机构性质',
#   `POSITION` varchar(500) DEFAULT NULL COMMENT '招考职位',
#   `POSITION_PROPERTY` varchar(500) DEFAULT NULL COMMENT '职位属性',
#   `POSITION_DISTRIBUTION` varchar(500) DEFAULT NULL COMMENT '职位分布',
#   `POSITION_DESCRIPTION` varchar(500) DEFAULT NULL COMMENT '职位简介',
#   `POSITION_CODE` varchar(500) DEFAULT NULL COMMENT '职位代码',
#   `AGENCY_HIERARCHY` varchar(500) DEFAULT NULL COMMENT '机构层级',
#   `TEST_TYPE` varchar(500) DEFAULT NULL COMMENT '考试类别',
#   `RECRUIT_QUOTA` varchar(500) DEFAULT NULL COMMENT '招考人数',
#   `MAJOR` varchar(500) DEFAULT NULL COMMENT '专业',
#   `EDUCATIONAL_BACKGROUND` varchar(500) DEFAULT NULL COMMENT '学历',
#   `DEGREE` varchar(500) DEFAULT NULL COMMENT '学位',
#   `POLITICAL_STATUS` varchar(500) DEFAULT NULL COMMENT '政治面貌',
#   `WORKING_EXPERIENCE` varchar(500) DEFAULT NULL COMMENT '基层工作最低年限',
#   `SERVE_WORKING_EXPERIENCE` varchar(500) DEFAULT NULL COMMENT '服务基层项目工作经历基层',
#   `INTERVIEW_MAJOR_TEST` varchar(500) DEFAULT NULL COMMENT '是否在面试阶段组织专业能力测试',
#   `INTERVIEW_RATIO` varchar(500) DEFAULT NULL COMMENT '面试人员比例',
#   `BASE` varchar(500) DEFAULT NULL COMMENT '工作地点',
#   `LUOHU_SITE` varchar(500) DEFAULT NULL COMMENT '落户地点',
#   `REMARK` varchar(500) DEFAULT NULL COMMENT '备注',
#   `DEPARTMENT_WEBSITE` varchar(500) DEFAULT NULL COMMENT '部门网站',
#   `CONSULT_LINE1` varchar(500) DEFAULT NULL COMMENT '联系电话1',
#   `CONSULT_LINE2` varchar(500) DEFAULT NULL COMMENT '联系电话2',
#   `CONSULT_LINE3` varchar(500) DEFAULT NULL COMMENT '联系电话3',
#    PRIMARY KEY (`ID`)
# ) ENGINE=InnoDB AUTO_INCREMENT=10205 DEFAULT CHARSET=utf8 COMMENT='国考职位表2019';
