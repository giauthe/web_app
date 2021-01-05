import re
from datetime import datetime


def find_latest_file(files, file_pattern, date_pattern):
    result_file = None
    result_date = None
    max_time = None
    for f in files:
        matcher = re.search(file_pattern, f)
        if matcher:
            date = matcher.group(1)
            time = datetime.strptime(date, date_pattern)
            if max_time is None or max_time < time:
                result_file = f
                result_date = date
                max_time = time

    return {'file': result_file, 'date': result_date}


def count_file(files, file_pattern):
    count = 0
    for f in files:
        matcher = re.search(file_pattern, f)
        if matcher:
            count += 1

    return count
