#!/usr/bin/env python3
# Script Name:                  Auto Brute Force Wordlist attack tool
# Author:                       Eduardo Ayala
# Date of latest revision:      07/31/23
# Purpose:                      Automated Brute Force attack 

# Import libraries
import time
# Mode 1: Offensive; Dictionary Iterator
def offensive_mode():
 # Accepts a user input word list file path and iterates through the word list, 
 # assigning the word being read to a variable. 
    file_path = input("Enter the word list file path: ")
    try:
        with open(file_path, 'r') as file:
            for word in file:
                word = word.strip()
                print(word)
                time.sleep(1)  # Adjust the delay time (in seconds) as needed
    except FileNotFoundError:
        print("File not found.")
# Mode 2: Defensive; Password Recognized
def defensive_mode():
# Accepts a user input string.        
    input_string = input("Enter a string: ")
# Accepts a user input word list file path.   
    file_path = input("Enter the word list file path: ")
    try:
        with open(file_path, 'r') as file:
            word_list = [word.strip() for word in file]
           # Prints to the screen whether the string appeared in the word list.
            if input_string in word_list:
                print("Password recognized.")
            else:
                print("Password not recognized.")
    except FileNotFoundError:
        print("File not found.")
# Main - 
def main():
   # Prompts the user to select a mode: Offensive (Mode 1) or Defensive (Mode 2). 
    print("Select a mode:")
   #  If the user chooses Mode 1, it calls the offensive_mode function.
    print("1. Offensive; Dictionary Iterator")
   # If the user chooses Mode 2, it calls the defensive_mode function.
    print("2. Defensive; Password Recognized")
    
    mode = input("Enter the mode number (1 or 2): ")

    if mode == "1":
        offensive_mode()
    elif mode == "2":
        defensive_mode()
    else:
        print("Invalid mode number. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
