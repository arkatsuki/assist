import xlrd
import xlwt

# excelFile = 'D:/testRd.xls'
excelFile = 'D:/svn info.xls'


def read_excel_all(excel_file):
    """
    读取excel，返回一个dict，key是sheet的name，value是表示行列的二维数组
    :param excel_file:
    :return:
    """
    rs_dict = {}
    data = xlrd.open_workbook(excel_file)
    # print('sheet_names:', data.sheet_names())
    # print('sheet len:',len(data.sheets()))
    for sheet_name in data.sheet_names():
        sheet_data = data.sheet_by_name(sheet_name)
        sheet_list = []
        rs_dict[sheet_name] = sheet_list
        nrows = sheet_data.nrows  # 行数
        ncols = sheet_data.ncols  # 列数
        for i in range(0, nrows):
            row_values = sheet_data.row_values(i)  # 某一行数据
            row_list = []
            for j in range(0, len(row_values)):
                row_list.append(row_values[j])
                pass
            sheet_list.append(row_list)
            pass
        pass
    return rs_dict


def write_excel_all(excel_path, data_dict):
    """
    写excel
    :param excel_path: excel路径
    :param data_dict: dict, key是sheet的name, value是一个二维数组，存放行列数据
    :return:
    """
    book = xlwt.Workbook()
    for sheet_name, sheet_data in data_dict.items():
        sheet1 = book.add_sheet(sheet_name, cell_overwrite_ok=True)
        for i in range(0, len(sheet_data)):
            for j in range(0, len(sheet_data[i])):
                # print('sheet_data[i][j]:', sheet_data[i][j])
                sheet1.write(i, j, sheet_data[i][j])
                pass
            pass
        pass

    book.save(excel_path)
    pass


if __name__ == "__main__":
    pass
