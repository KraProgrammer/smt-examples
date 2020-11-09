import argparse
from enum import Enum

from examples.cst import CSTExample


class Example(Enum):
    CST = 'cst'
    ALL = 'all'


def main():
    """Entry method."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', '-e',
                        type=Example,
                        choices=Example,
                        help='The example',
                        default=Example.ALL)
    args = parser.parse_args()

    print("Welcome to my SMT examples")
    if args.example == Example.ALL \
            or args.example == Example.CST:
        CSTExample.execute()


if __name__ == '__main__':
    main()
