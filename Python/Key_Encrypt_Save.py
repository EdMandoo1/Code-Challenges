#!/usr/bin/python

from cryptography.fernet import Fernet
import os

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file (optional, can be used to keep the key for later decryption)
def save_key(key, filename="encryption_key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the encryption key from a file (optional, can be used to load the key for decryption)
def load_key(filename="encryption_key.key"):
    return open(filename, "rb").read()

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
    print("Encrypted message:", encrypted_message.decode())

# Decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    print("Decrypted message:", decrypted_message.decode())

def main():
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    key = generate_key()

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
            encrypt_message(message, key)
        elif mode == 4:
            decrypt_message(message, key)

if __name__ == "__main__":
    main()