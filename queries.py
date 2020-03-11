"""Query Formalization"""
import os
import csv

DATA_PATH = '/var/tmp/cardDB/data'

def ParseInteger(lrange, rrange):
    assert lrange != 'MAX' and rrange != 'MIN'
    if lrange == 'MIN' and rrange == 'MAX':
        return None
    elif lrange == 'MIN':
        return '<=', int(float(rrange))
    elif rrange == 'MAX':
        return '>=', int(float(lrange))
    elif lrange == rrange:
        return '=', int(float(lrange))
    lrange = int(float(lrange))
    rrange = int(float(rrange))
    assert lrange < rrange
    return '[]', (lrange, rrange)

def LoadForestQueries(filename='query'):
    csv_file = os.path.join(DATA_PATH, 'forest', '{}.csv'.format(filename))
    print('load from query file: {}'.format(csv_file))
    num_attr = 10
    queries = []

    with open(csv_file, 'r') as infile:
        reader = csv.reader(infile, delimiter=',', quotechar='|')
        for query in reader:
            #  print(query)
            col_idxs = []
            ops = []
            vals = []
            for i in range(num_attr):
                # all values in forests are integers
                parsed = ParseInteger(query[i*2], query[i*2+1])
                if parsed is None:
                    continue
                else:
                    t_op, t_val = parsed
                    col_idxs.append(i)
                    ops.append(t_op)
                    vals.append(t_val)
            queries.append((col_idxs, ops, vals))

    print('{} queries in total'.format(len(queries)))

    return queries




