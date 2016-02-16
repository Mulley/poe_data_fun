"""Playing around."""
import pprint
from modules.analysis import (
    read_data, stats_of_col, data_per_class)
from modules.settings import CHOICES_LIST


def main():
    """Run this."""
    pp = pprint.PrettyPrinter(indent=4)
    data = read_data('data/poe.csv')
    class_data = data_per_class(data)
    for key, value in class_data.items():
        print('~~~~~~~~', key, '~~~~~~~~')
        for col in CHOICES_LIST:
            print('~~~~', col)
            pp.pprint(stats_of_col(value, col))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


if __name__ == '__main__':
    main()
