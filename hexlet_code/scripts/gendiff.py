#!/usr/bin/env python3

from hexlet_code.generate_diff import generate_diff
from hexlet_code.cli import cli_gendiff


def main():
    args = cli_gendiff()
    print(generate_diff(args.first_file, args.second_file, format_out=args.format))


if __name__ == '__main__':
    main()
