import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if os.path.isfile(file) and file != "encrypt.py" and file != "encryption-key.key" and file != "decrypt.py":
        files.append(file)

with open("encryption-key.key", "rb") as key_file:
    key = key_file.read()

for file in files:
    with open(file, "rb") as decryption_file:
        contents = decryption_file.read()
    decrypted_contents = Fernet(key).decrypt(contents)
    with open(file, "wb") as decryption_file:
        decryption_file.write(decrypted_contents)
