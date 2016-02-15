"""Playing around."""
import argparse
import pprint
from source.analysis import read_data, stats_of_col, percentile_for_characters


def main(args):
    """Run this."""
    pp = pprint.PrettyPrinter(indent=4)
    data = read_data('data/poe.csv')
    #  pp.pprint(data_for_account(data, 'Helman'))
    #  pp.pprint(stats_of_col(data, args.col))
    pp.pprint(percentile_for_characters(data, 'Mulley5'))


def get_args():
    """Get commandline args."""
    parser = argparse.ArgumentParser(description='Analyze POE data')
    parser.add_argument('col', choices=[
        'rank', 'account', 'character', 'class', 'level', 'exp', 'dead'])

    return parser.parse_args()


if __name__ == '__main__':
    main(get_args())
