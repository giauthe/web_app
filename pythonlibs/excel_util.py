from decimal import Decimal
import xlrd
import base64


def read_excel_to_dic(data, base_64=False, include_empty=False):
    xlsx = xlrd.open_workbook(file_contents=base64.b64decode(data) if base_64 else data)
    sheet = xlsx.sheet_by_index(0)
    num_rows = sheet.nrows
    num_cells = sheet.ncols
    keys = []
    rows = []
    for col_index in range(0, num_cells):
        key = sheet.cell_value(0, col_index)
        keys.append(key)
    for row_index in range(1, num_rows):
        row = {}
        for col_index in range(0, num_cells):
            cell_type = sheet.cell_type(row_index, col_index)
            cell_value = sheet.cell_value(row_index, col_index)
            if include_empty | cell_type != 0:  # 0=Empty
                if cell_type == 2:  # 2=Number
                    value = Decimal(cell_value)
                    row[keys[col_index]] = value.quantize(Decimal(1)) if value == value.to_integral() else value.normalize()
                else:
                    row[keys[col_index]] = cell_value
        rows.append(row)
    return rows
