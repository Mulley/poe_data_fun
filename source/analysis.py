"""Functions for manipulating data."""
import numpy as np
from scipy import stats


def read_data(data_path):
    """Return csv data as numpy array."""
    return np.loadtxt(open(data_path, 'rb'),
                      dtype={
                          'names': (
                              'rank',
                              'account',
                              'character',
                              'class',
                              'level',
                              'exp',
                              'dead'
                          ),
                          'formats': (
                              'i4',
                              'S30',
                              'S30',
                              'S10',
                              'i4',
                              'i4',
                              'S4'
                          )
                      },
                      delimiter=',',
                      skiprows=1,
                      usecols=(1, 2, 3, 4, 5, 6, 7))


def stats_of_col(data):
    """
    Return dict of stats for a column.

    data: numpy array. Specify key when passing. EG: data['rank']
    """
    mode = stats.mode(data)
    return {
        'mean': int(np.average(data)),
        'median': int(np.median(data)),
        'mode': {'value': mode[0][0], 'count': mode[1][0]},
        'max': int(np.amax(data)),
        'min': int(np.amin(data))
    }
