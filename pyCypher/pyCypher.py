# pycypher.py

"""Module providing pyCypher main funcionality"""

import os
import pathlib
from cryptography.fernet import Fernet


N_BYTES = 100
TOKEN_LENGTH = 128
KEY_LENGTH = 44
FLAG = b'Encrypted'
EXT_LENGTH = 10
EXT_NEW = '.cyp'


class Cypher:
    def __init__(self, path: str) -> None:
        self._path = pathlib.Path(path)

    def encrypt(self) -> int:
        if self._path.is_file():
            print(f'encrypt file {self._path}')
            # return self.encrypt_file(self._path)
        elif self._path.is_dir():
            print(f'encrypt folder {self._path}')
            return self.encrypt_folder()
        else:
            return -1

    def decrypt(self) -> int:
        if self._path.is_file():
            print(f'decrypt file {self._path}')
            # return self.decrypt_file(self._path)
        elif self._path.is_dir():
            print(f'decrypt folder {self._path}')
            # return self.decrypt_folder(self._path)
        else:
            return -1

    def encrypt_folder(self) -> int:
        for file in list(self._path.glob('*')):
            if file.is_file():
                self.encrypt_file(file)
        return 0

    def decrypt_folder(self) -> int:
        print(self._files)
        return 0

    def encrypt_file(self, file_path) -> int:
        file_path = pathlib.Path(file_path)
        print(file_path)
        self._file_name = file_path.stem
        self._file_ext = file_path.suffix
        # load first n bytes of file and flag
        with open(file_path, 'rb') as file:
            raw_bytes = file.read(N_BYTES)
            file.seek(-len(FLAG), 2)
            flag = file.read(len(FLAG))

        # if flag match return
        if flag == FLAG:
            return -1

        # generate key
        key = Fernet.generate_key()
        cypher_suite = Fernet(key)

        # get the file extension and ensure that its 10 bytes long
        extension = bytes(self._file_ext, 'utf-8') + \
            bytes([0] * (EXT_LENGTH - len(self._file_ext)))

        # encrypt raw bytes and separate them from token
        encrypted_bytes = cypher_suite.encrypt(raw_bytes)
        token = encrypted_bytes[N_BYTES:]
        encrypted_bytes = encrypted_bytes[:N_BYTES]

        with open(file_path, 'r+b') as file:
            # set pointer to the start of file and write encrypted bytes
            file.seek(0)
            file.write(encrypted_bytes)
            # set pointer to the end of file and write token, key, extension and flag
            file.seek(0, 2)
            file.write(token)
            file.write(key)
            file.write(extension)
            file.write(FLAG)

        # change the extension
        os.rename(file_path, self._file_name + EXT_NEW)
        return 0

    def decrypt_file(self) -> int:
        self._file_name = self._path.stem
        self._file_ext = self._path.suffix
        with open(self._path, 'rb') as file:
            # load encrypted bytes
            encrypted_bytes = file.read(N_BYTES)
            # load token, key and original extension
            file.seek(-KEY_LENGTH - TOKEN_LENGTH - EXT_LENGTH - len(FLAG), 2)
            token = file.read(TOKEN_LENGTH)
            key = file.read(KEY_LENGTH)
            extension = file.read(EXT_LENGTH)

        # try to get key, decide if its already decrypted
        try:
            cypher_suite = Fernet(key)
        except:
            return -1

        # decrypt bytes
        decrypted_bytes = cypher_suite.decrypt(encrypted_bytes + token)

        with open(self._path, 'r+b') as file:
            # set pointer to the start of file and write decrypted bytes
            file.seek(0)
            file.write(decrypted_bytes)
            # remove token, key, extension and flag from file
            file.seek(-KEY_LENGTH - TOKEN_LENGTH - EXT_LENGTH - len(FLAG), 2)
            file.truncate()

        # change the extension back
        extension = extension.replace(b'\x00', b'')
        os.rename(self._path, self._file_name + extension.decode())
        return 0
