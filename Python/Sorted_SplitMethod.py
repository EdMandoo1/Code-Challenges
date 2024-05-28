#!/usr/bin/env python3
# Script Name:                  Sorted_SplitMethod
# Author:                       Eduardo Ayala
# Date of latest revision:      05/26/24
# Purpose:        Reading the file, splitting each line into words, and then build list sorted in alphabetical order.

# Open the file romeo.txt in read mode
with open('C:\\Users\\ChosenOne\\Downloads\\romeo.txt', 'r') as file:
    words = set()  # Use a set to store unique words

    # Read the file line by line
    for line in file:
        # Split each line into words
        for word in line.split():
            words.add(word.lower())  # Add each word to the set in lowercase

# Convert the set to a list and sort it
sorted_words = sorted(words)

# Print the sorted list of words
print(sorted_words)
