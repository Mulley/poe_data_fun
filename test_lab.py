"""Playing around."""
from source.analysis import read_data


def main():
    """Run this."""
    result = read_data('data/poe.csv')
    print(result)

if __name__ == '__main__':
    main()
