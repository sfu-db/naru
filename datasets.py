"""Dataset registrations."""
import os

import numpy as np

import common

DATA_PATH = '/var/tmp/cardDB/data'


def LoadDmv(filename='Vehicle__Snowmobile__and_Boat_Registrations.csv'):
    csv_file = './datasets/{}'.format(filename)
    cols = [
        'Record Type', 'Registration Class', 'State', 'County', 'Body Type',
        'Fuel Type', 'Reg Valid Date', 'Color', 'Scofflaw Indicator',
        'Suspension Indicator', 'Revocation Indicator'
    ]
    # Note: other columns are converted to objects/strings automatically.  We
    # don't need to specify a type-cast for those because the desired order
    # there is the same as the default str-ordering (lexicographical).
    type_casts = {'Reg Valid Date': np.datetime64}
    return common.CsvTable('DMV', csv_file, cols, type_casts)

def LoadForest(filename='num.csv'):
    csv_file = os.path.join(DATA_PATH, 'forest', filename)
    cols = ['Elevation', 'Aspect', 'Slope',
            'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
            'Horizontal_Distance_To_Roadways', 'Hillshade_9am',
            'Hillshade_Noon', 'Hillshade_3pm', 'Horizontal_Distance_To_Fire_Points']

    # all data are integers, not need to cast type
    type_casts = {}
    return common.CsvTable('Forest', csv_file, cols, type_casts, pg_name='forest_num')

if __name__ == '__main__':
    table = LoadForest()
    print(table)
