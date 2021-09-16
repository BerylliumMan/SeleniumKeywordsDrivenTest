# -*- coding: utf-8 -*-
"""
读取用例
"""
# -*- coding: utf-8 -*-
import warnings
import xlrd

def merge_cell(sheet):
    rt = {}
    if sheet.merged_cells:
        # exists merged cell
        for item in sheet.merged_cells:
            for row in range(item[0], item[1]):
                for col in range(item[2], item[3]):
                    rt.update({(row, col): (item[0], item[2])})
    return rt

def get_mergge(filename):
    book = xlrd.open_workbook(filename)
    sheets = book.sheets()
    for index in range(len(sheets)):
        sheet = book.sheet_by_index(index)
        # 获取合并的单元格
        merged = merge_cell(sheet)
        # 获取sheet的行数（默认每一行就是一条用例）
        rows = sheet.nrows
        # 如果sheet为空，那么rows是0
        if rows:
            for row in range(rows):
                data = sheet.row_values(row)  # 单行数据
                for index, content in enumerate(data):
                    if merged.get((row, index)):
                        # 这是合并后的单元格，需要重新取一次数据
                        data[index] = sheet.cell_value(*merged.get((row, index)))
                        print(data)

def get_Cases(filename):
    warnings.filterwarnings("ignore", category=PendingDeprecationWarning)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    cases = []
    case = []
    count = 0
    module = ''
    for i in range(1, nrows):
        for j in range(ncols):
            count += 1
            value = str(table.cell_value(i, j)).strip(' ')
            if count == 2:
                if value != '':
                    module = value
                else:
                    value = module
            case.append(value)
            if count == 6:
                count = 0
                cases.append(case)
                case = []
    return cases

if __name__ == '__main__':
    get_Cases('./testCases_IPSec.xlsx')


