from estimators import QueryToPredicate
import datasets
import queries
import argparse
import csv
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, default='query-tiny', help='Query file.')
args = parser.parse_args()

if __name__ == '__main__':
    table = datasets.LoadForest()
    queries = queries.LoadForestQueries(args.query)

    with open('{}.sql'.format(args.query), 'w') as fout:
        for query in queries:
            cols, ops, vals = query
            sql = 'select * from {} {};\n'.format(table.pg_name, QueryToPredicate(np.take(table.columns, cols), ops, vals))
            #  print(sql)
            fout.write(sql)
