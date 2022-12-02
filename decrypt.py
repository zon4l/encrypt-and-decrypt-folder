import os
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
        # append file names to the list 'files'
        files.append(file)

# read encryption key from the key file
with open("encryption-key.key", "rb") as key_file:
    key = key_file.read()

# loop over file names saved to 'files' list
for file in files:
    # open files one by one and read contents
    with open(file, "rb") as decryption_file:
        contents = decryption_file.read()
    # decrypt file content
    decrypted_contents = Fernet(key).decrypt(contents)
    # read decrypted content to the file
    with open(file, "wb") as decryption_file:
        decryption_file.write(decrypted_contents)
