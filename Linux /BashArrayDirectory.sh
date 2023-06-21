#!/bin/bash

# Script Name:                  Bash Array
# Author:                       Eduardo Ayala
# Date of latest revision:      04/27/2023
# Purpose:                      Create 4 directories and put in an array

# Declaration of variables
directory=("dir1.txt" "dir2.txt" "dir3.txt" "dir4.txt")
# Declaration of functions
mkdir ${directory(0)}
mkdir ${directory(1)}
mkdir ${directory(2)}
mkdir ${directory(3)}
echo "I hope this works"
# Creating text files in directories
touch dir(1).txt
touch dir(2).txt
touch dir(3).txt
tough dir(4).txt
echo "four text directories created"
# Main