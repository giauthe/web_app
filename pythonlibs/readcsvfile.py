import csv
def read_csv_file(filename):
    file = open(filename, 'r')
    try:
        csvfile = csv.reader(file)
    finally:
        file.close
    return [row for row in csvfile]


def get_unique_column_values_of_csv(filename,columnIndex):
    file = open(filename, 'r')
    col_index = int(columnIndex)
    try:
        data = csv.reader(file, delimiter=',', skipinitialspace=True)
        list= []
        for row in data:
            if row[col_index] not in list:
                list.append(row[col_index])
    finally:
        file.close
    return list
