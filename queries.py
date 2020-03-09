"""Query Formalization"""
import os
import csv
import numpy as np

QUERY_PATH = '/var/tmp/cardDB/query'

def ParseInteger(lrange, rrange):
    assert lrange != 'MAX' and rrange != 'MIN'

    if lrange == 'MIN' and rrange == 'MAX':
        return None
    elif lrange == 'MIN':
        return ['<='], [int(float(rrange))]
    elif rrange == 'MAX':
        return ['>='], [int(float(lrange))]
    elif lrange == rrange:
        return ['='], [int(float(lrange))]
    else:
        return ['>=', '<='], [int(float(lrange)), int(float(rrange))]

def LoadForestQueries(filename='forest.csv'):
    csv_file = os.path.join(QUERY_PATH, filename)
    num_attr = 10
    queries = []

    with open(csv_file, 'r') as infile:
        reader = csv.reader(infile, delimiter=',', quotechar='|')
        for query in reader:
            print(query)
            col_idxs = []
            ops = []
            vals = []
            for i in range(num_attr):
                # all values in forests are integers
                parsed = ParseInteger(query[i*2], query[i*2+1])
                if parsed is None:
                    continue
                else:
                    t_ops, t_vals = parsed
                    assert len(t_ops) == len(t_vals)
                    col_idxs += [i] * len(t_ops)
                    ops += t_ops
                    vals += t_vals
            queries.append((col_idxs, ops, vals))

    return queries




