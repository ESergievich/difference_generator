import argparse


def cli_gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', choices=['stylish', 'plain'],
        help='set format of output'
    )

    args = parser.parse_args()
    return args
