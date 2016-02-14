"""Functions for manipulating data."""
import numpy as np


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
