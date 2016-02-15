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


def stats_of_col(data, column):
    """
    Return dict of stats for a column.

    data: numpy array.
    column: string. Valid options from argparse.
    """
    if column in ('rank', 'level', 'exp'):
        mode = stats.mode(data[column])
        return {
            'mean': int(np.average(data[column])),
            'median': int(np.median(data[column])),
            'mode': {'value': mode[0][0], 'count': mode[1][0]},
            'max': int(np.amax(data[column])),
            'min': int(np.amin(data[column]))
        }

    elif column in ('account', 'class', 'dead'):
        mode = stats.mode(data[column])
        return {
            'mode': {'value': mode[0][0], 'count': mode[1][0]},
        }
    else:
        return "You don't really care about that"


def data_for_account(data, account_name):
    """Return this account's data. Can contain multiple characters."""
    return [datum for datum in data
            if datum['account'].decode('utf-8') == account_name]


def data_for_character(data, character_name):
    """Return this character's data."""
    return [datum for datum in data
            if datum['character'].decode('utf-8') == character_name]


def percentile_for_characters(data, name):
    """Return a list of percentiles for a character or characters."""
    percentile_stats = []
    # Detect if account name or character name
    user_data = data_for_account(
        data, name) if data_for_account(
            data, name) else data_for_character(data, name)
    if not user_data:
        return {'error': True, 'message': 'Character or Account not found.'}
    # Crunch Numbers
    for datum in user_data:
        percentile_stats.append(
            {'character name': datum['character'].decode('utf-8'),
             'rank': datum['rank'],
             'percentile': 100 - stats.percentileofscore(
                data['rank'], datum['rank'])})
    return percentile_stats


def data_per_class(data):
    """Separate the data per class."""
    classes_dict = {'Witch': [], 'Shadow': [], 'Ranger': [], 'Duelist': [],
                    'Marauder': [], 'Templar': [], 'Scion': []}
    for datum in data:
        classes_dict[datum['class'].decode('utf-8')].append(datum)

    for key, value in classes_dict.items():
        classes_dict[key] = np.asarray(value)

    return classes_dict
