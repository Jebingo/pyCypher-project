# Cypher 🔐
CLI app that can encrypt or decrypt files.

It uses Fernet from cryptography library.

It only encrypts first 100 bytes of file and then it stores key and other information to the end of the file for decryption later.

**Disclaimer: This is a demo project. Exercise caution when encrypting your files.

### Install dependencies 📦
```
pip install -r requirements.txt
```

### Usage 🛠️
For information about usage use:
```
python cypher.py --help
```

---

#### TODO 📝
- let user specify extension of encrypted files
- safeguards
- threading
