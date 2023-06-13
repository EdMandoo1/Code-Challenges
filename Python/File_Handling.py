#!/usr/bin/env python3
# Script Name:                  File_Handling
# Author:                       Eduardo Ayala
# Date of latest revision:      06/12/23
# Purpose:                      Script to handle files

import os

# Define the file name and path
file_name = "test.txt"
file_path = "./" + file_name

# Create the file and append three lines
with open(file_path, "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Read the first line from the file and print it
with open(file_path, "r") as file:
    first_line = file.readline()
    print("First line:", first_line)

# Delete the file
os.remove(file_path)
print("File deleted.")