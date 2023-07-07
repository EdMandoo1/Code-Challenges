#!/usr/bin/env python3
# Script Name:                  Directory Creation
# Author:                       Eduardo Ayala
# Date of latest revision:      07/06/23
# Purpose:                      Generates all directories, sub-directories and files for a user-provided directory path.

# Import libraries
import os
import subprocess

# Declare function
def generate_directory_structure(path, output_file):
    with open(output_file, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(path):
            f.write("Directory: {}\n".format(dirpath))
            for dirname in dirnames:
                f.write("Subdirectory: {}\n".format(os.path.join(dirpath, dirname)))
            for filename in filenames:
                f.write("File: {}\n".format(os.path.join(dirpath, filename)))

# Read user input here into variable
user_path = input("Enter the directory path: ")
output_file = input("Enter the output file name (with .txt extension): ")


# Main
generate_directory_structure(user_path)
print("Directory structure saved to {}".format(output_file))

# Open the .txt file with LibreOffice Writer
subprocess.run(['libreoffice', '--writer', output_file])

# End