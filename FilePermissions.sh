#!/bin/bash

# Script Name:                  File Permissions    
# Author:                       Eduardo Ayala
# Date of latest revision:      06/01/2023
# Purpose:                      Alter file permissions of everything in a directory

# Prompt user for input directory path
read -p "Enter the input directory path:" input_path 

# Display the entered directory path
echo "You entered: $input_path"

# Change directory to the user specified path
cd "$input_path"

# Prompt user to enter permissions number
read -p "Enter the permissions_number:" permissions_number
echo "You entered: $permissions_number"

# Change permissions of all files in the directory
chmod "$permissions_number"

# List directory contents with new permissions settings
ls -l