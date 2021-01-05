import csv, codecs, cStringIO

def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
    # Redirect output to a queue
    self.queue = cStringIO.StringIO()
    self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
    self.stream = f
    self.encoder = codecs.getincrementalencoder(encoding)()
    
def write_row(self, row):
    self.writer.writerow([s.encode("utf-8") for s in row])
    # Fetch UTF-8 output from the queue ...
    data = self.queue.getvalue()
    data = data.decode("utf-8")
    # ... and reencode it into the target encoding
    data = self.encoder.encode(data)
    # write to the target stream
    self.stream.write(data)
    # empty queue
    self.queue.truncate(0)


def write_rows(csvfile, order_id , ext_id, amount, payment_type):

    f = open(csvfile, 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(('Equator Order ID', 'External Transaction ID','Amount','Payment Type'))
        writer.writerows([[order_id, ext_id, amount, payment_type]])
    finally:
        f.close()

def write_row_double(csvfile, order_id , ext_id, amount, payment_type):

    f = open(csvfile, 'at')
    try:
        writer = csv.writer(f)
        writer.writerows([[order_id, ext_id, amount, payment_type]])
    finally:
        f.close()

