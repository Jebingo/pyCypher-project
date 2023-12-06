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
    path = pathlib.Path(args.path)

    # cypher = Cypher(path)

    if path.is_file():
        if args.encrypt:
            # cypher.encrypt_file()
            print(f'encrypt file {path}')
        elif args.decrypt:
            # cypher.decrypt_file()
            print(f'decrypt file {path}')
        else:
            print('Please specify whether to encrypt or decrypt')
            sys.exit()
    elif path.is_dir():
        if args.encrypt:
            # cypher.encrypt_file()
            print(f'encrypt folder {path}')
        elif args.decrypt:
            # cypher.decrypt_file()
            print(f'decrypt folder {path}')
        else:
            print('Please specify whether to encrypt or decrypt')
            sys.exit()
    else:
        print('Path does not exist')
        sys.exit()
