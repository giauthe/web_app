try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
import csv
import base64


def read_csv_to_dic(data, base_64=False):
    data = base64.b64decode(data) if base_64 else data
    f = StringIO(data.encode("utf-8"))
    csv_reader = csv.DictReader(f)
    return [row for row in csv_reader]
