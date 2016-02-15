"""Playing around."""
import argparse
import pprint
from source.analysis import (read_data, stats_of_col,
                             percentile_for_characters, data_per_class)
from source.settings import CHOICES_LIST


def main(args):
    """Run this."""
    pp = pprint.PrettyPrinter(indent=4)
    data = read_data('data/poe.csv')
    #  pp.pprint(data_for_account(data, 'Helman'))
    #  pp.pprint(stats_of_col(data, args.col))
    #  pp.pprint(percentile_for_characters(data, 'Mulley5'))
    class_data = data_per_class(data)
    for key, value in class_data.items():
        print('~~~~~~~~', key, '~~~~~~~~')
        for col in CHOICES_LIST:
            print('~~~~', col)
            pp.pprint(stats_of_col(value, col))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def get_args():
    """Get commandline args."""
    parser = argparse.ArgumentParser(description='Analyze POE data')
    parser.add_argument('col', choices=CHOICES_LIST)

    return parser.parse_args()


if __name__ == '__main__':
    main(get_args())
