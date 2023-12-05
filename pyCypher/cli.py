# cli.py

"""Module providing pyCypher CLI funcionality"""

import sys
import argparse
import pathlib

from . import __version__
from .pyCypher import Cypher


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='cypher', description='Encrypt/Decrypt file')
    parser.version = f'pyCypher v{__version__}'

    parser.add_argument('-v', '--version', action='version')

    parser.add_argument('file_path', metavar='FILE_PATH', nargs='?',
                        default='.', help='Encrypt/Decrypt specified file')

    parser.add_argument('-e', '--encrypt',
                        action='store_true', help='Encrypt the file')
    parser.add_argument('-d', '--decrypt',
                        action='store_true', help='Decrypt the file')

    return parser.parse_args()


def main():
    args = parse_arguments()
    file_path = pathlib.Path(args.file_path)

    if not file_path.is_file():
        print('The specified file does not exist')
        sys.exit()

    cypher = Cypher(file_path)

    if args.encrypt:
        cypher.encrypt_file()
    elif args.decrypt:
        cypher.decrypt_file()
    else:
        print('Please specify either -e or -d option')
        sys.exit()
