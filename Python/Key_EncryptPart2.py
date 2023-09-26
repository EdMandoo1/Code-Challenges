#!/usr/bin/env python3
# Script Name:                  Part II of III Key Encryption
# Author:                       Eduardo Ayala
# Date of latest revision:      07/18/23
# Purpose:                      Recursive encrypt and decrypt folder

# Import Libraries
import os
from cryptography.fernet import Fernet

# Encrypt a file
def encrypt_file(filepath, key):
    with open(filepath, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Decrypt a file
def decrypt_file(filepath, key):
    with open(filepath, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filepath, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

# Encrypt files in a folder and its subfolders recursively
def encrypt_folder(path, key):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Decrypt files in a folder and its subfolders recursively
def decrypt_folder(path, key):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def main():
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder (recursive)\n6. Decrypt a folder (recursive)\n"))

    key = Fernet.generate_key()

    if mode == 1 or mode == 2:
        file_path = input("Enter the filepath: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        elif mode == 2:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        message = input("Enter the message: ")
        if mode == 3:
            encrypted_message = encrypt_message(message, key)
            print("Encrypted message:", encrypted_message.decode())
        elif mode == 4:
            decrypted_message = decrypt_message(message, key)
            print("Decrypted message:", decrypted_message)
    elif mode == 5:
        folder_path = input("Enter the folder path: ")
        encrypt_folder(folder_path, key)
        print("Folder and its contents encrypted successfully.")
    elif mode == 6:
        folder_path = input("Enter the folder path: ")
        decrypt_folder(folder_path, key)
        print("Folder and its contents decrypted successfully.")

if __name__ == "__main__":
    main()
