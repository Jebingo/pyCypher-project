# cli.py

"""Module providing pycypher CLI funcionality"""

import sys
import argparse
import pathlib

from . import __version__
from .pycypher import Cypher


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='cypher', description='Encrypt or decrypt file or all files in specified folder')
    parser.version = f'pycypher v{__version__}'

    parser.add_argument('-v', '--version', action='version')

    parser.add_argument('path', metavar='PATH', nargs='?',
                        default='.', help='specify path to file or folder')

    parser.add_argument('-e', '--encrypt',
                        action='store_true', help='encrypt file or folder')
    parser.add_argument('-d', '--decrypt',
                        action='store_true', help='decrypt file or folder')

    return parser.parse_args()


def main():
    args = parse_arguments()

    cypher = Cypher(args.path)

    if args.encrypt:
        cypher.encrypt()
    elif args.decrypt:
        cypher.decrypt()
    else:
        print('Please specify whether to encrypt or decrypt')
        sys.exit()
